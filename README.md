# ChatCoach

Use ChatGPT to practice speaking 20+ languages in real-time conversations. Supports multiple language levels and switching languages mid-conversation (although you'll have to listen to the other language in a heavy accent—just like a real teacher!)

To run ChatCoach:

1. Clone this repository \
```git clone https://github.com/markov24/ChatCoach.git```

2. Open a terminal in the repository directory, and use pip to install dependencies listed in ```requirements.txt``` \
```pip install -r requirements.txt```

3. This website uses OpenAI and AWS Amazon Polly API keys. Create a ```config.py``` file, where you set the following variables \
```openAI_key = "YOUR_OPENAI_KEY" ``` \
```aws_access_key = "YOUR_AWS_ACCESS_KEY" ``` \
```aws_secret_access_key = "YOUR_AWS_SECRET_ACCESS_KEY" ```

4. Run the app with Flask \
```flask run```

5. Open up your browser to 127.0.0.1:5000 or localhost:5000

6. Enter your language and level, and click "Go"

7. Click "Record", say something, then "Stop" and "Upload"

8. Wait until your Chat Coach responds...

9. ChatCoach's response should play automatically. Continue chatting by recording and uploading a new message.
