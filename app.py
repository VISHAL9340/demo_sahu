import streamlit as st
import yt_dlp
import os
import time

st.title("📥 Instagram Reel Downloader")

link = st.text_input("📌 Enter Instagram Reel Link:")

DOWNLOAD_FOLDER = "downloads"
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

# 👇 FFmpeg ka correct path yahan define karein
FFMPEG_PATH = "C:/ffmpeg/bin/ffmpeg.exe"  # Windows ke liye
# FFMPEG_PATH = "/usr/bin/ffmpeg"  # Linux/Mac ke liye

if st.button("🚀 Download Reel"):
    if link:
        try:
            filename = f"reel_{int(time.time())}.mp4"
            filepath = os.path.join(DOWNLOAD_FOLDER, filename)

            ydl_opts = {
                'outtmpl': filepath,
                'format': 'bestvideo+bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4',
                }],
                'ffmpeg_location': FFMPEG_PATH,  # 👈 FFmpeg path set karein
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])

            with open(filepath, "rb") as file:
                st.download_button(label="📥 Click here to Download", data=file, file_name=filename, mime="video/mp4")

        except Exception as e:
            st.error(f"❌ Something went wrong: {e}")
    else:
        st.warning("⚠ Please enter a valid Instagram reel link.")
