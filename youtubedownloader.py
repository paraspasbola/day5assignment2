# YouTube Video Downloader:



from pytube import YouTube

video = YouTube(input("Enter the link of that video : "))

print(video.title)

print(video.thumbnail_url)

streams = video.streams

for stream in streams:
    print(stream)

stream = video.streams.get_by_itag(
    input("Enter the itag number you see below for the preferred quality : "))


file_size = stream.filesize

print(round(file_size/(1024*1024)), " MB")

print("Download Started ....... wait for a while....")


print("Download Successfully Compledted !")


 # to make this program work make sure pytube package is installed on your device
 # to install pytube write this command in terinal...... pip install pytube