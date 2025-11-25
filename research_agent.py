
import random

class ResearchAgent:
    def respond(self, user_input):
        normal_responses = [
            "Sure, tell me more.",
            "Interesting, what else would you like to know?",
            "Okay! I'm listening.",
            "Got it. Continue...",
        ]
        if "research" in user_input.lower():
            return "I'll gather information from multiple sources and update you."
        return random.choice(normal_responses)
