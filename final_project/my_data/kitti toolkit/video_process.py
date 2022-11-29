import cv2
import os
import numpy as np
# converting mov to mp4 in ubuntu
# ffmpeg -i input.mov -vcodec h264 -acodec mp2 output.mp4


def video2img(file: str, outputfile):
    capture = cv2.VideoCapture(file)
    
    frameNr = 0
    
    while (True):
    
        success, frame = capture.read()
    
        if success:
            cv2.imwrite(f'./{outputfile}/{str(frameNr).zfill(6)}.png', frame)
    
        else:
            break
    
        frameNr = frameNr+1
    
    capture.release()


def video2gray(file: str, outputfile, frequency=1, starting_second=0):
    # 
    capture = cv2.VideoCapture(file)
    starting_frame = starting_second * 30 # assuming camera is 30Hz
    counter = 0
    frameNr = 0
    output_path = os.path.join(outputfile, "grey")
    os.mkdir(output_path)
    while (True):
    
        success, frame = capture.read()
        
        if success:
            if (counter % frequency == 0) and (counter > starting_frame):
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                cv2.imwrite(f'{output_path}/{str(frameNr).zfill(6)}.png', frame)
                frameNr = frameNr +1
    
        else:
            break
    
        counter = counter+1
    
    capture.release()
    return output_path

def imageResize(input_dir:str, output_dir:str):
    file_list = os.listdir(input_dir)
    output_path = os.path.join(output_dir, "image_0") # KITTI format
    os.mkdir(output_path)
    # if len(os.listdir(output_dir)):
    #     raise Exception('The destination dir is not empty!')
    for i in file_list:
        img = cv2.imread(os.path.join(input_dir,i))
        resized_img = cv2.resize(img, (640, 480))
        cv2.imwrite(f'{output_path}/'+i, resized_img)
    return output_path

def video2grayResized(file: str, outputfile, frequency=1, starting_second=0):
    # 
    capture = cv2.VideoCapture(file)
    starting_frame = starting_second * 30 # assuming camera is 30Hz
    counter = 0
    frameNr = 0
    output_path = os.path.join(outputfile, "image_0")
    os.mkdir(output_path)
    while (True):
    
        success, frame = capture.read()
        
        if success:
            if (counter % frequency == 0) and (counter > starting_frame):
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                frame = cv2.resize(frame, (640, 480))
                cv2.imwrite(f'{output_path}/{str(frameNr).zfill(6)}.png', frame)
                frameNr = frameNr +1
    
        else:
            break
    
        counter = counter+1
    
    capture.release()
    return output_path

def generatePseudoTimeStamp(time_duration_second:int, input_dir:str, output_dir:str, frame_interval):
    file_list = os.listdir(output_dir)
    if 'times.txt' in file_list:
        raise Exception('There is a existing times.txt!')
    file_list_num = len(os.listdir(input_dir))
    print(f"there are {file_list_num} frames")
    timeStamp = np.arange(0, time_duration_second, frame_interval)
    np.savetxt(f'{output_dir}/times.txt', timeStamp)
    


if __name__ == "__main__":
    input_video = "../house3_60Hz/house3_1080_60Hz.mp4"
    out_dir = "../house3_60Hz"
    total_duration_second = 129
    starting_second = 0
    # sample_frequency = 3 # every 3 frames sample one -> 10Hz
    # sample_frequency = 15 # every 3 frames sample one -> 2Hz
    sample_frequency = 1 # every 1 frames sample one -> 30Hz
    camera_frequency = 60

    frame_interval = 1/(camera_frequency/sample_frequency) # e.g. freq15 -> 2 frames per second -> frame_interval is 0.5s
    process_duration = total_duration_second - starting_second
    # raw_frames_path = video2gray(input_video, out_dir, frequency=sample_frequency, starting_second=starting_second) # freq15 -> 2 frames per second
    # raw_frames_path = '/home/mingxi/ws/final_proj_5554/my_data/outdoor/grey'
    # resized_frames_path = imageResize(raw_frames_path, out_dir)
    # resized_frames_path = '/home/mingxi/ws/final_proj_5554/my_data/outdoor/image_0'
    resized_frames_path = video2grayResized(input_video, out_dir, frequency=sample_frequency, starting_second=starting_second)
    generatePseudoTimeStamp(process_duration, resized_frames_path, out_dir, frame_interval)
