import cv2
from PyQt5 import QtCore
import qimage2ndarray
import pyautogui
import numpy as np
NoneType = type(None)

# from async_timer import AsyncTimer



class VideoStream:
    camera_capture = None
    frame_for_record = None
    frame_for_image = None
    image = None
    width = 1920
    height = 1080

    recording_screen = True

    devices_list = ['Экран']
    
    def __init__(self, fps):
        self.fps = fps
        self.frame_timer = QtCore.QTimer()

        self.update_devices_list()
        
        # if self.recording_screen:
        #     self.frame_timer = AsyncTimer(self.display_screen_stream)
        # else:
        #     self.frame_timer = AsyncTimer(self.display_video_stream)
        self.setup_camera()
    
    def setup_camera(self):
        if self.recording_screen:
            self.frame_timer.timeout.connect(self.display_screen_stream)
        else:
            self.frame_timer.timeout.connect(self.display_video_stream)
    
    def update_devices_list(self):
        arr = []

        cap = cv2.VideoCapture(cv2.CAP_DSHOW)

        if cap.read()[0]:
            arr.append(cv2.CAP_DSHOW)
            cap.release()
        
        index = 1
        while index <= 5:
            cap = cv2.VideoCapture(index)

            if cap.read()[0]:
                arr.append(index)
                cap.release()

            index += 1

        self.devices_list = [self.devices_list[0]] + arr
    
    def change_videostream(self, index):
        if 0 <= index < len(self.devices_list):
            if index == 0:
                if not self.recording_screen:
                    self.camera_capture.release()
                    self.camera_capture = None
                    self.recording_screen = True
                    # self.frame_timer.stop()
                    # self.frame_timer = AsyncTimer(self.display_screen_stream)
                    # self.frame_timer.start(1 / self.fps)
                    self.frame_timer.timeout.connect(self.display_screen_stream)
            else:
                if not self.recording_screen:
                    self.camera_capture.release()

                self.camera_capture = cv2.VideoCapture(self.devices_list[index])
                self.camera_capture.set(3, self.width)
                self.camera_capture.set(4, self.height)
                self.camera_capture.set(5, self.fps)
                
                self.recording_screen = False
                # self.frame_timer.stop()
                # self.frame_timer = AsyncTimer(self.display_video_stream)
                # self.frame_timer.start(1 / self.fps)
                self.frame_timer.timeout.connect(self.display_video_stream)
    
    def display_video_stream(self):
        if self.recording_screen:
            return False
        
        ret, tmp_frame = self.camera_capture.read()

        if not ret:
            return False
        
        tmp_frame = cv2.flip(tmp_frame, 1)
        
        self.frame_for_record = tmp_frame
        self.frame_for_image = cv2.cvtColor(tmp_frame, cv2.COLOR_BGR2RGB)
        
        return True
    
    def display_screen_stream(self):
        if not self.recording_screen:
            return False
        
        self.frame_for_image = np.array(pyautogui.screenshot())
        self.frame_for_record = cv2.cvtColor(self.frame_for_image, cv2.COLOR_BGR2RGB)

        return True

    def run(self, fps = None):
        if fps:
            self.fps = fps
            
            if not isinstance(self.camera_capture, NoneType):
                self.camera_capture.set(5, self.fps)
        
        # self.frame_timer.start(1 / self.fps)
        self.frame_timer.start(int(1000 // self.fps))
    
    def stop(self):
        self.frame_timer.stop()

        if not isinstance(self.camera_capture, NoneType):
            self.camera_capture.release()
    
    def get_image(self, width, height):
        if not isinstance(self.frame_for_image, NoneType):
            tmp_frame = cv2.resize(self.frame_for_image, (width, height), interpolation = cv2.INTER_AREA)
            
            self.image = qimage2ndarray.array2qimage(tmp_frame)

        return self.image
    
    def get_frame(self, width, height):
        if not isinstance(self.frame_for_record, NoneType):
        
            return cv2.resize(self.frame_for_record, (width, height), interpolation = cv2.INTER_AREA)
            
        return self.frame_for_record
    
    def get_fps(self):
        return self.fps
    
    def get_devices_list(self):
        return self.devices_list
