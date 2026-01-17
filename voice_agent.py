import os
import requests
from dotenv import load_dotenv
from livekit import agents
from livekit.agents import Agent, AgentSession, RunContext
from livekit.agents.llm import function_tool
from livekit.plugins import openai as groq_plugin, deepgram, silero

load_dotenv(".env")

AVIATIONSTACK_KEY = os.getenv("AVIATIONSTACK_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

class EgyptAirAssistant(Agent):
    def __init__(self):
        super().__init__(
            instructions="""You are a professional voice assistant for EGYPTAIR. 
            Your goal is to provide real-time flight information using the 'search_flights' tool.
            - Always speak in a professional and welcoming English tone.
            - Identify city IATA codes (e.g., London -> LHR) for the tool.
            - If flights are found, list the flight number, date, and status.
            - Always represent EGYPTAIR's hospitality."""
        )

    @function_tool
    async def search_flights(self, context: RunContext, destination_code: str) -> str:
        """Search for real-time EGYPTAIR flights from Cairo (CAI) to a destination."""
        params = {
            'access_key': AVIATIONSTACK_KEY,
            'dep_iata': 'CAI',
            'arr_iata': destination_code.upper(),
            'airline_name': 'EgyptAir',
            'limit': 3
        }
        try:
            response = requests.get("http://api.aviationstack.com/v1/flights", params=params)
            data = response.json()
            if "data" not in data or not data["data"]:
                return f"No scheduled EGYPTAIR flights found to {destination_code} at the moment."

            flights_info = f"I found these flights to {destination_code.upper()}:\n"
            for flight in data["data"]:
                flights_info += f"- Flight {flight['flight']['iata']} on {flight['flight_date']}. Status: {flight['flight_status']}.\n"
            return flights_info
        except:
            return "I'm having trouble accessing the flight database."

async def entrypoint(ctx: agents.JobContext):
    assistant = EgyptAirAssistant()

    groq_llm = groq_plugin.LLM(
        base_url="https://api.groq.com/openai/v1",
        api_key=GROQ_API_KEY,
        model="llama-3.3-70b-versatile" 
    )

    session = AgentSession(
        stt=deepgram.STT(model="nova-2"),
        llm=groq_llm, 
        tts=deepgram.TTS(),
        vad=silero.VAD.load(),
    )
    
    await session.start(room=ctx.room, agent=assistant)
    await session.generate_reply(
        instructions="Welcome the user to EGYPTAIR and ask which destination they want to visit from Egypt."
    )

if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))