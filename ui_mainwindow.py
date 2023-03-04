# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 400)
        self.actionAbout_TextEdit = QAction(MainWindow)
        self.actionAbout_TextEdit.setObjectName(u"actionAbout_TextEdit")
        self.actionQuitTextEdit = QAction(MainWindow)
        self.actionQuitTextEdit.setObjectName(u"actionQuitTextEdit")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        icon = QIcon()
        icon.addFile(u"images/new.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNew.setIcon(icon)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon1 = QIcon()
        icon1.addFile(u"images/open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon2 = QIcon()
        icon2.addFile(u"images/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave_as = QAction(MainWindow)
        self.actionSave_as.setObjectName(u"actionSave_as")
        icon3 = QIcon()
        icon3.addFile(u"images/save_as.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave_as.setIcon(icon3)
        self.actionRename = QAction(MainWindow)
        self.actionRename.setObjectName(u"actionRename")
        self.actionCut = QAction(MainWindow)
        self.actionCut.setObjectName(u"actionCut")
        icon4 = QIcon()
        icon4.addFile(u"images/cut.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCut.setIcon(icon4)
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        icon5 = QIcon()
        icon5.addFile(u"images/copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCopy.setIcon(icon5)
        self.actionPaste = QAction(MainWindow)
        self.actionPaste.setObjectName(u"actionPaste")
        icon6 = QIcon()
        icon6.addFile(u"images/paste.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPaste.setIcon(icon6)
        self.actionRedo = QAction(MainWindow)
        self.actionRedo.setObjectName(u"actionRedo")
        icon7 = QIcon()
        icon7.addFile(u"images/edit_redo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRedo.setIcon(icon7)
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        icon8 = QIcon()
        icon8.addFile(u"images/edit_undo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionUndo.setIcon(icon8)
        self.actionSelect_All = QAction(MainWindow)
        self.actionSelect_All.setObjectName(u"actionSelect_All")
        self.actionWhat_Help = QAction(MainWindow)
        self.actionWhat_Help.setObjectName(u"actionWhat_Help")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 22))
        self.menuTextEdit = QMenu(self.menubar)
        self.menuTextEdit.setObjectName(u"menuTextEdit")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuTextEdit.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuTextEdit.addAction(self.actionAbout_TextEdit)
        self.menuTextEdit.addAction(self.actionQuitTextEdit)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionRename)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionSelect_All)
        self.menuHelp.addAction(self.actionWhat_Help)
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionSave_as)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addAction(self.actionRedo)
        self.toolBar.addAction(self.actionUndo)

        self.retranslateUi(MainWindow)
        self.actionNew.triggered.connect(MainWindow.new_file)
        self.actionSave.triggered.connect(MainWindow.save_file)
        self.actionOpen.triggered.connect(MainWindow.open_file)
        self.actionSave_as.triggered.connect(MainWindow.save_as_file)
        self.actionRename.triggered.connect(MainWindow.rename_file)
        self.actionClose.triggered.connect(MainWindow.close_file)
        self.actionCopy.triggered.connect(MainWindow.copy_text)
        self.actionCut.triggered.connect(MainWindow.cut_text)
        self.actionPaste.triggered.connect(MainWindow.paste_text)
        self.actionRedo.triggered.connect(MainWindow.redo)
        self.actionUndo.triggered.connect(MainWindow.undo)
        self.actionAbout_TextEdit.triggered.connect(MainWindow.about)
        self.actionQuitTextEdit.triggered.connect(MainWindow.quit_app)
        self.actionSelect_All.triggered.connect(MainWindow.select_all)
        self.actionWhat_Help.triggered.connect(MainWindow.help)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TextEdit", None))
        self.actionAbout_TextEdit.setText(QCoreApplication.translate("MainWindow", u"About TextEdit", None))
        self.actionQuitTextEdit.setText(QCoreApplication.translate("MainWindow", u"Quit TextEdit", None))
#if QT_CONFIG(shortcut)
        self.actionQuitTextEdit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
#if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open...", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
#if QT_CONFIG(shortcut)
        self.actionClose.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+W", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_as.setText(QCoreApplication.translate("MainWindow", u"Save as...", None))
#if QT_CONFIG(shortcut)
        self.actionSave_as.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionRename.setText(QCoreApplication.translate("MainWindow", u"Rename", None))
        self.actionCut.setText(QCoreApplication.translate("MainWindow", u"Cut", None))
#if QT_CONFIG(shortcut)
        self.actionCut.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+X", None))
#endif // QT_CONFIG(shortcut)
        self.actionCopy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
#if QT_CONFIG(shortcut)
        self.actionCopy.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionPaste.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
#if QT_CONFIG(shortcut)
        self.actionPaste.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+V", None))
#endif // QT_CONFIG(shortcut)
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
#if QT_CONFIG(shortcut)
        self.actionRedo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+Z", None))
#endif // QT_CONFIG(shortcut)
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
#if QT_CONFIG(shortcut)
        self.actionUndo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Z", None))
#endif // QT_CONFIG(shortcut)
        self.actionSelect_All.setText(QCoreApplication.translate("MainWindow", u"Select All", None))
#if QT_CONFIG(shortcut)
        self.actionSelect_All.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.actionWhat_Help.setText(QCoreApplication.translate("MainWindow", u"What Help?", None))
        self.menuTextEdit.setTitle(QCoreApplication.translate("MainWindow", u"TextEdit", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

