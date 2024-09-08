import boxmot
import cv2
from ultralytics import YOLO
import numpy as np
from pathlib import Path
import os

class TrackObjectBoxMot:

    def __init__(self,tracker_type=None,objects=None,reid_wt_path=None,display=False):
        if tracker_type == None:
            tracker_type = 'botsort'
        if reid_wt_path==None:
            reid_wt_path = Path('.\weights\osnet_ain_x1_0_msmt17.pth')
        self.detector = YOLO('yolov10s.pt')
        self.tracker = boxmot.create_tracker(tracker_type=tracker_type,tracker_config=boxmot.get_tracker_config(tracker_type),
                                             reid_weights=reid_wt_path)
        self.classes_ids = []
        if objects == None:
            self.classes_ids = list(self.detector.names.keys())
        else:
            keys = list(self.detector.names.keys())
            values = list(self.detector.names.values())
            self.classes = list(objects.split(','))
            for cl in self.classes:
                if cl in values:
                    index = values.index(cl)
                    self.classes_ids.append(keys[index])
        
        self.object_history = {}
        self.display = display

    def generate_random_color(self):
        return (np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,255))

    def update_library(self,results):
        for result in results:
            track_id = result[4]
            if track_id in self.object_history.keys():
                    self.object_history[track_id]['position'].append(result[:5])
            else:
                self.object_history[track_id] = {
                    'position' : [result[:4]],
                    'color' : self.generate_random_color(),
                    'class' : result[6]
                }

    def track(self,video_path,save_path=None):
        video = cv2.VideoCapture(video_path)
        if save_path==None:
            save_path = "./output.mp4"
        width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(video.get(cv2.CAP_PROP_FPS)) 
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Replace 'mp4v' with your desired codec
        videoout = cv2.VideoWriter(Path(save_path), fourcc, fps, (width, height))
        while True:
            ret,frame = video.read()
            if not ret:
                break
            detections = self.detector(frame)
            dets = []
            for detection in detections:
                for det in detection.boxes.data.cpu().numpy():
                    x1,y1,x2,y2,conf, cls =  det
                    if cls in self.classes_ids:
                        dets.append([x1,y1,x2,y2,conf,int(cls)])
            print("Detected Objects: ")
            print(dets)
            print('Tracking Objects :')
            dets = np.array(dets)
            if len(dets)>0:
                results = self.tracker.update(dets,frame)
                self.update_library(results)
                for result in results:
                    print(result)
                    x1 = int(result[0])
                    y1 = int(result[1])
                    x2 = int(result[2])
                    y2 = int(result[3])
                    track_id = int(result[4])
                    conf = float(format(result[5],'.2f'))
                    cv2.rectangle(frame,(x1,y1),(x2,y2),self.object_history[track_id]['color'])
                    cv2.putText(frame,f"Id:{track_id}",(x1,y1+5),1,1,(0,255,0))
            if self.display:
                cv2.imshow('frame',frame)
            videoout.write(frame)
        cv2.destroyAllWindows()
        videoout.release()
        video.release()
        return save_path

                    
                        


