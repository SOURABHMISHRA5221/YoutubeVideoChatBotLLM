from youtube_transcript_api import YouTubeTranscriptApi


def generate_transcript_from_video_id(video_id):
	transcript = ""
	data = YouTubeTranscriptApi.get_transcript(video_id)
	for chunk in data:
		transcript += chunk['text']+" "
	return transcript

def chat_bot():
	url = input("Enter Youtube Video Link: ")
	video_id = url.split("=")[1]
	
	transcript = generate_transcript_from_video_id(video_id)
	pass

if __name__ == "__main__":
	chat_bot()