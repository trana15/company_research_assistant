
class AccountPlan:
    def __init__(self):
        self.sections = {
            "overview": "Not yet filled",
            "opportunities": "Not yet filled",
            "risks": "Not yet filled",
            "strategy": "Not yet filled",
        }

    def update_section(self, section, content):
        section = section.lower()
        if section in self.sections:
            self.sections[section] = content
        else:
            print("No such section exists.")

    def generate_plan(self):
        output = "\n---- ACCOUNT PLAN ----\n"
        for k, v in self.sections.items():
            output += f"\n{k.upper()}:\n{v}\n"
        return output
