import config
from groq import Groq

# Initialize the Groq client using the API key from config.py
#client = Groq(api_key=config.GROQ_API_KEY)
client = Groq(

api_key="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"

)

def get_ai_response(prompt_text: str) -> str:
  """Sends a prompt to the AI model and returns the output."""
  response = client.chat.completions.create(
      messages=[{"role": "user", "content": prompt_text}],
      model="llama3-8b-8192",
      temperature=0.7,
  )
  return response.choices[0].message.content


def main():
  # Define the three test prompts from the project assignment
  prompts = {
      "1. Vague Prompt": "Tell me about technology",
      "2. Specific Prompt": "Explain how AI works in self-driving cars",
      "3. Contextual Prompt": (
          "Given the advancements in autonomous vehicles, explain how AI is"
          " used in self-driving cars to make real-time driving decisions"
      ),
  }

  # Run each prompt and display the AI responses
  for label, prompt in prompts.items():
    print(f"\n{'='*20} {label} {'='*20}")
    print(f"Prompt: {prompt}\n")
    print("Response:")

    response = get_ai_response(prompt)
    print(response)
    print("-" * 50)


if __name__ == "__main__":
  main()