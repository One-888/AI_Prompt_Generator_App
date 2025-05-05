
import pyperclip
import webbrowser
import time
import pyautogui


class PromptGenerator:
    """
    A class for generating AI prompts based on user input.
    It allows users to select predefined purposes and target audiences.
    """

    def __init__(self):
        self.purpose_dict = {
            "1": "Generate an effective prompt in monospace ",
            "2": "Explain a concept in simple terms",
            "3": "Draft an email in monospace ",
            "4": "Enhance code readability with inline and header (block) comments; No change in the code yet",
            "5": "List top 10 stock tickers (excluding ETFs) in one line CSV",
            "6": "Explain a given code snippet",
            "7": "Generate an ASCII chart",
            "8": "Write one line in monospace; correct grammar, punctuation, and spelling without changing the meaning or structure of the text; remove 'Using the best practice'",
            "9": "Correct grammar, punctuation, and spelling, style, and vocabulary",
            "10": "Review and improve code using 'Code Complete 2'; Showing the suggestions but not change yet;",
            "11": "Summarize a passage into three bullet points",
            "12": "Evaluate companies using the 'CAN SLIM' methodology",
            "13": "Analyze and suggest as an financial advisor",
            "14": "Generate a concise Git commit message",
            "15": "Develop a Python-based application",
            "16": "Create a structured chain of prompts and hold the combined result",
            "17": "Write a user manual",
        }

        self.audience_dict = {
            "1": "General Public",
            "2": "Primary School Students",
            "3": "Pittburgh Water Coworkers",
            "4": "Undergraduate Students",
            "5": "Graduate Students",
            "6": "Non-Technical Users",
            "7": "Doctoral Candidates",
            "8": "Technical or Professional Users",
            "9": "Middle School Students",
            "10": "Both Middle School and Graduate Students",
            "11": "ECS Middle School Teachers",
            "12": "My boss or my manager",
        }

        self.purpose = None
        self.audience = None
        self.details = None

    def display_options(self, options_dict, label):
        """Displays available options for user selection."""
        print(f"Available {label}:")
        for number, option in options_dict.items():
            print(f"{number}. {option}")

    def ask_questions(self):
        """Collects user input for prompt generation."""
        print()
        print(
            "====================== Welcome to the AI Prompt Generator App! =================================="
        )
        print("Choose a purpose from the list below:")
        self.display_options(self.purpose_dict, "Purposes")

        purpose_choice = input("\nEnter the number corresponding to your choice: ")
        self.purpose = self.purpose_dict.get(
            purpose_choice, "Generate a general prompt "
        )
        print()
        print(
            "================================================================================================="
        )

        print("\nChoose an audience from the list below:")
        self.display_options(self.audience_dict, "Audiences")
        audience_choice = input(
            "\nEnter the number corresponding to your choice (or press Enter for General Public): "
        )

        self.audience = self.audience_dict.get(
            audience_choice, "General Public"
        )  # Defaults to 'General Public' if blank or invalid
        print()
        print(
            "================================================================================================="
        )
        self.details = input(
            "\nProvide additional details (e.g., topic, tone, length): "
        ).strip()
        print()
        print(
            "================================================================================================="
        )

        # Set default details if user does not provide input
        if not self.details:
            self.details = "The following prompts are the chaing prompts. Hold the combined answer until I say ok. "

    def display_results(self):
        """Displays user selections."""
        print("\n--- User Input Summary ---")
        print(f"1. Purpose: {self.purpose}")
        print(f"2. Audience: {self.audience}")
        print(f"3. Additional Details: {self.details}")

    def generate_prompt(self):
        """Generates a tailored prompt based on user input."""
        if (
            not self.purpose
            or self.purpose
            == "Invalid choice. Please restart and select a valid option."
        ):
            return "Error: Missing or invalid purpose. Please restart the application."

        return f"Purpose: {self.purpose}; Audience: {self.audience}; Additional Details: Using the best practice, {self.details}; "

    def copy_to_clipboard(self, text):
        """Copies the generated prompt to the clipboard."""
        pyperclip.copy(text)
        # print("\nThe generated prompt has been copied to the clipboard.")

    def open_website_and_automate(self, url, text):
        """Opens a specified website, pastes text into a textbox, and simulates pressing Enter."""
        webbrowser.open(url)
        time.sleep(1)  # Adjusted wait time for page loading
        """Closes all tabs before opening a website, pastes text into a textbox, and simulates pressing Enter."""
        for _ in range(10):  # Close tabs 10 times before proceeding
            pyautogui.hotkey("ctrl", "w")
            time.sleep(0.1)  # Small delay to ensure the action is registered
        webbrowser.open(url)
        # print(f"\nOpening website: {url}")
        time.sleep(2)  # Adjusted wait time for page loading

        pyautogui.typewrite(text)  # Paste the text
        pyautogui.press("enter")  # Simulate pressing Enter
        # print("\nText pasted and Enter key pressed.")

    def run(self):
        """Orchestrates the main workflow of the application."""
        self.ask_questions()
        if self.purpose != "Invalid choice. Please restart and select a valid option.":
            self.display_results()
            generated_prompt = self.generate_prompt()
            print("\n--- Generated AI Prompt ---")
            print(generated_prompt)
            self.copy_to_clipboard(generated_prompt)
            self.open_website_and_automate(
                "http://copilot.microsoft.com", generated_prompt
            )
            print()


if __name__ == "__main__":
    while True:
        app = PromptGenerator()
        app.run()
