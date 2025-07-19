"""
==========================================================
AI TRAVEL DESIGNER AGENT (CHAINLIT + GEMINI API)
==========================================================

✅ WHAT IT DOES:
- Suggests 3 destinations based on your mood.
- Picks the best one.
- Gives flight & hotel search terms (example-based).
- Lists top attractions & famous food.

==========================================================
1) PREREQUISITES (RUN THESE IN CMD ONE BY ONE)
==========================================================
# Check Python version (3.9 recommended)
python --version

# Install uv (fast package manager)
pip install uv

# Go to the folder where this file is saved
cd "D:\Agentic Ai\AI Travel Designer Agent"

# Install requirements using uv
uv pip install chainlit google-generativeai --system

# (If uv gives errors, use pip instead)
pip install chainlit google-generativeai

==========================================================
2) RUN THE AGENT
==========================================================
# Start Chainlit server
chainlit run ai_travel_designer_agent_complete.py -w

# Open the URL shown in the terminal, e.g.:
http://localhost:8000

==========================================================
3) HOW TO USE
==========================================================
Type your mood in the chat, for example:
- relaxing beach
- adventurous and exciting
- romantic and luxurious
- budget-friendly and exploring

You will get:
✔ 3 destinations
✔ Best one picked automatically
✔ Flight & hotel suggestions
✔ Attractions & famous food

==========================================================
4) IF PORT 8000 IS BUSY
==========================================================
chainlit run ai_travel_designer_agent_complete.py -w --port 8080

Then open:
http://localhost:8080

==========================================================
5) MAKE IT PUBLIC (OPTIONAL)
==========================================================
# Install localtunnel (Node.js required)
npm install -g localtunnel

# After running the agent
npx localtunnel --port 8000

You will get a public URL like:
https://cool-travel-agent.loca.lt

==========================================================
6) STOP THE SERVER
==========================================================
Press CTRL + C in terminal.

==========================================================


