# Integrity Pledge: The work I am submitting is my own J.O

#-------------------------
# Name: Joshua Oyelami
# Program: L10Q1JO.py
#-------------------------

from PIL import Image   

# Purpose: repair the frame image through multiple transformations

def repair_frame(frame):
    
    picture = Image.open(frame)
    
    width,height = picture.size
    
    halfwidth = width // 2
    
    halfheight = height // 2
    
    green = (0, 255, 0)
    
    yellow = (255, 255, 0)
    
    blue = (0, 0, 255)
    
    red = (255, 0, 0)
    
    # get the starting places for each colors coordinates
    
    gmin_x = width
    gmax_x = 0
    gmin_y = height
    gmax_y = 0
    
    ymin_x = width
    ymax_x = 0
    ymin_y = height
    ymax_y = 0
    
    bmin_x = width
    bmax_x = 0
    bmin_y = height
    bmax_y = 0
    
    rmin_x = width
    rmax_x = 0
    rmin_y = height
    rmax_y = 0    
    
    # depending on the color update that colors coordinates to find where it is in the image
    
    for x in range(width):
        for y in range(height):
            r, g, b = picture.getpixel((x,y))
            
            if (r, g, b) == green:
                if x < gmin_x:
                    gmin_x = x
                if x > gmax_x:
                    gmax_x = x
                if y < gmin_y:
                    gmin_y = y
                if y > gmax_y:
                    gmax_y = y
                    
            elif (r, g, b) == yellow:                
                if x < ymin_x:
                    ymin_x = x
                if x > ymax_x:
                    ymax_x = x
                if y < ymin_y:
                    ymin_y = y
                if y > ymax_y:
                    ymax_y = y
                    
            elif (r, g, b) == blue:
                if x < bmin_x:
                    bmin_x = x
                if x > bmax_x:
                    bmax_x = x
                if y < bmin_y:
                    bmin_y = y
                if y > bmax_y:
                    bmax_y = y 
                    
            elif (r, g, b) == red:                        
                if x < rmin_x:
                    rmin_x = x
                if x > rmax_x:
                    rmax_x = x
                if y < rmin_y:
                    rmin_y = y
                if y > rmax_y:
                    rmax_y = y                             
    
    # crop each color based on the coordinates obtained by detecting the specif color 
      
    greensec = picture.crop((gmin_x, gmin_y, gmax_x+1 , gmax_y+1))
    
    yellowsec = picture.crop((ymin_x, ymin_y, ymax_x+1, ymax_y+1))
    
    bluesec = picture.crop((bmin_x, bmin_y, bmax_x+1, bmax_y+1))
    
    redsec = picture.crop((rmin_x, rmin_y, rmax_x+1, rmax_y+1))
    
    # resize each section based on the size of the green section
    
    new_width, new_height = greensec.size
            
    yellowsec = yellowsec.resize((new_width, new_height))
        
    bluesec = bluesec.resize((new_width, new_height))
    
    redsec = redsec.resize((new_width, new_height))
    
    # rotate each section to its correct orientation
    
    greensec = greensec.transpose(Image.ROTATE_270)
    
    bluesec = bluesec.transpose(Image.ROTATE_180)
    
    redsec = redsec.transpose(Image.ROTATE_90)
    
    # paste the fixed section into the new image
    
    fixedpic = Image.new("RGB", (width,height))
    
    fixedpic.paste(redsec, (0,0))
    
    fixedpic.paste(bluesec, (halfwidth,0))
    
    fixedpic.paste(yellowsec, (0,halfheight))
    
    fixedpic.paste(greensec, (halfwidth,halfheight))
    
    return fixedpic

# Purpose: creating an angry robot

def draw_image():
    
    from PIL import Image, ImageDraw
    
    img = Image.new("RGB", (400,400), (0,102,102))
    
    w,h = img.size
        
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([(75,75), (325,325)], (128,128,128), (0,0,0))
    draw.rectangle([(25,150), (75,225)], (128,128,128), (0,0,0))
    draw.rectangle([(325,150), (375,225)], (128,128,128), (0,0,0))
    draw.ellipse([(118,135), (155,180)], (102,0,204))
    draw.ellipse([(244,135), (281,180)], (102,0,204))
    draw.polygon([(175,325), (226,325), (200,380)], (77,0,0), (0,0,0))
    draw.polygon([(175,180), (226,180), (200,250)], (230,238,255), (0,0,0))
    draw.line([(110,110), (165,125)], (0, 128, 102), 6)
    draw.line([(290,110), (230,125)], (0, 128, 102), 6)
    draw.line([(160,275), (240,275)], (130, 96, 102), 6)
    draw.text((275,375), "Angry Robot", (255, 198, 26))
    
    return img

# Purpose: Displaying and placing my drawing into the corrected frame

def frame_image(frame):
    
    framed = repair_frame(frame)
    
    drawing = draw_image()
    
    width,height = framed.size
    
    drawingwidth = int(width * 0.8)
    
    drawingheight = int(height * 0.8)
    
    drawing = drawing.resize(((drawingwidth), (drawingheight)))
    
    x = (width - drawingwidth) // 2
    y = (height - drawingheight) // 2
    
    framed.paste(drawing, (x,y))
    
    framed.show()
    
frame_image("broken_760.png")