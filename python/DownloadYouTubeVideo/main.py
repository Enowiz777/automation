from pytube import YouTube  
import pytube


try:
    youtube_link = input("Enter the URL of the YouTube video:")
    youtube = pytube.YouTube(str(youtube_link))
    
    video = youtube.streams.first()  
    video.download('C:/Users/enoch/Desktop/')  
    print("Download Successfull !!")
except:
    print("Something Went Wrong !!")