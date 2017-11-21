﻿import os
main_dir=os.path.dirname(os.path.abspath(__file__))+os.path.sep
import OpenGL.GL as gl
from PyQt4 import QtGui
from PyQt4 import QtCore
import PyQt4.QtOpenGL as qgl
from MainUI import Ui_MainUI
from suc_class import AreaCollector as area
import OpenGL.GLU as glu

class WfWidget(qgl.QGLWidget):
    def __init__(self, parent = None):
        super(WfWidget, self).__init__(parent)
        # self.pointsText = "(0, 0), (10, 0), (10, 7),(0,7)"
        # self.PointsList = area.getlist(self.pointsText)
        # self.PointCenter = area.getCenter(self.PointsList)
        # self.Area = area.getArea(self.PointsList)

        self.pointsText = ""
        self.PointsList = []
        self.PointCenter = ()
        self.Area = 0
        self.left=-100
        self.right=100
        self.bottom=-100
        self.top=100
        self.zNear=-1000
        self.zFar=1000
        self.lw=100
        self.lh=100
        self.setUpdatesEnabled(True)
        class llp(object):
            x=0
            y=0
        self.lastPos=0
        self.dx=0
        self.dy=0

        self.addx=0
        self.addy=0
        self.addz=0

        self.fpoints=[]

        self._gl_zoom=3

    def paintGL(self):
        self.myloppMain()

    def MyResier(self,w,h):
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        # gl.glOrtho(self.left, self.right, self.bottom, self.top, self.zNear, self.zFar)
        glu.gluPerspective(45.0, self.lw / self.lh, -100.0, 800)
        gl.glViewport(0, 0, w, h)
    def isPositive(self,val):
        pass
    def reinit(self):
        # gl.glViewport(0, 0, self.lw, self.lh)
        # gl.glMatrixMode(gl.GL_PROJECTION)
        # gl.glLoadIdentity()
        # glu.gluLookAt(0, 0, self._gl_zoom, 0, 0, 0, 0, 1, 0)
        gl.glClearColor(0.05, 0.05, 0.05, 1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glLoadIdentity()

        # if self.left >= 0 or self.right <= 0 or self.top <= 0 or self.bottom >= 0:
        #     glu.gluPerspective(45.0,self.lw/self.lh,1.0,800)
        #     # gl.glOrtho(-1, 1, -1, 1, self.zNear, self.zFar)
        # else:
        #     glu.gluPerspective(45.0,float(self.lw/self.lh),1.0,800.0)
        # glu.gluLookAt(0, 0, 6, 0, 0, 0, 0, 1, 0)
        # gl.glMatrixMode(gl.GL_MODELVIEW)

        # gl.glOrtho(self.left, self.right, self.bottom, self.right, self.zNear, self.zFar)
        # gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    def myloppMain(self):
        self.reinit()
        gl.glColor3f(0.60, 0.90, 0.12)
        # gl.glBegin(gl.GL_POLYGON)
        gl.glBegin(gl.GL_LINE_LOOP)
        # gl.glVertex3f(5,5,0.0)
        # gl.glVertex3f(2,7,0.0)
        # gl.glVertex3f(3,9,0.0)
        for a in self.PointsList:
            try:
                 # gl.glVertex3f(a[0]+self.addx,a[1]+self.addy,a[2]+self.addz)
                 gl.glVertex3f(a[0],a[1],a[2])
            except:
                pass
        gl.glEnd()
        #
        # glu.gluPerspective(45.0, self.lw / self.lh, 1.0, 800)
        # # glu.gluLookAt(0, 0, 10, 0, 0, 0, 0, 1, 0)
        # gl.glMatrixMode(gl.GL_MODELVIEW)
        # gl.glScalef(0.1, 0.1, 0.1)
        # glu.gluLookAt(10, 0, self._gl_zoom, 0, 0, 0, 0, 1, 0)

        self.update()
    def paintPoints(self,pointss=()):
        if len(pointss)==0:
            points=self.fpoints
        else:
            points=pointss
        gl.glColor3f(1.0, 1.0, 0.0)
        gl.glBegin(gl.GL_POINTS)
        for point in points:
            gl.glVertex3f(point[0],point[1],point[2])
        gl.glEnd()
        self.update()

    def resizeGL(self, w, h):
        self.lw=w
        self.lh=h
        self.MyResier(w,h)
    def initializeGL(self):
        gl.glViewport(0, 0, self.lw, self.lh)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        glu.gluPerspective(45.0, self.lw / self.lh, 1.0, 800)
        # glu.gluLookAt(0, 0, 10, 0, 0, 0, 0, 1, 0)
        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glScalef(0.1, 0.1, 0.1)
        glu.gluLookAt(0, 0, self._gl_zoom, 0, 0, 0, 0, 1, 0)
        # gl.glClearColor(0.05, 0.05, 0.05, 1.0)
        # gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        # gl.glLoadIdentity()
        # gl.glLineWidth(3.0)
    def mousePressEvent(self, event):
        self.lastPos = event.pos()
        # print("pressed")
    def wheelEvent(self,cv):
        val=cv.delta()
        inc=5
        if val<0:
            self._gl_zoom+=1
            self.top+=inc
            self.bottom-=inc
            self.right+=inc
            self.left-=inc
        else:
            self._gl_zoom-=1
            self.top-=inc
            self.bottom+=inc
            self.right-=inc
            self.left+=inc
        # self.initializeGL()
        self.myloppMain()
        # print(kwargs)
    def mouseMoveEvent(self, event):
        self.dx = event.x() - self.lastPos.x()
        self.dy = event.y() - self.lastPos.y()
        """

        """
        if event.buttons() & QtCore.Qt.LeftButton:
            # print(event.Wheel)
            if self.dx>0:
                self.addx+=self.dx/5.0
                self.addy -= self.dy / 5.0
                print("Up")
                # self.left+=self.dx
                # self.right-=self.dx
            else:
                self.addx+=self.dx/5.0
                print("Down")
                self.addy -= self.dy / 5.0
                # self.left+=-self.dx
                # self.right-=+self.dx

        self.lastPos = event.pos()
        # print("moving")
        # myloppMain
class mwindows(QtGui.QWidget,Ui_MainUI):
    def __init__(self):

        QtGui.QWidget.__init__(self)
        stl=open(main_dir+"darkorang_style.css",'r')
        self.setStyleSheet(stl.read())
        self.box=QtGui.QVBoxLayout(self)
        self.info=QtGui.QPushButton()
        self.info.setText("About")

        self.ggl = WfWidget(self)
        self.box.addWidget(self.ggl)

        self.bbp=QtGui.QPushButton()
        self.bbp.setText("Calculate")
        self.box.addWidget(self.bbp)
        self.textbox=QtGui.QLineEdit(self)
        self.box.addWidget(self.textbox)
        self.result=QtGui.QLineEdit(self)
        self.result.setText("Result")
        self.result.setDisabled(True)
        self.box.addWidget(self.result)
        # self.bbp.clicked.connect(self.close())
        self.setLayout(self.box)
        self.bbp.clicked.connect(self.vv)
        self.textbox.textChanged.connect(self.vv)
        self.textbox.setStyleSheet("""
        font-size:17pt;
        """)
        self.result.setStyleSheet("""
        font-size:17pt;
        """)
        self.bbp.setVisible(False)

        self.ShZNear=QtGui.QSlider()
        self.box.addWidget(self.ShZNear)
        self.ShZNear.setOrientation(QtCore.Qt.Horizontal)
        self.ShZNear.valueChanged.connect(self.changer)
        self.ShZNear.setRange(30,300)
        self.ShZNear.setValue(100)

        self.box.addWidget(self.info)
        self.info.clicked.connect(self.information)
    def information(self):
        v=QtGui.QMessageBox(self)
        v.setText('<p style="font-size:16px;">© 2016 Al-Banna-Techno ALL COPY RIGHT RESERVED</p>'
                  '<p style="font-size:16px;">email : Al_Banna_Techno@yahoo.com</p>'
                  '<p style="font-size:16px;">mobile number : +2 01098470235</p>'
                  )
        v.setWindowTitle("Info")
        v.exec_()
    def changer(self,val):
        self.ggl.top=val
        self.ggl.bottom=-val
        self.ggl.right=val
        self.ggl.left=-val
        try:
            pass
            self.ggl.paintGL()
          #  self.ggl.resize(self.size())
          #   self.ggl.update()
          #   self.repaint()
          #   self.ggl.updateGeometry()
        except:
            pass
    def vv(self):
        ok=True
        paintz=False
        gcounter=()
        self.ggl.pointsText = ""
        self.ggl.PointsList = []
        self.ggl.PointCenter = ()
        self.ggl.Area = 0
        try:
            fulltext=self.textbox.text().replace(" ","")
            gcounter = area.getlist(fulltext)
            print(gcounter)
            ln=len(gcounter[0])
            if not (ln==2 or ln ==3):
                self.result.setText("Invalid Inputs")
                return
            else:
                """
                This Program Will Only work with 2d and 3d points
                any points above this number will escaped
                and we append zero for every point so
                if we have 2d point
                it will be 3d point with z=0 : = 3d point
                    and if we have 3d point
                    we will add zero to it
                    but the program will escape the 4th value
                    when it's painting

                """
                for a in gcounter:
                    a = list(a)
                    a.append(0)
                    self.ggl.PointsList.append(a)

            # if ln==2:
            #     for a in gcounter:
            #         a=list(a)
            #         a.append(0)
            #         self.ggl.PointsList.append(a)
            # else:
            #     self.ggl.PointsList=gcounter
        except:
            ok=False
            # self.result.setText("Not Valid Input")
        if ok:
            if not len(self.ggl.PointsList)<3:
                try:
                    self.ggl.PointCenter = area.getCenter(self.ggl.PointsList,True)
                    self.ggl.Area = area.getArea(self.ggl.PointsList)
                    # self.ggl.fpoints=(self.ggl.PointCenter)
                except:
                    pass
                # self.setEnabled(True)
                self.result.setEnabled(True)
                self.result.enabledChange(False)
                self.result.setText("Area : %s , Center : %s" % (
                    self.ggl.Area,
                    self.ggl.PointCenter
                ))
            # if paintz:
            #     self.result.setText("You Can't calculate Area With 3D Mode")

            # self.ggl.update()
            # self.ggl.updateGeometry()
            # self.ggl.paintGL()
            # self.ggl.resize(self.size())


if __name__ == '__main__':
    app = QtGui.QApplication(["Winfred's PyQt OpenGL"])
    mainwindow=mwindows()
    mainwindow.setWindowTitle("Abt::PointsDraw")
    mainwindow.resize(500,400)
    mainwindow.show()
    app.exec_()
"""
(0,0),(5,6),(12,3),(16,-3),(11,-8)
"""

