import cv2
import os

def extract_frames(video_path, output_folder, range):
    """
    Extracts frames from a video and saves them as individual images.

    Args:
        video_path (str): Path to the input video file.
        output_folder (str): Directory to save the extracted frames.
        range (tuple): (from,to) Image extraction range inclusive
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:  # No more frames to read
            break
        if frame_count<range[0]:
            continue
        elif frame_count>range[1]:
            break

        frame_filename = os.path.join(output_folder, f"frame_{frame_count}.jpg")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

    cap.release()
    print(f"Extracted {frame_count} frames to {output_folder}")

if __name__ == "__main__":
    video_file = "your_video.mp4"  # Replace with your video file path
    output_directory = "extracted_frames"

    extract_frames(video_file, output_directory)