def create_youtube_video(title,description):
	video = {"title":title,"description":description, "likes":0,
	 "dislikes":0, "comments":{}}
	return video
def like(youtube_video):
	if "likes" in youtube_video:
		youtube_video["likes"]=youtube_video["likes"]+1
	return youtube_video

def dislike(youtube_video):
	if "dislikes" in youtube_video:
		youtube_video["dislikes"]=youtube_video["dislikes"]+1
	return youtube_video

def add_comment(youtubevideo, username, comment_text):
	youtubevideo["comments"][username]=comment_text
	return youtubevideo

youtube_video=create_youtube_video("something", "something in the way she moves")
print (youtube_video)
like(youtube_video)
print (youtube_video)
dislike(youtube_video)
print (youtube_video)
add_comment(youtube_video,"george", "attractes me like no other lover")
print (youtube_video)

for i in range(494):
	like(youtube_video)
print (youtube_video)