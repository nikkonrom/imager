# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(890, 519)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("python/C:/Users/jeavr/Desktop/unnamed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.boundariesButton = QtWidgets.QPushButton(self.groupBox)
        self.boundariesButton.setObjectName("boundariesButton")
        self.verticalLayout_2.addWidget(self.boundariesButton)
        self.semanticSegmentationButton = QtWidgets.QPushButton(self.groupBox)
        self.semanticSegmentationButton.setObjectName("semanticSegmentationButton")
        self.verticalLayout_2.addWidget(self.semanticSegmentationButton)
        self.pushButtonImageSaliency = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonImageSaliency.setObjectName("pushButtonImageSaliency")
        self.verticalLayout_2.addWidget(self.pushButtonImageSaliency)
        self.pushButtonFaceRecognition = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonFaceRecognition.setObjectName("pushButtonFaceRecognition")
        self.verticalLayout_2.addWidget(self.pushButtonFaceRecognition)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.stackedWidget = QtWidgets.QStackedWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.page)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.radioButtonRoberts = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButtonRoberts.setChecked(True)
        self.radioButtonRoberts.setObjectName("radioButtonRoberts")
        self.verticalLayout_4.addWidget(self.radioButtonRoberts)
        self.radioButtonPrewitt = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButtonPrewitt.setObjectName("radioButtonPrewitt")
        self.verticalLayout_4.addWidget(self.radioButtonPrewitt)
        self.radioButtonScharr = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButtonScharr.setObjectName("radioButtonScharr")
        self.verticalLayout_4.addWidget(self.radioButtonScharr)
        self.radioButtonSobel = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButtonSobel.setObjectName("radioButtonSobel")
        self.verticalLayout_4.addWidget(self.radioButtonSobel)
        self.horizontalLayout_4.addWidget(self.groupBox_2)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.page_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox_4 = QtWidgets.QGroupBox(self.page_3)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_5.addWidget(self.groupBox_4)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.page_4)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.groupBox_5 = QtWidgets.QGroupBox(self.page_4)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label = QtWidgets.QLabel(self.groupBox_5)
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.spinBoxR = QtWidgets.QSpinBox(self.groupBox_5)
        self.spinBoxR.setMaximum(255)
        self.spinBoxR.setProperty("value", 255)
        self.spinBoxR.setObjectName("spinBoxR")
        self.horizontalLayout_7.addWidget(self.spinBoxR)
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.spinBoxG = QtWidgets.QSpinBox(self.groupBox_5)
        self.spinBoxG.setMaximum(255)
        self.spinBoxG.setObjectName("spinBoxG")
        self.horizontalLayout_7.addWidget(self.spinBoxG)
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.spinBoxB = QtWidgets.QSpinBox(self.groupBox_5)
        self.spinBoxB.setMaximum(255)
        self.spinBoxB.setObjectName("spinBoxB")
        self.horizontalLayout_7.addWidget(self.spinBoxB)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.spinBoxWidth = QtWidgets.QSpinBox(self.groupBox_5)
        self.spinBoxWidth.setMaximum(10)
        self.spinBoxWidth.setObjectName("spinBoxWidth")
        self.horizontalLayout_8.addWidget(self.spinBoxWidth)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.spinBoxG.raise_()
        self.spinBoxR.raise_()
        self.spinBoxB.raise_()
        self.spinBoxR.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.spinBoxWidth.raise_()
        self.horizontalLayout_6.addWidget(self.groupBox_5)
        self.stackedWidget.addWidget(self.page_4)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout.addWidget(self.groupBox, 0, 3, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 0, 2, 1, 1)
        self.outputLabel = ScaledPixmap(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputLabel.sizePolicy().hasHeightForWidth())
        self.outputLabel.setSizePolicy(sizePolicy)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.outputLabel.setLineWidth(1)
        self.outputLabel.setText("")
        self.outputLabel.setScaledContents(False)
        self.outputLabel.setObjectName("outputLabel")
        self.gridLayout.addWidget(self.outputLabel, 0, 1, 1, 1)
        self.inputLabel = ScaledPixmap(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputLabel.sizePolicy().hasHeightForWidth())
        self.inputLabel.setSizePolicy(sizePolicy)
        self.inputLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inputLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.inputLabel.setLineWidth(1)
        self.inputLabel.setText("")
        self.inputLabel.setScaledContents(False)
        self.inputLabel.setObjectName("inputLabel")
        self.gridLayout.addWidget(self.inputLabel, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ignoreOverscaleCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.ignoreOverscaleCheckBox.setAcceptDrops(False)
        self.ignoreOverscaleCheckBox.setChecked(True)
        self.ignoreOverscaleCheckBox.setObjectName("ignoreOverscaleCheckBox")
        self.horizontalLayout_2.addWidget(self.ignoreOverscaleCheckBox)
        self.keepAspectRatioCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.keepAspectRatioCheckBox.setChecked(True)
        self.keepAspectRatioCheckBox.setObjectName("keepAspectRatioCheckBox")
        self.horizontalLayout_2.addWidget(self.keepAspectRatioCheckBox)
        self.loadButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadButton.setObjectName("loadButton")
        self.horizontalLayout_2.addWidget(self.loadButton)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButtonExportSettings = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonExportSettings.setObjectName("pushButtonExportSettings")
        self.horizontalLayout_2.addWidget(self.pushButtonExportSettings)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 890, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionOpen_2 = QtWidgets.QAction(MainWindow)
        self.actionOpen_2.setObjectName("actionOpen_2")
        self.actionOpen_3 = QtWidgets.QAction(MainWindow)
        self.actionOpen_3.setObjectName("actionOpen_3")
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Imager"))
        self.groupBox.setTitle(_translate("MainWindow", "Controlls"))
        self.boundariesButton.setText(_translate("MainWindow", "Boundaries"))
        self.semanticSegmentationButton.setText(_translate("MainWindow", "Semantic Segmentation"))
        self.pushButtonImageSaliency.setText(_translate("MainWindow", "Saliency"))
        self.pushButtonFaceRecognition.setText(_translate("MainWindow", "Face Recognition"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Boundaries options"))
        self.radioButtonRoberts.setText(_translate("MainWindow", "Roberts filter"))
        self.radioButtonPrewitt.setText(_translate("MainWindow", "Prewitt filter"))
        self.radioButtonScharr.setText(_translate("MainWindow", "Scharr filter"))
        self.radioButtonSobel.setText(_translate("MainWindow", "Sobel filter"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Semantis Segmentation options"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Saliency options"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Face Recognition options"))
        self.label.setText(_translate("MainWindow", "R"))
        self.label_2.setText(_translate("MainWindow", "G"))
        self.label_3.setText(_translate("MainWindow", "B"))
        self.label_4.setText(_translate("MainWindow", "Rectangle width"))
        self.ignoreOverscaleCheckBox.setText(_translate("MainWindow", "Ignore original size"))
        self.keepAspectRatioCheckBox.setText(_translate("MainWindow", "Maintain propotions"))
        self.loadButton.setText(_translate("MainWindow", "Load"))
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.pushButtonExportSettings.setText(_translate("MainWindow", "Export options"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionOpen_2.setText(_translate("MainWindow", "Open"))
        self.actionOpen_3.setText(_translate("MainWindow", "Open"))

from scaledpixmap import ScaledPixmap
