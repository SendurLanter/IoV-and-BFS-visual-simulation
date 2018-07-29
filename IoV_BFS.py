from tkinter import *
from time import sleep
from threading import Thread
from random import randint

graph = { '1':['2','5'] , '2':['1','3','6','15'] , '3':['2','4','7','15'] , '4':['3','8','25','26'] , '5':['1','6','9','22'],
          '6':['2','5','7','10'] , '7':['3','6','8','11'] , '8':['4','7','12','16'] , '9':['5','10'] , '10':['6','9','11','13'],
          '11':['7','10','12','19'] , '12':['8','11','18','27'] , '13':['10','14','19','28'] , '14':['13','20','21'] , '15':['2','3','23','24'],
          '16':['8','17','32'] , '17':['16','18','32','36'] , '18':['12','17','36'] , '19':['11','13'] , '20':['14','33'],
          '21':['14','29'] , '22':['5','30'] , '23':['15','34'] , '24':['15','35'] , '25':['4','31'] , '26':['4'] , '27':['12'] , '28':['13'],
          '29':['21'] , '30':['22'] , '31':['25'] , '32':['17','16'] ,'33':['20'] , '34':['23'] , '35':['24'] ,'36':['17','18'] }

location = {'1':(280,480) , '2':(400,480) , '3':(520,480) , '4':(640,480) , '5':(280,380),
            '6':(400,380) , '7':(520,380) , '8':(640,380) , '9':(280,280) , '10':(400,280),
            '11':(520,280) , '12':(640,280), '13':(400,180) , '14':(280,180) , '15':(460,540),
            '16':(880,380) , '17':(880,90) , '18':(640,90) , '19':(520,180) , '20':(215,115),
            '21':(180,280) , '22':(180,480) , '23':(380,620) , '24':(540,620) , '25':(740,580) , '26':(760,480) , '27':(760,280) , '28':(400,50),
            '29':(80,380) , '30':(80,580) , '31':(840,680) , '32':(880,235) , '33':(150,50) , '34':(320,680) , '35':(600,680) , '36':(760,90)}


def initialize():

    #紅
    route.create_line(400, 50, 400, 480,fill = 'red',width = 3)
    route.create_line(400, 480, 760, 480,fill = 'red',width = 3)

    #綠
    route.create_line(760, 280, 280, 280,fill = 'green',width = 3)
    route.create_line(280, 480, 280, 280,fill = 'green',width = 3)
    route.create_line(280, 480, 400, 480,fill = 'green',width = 3)
    route.create_line(600, 680, 400, 480,fill = 'green',width = 3)

    #藍
    route.create_line(280, 380, 880, 380,fill = 'blue',width = 3)
    route.create_line(280, 380, 80, 580,fill = 'blue',width = 3)

    #黃
    route.create_line(280, 180, 520, 180,fill = 'yellow',width = 3)
    route.create_line(520, 480, 520, 180,fill = 'yellow',width = 3)
    route.create_line(520, 480, 320, 680,fill = 'yellow',width = 3)
    route.create_line(150, 50, 280, 180,fill = 'yellow',width = 3)
    route.create_line(80, 380, 280, 180,fill = 'yellow',width = 3)
    #棕
    route.create_line(640, 480, 640, 90,fill = 'brown',width = 3)
    route.create_line(640, 480, 840, 680,fill = 'brown',width = 3)
    route.create_line(640, 90, 880, 90,fill = 'brown',width = 3)
    route.create_line(880, 90, 880, 380,fill = 'brown',width = 3)

    route.create_text( 760,130,text="黑壓壓",font=('Arial', 32))

    for e in location.values():
        route.create_oval( e[0]-6, e[1]-6, e[0]+6, e[1]+6, width = 3 )
        
    for i in range(50):
        Thread(target = instance ).start()
    root.mainloop()


def instance():

    a = str(randint(1,36))
    b = str(randint(1,36))
    obj = route.create_oval( location[a][0]-4, location[a][1]-4, location[a][0]+4, location[a][1]+4, width = 3 )
    
    order = determine(a,b)
    
    for i in range(1,len(order)):
        moving(obj,order[i-1],order[i])
        
    route.delete(obj)
    

def moving(obj,CURRENT,NEXT):

    if ( location[str(NEXT)][0] - location[str(CURRENT)][0] ) >0:
        x=1
    elif ( location[str(NEXT)][0] - location[str(CURRENT)][0] ) <0:
        x=-1
    else:
        x=0
        
    if ( location[str(NEXT)][1] - location[str(CURRENT)][1] ) >0:
        y=1
    elif ( location[str(NEXT)][1] - location[str(CURRENT)][1] ) <0:
        y=-1
    else:
        y=0
        
    while ((route.coords(obj)[0]+route.coords(obj)[2])/2,(route.coords(obj)[1]+route.coords(obj)[3])/2)!=location[str(NEXT)]:
        
        #if len(route.find_enclosed(route.coords(obj)[0]-5, route.coords(obj)[1]-5, route.coords(obj)[2]+5, route.coords(obj)[3]+5)) <=2:
        route.move(obj, x, y)
        sleep(0.01)

            
def add(event):
    Thread(target = instance ).start()
    Thread(target = instance ).start()
    Thread(target = instance ).start()
    

def determine(source , destination):
    
    result = list()

    def BFS(source , destination , path):
    
        if destination in graph[source]:
            path.append(destination)
            result.append(path)
            return 

        else:

            for e in graph[source]:
                if e not in path:
                    BFS(e , destination ,path + [e])
                    
    BFS(source , destination , [source])

    return min(result , key =len)
    
    
if __name__ == '__main__':
    
    root = Tk()
    route = Canvas(root,width=1000, height=720)
    route.pack()
    route.bind( "<Button-1>", add )
    
    initialize()
