# -*- coding: utf-8 -*-
#!/usr/bin/env python

import logging
import os
import sys
#import threading,time
import time
#from PyQt5 import QtSvg
from OCC.Core.BRepBndLib import brepbndlib_Add
from OCC.Core.BRepGProp import brepgprop_SurfaceProperties, brepgprop_VolumeProperties
from OCC.Core.BRepMesh import BRepMesh_IncrementalMesh
from OCC.Core.BRepTools import breptools_Write
from OCC.Core.Bnd import Bnd_Box
from OCC.Core.GProp import GProp_GProps
from OCC.Core.TCollection import TCollection_ExtendedString
from OCC.Core.gp import gp_Pnt

from OCC.Display.OCCViewer import OffscreenRenderer
from OCC.Display.backend import load_backend, get_qt_modules
from OCC.Extend.TopologyUtils import TopologyExplorer
from PyQt5.QtWidgets import QHBoxLayout, QDockWidget, \
    QListWidget, QFileDialog
#from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtWidgets
#from graphics import GraphicsView, GraphicsPixmapItem
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Display.SimpleGui import init_display
from OCC.Core.BRepTools import breptools_Read,breptools_Write
from OCC.Core.TopoDS import TopoDS_Shape, topods_Edge, topods_Face, TopoDS_Solid
from OCC.Core.BRep import BRep_Builder
from OCC.Display.SimpleGui import init_display
from OCC.Extend.DataExchange import read_iges_file,read_step_file,read_stl_file
from OCC.Core.TopAbs import (TopAbs_FACE, TopAbs_EDGE, TopAbs_VERTEX,
                             TopAbs_SHELL, TopAbs_SOLID)
import Vision
from PyQt5.QtGui import QPixmap ,QFont
from OCC.Core.AIS import AIS_Shape, AIS_RadiusDimension,AIS_AngleDimension,AIS_LengthDimension
from OCC.Core.gp import (gp_Pnt2d, gp_Ax2d, gp_Dir2d, gp_Circ2d, gp_Origin2d, gp_DX2d,
                         gp_Ax2, gp_OX2d, gp_Lin2d, gp_Trsf, gp_XOY,
                         gp_Pnt, gp_Vec, gp_Ax3, gp_Pln, gp_Origin, gp_DX, gp_DY,
                         gp_DZ, gp_OZ)




#------------------------------------------------------------开始初始化环境
import core_geometry_bounding_box

log = logging.getLogger(__name__)
def check_callable(_callable):
    if not callable(_callable):
        raise AssertionError("The function supplied is not callable")
backend_str=None
size=[850, 873]
display_triedron=True
background_gradient_color1=[206, 215, 222]
background_gradient_color2=[128, 128, 128]
if os.getenv("PYTHONOCC_OFFSCREEN_RENDERER") == "1":
    # create the offscreen renderer
    offscreen_renderer = OffscreenRenderer()


    def do_nothing(*kargs, **kwargs):
        """ takes as many parameters as you want,
        ans does nothing
        """
        pass


    def call_function(s, func):
        """ A function that calls another function.
        Helpfull to bypass add_function_to_menu. s should be a string
        """
        check_callable(func)
        log.info("Execute %s :: %s menu fonction" % (s, func.__name__))
        func()
        log.info("done")

    # returns empty classes and functions
used_backend = load_backend(backend_str)
log.info("GUI backend set to: %s", used_backend)
#------------------------------------------------------------初始化结束
from OCC.Display.qtDisplay import qtViewer3d
import MainGui
import Create_price_parameter
from PyQt5.QtGui import QPixmap
QtCore, QtGui, QtWidgets, QtOpenGL = get_qt_modules()
from OCC.Extend.DataExchange import read_step_file,write_step_file,write_iges_file,write_stl_file
from OCC.Core.TopoDS import TopoDS_Shape,TopoDS_Builder,TopoDS_Compound,topods_CompSolid ,topods_Solid,topods_Shell,TopoDS_Face,TopoDS_Face,TopoDS_Shell



class Mywindown(QtWidgets.QMainWindow,MainGui.Ui_MainWindow,Create_price_parameter.price_parameter):
    pass
    def __init__(self, parent=None):
        super(Mywindown,self).__init__(parent)
        self.setupUi(self)
        #3D显示设置
        self.canva = qtViewer3d(self.tab)#链接3D模块
        self.setWindowTitle("三维模型测量软件")
        #self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.setFixedSize(self.width(), self.height());
        self.canva.setGeometry(QtCore.QRect(0, 0, 481, 515))
        self.centerOnScreen()
        #------------------------------------------------------------------视图设置
        self.quit.triggered.connect(self.Quit)
        self.actionView_Right.triggered.connect(self.View_Right)
        self.actionView_Left.triggered.connect(self.View_Left)
        self.actionView_Top.triggered.connect(self.View_Top)
        self.actionView_Bottom.triggered.connect(self.View_Bottom)
        self.actionView_Front.triggered.connect(self.View_Front)
        self.actionView_Iso.triggered.connect(self.View_Iso)
        self.imprt_part.triggered.connect(self.Import_part)
        self.measure.triggered.connect(self.set_measure_signal)
        self.Output_stp.triggered.connect(self.Output_stp_data)
        self.Output_iges.triggered.connect(self.Output_iges_data)
        self.Output_stl.triggered.connect(self.Output_stl_data)
        self.measure_signal=0
        #------------------------------------------------------------尺寸数据显示设置

        #--------------------------------------------------------------状态栏
        self.statusBar().showMessage('状态：软件运行正常')



        #--------------------------------------------------------------控件更新信号
        self.radioButton_3.clicked.connect(self.choose_filt_face)
        self.radioButton_4.clicked.connect(self.choose_filt_shape)
        self.tabWidget.tabBarClicked.connect(self.updata_show_1)
        self.comboBox.currentTextChanged.connect(self.updata_show_1)
        self.comboBox_2.currentTextChanged.connect(self.updata_show_2)
        self.comboBox_3.currentTextChanged.connect(self.updata_show_3)


        #self.manufacture=self.comboBox.currentText()

        #-----------------------------------------------------------------------初始化变量
        self.shape = TopoDS_Shape
        self.filename=str()

    def View_Bottom(self):
        pass
        self.canva._display.View_Bottom()
    def View_Front(self):
        pass
        self.canva._display.View_Front()
    def View_Iso(self):
        pass
        self.canva._display.View_Iso()

    def View_Left(self):
        pass
        self.canva._display.View_Left()
    def View_Right(self):
        pass
        self.canva._display.View_Right()

    def View_Top(self):
        pass
        self.canva._display.View_Top()

    def centerOnScreen(self):
        '''Centers the window on the screen.'''
        resolution = QtWidgets.QApplication.desktop().screenGeometry()
        x = (resolution.width() - self.frameSize().width()) / 2
        y = (resolution.height() - self.frameSize().height()) / 2
        self.move(x, y)
    #选择器---------------------------------------------------------------
    def choose_filt_face(self):
        if self.radioButton_3.isChecked():
            self.canva._display.SetSelectionModeNeutral()
            self.canva._display.SetSelectionMode(TopAbs_FACE)
            #print("选择面")
    def choose_filt_shape(self):
        if self.radioButton_4.isChecked():
            self.canva._display.SetSelectionModeNeutral()
            self.canva._display.SetSelectionMode(TopAbs_SOLID)

            #print("选择体")

    # 选择器---------------------------------------------------------------

    def set_measure_signal(self):#测量信号 只有测量完成后才会显示体积 表面积等参数
        self.measure_signal=1
    #-------------导入3D数据-----------------------------
    def Import_part(self):#导入数据
        pass
        #清除之前数据
        self.clear_show()
        try:
            self.chose_document = QFileDialog.getOpenFileName(self,'打开文件','./',
            " STP files(*.stp , *.step);;(*.iges);;(*.stl)")  # 选择转换的文价夹
            filepath=self.chose_document[0]#获取打开文件夹路径
            #判断文件类型 选择对应的导入函数
            end_with=str(filepath).lower()
            if end_with.endswith(".step") or end_with.endswith("stp"):
                self.import_shape=read_step_file(filepath)

            elif end_with.endswith("iges"):
                self.import_shape=read_iges_file(filepath)
            elif end_with.endswith("stl"):
                self.import_shape=read_stl_file(filepath)
            self.Show_3d_model()
            self.Make_diamension()
            print("ok")
            self.statusbar.showMessage("状态：打开成功")  ###
            self.statusBar().showMessage('状态：软件运行正常')
        except:
            pass
    def Output_stp_data(self):#将数据转换成stp并导出
        try:
            pass
            self.part_name = self.chose_document[0].split("/")  # 获取路径最后一个
            self.part_name = self.part_name[-1].split(".")  # 获取去除后缀的名字
            path = "./" + self.part_name[0]
            fileName, ok = QFileDialog.getSaveFileName(self, "文件保存", path, "All Files (*) (*.step)")
            fileName = fileName.split("/")
            fileName = fileName[0] + "\\" + fileName[1] + "\\" + fileName[2]+"\\"+self.part_name[0]+".step"
            write_step_file(self.import_shape, fileName)

        except:
            pass
            self.statusBar().showMessage('错误：没用模型可以导出')
    def Output_iges_data(self):#将数据转换成iges并导出
        try:
            pass
            self.part_name = self.chose_document[0].split("/")  # 获取路径最后一个
            self.part_name = self.part_name[-1].split(".")  # 获取去除后缀的名字
            path = "./" + self.part_name[0]
            fileName, ok = QFileDialog.getSaveFileName(self, "文件保存", path, "All Files (*) (*.iges)")
            fileName = fileName.split("/")
            fileName = fileName[0] + "\\" + fileName[1] + "\\" + fileName[2]+"\\"+self.part_name[0]+".iges"
            write_iges_file(self.import_shape, fileName)

        except:
            pass
            self.statusBar().showMessage('错误：没用模型可以导出')
    def Output_stl_data(self):#stl
        try:
            pass
            self.part_name = self.chose_document[0].split("/")  # 获取路径最后一个
            self.part_name = self.part_name[-1].split(".")  # 获取去除后缀的名字
            path = "./" + self.part_name[0]
            fileName, ok = QFileDialog.getSaveFileName(self, "文件保存", path, "All Files (*) (*.iges)")
            fileName = fileName.split("/")
            fileName = fileName[0] + "\\" + fileName[1] + "\\" + fileName[2]+"\\"+self.part_name[0]+".stl"
            write_stl_file(self.import_shape, fileName)

        except:
            pass
            self.statusBar().showMessage('错误：没用模型可以导出')
    #-------------显示3D数据------------------------------------
    def Show_3d_model(self):#显示3D数据

        try:
            #self.canva._display.Context.Remove(self.show[0], True)
            self.canva._display.EraseAll()
            self.canva._display.hide_triedron()
            self.canva._display.display_triedron()
            self.aCompound.Free()
            
        except:
            pass
            self.show = self.canva._display.DisplayShape(self.import_shape, color="WHITE", update=True)
            self.canva._display.FitAll()

        return True
    #-----------------------将获取参数输入文件信息界面--------------------------------
    def Input_data_gui(self):
        pass
        try:
            #获取零件名字输入到文件参数
            self.part_name=self.chose_document[0].split("/")#获取路径最后一个
            self.part_name=self.part_name[-1].split(".")#获取去除后缀的名字
            self.lineEdit_5.setText(str(self.part_name[0]))
            #h获取表面积输入到文件参数
            self.lineEdit_7.setText(str(self.part_surface)+" mm^2")
            #获取体积并输入到文件参数
            self.lineEdit_8.setText(str(self.part_volume)+"  mm^3")
            #获取复杂度并输入到文件参数
            self.lineEdit_9.setText(str(0.26))
            #获取最大尺寸并输入到文件参数
            max_x="{:.2f}".format(self.max_diamension[0])
            max_y = "{:.2f}".format(self.max_diamension[1])
            max_z = "{:.2f}".format(self.max_diamension[2])
            ls_max_diamention=str(max_x)+"*"+str(max_y)+"*"+str(max_z)+"mm"
            self.lineEdit_6.setText(ls_max_diamention)
        except:
            pass
    #--------------清除之前的数据------------------------------------
    def clear_show(self):#清除之前数据
        self.lineEdit_2.clear()
        self.lineEdit.clear()
        self.lineEdit_3.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()
        self.lineEdit_9.clear()
        self.lineEdit_10.clear()
        self.tableWidget.clear()
    #-----------点击测量物体的回调函数 并获取体积表面积--------------------------
    def line_clicked(self,shp, *kwargs):
        """ This function is called whenever a line is selected
        """
        if self.measure_signal==1:#确认是否已经进行测量
            pass
            for i in shp:#获取最大尺寸
                for e in TopologyExplorer(i).solids():
                    self.max_diamension = core_geometry_bounding_box.get_boundingbox(e)
            for i in shp:#获取体积 质量
                try:
                    #print(i)

                    pass
                    props = GProp_GProps()  # 测量属性的类
                    brepgprop_VolumeProperties(i, props)  # 设置测量属性为体积
                    # Get inertia properties
                    mass = "{:.3f}".format(props.Mass())  # 获取体积
                    self.lineEdit_3.setText(str(mass) + " mm^3")  # 输入到文本框
                    self.part_volume=mass
                    # 计算质量
                    mass = props.Mass()  # 再次获取体积
                    density = (float(self.lineEdit_4.text()))  # 获取密度
                    m = mass * density
                    m = "{:.3f}".format(m)
                    self.lineEdit_2.setText(str(m) + " g")  # 输入到文本框
                    self.statusBar().showMessage('状态：计算成功')

                except:
                    pass
                    self.statusBar().showMessage('状态：计算错误 所选模型错误')
                # 测量表面积
                for i in shp:
                    try:
                        pass
                        all_face_add_area = 0  # 初始化物体表面积
                        t = TopologyExplorer(i)
                        props = GProp_GProps()  # 测量属性的类
                        brepgprop_SurfaceProperties(i, props)  # 设置测量属性为面积
                        for face in t.faces():
                            brepgprop_SurfaceProperties(face, props)
                            face_surf = props.Mass()  # 获取面的面积
                            all_face_add_area += face_surf  # 循环求所有表面积之和
                        all_face_add_area = "{:.2f}".format(props.Mass())  # 获取体积
                        self.lineEdit.setText(str(all_face_add_area) + " mm^2")  # 输入到文本框
                        self.part_surface=all_face_add_area
                    except:
                        pass
                        self.statusBar().showMessage('状态：计算错误 所选模型错误')
                        # print("失败")
        self.measure_signal=0
        self.Input_data_gui()


    def updata_show_1(self):#更新制造参数界面 对应combox改变更新界面
        try:
            new_parameter=Create_price_parameter.price_parameter()#初始化类
            #-------------------根据选择更新界面
            if True:
                pass
                self.manufacture=self.comboBox.currentText()
                if self.manufacture=="金属烧结（SLM）":
                    self.comboBox_2.clear()
                    for item in new_parameter.dict_price_parameter_slm.keys():
                         self.comboBox_2.addItem(item)
                elif self.manufacture=="粉末烧结（SLS）":
                    self.comboBox_2.clear()
                    for item in new_parameter.dict_price_parameter_sls.keys():
                         self.comboBox_2.addItem(item)
                    self.comboBox_3.setCurrentText("-")
                elif self.manufacture == "光固化（SLA）":
                    self.comboBox_2.clear()
                    for item in new_parameter.dict_price_parameter_sla.keys():
                        self.comboBox_2.addItem(item)
            #计算数据 在界面显示计算得出的数据
            self.material=self.comboBox_2.currentText()#获取界面选取的材料
            self.process=self.comboBox_3.currentText()#获取处理方式
            self.average_price=new_parameter.manufacture_parameter[self.manufacture[5:8]][self.material]["price"]#获取单价 元/克
            self.density=new_parameter.manufacture_parameter[self.manufacture[5:8]][self.material]["density"]#获取密度 单位立方厘米/g
            if self.process=="普通级":
                pass
                self.process_series=1.0
            elif self.process=="精密级":
                pass
                self.process_series = 1.1
            elif self.process=="高难度级":
                self.process_series = 1.2
            elif self.process=="-":
                pass
                self.process_series = 1.0
            self.quality=float(self.part_volume)/1000*self.density
            self.quality="{:.2f}".format(self.quality)
            #获取处理方式

            self.price=float(self.quality)*self.average_price
            self.lineEdit_10.setText(str(self.quality)+" g")#填入界面中

            if True:
                pass

                #零件名字写入单元格
                self.tableWidget.setHorizontalHeaderLabels(['零件名', '单价（元/克）', '数量（个）',"总价（元）"])
                newItem = QtWidgets.QTableWidgetItem(str(self.part_name[0]))
                self.tableWidget.setItem(0, 0, newItem)  # 零件名称
                newItem.setBackground(QtGui.QBrush(QtGui.QColor(240, 255, 191)))  # 设置背景颜色
                newItem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)  # 文字居中
                newItem.setFont(QFont("song", 9, QFont.Black))#设置单元格背景 字体
                #----------------------------单价写入单元格
                newItem = QtWidgets.QTableWidgetItem(str(self.average_price))
                self.tableWidget.setItem(0, 1, newItem)  # 代码
                newItem.setBackground(QtGui.QBrush(QtGui.QColor(240, 255, 191)))  # 设置背景颜色
                newItem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)  # 文字居中
                newItem.setFont(QFont("song", 9, QFont.Black))  # 设置单元格背景 字体
                #-------------------------------数量写入单元格 默认为1
                newItem = QtWidgets.QTableWidgetItem("1")
                self.tableWidget.setItem(0, 2, newItem)  # 代码
                newItem.setBackground(QtGui.QBrush(QtGui.QColor(240, 255, 191)))  # 设置背景颜色
                newItem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)  # 文字居中
                newItem.setFont(QFont("song", 9, QFont.Black))  # 设置单元格背景 字体
                #-------------------------------计算总价 写入单元格
                self.total_price=float(self.quality)*float(self.tableWidget.item(0, 1).text())*self.process_series
                self.total_price="{:.2f}".format(self.total_price)
                newItem = QtWidgets.QTableWidgetItem(str(self.total_price))
                self.tableWidget.setItem(0, 3, newItem)  # 代码
                newItem.setBackground(QtGui.QBrush(QtGui.QColor(240, 255, 191)))  # 设置背景颜色
                newItem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)  # 文字居中
                newItem.setFont(QFont("song", 9, QFont.Black))  # 设置单元格背景 字体

        except:
            pass
            #print("还未导入数据")

    def updata_show_2(self):  #更新制造参数界面 对应combox1改变更新界面
        try:
            new_parameter = Create_price_parameter.price_parameter()  # 初始化类
            # 计算数据 在界面显示计算得出的数据
            self.material = self.comboBox_2.currentText()  # 获取界面选取的材料
            self.process = self.comboBox_3.currentText()  # 获取处理方式
            average_price = new_parameter.manufacture_parameter[self.manufacture[5:8]][self.material][
                "price"]  # 获取单价 元/克
            density = new_parameter.manufacture_parameter[self.manufacture[5:8]][self.material][
                "density"]  # 获取密度 单位立方厘米/g

            self.quality = float(self.part_volume) / 1000 * density
            self.quality = "{:.2f}".format(self.quality)
            self.price = float(self.quality) * average_price
            self.lineEdit_10.setText(str(self.quality) + " g")  # 填入界面中
            if True:
                pass
                # 零件名字写入单元格
                self.tableWidget.setHorizontalHeaderLabels(['零件名', '单价（元/克）', '数量（个）', "总价（元）"])
                newItem = QtWidgets.QTableWidgetItem(str(self.part_name[0]))
                self.tableWidget.setItem(0, 0, newItem)  # 零件名称
                newItem.setBackground(QtGui.QBrush(QtGui.QColor(240, 255, 191)))  # 设置背景颜色
                newItem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)  # 文字居中
                newItem.setFont(QFont("song", 9, QFont.Black))  # 设置单元格背景 字体
                # ----------------------------单价写入单元格
                newItem = QtWidgets.QTableWidgetItem(str(self.average_price))
                self.tableWidget.setItem(0, 1, newItem)  # 代码
                newItem.setBackground(QtGui.QBrush(QtGui.QColor(240, 255, 191)))  # 设置背景颜色
                newItem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)  # 文字居中
                newItem.setFont(QFont("song", 9, QFont.Black))  # 设置单元格背景 字体
                # -------------------------------数量写入单元格 默认为1
                newItem = QtWidgets.QTableWidgetItem("1")
                self.tableWidget.setItem(0, 2, newItem)  # 代码
                newItem.setBackground(QtGui.QBrush(QtGui.QColor(240, 255, 191)))  # 设置背景颜色
                newItem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)  # 文字居中
                newItem.setFont(QFont("song", 9, QFont.Black))  # 设置单元格背景 字体
                # -------------------------------计算总价 写入单元格
                self.total_price = float(self.quality) * float(self.tableWidget.item(0, 1).text()) * self.process_series
                self.total_price = "{:.2f}".format(self.total_price)
                newItem = QtWidgets.QTableWidgetItem(str(self.total_price))
                self.tableWidget.setItem(0, 3, newItem)  # 代码
                newItem.setBackground(QtGui.QBrush(QtGui.QColor(240, 255, 191)))  # 设置背景颜色
                newItem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)  # 文字居中
                newItem.setFont(QFont("song", 9, QFont.Black))  # 设置单元格背景 字体
        except:
            pass


    def updata_show_3(self): #更新制造参数界面 对应combox2改变更新界面
        try:
            new_parameter = Create_price_parameter.price_parameter()  # 初始化类
            # 计算数据 在界面显示计算得出的数据
            self.material = self.comboBox_2.currentText()  # 获取界面选取的材料
            self.process = self.comboBox_3.currentText()  # 获取处理方式
            average_price = new_parameter.manufacture_parameter[self.manufacture[5:8]][self.material][
                "price"]  # 获取单价 元/克
            density = new_parameter.manufacture_parameter[self.manufacture[5:8]][self.material][
                "density"]  # 获取密度 单位立方厘米/g

            self.quality = float(self.part_volume) / 1000 * density
            self.quality = "{:.2f}".format(self.quality)
            self.price = float(self.quality) * average_price
            self.lineEdit_10.setText(str(self.quality) + " g")  # 填入界面中
            if True:
                pass
                # 零件名字写入单元格
                self.tableWidget.setHorizontalHeaderLabels(['零件名', '单价（元/克）', '数量（个）', "总价（元）"])
                newItem = QtWidgets.QTableWidgetItem(str(self.part_name[0]))
                self.tableWidget.setItem(0, 0, newItem)  # 零件名称
                newItem.setBackground(QtGui.QBrush(QtGui.QColor(240, 255, 191)))  # 设置背景颜色
                newItem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)  # 文字居中
                newItem.setFont(QFont("song", 9, QFont.Black))  # 设置单元格背景 字体
                # ----------------------------单价写入单元格
                newItem = QtWidgets.QTableWidgetItem(str(self.average_price)  )
                self.tableWidget.setItem(0, 1, newItem)  # 代码
                newItem.setBackground(QtGui.QBrush(QtGui.QColor(240, 255, 191)))  # 设置背景颜色
                newItem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)  # 文字居中
                newItem.setFont(QFont("song", 9, QFont.Black))  # 设置单元格背景 字体
                # -------------------------------数量写入单元格 默认为1
                newItem = QtWidgets.QTableWidgetItem("1")
                self.tableWidget.setItem(0, 2, newItem)  # 代码
                newItem.setBackground(QtGui.QBrush(QtGui.QColor(240, 255, 191)))  # 设置背景颜色
                newItem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)  # 文字居中
                newItem.setFont(QFont("song", 9, QFont.Black))  # 设置单元格背景 字体
                # -------------------------------计算总价 写入单元格
                self.total_price = float(self.quality) * float(self.tableWidget.item(0, 1).text()) * self.process_series
                self.total_price = "{:.2f}".format(self.total_price)
                newItem = QtWidgets.QTableWidgetItem(str(self.total_price) )
                self.tableWidget.setItem(0, 3, newItem)  # 代码
                newItem.setBackground(QtGui.QBrush(QtGui.QColor(240, 255, 191)))  # 设置背景颜色
                newItem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)  # 文字居中
                newItem.setFont(QFont("song", 9, QFont.Black))  # 设置单元格背景 字体
        except:
            pass

    def Make_diamension(self):
        pt1=gp_Pnt(-19.82,-16.200792819,0.000000000)
        pt2=gp_Pnt(-19.82,-32.200792819,0)
        plane= gp_Pln(gp_Origin(), gp_DZ())
        am = AIS_LengthDimension(pt1,pt2,plane)
        a123=TCollection_ExtendedString("k")
        am.SetCustomValue(a123)
        am.HilightOwnerWithColor

        self.canva._display.Context.Display(am, True)
        print("9999")


    def Quit(self):#退出
        self.close()

    def Vision(self):#版本显示
        pass




class Vision(QtWidgets.QMainWindow,Vision.Ui_Form):
    def __init__(self,parent=None):
        super(Vision, self).__init__(parent)
        self.setupUi(self)
        global part_volume
        global part_surface_area







# following couple of lines is a tweak to enable ipython --gui='qt'
if __name__ == '__main__':
    app = QtWidgets.QApplication.instance()  # checks if QApplication already exists
    if not app:  # create QApplication if it doesnt exist
        app = QtWidgets.QApplication(sys.argv)
    #启动界面
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap("Pic\\setup_pic.jpg"))#启动图片设置
    splash.show()
    splash.showMessage("软件启动中......")
    time.sleep(0.5)
    #--------------------
    win = Mywindown()
    win_calculation=Vision()
    win.calculation.triggered.connect(win_calculation.show)
    win.show()
    win.centerOnScreen()
    win.canva.InitDriver()
    win.resize(size[0], size[1])
    win.canva.qApp = app

    display = win.canva._display
    display.display_triedron()
    display.register_select_callback(win.line_clicked)
    if background_gradient_color1 and background_gradient_color2:
    # background gradient
        display.set_bg_gradient_color(background_gradient_color1, background_gradient_color2)
    win.raise_()  # make the application float to the top
    splash.finish(win)

    app.exec_()