import boto3

polly_client = boto3.Session(
    aws_access_key_id="AKIA3DJJ5GR64YYH5XOM",                     
    aws_secret_access_key="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",
    region_name='us-west-2').client('polly')

response = polly_client.synthesize_speech(VoiceId='Amy',
                OutputFormat='mp3', 
                Text = "Greetings, sir. This is Jarvis, and I am pleased to report that your suit status is fully operational. All systems are functioning at optimal levels, and the suit is ready for deployment should you require it. Shall I provide you with a detailed breakdown of the suit's current capabilities, or is there anything else you require at this time, sir?",
                Engine = 'neural')

file = open('speech.mp3', 'wb')
file.write(response['AudioStream'].read())
file.close()
