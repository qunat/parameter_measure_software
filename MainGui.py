# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainGui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 776)
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        MainWindow.setToolTip("")
        MainWindow.setToolTipDuration(-3)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 851, 110))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("Pic/666.jpg"))
        self.label_5.setObjectName("label_5")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 640, 351, 81))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(21, 40, 321, 27))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_3 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 0, 0, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout.addWidget(self.radioButton_4, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(380, 640, 471, 111))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget_2.setGeometry(QtCore.QRect(30, 30, 411, 71))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_3.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_2.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_4.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_4.addWidget(self.lineEdit_4)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 130, 341, 501))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.frame = QtWidgets.QFrame(self.tab_3)
        self.frame.setGeometry(QtCore.QRect(-40, 20, 371, 401))
        self.frame.setObjectName("frame")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(50, 51, 48, 21))
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(110, 51, 250, 27))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(110, 126, 250, 27))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(60, 126, 32, 21))
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_7.setGeometry(QtCore.QRect(110, 201, 250, 27))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(50, 201, 48, 21))
        self.label_8.setObjectName("label_8")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_8.setGeometry(QtCore.QRect(110, 276, 250, 27))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(50, 276, 32, 21))
        self.label_9.setObjectName("label_9")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_9.setGeometry(QtCore.QRect(110, 351, 250, 27))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(50, 351, 48, 21))
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.widget = QtWidgets.QWidget(self.tab_4)
        self.widget.setGeometry(QtCore.QRect(10, 40, 351, 381))
        self.widget.setObjectName("widget")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(150, 2, 131, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setGeometry(QtCore.QRect(2, 2, 64, 21))
        self.label_11.setObjectName("label_11")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setGeometry(QtCore.QRect(150, 111, 131, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setGeometry(QtCore.QRect(2, 111, 32, 21))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setGeometry(QtCore.QRect(2, 220, 48, 21))
        self.label_13.setObjectName("label_13")
        self.comboBox_3 = QtWidgets.QComboBox(self.widget)
        self.comboBox_3.setGeometry(QtCore.QRect(150, 220, 131, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_10.setGeometry(QtCore.QRect(150, 328, 131, 27))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setGeometry(QtCore.QRect(2, 328, 48, 21))
        self.label_14.setObjectName("label_14")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 321, 441))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(11)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(87)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget.verticalHeader().setDefaultSectionSize(36)
        self.tableWidget.verticalHeader().setMinimumSectionSize(27)
        self.tabWidget.addTab(self.tab_5, "")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setGeometry(QtCore.QRect(360, 120, 481, 521))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget_2.addTab(self.tab, "")
        self.groupBox_2.raise_()
        self.label_5.raise_()
        self.groupBox.raise_()
        self.tabWidget.raise_()
        self.tabWidget_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 850, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.menu.setFont(font)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menuBar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menuBar)
        self.menu_4.setObjectName("menu_4")
        self.menu_V = QtWidgets.QMenu(self.menuBar)
        self.menu_V.setObjectName("menu_V")
        MainWindow.setMenuBar(self.menuBar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setCheckable(False)
        self.action.setObjectName("action")
        self.quit = QtWidgets.QAction(MainWindow)
        self.quit.setObjectName("quit")
        self.action112 = QtWidgets.QAction(MainWindow)
        self.action112.setObjectName("action112")
        self.calculation = QtWidgets.QAction(MainWindow)
        self.calculation.setObjectName("calculation")
        self.actionView_Bottom = QtWidgets.QAction(MainWindow)
        self.actionView_Bottom.setObjectName("actionView_Bottom")
        self.actionView_Front = QtWidgets.QAction(MainWindow)
        self.actionView_Front.setObjectName("actionView_Front")
        self.actionView_Iso = QtWidgets.QAction(MainWindow)
        self.actionView_Iso.setObjectName("actionView_Iso")
        self.actionView_Left = QtWidgets.QAction(MainWindow)
        self.actionView_Left.setObjectName("actionView_Left")
        self.actionView_Right = QtWidgets.QAction(MainWindow)
        self.actionView_Right.setObjectName("actionView_Right")
        self.actionView_Top = QtWidgets.QAction(MainWindow)
        self.actionView_Top.setObjectName("actionView_Top")
        self.measure = QtWidgets.QAction(MainWindow)
        self.measure.setObjectName("measure")
        self.imprt_part = QtWidgets.QAction(MainWindow)
        self.imprt_part.setObjectName("imprt_part")
        self.Output_stl = QtWidgets.QAction(MainWindow)
        self.Output_stl.setObjectName("Output_stl")
        self.Output_stp = QtWidgets.QAction(MainWindow)
        self.Output_stp.setObjectName("Output_stp")
        self.Output_iges = QtWidgets.QAction(MainWindow)
        self.Output_iges.setObjectName("Output_iges")
        self.menu.addAction(self.quit)
        self.menu_2.addAction(self.Output_stp)
        self.menu_2.addAction(self.Output_stl)
        self.menu_2.addAction(self.Output_iges)
        self.menu_3.addAction(self.actionView_Bottom)
        self.menu_3.addAction(self.actionView_Front)
        self.menu_3.addAction(self.actionView_Iso)
        self.menu_3.addAction(self.actionView_Left)
        self.menu_3.addAction(self.actionView_Right)
        self.menu_3.addAction(self.actionView_Top)
        self.menu_4.addAction(self.imprt_part)
        self.menu_V.addAction(self.measure)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_3.menuAction())
        self.menuBar.addAction(self.menu_4.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.menuBar.addAction(self.menu_V.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "选择器"))
        self.radioButton_3.setText(_translate("MainWindow", "面"))
        self.radioButton_4.setText(_translate("MainWindow", "体"))
        self.groupBox.setTitle(_translate("MainWindow", "显示数据"))
        self.label.setText(_translate("MainWindow", "表面积"))
        self.label_3.setText(_translate("MainWindow", "体积"))
        self.label_2.setText(_translate("MainWindow", "质量"))
        self.label_4.setText(_translate("MainWindow", "设置密度"))
        self.lineEdit_4.setToolTip(_translate("MainWindow", "单位：g*cm"))
        self.lineEdit_4.setText(_translate("MainWindow", "1.0"))
        self.label_6.setText(_translate("MainWindow", "文件名"))
        self.label_7.setText(_translate("MainWindow", "尺寸"))
        self.label_8.setText(_translate("MainWindow", "表面积"))
        self.label_9.setText(_translate("MainWindow", "体积"))
        self.label_10.setText(_translate("MainWindow", "复杂度"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "文件信息"))
        self.comboBox.setItemText(0, _translate("MainWindow", "金属烧结（SLM）"))
        self.comboBox.setItemText(1, _translate("MainWindow", "粉末烧结（SLS）"))
        self.comboBox.setItemText(2, _translate("MainWindow", "光固化（SLA）"))
        self.label_11.setText(_translate("MainWindow", "制造工艺"))
        self.label_12.setText(_translate("MainWindow", "材料"))
        self.label_13.setText(_translate("MainWindow", "后处理磨抛"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "普通级"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "精密级"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "高难度级"))
        self.label_14.setText(_translate("MainWindow", "质量"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "制造参数"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "11"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "零件名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "单价（元/克）"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "数量（个）"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "总价（元）"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "报价单"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "3D显示"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "导出数据"))
        self.menu_3.setTitle(_translate("MainWindow", "视图"))
        self.menu_4.setTitle(_translate("MainWindow", "导入数据"))
        self.menu_V.setTitle(_translate("MainWindow", "测量"))
        self.action.setText(_translate("MainWindow", "menu"))
        self.action.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.quit.setText(_translate("MainWindow", "退出"))
        self.action112.setText(_translate("MainWindow", "宁波启迪自动化零件有限公司"))
        self.calculation.setText(_translate("MainWindow", "报价单计算"))
        self.actionView_Bottom.setText(_translate("MainWindow", "View_Bottom"))
        self.actionView_Front.setText(_translate("MainWindow", "View_Front"))
        self.actionView_Iso.setText(_translate("MainWindow", "View_Iso"))
        self.actionView_Left.setText(_translate("MainWindow", "View_Left"))
        self.actionView_Right.setText(_translate("MainWindow", "View_Right"))
        self.actionView_Top.setText(_translate("MainWindow", "View_Top"))
        self.measure.setText(_translate("MainWindow", "测量数据"))
        self.measure.setToolTip(_translate("MainWindow", "测量数据"))
        self.imprt_part.setText(_translate("MainWindow", "导入数据"))
        self.imprt_part.setToolTip(_translate("MainWindow", "导入数据"))
        self.Output_stl.setText(_translate("MainWindow", "导出stl"))
        self.Output_stp.setText(_translate("MainWindow", "导出step/stp"))
        self.Output_stp.setToolTip(_translate("MainWindow", "转换成stp"))
        self.Output_iges.setText(_translate("MainWindow", "导出iges"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
