import shutil
import cv2
import os



CWD = os.getcwd()
BASE_DIR = os.path.join(CWD,"resources","city")
vids = ["la_lower","shanghai"]

video_dir = os.path.join(BASE_DIR,"video","train")
img_output_dir = os.path.join(BASE_DIR,"preprocessed","images")
raw_data_dir = os.path.join(BASE_DIR,"raw-labels")
labels_output_dir = os.path.join(BASE_DIR,"preprocessed","labels")



def extract_frames(video_name, output_folder, ls, inds):
    """
    Extracts frames from a video and saves them as individual images.

    Args:
        video_name (str): Name of video file.
        output_folder (str): Directory to save the extracted frames.
        range (tuple): (from,to) Image extraction range inclusive
    """

    video_path = os.path.join(video_dir,video_name+".mp4")

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

        if frame_count in inds:
            base_file = ls[frame_count][6:-4]
            frame_filename = os.path.join(output_folder, f"{video_name}_{base_file}.jpg")
            cv2.imwrite(frame_filename, frame)

        #print(f"Extracted frame# {frame_count} to {output_folder}")
        frame_count += 1

    cap.release()

def copy_label(video_name, output_folder, ls, inds):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    #go thru list of given filenames (frame_123456.jpg) and copy them and rename them
    for ind in inds:
        base_file = ls[ind][6:-4]
        from_f = os.path.join(raw_data_dir, video_name,"obj_train_data", ls[ind])
        shutil.copy(from_f,output_folder)

        os.rename(os.path.join(output_folder, ls[ind]), os.path.join(output_folder, f"{video_name}_{base_file}.txt"))



for vid in vids:
    # process labels first to get the ones with actual content (and the images with actual labels)
    targets = []
    data = os.path.join(raw_data_dir,vid,"obj_train_data")
    labels = os.listdir(data)

    for i in range(len(labels)):
        with open(os.path.join(data,labels[i])) as f:
            if len(f.readlines())!=0:
                targets.append(i)

    print(targets)

    true_frames = sorted([int(labels[i][6:-4]) for i in targets])

    print(true_frames)

    extract_frames(vid,os.path.join(img_output_dir,vid),labels,true_frames)
    copy_label(vid,os.path.join(labels_output_dir,vid),labels,targets)