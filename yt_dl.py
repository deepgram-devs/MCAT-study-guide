import youtube_dl

# Populate this list with the URLs of the videos you wish to download!
vids = [ 'https://www.youtube.com/watch?v=ss7Ap-6bFYw&list=PL1O_shUH1zgUDu-2PDyHfGui9MgaB87zb' ]


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    # change this to change the path you want your downloads to be located
    'outtmpl': './hour_audio.mp3',
    'verbose': True
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(vids)

