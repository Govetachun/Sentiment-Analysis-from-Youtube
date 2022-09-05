import json
from yt_extracion import get_audio_url,get_video_infos
from api_communication import save_transcript

def save_video_sentiments(url):
    video_infos = get_video_infos(url)
    audio_url = get_audio_url(video_infos)
    filename = video_infos["title"]
    filename = filename.strip().replace(" ","_")
    filename = "data/"  +filename
    save_transcript(audio_url, filename,sentiment_analysis = True)
    
if __name__ =="__main__":
    # save_video_sentiments("https://www.youtube.com/watch?v=cJuVfTG_iOY")
    with open("data/A_Day_In_The_Life_Of_Tim_Cook_(Apple's_CEO)_sentiments.json", "r") as f:
        data = json.load(f)
    
    positives = []
    negatives = []
    neutrals = []
    for result in data:
        text = result["text"]
        if result["sentiment"] == "POSITIVE":
            positives.append(text)
        elif result["sentiment"] == "NEGATIVE":
            negatives.append(text)
        else:
            neutrals.append(text)
        
    n_pos = len(positives)
    n_neg  = len(negatives)
    n_neut = len(neutrals)

    print("Num positives:", n_pos)
    print("Num negatives:", n_neg)
    print("Num neutrals:", n_neut)

    # ignore neutrals here
    r = n_pos / (n_pos + n_neg)
    print(f"Positive ratio: {r:.3f}")