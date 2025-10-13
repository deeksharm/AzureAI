import os
import openai

def main():
    openai.api_key = "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"

    if not openai.api_key:
        print("Please set your OPENAI_API_KEY environment variable.")
        return

    print("Chatbot is ready! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        try:
            response = openai.chat.completions.create(
                model="gpt-4o-mini",  # or your preferred model
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ],
                max_tokens=150,
                temperature=0.7,
            )
            answer = response.choices[0].message.content.strip()
            print("Bot:", answer)

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
