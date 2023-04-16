import openai


person = "George Washington"

openai.api_key = "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"
# audio_file = open("gettysburg_address.mp3", "rb")
# transcript = openai.Audio.transcribe(file=audio_file, model="whisper-1", response_format="text")

context = (f"You are {person}")

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": 'hola buenos dias'},
        {"role": "user", "content": "$"}
  ]
)

print(response['choices'][0]['message']['content'])

