from moviepy import VideoFileClip, TextClip, CompositeVideoClip, concatenate_videoclips

def create_clip_with_text(video_path, text, text_duration, font_path="arial.ttf", font_size=70, color='white'):
    # Load the video clip
    clip = VideoFileClip(video_path)
    # Create a text overlay
    txt_clip = (TextClip(text=text, font=font_path, font_size=font_size, color=color)
                .with_duration(text_duration)
                .with_position('center'))
    # Overlay the text onto the video
    return CompositeVideoClip([clip, txt_clip])

# Define information for each clip
clip_info = [
    ("clip1.mp4", "Wonderful flower field", 5),
    ("clip2.mp4", "Spectacular mountains", 5),
    ("clip3.mp4", "Enchanting waterfall", 5)
]

# Create clips with text overlays
clips = [create_clip_with_text(video, text, duration) for video, text, duration in clip_info]

# Concatenate them into a single video
final_video = concatenate_videoclips(clips, method="compose")

# Export the resulting video
final_video.write_videofile("final_video.mp4")
