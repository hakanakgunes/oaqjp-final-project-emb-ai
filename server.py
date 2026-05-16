"""
Flask server for emotion detection.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """
    Render function for the home page.
    """
    return render_template('index.html')

@app.route("/emotionDetector", methods=['GET'])
def emotion_detector_route():
    """
    Analyze the emotions according to the text.
    """
    text_to_analyze=request.args.get('textToAnalyze')
    if not text_to_analyze:
        return "Invalid text! Please provide text to analyze."
    emotion_dict=emotion_detector(text_to_analyze)
    dominant_emotion=emotion_dict.get('dominant_emotion')

    if not dominant_emotion:
        return "Invalid text! Please try again."
    response = (
        f"For the given statement, the system response is "
        f"'anger': {emotion_dict.get('anger')}, 'disgust': {emotion_dict.get('disgust')}, "
        f"'fear': {emotion_dict.get('fear')}, 'joy': {emotion_dict.get('joy')} and "
        f"'sadness': {emotion_dict.get('sadness')}. The dominant emotion is {dominant_emotion}."
    )
    return response
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
