import py5

mode = 0    # global variables (values you can use anywhere in your program)
face_x = 0  # the postion of mouse x-cornidate
face_y = 0  # the postion of mouse y-cornidate
size_rect = 100
growing_circle = True   # tell us if circle is getting bigger or shrinking
growing_rect = True # tell us if rectangle is getteing bigger or shrinking
radius = 50   

def key_pressed():
    global mode # allows us to change global mode variable
    if py5.key >= '0' and py5.key <= '9': # only works if the key is a number (0-9)
        mode = int(py5.key) - int('0')  # converts key to a number
        print(mode) #shows the chosen mode in the console

def setup():
    py5.size(500,500) #set picture to 500 by 500 pixels

def draw():
    global mode
    if mode == 0:
        global radius, growing_circle
    
        py5.background(255,255,255)   
        
        py5.fill(255, 0, 0) # red circle
        py5.circle(py5.width/2, py5.height/2, radius * 2) # draw a circle in the middle of the picture.controlled by radius
        
        
        if growing_circle: #if true it gets bigger
            radius += 2
            if radius > 150:   # once reach 150 change it to false and start shrinking
                growing_circle = False
        else:
            radius -= 2
            if radius < 50:    # once reach 50 change to true and starts growing
                growing_circle = True
        

    elif mode == 1:
        global size_rect, growing_rect
        py5.background(255,255,255)
        py5.rect_mode(py5.CENTER) # draw rectangle from center
        py5.fill(0,0,255) # blue rectangle
        py5.rect(py5.width/2, py5.height/3, size_rect, size_rect) # draw rectangle at the center-top of the picture

        if growing_rect:
            size_rect += 2
            if size_rect > 200:
                growing_rect = False

        else:
            size_rect -= 2
            if size_rect < 50:
                growing_rect = True

        
       
    elif mode == 2:
        global face_x, face_y
        py5.background(255,255,255) 
        py5.fill(0,255,0)
        py5.stroke(0)  # adds a black outline
        py5.stroke_weight(2)

        face_x = py5.mouse_x
        face_y = py5.mouse_y

        face_diameter = 100
        py5.circle(face_x, face_y, face_diameter) # draw the green head with diameter 100

        eye_radius = 10 # radius of eye
        eye_offset_x = 25 # move eye 25 in x direction from center
        eye_offset_y = -20 # move eye -20 in y direction from center

        py5.fill(0) 
        py5.circle(face_x - eye_offset_x, face_y + eye_offset_y, eye_radius) # left eye
        py5.circle(face_x + eye_offset_x, face_y + eye_offset_y, eye_radius) # right eye

    
        mouth_width = 50
        mouth_height = 20
        mouth_offset_y = 30

        py5.no_fill() 
        py5.arc(face_x, face_y + mouth_offset_y, mouth_width, mouth_height, 0, py5.PI) # face_x (arc center), face_y+mouth_offset_y(y-coordinate add offset to move below eye),0(starting angle start rhs pointing east),py5.PI(means 180 a half-turn so arc go right-left, combine with 0 create half of ellipse)

    elif mode == 3:
        py5.background(255,255,255)  
    
        x = py5.mouse_x # set mushroom postion to mouse postion
        y = py5.mouse_y
        
        
        py5.fill(255)
        py5.rect_mode(py5.CENTER)
        py5.rect(x, y + 40, 30,40,30)  # round rectangle stem
        
        
        py5.fill(255, 0, 0)
        py5.ellipse(x, y, 100, 60)
        
        # draw white spots on the cap
        py5.fill(255)
        py5.circle(x - 20, y - 10, 15)
        py5.circle(x + 15, y - 5, 10)
        py5.circle(x, y + 5, 8)

        
        



py5.run_sketch()
        


