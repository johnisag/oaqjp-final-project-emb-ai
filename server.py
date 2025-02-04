''' Executing this function initiates the application of emotion
    detector to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import request, render_template, Flask
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_detector():
    """do the detection"""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract data
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    sadness = response['sadness']
    joy = response['joy']
    dominant_emotion = response['dominant_emotion']

    # Check if the label is None, indicating an error or invalid input
    if response['anger'] is None:
        return "Invalid text! Please try again!"
    # Return a formatted string
    response_str = f"For the given statement, the system response is 'anger': {anger}, \
    'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. \
    The dominant emotion is {dominant_emotion}"
    return response_str

@app.route("/")
def render_index_page():
    """landing page"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
