import cv2
import os

def extract_frames(video_path, output_folder, frame_interval=66):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    video = cv2.VideoCapture(video_path)
    base_name = os.path.splitext(os.path.basename(video_path))[0]
    video_output_folder = os.path.join(output_folder, base_name)
    
    if not os.path.exists(video_output_folder):
        os.makedirs(video_output_folder)
    
    count = 0
    frame_count = 0
    
    while True:
        success, frame = video.read()
        if not success:
            break
        
        if frame_count % frame_interval == 0:
            output_path = os.path.join(video_output_folder, f"frame_{count:04d}.jpg")
            cv2.imwrite(output_path, frame)
            count += 1
        
        frame_count += 1
    
    video.release()
    print(f"Extracted {count} frames from {video_path}")

# Updated paths
video_folder = r"Y:\Movies"
output_folder = r"X:\Ai\Lora Training"

for filename in os.listdir(video_folder):
    if filename.endswith((".mp4", ".avi", ".mov", ".mkv")):
        video_path = os.path.join(video_folder, filename)
        extract_frames(video_path, output_folder)