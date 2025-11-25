
from research_agent import ResearchAgent
from account_plan import AccountPlan

class ConversationManager:
    def __init__(self):
        self.agent = ResearchAgent()
        self.plan = AccountPlan()

    def chat_loop(self):
        print("Type 'exit' to stop.")
        while True:
            user = input("You: ").strip()
            if user.lower() == "exit":
                print("Bot: Goodbye!")
                break

            if "generate plan" in user.lower():
                print("Bot: Generating plan...")
                print(self.plan.generate_plan())
                continue

            if "update" in user.lower():
                sec = input("Which section? ").strip()
                val = input("New content: ").strip()
                self.plan.update_section(sec, val)
                print("Bot: Updated.")
                continue

            reply = self.agent.respond(user)
            print("Bot:", reply)
