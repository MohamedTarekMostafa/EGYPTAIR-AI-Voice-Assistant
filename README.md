# ✈️ EGYPTAIR AI Voice Assistant: Reimagining Flight Booking with Groq & LiveKit

Welcome to the **EGYPTAIR Voice Assistant** – a cutting-edge, low-latency voice agent designed to transform how users find and book flights. This isn't just a chatbot; it’s a fully autonomous voice agent that "thinks" and "acts" in real-time to provide actual flight data using a sophisticated AI stack.

---

##  Why This Project Matters
Most voice assistants feel sluggish and robotic. This project solves that by leveraging **Groq’s ** for near-instant response times and **LiveKit’s real-time communication protocol**. The result? A natural, human-like conversation where the AI understands context and interacts with external APIs .

---

##  The Tech Stack 
I carefully selected these tools to balance speed, intelligence, and reliability:

* **Brain (LLM):** `Llama-3.3-70b` (via **Groq**) – For lightning-fast reasoning and intent detection.
* **Real-time Protocol:** **LiveKit Agents** – The backbone for handling voice streams and agent orchestration.
* **Ears (STT):** **Deepgram Nova-2** – High-accuracy speech-to-text to capture every word perfectly.
* **Voice (TTS):** **Deepgram** – For natural, professional English synthesis.
* **Awareness (VAD):** **Silero** – Advanced Voice Activity Detection to handle silence and interruptions.
* **Data Source:** **AviationStack API** – Real-time integration with global flight databases.

---

##  Key Features
* **Dynamic IATA Mapping:** The agent automatically converts natural city names (e.g., "London") into technical airport codes (LHR) to communicate with flight APIs.
* **Autonomous Tool Use:** Uses **Function Calling** to fetch live data from EGYPTAIR’s database without hardcoded responses.
* **Low-Latency Performance:** Optimized for under 1-second response times, making the conversation feel fluid.
* **Professional Persona:** Tailored instructions ensure the agent maintains EGYPTAIR’s brand hospitality.

---

##  Technical Challenges I Overcame
### 1. The Latency Gap
**Challenge:** Standard LLMs take 2-4 seconds to respond, which kills the flow of a voice conversation.
**Solution:** Migrated the entire logic to **Groq**, reducing inference time by over 70%.

### 2. API Schema Compatibility
**Challenge:** Connecting an OpenAI-based plugin to Groq's API while satisfying environmental variable requirements.
**Solution:** Implemented a custom LLM configuration that bridges the OpenAI interface with Groq's endpoint, ensuring seamless functionality without dependency conflicts.

### 3. Contextual Data Fetching
**Challenge:** Users don't speak in "airport codes," but APIs do.
**Solution:** Prompt-engineered the agent to act as a translator, silently mapping user geography to technical data points.

---

##  How to Run It
1.  **Clone the repo:** `git clone https://github.com/your-username/egyptair-voice-assistant.git`
2.  **Install dependencies:** `pip install livekit-agents livekit-plugins-openai livekit-plugins-deepgram livekit-plugins-silero python-dotenv requests`
3.  **Setup `.env`:**
    ```env
    LIVEKIT_URL=<your_url>
    LIVEKIT_API_KEY=<your_key>
    LIVEKIT_API_SECRET=<your_secret>
    GROQ_API_KEY=<your_groq_key>
    AVIATIONSTACK_API_KEY=<your_aviationstack_key>
    OPENAI_API_KEY=<your_groq_key_again> # To satisfy the plugin requirements
    ```
4.  **Run the agent:** `python voice_agent_project.py dev`

---

## Future Roadmap
* [ ] **Full Reservation Flow:** Adding a booking tool to collect passenger names and confirm seats.
* [ ] **Multilingual Support:** Enabling the agent to switch between Arabic and English seamlessly.
* [ ] **WhatsApp Integration:** Sending flight details via SMS/WhatsApp after the call.

---
