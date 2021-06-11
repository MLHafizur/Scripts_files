import cv2
video_path = r"/media/usman-pc/New Volume/Home_Survillence_Data/sur_4.mp4"
OUT_PATH = r"/media/usman-pc/New Volume/Home_Survillence_Data/sur_4/sur_4_"

vidcap = cv2.VideoCapture(video_path)
VIDEO_LENGTH = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

print(VIDEO_LENGTH)

def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite(OUT_PATH + str(count).zfill(len(str(VIDEO_LENGTH))) +".jpg", image)     
    return hasFrames

sec = 0
frameRate = 0.25
count=0
success = getFrame(sec)

while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
