import cv2
from PyQt5 import QtCore
from threading import Thread
import time
import pyaudio
import wave

from async_timer import AsyncTimer



WAITING_BETWEEN_FRAME_READS_COEF_SCREEN = 0.05
WAITING_BETWEEN_FRAME_READS_COEF_CAMERA = 0.55
VIDEO_PART_LENGTH_IN_SEC = 10 * 60
SAVE_CHECKS_COUNT = 200



class VideoRecorder(QtCore.QObject):
    recording = False
    video_processing = False
    recording_screen = True
    waiting_between_frame_reads_coef = WAITING_BETWEEN_FRAME_READS_COEF_SCREEN
    cur_file_part_index = 1
    begin_audio_part_index = 0
    end_audio_part_index = 0
    
    end_rendering = QtCore.pyqtSignal()

    def __init__(self, video_stream):
        super().__init__()
        self.video_stream = video_stream
        self.video_size = (1920, 1080)
    
    def prepare_video_recording(self):
        self.fourcc = cv2.VideoWriter_fourcc(*'X264')
        self.ofstream = cv2.VideoWriter(self.filename + '.mp4', self.fourcc, self.video_stream.get_fps(), self.video_size)
        
        self.frame_timer = AsyncTimer(self.record_video)
        # self.frame_timer = QtCore.QTimer()
        # self.frame_timer.timeout.connect(self.record_video)
    
    def start_video_recording(self):
        self.frame_timer.start(1 / self.video_stream.get_fps() * self.waiting_between_frame_reads_coef)
        # self.frame_timer.start(int(100 / self.video_stream.get_fps() * self.waiting_between_frame_reads_coef))
    
    def record_video(self):
        self.ofstream.write(self.video_stream.get_frame(self.video_size[0], self.video_size[1]))
    
    def stop_video_recording(self):
        self.frame_timer.stop()
        self.ofstream.release()
    
    def prepare_audio_recording(self, audio_device_index):
        self.audio_chunk = 1024
        self.audio_sample_format = pyaudio.paInt16
        self.audio_channels_count = 2
        self.audio_fs = 44100
        self.pyaudio = pyaudio.PyAudio()
        self.audio_frames = []
        
        self.audio_stream = self.pyaudio.open(format = self.audio_sample_format,
                                               channels = self.audio_channels_count,
                                               rate = self.audio_fs,
                                               frames_per_buffer = self.audio_chunk,
                                               input = True,
                                               input_device_index = audio_device_index)
        
        self.audio_recording_thread = Thread(target = self.record_audio, args = [])
    
    def start_audio_recording(self):
        self.audio_recording_thread.start()
    
    def record_audio(self):
        while self.recording:
            self.audio_frames.append(self.audio_stream.read(self.audio_chunk))
    
    def stop_audio_recording(self):
        self.audio_stream.stop_stream()
        self.audio_stream.close()
        self.pyaudio.terminate()

    def start(self, filename, audio_device_index):
        self.filename_without_index = filename
        self.cur_file_part_index = 1
        self.filename = filename + '_' + str(self.cur_file_part_index)
        self.recording = True
        
        self.video_saving_thread = Thread(target = self.save_video, args = [])
        
        self.prepare_video_recording()
        self.prepare_audio_recording(audio_device_index)
        
        self.start_video_recording()
        self.start_audio_recording()
        self.video_saving_thread.start()

    def stop(self):
        self.recording = False
        self.video_processing = True

        self.stop_video_recording()
        self.stop_audio_recording()
        
        self.video_rendering_thread = Thread(target = self.render_video, args = [])
        self.video_rendering_thread.start()
    
    def save_video_part(self):
        wf = wave.open(self.filename + '.wav', 'wb')

        self.cur_file_part_index += 1
        self.filename = self.filename_without_index + '_' + str(self.cur_file_part_index)
        
        new_ofstream = cv2.VideoWriter(self.filename + '.mp4', self.fourcc, self.video_stream.get_fps(), self.video_size)
        old_ofstream = self.ofstream

        new_audio_frames = []
        old_audio_frames = self.audio_frames
        self.audio_frames = new_audio_frames
        
        self.ofstream = new_ofstream
        old_ofstream.release()
        
        wf.setnchannels(self.audio_channels_count)
        wf.setsampwidth(self.pyaudio.get_sample_size(self.audio_sample_format))
        wf.setframerate(self.audio_fs)
        wf.writeframes(b''.join(old_audio_frames))
        wf.close()
    
    def save_video(self):
        while self.recording:
            for i in range(SAVE_CHECKS_COUNT):
                time.sleep(VIDEO_PART_LENGTH_IN_SEC / SAVE_CHECKS_COUNT)
                
                if not self.recording:
                    break

            if self.recording:
                self.save_video_part()
    
    def render_video(self):
        wf = wave.open(self.filename + '.wav', 'wb')
        wf.setnchannels(self.audio_channels_count)
        wf.setsampwidth(self.pyaudio.get_sample_size(self.audio_sample_format))
        wf.setframerate(self.audio_fs)
        wf.writeframes(b''.join(self.audio_frames))
        wf.close()
        
        self.video_processing = False
        self.end_rendering.emit()
    
    def is_recording(self):
        return self.recording
    
    def change_video_device_to_screen(self):
        self.recording_screen = True
        self.waiting_between_frame_reads_coef = WAITING_BETWEEN_FRAME_READS_COEF_SCREEN

        if self.recording:
            self.frame_timer.stop()
            self.frame_timer = AsyncTimer(self.record_video)
            self.frame_timer.start(1 / self.video_stream.get_fps() * self.waiting_between_frame_reads_coef)
            # self.frame_timer.start(int(1000 / self.video_stream.get_fps() * self.waiting_between_frame_reads_coef))
    
    def change_video_device_to_camera(self):
        self.recording_screen = False
        self.waiting_between_frame_reads_coef = WAITING_BETWEEN_FRAME_READS_COEF_CAMERA

        if self.recording:
            self.frame_timer.stop()
            self.frame_timer = AsyncTimer(self.record_video)
            self.frame_timer.start(1 / self.video_stream.get_fps() * self.waiting_between_frame_reads_coef)
            # self.frame_timer.start(int(1000 / self.video_stream.get_fps() * self.waiting_between_frame_reads_coef))
    
    def is_video_processing(self):
        return self.video_processing
