from pytube import YouTube

youtube_url = input("Enter the url of the video you want to download: ")

video = YouTube(youtube_url)

print(video.title)

print(video.thumbnail_url)

print(video.views)

print(video.description)

video = video.streams.get_highest_resolution()

video.download()
