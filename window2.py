#Copyright (C)  2017  Nihal Rao I, Sanjan S Poojari, Shishir Upadhya

from PyQt5 import QtCore, QtGui, QtWidgets
import lightstyle

class Ui_window2(object):
    def setupUi(self, window2):
        window2.setObjectName("window2")
        window2.resize(920, 469)
        window2.setStyleSheet(lightstyle.css)
        window2.setWindowIcon(QtGui.QIcon('icons/favicon.ico'))
        self.centralwidget = QtWidgets.QWidget(window2)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, 0, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 3, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.assignBtn = QtWidgets.QPushButton(self.centralwidget)
        self.assignBtn.setMinimumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.assignBtn.setFont(font)
        self.assignBtn.setObjectName("assignBtn")
        self.horizontalLayout.addWidget(self.assignBtn)
        self.undoBtn = QtWidgets.QPushButton(self.centralwidget)
        self.undoBtn.setMinimumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.undoBtn.setFont(font)
        self.undoBtn.setObjectName("undoBtn")
        self.horizontalLayout.addWidget(self.undoBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.backBtn = QtWidgets.QPushButton(self.centralwidget)
        self.backBtn.setMinimumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.backBtn.setFont(font)
        self.backBtn.setObjectName("backBtn")
        self.horizontalLayout.addWidget(self.backBtn)
        self.nextBtn = QtWidgets.QPushButton(self.centralwidget)
        self.nextBtn.setMinimumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.nextBtn.setFont(font)
        self.nextBtn.setObjectName("nextBtn")
        self.horizontalLayout.addWidget(self.nextBtn)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 4)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 2, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.assigned_list = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assigned_list.sizePolicy().hasHeightForWidth())
        self.assigned_list.setSizePolicy(sizePolicy)
        self.assigned_list.setMinimumSize(QtCore.QSize(596, 290))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.assigned_list.setFont(font)
        self.assigned_list.setAlternatingRowColors(True)
        self.assigned_list.setObjectName("assigned_list")
        self.gridLayout.addWidget(self.assigned_list, 3, 0, 1, 4)
        self.faculty_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.faculty_combobox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.faculty_combobox.setFont(font)
        self.faculty_combobox.setObjectName("faculty_combobox")
        self.gridLayout.addWidget(self.faculty_combobox, 2, 0, 1, 1)
        self.semester_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.semester_combobox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.semester_combobox.setFont(font)
        self.semester_combobox.setObjectName("semester_combobox")
        self.gridLayout.addWidget(self.semester_combobox, 2, 1, 1, 1)
        self.subject_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.subject_combobox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.subject_combobox.setFont(font)
        self.subject_combobox.setObjectName("subject_combobox")
        self.gridLayout.addWidget(self.subject_combobox, 2, 3, 1, 1)
        self.section_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.section_combobox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.section_combobox.setFont(font)
        self.section_combobox.setObjectName("section_combobox")
        self.gridLayout.addWidget(self.section_combobox, 2, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        window2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 920, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        window2.setMenuBar(self.menubar)
        self.actionSave = QtWidgets.QAction(window2)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.setShortcut("Ctrl+S")
        self.actionSaveAs = QtWidgets.QAction(window2)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionSaveAs.setShortcut("Ctrl+Shift+S")
        self.actionLoad = QtWidgets.QAction(window2)
        self.actionLoad.setObjectName("actionLoad")
        self.actionLoad.setShortcut("Ctrl+L")
        self.actionExit = QtWidgets.QAction(window2)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(window2)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout_2 = QtWidgets.QAction(window2)
        self.actionAbout_2.setObjectName("actionAbout_2")
        self.actionClear_All = QtWidgets.QAction(window2)
        self.actionClear_All.setObjectName("actionClear_All")
        self.actionClear_All.setShortcut("Ctrl+R")
        self.actionSet_Year_Department = QtWidgets.QAction(window2)
        self.actionSet_Year_Department.setObjectName("actionSet_Year_Department")
        self.aboutMenu = QtWidgets.QAction(window2)
        self.aboutMenu.setObjectName("aboutMenu")
        self.LicenseMenu = QtWidgets.QAction(window2)
        self.LicenseMenu.setObjectName("LicenseMenu")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSet_Year_Department)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClear_All)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.aboutMenu)
        self.menuHelp.addAction(self.LicenseMenu)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(window2)
        QtCore.QMetaObject.connectSlotsByName(window2)
        window2.setTabOrder(self.faculty_combobox, self.semester_combobox)
        window2.setTabOrder(self.semester_combobox, self.section_combobox)
        window2.setTabOrder(self.section_combobox, self.subject_combobox)
        window2.setTabOrder(self.subject_combobox, self.assignBtn)
        window2.setTabOrder(self.assignBtn, self.undoBtn)
        window2.setTabOrder(self.undoBtn, self.assigned_list)
        window2.setTabOrder(self.assigned_list, self.backBtn)
        window2.setTabOrder(self.backBtn, self.nextBtn)

    def retranslateUi(self, window2):
        _translate = QtCore.QCoreApplication.translate
        window2.setWindowTitle(_translate("window2", "TimeTable Generator"))
        self.assignBtn.setText(_translate("window2", "Assign"))
        self.undoBtn.setText(_translate("window2", "Undo"))
        self.backBtn.setText(_translate("window2", "Back"))
        self.nextBtn.setText(_translate("window2", "Next"))
        self.label_3.setText(_translate("window2", "Semester:"))
        self.label_4.setText(_translate("window2", "Section:"))
        self.label_5.setText(_translate("window2", "Subject:"))
        self.label.setText(_translate("window2", "Faculty Assignment"))
        self.label_2.setText(_translate("window2", "Faculty:"))
        self.menuFile.setTitle(_translate("window2", "File"))
        self.menuHelp.setTitle(_translate("window2", "Help"))
        self.actionSave.setText(_translate("window2", "Save"))
        self.actionSaveAs.setText(_translate("window2", "Save As"))
        self.actionLoad.setText(_translate("window2", "Load"))
        self.actionExit.setText(_translate("window2", "Exit"))
        self.actionAbout.setText(_translate("window2", "About"))
        self.actionAbout_2.setText(_translate("window2", "About"))
        self.actionSet_Year_Department.setText(_translate("window2", "Set Year/Department"))
        self.actionClear_All.setText(_translate("window2", "Clear All"))
        self.aboutMenu.setText(_translate("window2", "About"))
        self.LicenseMenu.setText(_translate("window", "License"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window2 = QtWidgets.QMainWindow()
    ui = Ui_window2()
    ui.setupUi(window2)
    window2.show()
    sys.exit(app.exec_())

