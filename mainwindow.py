from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName('Lessons Recorder')
        MainWindow.resize(916, 663)
        font = QtGui.QFont()
        font.setPointSize(15)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QMainWindow {\n"
                                 "    background-color: #ECEFF4;\n"
                                 "}\n"
                                 "\n"
                                 "QWidget {\n"
                                 "    background-color: #ECEFF4;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton {\n"
                                 "    background-color: #9EB8D2;\n"
                                 "    border: 2px solid #81A1C1;\n"
                                 "    border-radius: 10px;\n"
                                 "    padding: 7px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "    background: #81A1C1;\n"
                                 "    transition: background 0s;\n"
                                 "}\n"
                                 "\n"
                                 "QGroupBox {\n"
                                 "    background-color: #D8DEE9;\n"
                                 "    border: 2px solid #81A1C1;\n"
                                 "    border-radius: 7px;\n"
                                 "}\n"
                                 "\n"
                                 "QLabel {\n"
                                 "    background-color: #D8DEE9;\n"
                                 "}\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.main_frame.setObjectName("main_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.main_frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.recording_gb = QtWidgets.QGroupBox(self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recording_gb.sizePolicy().hasHeightForWidth())
        self.recording_gb.setSizePolicy(sizePolicy)
        self.recording_gb.setTitle("")
        self.recording_gb.setObjectName("recording_gb")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.recording_gb)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_7.addItem(spacerItem, 4, 0, 1, 1)
        self.select_fps_lbl = QtWidgets.QLabel(self.recording_gb)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_fps_lbl.sizePolicy().hasHeightForWidth())
        self.select_fps_lbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_fps_lbl.setFont(font)
        self.select_fps_lbl.setObjectName("select_fps_lbl")
        self.gridLayout_7.addWidget(self.select_fps_lbl, 1, 0, 1, 1)
        self.select_fps_cb = QtWidgets.QComboBox(self.recording_gb)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_fps_cb.sizePolicy().hasHeightForWidth())
        self.select_fps_cb.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_fps_cb.setFont(font)
        self.select_fps_cb.setObjectName("select_fps_cb")
        self.gridLayout_7.addWidget(self.select_fps_cb, 2, 0, 1, 1)
        self.recording_btn = QtWidgets.QPushButton(self.recording_gb)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recording_btn.sizePolicy().hasHeightForWidth())
        self.recording_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.recording_btn.setFont(font)
        self.recording_btn.setObjectName("recording_btn")
        self.gridLayout_7.addWidget(self.recording_btn, 5, 0, 1, 1)
        self.gridLayout_2.addWidget(self.recording_gb, 2, 0, 1, 1)
        self.audio_source_gb = QtWidgets.QGroupBox(self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.audio_source_gb.sizePolicy().hasHeightForWidth())
        self.audio_source_gb.setSizePolicy(sizePolicy)
        self.audio_source_gb.setTitle("")
        self.audio_source_gb.setObjectName("audio_source_gb")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.audio_source_gb)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.select_audio_source_lbl = QtWidgets.QLabel(self.audio_source_gb)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_audio_source_lbl.sizePolicy().hasHeightForWidth())
        self.select_audio_source_lbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_audio_source_lbl.setFont(font)
        self.select_audio_source_lbl.setObjectName("select_audio_source_lbl")
        self.gridLayout_6.addWidget(self.select_audio_source_lbl, 0, 0, 1, 1)
        self.select_audio_source_cb = QtWidgets.QComboBox(self.audio_source_gb)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_audio_source_cb.sizePolicy().hasHeightForWidth())
        self.select_audio_source_cb.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_audio_source_cb.setFont(font)
        self.select_audio_source_cb.setObjectName("select_audio_source_cb")
        self.gridLayout_6.addWidget(self.select_audio_source_cb, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_6.addItem(spacerItem1, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.audio_source_gb, 2, 2, 1, 1)
        self.video_source_gb = QtWidgets.QGroupBox(self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.video_source_gb.sizePolicy().hasHeightForWidth())
        self.video_source_gb.setSizePolicy(sizePolicy)
        self.video_source_gb.setTitle("")
        self.video_source_gb.setObjectName("video_source_gb")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.video_source_gb)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.select_video_source_cb = QtWidgets.QComboBox(self.video_source_gb)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_video_source_cb.sizePolicy().hasHeightForWidth())
        self.select_video_source_cb.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_video_source_cb.setFont(font)
        self.select_video_source_cb.setStyleSheet("")
        self.select_video_source_cb.setObjectName("select_video_source_cb")
        self.gridLayout_5.addWidget(self.select_video_source_cb, 1, 0, 1, 1)
        self.select_video_source_lbl = QtWidgets.QLabel(self.video_source_gb)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_video_source_lbl.sizePolicy().hasHeightForWidth())
        self.select_video_source_lbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_video_source_lbl.setFont(font)
        self.select_video_source_lbl.setObjectName("select_video_source_lbl")
        self.gridLayout_5.addWidget(self.select_video_source_lbl, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_5.addItem(spacerItem2, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.video_source_gb, 2, 1, 1, 1)
        self.videoplayer_gb = QtWidgets.QGroupBox(self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoplayer_gb.sizePolicy().hasHeightForWidth())
        self.videoplayer_gb.setSizePolicy(sizePolicy)
        self.videoplayer_gb.setTitle("")
        self.videoplayer_gb.setObjectName("videoplayer_gb")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.videoplayer_gb)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.video_lbl = QtWidgets.QLabel(self.videoplayer_gb)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.video_lbl.sizePolicy().hasHeightForWidth())
        self.video_lbl.setSizePolicy(sizePolicy)
        self.video_lbl.setText("")
        self.video_lbl.setObjectName("video_lbl")
        self.gridLayout_3.addWidget(self.video_lbl, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 0, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem4, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.videoplayer_gb, 0, 0, 2, 3)
        self.gridLayout_4.addWidget(self.main_frame, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 916, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate('Lessons Recorder', 'Lessons Recorder'))
        self.select_fps_lbl.setText(_translate('Lessons Recorder', "Частота кадров"))
        self.recording_btn.setText(_translate('Lessons Recorder', "Начать запись"))
        self.select_audio_source_lbl.setText(_translate('Lessons Recorder', "Источник аудио"))
        self.select_video_source_lbl.setText(_translate('Lessons Recorder', "Источник видео"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
