class AreaCollector():
    def __init__(self):
        pass
    @staticmethod
    def getlist(cont):
        loc = {}
        glob = {}
        c = "FFFF_0xxFF=%s\n" % cont
        exec(c, glob, loc)
        return list(loc["FFFF_0xxFF"])
    @staticmethod
    def getlenght(points):
        ln = 0
        if len(points) == 2:
            a = points[0]
            b = points[1]
            xa = a[0]
            ya = a[1]
            xb = b[0]
            yb = b[1]
            ln = (((xa - xb) ** 2) + ((ya - yb) ** 2)) ** 0.5
            return ln
    @staticmethod
    def getTriArea(rectps):
        p1 = rectps[0]
        p2 = rectps[1]
        p3 = rectps[2]
        r1 = AreaCollectore.getlenght((p1, p2))
        r2 = AreaCollectore.getlenght((p2, p3))
        r3 = AreaCollectore.getlenght((p1, p3))
        s = (r1 + r2 + r3) / 2.0
        A = (s * (s - r1) * (s - r2) * (s - r3)) ** 0.5
        return A
    @staticmethod
    def getArea(point_s):
        # points=getlist(point_s)
        points = point_s
        RectN = len(points) - 2
        if len(points) < 3:
            raise Exception("ERROR::POINT::NUMBER")
        print(RectN)
        p1 = points[0]
        Farea = 0
        for a in range(0, RectN):
            pps = [p1]
            pps.append(points[a + 1])
            pps.append(points[a + 2])
            tArea = AreaCollectore.getTriArea(pps)
            Farea += tArea
        return Farea
    @staticmethod
    def getCenter(points,z=False):
        Xs=[]
        Ys=[]
        if z:
            # this step reduce memory but increase data size
            Zs=[]
            for a in points:
                try:
                    Xs.append(a[0])
                    Ys.append(a[1])
                    Zs.append(a[2])
                except:
                    return
        for a in points:
            try:
                Xs.append(a[0])
                Ys.append(a[1])
            except:
                return
        if z:
            Centroid=[(sum(Xs)/len(Xs)),(sum(Ys)/len(Ys)),(sum(Zs)/len(Zs))]

        else:
            Centroid=[(sum(Xs)/len(Xs)),(sum(Ys)/len(Ys))]
        return Centroid

def main():
    #pp = ((5, 0), (5, 5), (0, 0))
    #pp = "(5, 0), (5, 5), (0, 0)"
    pp = "(0, 0), (10, 0), (10, 7),(0,7)"
    pp=AreaCollectore.getlist(pp)
    Center=AreaCollectore.getCenter(pp)
    pp=AreaCollectore.getArea(pp)
    print(pp)
    print(Center)

if __name__=="__main__":
    main()
