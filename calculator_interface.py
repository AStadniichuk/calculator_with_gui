# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator_interface.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(350, 500)
        MainWindow.setMinimumSize(QSize(350, 500))
        icon = QIcon()
        icon.addFile(u":/icons/C:/Users/stadn/Downloads/icons/calculate_FILL0_wght400_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    color: #C4DFE6;\n"
"    background-color: #003B46;\n"
"    font-family: Rubik;\n"
"    font-size: 16pt;\n"
"    font-weight: 600;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_temp = QLabel(self.centralwidget)
        self.label_temp.setObjectName(u"label_temp")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_temp.sizePolicy().hasHeightForWidth())
        self.label_temp.setSizePolicy(sizePolicy)
        self.label_temp.setStyleSheet(u"color: #66A5AD;")
        self.label_temp.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_temp)

        self.line_edit_entry = QLineEdit(self.centralwidget)
        self.line_edit_entry.setObjectName(u"line_edit_entry")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line_edit_entry.sizePolicy().hasHeightForWidth())
        self.line_edit_entry.setSizePolicy(sizePolicy1)
        self.line_edit_entry.setStyleSheet(u"font-size: 32pt;\n"
"border: none;\n"
"")
        self.line_edit_entry.setMaxLength(12)
        self.line_edit_entry.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.line_edit_entry.setReadOnly(True)

        self.verticalLayout.addWidget(self.line_edit_entry)

        self.layout_buttons = QGridLayout()
        self.layout_buttons.setObjectName(u"layout_buttons")
        self.button_sub = QPushButton(self.centralwidget)
        self.button_sub.setObjectName(u"button_sub")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.button_sub.sizePolicy().hasHeightForWidth())
        self.button_sub.setSizePolicy(sizePolicy2)
        self.button_sub.setStyleSheet(u"QPushButton {\n"
"    background-color: #07575B;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #66A5AD;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #003B46;\n"
"}")

        self.layout_buttons.addWidget(self.button_sub, 3, 3, 1, 1)

        self.button_8 = QPushButton(self.centralwidget)
        self.button_8.setObjectName(u"button_8")
        sizePolicy2.setHeightForWidth(self.button_8.sizePolicy().hasHeightForWidth())
        self.button_8.setSizePolicy(sizePolicy2)
        self.button_8.setStyleSheet(u"QPushButton {\n"
"    background-color: #66A5AD;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #07575B;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #07575B;\n"
"}")

        self.layout_buttons.addWidget(self.button_8, 2, 1, 1, 1)

        self.button_dot = QPushButton(self.centralwidget)
        self.button_dot.setObjectName(u"button_dot")
        sizePolicy2.setHeightForWidth(self.button_dot.sizePolicy().hasHeightForWidth())
        self.button_dot.setSizePolicy(sizePolicy2)
        self.button_dot.setStyleSheet(u"QPushButton {\n"
"    background-color: #66A5AD;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #07575B;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #07575B;\n"
"}\n"
"")

        self.layout_buttons.addWidget(self.button_dot, 5, 2, 1, 1)

        self.button_2 = QPushButton(self.centralwidget)
        self.button_2.setObjectName(u"button_2")
        sizePolicy2.setHeightForWidth(self.button_2.sizePolicy().hasHeightForWidth())
        self.button_2.setSizePolicy(sizePolicy2)
        self.button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #66A5AD;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #07575B;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #07575B;\n"
"}")

        self.layout_buttons.addWidget(self.button_2, 4, 1, 1, 1)

        self.button_3 = QPushButton(self.centralwidget)
        self.button_3.setObjectName(u"button_3")
        sizePolicy2.setHeightForWidth(self.button_3.sizePolicy().hasHeightForWidth())
        self.button_3.setSizePolicy(sizePolicy2)
        self.button_3.setStyleSheet(u"QPushButton {\n"
"    background-color: #66A5AD;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #07575B;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #07575B;\n"
"}")

        self.layout_buttons.addWidget(self.button_3, 4, 2, 1, 1)

        self.button_square = QPushButton(self.centralwidget)
        self.button_square.setObjectName(u"button_square")
        sizePolicy2.setHeightForWidth(self.button_square.sizePolicy().hasHeightForWidth())
        self.button_square.setSizePolicy(sizePolicy2)
        self.button_square.setStyleSheet(u"QPushButton {\n"
"    background-color: #07575B;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #66A5AD;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #003B46;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/C:/Users/stadn/Downloads/icons/x^2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_square.setIcon(icon1)
        self.button_square.setIconSize(QSize(50, 50))

        self.layout_buttons.addWidget(self.button_square, 1, 1, 1, 1)

        self.button_mul = QPushButton(self.centralwidget)
        self.button_mul.setObjectName(u"button_mul")
        sizePolicy2.setHeightForWidth(self.button_mul.sizePolicy().hasHeightForWidth())
        self.button_mul.setSizePolicy(sizePolicy2)
        self.button_mul.setStyleSheet(u"QPushButton {\n"
"    background-color: #07575B;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #66A5AD;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #003B46;\n"
"}")

        self.layout_buttons.addWidget(self.button_mul, 2, 3, 1, 1)

        self.button_4 = QPushButton(self.centralwidget)
        self.button_4.setObjectName(u"button_4")
        sizePolicy2.setHeightForWidth(self.button_4.sizePolicy().hasHeightForWidth())
        self.button_4.setSizePolicy(sizePolicy2)
        self.button_4.setStyleSheet(u"QPushButton {\n"
"    background-color: #66A5AD;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #07575B;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #07575B;\n"
"}")

        self.layout_buttons.addWidget(self.button_4, 3, 0, 1, 1)

        self.button_0 = QPushButton(self.centralwidget)
        self.button_0.setObjectName(u"button_0")
        sizePolicy2.setHeightForWidth(self.button_0.sizePolicy().hasHeightForWidth())
        self.button_0.setSizePolicy(sizePolicy2)
        self.button_0.setStyleSheet(u"QPushButton {\n"
"    background-color: #66A5AD;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #07575B;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #07575B;\n"
"}")

        self.layout_buttons.addWidget(self.button_0, 5, 1, 1, 1)

        self.button_1 = QPushButton(self.centralwidget)
        self.button_1.setObjectName(u"button_1")
        sizePolicy2.setHeightForWidth(self.button_1.sizePolicy().hasHeightForWidth())
        self.button_1.setSizePolicy(sizePolicy2)
        self.button_1.setStyleSheet(u"QPushButton {\n"
"    background-color: #66A5AD;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #07575B;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #07575B;\n"
"}")

        self.layout_buttons.addWidget(self.button_1, 4, 0, 1, 1)

        self.button_9 = QPushButton(self.centralwidget)
        self.button_9.setObjectName(u"button_9")
        sizePolicy2.setHeightForWidth(self.button_9.sizePolicy().hasHeightForWidth())
        self.button_9.setSizePolicy(sizePolicy2)
        self.button_9.setStyleSheet(u"QPushButton {\n"
"    background-color: #66A5AD;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #07575B;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #07575B;\n"
"}")

        self.layout_buttons.addWidget(self.button_9, 2, 2, 1, 1)

        self.button_equal = QPushButton(self.centralwidget)
        self.button_equal.setObjectName(u"button_equal")
        sizePolicy2.setHeightForWidth(self.button_equal.sizePolicy().hasHeightForWidth())
        self.button_equal.setSizePolicy(sizePolicy2)
        self.button_equal.setStyleSheet(u"QPushButton {\n"
"    background-color: #07575B;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #66A5AD;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #003B46;\n"
"}")

        self.layout_buttons.addWidget(self.button_equal, 5, 3, 1, 1)

        self.button_neg = QPushButton(self.centralwidget)
        self.button_neg.setObjectName(u"button_neg")
        sizePolicy2.setHeightForWidth(self.button_neg.sizePolicy().hasHeightForWidth())
        self.button_neg.setSizePolicy(sizePolicy2)
        self.button_neg.setStyleSheet(u"QPushButton {\n"
"    background-color: #66A5AD;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #07575B;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #07575B;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/C:/Users/stadn/Downloads/icons/symbol.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_neg.setIcon(icon2)
        self.button_neg.setIconSize(QSize(36, 36))

        self.layout_buttons.addWidget(self.button_neg, 5, 0, 1, 1)

        self.button_6 = QPushButton(self.centralwidget)
        self.button_6.setObjectName(u"button_6")
        sizePolicy2.setHeightForWidth(self.button_6.sizePolicy().hasHeightForWidth())
        self.button_6.setSizePolicy(sizePolicy2)
        self.button_6.setStyleSheet(u"QPushButton {\n"
"    background-color: #66A5AD;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #07575B;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #07575B;\n"
"}")

        self.layout_buttons.addWidget(self.button_6, 3, 2, 1, 1)

        self.button_square_root = QPushButton(self.centralwidget)
        self.button_square_root.setObjectName(u"button_square_root")
        sizePolicy2.setHeightForWidth(self.button_square_root.sizePolicy().hasHeightForWidth())
        self.button_square_root.setSizePolicy(sizePolicy2)
        self.button_square_root.setStyleSheet(u"QPushButton {\n"
"    background-color: #07575B;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #66A5AD;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #003B46;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/C:/Users/stadn/Downloads/icons/sqr_x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_square_root.setIcon(icon3)
        self.button_square_root.setIconSize(QSize(50, 50))

        self.layout_buttons.addWidget(self.button_square_root, 1, 2, 1, 1)

        self.button_one_div_x = QPushButton(self.centralwidget)
        self.button_one_div_x.setObjectName(u"button_one_div_x")
        sizePolicy2.setHeightForWidth(self.button_one_div_x.sizePolicy().hasHeightForWidth())
        self.button_one_div_x.setSizePolicy(sizePolicy2)
        self.button_one_div_x.setStyleSheet(u"QPushButton {\n"
"    background-color: #07575B;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #66A5AD;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #003B46;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/C:/Users/stadn/Downloads/icons/1_div_x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_one_div_x.setIcon(icon4)
        self.button_one_div_x.setIconSize(QSize(36, 36))

        self.layout_buttons.addWidget(self.button_one_div_x, 1, 0, 1, 1)

        self.button_7 = QPushButton(self.centralwidget)
        self.button_7.setObjectName(u"button_7")
        sizePolicy2.setHeightForWidth(self.button_7.sizePolicy().hasHeightForWidth())
        self.button_7.setSizePolicy(sizePolicy2)
        self.button_7.setStyleSheet(u"QPushButton {\n"
"    background-color: #66A5AD;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #07575B;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #07575B;\n"
"}")

        self.layout_buttons.addWidget(self.button_7, 2, 0, 1, 1)

        self.button_add = QPushButton(self.centralwidget)
        self.button_add.setObjectName(u"button_add")
        sizePolicy2.setHeightForWidth(self.button_add.sizePolicy().hasHeightForWidth())
        self.button_add.setSizePolicy(sizePolicy2)
        self.button_add.setStyleSheet(u"QPushButton {\n"
"    background-color: #07575B;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #66A5AD;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #003B46;\n"
"}")

        self.layout_buttons.addWidget(self.button_add, 4, 3, 1, 1)

        self.button_5 = QPushButton(self.centralwidget)
        self.button_5.setObjectName(u"button_5")
        sizePolicy2.setHeightForWidth(self.button_5.sizePolicy().hasHeightForWidth())
        self.button_5.setSizePolicy(sizePolicy2)
        self.button_5.setStyleSheet(u"QPushButton {\n"
"    background-color: #66A5AD;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #07575B;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #07575B;\n"
"}")

        self.layout_buttons.addWidget(self.button_5, 3, 1, 1, 1)

        self.button_div = QPushButton(self.centralwidget)
        self.button_div.setObjectName(u"button_div")
        sizePolicy2.setHeightForWidth(self.button_div.sizePolicy().hasHeightForWidth())
        self.button_div.setSizePolicy(sizePolicy2)
        self.button_div.setStyleSheet(u"QPushButton {\n"
"    background-color: #07575B;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #66A5AD;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #003B46;\n"
"}")

        self.layout_buttons.addWidget(self.button_div, 1, 3, 1, 1)

        self.button_backspace = QPushButton(self.centralwidget)
        self.button_backspace.setObjectName(u"button_backspace")
        sizePolicy2.setHeightForWidth(self.button_backspace.sizePolicy().hasHeightForWidth())
        self.button_backspace.setSizePolicy(sizePolicy2)
        self.button_backspace.setStyleSheet(u"QPushButton {\n"
"    background-color: #07575B;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #66A5AD;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #003B46;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/C:/Users/stadn/Downloads/icons/backspace.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_backspace.setIcon(icon5)
        self.button_backspace.setIconSize(QSize(24, 16))

        self.layout_buttons.addWidget(self.button_backspace, 0, 3, 1, 1)

        self.button_clear = QPushButton(self.centralwidget)
        self.button_clear.setObjectName(u"button_clear")
        sizePolicy2.setHeightForWidth(self.button_clear.sizePolicy().hasHeightForWidth())
        self.button_clear.setSizePolicy(sizePolicy2)
        self.button_clear.setStyleSheet(u"QPushButton {\n"
"    background-color: #07575B;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #66A5AD;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #003B46;\n"
"}")

        self.layout_buttons.addWidget(self.button_clear, 0, 2, 1, 1)

        self.button_ce = QPushButton(self.centralwidget)
        self.button_ce.setObjectName(u"button_ce")
        sizePolicy2.setHeightForWidth(self.button_ce.sizePolicy().hasHeightForWidth())
        self.button_ce.setSizePolicy(sizePolicy2)
        self.button_ce.setStyleSheet(u"QPushButton {\n"
"    background-color: #07575B;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #66A5AD;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #003B46;\n"
"}")

        self.layout_buttons.addWidget(self.button_ce, 0, 1, 1, 1)

        self.button_interest = QPushButton(self.centralwidget)
        self.button_interest.setObjectName(u"button_interest")
        sizePolicy2.setHeightForWidth(self.button_interest.sizePolicy().hasHeightForWidth())
        self.button_interest.setSizePolicy(sizePolicy2)
        self.button_interest.setStyleSheet(u"QPushButton {\n"
"    background-color: #07575B;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #66A5AD;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #003B46;\n"
"}")

        self.layout_buttons.addWidget(self.button_interest, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.layout_buttons)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.label_temp.setText("")
        self.line_edit_entry.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.button_sub.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        self.button_sub.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.button_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.button_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.button_dot.setText(QCoreApplication.translate("MainWindow", u".", None))
#if QT_CONFIG(shortcut)
        self.button_dot.setShortcut(QCoreApplication.translate("MainWindow", u".", None))
#endif // QT_CONFIG(shortcut)
        self.button_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.button_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.button_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.button_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.button_square.setText("")
        self.button_mul.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
#if QT_CONFIG(shortcut)
        self.button_mul.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.button_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.button_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.button_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.button_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.button_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.button_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.button_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.button_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.button_equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)
        self.button_equal.setShortcut(QCoreApplication.translate("MainWindow", u"=", None))
#endif // QT_CONFIG(shortcut)
        self.button_neg.setText("")
        self.button_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.button_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.button_square_root.setText("")
        self.button_one_div_x.setText("")
        self.button_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.button_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.button_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.button_add.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.button_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.button_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.button_div.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
#if QT_CONFIG(shortcut)
        self.button_div.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.button_backspace.setText("")
#if QT_CONFIG(shortcut)
        self.button_backspace.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.button_clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.button_ce.setText(QCoreApplication.translate("MainWindow", u"CE", None))
#if QT_CONFIG(shortcut)
        self.button_ce.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.button_interest.setText(QCoreApplication.translate("MainWindow", u"%", None))
#if QT_CONFIG(shortcut)
        self.button_interest.setShortcut(QCoreApplication.translate("MainWindow", u"%", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

