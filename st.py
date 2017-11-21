def getlist(cont):
    loc={}
    glob={}
    c="FFFF_0xxFF=%s\n"%cont
    exec(c,glob,loc)
    return list(loc["FFFF_0xxFF"])
# l=getlist("(60,80),(40)")
# print(l)
# print(len(l))
def getlenght(points):
    ln=0
    if len(points)==2:
        a=points[0]
        b=points[1]
        xa=a[0]
        ya=a[1]
        xb=b[0]
        yb=b[1]
        ln=(((xa-xb)**2)+((ya-yb)**2))**0.5
        return ln
def getTriArea(rectps):
    p1=rectps[0]
    p2=rectps[1]
    p3=rectps[2]
    r1=getlenght((p1,p2))
    r2=getlenght((p2,p3))
    r3=getlenght((p1,p3))
    s=(r1+r2+r3)/2.0
    A=(s*(s-r1)*(s-r2)*(s-r3))**0.5
    return A
def getArea(point_s):
    # points=getlist(point_s)
    points=point_s
    RectN=len(points)-2
    if len(points)<3:
        raise Exception("ERROR::POINT::NUMBER")
    print(RectN)
    p1 = points[0]
    Farea = 0
    for a in range(0,RectN):
        pps=[p1]
        pps.append(points[a+1])
        pps.append(points[a+2])
        tArea=getTriArea(pps)
        Farea+=tArea
    return Farea

#ar=getArea("(5,5),(5,5),(0,0)")

# pp=((5,0),(5,5),(0,0))
# ar=getArea(pp)
# print(ar)


# ps=((0,0),(5,5))
# print(getlenght(ps))

# pp=((5,0),(5,5),(0,0))
# ar=getTriArea(pp)
# print(ar)



pp=((5,0),(5,5),(0,0))
ar=getArea(pp)
print(ar)

