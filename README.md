#  EGYPTAIR AI Voice Assistant: The Pipeline Foundation (V1)

> ** NEW: I have evolved this project!** > Experience the next generation with **10x lower latency** and **Native Audio Intelligence** in the new **Realtime API Version**.
> #### 👉 [Check out the Realtime API Version here](https://github.com/MohamedTarekMostafa/Realtime-AI-Voice-Assistance)

---

## 📺 The Pipeline in Action


https://github.com/user-attachments/assets/d479907b-22f3-45a6-a2ae-786687f943cf


---

##  Project Overview
"This project was my first deep dive into reinventing the travel experience. I wanted to see if I could build a voice concierge for EGYPTAIR that felt less like a computer and more like a real person. I started with a Sequential Pipeline (linking speech, logic, and voice) to push the boundaries of how AI handles complex, real-world tasks like fetching live flight data on the fly."
### Why This Project Matters
Most voice assistants feel sluggish. This project solved that by leveraging **Groq’s LPU inference** for near-instant reasoning and **LiveKit’s real-time communication protocol**. 

---

##  The Tech Stack (V1 Architecture)
I carefully selected these tools to balance speed and reliability in a pipeline setup:

* **Brain (LLM):** `Llama-3.3-70b` (via **Groq**) – For lightning-fast reasoning and intent detection.
* **Real-time Protocol:** **LiveKit Agents** – Orchestrating voice streams.
* **Ears (STT):** **Deepgram Nova-2** – High-accuracy speech-to-text.
* **Voice (TTS):** **Deepgram** – Natural English synthesis.
* **Data Source:** **AviationStack API** – Real-time integration with global flight databases.

---

##  Key Features & Challenges
* **Dynamic IATA Mapping:** Converts natural city names (e.g., "London") into technical codes (LHR) on the fly.
* **Autonomous Tool Use:** Uses **Function Calling** to fetch live data without hardcoded responses.
* **The Latency Gap:** Migrated to Groq to reduce inference time by 70%, achieving under 1-second response times for the pipeline.

---

##  The Evolution to Realtime API
While this V1 Pipeline is highly optimized, it led me to explore the **Native Multimodal** approach. In the [newest version](https://github.com/MohamedTarekMostafa/Realtime-AI-Voice-Assistance), I moved away from separate STT/TTS models to **Gemini's Realtime API**, which allows the AI to "hear" and "speak" natively, eliminating the pipeline overhead entirely.

---

## 💻 How to Run (V1)
1. **Clone the repo:** `git clone https://github.com/MohamedTarekMostafa/EGYPTAIR-AI-Voice-Assistant`
2. **Install dependencies:** `pip install livekit-agents livekit-plugins-openai livekit-plugins-deepgram livekit-plugins-silero python-dotenv requests`
3. **Run the agent:** `python voice_agent_project.py dev`

---
*This project was the essential foundation for my journey into high-performance AI Voice Agents.*
