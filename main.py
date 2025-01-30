import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2024-08-01-preview",
)

model = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

# Read system prompt from file
with open("system_prompt.txt", "r", encoding="utf-8") as f:
    system_prompt = f.read()

# Initialize conversation history with system message
messages = [{"role": "system", "content": system_prompt}]


def get_completion(messages):
    response = client.chat.completions.create(model=model, messages=messages)
    return response.choices[0].message.content


print("Japanese Language Learning Assistant")
print("----------------------------------------")
print("Ask about any Japanese word, phrase, or grammar point")
print("Press Ctrl+C to exit")
print("----------------------------------------")

try:
    while True:
        try:
            # Get user input
            user_input = input("You: ").strip()

            # Skip empty inputs
            if not user_input:
                print("Please enter a non-empty message.")
                continue

            # Add user message to history
            messages.append({"role": "user", "content": user_input})

            try:
                # Get AI response
                assistant_response = get_completion(messages)

                # Add assistant response to history
                messages.append({"role": "assistant", "content": assistant_response})

                # Print assistant response
                print("\nAssistant:", assistant_response, "\n")

            except Exception as e:
                print(f"\nError: {str(e)}")
                continue

        except EOFError:
            break
except KeyboardInterrupt:
    print("\nGoodbye!")
