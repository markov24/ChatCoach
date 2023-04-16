import boto3
import time
import os

def TTS(text, language):
    language_to_engine = {"Arabic":"Zeina",
                        "Chinese":"Zhiyu",
                        "Danish":"Naja",
                        "Dutch":"Lotte",
                        "English":"Salli",
                        "French":"Léa",
                        "German":"Hans",
                        "Hindi":"Aditi",
                        "Icelandic":"Karl",
                        "Italian":"Giorgo",
                        "Japanese":"Mizuki",
                        "Korean":"Seoyeon",
                        "Norwegian":"Liv",
                        "Polish":"Ewa",
                        "Portuguese":"Cristiano",
                        "Romanian":"Carmen",
                        "Russian":"Tatyana",
                        "Spanish":"Miguel",
                        "Swedish":"Astrid",
                        "Turkish":"Filiz",
                        }

    polly_client = boto3.Session(
        aws_access_key_id="AKIA3DJJ5GR64YYH5XOM",                     
        aws_secret_access_key="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",
        region_name='us-west-2').client('polly')
    
    model = language_to_engine[language]
        
    response = polly_client.synthesize_speech(VoiceId=model,
                    OutputFormat='mp3', 
                    Text = text,
                    Engine = 'standard')

    # os.remove('static/speech.mp3')
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    file_name = "speech" + current_time + ".mp3"
    file = open("static/"+file_name, 'wb')
    file.write(response['AudioStream'].read())
    file.close()

    return file_name
