from youtube_transcript_api import YouTubeTranscriptApi

def get_subtitles(url):
    id= url.split("=")[-1]
    print(id)
    transcript = YouTubeTranscriptApi.get_transcript(id)
    script = " "
    for text in transcript:
        t = text["text"]
        if t !='[Music]':
            script += t + " "

    return script        

