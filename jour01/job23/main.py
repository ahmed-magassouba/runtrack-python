def draw_traiangle(height):
    for i in range(height):
        if(i < height - 1):     
          print(" "*(height-i-1)+
              "/"+" "*(i*2)+
              "\\")
        if(i == height - 1):
            print("/"+"_"*(i*2)+"\\")
   
draw_traiangle(5)