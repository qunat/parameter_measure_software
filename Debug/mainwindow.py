# -*- coding: UTF-8 -*-
import sys
from OCC.Core.gp import gp_Pnt
from OCC.Extend.DataExchange import read_iges_file
from PyQt5.QtGui import QIcon

from qtDisplay import qtViewer3d
from PyQt5 import  QtCore
from PyQt5.QtWidgets import QFileDialog, QAction, QApplication, QMenu, QMainWindow, QHBoxLayout, QDockWidget, \
    QListWidget, QLabel, qApp





class MainWindow(QMainWindow):
    def __init__(self, *args):
        ''' 初始化界面 '''
        # 中心控件
        # 中心控件
        QMainWindow.__init__(self, *args)
        layout=QHBoxLayout()         # 水平布局
        self.canva = qtViewer3d(self)
        # 显示设置
        self.canva.InitDriver()        # canva的驱动,设置驱动后，才能成功display
        display = self.canva._display
        display.set_bg_gradient_color([206, 215, 222], [128, 128, 128])  # 设置背景渐变色
        display.display_triedron=True   # display black trihedron
        self.setWindowTitle("Aim")
        # self.setWindowIcon(QIcon('./icons/aim.png'))        #设置程序图标
        self.setCentralWidget(self.canva)
        self.resize(1024,768)
        self.centerOnScreen()

        # 容器控件
        # 容器控件
        self.items=QDockWidget('功能区',self)
        self.listWidget=QListWidget()
        self.listWidget.addItem('item1')
        self.listWidget.addItem('item2')
        self.listWidget.addItem('item3')
        self.items.setWidget(self.listWidget)
        self.items.setFloating(False)
        print(())
        print(type(QtCore.Qt.RightDockWidgetArea))
        print(type(self.items))

        self.addDockWidget(QtCore.Qt.RightDockWidgetArea,self.items)


        # #### 菜单栏
        # #### 菜单栏

        menubar = self.menuBar()
        # 第一个菜单栏‘打开文件’
        file=menubar.addMenu('&打开文件')
        file.addAction('模型导入')
        file.addAction('打开表格文件')
        file.addAction('打开图片')

        # #### 工具栏

        #工具一：打开文件
        exitAction = QAction(QIcon('./icons/open.gif'), '打开文件', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(QFileDialog.getOpenFileName)
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        # #### label标签
        label=QLabel(self)
        label.move(900,0)
        label.setText("<a href='https://blog.csdn.net/weixin_42755384/article/details/87893697'>PythonOCC帮助</a>")
        label.setOpenExternalLinks(True)
        self.setLayout(layout)
        # 临时读入一个文件
        P0 = gp_Pnt(0, 0, 1)
        P1 = gp_Pnt(0, 30, 20)
        display.DisplayShape(P0)
        display.DisplayShape(P1)
        # display.DisplayShape(shapes,update=True)
    def centerOnScreen(self):
        '''屏幕居中'''
        resolution = QApplication.desktop().screenGeometry()
        x = (resolution.width() - self.frameSize().width()) / 2
        y = (resolution.height() - self.frameSize().height()) / 2
        self.move(x, y)



if __name__ == '__main__':
        app = QApplication(sys.argv)  # 创建应用
        win = MainWindow()            # 创建主窗口
        win.canva.qApp = app          # 将自己创建的应用与canva中的 Qapp连接起来
        win.show()                    # 主窗口显示
        win.canva.InitDriver()        # 社区反馈，添加此语句，以下的bug不会出现。
        win.raise_()                  # 窗口置顶
        sys.exit(app.exec_())
