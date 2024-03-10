from pytube import YouTube

def Download(link):
  youtubeObject = YouTube(link)
  print(youtubeObject.title)
  print(youtubeObject.metadata)
  print(youtubeObject.channel_url)
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  try:
    # youtubeObject.download()
    print('something')
  except:
    print('An error has occurred')
  print('download is completed successfully')


link = input('Please enter your link: ')
print(link)
Download(link)