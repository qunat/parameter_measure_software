#!/usr/bin/env python

# Copyright 2009-2016 Thomas Paviot (tpaviot@gmail.com)
##
# This file is part of pythonOCC.
##
# pythonOCC is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
##
# pythonOCC is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
##
# You should have received a copy of the GNU Lesser General Public License
# along with pythonOCC.  If not, see <http://www.gnu.org/licenses/>.

import logging
import os
import sys

from OCC import VERSION
from OCC.Display import OCCViewer
from OCC.Display.backend import load_backend, get_qt_modules
from OCC.Display.OCCViewer import OffscreenRenderer
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QListWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap,QPalette
import sys
import sys
from OCC.Core.gp import gp_Pnt
from OCC.Extend.DataExchange import read_iges_file
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox


from PyQt5 import  QtCore
from PyQt5.QtWidgets import QFileDialog, QAction, QApplication, QMenu, QMainWindow, QHBoxLayout, QDockWidget, \
    QListWidget, QLabel, qApp
import sys
from OCC.Core.gp import gp_Pnt
from OCC.Extend.DataExchange import read_iges_file
from PyQt5.QtGui import QIcon

from qtDisplay import qtViewer3d, QtWidgets, QtGui, qtBaseViewer, HAVE_PYQT_SIGNAL
from PyQt5 import  QtCore
from PyQt5.QtWidgets import QFileDialog, QAction, QApplication, QMenu, QMainWindow, QHBoxLayout, QDockWidget, \
    QListWidget, QLabel, qApp




log = logging.getLogger(__name__)


class QDockWidget(QWidget):
    """
    QDockWidget(str, parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
    QDockWidget(parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
    """
    def allowedAreas(self): # real signature unknown; restored from __doc__
        """ allowedAreas(self) -> Qt.DockWidgetAreas """
        pass

    def allowedAreasChanged(self, Union, Qt_DockWidgetAreas=None, Qt_DockWidgetArea=None): # real signature unknown; restored from __doc__
        """ allowedAreasChanged(self, Union[Qt.DockWidgetAreas, Qt.DockWidgetArea]) [signal] """
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ changeEvent(self, QEvent) """
        pass

    def closeEvent(self, QCloseEvent): # real signature unknown; restored from __doc__
        """ closeEvent(self, QCloseEvent) """
        pass

    def dockLocationChanged(self, Qt_DockWidgetArea): # real signature unknown; restored from __doc__
        """ dockLocationChanged(self, Qt.DockWidgetArea) [signal] """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def features(self): # real signature unknown; restored from __doc__
        """ features(self) -> QDockWidget.DockWidgetFeatures """
        pass

    def featuresChanged(self, Union, QDockWidget_DockWidgetFeatures=None, QDockWidget_DockWidgetFeature=None): # real signature unknown; restored from __doc__
        """ featuresChanged(self, Union[QDockWidget.DockWidgetFeatures, QDockWidget.DockWidgetFeature]) [signal] """
        pass

    def initStyleOption(self, QStyleOptionDockWidget): # real signature unknown; restored from __doc__
        """ initStyleOption(self, QStyleOptionDockWidget) """
        pass

    def isAreaAllowed(self, Qt_DockWidgetArea): # real signature unknown; restored from __doc__
        """ isAreaAllowed(self, Qt.DockWidgetArea) -> bool """
        return False

    def isFloating(self): # real signature unknown; restored from __doc__
        """ isFloating(self) -> bool """
        return False

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def setAllowedAreas(self, Union, Qt_DockWidgetAreas=None, Qt_DockWidgetArea=None): # real signature unknown; restored from __doc__
        """ setAllowedAreas(self, Union[Qt.DockWidgetAreas, Qt.DockWidgetArea]) """
        pass

    def setFeatures(self, Union, QDockWidget_DockWidgetFeatures=None, QDockWidget_DockWidgetFeature=None): # real signature unknown; restored from __doc__
        """ setFeatures(self, Union[QDockWidget.DockWidgetFeatures, QDockWidget.DockWidgetFeature]) """
        pass

    def setFloating(self, bool): # real signature unknown; restored from __doc__
        """ setFloating(self, bool) """
        pass

    def setTitleBarWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ setTitleBarWidget(self, QWidget) """
        pass

    def setWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ setWidget(self, QWidget) """
        pass

    def titleBarWidget(self): # real signature unknown; restored from __doc__
        """ titleBarWidget(self) -> QWidget """
        return QWidget

    def toggleViewAction(self): # real signature unknown; restored from __doc__
        """ toggleViewAction(self) -> QAction """
        return QAction

    def topLevelChanged(self, bool): # real signature unknown; restored from __doc__
        """ topLevelChanged(self, bool) [signal] """
        pass

    def visibilityChanged(self, bool): # real signature unknown; restored from __doc__
        """ visibilityChanged(self, bool) [signal] """
        pass

    def widget(self): # real signature unknown; restored from __doc__
        """ widget(self) -> QWidget """
        return QWidget

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AllDockWidgetFeatures = 7
    DockWidgetClosable = 1
    DockWidgetFloatable = 4
    DockWidgetMovable = 2
    DockWidgetVerticalTitleBar = 8
    NoDockWidgetFeatures = 0


def check_callable(_callable):
    if not callable(_callable):
        raise AssertionError("The function supplied is not callable")




from OCC.Display.qtDisplay import qtViewer3d
class qtViewer3d(qtBaseViewer):

    # emit signal when selection is changed
    # is a list of TopoDS_*
    if HAVE_PYQT_SIGNAL:
        sig_topods_selected = QtCore.pyqtSignal(list)

    def __init__(self, *kargs):
        qtBaseViewer.__init__(self, *kargs)

        self.setObjectName("qt_viewer_3d")

        self._drawbox = False
        self._zoom_area = False
        self._select_area = False
        self._inited = False
        self._leftisdown = False
        self._middleisdown = False
        self._rightisdown = False
        self._selection = None
        self._drawtext = True
        self._qApp = QtWidgets.QApplication.instance()
        self._key_map = {}
        self._current_cursor = "arrow"
        self._available_cursors = {}

    @property
    def qApp(self):
        # reference to QApplication instance
        return self._qApp

    @qApp.setter
    def qApp(self, value):
        self._qApp = value

    def InitDriver(self):
        self._display = OCCViewer.Viewer3d(window_handle=self.GetHandle(), parent=self)
        self._display.Create()
        # background gradient
        self._display.SetModeShaded()
        self._inited = True
        # dict mapping keys to functions
        self._key_map = {ord('W'): self._display.SetModeWireFrame,
                         ord('S'): self._display.SetModeShaded,
                         ord('A'): self._display.EnableAntiAliasing,
                         ord('B'): self._display.DisableAntiAliasing,
                         ord('H'): self._display.SetModeHLR,
                         ord('F'): self._display.FitAll,
                         ord('G'): self._display.SetSelectionMode}
        self.createCursors()

    def createCursors(self):
        module_pth = os.path.abspath(os.path.dirname(__file__))
        icon_pth = os.path.join(module_pth, "icons")

        _CURSOR_PIX_ROT = QtGui.QPixmap(os.path.join(icon_pth, "cursor-rotate.png"))
        _CURSOR_PIX_PAN = QtGui.QPixmap(os.path.join(icon_pth, "cursor-pan.png"))
        _CURSOR_PIX_ZOOM = QtGui.QPixmap(os.path.join(icon_pth, "cursor-magnify.png"))
        _CURSOR_PIX_ZOOM_AREA = QtGui.QPixmap(os.path.join(icon_pth, "cursor-magnify-area.png"))

        self._available_cursors = {
            "arrow": QtGui.QCursor(QtCore.Qt.ArrowCursor),  # default
            "pan": QtGui.QCursor(_CURSOR_PIX_PAN),
            "rotate": QtGui.QCursor(_CURSOR_PIX_ROT),
            "zoom": QtGui.QCursor(_CURSOR_PIX_ZOOM),
            "zoom-area": QtGui.QCursor(_CURSOR_PIX_ZOOM_AREA),
        }

        self._current_cursor = "arrow"

    def keyPressEvent(self, event):
        code = event.key()
        if code in self._key_map:
            self._key_map[code]()
        elif code in range(256):
            log.info('key: "%s"(code %i) not mapped to any function' % (chr(code), code))
        else:
            log.info('key: code %i not mapped to any function' % code)

    def focusInEvent(self, event):
        if self._inited:
            self._display.Repaint()

    def focusOutEvent(self, event):
        if self._inited:
            self._display.Repaint()

    def paintEvent(self, event):
        if self._drawbox:
            self._display.Repaint()
            self._display.Repaint()
            painter = QtGui.QPainter(self)
            painter.setPen(QtGui.QPen(QtGui.QColor(0, 0, 0), 2))
            rect = QtCore.QRect(*self._drawbox)
            painter.drawRect(rect)

    def wheelEvent(self, event):
        try:  # PyQt4/PySide
            delta = event.delta()
        except:  # PyQt5
            delta = event.angleDelta().y()
        if delta > 0:
            zoom_factor = 2.
        else:
            zoom_factor = 0.5
        self._display.ZoomFactor(zoom_factor)

    @property
    def cursor(self):
        return self._current_cursor

    @cursor.setter
    def cursor(self, value):
        if not self._current_cursor == value:

            self._current_cursor = value
            cursor = self._available_cursors.get(value)

            if cursor:
                self.qApp.setOverrideCursor(cursor)
            else:
                self.qApp.restoreOverrideCursor()

    def mousePressEvent(self, event):
        self.setFocus()
        ev = event.pos()
        self.dragStartPosX = ev.x()
        self.dragStartPosY = ev.y()
        self._display.StartRotation(self.dragStartPosX, self.dragStartPosY)

    def mouseReleaseEvent(self, event):
        pt = event.pos()
        modifiers = event.modifiers()

        if event.button() == QtCore.Qt.LeftButton:
            if self._select_area:
                [Xmin, Ymin, dx, dy] = self._drawbox
                self._display.SelectArea(Xmin, Ymin, Xmin + dx, Ymin + dy)
                self._select_area = False
            else:
                # multiple select if shift is pressed
                if modifiers == QtCore.Qt.ShiftModifier:
                    self._display.ShiftSelect(pt.x(), pt.y())
                else:
                    # single select otherwise
                    self._display.Select(pt.x(), pt.y())

                    if (self._display.selected_shapes is not None) and HAVE_PYQT_SIGNAL:
                        self.sig_topods_selected.emit(self._display.selected_shapes)


        elif event.button() == QtCore.Qt.RightButton:
            if self._zoom_area:
                [Xmin, Ymin, dx, dy] = self._drawbox
                self._display.ZoomArea(Xmin, Ymin, Xmin + dx, Ymin + dy)
                self._zoom_area = False

        self.cursor = "arrow"

    def DrawBox(self, event):
        tolerance = 2
        pt = event.pos()
        dx = pt.x() - self.dragStartPosX
        dy = pt.y() - self.dragStartPosY
        if abs(dx) <= tolerance and abs(dy) <= tolerance:
            return
        self._drawbox = [self.dragStartPosX, self.dragStartPosY, dx, dy]


    def mouseMoveEvent(self, evt):
        pt = evt.pos()
        buttons = int(evt.buttons())
        modifiers = evt.modifiers()
        # ROTATE
        if (buttons == QtCore.Qt.LeftButton and
                not modifiers == QtCore.Qt.ShiftModifier):
            self.cursor = "rotate"
            self._display.Rotation(pt.x(), pt.y())
            self._drawbox = False
        # DYNAMIC ZOOM
        elif (buttons == QtCore.Qt.RightButton and
              not modifiers == QtCore.Qt.ShiftModifier):
            self.cursor = "zoom"
            self._display.Repaint()
            self._display.DynamicZoom(abs(self.dragStartPosX),
                                      abs(self.dragStartPosY), abs(pt.x()),
                                      abs(pt.y()))
            self.dragStartPosX = pt.x()
            self.dragStartPosY = pt.y()
            self._drawbox = False
        # PAN
        elif buttons == QtCore.Qt.MidButton:
            dx = pt.x() - self.dragStartPosX
            dy = pt.y() - self.dragStartPosY
            self.dragStartPosX = pt.x()
            self.dragStartPosY = pt.y()
            self.cursor = "pan"
            self._display.Pan(dx, -dy)
            self._drawbox = False
        # DRAW BOX
        # ZOOM WINDOW
        elif (buttons == QtCore.Qt.RightButton and
              modifiers == QtCore.Qt.ShiftModifier):
            self._zoom_area = True
            self.cursor = "zoom-area"
            self.DrawBox(evt)
            self.update()
        # SELECT AREA
        elif (buttons == QtCore.Qt.LeftButton and
              modifiers == QtCore.Qt.ShiftModifier):
            self._select_area = True
            self.DrawBox(evt)
            self.update()
        else:
            self._drawbox = False
            self._display.MoveTo(pt.x(), pt.y())
            self.cursor = "arrow"





class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args):
        QtWidgets.QMainWindow.__init__(self, *args)
        self.canva = qtViewer3d(self)
        self.setWindowTitle("666666")
        self.setCentralWidget(self.canva)
        if sys.platform != 'darwin':
            self.menu_bar = self.menuBar()
        else:
            # create a parentless menubar
            # see: http://stackoverflow.com/questions/11375176/qmenubar-and-qmenu-doesnt-show-in-mac-os-x?lq=1
            # noticeable is that the menu ( alas ) is created in the
            # topleft of the screen, just
            # next to the apple icon
            # still does ugly things like showing the "Python" menu in
            # bold
            self.menu_bar = QtWidgets.QMenuBar()
        self._menus = {}
        self._menu_methods = {}
        # place the window in the center of the screen, at half the
        # screen size
        self.centerOnScreen()

    def centerOnScreen(self):
        '''Centers the window on the screen.'''
        resolution = QtWidgets.QApplication.desktop().screenGeometry()
        x = (resolution.width() - self.frameSize().width()) / 2
        y = (resolution.height() - self.frameSize().height()) / 2
        self.move(x, y)

    def add_menu(self, menu_name):
        _menu = self.menu_bar.addMenu("&" + menu_name)
        self._menus[menu_name] = _menu

    def add_function_to_menu(self, menu_name, _callable):
        check_callable(_callable)
        try:
            _action = QtWidgets.QAction(_callable.__name__.replace('_', ' ').lower(), self)
            # if not, the "exit" action is now shown...
            _action.setMenuRole(QtWidgets.QAction.NoRole)
            _action.triggered.connect(_callable)

            self._menus[menu_name].addAction(_action)
        except KeyError:
            raise ValueError('the menu item %s does not exist' % menu_name)


# following couple of lines is a tweak to enable ipython --gui='qt'

if __name__=="__main__":
		backend_str=None,
		size=(1024, 768),
		display_triedron=True,
		background_gradient_color1=[206, 215, 222]
		background_gradient_color2=[128, 128, 128]
		app = QtWidgets.QApplication.instance()  # checks if QApplication already exists
		if not app:  # create QApplication if it doesnt exist
			app = QtWidgets.QApplication(sys.argv)
		win = MainWindow()
		win.resize(size[0] -1, size[1] -1)
		win.show()
		win.centerOnScreen()
		win.canva.InitDriver()
		win.resize(size[0], size[1])
		win.canva.qApp = app
		display = win.canva._display
