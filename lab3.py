import pandas as pd
import py5


#Load Data#
df = pd.read_csv("week3/HabHYG15ly.csv", encoding ="latin-1")     #df = data frame to load data
print (f"Loaded {len(df)} stars")

#access columns
distance = df['Distance']
x_coords = df['Xg']
y_coords = df['Yg']
z_coords = df['Zg']
for index, row in df.iterrows():
    x = row['Xg']
    y = row['Yg']
    z = row['Zg']
    name = row['Display Name']
    distance = row['Distance']
    

def setup():
    py5.size(500,500)
    py5.no_fill()

def draw():
    py5.background(0)
    w = py5.width
    h = py5.height
    cell_size = 50
    py5.stroke(255,0,255)

    for x in range(0,w,cell_size):
        py5.line(x,0,x,h)

    for y in range(0,h,cell_size):
        py5.line(0, y, w, y)

    for i, row in df.iterrows():
        xg= row['Xg']
        yg = row['Yg']
        zg = row['Zg']
        name = row['Display Name']
        distance = row['Distance']
        
        
        x = py5.remap(xg, -5,5,0,py5.width)
        y = py5.remap(yg, -5, 5, 0, py5.width)
        
        
       
        py5.fill(0)
        py5.stroke(225,0,0)
        py5.circle(x,y, 10)
        
        py5.fill(225,225,225)
        py5.text_size(10)
        py5.text(name, x,y)


        
        py5.stroke(225,225,0)
        py5.line(x,y+5,x,y-5)
        py5.line(x+5,y,x-5,y)
       
        
        
py5.run_sketch()