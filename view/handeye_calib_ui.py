# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'handeye_calib.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HandeyeCalib(object):
    def setupUi(self, HandeyeCalib):
        HandeyeCalib.setObjectName("HandeyeCalib")
        HandeyeCalib.resize(1080, 800)
        HandeyeCalib.setStyleSheet("")
        self.frame = QtWidgets.QFrame(HandeyeCalib)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1080, 550))
        self.frame.setMaximumSize(QtCore.QSize(1080, 550))
        self.frame.setStyleSheet("background-color: rgb(44, 51, 58)")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.PixmapLabel = PixmapLabel(self.frame)
        self.PixmapLabel.setGeometry(QtCore.QRect(240, 34, 640, 480))
        self.PixmapLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PixmapLabel.setObjectName("PixmapLabel")
        self.exit = PillToolButton(self.frame)
        self.exit.setGeometry(QtCore.QRect(1050, 6, 25, 25))
        self.exit.setCheckable(False)
        self.exit.setObjectName("exit")
        self.minimize = PillToolButton(self.frame)
        self.minimize.setGeometry(QtCore.QRect(1020, 6, 25, 25))
        self.minimize.setCheckable(False)
        self.minimize.setObjectName("minimize")
        self.frame_8 = QtWidgets.QFrame(self.frame)
        self.frame_8.setGeometry(QtCore.QRect(30, 280, 156, 257))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.SubtitleLabel_8 = SubtitleLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SubtitleLabel_8.setFont(font)
        self.SubtitleLabel_8.setStyleSheet("color: white;\n"
"FluentLabelBase {\n"
"    color: black;\n"
"}\n"
"\n"
"HyperlinkLabel {\n"
"    color: #009faa;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=true] {\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=false] {\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"HyperlinkLabel:hover {\n"
"    color: #007780;\n"
"}\n"
"\n"
"HyperlinkLabel:pressed {\n"
"    color: #00a7b3;\n"
"}\n"
"FluentLabelBase{color:#000000}")
        self.SubtitleLabel_8.setAlignment(QtCore.Qt.AlignCenter)
        self.SubtitleLabel_8.setObjectName("SubtitleLabel_8")
        self.verticalLayout_2.addWidget(self.SubtitleLabel_8)
        self.robot_x = SubtitleLabel(self.frame_8)
        self.robot_x.setStyleSheet("color: white;\n"
"FluentLabelBase {\n"
"    color: black;\n"
"}\n"
"\n"
"HyperlinkLabel {\n"
"    color: #009faa;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=true] {\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=false] {\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"HyperlinkLabel:hover {\n"
"    color: #007780;\n"
"}\n"
"\n"
"HyperlinkLabel:pressed {\n"
"    color: #00a7b3;\n"
"}\n"
"FluentLabelBase{color:#000000}")
        self.robot_x.setAlignment(QtCore.Qt.AlignCenter)
        self.robot_x.setObjectName("robot_x")
        self.verticalLayout_2.addWidget(self.robot_x)
        self.robot_y = SubtitleLabel(self.frame_8)
        self.robot_y.setStyleSheet("color: white;\n"
"FluentLabelBase {\n"
"    color: black;\n"
"}\n"
"\n"
"HyperlinkLabel {\n"
"    color: #009faa;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=true] {\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=false] {\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"HyperlinkLabel:hover {\n"
"    color: #007780;\n"
"}\n"
"\n"
"HyperlinkLabel:pressed {\n"
"    color: #00a7b3;\n"
"}\n"
"FluentLabelBase{color:#000000}")
        self.robot_y.setAlignment(QtCore.Qt.AlignCenter)
        self.robot_y.setObjectName("robot_y")
        self.verticalLayout_2.addWidget(self.robot_y)
        self.robot_z = SubtitleLabel(self.frame_8)
        self.robot_z.setStyleSheet("color: white;\n"
"FluentLabelBase {\n"
"    color: black;\n"
"}\n"
"\n"
"HyperlinkLabel {\n"
"    color: #009faa;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=true] {\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=false] {\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"HyperlinkLabel:hover {\n"
"    color: #007780;\n"
"}\n"
"\n"
"HyperlinkLabel:pressed {\n"
"    color: #00a7b3;\n"
"}\n"
"FluentLabelBase{color:#000000}")
        self.robot_z.setAlignment(QtCore.Qt.AlignCenter)
        self.robot_z.setObjectName("robot_z")
        self.verticalLayout_2.addWidget(self.robot_z)
        self.robot_rx = SubtitleLabel(self.frame_8)
        self.robot_rx.setStyleSheet("color: white;\n"
"FluentLabelBase {\n"
"    color: black;\n"
"}\n"
"\n"
"HyperlinkLabel {\n"
"    color: #009faa;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=true] {\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=false] {\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"HyperlinkLabel:hover {\n"
"    color: #007780;\n"
"}\n"
"\n"
"HyperlinkLabel:pressed {\n"
"    color: #00a7b3;\n"
"}\n"
"FluentLabelBase{color:#000000}")
        self.robot_rx.setAlignment(QtCore.Qt.AlignCenter)
        self.robot_rx.setObjectName("robot_rx")
        self.verticalLayout_2.addWidget(self.robot_rx)
        self.robot_ry = SubtitleLabel(self.frame_8)
        self.robot_ry.setStyleSheet("color: white;\n"
"FluentLabelBase {\n"
"    color: black;\n"
"}\n"
"\n"
"HyperlinkLabel {\n"
"    color: #009faa;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=true] {\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=false] {\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"HyperlinkLabel:hover {\n"
"    color: #007780;\n"
"}\n"
"\n"
"HyperlinkLabel:pressed {\n"
"    color: #00a7b3;\n"
"}\n"
"FluentLabelBase{color:#000000}")
        self.robot_ry.setAlignment(QtCore.Qt.AlignCenter)
        self.robot_ry.setObjectName("robot_ry")
        self.verticalLayout_2.addWidget(self.robot_ry)
        self.robot_rz = SubtitleLabel(self.frame_8)
        self.robot_rz.setStyleSheet("color: white;\n"
"FluentLabelBase {\n"
"    color: black;\n"
"}\n"
"\n"
"HyperlinkLabel {\n"
"    color: #009faa;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=true] {\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=false] {\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"HyperlinkLabel:hover {\n"
"    color: #007780;\n"
"}\n"
"\n"
"HyperlinkLabel:pressed {\n"
"    color: #00a7b3;\n"
"}\n"
"FluentLabelBase{color:#000000}")
        self.robot_rz.setAlignment(QtCore.Qt.AlignCenter)
        self.robot_rz.setObjectName("robot_rz")
        self.verticalLayout_2.addWidget(self.robot_rz)
        self.frame_9 = QtWidgets.QFrame(self.frame)
        self.frame_9.setGeometry(QtCore.QRect(30, 10, 156, 257))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.SubtitleLabel_15 = SubtitleLabel(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SubtitleLabel_15.setFont(font)
        self.SubtitleLabel_15.setStyleSheet("color: white;\n"
"FluentLabelBase {\n"
"    color: black;\n"
"}\n"
"\n"
"HyperlinkLabel {\n"
"    color: #009faa;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=true] {\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=false] {\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"HyperlinkLabel:hover {\n"
"    color: #007780;\n"
"}\n"
"\n"
"HyperlinkLabel:pressed {\n"
"    color: #00a7b3;\n"
"}\n"
"FluentLabelBase{color:#000000}")
        self.SubtitleLabel_15.setAlignment(QtCore.Qt.AlignCenter)
        self.SubtitleLabel_15.setObjectName("SubtitleLabel_15")
        self.verticalLayout_3.addWidget(self.SubtitleLabel_15)
        self.target_x = SubtitleLabel(self.frame_9)
        self.target_x.setStyleSheet("color: white;\n"
"FluentLabelBase {\n"
"    color: black;\n"
"}\n"
"\n"
"HyperlinkLabel {\n"
"    color: #009faa;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=true] {\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=false] {\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"HyperlinkLabel:hover {\n"
"    color: #007780;\n"
"}\n"
"\n"
"HyperlinkLabel:pressed {\n"
"    color: #00a7b3;\n"
"}\n"
"FluentLabelBase{color:#000000}")
        self.target_x.setAlignment(QtCore.Qt.AlignCenter)
        self.target_x.setObjectName("target_x")
        self.verticalLayout_3.addWidget(self.target_x)
        self.target_y = SubtitleLabel(self.frame_9)
        self.target_y.setStyleSheet("color: white;\n"
"FluentLabelBase {\n"
"    color: black;\n"
"}\n"
"\n"
"HyperlinkLabel {\n"
"    color: #009faa;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=true] {\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=false] {\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"HyperlinkLabel:hover {\n"
"    color: #007780;\n"
"}\n"
"\n"
"HyperlinkLabel:pressed {\n"
"    color: #00a7b3;\n"
"}\n"
"FluentLabelBase{color:#000000}")
        self.target_y.setAlignment(QtCore.Qt.AlignCenter)
        self.target_y.setObjectName("target_y")
        self.verticalLayout_3.addWidget(self.target_y)
        self.target_z = SubtitleLabel(self.frame_9)
        self.target_z.setStyleSheet("color: white;\n"
"FluentLabelBase {\n"
"    color: black;\n"
"}\n"
"\n"
"HyperlinkLabel {\n"
"    color: #009faa;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=true] {\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=false] {\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"HyperlinkLabel:hover {\n"
"    color: #007780;\n"
"}\n"
"\n"
"HyperlinkLabel:pressed {\n"
"    color: #00a7b3;\n"
"}\n"
"FluentLabelBase{color:#000000}")
        self.target_z.setAlignment(QtCore.Qt.AlignCenter)
        self.target_z.setObjectName("target_z")
        self.verticalLayout_3.addWidget(self.target_z)
        self.target_rx = SubtitleLabel(self.frame_9)
        self.target_rx.setStyleSheet("color: white;\n"
"FluentLabelBase {\n"
"    color: black;\n"
"}\n"
"\n"
"HyperlinkLabel {\n"
"    color: #009faa;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=true] {\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=false] {\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"HyperlinkLabel:hover {\n"
"    color: #007780;\n"
"}\n"
"\n"
"HyperlinkLabel:pressed {\n"
"    color: #00a7b3;\n"
"}\n"
"FluentLabelBase{color:#000000}")
        self.target_rx.setAlignment(QtCore.Qt.AlignCenter)
        self.target_rx.setObjectName("target_rx")
        self.verticalLayout_3.addWidget(self.target_rx)
        self.target_ry = SubtitleLabel(self.frame_9)
        self.target_ry.setStyleSheet("color: white;\n"
"FluentLabelBase {\n"
"    color: black;\n"
"}\n"
"\n"
"HyperlinkLabel {\n"
"    color: #009faa;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=true] {\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=false] {\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"HyperlinkLabel:hover {\n"
"    color: #007780;\n"
"}\n"
"\n"
"HyperlinkLabel:pressed {\n"
"    color: #00a7b3;\n"
"}\n"
"FluentLabelBase{color:#000000}")
        self.target_ry.setAlignment(QtCore.Qt.AlignCenter)
        self.target_ry.setObjectName("target_ry")
        self.verticalLayout_3.addWidget(self.target_ry)
        self.target_rz = SubtitleLabel(self.frame_9)
        self.target_rz.setStyleSheet("color: white;\n"
"FluentLabelBase {\n"
"    color: black;\n"
"}\n"
"\n"
"HyperlinkLabel {\n"
"    color: #009faa;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=true] {\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=false] {\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"HyperlinkLabel:hover {\n"
"    color: #007780;\n"
"}\n"
"\n"
"HyperlinkLabel:pressed {\n"
"    color: #00a7b3;\n"
"}\n"
"FluentLabelBase{color:#000000}")
        self.target_rz.setAlignment(QtCore.Qt.AlignCenter)
        self.target_rz.setObjectName("target_rz")
        self.verticalLayout_3.addWidget(self.target_rz)
        self.frame_2 = QtWidgets.QFrame(HandeyeCalib)
        self.frame_2.setGeometry(QtCore.QRect(0, 550, 1080, 250))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 250))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.HeaderCardWidget = HeaderCardWidget(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.HeaderCardWidget.setFont(font)
        self.HeaderCardWidget.setStyleSheet("HeaderCardWidget #headerLabel {\n"
"    color: black;\n"
"}\n"
"\n"
"HeaderCardWidget > #headerView {\n"
"    background-color: rgb(222, 222, 222);\n"
"},\n"
"HeaderCardWidget > #view {\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.HeaderCardWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.HeaderCardWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.HeaderCardWidget.setBorderRadius(5)
        self.HeaderCardWidget.setObjectName("HeaderCardWidget")
        self.start = PrimaryPushButton(self.HeaderCardWidget)
        self.start.setGeometry(QtCore.QRect(900, 9, 131, 32))
        self.start.setObjectName("start")
        self.HorizontalSeparator = HorizontalSeparator(self.HeaderCardWidget)
        self.HorizontalSeparator.setGeometry(QtCore.QRect(20, 140, 1021, 3))
        self.HorizontalSeparator.setObjectName("HorizontalSeparator")
        self.frame_3 = QtWidgets.QFrame(self.HeaderCardWidget)
        self.frame_3.setGeometry(QtCore.QRect(33, 70, 321, 52))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.StrongBodyLabel = StrongBodyLabel(self.frame_3)
        self.StrongBodyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.StrongBodyLabel.setObjectName("StrongBodyLabel")
        self.horizontalLayout.addWidget(self.StrongBodyLabel)
        self.mount_type = ComboBox(self.frame_3)
        self.mount_type.setText("")
        self.mount_type.setAutoDefault(False)
        self.mount_type.setDefault(False)
        self.mount_type.setFlat(False)
        self.mount_type.setObjectName("mount_type")
        self.horizontalLayout.addWidget(self.mount_type)
        self.frame_4 = QtWidgets.QFrame(self.HeaderCardWidget)
        self.frame_4.setGeometry(QtCore.QRect(33, 160, 321, 52))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.StrongBodyLabel_2 = StrongBodyLabel(self.frame_4)
        self.StrongBodyLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.StrongBodyLabel_2.setObjectName("StrongBodyLabel_2")
        self.horizontalLayout_2.addWidget(self.StrongBodyLabel_2)
        self.target_type = ComboBox(self.frame_4)
        self.target_type.setText("")
        self.target_type.setObjectName("target_type")
        self.horizontalLayout_2.addWidget(self.target_type)
        self.frame_5 = QtWidgets.QFrame(self.HeaderCardWidget)
        self.frame_5.setGeometry(QtCore.QRect(420, 70, 251, 52))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.StrongBodyLabel_3 = StrongBodyLabel(self.frame_5)
        self.StrongBodyLabel_3.setMaximumSize(QtCore.QSize(70, 16777215))
        self.StrongBodyLabel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.StrongBodyLabel_3.setObjectName("StrongBodyLabel_3")
        self.horizontalLayout_3.addWidget(self.StrongBodyLabel_3)
        self.robot_ip = LineEdit(self.frame_5)
        self.robot_ip.setMaximumSize(QtCore.QSize(155, 33))
        self.robot_ip.setAlignment(QtCore.Qt.AlignCenter)
        self.robot_ip.setObjectName("robot_ip")
        self.horizontalLayout_3.addWidget(self.robot_ip)
        self.frame_6 = QtWidgets.QFrame(self.HeaderCardWidget)
        self.frame_6.setGeometry(QtCore.QRect(420, 160, 251, 52))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.StrongBodyLabel_4 = StrongBodyLabel(self.frame_6)
        self.StrongBodyLabel_4.setMaximumSize(QtCore.QSize(70, 16777215))
        self.StrongBodyLabel_4.setObjectName("StrongBodyLabel_4")
        self.horizontalLayout_4.addWidget(self.StrongBodyLabel_4)
        self.calibration_algorithm = ComboBox(self.frame_6)
        self.calibration_algorithm.setText("")
        self.calibration_algorithm.setAutoDefault(False)
        self.calibration_algorithm.setDefault(False)
        self.calibration_algorithm.setFlat(False)
        self.calibration_algorithm.setObjectName("calibration_algorithm")
        self.horizontalLayout_4.addWidget(self.calibration_algorithm)
        self.connect_robot = ToggleButton(self.HeaderCardWidget)
        self.connect_robot.setGeometry(QtCore.QRect(740, 9, 131, 32))
        self.connect_robot.setObjectName("connect_robot")
        self.connect_camera = ToggleButton(self.HeaderCardWidget)
        self.connect_camera.setGeometry(QtCore.QRect(600, 9, 131, 32))
        self.connect_camera.setObjectName("connect_camera")
        self.frame_7 = QtWidgets.QFrame(self.HeaderCardWidget)
        self.frame_7.setGeometry(QtCore.QRect(740, 70, 261, 52))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.StrongBodyLabel_5 = StrongBodyLabel(self.frame_7)
        self.StrongBodyLabel_5.setMaximumSize(QtCore.QSize(80, 16777215))
        self.StrongBodyLabel_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.StrongBodyLabel_5.setObjectName("StrongBodyLabel_5")
        self.horizontalLayout_5.addWidget(self.StrongBodyLabel_5)
        self.robot_type = ComboBox(self.frame_7)
        self.robot_type.setText("")
        self.robot_type.setAutoDefault(False)
        self.robot_type.setDefault(False)
        self.robot_type.setFlat(False)
        self.robot_type.setObjectName("robot_type")
        self.horizontalLayout_5.addWidget(self.robot_type)
        self.gridLayout_2.addWidget(self.HeaderCardWidget, 0, 0, 1, 1)

        self.retranslateUi(HandeyeCalib)
        QtCore.QMetaObject.connectSlotsByName(HandeyeCalib)

    def retranslateUi(self, HandeyeCalib):
        _translate = QtCore.QCoreApplication.translate
        HandeyeCalib.setWindowTitle(_translate("HandeyeCalib", "Form"))
        self.SubtitleLabel_8.setText(_translate("HandeyeCalib", "Robot Pose"))
        self.robot_x.setText(_translate("HandeyeCalib", "X:"))
        self.robot_y.setText(_translate("HandeyeCalib", "Y:"))
        self.robot_z.setText(_translate("HandeyeCalib", "Z:"))
        self.robot_rx.setText(_translate("HandeyeCalib", "Rx:"))
        self.robot_ry.setText(_translate("HandeyeCalib", "Ry:"))
        self.robot_rz.setText(_translate("HandeyeCalib", "Rz:"))
        self.SubtitleLabel_15.setText(_translate("HandeyeCalib", "Target Pose"))
        self.target_x.setText(_translate("HandeyeCalib", "X:"))
        self.target_y.setText(_translate("HandeyeCalib", "Y:"))
        self.target_z.setText(_translate("HandeyeCalib", "Z:"))
        self.target_rx.setText(_translate("HandeyeCalib", "Rx:"))
        self.target_ry.setText(_translate("HandeyeCalib", "Ry:"))
        self.target_rz.setText(_translate("HandeyeCalib", "Rz:"))
        self.HeaderCardWidget.setTitle(_translate("HandeyeCalib", "Handeye Calibration Settings"))
        self.start.setText(_translate("HandeyeCalib", "Start"))
        self.StrongBodyLabel.setText(_translate("HandeyeCalib", "Sensor Mount Type"))
        self.StrongBodyLabel_2.setText(_translate("HandeyeCalib", "Target Type"))
        self.StrongBodyLabel_3.setText(_translate("HandeyeCalib", "Robot IP"))
        self.robot_ip.setText(_translate("HandeyeCalib", "192.168.56.102"))
        self.StrongBodyLabel_4.setText(_translate("HandeyeCalib", "Algorithm"))
        self.connect_robot.setText(_translate("HandeyeCalib", "Robot"))
        self.connect_camera.setText(_translate("HandeyeCalib", "Camera"))
        self.StrongBodyLabel_5.setText(_translate("HandeyeCalib", "Robot Type"))
from qfluentwidgets import ComboBox, HeaderCardWidget, HorizontalSeparator, LineEdit, PillToolButton, PixmapLabel, PrimaryPushButton, StrongBodyLabel, SubtitleLabel, ToggleButton
