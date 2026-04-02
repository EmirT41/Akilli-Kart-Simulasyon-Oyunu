from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(365, 652)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(8)
        Form.setFont(font)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.athleteCard = QtWidgets.QWidget(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.athleteCard.sizePolicy().hasHeightForWidth())
        self.athleteCard.setSizePolicy(sizePolicy)
        self.athleteCard.setMinimumSize(QtCore.QSize(320, 500))
        self.athleteCard.setMaximumSize(QtCore.QSize(340, 590))
        self.athleteCard.setStyleSheet("#athleteCard {\n"
"    border-radius:10px;\n"
"    border: none;\n"
"    background-color: #1a1a1a;\n"
"}")
        self.athleteCard.setObjectName("athleteCard")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.athleteCard)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.topInformationLayout = QtWidgets.QHBoxLayout()
        self.topInformationLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.topInformationLayout.setObjectName("topInformationLayout")
        self.backBtn = QtWidgets.QPushButton(parent=self.athleteCard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backBtn.sizePolicy().hasHeightForWidth())
        self.backBtn.setSizePolicy(sizePolicy)
        self.backBtn.setMinimumSize(QtCore.QSize(44, 44))
        self.backBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.backBtn.setStyleSheet("#backBtn {\n"
"    border: none;\n"
"}\n"
"#backBtn:hover {\n"
"    border-radius: 10px;\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #333333,\n"
"        stop:0.6 #2e2e2e,\n"
"        stop:1 #1a1a1a\n"
"    );\n"
"}")
        self.backBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("GUI/icons/arrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.backBtn.setIcon(icon)
        self.backBtn.setIconSize(QtCore.QSize(40, 40))
        self.backBtn.setObjectName("backBtn")
        self.topInformationLayout.addWidget(self.backBtn)
        self.athleteType = QtWidgets.QLabel(parent=self.athleteCard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.athleteType.sizePolicy().hasHeightForWidth())
        self.athleteType.setSizePolicy(sizePolicy)
        self.athleteType.setMinimumSize(QtCore.QSize(197, 44))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setItalic(True)
        self.athleteType.setFont(font)
        self.athleteType.setStyleSheet("#athleteType {\n"
"    color: white;\n"
"}")
        self.athleteType.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.athleteType.setObjectName("athleteType")
        self.topInformationLayout.addWidget(self.athleteType)
        self.shareBtn = QtWidgets.QPushButton(parent=self.athleteCard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shareBtn.sizePolicy().hasHeightForWidth())
        self.shareBtn.setSizePolicy(sizePolicy)
        self.shareBtn.setMinimumSize(QtCore.QSize(44, 44))
        self.shareBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.shareBtn.setStyleSheet("#shareBtn {\n"
"    border: none;\n"
"}\n"
"#shareBtn:hover {\n"
"    border-radius: 10px;\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.8,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #333333,\n"
"        stop:0.6 #2e2e2e,\n"
"        stop:1 #1a1a1a\n"
"    );\n"
"}")
        self.shareBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("GUI/icons/share.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.shareBtn.setIcon(icon1)
        self.shareBtn.setIconSize(QtCore.QSize(40, 40))
        self.shareBtn.setObjectName("shareBtn")
        self.topInformationLayout.addWidget(self.shareBtn)
        self.verticalLayout_2.addLayout(self.topInformationLayout)
        self.line_3 = QtWidgets.QFrame(parent=self.athleteCard)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.athleteImgWidget = QtWidgets.QWidget(parent=self.athleteCard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.athleteImgWidget.sizePolicy().hasHeightForWidth())
        self.athleteImgWidget.setSizePolicy(sizePolicy)
        self.athleteImgWidget.setMinimumSize(QtCore.QSize(280, 230))
        self.athleteImgWidget.setMaximumSize(QtCore.QSize(300, 250))
        self.athleteImgWidget.setObjectName("athleteImgWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.athleteImgWidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.athleteImage = QtWidgets.QLabel(parent=self.athleteImgWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.athleteImage.sizePolicy().hasHeightForWidth())
        self.athleteImage.setSizePolicy(sizePolicy)
        self.athleteImage.setMinimumSize(QtCore.QSize(280, 210))
        self.athleteImage.setMaximumSize(QtCore.QSize(280, 210))
        self.athleteImage.setStyleSheet("#athleteImage {\n"
"    border-radius: 10px;\n"
"    border: none;\n"
"}")
        self.athleteImage.setText("")
        self.athleteImage.setPixmap(QtGui.QPixmap("resimler/basketbolcular/lebron.jpg"))
        self.athleteImage.setScaledContents(True)
        self.athleteImage.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.athleteImage.setObjectName("athleteImage")
        # addWidget satırına hizalama parametresi ekliyoruz
        self.verticalLayout_4.addWidget(self.athleteImage, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.abilityLabel = QtWidgets.QLabel(parent=self.athleteImgWidget)
        self.abilityLabel.setMinimumSize(QtCore.QSize(70, 30))
        self.abilityLabel.setMaximumSize(QtCore.QSize(70, 30))
        self.abilityLabel.setText("")
        self.abilityLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.abilityLabel.setObjectName("abilityLabel")
        self.verticalLayout_4.addWidget(self.abilityLabel, 0, QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTop)
        self.athleteNameText = QtWidgets.QLabel(parent=self.athleteImgWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.athleteNameText.sizePolicy().hasHeightForWidth())
        self.athleteNameText.setSizePolicy(sizePolicy)
        self.athleteNameText.setMinimumSize(QtCore.QSize(110, 60))
        self.athleteNameText.setMaximumSize(QtCore.QSize(140, 90))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        self.athleteNameText.setFont(font)
        self.athleteNameText.setStyleSheet("#athleteNameText {\n"
"    color: #4da6ff;\n"
    "text-shadow:\n" 
        "-1px -1px 0 #000,\n"  
         "1px -1px 0 #000,\n"
        "-1px  1px 0 #000,\n"
         "1px  1px 0 #000;\n"
"}")
        self.athleteNameText.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.athleteNameText.setObjectName("athleteNameText")
        self.verticalLayout_4.addWidget(self.athleteNameText, 0, QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.athleteImage.raise_()
        self.athleteNameText.raise_()
        self.abilityLabel.raise_()
        self.verticalLayout.addWidget(self.athleteImgWidget, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.energyLayout = QtWidgets.QGridLayout()
        self.energyLayout.setObjectName("energyLayout")
        self.energyValue = QtWidgets.QLabel(parent=self.athleteCard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.energyValue.sizePolicy().hasHeightForWidth())
        self.energyValue.setSizePolicy(sizePolicy)
        self.energyValue.setMinimumSize(QtCore.QSize(136, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setKerning(True)
        self.energyValue.setFont(font)
        self.energyValue.setStyleSheet("#energyValue {\n"
"    color: #009900;\n"
"}")
        self.energyValue.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.energyValue.setObjectName("energyValue")
        self.energyLayout.addWidget(self.energyValue, 0, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.energyBar = QtWidgets.QProgressBar(parent=self.athleteCard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.energyBar.sizePolicy().hasHeightForWidth())
        self.energyBar.setSizePolicy(sizePolicy)
        self.energyBar.setMinimumSize(QtCore.QSize(280, 30))
        self.energyBar.setMaximumSize(QtCore.QSize(280, 30))
        self.energyBar.setMouseTracking(False)
        self.energyBar.setAutoFillBackground(False)
        self.energyBar.setStyleSheet("#energyBar {\n"
"    border-radius: 15px;\n"
"    border: none;\n"
"}\n"
"#energyBar::chunk {\n"
"    border-radius: 15px;\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #009900,\n"
"        stop:1 #00e600\n"
"    );\n"
"}")
        self.energyBar.setProperty("value", 100)
        self.energyBar.setTextVisible(False)
        self.energyBar.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.energyBar.setTextDirection(QtWidgets.QProgressBar.Direction.TopToBottom)
        self.energyBar.setObjectName("energyBar")
        self.energyLayout.addWidget(self.energyBar, 1, 0, 1, 2, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.energyText = QtWidgets.QLabel(parent=self.athleteCard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.energyText.sizePolicy().hasHeightForWidth())
        self.energyText.setSizePolicy(sizePolicy)
        self.energyText.setMinimumSize(QtCore.QSize(136, 15))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.energyText.setFont(font)
        self.energyText.setStyleSheet("#energyText {\n"
"    color: #cccc00;\n"
"}")
        self.energyText.setObjectName("energyText")
        self.energyLayout.addWidget(self.energyText, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.verticalLayout_2.addLayout(self.energyLayout)
        self.line_2 = QtWidgets.QFrame(parent=self.athleteCard)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.statisticsLayout = QtWidgets.QGridLayout()
        self.statisticsLayout.setObjectName("statisticsLayout")
        self.durabilityWidget = QtWidgets.QWidget(parent=self.athleteCard)
        self.durabilityWidget.setMinimumSize(QtCore.QSize(156, 106))
        self.durabilityWidget.setObjectName("durabilityWidget")
        self.durabilityText = QtWidgets.QLabel(parent=self.durabilityWidget)
        self.durabilityText.setGeometry(QtCore.QRect(30, 5, 90, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.durabilityText.sizePolicy().hasHeightForWidth())
        self.durabilityText.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(True)
        self.durabilityText.setFont(font)
        self.durabilityText.setStyleSheet("#durabilityText {\n"
"    color: #8a8a5c;\n"
"}")
        self.durabilityText.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.durabilityText.setObjectName("durabilityText")
        self.durabilityStatus = QtWidgets.QLabel(parent=self.durabilityWidget)
        self.durabilityStatus.setGeometry(QtCore.QRect(0, 0, 140, 90))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.durabilityStatus.sizePolicy().hasHeightForWidth())
        self.durabilityStatus.setSizePolicy(sizePolicy)
        self.durabilityStatus.setMinimumSize(QtCore.QSize(140, 90))
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro Medi")
        font.setPointSize(16)
        self.durabilityStatus.setFont(font)
        self.durabilityStatus.setStyleSheet("#durabilityStatus {\n"
"    border-radius: 10px;\n"
"    border: none;\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #333333,\n"
"        stop:1 #404040\n"
"    );\n"
"    color: white;\n"
"}")
        self.durabilityStatus.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.durabilityStatus.setObjectName("durabilityStatus")
        self.durabilityStatus.raise_()
        self.durabilityText.raise_()
        self.statisticsLayout.addWidget(self.durabilityWidget, 1, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignBottom)
        self.oneOnOneWithGoalkeeperWidget = QtWidgets.QWidget(parent=self.athleteCard)
        self.oneOnOneWithGoalkeeperWidget.setMinimumSize(QtCore.QSize(156, 106))
        self.oneOnOneWithGoalkeeperWidget.setObjectName("oneOnOneWithGoalkeeperWidget")
        self.oneOnOneWithGoalkeeperStatus = QtWidgets.QLabel(parent=self.oneOnOneWithGoalkeeperWidget)
        self.oneOnOneWithGoalkeeperStatus.setGeometry(QtCore.QRect(0, 0, 140, 90))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oneOnOneWithGoalkeeperStatus.sizePolicy().hasHeightForWidth())
        self.oneOnOneWithGoalkeeperStatus.setSizePolicy(sizePolicy)
        self.oneOnOneWithGoalkeeperStatus.setMinimumSize(QtCore.QSize(140, 90))
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro Medi")
        font.setPointSize(16)
        self.oneOnOneWithGoalkeeperStatus.setFont(font)
        self.oneOnOneWithGoalkeeperStatus.setStyleSheet("#oneOnOneWithGoalkeeperStatus {\n"
"    border-radius: 10px;\n"
"    border: none;\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #333333,\n"
"        stop:1 #404040\n"
"    );\n"
"    color: white;\n"
"}")
        self.oneOnOneWithGoalkeeperStatus.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.oneOnOneWithGoalkeeperStatus.setObjectName("oneOnOneWithGoalkeeperStatus")
        self.oneOnOneWithGoalkeeperText = QtWidgets.QLabel(parent=self.oneOnOneWithGoalkeeperWidget)
        self.oneOnOneWithGoalkeeperText.setGeometry(QtCore.QRect(15, 5, 110, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oneOnOneWithGoalkeeperText.sizePolicy().hasHeightForWidth())
        self.oneOnOneWithGoalkeeperText.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(True)

        self.oneOnOneWithGoalkeeperText.setFont(font)
        self.oneOnOneWithGoalkeeperText.setStyleSheet("#oneOnOneWithGoalkeeperText {\n"
"    color: #8a8a5c;\n"
"}")
        self.oneOnOneWithGoalkeeperText.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.oneOnOneWithGoalkeeperText.setObjectName("oneOnOneWithGoalkeeperText")
        self.statisticsLayout.addWidget(self.oneOnOneWithGoalkeeperWidget, 1, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignBottom)
        self.penaltyWidget = QtWidgets.QWidget(parent=self.athleteCard)
        self.penaltyWidget.setMinimumSize(QtCore.QSize(156, 106))
        self.penaltyWidget.setObjectName("penaltyWidget")
        self.penaltyText = QtWidgets.QLabel(parent=self.penaltyWidget)
        self.penaltyText.setGeometry(QtCore.QRect(45, 5, 60, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.penaltyText.sizePolicy().hasHeightForWidth())
        self.penaltyText.setSizePolicy(sizePolicy)
        self.penaltyText.setMinimumSize(QtCore.QSize(60, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(True)
        self.penaltyText.setFont(font)
        self.penaltyText.setStyleSheet("#penaltyText {\n"
"    color: #8a8a5c;\n"
"}")
        self.penaltyText.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.penaltyText.setObjectName("penaltyText")
        self.penaltyStatus = QtWidgets.QLabel(parent=self.penaltyWidget)
        self.penaltyStatus.setGeometry(QtCore.QRect(0, 0, 140, 90))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.penaltyStatus.sizePolicy().hasHeightForWidth())
        self.penaltyStatus.setSizePolicy(sizePolicy)
        self.penaltyStatus.setMinimumSize(QtCore.QSize(140, 90))
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro Medi")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.penaltyStatus.setFont(font)
        self.penaltyStatus.setStyleSheet("#penaltyStatus {\n"
"    border-radius: 10px;\n"
"    border: none;\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #333333,\n"
"        stop:1 #404040\n"
"    );\n"
"    color: white;\n"
"}")
        self.penaltyStatus.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.penaltyStatus.setObjectName("penaltyStatus")
        self.penaltyStatus.raise_()
        self.penaltyText.raise_()
        self.statisticsLayout.addWidget(self.penaltyWidget, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.freeKickWidget = QtWidgets.QWidget(parent=self.athleteCard)
        self.freeKickWidget.setMinimumSize(QtCore.QSize(156, 106))
        self.freeKickWidget.setObjectName("freeKickWidget")
        self.freeKickText = QtWidgets.QLabel(parent=self.freeKickWidget)
        self.freeKickText.setGeometry(QtCore.QRect(15, 5, 110, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freeKickText.sizePolicy().hasHeightForWidth())
        self.freeKickText.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(True)

        self.freeKickText.setFont(font)
        self.freeKickText.setStyleSheet("#freeKickText {\n"
"    color: #8a8a5c;\n"
"}")
        self.freeKickText.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.freeKickText.setObjectName("freeKickText")
        self.freeKickStatus = QtWidgets.QLabel(parent=self.freeKickWidget)
        self.freeKickStatus.setGeometry(QtCore.QRect(0, 0, 140, 90))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freeKickStatus.sizePolicy().hasHeightForWidth())
        self.freeKickStatus.setSizePolicy(sizePolicy)
        self.freeKickStatus.setMinimumSize(QtCore.QSize(140, 90))
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro Medi")
        font.setPointSize(16)
        self.freeKickStatus.setFont(font)
        self.freeKickStatus.setStyleSheet("#freeKickStatus {\n"
"    border-radius: 10px;\n"
"    border: none;\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #333333,\n"
"        stop:1 #404040\n"
"    );\n"
"    color: white;\n"
"}")
        self.freeKickStatus.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.freeKickStatus.setObjectName("freeKickStatus")
        self.freeKickStatus.raise_()
        self.freeKickText.raise_()
        self.statisticsLayout.addWidget(self.freeKickWidget, 0, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTop)
        self.verticalLayout_2.addLayout(self.statisticsLayout)
        self.verticalLayout_3.addWidget(self.athleteCard)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.athleteType.setText(_translate("Form", "BASKETBOL"))
        self.athleteNameText.setText(_translate("Form", "Gabriela\n"
"Guimaraes"))
        self.energyValue.setText(_translate("Form", "100%"))
        self.energyText.setText(_translate("Form", "Enerji Seviyesi"))
        self.durabilityText.setText(_translate("Form", "Dayanıklılık"))
        self.durabilityStatus.setText(_translate("Form", "56"))
        self.oneOnOneWithGoalkeeperStatus.setText(_translate("Form", "10"))
        self.oneOnOneWithGoalkeeperText.setText(_translate("Form", "Serbest Atış"))
        self.penaltyText.setText(_translate("Form", "Üçlük"))
        self.penaltyStatus.setText(_translate("Form", "95"))
        self.freeKickText.setText(_translate("Form", "İkilik"))
        self.freeKickStatus.setText(_translate("Form", "98"))


class AthleteCardWidget(QtWidgets.QWidget, Ui_Form):
    def __init__(self, athlete_data, parent=None):
        super().__init__(parent)
        self.setupUi(self) 
        
        self.athleteNameText.setText(athlete_data.get('name', ''))
        self.athleteType.setText(athlete_data.get('type', ''))
        
        image_path = athlete_data.get('image_path', '')
        if image_path:
            pixmap = QPixmap(image_path)
            if not pixmap.isNull():
                self.athleteImage.setPixmap(pixmap)
                self.athleteImage.setScaledContents(True)

        energy = athlete_data.get('energy_value', 0)
        self.energyBar.setValue(int(energy))
        self.energyValue.setText(f"{str(energy)}%")

        self.penaltyStatus.setText(str(athlete_data.get('stat1', 0)))
        self.freeKickStatus.setText(str(athlete_data.get('stat2', 0)))
        self.oneOnOneWithGoalkeeperStatus.setText(str(athlete_data.get('stat3', 0)))
        self.durabilityStatus.setText(str(athlete_data.get('stat4', 0)))

        self.penaltyText.setText(athlete_data.get('statText1', "Stat 1"))
        self.freeKickText.setText(athlete_data.get('statText2', "Stat 2"))
        self.oneOnOneWithGoalkeeperText.setText(athlete_data.get('statText3', "Stat 3"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
