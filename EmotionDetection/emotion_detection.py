import requests
import json

def emotion_detector(text_to_analyze):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myObj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=myObj, headers=header)
    if response.status_code == 400:
        return {
            "anger": None, 
            "disgust":  None, 
            "fear":  None, 
            "joy":  None, 
            "sadness":  None, 
            "dominant_emotion": None
            }
    formatted_response = json.loads(response.text)
    predictions = formatted_response.get('emotionPredictions', [])

    if predictions:
        emotion_dict = predictions[0]["emotion"]
        emotion_dict["dominant_emotion"] = max(emotion_dict, key=emotion_dict.get)
    else:
        emotion_dict = {}    

    return emotion_dict