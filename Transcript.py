from youtube_transcript_api import YouTubeTranscriptApi


def write_trancscript_to_text(transcript):
	file = open("transcript.txt","w")
	file.write(transcript)
	file.close()
	return

def generate_transcript_from_video_id(video_id):
	transcript = ""
	data = YouTubeTranscriptApi.get_transcript(video_id)
	for chunk in data:
		transcript += chunk['text']+" "
	return transcript

def get_transcript():
	url = input("Enter Youtube Video Link: ")
	video_id = url.split("=")[1]
	
	transcript = generate_transcript_from_video_id(video_id)
	write_trancscript_to_text(transcript)
	return


	

