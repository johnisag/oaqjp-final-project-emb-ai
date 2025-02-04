import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):
    # Define the URL for the emoton detection API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Parse the response from the API
    formatted_response = json.loads(response.text)

    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
        sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        joy = formatted_response['emotionPredictions'][0]['emotion']['joy']

        data = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness
        }

        # derived
        data['dominant_emotion'] = max(data, key = data.get)
        
    # If the response status code is 500, set label and score to None
    elif response.status_code == 400:
        data = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    return data