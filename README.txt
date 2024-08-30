This is a simple windows script built to extract individual images from movie files and save the individual images in a chosen folder.
 
1) Set the folder that includes the video files you want to extract images from, and the folder you want to export the images to in the following line in the text file:

# Updated paths
video_folder = r"Y:\Movies"
output_folder = r"X:\Exports"

(your file directories will differ)

Supports .avi, .mp4, .mov, and .mkv formats. Subfolders will be included.

* Ensure that you will have enough space on the drive (image extraction will take about a significant amount of time and space depending on the number of images you want to extract).

3) Adjust the frame interval setting, it can be customized to extract every frame (probably overkill -- but your choice) or every n-th frame (10th, 24th etc.) You can adjust this depending on your needs by editing the number of the frame interval in the first function:

def extract_frames(video_path, output_folder, frame_interval=66). 

(66 frames at 24 fps = ~2.5 seconds; you can replace 66 with your preferred interval)

3) Once the above settings are set, you can run the script by 

Install Python and dependencies: 

1. Python Installation
If you don't have Python installed, download and install it from the official Python website (https://www.python.org/downloads/). Make sure to add Python to your system's PATH during installation.
2. Install Required Libraries
This script requires the OpenCV library.

Open a command prompt or terminal and run:

pip install opencv-python

3. Save the Script
Copy the entire script you provided and save it to a file with a .py extension, for example, extract_frames.py.
4. Run the Script
Open a command prompt or terminal, navigate to the directory where you saved the script, and run:

python extract_frames.py

Additional Notes:

Make sure the paths in the script are correct:
video_folder = r"Y:\Movies" should point to the folder containing your video files.
output_folder = r"X:\Ai\Lora Training" should point to where you want to save the extracted frames.
The script will process all video files with the extensions .mp4, .avi, .mov, and .mkv in the specified video folder.
It will create a new folder for each video in the output folder, named after the video file.
Frames are extracted every 66 frames (adjustable by changing the frame_interval parameter in the extract_frames function).
If you encounter any permission errors, make sure you have write access to the output folder.
For large videos or many videos, this script may take a while to run and could use significant disk space for the extracted frames.

4) Please let me know if you run into any issues and I will try my best to help.
