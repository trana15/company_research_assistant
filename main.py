
from conversation_manager import ConversationManager

def main():
    print("🤖 Company Research Assistant Started!")
    bot = ConversationManager()
    bot.chat_loop()

if __name__ == "__main__":
    main()
