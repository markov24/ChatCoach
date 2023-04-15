import openai
import os

openai.api_key = os.environ['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']
prompt = "Respond to me as if you are Snoop Dog"

response = openai.Completion.create(
    engine="gpt-3",
    prompt=prompt,
    max_tokens=50,
)

# Print the generated text
print(response.choices[0].text)