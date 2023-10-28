from flask import Flask, request
from flask_cors import CORS
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline


app = Flask(__name__)
CORS(app, resources={r"/summary": {"origins": "http://localhost:5501"}})
CORS(app, resources={r"/summary/*": {"origins": "http://localhost:5000"}})  # Adjust the route and origin as needed

@app.get('/summary')
def summary_api():
    url = request.args.get('url', '')
    video_id = url.split('=')[1]
    transcript = get_transcript(video_id);
    return transcript,200;
    # initial task was to get summery of this text
    # summary = get_summary(get_transcript(video_id))
    # return summary, 200

def get_transcript(video_id):
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    transcript = ' '.join([d['text'] for d in transcript_list])
    return transcript

# def get_summary(transcript):
#     summariser = pipeline('summarization')
#     summary = ''
#     for i in range(0, (len(transcript)//1000)+1):
#         summary_text = summariser(transcript[i*1000:(i+1)*1000])[0]['summary_text']
#         summary = summary + summary_text + ' '
#     return summary
    

if __name__ == '__main__':
    app.run(host='0.0.0.0')  # Ensure Flask runs on port 5001