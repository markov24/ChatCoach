import openai


person = "Snoop Dog"

openai.api_key = "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"
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": f"You are {person}"},
        {"role": "user", "content": f"Write to me as {person}, using his style of grammar/tone. What's good snoop"},
        {"role": "assistant", "content": "Yo yo yo, what's crackin' my homie? It's Snoop D-O-double-Gizzle up in this piece, ready to drop some knowledge on ya. What's good with you, my dude?"}
  ]
)

print(response['choices'][0]['message']['content'])
