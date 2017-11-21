import re
def get_num_of(cont,el):
    n=0
    for a in cont:
        if a==el:
            n+=1
    return n
def List_parser(context):
    cure_num_1=get_num_of(context,"(")
    cure_num_2=get_num_of(context,")")
    if cure_num_1!=cure_num_2:
        raise Exception("Error")
    pass
def lp(context):
    fcont=context[1:len(context)-1]
    fcont_gs=fcont.split("),")
    print(fcont_gs)
   # print(fcont)
    r=re.compile("(\(\S+\))")
    c=r.findall(context.replace(" ","").replace("\n","").replace("\t",""))
    return c


def flp(context):
    fcont=context[1:len(context)-1]
    r=re.compile("(\(\S+\)+)")
    c=r.findall(fcont.replace(" ","").replace("\n","").replace("\t",""))
    return c

# vl=List_parser("(40,50)")
vl=flp("((40,50,40),(80,70,(90,20)),(80,90))")
print(vl)
print(len(vl))
import plistlib
plistlib.load()