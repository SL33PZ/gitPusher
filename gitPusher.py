# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowUKjcfO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from src.git import gitPusher


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setEnabled(True)
        self.resize(700, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(700, 500))
        self.setMaximumSize(QSize(700, 500))
        self.setStyleSheet(u"font: 11pt \"Comfortaa\";")
        self.horizontalLayoutWidget = QWidget(self)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 741, 111))
        self.hL = QHBoxLayout(self.horizontalLayoutWidget)
        self.hL.setObjectName(u"hL")
        self.hL.setContentsMargins(0, 0, 0, 0)
        self.hs2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hL.addItem(self.hs2)

        self.title_label = QLabel(self.horizontalLayoutWidget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setStyleSheet(u"QLabel#title_label {\n"
"font: 48pt \"JK Abode\";\n"
"}")

        self.hL.addWidget(self.title_label)

        self.hS = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hL.addItem(self.hS)

        self.verticalLayoutWidget = QWidget(self)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(110, 110, 469, 391))
        self.vL = QVBoxLayout(self.verticalLayoutWidget)
        self.vL.setObjectName(u"vL")
        self.vL.setContentsMargins(0, 0, 0, 0)
        self.vS = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vL.addItem(self.vS)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.repopathTitle = QLabel(self.verticalLayoutWidget)
        self.repopathTitle.setObjectName(u"repopathTitle")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.repopathTitle)

        self.repopathLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.repopathLineEdit.setObjectName(u"repopathLineEdit")
        self.repopathLineEdit.setMinimumSize(QSize(350, 0))
        self.repopathLineEdit.setMaximumSize(QSize(300, 16777215))
        self.repopathLineEdit.setFocusPolicy(Qt.TabFocus)
        self.repopathLineEdit.setAutoFillBackground(False)
        self.repopathLineEdit.setStyleSheet(u"font: 10pt \"Comfortaa\";")
        self.repopathLineEdit.setFrame(True)
        self.repopathLineEdit.setEchoMode(QLineEdit.Normal)
        self.repopathLineEdit.setClearButtonEnabled(False)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.repopathLineEdit)

        self.repourlLabel = QLabel(self.verticalLayoutWidget)
        self.repourlLabel.setObjectName(u"repourlLabel")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.repourlLabel)

        self.repourlLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.repourlLineEdit.setObjectName(u"repourlLineEdit")
        self.repourlLineEdit.setAutoFillBackground(False)
        self.repourlLineEdit.setStyleSheet(u"font: 10pt \"Comfortaa\";")
        self.repourlLineEdit.setFrame(True)
        self.repourlLineEdit.setEchoMode(QLineEdit.Normal)
        self.repourlLineEdit.setClearButtonEnabled(False)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.repourlLineEdit)

        self.commitLabel = QLabel(self.verticalLayoutWidget)
        self.commitLabel.setObjectName(u"commitLabel")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.commitLabel)

        self.commitLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.commitLineEdit.setObjectName(u"commitLineEdit")
        self.commitLineEdit.setAutoFillBackground(False)
        self.commitLineEdit.setStyleSheet(u"font: 10pt \"Comfortaa\";")
        self.commitLineEdit.setFrame(True)
        self.commitLineEdit.setEchoMode(QLineEdit.Normal)
        self.commitLineEdit.setClearButtonEnabled(False)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.commitLineEdit)

        self.accesstokenLabel = QLabel(self.verticalLayoutWidget)
        self.accesstokenLabel.setObjectName(u"accesstokenLabel")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.accesstokenLabel)

        self.accesstokenLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.accesstokenLineEdit.setObjectName(u"accesstokenLineEdit")
        self.accesstokenLineEdit.setAutoFillBackground(False)
        self.accesstokenLineEdit.setStyleSheet(u"font: 10pt \"Comfortaa\";")
        self.accesstokenLineEdit.setFrame(True)
        self.accesstokenLineEdit.setEchoMode(QLineEdit.Normal)
        self.accesstokenLineEdit.setClearButtonEnabled(False)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.accesstokenLineEdit)


        self.vL.addLayout(self.formLayout_2)

        self.vS2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vL.addItem(self.vS2)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(125, 0))
        self.pushButton.setMaximumSize(QSize(150, 16777215))

        self.vL.addWidget(self.pushButton, 0, Qt.AlignHCenter)

        self.vS3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vL.addItem(self.vS3)

        self.line = QFrame(self)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(-80, 99, 791, 31))
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.HLine)
        self.clearPushButton = QPushButton(self)
        self.clearPushButton.setObjectName(u"clearPushButton")
        self.clearPushButton.setGeometry(QRect(590, 440, 90, 40))
#if QT_CONFIG(shortcut)
        self.repopathTitle.setBuddy(self.repopathLineEdit)
        self.repourlLabel.setBuddy(self.repourlLineEdit)
        self.commitLabel.setBuddy(self.commitLineEdit)
        self.accesstokenLabel.setBuddy(self.accesstokenLineEdit)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi()
        self.clearPushButton.clicked.connect(self.accesstokenLineEdit.clear)
        self.clearPushButton.clicked.connect(self.commitLineEdit.clear)
        self.clearPushButton.clicked.connect(self.repourlLineEdit.clear)
        self.clearPushButton.clicked.connect(self.repopathLineEdit.clear)
        self.accesstokenLineEdit.textChanged.connect(self.accesstokenLineEdit.setText)
        self.commitLineEdit.textChanged.connect(self.commitLineEdit.setText)
        self.repourlLineEdit.textChanged.connect(self.repourlLineEdit.setText)
        self.repopathLineEdit.textChanged.connect(self.repopathLineEdit.setText)
        self.pushButton.clicked.connect(lambda: self.pushEvent())

        QMetaObject.connectSlotsByName(self)
        
        
        
    def pushEvent(self):
        repo_path = self.repopathLineEdit.text()
        repo_url = self.repourlLineEdit.text()
        message = self.commitLineEdit.text()
        access_token = self.accesstokenLineEdit.text()
        try:
            push = gitPusher(repo_path=repo_path, 
                        dirs=".",
                        message=message, 
                        repo_url=repo_url,
                        access_token=access_token)
            push.start()
        
        except KeyboardInterrupt:
            sys.exit("gitPusher closed...")
        
        
        
        
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("Form", u"gitPush", None))
        self.repopathTitle.setText(QCoreApplication.translate("Form", u"Repo Path:", None))
        self.repopathLineEdit.setText("")
        self.repopathLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"e.g: ../<Repository>", None))
        self.repourlLabel.setText(QCoreApplication.translate("Form", u"Repo URL:", None))
        self.repourlLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"e.g: ../<Repository>", None))
        self.commitLabel.setText(QCoreApplication.translate("Form", u"Commit:", None))
        self.commitLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"e.g: ../<Repository>", None))
        self.accesstokenLabel.setText(QCoreApplication.translate("Form", u"Access Token:", None))
        self.accesstokenLineEdit.setText(QCoreApplication.translate("Form", u"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", None))
        self.accesstokenLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"e.g: ../<Repository>", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Push it!", None))
        self.clearPushButton.setText(QCoreApplication.translate("Form", u"Clear", None))
    # retranslateUi



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec())