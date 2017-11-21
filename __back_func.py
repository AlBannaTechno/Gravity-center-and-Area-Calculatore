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
        # self.result.setText("Not Valid Input")
    if ok:
        if not len(self.ggl.PointsList) < 3:
            try:
                self.ggl.PointCenter = area.getCenter(self.ggl.PointsList, True)
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
            # if paintz:
            #     self.result.setText("You Can't calculate Area With 3D Mode")

            # self.ggl.update()
            # self.ggl.updateGeometry()
            # self.ggl.paintGL()
            # self.ggl.resize(self.size())
