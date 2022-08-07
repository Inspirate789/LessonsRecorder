import cv2
import os
from PyQt5 import QtCore, QtGui, QtWidgets
import pyaudio # +sounddevice?

from mainwindow import Ui_MainWindow
from videostream import VideoStream
from videorecorder import VideoRecorder



OUTPUT_DIR_NAME = 'Video'

if not os.path.exists(OUTPUT_DIR_NAME):
    os.mkdir(OUTPUT_DIR_NAME)



class Window(QtWidgets.QMainWindow):
    video_device_changed = QtCore.pyqtSignal()
    resized = QtCore.pyqtSignal()
    closed = QtCore.pyqtSignal()

    def  __init__(self, parent = None):
        super(Window, self).__init__(parent=parent)
    
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_F2:
            self.video_device_changed.emit()

        return super(Window, self).keyPressEvent(event)

    def resizeEvent(self, event):
        self.resized.emit()

        return super(Window, self).resizeEvent(event)
    
    def closeEvent(self, event):
        self.closed.emit()

        return super(Window, self).closeEvent(event)



class Interface(Ui_MainWindow):
    recording = False
    fps_list = [30, 60]
    result_video_index = 1
    audio_device_index = 0
    last_camera_index = 1

    def __init__(self):
        super().__init__()
        self.fps = self.fps_list[0]

        self.video_stream = VideoStream(self.fps)
        self.recorder = VideoRecorder(self.video_stream)
        
        self.frame_timer = QtCore.QTimer()
        self.frame_timer.timeout.connect(self.display_video_stream)
    
    def setupUi(self, MainWindow: Window):
        self.MainWindow = MainWindow

        super().setupUi(self.MainWindow)

        self.video_size = QtCore.QSize(self.MainWindow.geometry().width(),
                                   int(self.MainWindow.geometry().width() * 9 / 16))
        self.video_size *= 0.67

        self.video_lbl.setFixedSize(self.video_size)

        self.select_fps_cb.currentIndexChanged.connect(self.select_fps_cb_changed)
        self.select_video_source_cb.currentIndexChanged.connect(self.select_video_source_cb_changed)
        self.select_audio_source_cb.currentIndexChanged.connect(self.select_audio_source_cb_changed)
        self.recording_btn.clicked.connect(self.recording_btn_pressed)

        self.MainWindow.resized.connect(self.resizeEvent)
        self.MainWindow.closed.connect(self.closeEvent)
        self.MainWindow.video_device_changed.connect(self.change_video_device)
        self.recorder.end_rendering.connect(self.end_rendering)

        for i in range(len(self.fps_list)):
            self.select_fps_cb.addItem(str(self.fps_list[i]) + " кадров в секунду")
        
        self.video_devices_list = self.video_stream.get_devices_list()
        self.update_audio_devices_list()
        
        self.select_video_source_cb.addItem(str(self.video_devices_list[0]))
        for i in range(1, len(self.video_devices_list)):
            self.select_video_source_cb.addItem('Камера ' + str(i))
        
        for i in range(len(self.audio_devices_list)):
            self.select_audio_source_cb.addItem(self.audio_devices_list[i]['name'])
    
    def update_audio_devices_list(self):
        self.audio_devices_list = []
        device_names = []
        p = pyaudio.PyAudio()

        for i in range(p.get_device_count()):
            device_name = p.get_device_info_by_index(i)['name']
            low_str = device_name.lower()

            if device_name in device_names:
                continue
            
            if low_str.find('microphone') != -1 or low_str.find('микрофон') != -1 or \
               low_str.find('headphones') != -1 or low_str.find('наушники') != -1 or \
               low_str.find('phone') != -1 or low_str.find('телефон') != -1:
                device = {'index': i, 'name': device_name}
                self.audio_devices_list.append(device)
    
    def run_videoplayer(self):
        self.video_stream.run()
        self.frame_timer.start(int(1000 // self.fps))
    
    def display_video_stream(self):
        image = self.video_stream.get_image(self.video_size.width(), self.video_size.height())

        if image:
            self.video_lbl.setPixmap(QtGui.QPixmap.fromImage(image))
    
    def select_fps_cb_changed(self):
        try:
            self.fps = self.fps_list[self.select_fps_cb.currentIndex()]
            self.frame_timer.start(int(1000 // self.fps))
            self.video_stream.run(self.fps)
        except Exception as e:
            self.handle_exception(e, 'Не удалось изменить частоту кадров.')
    
    def select_video_source_cb_changed(self):
        try:
            self.video_stream.change_videostream(self.select_video_source_cb.currentIndex())

            if self.select_video_source_cb.currentIndex() == 0:
                self.recorder.change_video_device_to_screen()
            else:
                self.recorder.change_video_device_to_camera()
                self.last_camera_index = self.select_video_source_cb.currentIndex()
        except Exception as e:
            self.handle_exception(e, 'Не удалось изменить устройство захвата видео.')
    
    def select_audio_source_cb_changed(self):
        try:
            i = self.select_audio_source_cb.currentIndex()
            self.audio_device_index = self.audio_devices_list[i]['index']
        except Exception as e:
            self.handle_exception(e, 'Не удалось изменить устройство захвата аудио.')
    
    def end_rendering(self):
        self.recording_btn.setEnabled(True)
        self.select_audio_source_cb.setEnabled(True)
        self.select_fps_cb.setEnabled(True)
        self.recording_btn.setText('Начать запись')
    
    def recording_btn_pressed(self):
        if not self.recorder.is_video_processing():
            if self.recording:
                self.recording_btn.setText('Сохранение...')
                self.recording_btn.setEnabled(False)

                self.recording = False
                
                try:
                    self.recorder.stop()
                except Exception as e:
                    self.handle_exception(e, 'Не удалось остановить запись.')
            else:
                self.select_fps_cb.setEnabled(False)
                self.select_audio_source_cb.setEnabled(False)
                self.recording_btn.setEnabled(False)
                
                con_output_dir_name = OUTPUT_DIR_NAME + '\\Record' + str(self.result_video_index)

                while os.path.exists(con_output_dir_name):
                    self.result_video_index += 1
                    con_output_dir_name = OUTPUT_DIR_NAME + '\\Record' + str(self.result_video_index)

                if not os.path.exists(con_output_dir_name):
                    os.mkdir(con_output_dir_name)

                output_video_filename = con_output_dir_name + '\\Record' + str(self.result_video_index)
                
                self.recording = True

                try:
                    self.recorder.start(output_video_filename, self.audio_device_index)
                except Exception as e:
                    self.handle_exception(e, 'Не удалось начать запись.')
                    
                self.result_video_index += 1

                self.recording_btn.setEnabled(True)
                self.recording_btn.setText('Остановить запись')
    
    def handle_exception(exception, message):
        # print(exception)
        msg = QtWidgets.QMessageBox()
        msg.setStyleSheet('')
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setWindowTitle('Ошибка')
        msg.setText(message)
        msg.exec()
    
    def change_video_device(self):
        index = self.select_video_source_cb.currentIndex()
        
        if index == 0:
            self.select_video_source_cb.setCurrentIndex(self.last_camera_index)
        else:
            self.select_video_source_cb.setCurrentIndex(0)
    
    def resizeEvent(self):
        self.video_size = QtCore.QSize(self.MainWindow.geometry().width(),
                                   int(self.MainWindow.geometry().width() * 9 / 16))
        self.video_size *= 0.67
        self.video_lbl.setFixedSize(self.video_size)

    def closeEvent(self):
        if self.recording:
            self.recorder.stop()
        
        self.frame_timer.stop()
        self.video_stream.stop()
        cv2.destroyAllWindows()
