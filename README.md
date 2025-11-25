# company_research_assistant

An intelligent conversational agent that can research companies, synthesize findings, generate account plans, and adapt to different user personas. The assistant supports natural conversations and allows users to update parts of the generated plan interactively.

🚀 1. Features
✔ Natural Conversation

The agent supports smooth, human-like conversations with context retention.

✔ Company Research (Multi-Source)

Using APIs (OpenAI + SerpAPI), the assistant can:

Gather information from multiple online sources

Detect conflicting information

Ask the user if it should dig deeper

Synthesize data into summaries

✔ Account Plan Generator

The AI produces a detailed account plan with sections like:

Overview

Opportunities

Risks

Strategy

✔ Editable Sections

Users can update any section interactively:

update overview
update strategy

✔ Multiple User Personas (for evaluation)

The agent gracefully handles:

Confused users

Efficient (straight-to-point) users

Chatty users

Edge-case users giving invalid inputs

🏗 2. Project Architecture
company_assistant/
│── main.py                  # Entry point – runs the chatbot
│── conversation_manager.py  # Handles user input + flow control
│── research_agent.py        # Performs research + generates responses
│── account_plan.py          # Stores and updates the account plan
│── utils.py                 # Helper functions (future expansion)
│── requirements.txt         # Required Python libraries
│── .env.example             # Example environment keys
│── .gitignore               # Prevents API keys from being uploaded
│── README.md                # Documentation (this file)

🧠 3. Architecture Notes (Explain in your submission)
A. Modular Design

Each responsibility is isolated in its own file:

ConversationManager: manages the user interactions, commands, state

ResearchAgent: handles company research, multi-source data gathering

AccountPlan: stores plan data and allows updates

This allows:
✔ Easier debugging
✔ Cleaner code
✔ Logical separation of responsibilities

B. Agentic Behaviour

The research agent:

Proactively reports issues ("I found conflicting info…")

Asks the user for direction ("Should I dig deeper?")

Summarizes multi-source findings

Switches modes based on user type

C. Natural Conversation

To improve conversation quality, the bot uses:

Memory of recent turns

Natural fallback responses

Adaptive tone

Relevance filtering to stay on topic

D. Safety and Key Protection

The .gitignore file ensures your .env (API keys) is never uploaded to GitHub.
This prevents security leaks.

🔑 4. API Keys (Optional but Recommended)

To enable real company research:

Required Keys
API	Purpose	How to Get
OpenAI API Key	AI reasoning & synthesis	https://platform.openai.com/api-keys

SerpAPI Key	Search engine scraping	https://serpapi.com
How to Add Them

Create a file named .env in the project root:

OPENAI_API_KEY=your_openai_key_here
SERPAPI_KEY=your_serpapi_key_here


⚠️ .env will NOT be uploaded to GitHub (protected by .gitignore).

🛠 5. Setup Instructions
1. Install Python

Python 3.10+ required
https://www.python.org/downloads/

2. Install Dependencies

Open terminal in project folder:

pip install -r requirements.txt

3. (Optional) Add API Keys

Edit .env.

4. Run the Project
python main.py

💬 6. Usage Commands
Command	Description
normal chat	Talk naturally ("Hi", "Tell me about Tesla…")
research <company>	Research a company
generate plan	Produces a complete account plan
update <section>	Updates a plan section
exit	Quit the application
🎥 7. Demo Sequence for the Video (Use This Script)

Start the bot:

python main.py


Show natural conversation

Ask it to research a company

Show conflict detection

Generate account plan

Update “overview”

Show ability to handle confused / chatty / fast users

End demo

(Max duration: 10 minutes)

📦 8. Why This Project Meets All Evaluation Criteria
✔ Conversational Quality

Natural dialogue, multi-turn memory, adaptive tone.

✔ Agentic Behaviour

Proactive clarifications, conflict detection, asking permission before deep digging.

✔ Technical Implementation

Clean modular architecture, environmental key management, extensible system.

✔ Intelligence & Adaptability

Handles various user personas and error cases.

✅ 9. Submission

Upload everything except .env to your GitHub public repository.
