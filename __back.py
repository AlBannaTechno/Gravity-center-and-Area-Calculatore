import OpenGL.GL as gl
from PyQt4 import QtGui
from PyQt4 import QtCore
import PyQt4.QtOpenGL as qgl
from MainUI import Ui_MainUI
from suc_class import AreaCollectore as area


class WfWidget(qgl.QGLWidget):
    def __init__(self, parent=None):
        super(WfWidget, self).__init__(parent)
        # self.pointsText = "(0, 0), (10, 0), (10, 7),(0,7)"
        # self.PointsList = area.getlist(self.pointsText)
        # self.PointCenter = area.getCenter(self.PointsList)
        # self.Area = area.getArea(self.PointsList)

        self.pointsText = ""
        self.PointsList = []
        self.PointCenter = ()
        self.Area = 0
        self.left = -100
        self.right = 100
        self.bottom = -100
        self.top = 100
        self.zNear = -1000
        self.zFar = 1000
        self.lw = 100
        self.lh = 100
        self.setUpdatesEnabled(True)

        class llp(object):
            x = 0
            y = 0

        self.lastPos = 0
        self.dx = 0
        self.dy = 0

        self.addx = 0
        self.addy = 0
        self.addz = 0

    def paintGL(self):
        self.myloppMain()

    def MyResier(self, w, h):
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glOrtho(self.left, self.right, self.bottom, self.top, self.zNear, self.zFar)
        gl.glViewport(0, 0, w, h)

    def isPositive(self, val):
        pass

    def myloppMain(self):
        # glColor3f(0.0, 0.0, 1.0)
        # glRectf(-5, -5, 5, 5)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        # print(self.left+10,end=" , ")
        # print(self.right+10,end=" , ")
        # print(self.bottom+10,end=" , ")
        # print( self.top+10,end=" , ")
        # print(self.zNear+10,end=" , ")
        # print(self.zFar+10,end=" , ")
        # print("\n")
        if self.left >= 0 or self.right <= 0 or self.top <= 0 or self.bottom >= 0:
            gl.glOrtho(-1, 1, -1, 1, self.zNear, self.zFar)
        else:
            gl.glOrtho(self.left, self.right, self.bottom, self.right, self.zNear, self.zFar)

        # try:
        #     if self.left>=0 or self.right<=0 or self.top<=0 or self.bottom>=0:
        #         gl.glOrtho(self.left, self.right, self.bottom, self.top, self.zNear, self.zFar)
        #
        #     gl.glOrtho(self.left, self.right, self.bottom, self.top, self.zNear, self.zFar)
        # except:
        #     gl.glOrtho(self.left+10, self.right+10, self.bottom+10, self.top+10, self.zNear+10, self.zFar+10)


        gl.glViewport(0, 0, self.lw, self.lh)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        # self.update()
        gl.glColor3f(1.0, 0.0, 0.0)
        gl.glBegin(gl.GL_LINE_LOOP)
        for a in self.PointsList:
            try:
                gl.glVertex3f(a[0] + self.addx, a[1] + self.addy, a[2] + self.addz)
                # gl.glVertex3f(a[0],a[1].addy,a[2])
                # gl.glTranslatef(self.addx,self.addy,self.addz)
            except:
                pass
        gl.glEnd()
        # self.qglClearColor()

        self.update()

    def resizeGL(self, w, h):
        self.lw = w
        self.lh = h
        self.MyResier(w, h)

    def initializeGL(self):
        gl.glClearColor(0.05, 0.05, 0.05, 1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    def mousePressEvent(self, event):
        self.lastPos = event.pos()
        # print("pressed")

    def wheelEvent(self, cv):
        val = cv.delta()
        inc = 5
        if val < 0:
            self.top += inc
            self.bottom -= inc
            self.right += inc
            self.left -= inc
        else:
            self.top -= inc
            self.bottom += inc
            self.right -= inc
            self.left += inc
            # print(kwargs)

    def mouseMoveEvent(self, event):
        self.dx = event.x() - self.lastPos.x()
        self.dy = event.y() - self.lastPos.y()
        """

        """
        if event.buttons() & QtCore.Qt.LeftButton:
            # print(event.Wheel)
            if self.dx > 0:
                self.addx += self.dx / 5.0
                self.addy -= self.dy / 5.0
                print("Up")
                # self.left+=self.dx
                # self.right-=self.dx
            else:
                self.addx += self.dx / 5.0
                print("Down")
                self.addy -= self.dy / 5.0
                # self.left+=-self.dx
                # self.right-=+self.dx

        self.lastPos = event.pos()
        # print("moving")


class mwindows(QtGui.QWidget, Ui_MainUI):
    def __init__(self):

        QtGui.QWidget.__init__(self)
        stl = open("darkorang_style.css", 'r')
        self.setStyleSheet(stl.read())
        self.box = QtGui.QVBoxLayout(self)
        self.info = QtGui.QPushButton()
        self.info.setText("About")

        self.ggl = WfWidget(self)
        self.box.addWidget(self.ggl)

        self.bbp = QtGui.QPushButton()
        self.bbp.setText("Calculate")
        self.box.addWidget(self.bbp)
        self.textbox = QtGui.QLineEdit(self)
        self.box.addWidget(self.textbox)
        self.result = QtGui.QLineEdit(self)
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

        self.ShZNear = QtGui.QSlider()
        self.box.addWidget(self.ShZNear)
        self.ShZNear.setOrientation(QtCore.Qt.Horizontal)
        self.ShZNear.valueChanged.connect(self.changer)
        self.ShZNear.setRange(30, 300)
        self.ShZNear.setValue(100)

        self.box.addWidget(self.info)
        self.info.clicked.connect(self.information)

    def information(self):
        v = QtGui.QMessageBox(self)
        v.setText('<p style="font-size:16px;">© 2016 Al-Banna-Techno ALL COPY RIGHT RESERVED</p>'
                  '<p style="font-size:16px;">email : Al_Banna_Techno@yahoo.com</p>'
                  '<p style="font-size:16px;">mobile number : +2 01098470235</p>'
                  )
        v.exec_()

    def changer(self, val):
        self.ggl.top = val
        self.ggl.bottom = -val
        self.ggl.right = val
        self.ggl.left = -val
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
        ok = True
        paintz = False
        gcounter = ()
        self.ggl.pointsText = ""
        self.ggl.PointsList = []
        self.ggl.PointCenter = ()
        self.ggl.Area = 0
        try:
            fulltext = self.textbox.text().replace(" ", "")
            if fulltext[0] == "$":
                paintz = True
                gcounter = area.getlist(fulltext[1:])
            else:
                gcounter = area.getlist(fulltext)
            print(gcounter)
            # self.ggl.PointsList=gcounter
            # print(gcounter)
            if not paintz:
                for a in gcounter:
                    a = list(a)
                    a.append(0)
                    self.ggl.PointsList.append(a)
            else:
                self.ggl.PointsList = gcounter

        except:
            ok = False
            print("false")
            # self.result.setText("Not Valid Input")
        if ok:
            if not len(self.ggl.PointsList) < 3 and not paintz:
                try:
                    self.ggl.PointCenter = area.getCenter(self.ggl.PointsList)
                    self.ggl.Area = area.getArea(self.ggl.PointsList)
                except:
                    pass
                # self.setEnabled(True)
                self.result.setEnabled(True)
                self.result.enabledChange(False)
                self.result.setText("Area : %s , Center : %s" % (
                    self.ggl.Area,
                    self.ggl.PointCenter
                ))
            if paintz:
                self.result.setText("You Can't calculate Area With 3D Mode")

                # self.ggl.update()
                # self.ggl.updateGeometry()
                # self.ggl.paintGL()
                # self.ggl.resize(self.size())


if __name__ == '__main__':
    app = QtGui.QApplication(["Winfred's PyQt OpenGL"])
    mainwindow = mwindows()
    mainwindow.resize(500, 400)
    mainwindow.show()
    app.exec_()
"""
(0,0),(5,6),(12,3),(16,-3),(11,-8)
"""

