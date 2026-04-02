from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from GUI.gui import Ui_MainWindow
from GUI.athleteCard import AthleteCardWidget
from account_service import AccountService
from score_service import ScoreService
from utils import VeriOkuyucu
from logic import OyunYonetici
from models import KolayStrateji, OrtaStrateji
import random


def handleRegistriation(ui, accountService):
    username = ui.registerUsernameInput.text().lower().strip()
    password = ui.registerPasswordInput.text().strip()

    if not password or not username:
        return ui.clickedConfirmBtn(False)
    
    isSuccess = accountService.registerUser(username, password)

    ui.clickedConfirmBtn(isSuccess)

def handleLogIn(ui, accountService):
    ui.username = ui.logInUsernameInput.text().lower().strip()
    password = ui.logInPasswordInput.text().strip()

    if not password or not ui.username:
        return ui.clickedConfirmBtn(False)
    
    isSuccess = accountService.logIn(ui.username, password)

    if isSuccess:
        ui.isLoggedIn = True

    ui.clickedConfirmBtn(isSuccess)


def placeTheCard(ui, player):

    if ui.playCurrent % 2 == 0:
        if ui.frame.layout() is not None:
            while ui.frame.layout().count():
                item = ui.frame.layout().takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
    else:
        if ui.frame_2.layout() is not None:
            while ui.frame_2.layout().count():
                item = ui.frame_2.layout().takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()

    if player.brans.lower().strip() == "futbol":
        data = {
            'name': "\n".join(player.sporcuAdi.split(" ")),
            'type': player.brans.upper(),
            'image_path': f'GUI/Pictures/{"_".join(player.sporcuAdi.split(" ")).title()}.jpg',
            'stat1': str(player.penalti),
            'stat2': str(player.serbestVurus),
            'stat3': str(player.kaleciKarsiKarsiya),
            'stat4': str(player.dayaniklilik),
            'statText1': "PENALTI",
            'statText2': "SERBEST VURUŞ",
            'statText3': "KALECİ KARŞISINDA",
            'energy_value': str(player.enerji)
        }
    elif player.brans.lower().strip() == "basketbol":
        data = {
            'name': "\n".join(player.sporcuAdi.split(" ")),
            'type': player.brans.upper(),
            'image_path': f'GUI/Pictures/{"_".join(player.sporcuAdi.split(" "))}.jpg',
            'stat1': str(player.ucluk),
            'stat2': str(player.ikilik),
            'stat3': str(player.serbestAtis),
            'stat4': str(player.dayaniklilik),
            'statText1': "UCLUK",
            'statText2': "IKILIK",
            'statText3': "SERBEST ATIŞ",
            'energy_value': str(player.enerji)
        }
    elif player.brans.lower().strip() == "voleybol":
        data = {
            'name': "\n".join(player.sporcuAdi.split(" ")),
            'type': player.brans.upper(),
            'image_path': f'GUI/Pictures/{"_".join(player.sporcuAdi.split(" "))}.jpg',
            'stat1': str(player.servis),
            'stat2': str(player.blok),
            'stat3': str(player.smac),
            'stat4': str(player.dayaniklilik),
            'statText1': "SERVİS",
            'statText2': "BLOK",
            'statText3': "SMAÇ",
            'energy_value': str(player.enerji)
        }

    cardWidget = AthleteCardWidget(data)

    if ui.playCurrent % 2 == 0:
        if ui.frame.layout() is None:
            layout = QtWidgets.QHBoxLayout(ui.frame)
            ui.frame.setLayout(layout)

        ui.frame.layout().addWidget(cardWidget)
    else:
        if ui.frame_2.layout() is None:
            layout = QtWidgets.QHBoxLayout(ui.frame_2)
            ui.frame_2.setLayout(layout)

        ui.frame_2.layout().addWidget(cardWidget)

    ui.playCurrent += 1

def clickPlayBtnProcess(ui):
    ui.isOver = False
    kartlar = VeriOkuyucu.kartlariOku("sporcular.txt")
    ui.yonetici = OyunYonetici(kartlar)
    if ui.difficultyBtn.text().lower().strip() == "kolay":
        ui.strateji = KolayStrateji()
    else:
        ui.strateji = OrtaStrateji()

    ui.brans = ui.yonetici.tur_sirasi[ui.yonetici.tur_sayisi]
    ui.u_uygun = [k for k in ui.yonetici.kullanici_eli if k.brans == ui.brans and k.enerji > 0]

    if ui.u_uygun:
        ui.u_kart = random.choice(ui.u_uygun) 
    else:
        ui.u_kart = None

    ui.c_kart = ui.strateji.kartSec(ui.yonetici.bilgisayar_eli, ui.brans)

    placeTheCard(ui, ui.u_kart)
    placeTheCard(ui, ui.c_kart)

    ui.stackedWidget_2.setCurrentIndex(0)

def handlePlayGameClick(ui):
    if ui.isLoggedIn:
        ui.stackedWidget.setCurrentIndex(2)
        clickPlayBtnProcess(ui)
        updateDeckList(ui)
    else:
        QMessageBox.warning(None, "Giriş Başarısız", "Önce Giriş Yapmalısınız!")

def clickEndTourBtnProcess(ui):
    if ui.yonetici.tur_sayisi < 12:
        if ui.u_kart is None and ui.c_kart is not None:
            sonuc = "Bilgisayar Hukmen Kazandi"
            ui.yonetici.bilgisayar_skor += 8
        elif ui.c_kart is None and ui.u_kart is not None:
            sonuc = "Kullanici Hukmen Kazandi"
            ui.yonetici.kullanici_skor += 8
        elif ui.u_kart is not None and ui.c_kart is not None:
            sonuc = ui.yonetici.karsilastir(ui.u_kart, ui.c_kart, ui.brans)
        else:
            sonuc = "BERABERLİK"

        ui.label_7.setText(str(int(ui.yonetici.kullanici_skor)))

        ui.yonetici.tur_sayisi += 1

        if sonuc == "KAZANDIN":
            ui.resultLabel.setText("TURU KAZANDIN")
        elif sonuc == "KAYBETTİN":
            ui.resultLabel.setText("TURU KAYBETTİN")
        else:
            ui.resultLabel.setText(sonuc)

        if ui.u_kart:
            if ui.yonetici.kullaniciOzelYetenek:
                ui.specialSkillBonusValue.setText(f"+ {str(15)}")
            else:
                ui.specialSkillBonusValue.setText(f"+ {0}")

            moral_bonus = 10 if ui.yonetici.kullanici_moral >= 80 else (5 if ui.yonetici.kullanici_moral >= 50 else -5)
            if moral_bonus > 0:
                ui.moralBonusValue.setText(f"+ {str(moral_bonus)}")
                ui.moralBonusWidget.setStyleSheet("#moralBonusWidget {\n"
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
            else:
                ui.moralBonusValue.setText(f"- {str(abs(moral_bonus))}")
                ui.moralBonusWidget.setStyleSheet("#moralBonusWidget {\n"
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
                

            secilen = getattr(ui.u_kart, ui.yonetici.secilen)
            enerjiCeza = (secilen * 0.10 // 1) if ui.u_kart.enerji <= 70 else 0
            seviyeBonusu = 10 if ui.u_kart.seviye == 3 else (5 if ui.u_kart.seviye == 2 else 0)
            
            ui.basicAttributeValue.setText(f"+ {str(secilen)}")
            ui.energyLossPunishmentValue.setText(f"- {str(enerjiCeza)}")
            ui.levelBonusLabelValue.setText(f"+ {str(seviyeBonusu)}")
            
        

        ui.goBtn.setText("DEVAM ET")

        if ui.yonetici.tur_sayisi < 12:
            ui.brans = ui.yonetici.tur_sirasi[ui.yonetici.tur_sayisi]
            ui.u_uygun = [k for k in ui.yonetici.kullanici_eli if k.brans == ui.brans and k.enerji > 0]

            if ui.u_uygun:
                ui.u_kart = random.choice(ui.u_uygun) 
            else:
                ui.u_kart = None

            ui.c_kart = ui.strateji.kartSec(ui.yonetici.bilgisayar_eli, ui.brans)
            
            placeTheCard(ui, ui.u_kart)
            placeTheCard(ui, ui.c_kart)
        else:
            ui.isOver = True
            if ui.yonetici.kullanici_skor > ui.yonetici.bilgisayar_skor:
                ui.resultLabel.setText("OYUNU KAZANDIN🎉🥳")
            elif ui.yonetici.bilgisayar_skor > ui.yonetici.kullanici_skor:
                ui.resultLabel.setText("OYUNU KAYBETTİN😫🥀")
            ui.goBtn.setText("OYUNU BİTİR")

    ui.stackedWidget.setCurrentIndex(5)
    updateDeckList(ui)


def addScoreRow(ui, username, difficulty, score):
    row_frame = QtWidgets.QFrame(parent=ui.statisticsScrollAreaWidgetContents)
    row_frame.setMinimumSize(QtCore.QSize(1200, 50))
    row_frame.setMaximumSize(QtCore.QSize(1277, 60))
    row_frame.setStyleSheet("""
                QFrame {
                    border: 1px solid #4d79ff;
                    border-radius: 8px;
                    background-color: rgba(255, 255, 255, 0.1);
                }
            """)
            
    row_layout = QtWidgets.QHBoxLayout(row_frame)
    row_layout.setSpacing(100) # Header ile uyumlu olması için ayarlayın

    font = QtGui.QFont("Verdana", 14)
            
    name_lbl = QtWidgets.QLabel(username, row_frame)
    name_lbl.setFont(font)
    name_lbl.setStyleSheet("color: white; border: none;")
    name_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    diff_lbl = QtWidgets.QLabel(difficulty, row_frame)
    diff_lbl.setFont(font)
    diff_lbl.setStyleSheet("color: white; border: none;")
    diff_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    score_lbl = QtWidgets.QLabel(str(score), row_frame)
    score_lbl.setFont(font)
    score_lbl.setStyleSheet("color: white; border: none;")
    score_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    row_layout.addWidget(name_lbl)
    row_layout.addWidget(diff_lbl)
    row_layout.addWidget(score_lbl)

    ui.verticalLayout.insertWidget(0, row_frame)

def clickedResultPageGoBtn(ui, isOver, scoreService):
    if isOver:
        while ui.verticalLayout.count() > 1:
            item = ui.verticalLayout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        scoreService.addScore(ui.username, ui.difficultyBtn.text(), ui.yonetici.kullanici_skor)

        leaderboard = scoreService.getLeaderboard()

        for data in leaderboard:
            username = data['username']
            difficulty = data['difficulty']
            score = data['score']
            addScoreRow(ui, username, difficulty, score)
        ui.stackedWidget.setCurrentIndex(0)
        
    else:
        ui.stackedWidget.setCurrentIndex(2)

def clickedStatisticsBtn(ui, scoreService):
    while ui.verticalLayout.count() > 1:
        item = ui.verticalLayout.takeAt(0)
        widget = item.widget()
        if widget:
            widget.deleteLater()

    leaderboard = scoreService.getLeaderboard()
    
    for data in leaderboard:
        username = data['username']
        difficulty = data['difficulty']
        score = data['score']
        addScoreRow(ui, username, difficulty, score)
    
    ui.stackedWidget.setCurrentIndex(1)

def updateDeckList(ui):
    while ui.verticalLayout_28.count():
        item = ui.verticalLayout_28.takeAt(0)
        widget = item.widget()
        if widget:
            widget.deleteLater()

    for player in ui.yonetici.kullanici_eli:
        card_row = QtWidgets.QFrame()
        card_row.setMinimumSize(QtCore.QSize(0, 80))
        card_row.setStyleSheet("""
            QFrame {
                border: 1px solid #4d79ff;
                border-radius: 5px;
                background-color: rgba(255, 255, 255, 0.1);
                margin: 2px;
            }
        """)
        
        row_layout = QtWidgets.QHBoxLayout(card_row)

        font = QtGui.QFont("Verdana", 10)
        font.setBold(True)

        # Bilgileri ekle
        name_lbl = QtWidgets.QLabel(f"İsim: {player.sporcuAdi}")
        type_lbl = QtWidgets.QLabel(f"Branş: {player.brans}")
        energy_lbl = QtWidgets.QLabel(f"Enerji: {player.enerji}%")

        for lbl in [name_lbl, type_lbl, energy_lbl]:
            lbl.setFont(font)
            lbl.setStyleSheet("color: white; border: none;")
            row_layout.addWidget(lbl)

        ui.verticalLayout_28.addWidget(card_row)
    
    ui.verticalLayout_28.addStretch()

def main():
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    ui.isOver = False
    ui.playCurrent = 0
    ui.isLoggedIn = False
    ui.gameResult = ""

    accountService = AccountService()
    scoreService = ScoreService()
    
    ui.confirmBtn.clicked.connect(lambda: handleRegistriation(ui, accountService))
    ui.confirmBtn_5.clicked.connect(lambda: handleLogIn(ui, accountService))

    ui.playGameBtn.clicked.connect(lambda: handlePlayGameClick(ui))

    ui.endTourBtn.clicked.connect(lambda: clickEndTourBtnProcess(ui))

    ui.goBtn.clicked.connect(lambda: clickedResultPageGoBtn(ui, ui.isOver, scoreService))

    ui.statisticsBtn.clicked.connect(lambda: clickedStatisticsBtn(ui, scoreService))

    MainWindow.show()
    sys.exit(app.exec())



if __name__ == "__main__":
    main()