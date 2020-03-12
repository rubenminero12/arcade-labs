import arcade


def draw_section_outlines():
    # Draw squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

    # Draw squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)


def draw_section_1():
    for row in range(30):
        row=(row+0.5)*10
        for column in range(30):
            column=(column+0.5)*10
            arcade.draw_rectangle_filled(column, row, 5, 5, arcade.color.WHITE)


def draw_section_2():
    for row in range(30):
        row=(row+0.5)*10
        contador=1
        for column in range(30):
            column=(column+30.5)*10
            if (contador % 2!=0):
                arcade.draw_rectangle_filled(column, row, 5, 5, arcade.color.WHITE)
            else:
                arcade.draw_rectangle_filled(column, row, 5, 5, arcade.color.BLACK)
            contador+=1

            



def draw_section_3():
    contador=1
    for row in range(30):
        row=(row+0.5)*10
        if (contador % 2!=0):
            color=arcade.color.WHITE
        else:
            color=arcade.color.BLACK    
        contador+=1
        for column in range(30):
            column=(column+60.5)*10
            arcade.draw_rectangle_filled(column, row, 5, 5,color)
           

def draw_section_4():
    contador=1
    contador2=1
    for row in range(30):
        row=(row+0.5)*10
        if (contador2 % 2!=0):
            color=arcade.color.BLACK    
        contador2+=1
        for column in range(30):
            column=(column+90.5)*10
            if (contador2 % 2!=0):
                arcade.draw_rectangle_filled(column, row, 5, 5,color)
            else:
                if (contador % 2!=0):
                    arcade.draw_rectangle_filled(column, row, 5, 5, arcade.color.WHITE)
                else:
                    arcade.draw_rectangle_filled(column, row, 5, 5, arcade.color.BLACK)
            contador+=1



def draw_section_5():
    for row in range(30):
        y=row
        row=(row+30.5)*10
        for column in range(30-y):
            column=(column+0.5+y)*10
            arcade.draw_rectangle_filled(column, row, 5, 5, arcade.color.WHITE)

        
        

            



def draw_section_6():
    for row in range(30):
        y=row
        row=(row+30.5)*10
        for column in range(30-y):
            column=(column+30.5)*10
            arcade.draw_rectangle_filled(column, row, 5, 5, arcade.color.WHITE)


def draw_section_7():
    for row in range(30):
        y=29-row
        row=(row+30.5)*10
        for column in range(30-y):
            column=(column+60.5)*10
            arcade.draw_rectangle_filled(column, row, 5, 5, arcade.color.WHITE)


def draw_section_8():
    for row in range(30,-1,-1):
        y=row
        ys=29-(y)
        row=(row+30.5)*10
        for column in range(y+1):
            column=(column+90.5+ys)*10
            arcade.draw_rectangle_filled(column, row, 5, 5, arcade.color.WHITE)


def main():
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Draw the outlines for the sections
    draw_section_outlines()

    # Draw the sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()


main()