from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        font = QtGui.QFont()
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet("#stackedWidget {\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #666666,\n"
"        stop:0.6 #4d4d4d,\n"
"        stop:1 #333333\n"
"    );\n"
"}\n"
"QLabel {color: black;}\n"
"QPushButton {color:black;}"
"QLineEdit {color:black;}")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.stackedWidget.setObjectName("stackedWidget")

        self.menuPage()

        self.statisticsPage()

        self.gamePage()

        self.registerPage()

        self.logInPage()

        self.resultPage()

        self.verticalLayout_5.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logInBtn.setText(_translate("MainWindow", "GİRİŞ YAP"))
        self.registerBtn.setText(_translate("MainWindow", "KAYIT OL"))
        self.mainMenuLabel.setText(_translate("MainWindow", "SPORCU\n"
"KART OYUNU"))
        self.difficultyBtn.setText(_translate("MainWindow", "KOLAY"))
        self.playGameBtn.setText(_translate("MainWindow", "OYUNA BAŞLA"))
        self.statisticsBtn.setText(_translate("MainWindow", "İSTATİSTİKLER"))
        self.userNameLabel.setText(_translate("MainWindow", "OYUNCU ADI"))
        self.difficultyLabel.setText(_translate("MainWindow", "ZORLUK DERECESİ"))
        self.pointLabel.setText(_translate("MainWindow", "PUANI"))
        self.PCLabel.setText(_translate("MainWindow", "BİLGİSAYAR"))
        self.deckBtn.setText(_translate("MainWindow", "DESTEM"))
        self.label_5.setText(_translate("MainWindow", "VS"))
        self.endTourBtn.setText(_translate("MainWindow", "TURU BİTİR"))
        self.youLabel.setText(_translate("MainWindow", "SEN"))
        self.confirmBtn.setText(_translate("MainWindow", "ONAYLA"))
        self.label_3.setText(_translate("MainWindow", "Kullanıcı Adı:"))
        self.registerLabel.setText(_translate("MainWindow", "KAYIT OL"))
        self.label_2.setText(_translate("MainWindow", "Şifre:"))
        self.label_9.setText(_translate("MainWindow", "Kullanıcı Adı:"))
        self.registerLabel_5.setText(_translate("MainWindow", "GİRİŞ YAP"))
        self.confirmBtn_5.setText(_translate("MainWindow", "ONAYLA"))
        self.label_4.setText(_translate("MainWindow", "Şifre:"))
        self.resultLabel.setText(_translate("MainWindow", "SONUÇ EKRANI"))
        self.label_8.setText(_translate("MainWindow", "TOPLAM PUAN:"))
        self.label_7.setText(_translate("MainWindow", "125"))
        self.basicAttributeLabel.setText(_translate("MainWindow", "Temel Özellik"))
        self.basicAttributeValue.setText(_translate("MainWindow", "+32"))
        self.moralBonusLabel.setText(_translate("MainWindow", "Moral Bonusu"))
        self.moralBonusValue.setText(_translate("MainWindow", "+12"))
        self.specialSkillBonusLabel.setText(_translate("MainWindow", "Özel Yetenek Bonusu"))
        self.specialSkillBonusValue.setText(_translate("MainWindow", "+5"))
        self.energyLossPunishmentLabel.setText(_translate("MainWindow", "Enerji kaybı Cezası"))
        self.energyLossPunishmentValue.setText(_translate("MainWindow", "-23"))
        self.levelBonusLabel.setText(_translate("MainWindow", "Seviye Bonusu"))
        self.levelBonusLabelValue.setText(_translate("MainWindow", "+21"))
        self.goBtn.setText(_translate("MainWindow", "Devam Et"))

    def menuPage(self):
        self.menuPage = QtWidgets.QWidget()
        self.menuPage.setStyleSheet("")
        self.menuPage.setObjectName("menuPage")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.menuPage)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTop|QtCore.Qt.AlignmentFlag.AlignTrailing)
        self.formLayout.setObjectName("formLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget = QtWidgets.QWidget(parent=self.menuPage)
        self.widget.setObjectName("widget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.logInBtn = QtWidgets.QPushButton(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logInBtn.sizePolicy().hasHeightForWidth())
        self.logInBtn.setSizePolicy(sizePolicy)
        self.logInBtn.setMinimumSize(QtCore.QSize(100, 50))
        self.logInBtn.setMaximumSize(QtCore.QSize(70, 50))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        self.logInBtn.setFont(font)
        self.logInBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.logInBtn.setStyleSheet("#logInBtn {\n"
"    border-radius: 10px;\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #e60000,\n"
"        stop:0.6 #b30000,\n"
"        stop:1 #800000\n"
"    );\n"
"}\n"
"#logInBtn:hover {\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #cc0000,\n"
"        stop:0.6 #990000,\n"
"        stop:1 #660000\n"
"    );\n"
"}")
        self.logInBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.logInBtn.setObjectName("logInBtn")
        self.verticalLayout_7.addWidget(self.logInBtn)
        self.registerBtn = QtWidgets.QPushButton(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerBtn.sizePolicy().hasHeightForWidth())
        self.registerBtn.setSizePolicy(sizePolicy)
        self.registerBtn.setMinimumSize(QtCore.QSize(100, 50))
        self.registerBtn.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        self.registerBtn.setFont(font)
        self.registerBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.registerBtn.setStyleSheet("#registerBtn {\n"
"    border-radius: 10px;\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #00cc00,\n"
"        stop:0.6 #009900,\n"
"        stop:1 #006600\n"
"    );\n"
"}\n"
"#registerBtn:hover {\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #00b300,\n"
"        stop:0.6 #008000,\n"
"        stop:1 #004d00\n"
"    );\n"
"}")
        self.registerBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.registerBtn.setObjectName("registerBtn")
        self.verticalLayout_7.addWidget(self.registerBtn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.verticalLayout_6.addWidget(self.widget)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.mainMenuLabel = QtWidgets.QLabel(parent=self.menuPage)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(57)
        font.setBold(True)
        self.mainMenuLabel.setFont(font)
        self.mainMenuLabel.setStyleSheet("")
        self.mainMenuLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mainMenuLabel.setObjectName("mainMenuLabel")
        self.horizontalLayout_2.addWidget(self.mainMenuLabel)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_2 = QtWidgets.QWidget(parent=self.menuPage)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.settingsBtn = QtWidgets.QPushButton(parent=self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsBtn.sizePolicy().hasHeightForWidth())
        self.settingsBtn.setSizePolicy(sizePolicy)
        self.settingsBtn.setMinimumSize(QtCore.QSize(70, 66))
        self.settingsBtn.setMaximumSize(QtCore.QSize(70, 66))
        self.settingsBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.settingsBtn.setAcceptDrops(False)
        self.settingsBtn.setStyleSheet("#settingsBtn {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"#settingsBtn:hover {\n"
"background-color: qradialgradient(\n"
"cx:0.5, cy:0.5, radius:0.8,\n"
"fx:0.5, fy:0.5,\n"
"stop:0 #333333,\n"
"stop:0.6 #4d4d4d,\n"
"stop:1 #666666\n"
");\n"
"}")
        self.settingsBtn.clicked.connect(self.clickedSettingBtn)
        self.settingsBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("GUI\\icons\\settingsIcon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.settingsBtn.setIcon(icon)
        self.settingsBtn.setIconSize(QtCore.QSize(64, 64))
        self.settingsBtn.setCheckable(True)
        self.settingsBtn.setFlat(False)
        self.settingsBtn.setObjectName("settingsBtn")
        self.verticalLayout_9.addWidget(self.settingsBtn, 0, QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTop)
        self.verticalLayout_3.addWidget(self.widget_2)
        self.settingsWidget = QtWidgets.QWidget(parent=self.menuPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsWidget.sizePolicy().hasHeightForWidth())
        self.settingsWidget.setSizePolicy(sizePolicy)
        self.settingsWidget.setMinimumSize(QtCore.QSize(90, 180))
        self.settingsWidget.setMaximumSize(QtCore.QSize(90, 180))
        self.settingsWidget.setObjectName("settingsWidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.settingsWidget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.soundBtn = QtWidgets.QPushButton(parent=self.settingsWidget)
        self.settingsWidget.hide()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.soundBtn.sizePolicy().hasHeightForWidth())
        self.soundBtn.setSizePolicy(sizePolicy)
        self.soundBtn.setMinimumSize(QtCore.QSize(70, 64))
        self.soundBtn.setMaximumSize(QtCore.QSize(70, 64))
        self.soundBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.soundBtn.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.soundBtn.setStyleSheet("#soundBtn {\n"
"    border: none;\n"
"    border-radius: 30px;\n"
"}\n"
"#soundBtn:hover {\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #262626,\n"
"        stop:0.6 #4d4d4d,\n"
"        stop:1 #666666\n"
"    );\n"
"}")
        self.soundBtn.clicked.connect(self.toggleSoundIcon)
        self.soundBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("GUI\\icons\\openVolumeIcon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.soundBtn.setIcon(icon1)
        self.soundBtn.setIconSize(QtCore.QSize(64, 64))
        self.soundBtn.setCheckable(True)
        self.soundBtn.setObjectName("soundBtn")
        self.verticalLayout_8.addWidget(self.soundBtn)
        self.difficultyBtn = QtWidgets.QPushButton(parent=self.settingsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.difficultyBtn.sizePolicy().hasHeightForWidth())
        self.difficultyBtn.setSizePolicy(sizePolicy)
        self.difficultyBtn.setMinimumSize(QtCore.QSize(70, 64))
        self.difficultyBtn.setMaximumSize(QtCore.QSize(70, 64))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        self.difficultyBtn.setFont(font)
        self.difficultyBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.difficultyBtn.setStyleSheet("#difficultyBtn {\n"
"    border-radius: 30px;\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #33cc33,\n"
"        stop:1 #29a329\n"
"    );\n"
"}\n"
"#difficultyBtn:hover {\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #2eb82e,\n"
"        stop:1 #248f24\n"
"    );;\n"
"}")
        self.difficultyBtn.setCheckable(True)
        self.difficultyBtn.clicked.connect(self.toggleDifficultyBtn)
        self.difficultyBtn.setObjectName("difficultyBtn")
        self.verticalLayout_8.addWidget(self.difficultyBtn)
        self.verticalLayout_3.addWidget(self.settingsWidget, 0, QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTop)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 30)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.playGameBtn = QtWidgets.QPushButton(parent=self.menuPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playGameBtn.sizePolicy().hasHeightForWidth())
        self.playGameBtn.setSizePolicy(sizePolicy)
        self.playGameBtn.setMinimumSize(QtCore.QSize(400, 70))
        self.playGameBtn.setMaximumSize(QtCore.QSize(800, 140))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(24)
        font.setBold(False)
        self.playGameBtn.setFont(font)
        self.playGameBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.playGameBtn.setStyleSheet("#playGameBtn {\n"
"    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #258e25,\n"
"        stop:1 #1a651a\n"
"    );\n"
"}\n"
"#playGameBtn:hover {\n"
"        background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #1f7a1f,\n"
"        stop:1 #155115\n"
"    );\n"
"}")
        self.playGameBtn.setAutoDefault(False)
        self.playGameBtn.setDefault(False)
        self.playGameBtn.setObjectName("playGameBtn")
        self.verticalLayout_2.addWidget(self.playGameBtn, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.statisticsBtn = QtWidgets.QPushButton(parent=self.menuPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statisticsBtn.sizePolicy().hasHeightForWidth())
        self.statisticsBtn.setSizePolicy(sizePolicy)
        self.statisticsBtn.setMinimumSize(QtCore.QSize(400, 70))
        self.statisticsBtn.setMaximumSize(QtCore.QSize(800, 140))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(24)
        font.setBold(False)
        self.statisticsBtn.setFont(font)
        self.statisticsBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.statisticsBtn.setStyleSheet("#statisticsBtn {\n"
"    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #b3b300,\n"
"        stop:1 #808000\n"
"    );\n"
"}\n"
"#statisticsBtn:hover {\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #999900,\n"
"        stop:1 #666600\n"
"    );\n"
"}")
        self.statisticsBtn.setObjectName("statisticsBtn")
        self.verticalLayout_2.addWidget(self.statisticsBtn, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.formLayout)
        self.stackedWidget.addWidget(self.menuPage)

    def statisticsPage(self):
        self.statisticsPage = QtWidgets.QWidget()
        self.statisticsPage.setObjectName("statisticsPage")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.statisticsPage)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.backBtn_2 = QtWidgets.QPushButton(parent=self.statisticsPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.backBtn_2.sizePolicy().hasHeightForWidth())
        self.backBtn_2.setSizePolicy(sizePolicy)
        self.backBtn_2.setMinimumSize(QtCore.QSize(60, 60))
        self.backBtn_2.setMaximumSize(QtCore.QSize(60, 60))
        self.backBtn_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.backBtn_2.setStyleSheet("#backBtn_2 {\n"
"    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #669999,\n"
"        stop:1 #a3c2c2\n"
"    );\n"
"}\n"
"#backBtn_2:hover {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #5c8a8a,\n"
"        stop:1 #94b8b8\n"
"    );\n"
"}")
        self.backBtn_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.backBtn_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("GUI\\icons\\backArrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.backBtn_2.setIcon(icon2)
        self.backBtn_2.setIconSize(QtCore.QSize(64, 64))
        self.backBtn_2.setObjectName("backBtn_2")
        self.verticalLayout_13.addWidget(self.backBtn_2)
        self.statisticsScrollArea = QtWidgets.QScrollArea(parent=self.statisticsPage)
        self.statisticsScrollArea.setMinimumSize(QtCore.QSize(1300, 900))
        self.statisticsScrollArea.setMaximumSize(QtCore.QSize(1300, 900))
        self.statisticsScrollArea.setStyleSheet("")
        self.statisticsScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.statisticsScrollArea.setWidgetResizable(True)
        self.statisticsScrollArea.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.statisticsScrollArea.setObjectName("statisticsScrollArea")
        self.statisticsScrollAreaWidgetContents = QtWidgets.QWidget()
        self.statisticsScrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1299, 877))
        self.statisticsScrollAreaWidgetContents.setStyleSheet("#statisticsScrollAreaWidgetContents {\n"
"    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #001e80,\n"
"        stop:0.6 #001866,\n"
"        stop:1 #00061a\n"
"    );\n"
"}")
        self.statisticsScrollAreaWidgetContents.setObjectName("statisticsScrollAreaWidgetContents")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.statisticsScrollAreaWidgetContents)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.statisticsLabels = QtWidgets.QFrame(parent=self.statisticsScrollAreaWidgetContents)
        self.statisticsLabels.setMinimumSize(QtCore.QSize(1277, 67))
        self.statisticsLabels.setMaximumSize(QtCore.QSize(1277, 67))
        self.statisticsLabels.setStyleSheet("#statisticsLabels {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #002db3,\n"
"        stop:0.6 #002080,\n"
"        stop:1 #00134d\n"
"    );\n"
"}")
        self.statisticsLabels.setObjectName("statisticsLabels")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.statisticsLabels)
        self.horizontalLayout_3.setSpacing(300)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.userNameLabel = QtWidgets.QLabel(parent=self.statisticsLabels)
        self.userNameLabel.setMinimumSize(QtCore.QSize(221, 45))
        self.userNameLabel.setMaximumSize(QtCore.QSize(221, 69))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        font.setBold(True)
        self.userNameLabel.setFont(font)
        self.userNameLabel.setStyleSheet("#userNameLabel {\n"
"    border: 2px solid blue;\n"
"    border-radius: 5px;\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #b3c6ff,\n"
"        stop:0.6 #809fff,\n"
"        stop:1 #4d79ff\n"
"    );\n"
"}")
        self.userNameLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.userNameLabel.setObjectName("userNameLabel")
        self.horizontalLayout_3.addWidget(self.userNameLabel)
        self.difficultyLabel = QtWidgets.QLabel(parent=self.statisticsLabels)
        self.difficultyLabel.setMaximumSize(QtCore.QSize(320, 69))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        font.setBold(True)
        self.difficultyLabel.setFont(font)
        self.difficultyLabel.setStyleSheet("#difficultyLabel {\n"
"    border: 2px solid blue;\n"
"    border-radius: 5px;\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #b3c6ff,\n"
"        stop:0.6 #809fff,\n"
"        stop:1 #4d79ff\n"
"    );\n"
"}\n"
"")
        self.difficultyLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.difficultyLabel.setObjectName("difficultyLabel")
        self.horizontalLayout_3.addWidget(self.difficultyLabel)
        self.pointLabel = QtWidgets.QLabel(parent=self.statisticsLabels)
        self.pointLabel.setMinimumSize(QtCore.QSize(114, 45))
        self.pointLabel.setMaximumSize(QtCore.QSize(114, 69))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        font.setBold(True)
        self.pointLabel.setFont(font)
        self.pointLabel.setStyleSheet("#pointLabel {\n"
"    border: 2px solid blue;\n"
"    border-radius: 5px;\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #b3c6ff,\n"
"        stop:0.6 #809fff,\n"
"        stop:1 #4d79ff\n"
"    );\n"
"}")
        self.pointLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.pointLabel.setObjectName("pointLabel")
        self.horizontalLayout_3.addWidget(self.pointLabel)
        self.verticalLayout_10.addWidget(self.statisticsLabels, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.verticalLayout_10.addLayout(self.verticalLayout)
        self.statisticsScrollArea.setWidget(self.statisticsScrollAreaWidgetContents)
        self.verticalLayout_13.addWidget(self.statisticsScrollArea, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.stackedWidget.addWidget(self.statisticsPage)

    def gamePage(self):
        self.gamePage = QtWidgets.QWidget()
        self.gamePage.setObjectName("gamePage")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gamePage)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.playerAreaWidget = QtWidgets.QWidget(parent=self.gamePage)
        self.playerAreaWidget.setObjectName("playerAreaWidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.playerAreaWidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame = QtWidgets.QFrame(parent=self.playerAreaWidget)
        self.frame.setMinimumSize(QtCore.QSize(360, 620))
        self.frame.setMaximumSize(QtCore.QSize(360, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_7.addWidget(self.frame)
        self.gridLayout_3.addWidget(self.playerAreaWidget, 2, 2, 1, 1)
        self.PCLabel = QtWidgets.QLabel(parent=self.gamePage)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(30)
        font.setBold(False)
        self.PCLabel.setFont(font)
        self.PCLabel.setStyleSheet("#PCLabel {\n"
"    color: #800000;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}")
        self.PCLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.PCLabel.setObjectName("PCLabel")
        self.gridLayout_3.addWidget(self.PCLabel, 0, 5, 1, 1)
        self.PCAreaWidget = QtWidgets.QWidget(parent=self.gamePage)
        self.PCAreaWidget.setObjectName("PCAreaWidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.PCAreaWidget)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_2 = QtWidgets.QFrame(parent=self.PCAreaWidget)
        self.frame_2.setMinimumSize(QtCore.QSize(360, 620))
        self.frame_2.setMaximumSize(QtCore.QSize(360, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_8.addWidget(self.frame_2, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.gridLayout_3.addWidget(self.PCAreaWidget, 2, 5, 1, 1)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(parent=self.gamePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget_2.sizePolicy().hasHeightForWidth())
        self.stackedWidget_2.setSizePolicy(sizePolicy)
        self.stackedWidget_2.setMaximumSize(QtCore.QSize(400, 790))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.deckBtn = QtWidgets.QPushButton(parent=self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(250)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.deckBtn.sizePolicy().hasHeightForWidth())
        self.deckBtn.setSizePolicy(sizePolicy)
        self.deckBtn.setMinimumSize(QtCore.QSize(250, 60))
        self.deckBtn.setMaximumSize(QtCore.QSize(250, 60))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.deckBtn.setFont(font)
        self.deckBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.deckBtn.setStyleSheet("#deckBtn {\n"
"    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #6600cc,\n"
"        stop:1 #400080\n"
"    );\n"
"}\n"
"#deckBtn:hover {\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #5900b3,\n"
"        stop:1 #330066\n"
"    );\n"
"}")
        self.deckBtn.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(1))
        self.deckBtn.setObjectName("deckBtn")
        self.verticalLayout_26.addWidget(self.deckBtn, 0, QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.stackedWidget_2.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.widget_3 = QtWidgets.QWidget(parent=self.page_2)
        self.widget_3.setStyleSheet("#widget_3 {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #5c5c8a,\n"
"        stop:0.6 #47476b,\n"
"        stop:1 #33334d\n"
"    );\n"
"}")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.backBtn_8 = QtWidgets.QPushButton(parent=self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backBtn_8.sizePolicy().hasHeightForWidth())
        self.backBtn_8.setSizePolicy(sizePolicy)
        self.backBtn_8.setMinimumSize(QtCore.QSize(44, 44))
        self.backBtn_8.setMaximumSize(QtCore.QSize(44, 44))
        self.backBtn_8.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.backBtn_8.setStyleSheet("#backBtn_8 {\n"
"    border: none;\n"
"}\n"
"#backBtn_8:hover {\n"
"    border-radius: 10px;\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #47476b,\n"
"        stop:0.6 #5c5c8a,\n"
"        stop:1 #7575a3\n"
"    );\n"
"}")
        self.backBtn_8.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(0))
        self.backBtn_8.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("GUI\\icons\\arrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.backBtn_8.setIcon(icon3)
        self.backBtn_8.setIconSize(QtCore.QSize(40, 40))
        self.backBtn_8.setObjectName("backBtn_8")
        self.horizontalLayout_9.addWidget(self.backBtn_8, 0, QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.verticalLayout_27.addWidget(self.widget_3)
        self.scrollArea_2 = QtWidgets.QScrollArea(parent=self.page_2)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.deckScrollAreaWidgetContents = QtWidgets.QWidget()
        self.deckScrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 376, 693))
        self.deckScrollAreaWidgetContents.setStyleSheet("#deckScrollAreaWidgetContents {\n"
"    border: 1px solid black;\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #004080,\n"
"        stop:0.6 #00264d,\n"
"        stop:1 #000d1a\n"
"    );\n"
"}")
        self.deckScrollAreaWidgetContents.setObjectName("deckScrollAreaWidgetContents")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.deckScrollAreaWidgetContents)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.scrollArea_2.setWidget(self.deckScrollAreaWidgetContents)
        self.verticalLayout_27.addWidget(self.scrollArea_2)
        self.stackedWidget_2.addWidget(self.page_2)
        self.gridLayout_3.addWidget(self.stackedWidget_2, 2, 0, 1, 1)
        self.backBtn = QtWidgets.QPushButton(parent=self.gamePage)
        self.backBtn.setMinimumSize(QtCore.QSize(60, 60))
        self.backBtn.setMaximumSize(QtCore.QSize(60, 60))
        self.backBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.backBtn.setStyleSheet("#backBtn {\n"
"    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #669999,\n"
"        stop:1 #a3c2c2\n"
"    );\n"
"}\n"
"#backBtn:hover {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #5c8a8a,\n"
"        stop:1 #94b8b8\n"
"    );\n"
"}")
        self.backBtn.clicked.connect(self.clickedGamePageBackBtn)
        self.backBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("GUI\\icons\\backArrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.backBtn.setIcon(icon2)
        self.backBtn.setIconSize(QtCore.QSize(64, 64))
        self.backBtn.setObjectName("backBtn")
        self.gridLayout_3.addWidget(self.backBtn, 0, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(parent=self.gamePage)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 1, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.gamePage)
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(65)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 2, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 2, 6, 1, 1)
        self.endTourBtn = QtWidgets.QPushButton(parent=self.gamePage)
        self.endTourBtn.setMinimumSize(QtCore.QSize(300, 100))
        self.endTourBtn.setMaximumSize(QtCore.QSize(300, 100))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(20)
        font.setBold(False)
        self.endTourBtn.setFont(font)
        self.endTourBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.endTourBtn.setStyleSheet("#endTourBtn {\n"
"    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #006600,\n"
"        stop:1 #00cc00\n"
"    );\n"
"}\n"
"#endTourBtn:hover {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #004d00,\n"
"        stop:1 #00b300\n"
"    );\n"
"}\n"
"")
        self.endTourBtn.setObjectName("endTourBtn")

        self.gridLayout_3.addWidget(self.endTourBtn, 2, 6, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignBottom)

        self.youLabel = QtWidgets.QLabel(parent=self.gamePage)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        self.youLabel.setFont(font)
        self.youLabel.setStyleSheet("#youLabel {\n"
"    color: #000066;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}")
        self.youLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.youLabel.setObjectName("youLabel")
        self.gridLayout_3.addWidget(self.youLabel, 0, 2, 1, 1)
        self.line = QtWidgets.QFrame(parent=self.gamePage)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 1, 2, 1, 1)
        self.line_9 = QtWidgets.QFrame(parent=self.gamePage)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_9.setLineWidth(2)
        self.line_9.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_9.setObjectName("line_9")
        self.gridLayout_3.addWidget(self.line_9, 2, 1, 1, 1)
        self.stackedWidget.addWidget(self.gamePage)

    def registerPage(self):
        self.registerPage = QtWidgets.QWidget()
        self.registerPage.setObjectName("registerPage")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.registerPage)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.registerWidget = QtWidgets.QWidget(parent=self.registerPage)
        self.registerWidget.setMinimumSize(QtCore.QSize(580, 400))
        self.registerWidget.setMaximumSize(QtCore.QSize(580, 400))
        self.registerWidget.setStyleSheet("#registerWidget {\n"
"    border: 1px solid black;\n"
"    border-radius: 15px;\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #3873ad,\n"
"        stop:0.6 #2c5987,\n"
"        stop:1 #1f4060\n"
"    );\n"
"}")
        self.registerWidget.setObjectName("registerWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.registerWidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem4, 4, 0, 1, 1)
        self.confirmBtn = QtWidgets.QPushButton(parent=self.registerWidget)
        self.confirmBtn.setMinimumSize(QtCore.QSize(120, 60))
        self.confirmBtn.setMaximumSize(QtCore.QSize(120, 60))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(12)
        font.setBold(True)
        self.confirmBtn.setFont(font)
        self.confirmBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.confirmBtn.setStyleSheet("#confirmBtn {\n"
"    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #009900,\n"
"        stop:1 #00e600\n"
"    );\n"
"}\n"
"#confirmBtn:hover {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #008000,\n"
"        stop:1 #00cc00\n"
"    );\n"
"}")
        self.confirmBtn.setObjectName("confirmBtn")
        self.gridLayout.addWidget(self.confirmBtn, 7, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.backBtn_9 = QtWidgets.QPushButton(parent=self.registerWidget)
        self.backBtn_9.setMinimumSize(QtCore.QSize(60, 60))
        self.backBtn_9.setMaximumSize(QtCore.QSize(60, 60))
        self.backBtn_9.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.backBtn_9.setStyleSheet("#backBtn_9 {\n"
"    border-radius: 10px;\n"
"}\n"
"#backBtn_9:hover {\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #254d74,\n"
"        stop:0.6 #31669b,\n"
"        stop:1 #3d80c2\n"
"    );\n"
"}")
        self.backBtn_9.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.backBtn_9.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("GUI\\icons\\backArrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.backBtn_9.setIcon(icon2)
        self.backBtn_9.setIconSize(QtCore.QSize(64, 64))
        self.backBtn_9.setObjectName("backBtn_9")
        self.gridLayout.addWidget(self.backBtn_9, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.registerWidget)
        self.label_3.setMinimumSize(QtCore.QSize(130, 30))
        self.label_3.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro Blac")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.registerUsernameInput = QtWidgets.QLineEdit(parent=self.registerWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerUsernameInput.sizePolicy().hasHeightForWidth())
        self.registerUsernameInput.setSizePolicy(sizePolicy)
        self.registerUsernameInput.setMinimumSize(QtCore.QSize(160, 40))
        self.registerUsernameInput.setMaximumSize(QtCore.QSize(160, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(12)
        font.setBold(True)
        self.registerUsernameInput.setFont(font)
        self.registerUsernameInput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.registerUsernameInput.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.registerUsernameInput)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.gridLayout.addItem(spacerItem6, 8, 1, 1, 1)
        self.registerLabel = QtWidgets.QLabel(parent=self.registerWidget)
        self.registerLabel.setMinimumSize(QtCore.QSize(310, 110))
        self.registerLabel.setMaximumSize(QtCore.QSize(310, 110))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(38)
        font.setItalic(False)
        font.setBold(True)
        self.registerLabel.setFont(font)
        self.registerLabel.setStyleSheet("#registerLabel {\n"
"    border: none;\n"
"    color: #000066;\n"
"}")
        self.registerLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.registerLabel.setObjectName("registerLabel")
        self.gridLayout.addWidget(self.registerLabel, 0, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(parent=self.registerWidget)
        self.label_2.setMinimumSize(QtCore.QSize(130, 30))
        self.label_2.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro Blac")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.registerPasswordInput = QtWidgets.QLineEdit(parent=self.registerWidget)
        self.registerPasswordInput.setMinimumSize(QtCore.QSize(160, 40))
        self.registerPasswordInput.setMaximumSize(QtCore.QSize(160, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(12)
        font.setBold(True)
        self.registerPasswordInput.setFont(font)
        self.registerPasswordInput.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.registerPasswordInput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.registerPasswordInput.setObjectName("lineEdit_2")
        self.horizontalLayout_5.addWidget(self.registerPasswordInput)
        self.gridLayout.addLayout(self.horizontalLayout_5, 6, 1, 1, 1)
        self.verticalLayout_12.addWidget(self.registerWidget, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.stackedWidget.addWidget(self.registerPage)

    def logInPage(self):
        self.logInPage = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setBold(True)
        self.logInPage.setFont(font)
        self.logInPage.setObjectName("logInPage")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.logInPage)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.logInWidget = QtWidgets.QWidget(parent=self.logInPage)
        self.logInWidget.setMinimumSize(QtCore.QSize(580, 400))
        self.logInWidget.setMaximumSize(QtCore.QSize(580, 400))
        self.logInWidget.setStyleSheet("#logInWidget {\n"
"    border: 1px solid black;\n"
"    border-radius: 15px;\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #3873ad,\n"
"        stop:0.6 #2c5987,\n"
"        stop:1 #1f4060\n"
"    );\n"
"}")
        self.logInWidget.setObjectName("logInWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.logInWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_9 = QtWidgets.QLabel(parent=self.logInWidget)
        self.label_9.setMinimumSize(QtCore.QSize(130, 30))
        self.label_9.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro Blac")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.logInUsernameInput = QtWidgets.QLineEdit(parent=self.logInWidget)
        self.logInUsernameInput.setMinimumSize(QtCore.QSize(160, 40))
        self.logInUsernameInput.setMaximumSize(QtCore.QSize(160, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(12)
        font.setBold(True)
        self.logInUsernameInput.setFont(font)
        self.logInUsernameInput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.logInUsernameInput.setObjectName("lineEdit_5")
        self.horizontalLayout_10.addWidget(self.logInUsernameInput)
        self.gridLayout_2.addLayout(self.horizontalLayout_10, 2, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.gridLayout_2.addItem(spacerItem7, 5, 1, 1, 1)
        self.registerLabel_5 = QtWidgets.QLabel(parent=self.logInWidget)
        self.registerLabel_5.setMinimumSize(QtCore.QSize(350, 110))
        self.registerLabel_5.setMaximumSize(QtCore.QSize(350, 110))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(38)
        font.setBold(True)
        font.setItalic(False)
        self.registerLabel_5.setFont(font)
        self.registerLabel_5.setStyleSheet("#registerLabel_5 {\n"
"    border: none;\n"
"    color: #000066;\n"
"}")
        self.registerLabel_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.registerLabel_5.setObjectName("registerLabel_5")
        self.gridLayout_2.addWidget(self.registerLabel_5, 0, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.backBtn_10 = QtWidgets.QPushButton(parent=self.logInWidget)
        self.backBtn_10.setMinimumSize(QtCore.QSize(60, 60))
        self.backBtn_10.setMaximumSize(QtCore.QSize(60, 60))
        self.backBtn_10.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.backBtn_10.setStyleSheet("#backBtn_10 {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"#backBtn_10:hover {\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #254d74,\n"
"        stop:0.6 #31669b,\n"
"        stop:1 #3d80c2\n"
"    );\n"
"}\n"
"")
        self.backBtn_10.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.backBtn_10.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("GUI\\icons\\backArrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.backBtn_10.setIcon(icon2)
        self.backBtn_10.setIconSize(QtCore.QSize(64, 64))
        self.backBtn_10.setObjectName("backBtn_10")
        self.gridLayout_2.addWidget(self.backBtn_10, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 1, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 0, 2, 1, 1)
        self.confirmBtn_5 = QtWidgets.QPushButton(parent=self.logInWidget)
        self.confirmBtn_5.setMinimumSize(QtCore.QSize(120, 60))
        self.confirmBtn_5.setMaximumSize(QtCore.QSize(120, 60))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(12)
        font.setBold(True)
        self.confirmBtn_5.setFont(font)
        self.confirmBtn_5.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.confirmBtn_5.setStyleSheet("#confirmBtn_5 {\n"
"    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #009900,\n"
"        stop:1 #00e600\n"
"    );\n"
"}\n"
"#confirmBtn_5:hover {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #008000,\n"
"        stop:1 #00cc00\n"
"    );\n"
"}")
        self.confirmBtn_5.setObjectName("confirmBtn_5")
        self.gridLayout_2.addWidget(self.confirmBtn_5, 4, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(parent=self.logInWidget)
        self.label_4.setMinimumSize(QtCore.QSize(130, 30))
        self.label_4.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro Blac")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.logInPasswordInput = QtWidgets.QLineEdit(parent=self.logInWidget)
        self.logInPasswordInput.setMinimumSize(QtCore.QSize(160, 40))
        self.logInPasswordInput.setMaximumSize(QtCore.QSize(160, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(12)
        font.setBold(True)
        self.logInPasswordInput.setFont(font)
        self.logInPasswordInput.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.logInPasswordInput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.logInPasswordInput.setObjectName("lineEdit_3")
        self.horizontalLayout_6.addWidget(self.logInPasswordInput)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 3, 1, 1, 1)
        self.verticalLayout_11.addWidget(self.logInWidget, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.stackedWidget.addWidget(self.logInPage)

    def resultPage(self):
        self.resultPage = QtWidgets.QWidget()
        self.resultPage.setObjectName("resultPage")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.resultPage)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.resultScrollArea = QtWidgets.QScrollArea(parent=self.resultPage)
        self.resultScrollArea.setMinimumSize(QtCore.QSize(570, 620))
        self.resultScrollArea.setMaximumSize(QtCore.QSize(570, 620))
        self.resultScrollArea.setStyleSheet("")
        self.resultScrollArea.setWidgetResizable(True)
        self.resultScrollArea.setObjectName("resultScrollArea")
        self.resultScrollAreaWidgetContents = QtWidgets.QWidget()
        self.resultScrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 568, 618))
        self.resultScrollAreaWidgetContents.setStyleSheet("#resultScrollAreaWidgetContents {\n"
"    border: 1px solid black;\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #48486a,\n"
"        stop:0.6 #34344c,\n"
"        stop:1 #1f1f2e\n"
"    );\n"
"}")
        self.resultScrollAreaWidgetContents.setObjectName("resultScrollAreaWidgetContents")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.resultScrollAreaWidgetContents)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.resultLabel = QtWidgets.QLabel(parent=self.resultScrollAreaWidgetContents)
        self.resultLabel.setMinimumSize(QtCore.QSize(537, 65))
        self.resultLabel.setMaximumSize(QtCore.QSize(537, 65))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(18)
        self.resultLabel.setFont(font)
        self.resultLabel.setStyleSheet("#resultLabel {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #5c5c8a,\n"
"        stop:0.6 #47476b,\n"
"        stop:1 #33334d\n"
"    );\n"
"}")
        self.resultLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resultLabel.setObjectName("resultLabel")
        self.verticalLayout_29.addWidget(self.resultLabel)
        self.line_8 = QtWidgets.QFrame(parent=self.resultScrollAreaWidgetContents)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_8.setLineWidth(2)
        self.line_8.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_29.addWidget(self.line_8)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_8 = QtWidgets.QLabel(parent=self.resultScrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_11.addWidget(self.label_8)
        self.label_7 = QtWidgets.QLabel(parent=self.resultScrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_11.addWidget(self.label_7)
        self.verticalLayout_29.addLayout(self.horizontalLayout_11)
        self.line_7 = QtWidgets.QFrame(parent=self.resultScrollAreaWidgetContents)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_7.setLineWidth(2)
        self.line_7.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_29.addWidget(self.line_7)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.basicAttributeWidget = QtWidgets.QWidget(parent=self.resultScrollAreaWidgetContents)
        self.basicAttributeWidget.setMinimumSize(QtCore.QSize(544, 66))
        self.basicAttributeWidget.setMaximumSize(QtCore.QSize(544, 66))
        self.basicAttributeWidget.setStyleSheet("#basicAttributeWidget {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #009900,\n"
"        stop:0.6 #008000,\n"
"        stop:1 #004d00\n"
"    );\n"
"}")
        self.basicAttributeWidget.setObjectName("basicAttributeWidget")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.basicAttributeWidget)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.basicAttributeLabel = QtWidgets.QLabel(parent=self.basicAttributeWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(16)
        font.setBold(False)
        self.basicAttributeLabel.setFont(font)
        self.basicAttributeLabel.setStyleSheet("#basicAttributeLabel {\n"
"    color: white;\n"
"}")
        self.basicAttributeLabel.setObjectName("basicAttributeLabel")
        self.horizontalLayout_13.addWidget(self.basicAttributeLabel)
        self.basicAttributeValue = QtWidgets.QLabel(parent=self.basicAttributeWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(18)
        font.setBold(False)
        self.basicAttributeValue.setFont(font)
        self.basicAttributeValue.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.basicAttributeValue.setObjectName("basicAttributeValue")
        self.horizontalLayout_13.addWidget(self.basicAttributeValue)
        self.horizontalLayout_12.addWidget(self.basicAttributeWidget)
        self.verticalLayout_29.addLayout(self.horizontalLayout_12)
        self.verticalLayout_30 = QtWidgets.QVBoxLayout()
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.moralBonusWidget = QtWidgets.QWidget(parent=self.resultScrollAreaWidgetContents)
        self.moralBonusWidget.setMinimumSize(QtCore.QSize(544, 66))
        self.moralBonusWidget.setMaximumSize(QtCore.QSize(544, 66))
        self.moralBonusWidget.setStyleSheet("#moralBonusWidget {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #009900,\n"
"        stop:0.6 #008000,\n"
"        stop:1 #004d00\n"
"    );\n"
"}")
        self.moralBonusWidget.setObjectName("moralBonusWidget")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.moralBonusWidget)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.moralBonusLabel = QtWidgets.QLabel(parent=self.moralBonusWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(16)
        font.setBold(False)
        self.moralBonusLabel.setFont(font)
        self.moralBonusLabel.setStyleSheet("#moralBonusLabel {\n"
"    color: white;\n"
"}")
        self.moralBonusLabel.setObjectName("moralBonusLabel")
        self.horizontalLayout_14.addWidget(self.moralBonusLabel)
        self.moralBonusValue = QtWidgets.QLabel(parent=self.moralBonusWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(18)
        self.moralBonusValue.setFont(font)
        self.moralBonusValue.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.moralBonusValue.setObjectName("moralBonusValue")
        self.horizontalLayout_14.addWidget(self.moralBonusValue)
        self.verticalLayout_30.addWidget(self.moralBonusWidget)
        self.verticalLayout_29.addLayout(self.verticalLayout_30)
        self.verticalLayout_31 = QtWidgets.QVBoxLayout()
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.specialSkillBonusWidget = QtWidgets.QWidget(parent=self.resultScrollAreaWidgetContents)
        self.specialSkillBonusWidget.setMinimumSize(QtCore.QSize(544, 66))
        self.specialSkillBonusWidget.setMaximumSize(QtCore.QSize(544, 65))
        self.specialSkillBonusWidget.setStyleSheet("#specialSkillBonusWidget {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #009900,\n"
"        stop:0.6 #008000,\n"
"        stop:1 #004d00\n"
"    );\n"
"}")
        self.specialSkillBonusWidget.setObjectName("specialSkillBonusWidget")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.specialSkillBonusWidget)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.specialSkillBonusLabel = QtWidgets.QLabel(parent=self.specialSkillBonusWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(16)
        self.specialSkillBonusLabel.setFont(font)
        self.specialSkillBonusLabel.setStyleSheet("#specialSkillBonusLabel {\n"
"    color: white;\n"
"}")
        self.specialSkillBonusLabel.setObjectName("specialSkillBonusLabel")
        self.horizontalLayout_15.addWidget(self.specialSkillBonusLabel)
        self.specialSkillBonusValue = QtWidgets.QLabel(parent=self.specialSkillBonusWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(18)
        self.specialSkillBonusValue.setFont(font)
        self.specialSkillBonusValue.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.specialSkillBonusValue.setObjectName("specialSkillBonusValue")
        self.horizontalLayout_15.addWidget(self.specialSkillBonusValue)
        self.verticalLayout_31.addWidget(self.specialSkillBonusWidget)
        self.verticalLayout_29.addLayout(self.verticalLayout_31)
        self.verticalLayout_32 = QtWidgets.QVBoxLayout()
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.energyLossPunishmentWidget = QtWidgets.QWidget(parent=self.resultScrollAreaWidgetContents)
        self.energyLossPunishmentWidget.setMinimumSize(QtCore.QSize(544, 66))
        self.energyLossPunishmentWidget.setMaximumSize(QtCore.QSize(544, 66))
        self.energyLossPunishmentWidget.setStyleSheet("#energyLossPunishmentWidget {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #cc0000,\n"
"        stop:0.6 #990000,\n"
"        stop:1 #660000\n"
"    );\n"
"}")
        self.energyLossPunishmentWidget.setObjectName("energyLossPunishmentWidget")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.energyLossPunishmentWidget)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.energyLossPunishmentLabel = QtWidgets.QLabel(parent=self.energyLossPunishmentWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(16)
        self.energyLossPunishmentLabel.setFont(font)
        self.energyLossPunishmentLabel.setStyleSheet("#energyLossPunishmentLabel {\n"
"    color: white;\n"
"}")
        self.energyLossPunishmentLabel.setObjectName("energyLossPunishmentLabel")
        self.horizontalLayout_16.addWidget(self.energyLossPunishmentLabel)
        self.energyLossPunishmentValue = QtWidgets.QLabel(parent=self.energyLossPunishmentWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(18)
        self.energyLossPunishmentValue.setFont(font)
        self.energyLossPunishmentValue.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.energyLossPunishmentValue.setObjectName("energyLossPunishmentValue")
        self.horizontalLayout_16.addWidget(self.energyLossPunishmentValue)
        self.verticalLayout_32.addWidget(self.energyLossPunishmentWidget)
        self.verticalLayout_29.addLayout(self.verticalLayout_32)
        self.verticalLayout_33 = QtWidgets.QVBoxLayout()
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.levelBonusWidget = QtWidgets.QWidget(parent=self.resultScrollAreaWidgetContents)
        self.levelBonusWidget.setMinimumSize(QtCore.QSize(544, 66))
        self.levelBonusWidget.setMaximumSize(QtCore.QSize(544, 66))
        self.levelBonusWidget.setStyleSheet("#levelBonusWidget {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #009900,\n"
"        stop:0.6 #008000,\n"
"        stop:1 #004d00\n"
"    );\n"
"}")
        self.levelBonusWidget.setObjectName("levelBonusWidget")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.levelBonusWidget)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.levelBonusLabel = QtWidgets.QLabel(parent=self.levelBonusWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(16)
        self.levelBonusLabel.setFont(font)
        self.levelBonusLabel.setStyleSheet("#levelBonusLabel {\n"
"    color: white;\n"
"}")
        self.levelBonusLabel.setObjectName("levelBonusLabel")
        self.horizontalLayout_17.addWidget(self.levelBonusLabel)
        self.levelBonusLabelValue = QtWidgets.QLabel(parent=self.levelBonusWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(18)
        self.levelBonusLabelValue.setFont(font)
        self.levelBonusLabelValue.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.levelBonusLabelValue.setObjectName("levelBonusLabelValue")
        self.horizontalLayout_17.addWidget(self.levelBonusLabelValue)
        self.verticalLayout_33.addWidget(self.levelBonusWidget)
        self.verticalLayout_29.addLayout(self.verticalLayout_33)
        self.goBtn = QtWidgets.QPushButton(parent=self.resultScrollAreaWidgetContents)
        self.goBtn.setMinimumSize(QtCore.QSize(250, 75))
        self.goBtn.setMaximumSize(QtCore.QSize(250, 75))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setBold(False)
        self.goBtn.setFont(font)
        self.goBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.goBtn.setStyleSheet("#goBtn {\n"
"    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #4d9900,\n"
"        stop:0.6 #336600,\n"
"        stop:1 #264d00\n"
"    );\n"
"}\n"
"#goBtn:hover {\n"
"        background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #428000,\n"
"        stop:0.6 #284d00,\n"
"        stop:1 #1a3300\n"
"    );\n"
"}")
        self.goBtn.setObjectName("goBtn")
        self.verticalLayout_29.addWidget(self.goBtn, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.resultScrollArea.setWidget(self.resultScrollAreaWidgetContents)
        self.horizontalLayout_18.addWidget(self.resultScrollArea)
        self.stackedWidget.addWidget(self.resultPage)


    def toggleSoundIcon(self):
        icon = QtGui.QIcon()
        if self.soundBtn.isChecked():
                icon.addPixmap(QtGui.QPixmap("GUI\\icons\\muteVolumeIcon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        else:
                icon.addPixmap(QtGui.QPixmap("GUI\\icons\\openVolumeIcon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        
        self.soundBtn.setIcon(icon)

    def toggleDifficultyBtn(self):
        if self.difficultyBtn.isChecked():
            self.difficultyBtn.setText("ZOR")
            self.difficultyBtn.setStyleSheet("#difficultyBtn {\n"
	"border-radius: 30px;"
	"background-color: qradialgradient("
        "cx:0.5, cy:0.5, radius:0.8,"
        "fx:0.5, fy:0.5,"
        "stop:0 #b30000,"
        "stop:1 #800000"
  "  );"
"}"
"#difficultyBtn:hover {"
	"background-color: qradialgradient("
        "cx:0.5, cy:0.5, radius:0.8,"
        "fx:0.5, fy:0.5,"
        "stop:0 #990000,"
        "stop:1 #660000"
    ");"
"}")
        else:
             self.difficultyBtn.setText("KOLAY")
             self.difficultyBtn.setStyleSheet("#difficultyBtn {\n"
"    border-radius: 30px;\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #33cc33,\n"
"        stop:1 #29a329\n"
"    );\n"
"}\n"
"#difficultyBtn:hover {\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #2eb82e,\n"
"        stop:1 #248f24\n"
"    );;\n"
"}")
             

    def clickedConfirmBtn(self, isOk):
        if isOk:
            self.stackedWidget.setCurrentIndex(0)
        else:
            QMessageBox.warning(None, "Hatalı Giriş", "Kullanıcı Adı veya Şifre Hatalı!")

    def clickedGamePageBackBtn(self):
        answer = QMessageBox.warning(
            None,
            "Çıkış Onayı",
            "Mevcut ilerlemeniz kaybolacaktır!\nÇıkmak istediğinize emin misiniz?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if answer == QMessageBox.StandardButton.Yes:
            self.stackedWidget.setCurrentIndex(0)            

    def clickedSettingBtn(self):
        isVisible = self.settingsWidget.isVisible()
        self.settingsWidget.setVisible(not isVisible)
                  

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.playGameBtn.clicked.connect(lambda: ui.clickedPlayGameBtn(True))

    ui.goBtn.clicked.connect(lambda: ui.clickedResultPageGoBtn(True))

    MainWindow.show()
    sys.exit(app.exec())
