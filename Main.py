import time
import subprocess
no_turtle_file_path = "Extras/No_Turtle"
try:
    import turtle
except:
    try:
        subprocess.run(no_turtle_file_path)
    except:
        pass
    pass


screen = turtle.Screen()
screen.title("The Dungeon Company")
screen.bgcolor("black")
screen.setup(width=1500, height=900)
stone_floor1_path = "Assets/stone brick floor 1.gif"
debug_stone_floor1_path = "C:/Users/Kasen/OneDrive/Documents/The_Dungeon_Company/Assets/stone brick floor 1.gif"
stone_wall1_path = "Assets/stone brick wall 1.gif"
debug_stone_wall1_path = "C:/Users/Kasen/OneDrive/Documents/The_Dungeon_Company/Assets/stone brick wall 1.gif"
stone_wall2_path = "Assets/stone brick wall 2.gif"
debug_stone_wall2_path = "C:/Users/Kasen/OneDrive/Documents/The_Dungeon_Company/Assets/stone brick wall 2.gif"
stone_wall3_path = "Assets/stone brick wall 3.gif"
debug_stone_wall3_path = "C:/Users/Kasen/OneDrive/Documents/The_Dungeon_Company/Assets/stone brick wall 3.gif"
stone_wall4_path = "Assets/stone brick wall 4.gif"
debug_stone_wall4_path = "C:/Users/Kasen/OneDrive/Documents/The_Dungeon_Company/Assets/stone brick wall 4.gif"
stone_wall5_path = "Assets/stone brick wall 5.gif"
debug_stone_wall5_path = "C:/Users/Kasen/OneDrive/Documents/The_Dungeon_Company/Assets/stone brick wall 5.gif"
stickman_character1_path = "Assets/stickman char 1.gif"
debug_stickman_character1_path = "C:/Users/Kasen/OneDrive/Documents/The_Dungeon_Company/Assets/stickman char 1.gif"
stickman_character2_path = "Assets/stickman char 2.gif"
debug_stickman_character2_path = "C:/Users/Kasen/OneDrive/Documents/The_Dungeon_Company/Assets/stickman char 2.gif"
stickman_character2_1_path = "Assets/stickman char 2_1.gif"
debug_stickman_character2_1_path = "C:/Users/Kasen/OneDrive/Documents/The_Dungeon_Company/Assets/stickman char 2_1.gif"
stickman_character2_2_path = "Assets/stickman char 2_2.gif"
debug_stickman_character2_2_path = "C:/Users/Kasen/OneDrive/Documents/The_Dungeon_Company/Assets/stickman char 2_2.gif"
door1_path = "Assets/door.gif"
debug_door1_path = "C:/Users/Kasen/OneDrive/Documents/The_Dungeon_Company/Assets/door.gif"
square_path = "Assets/square.gif"
debug_square_path = "C:/Users/Kasen/OneDrive/Documents/The_Dungeon_Company/Assets/square.gif"

error_text = "Automatic Fix For This Error Available, Attempting Repair..."
e = "ERROR Code |"
d = "Debug Code |"
d1 = "Debug? |"
e1 = "This error code is similar to error code 1 but with a different sprite."

error_data = {'?': "This error code means that the error you are experiencing is either expected, unknown, or a placeholder",
              '1': "This error code means nothing if you are not a dev of the game (it means the debug file path of a sprite is not able to load due to a error, this doesn't affect your game)", 
              '2': e1,
              '3': e1,
              '4': e1, 
              '5': e1, 
              '6': e1, 
              '7': e1, 
              '8': e1, 
              '9': "This error code means that the variable 'y_above_wanted' or any of the other 3 variables similar to it is neither at 1 or 0 when a key 'w, a, s, or d', it should only be at 1 or 0 if a console command is not used to change it.", 
              '10': "This error code means that the variable 'x_above_wanted' and 'x_below_wanted' are both '1' at the same time, this shouldn't be possible without hardcode console commands but we have ran into issues of this error happening without them somehow.", 
              '11': "This error code means that the variable 'y_above_wanted' is '1' even though the character's y position isn't high enough for this to happen.", 
              '12': "This error code means that when the 'esc' key is pressed in settings it is running into an error where it cannot clear the Turtle(s) graphics, audio, etc.",
              '13': "This error code means that 'y1' variable isn't accessible in the 'w' or 's' key function(s)",
              '14': e1,
              '15': e1,
              '16': e1}

y1 = 0
x1 = 0

def a_key1():
    pass

def d_key1():
    pass

def s_key1():
    pass

def w_key1():
    pass


def calc1():
    global stickman_character2_calc2
    stickman_character2_calc2 = stickman_character2.ycor()
    stickman_character2_calc2 = stickman_character2_calc2 - 5

def calc():
    global stickman_character2_calc1
    stickman_character2_calc1 = stickman_character2.xcor()
    stickman_character2_calc1 = stickman_character2_calc1 + 5
    print(d1, e, "0011-2 Fix |", stickman_character2_calc1)

def d_key():
    global stickman_character_check, x1_above_wanted
    if starting_screen == 0:
        if stickman_character_check == 1:
            if x1_above_wanted == 1:
                print(d, "0013-2")
                if x1_above_wanted == 1 and x1_below_wanted == 1:
                    print(e, "0010-2")
                    print(error_text)
                    stickman_character2.goto(-345, y1)
                    x1_above_wanted = 0
                elif x1_above_wanted == 1 and stickman_character2.xcor() < 275:
                    print(e, "0011-2")
                    print(error_text)
                    calc()
                    stickman_character2.goto(stickman_character2_calc1, y1)
                    x1_above_wanted = 0
                    if y1 == 195 and x1 >= -65 and x1 <= -5:
                        print("open door")
                        door.clear()
            elif x1_above_wanted == 0:
                print(d, "0011-5")
                stickman_character2.penup()
                stickman_character2.forward(5)
                test_rn()
                try:
                    stickman_character2.shape(stickman_character2_1_path)
                except:
                    try:
                        stickman_character2.shape(debug_stickman_character2_1_path)
                    except:
                        pass
                if y1 >= 195 and x1 >= -65 and x1 <= -5:
                    print("open door")
                    door.clear()
            else:
                print(e, "9-4")
        else:
            print(d, "12-4")
    elif starting_screen == 1:
        print(d, "10-4")


def s_key():
    global stickman_character_check, y1
    if starting_screen == 0:
        if stickman_character_check == 1:
            if y1_below_wanted == 1:
                pass
            elif y1_below_wanted == 0:
                if not y1 == -195 or not -195 >= y1:
                    print(d, "0011-4-2")
                    stickman_character2.penup()
                    y_thing = stickman_character2.ycor()
                    stickman_character2.sety(y_thing - 5)
                    test_rn()
                else:
                    print(d, "9-3")
                    print(y1)
            else:
                print(e, "9-3")
    elif starting_screen == 1:
        print(d, "0010-3")



def a_key():
    global stickman_character_check
    if starting_screen == 0:
        if stickman_character_check == 1:
            if x1_below_wanted == 1:
                print(d, "0013-1")
            elif x1_below_wanted == 0:
                print(d, "0011-3")
                stickman_character2.penup()
                stickman_character2.backward(5)
                test_rn()
                try:
                    stickman_character2.shape(stickman_character2_2_path)
                except:
                    try:
                        stickman_character2.shape(debug_stickman_character2_2_path)
                    except:
                        pass
                if y1 >= 195 and x1 >= -65 and x1 <= -5:
                    print("door open")
                    door.clear()
            else:
                print(e, "9-2")
        else:
            print(d, "12-2")
    elif starting_screen == 1:
        print(d, "10-2")


def w_key():
    global stickman_character_check, y1_above_wanted, y1
    if starting_screen == 0:
        if stickman_character_check == 1:
            if y1_above_wanted == 1:
                pass
            elif y1_above_wanted == 0:
                try:
                    if y1 > 245:
                        pass
                    else:
                        stickman_character2.penup()
                        y_thing = stickman_character2.ycor()
                        stickman_character2.sety(y_thing + 5)
                        test_rn()
                        if y1 >= 195 and x1 >= -65 and x1 <= -5:
                            print("door open")
                            door.clear()
                except:
                    print(e, "13")
                    pass
            else:
                print(e, "9-1")

def esc_key():
    if settings_screen == 1:
        setup()
        try:
            graphics.clear()
            controls.clear()
            audio.clear()
        except:
            print(e, "12")
    elif settings_screen == 0:
        pass
    elif settings_screen < 0 or settings_screen > 1:
        pass

def f1_key():
    global console_command1, stickman_character_check, y1_below_wanted, y1_above_wanted, y1
    console_command1 = input("Console Command Terminal: ")
    if console_command1 == "level1floordelete" or console_command1 == "lev1floordel" or console_command1 == "0" or console_command1 == "floor.clear()":
        floor.clear()
        console_command1 = 0
    elif console_command1 == "stickmancharacterselect" or console_command1 == "stickmancharsel" or console_command1 == "stickman char sel" or console_command1 == "1":
        print("Debug Code 0011-1")
        stickman_character_check = 1
        console_command1 = 0
    elif console_command1 == "printstickmancharactercheck" or console_command1 == "printstickmancharcheck" or console_command1 == "2" or console_command1 == "print(stickman_character_check)":
        print(stickman_character_check)
        console_command1 = 0
    elif console_command1 == "printy1" or console_command1 == "print y1":
        print(y1)
    elif console_command1 == "print x1 below" or console_command1 == "printx1below":
        print(x1_below_wanted)
    elif console_command1 == "print x1 above" or console_command1 == "printx1above":
        print(x1_above_wanted)
    elif console_command1 == "calc c" or console_command1 == "calcc":
        calc()
    elif console_command1 == "set y below wanted" or console_command1 == "set y s" or console_command1 == "setys" or console_command1 == "setybelowwanted" or console_command1 == "6":
        setybelowwanted = input("Set Variable 'y1_below_wanted' to | ")
        if setybelowwanted == "0":
            y1_below_wanted = 0
        elif setybelowwanted == "1":
            y1_below_wanted = 1
        else:
            print("error, cannot set to a value that is not 0 or 1")
    elif console_command1 == "set y above wanted" or console_command1 == "set y w" or console_command1 == "setyw" or console_command1 == "setyabovewanted" or console_command1 == "7":
        setyabovewanted = input("Set Variable 'y1_above_wanted' to | ")
        if setyabovewanted == "0":
            y1_above_wanted = 0
        elif setyabovewanted == "1":
            y1_above_wanted = 1
        else:
            print("error, cannot set to a value that is not 0 or 1")
    elif console_command1 == "errorcodes" or console_command1 == "error codes" or console_command1 == "errorinfo" or console_command1 == "error info" or console_command1 == "8":
        inputerrorthing = input("What error number do you want more info about? | ")
        try:
            print(error_data[inputerrorthing])
        except:
            print("No known error with that code")
    elif console_command1 == "print y above wanted" or console_command1 == "printyabovewanted" or console_command1 == "printyw" or console_command1 == "9":
        print(y1_above_wanted)
    elif console_command1 == "stickmangoto" or console_command1 == "stickman goto" or console_command1 == "10":
        stickmangoto1 = input("X coordinate | ")
        stickmangoto2 = input("Y coordinate | ")
        stickmangoto1 = int(stickmangoto1)
        stickmangoto2 = int(stickmangoto2)
        stickman_character2.goto(stickmangoto1, stickmangoto2)

turtle.onkey(f1_key, 'F1')
turtle.onkey(esc_key, 'Escape')
turtle.onkeypress(w_key, 'w')
turtle.onkeyrelease(w_key1, 'w')
turtle.onkeypress(a_key, 'a')
turtle.onkeyrelease(a_key1, 'a')
turtle.onkeypress(s_key, 's')
turtle.onkeyrelease(s_key1, 's')
turtle.onkeypress(d_key, 'd')
turtle.onkeyrelease(d_key1, 'd')

x1_below_wanted = 0
x1_above_wanted = 0
y1_below_wanted = 0
y1_above_wanted = 0

settings_screen = 0
try:
    screen.addshape(stone_floor1_path)
except:
    print(d, "0002")
    pass

try:
    screen.addshape(debug_stone_floor1_path)
except:
    print(e, "1")
    pass

try:
    screen.addshape(stone_wall1_path)
except:
    print(d, "3")
    pass

try:
    screen.addshape(debug_stone_wall1_path)
except:
    print(e, "2")
    pass

try:
    screen.addshape(stone_wall2_path)
except:
    print(d, "4")
    pass

try:
    screen.addshape(debug_stone_wall2_path)
except:
    print(e, "3")
    pass

try:
    screen.addshape(stone_wall3_path)
except:
    print(d, "5")
    pass

try:
    screen.addshape(debug_stone_wall3_path)
except:
    print(e, "4")
    pass

try:
    screen.addshape(stone_wall4_path)
except:
    print(d, "6")
    pass

try:
    screen.addshape(debug_stone_wall4_path)
except:
    print(e, "5")
    pass

try:
    screen.addshape(stone_wall5_path)
except:
    print("Debug Code 0007")
    pass

try:
    screen.addshape(debug_stone_wall5_path)
except:
    print(e, "6")
    pass

try:
    screen.addshape(stickman_character1_path)
except:
    print("Debug Code 0008")
    pass

try:
    screen.addshape(debug_stickman_character1_path)
except:
    print(e, "7")
    pass

try:
    screen.addshape(stickman_character2_path)
except:
    print("Debug Code 0009")
    pass

try:
    screen.addshape(debug_stickman_character2_path)
except:
    print(e, "8")
    pass

try:
    screen.addshape(door1_path)
except:
    pass

try:
    screen.addshape(debug_door1_path)
except:
    print(e, "14")
    pass

try:
    screen.addshape(stickman_character2_1_path)
except:
    pass

try:
    screen.addshape(debug_stickman_character2_1_path)
except:
    print(e, "15")
    pass

try:
    screen.addshape(stickman_character2_2_path)
except:
    pass

try:
    screen.addshape(debug_stickman_character2_2_path)
except:
    print(e, '16')
    pass

try:
    screen.addshape(square_path)
except:
    pass

try:
    screen.addshape(debug_square_path)
except:
    print(e, "17")
    pass

turtle.listen()

def setup():
    global starting_screen, title, start, stickman_character_check, settings, settings_screen
    stickman_character_check = 0
    starting_screen = 1
    settings_screen = 0
    title = turtle.Turtle()
    title.speed(0)
    title.color("white")
    title.penup()
    title.hideturtle()
    title.goto(0, 300)
    title.write("The Dungeon Company", align="center", font=("Courier", 40, "normal"))
    
    start = turtle.Turtle()
    start.speed(0)
    start.color("white")
    start.penup()
    start.hideturtle()
    start.goto(-200, 100)
    start.write("Start", align="center", font=("Courier", 40, "normal"))

    settings = turtle.Turtle()
    settings.speed(0)
    settings.color("white")
    settings.penup()
    settings.hideturtle()
    settings.goto(-400, -300)
    settings.write("Settings", align="center", font=("Courier", 40, "normal"))
    

def test_rn():
    global x1, y1, x1_below_wanted, x1_above_wanted, y1_below_wanted, y1_above_wanted
    x1 = stickman_character2.xcor()
    print("Debug Code? | x_move/xcor()", x1)
    y1 = stickman_character2.ycor()
    print("Debug Code? | y_move/ycor()", y1)
    if x1 <= -345:
        x1_below_wanted = 1
    elif x1 >= -345 and x1 <= 275:
        x1_below_wanted = 0
    elif x1 >= 275:
        x1_above_wanted = 1
    elif x1 <= 275 and x1 >= -345:
        x1_above_wanted = 0
    elif y1 >= 250:
        y1_above_wanted = 1
    elif y1 <= -170:
        y1_below_wanted = 1
    elif y1 < 250 and y1 > -170:
        y1_above_wanted = 0
        y1_below_wanted = 0



def draw_char_select1():
    global stickman_character1, stickman_character2
    stickman_character1.speed(0)
    stickman_character1.penup()
    stickman_character1.hideturtle()
    stickman_character2.speed(0)
    stickman_character2.penup()
    stickman_character2.hideturtle()
    stickman_character2.goto(-30, 10)
    stickman_character2.showturtle()
    stickman_character2.speed(1)


def draw_wall1():
    wall.speed(0)
    wall1.speed(0)
    wall2.speed(0)
    wall3.speed(0)
    wall4.speed(0)
    wall.penup()
    wall1.penup()
    wall2.penup()
    wall3.penup()
    wall4.penup()
    turtle.tracer(0, 0)
    wall1.goto(300, 250)
    wall1.stamp()
    wall1.goto(250, 250)
    wall1.stamp()
    wall1.goto(200, 250)
    wall1.stamp()
    wall1.goto(150, 250)
    wall1.stamp()
    wall1.goto(100, 250)
    wall1.stamp()
    wall1.goto(50, 250)
    wall1.stamp()
    wall1.goto(-50, 250)
    wall1.stamp()
    wall1.goto(-100, 250)
    wall1.stamp()
    wall1.goto(-150, 250)
    wall1.stamp()
    wall1.goto(-200, 250)
    wall1.stamp()
    wall1.goto(-250, 250)
    wall1.stamp()
    wall1.goto(-300, 250)
    wall1.stamp()
    wall.goto(-300, 300)
    wall.stamp()
    wall.goto(-250, 300)
    wall.stamp()
    wall.goto(-200, 300)
    wall.stamp()
    wall.goto(-150, 300)
    wall.stamp()
    wall.goto(-100, 300)
    wall.stamp()
    wall.goto(-50, 300)
    wall.stamp()
    wall.goto(50, 300)
    wall.stamp()
    wall.goto(100, 300)
    wall.stamp()
    wall.goto(150, 300)
    wall.stamp()
    wall.goto(200, 300)
    wall.stamp()
    wall.goto(250, 300)
    wall.stamp()
    wall.goto(300, 300)
    wall.stamp()
    wall2.goto(-335, 323)
    wall2.stamp()
    wall2.goto(-335, 298)
    wall2.stamp()
    wall2.goto(-335, 273)
    wall2.stamp()
    wall2.goto(-335, 248)
    wall2.stamp()
    wall2.goto(-335, 223)
    wall2.stamp()
    wall2.goto(-335, 198)
    wall2.stamp()
    wall2.goto(-335, 173)
    wall2.stamp()
    wall2.goto(-335, 148)
    wall2.stamp()
    wall2.goto(-335, 123)
    wall2.stamp()
    wall2.goto(-335, 98)
    wall2.stamp()
    wall2.goto(-335, 73)
    wall2.stamp()
    wall2.goto(-335, 48)
    wall2.stamp()
    wall2.goto(-335, 23)
    wall2.stamp()
    wall2.goto(-335, -2)
    wall2.stamp()
    wall2.goto(-335, -27)
    wall2.stamp()
    wall2.goto(-335, -52)
    wall2.stamp()
    wall2.goto(-335, -77)
    wall2.stamp()
    wall2.goto(-335, -102)
    wall2.stamp()
    wall2.goto(-335, -127)
    wall2.stamp()
    wall2.goto(-335, -152)
    wall2.stamp()
    wall2.goto(-335, -177)
    wall2.stamp()
    wall2.goto(-335, -202)
    wall2.stamp()
    wall3.goto(-335, -217)
    wall3.stamp()
    wall3.goto(-315, -217)
    wall3.stamp()
    wall3.goto(-290, -217)
    wall3.stamp()
    wall3.goto(-265, -217)
    wall3.stamp()
    wall3.goto(-240, -217)
    wall3.stamp()
    wall3.goto(-215, -217)
    wall3.stamp()
    wall3.goto(-190, -217)
    wall3.stamp()
    wall3.goto(-165, -217)
    wall3.stamp()
    wall3.goto(-140, -217)
    wall3.stamp()
    wall3.goto(-115, -217)
    wall3.stamp()
    wall3.goto(-90, -217)
    wall3.stamp()
    wall3.goto(-65, -217)
    wall3.stamp()
    wall3.goto(-40, -217)
    wall3.stamp()
    wall3.goto(-15, -217)
    wall3.stamp()
    wall3.goto(10, -217)
    wall3.stamp()
    wall3.goto(35, -217)
    wall3.stamp()
    wall3.goto(60, -217)
    wall3.stamp()
    wall3.goto(85, -217)
    wall3.stamp()
    wall3.goto(110, -217)
    wall3.stamp()
    wall3.goto(135, -217)
    wall3.stamp()
    wall3.goto(160, -217)
    wall3.stamp()
    wall3.goto(185, -217)
    wall3.stamp()
    wall3.goto(210, -217)
    wall3.stamp()
    wall3.goto(235, -217)
    wall3.stamp()
    wall3.goto(260, -217)
    wall3.stamp()
    wall3.goto(285, -217)
    wall3.stamp()
    wall3.goto(310, -217)
    wall3.stamp()
    wall3.goto(320, -217)
    wall3.stamp()
    wall4.goto(330, 323)
    wall4.stamp()
    wall4.goto(330, 298)
    wall4.stamp()
    wall4.goto(330, 273)
    wall4.stamp()
    wall4.goto(330, 248)
    wall4.stamp()
    wall4.goto(330, 223)
    wall4.stamp()
    wall4.goto(330, 198)
    wall4.stamp()
    wall4.goto(330, 173)
    wall4.stamp()
    wall4.goto(330, 148)
    wall4.stamp()
    wall4.goto(330, 123)
    wall4.stamp()
    wall4.goto(330, 98)
    wall4.stamp()
    wall4.goto(330, 73)
    wall4.stamp()
    wall4.goto(330, 48)
    wall4.stamp()
    wall4.goto(330, 23)
    wall4.stamp()
    wall4.goto(330, -2)
    wall4.stamp()
    wall4.goto(330, -27)
    wall4.stamp()
    wall4.goto(330, -52)
    wall4.stamp()
    wall4.goto(330, -77)
    wall4.stamp()
    wall4.goto(330, -102)
    wall4.stamp()
    wall4.goto(330, -127)
    wall4.stamp()
    wall4.goto(330, -152)
    wall4.stamp()
    wall4.goto(330, -177)
    wall4.stamp()
    wall4.goto(330, -202)
    wall4.stamp()
    turtle.update()
    turtle.tracer(1, 10)

def draw_floor1():
    floor.speed(0)
    turtle.tracer(0, 0)
    floor.goto(0, 0)
    floor.stamp()
    floor.hideturtle()
    floor.goto(50, 0)
    floor.stamp()
    floor.goto(100, 0)
    floor.stamp()
    floor.goto(150, 0)
    floor.stamp()
    floor.goto(200, 0)
    floor.stamp()
    floor.goto(250, 0)
    floor.stamp()
    floor.goto(300, 0)
    floor.stamp()
    floor.goto(300, 50)
    floor.stamp()
    floor.goto(300, 100)
    floor.stamp()
    floor.goto(300, 150)
    floor.stamp()
    floor.goto(300, 200)
    floor.stamp()
    floor.goto(250, 200)
    floor.stamp()
    floor.goto(200, 200)
    floor.stamp()
    floor.goto(150, 200)
    floor.stamp()
    floor.goto(100, 200)
    floor.stamp()
    floor.goto(50, 200)
    floor.stamp()
    floor.goto(0, 200)
    floor.stamp()
    floor.goto(-50, 200)
    floor.stamp()
    floor.goto(-100, 200)
    floor.stamp()
    floor.goto(-150, 200)
    floor.stamp()
    floor.goto(-200, 200)
    floor.stamp()
    floor.goto(-250, 200)
    floor.stamp()
    floor.goto(-300, 200)
    floor.stamp()
    floor.goto(-300, 150)
    floor.stamp()
    floor.goto(-250, 150)
    floor.stamp()
    floor.goto(-200, 150)
    floor.stamp()
    floor.goto(-150, 150)
    floor.stamp()
    floor.goto(-100, 150)
    floor.stamp()
    floor.goto(-50, 150)
    floor.stamp()
    floor.goto(0, 150)
    floor.stamp()
    floor.goto(50, 150)
    floor.stamp()
    floor.goto(100, 150)
    floor.stamp()
    floor.goto(150, 150)
    floor.stamp()
    floor.goto(200, 150)
    floor.stamp()
    floor.goto(250, 150)
    floor.stamp()
    floor.goto(250, 100)
    floor.stamp()
    floor.goto(200, 100)
    floor.stamp()
    floor.goto(150, 100)
    floor.stamp()
    floor.goto(100, 100)
    floor.stamp()
    floor.goto(50, 100)
    floor.stamp()
    floor.goto(0, 100)
    floor.stamp()
    floor.goto(-50, 100)
    floor.stamp()
    floor.goto(-100, 100)
    floor.stamp()
    floor.goto(-150, 100)
    floor.stamp()
    floor.goto(-200, 100)
    floor.stamp()
    floor.goto(-250, 100)
    floor.stamp()
    floor.goto(-300, 100)
    floor.stamp()
    floor.goto(-300, 50)
    floor.stamp()
    floor.goto(-250, 50)
    floor.stamp()
    floor.goto(-200, 50)
    floor.stamp()
    floor.goto(-150, 50)
    floor.stamp()
    floor.goto(-100, 50)
    floor.stamp()
    floor.goto(-50, 50)
    floor.stamp()
    floor.goto(0, 50)
    floor.stamp()
    floor.goto(50, 50)
    floor.stamp()
    floor.goto(100, 50)
    floor.stamp()
    floor.goto(150, 50)
    floor.stamp()
    floor.goto(200, 50)
    floor.stamp()
    floor.goto(250, 50)
    floor.stamp()
    floor.penup()
    floor.goto(-50, 0)
    floor.stamp()
    floor.goto(-100, 0)
    floor.stamp()
    floor.goto(-150, 0)
    floor.stamp()
    floor.goto(-200, 0)
    floor.stamp()
    floor.goto(-250, 0)
    floor.stamp()
    floor.goto(-300, 0)
    floor.stamp()
    floor.goto(-300, -50)
    floor.stamp()
    floor.goto(-250, -50)
    floor.stamp()
    floor.goto(-200, -50)
    floor.stamp()
    floor.goto(-150, -50)
    floor.stamp()
    floor.goto(-100, -50)
    floor.stamp()
    floor.goto(-50, -50)
    floor.stamp()
    floor.goto(0, -50)
    floor.stamp()
    floor.goto(50, -50)
    floor.stamp()
    floor.goto(100, -50)
    floor.stamp()
    floor.goto(150, -50)
    floor.stamp()
    floor.goto(200, -50)
    floor.stamp()
    floor.goto(250, -50)
    floor.stamp()
    floor.goto(300, -50)
    floor.stamp()
    floor.goto(300, -100)
    floor.stamp()
    floor.goto(250, -100)
    floor.stamp()
    floor.goto(200, -100)
    floor.stamp()
    floor.goto(150, -100)
    floor.stamp()
    floor.goto(100, -100)
    floor.stamp()
    floor.goto(50, -100)
    floor.stamp()
    floor.goto(0, -100)
    floor.stamp()
    floor.goto(-50, -100)
    floor.stamp()
    floor.goto(-100, -100)
    floor.stamp()
    floor.goto(-150, -100)
    floor.stamp()
    floor.goto(-200, -100)
    floor.stamp()
    floor.goto(-250, -100)
    floor.stamp()
    floor.goto(-300, -100)
    floor.stamp()
    floor.goto(-300, -150)
    floor.stamp()
    floor.goto(-250, -150)
    floor.stamp()
    floor.goto(-200, -150)
    floor.stamp()
    floor.goto(-150, -150)
    floor.stamp()
    floor.goto(-100, -150)
    floor.stamp()
    floor.goto(-50, -150)
    floor.stamp()
    floor.goto(0, -150)
    floor.stamp()
    floor.goto(50, -150)
    floor.stamp()
    floor.goto(100, -150)
    floor.stamp()
    floor.goto(150, -150)
    floor.stamp()
    floor.goto(200, -150)
    floor.stamp()
    floor.goto(250, -150)
    floor.stamp()
    floor.goto(300, -150)
    floor.stamp()
    floor.goto(300, -200)
    floor.stamp()
    floor.goto(250, -200)
    floor.stamp()
    floor.goto(200, -200)
    floor.stamp()
    floor.goto(150, -200)
    floor.stamp()
    floor.goto(100, -200)
    floor.stamp()
    floor.goto(50, -200)
    floor.stamp()
    floor.goto(0, -200)
    floor.stamp()
    floor.goto(-50, -200)
    floor.stamp()
    floor.goto(-100, -200)
    floor.stamp()
    floor.goto(-150, -200)
    floor.stamp()
    floor.goto(-200, -200)
    floor.stamp()
    floor.goto(-250, -200)
    floor.stamp()
    floor.goto(-300, -200)
    floor.stamp()
    turtle.update()
    turtle.tracer(1, 10)


def draw_squares():
    turtle.tracer(0, 0)
    square = turtle.Turtle()
    square.penup()
    try:
        square.shape(square_path)
    except:
        try:
            square.shape(debug_square_path)
        except:
            pass
    square1 = turtle.Turtle()
    square1.penup()
    try:
        square1.shape(square_path)
    except:
        try:
            square1.shape(debug_square_path)
        except:
            pass
    square2 = turtle.Turtle()
    square2.penup()
    try:
        square2.shape(square_path)
    except:
        try:
            square2.shape(debug_square_path)
        except:
            pass
    square3 = turtle.Turtle()
    square3.penup()
    try:
        square3.shape(square_path)
    except:
        try:
            square3.shape(debug_square_path)
        except:
            pass
    square.goto(-300, -300)
    square1.goto(-100, -300)
    square2.goto(100, -300)
    square3.goto(300, -300)
    turtle.update()
    turtle.tracer(1, 10)


def draw_doors1():
    turtle.tracer(0, 0)
    door.goto(-8, 262)
    door.stamp()
    turtle.tracer(1, 10)
    turtle.update()


def start_click():
    global floor, wall, wall1, wall2, wall3, wall4, stickman_character1, starting_screen, stickman_character2, char_select, door
    starting_screen = 0
    char_select = 1
    start.clear()
    settings.clear()
    title.clear()
    floor = turtle.Turtle()
    try:
        floor.shape(stone_floor1_path)
    except:
        floor.shape(debug_stone_floor1_path)
    floor.hideturtle()
    wall = turtle.Turtle()
    try:
        wall.shape(stone_wall1_path)
    except:
        wall.shape(debug_stone_wall1_path)
    wall.hideturtle()
    wall1 = turtle.Turtle()
    try:
        wall1.shape(stone_wall2_path)
    except:
        wall1.shape(debug_stone_wall2_path)
    wall1.hideturtle()
    wall2 = turtle.Turtle()
    try:
        wall2.shape(stone_wall3_path)
    except:
        wall2.shape(debug_stone_wall3_path)
    wall2.hideturtle()
    wall3 = turtle.Turtle()
    try:
        wall3.shape(stone_wall4_path)
    except:
        wall3.shape(debug_stone_wall4_path)
    wall3.hideturtle()
    wall4 = turtle.Turtle()
    try:
        wall4.shape(stone_wall5_path)
    except:
        wall4.shape(debug_stone_wall5_path)
    wall4.hideturtle()
    stickman_character1 = turtle.Turtle()
    stickman_character1.hideturtle()
    try:
        stickman_character1.shape(stickman_character1_path)
    except:
        stickman_character1.shape(debug_stickman_character1_path)
    draw_wall1()
    draw_floor1()
    stickman_character2 = turtle.Turtle()
    try:
        stickman_character2.shape(stickman_character2_path)
    except:
        stickman_character2.shape(debug_stickman_character2_path)
        draw_char_select1()
    door = turtle.Turtle()
    try:
        door.shape(door1_path)
    except:
        door.shape(debug_door1_path)
    door.speed(0)
    door.penup()
    door.hideturtle()
    draw_doors1()
    draw_squares()



def settings_click():
    global starting_screen, settings_screen, graphics, audio, controls
    start.clear()
    title.clear()
    settings.clear()
    starting_screen = 0
    settings_screen = 1
    #
    graphics = turtle.Turtle()
    graphics.speed(0)
    graphics.color("white")
    graphics.penup()
    graphics.hideturtle()
    graphics.goto(-600, 400)
    graphics.write("Graphics", align="center", font=("Courier", 30, "normal"))
    #
    controls = turtle.Turtle()
    controls.speed(0)
    controls.color("white")
    controls.penup()
    controls.hideturtle()
    controls.goto(-350, 400)
    controls.write("Controls", align="center", font=("Courier", 30, "normal"))
    #
    audio = turtle.Turtle()
    audio.speed(0)
    audio.color("white")
    audio.penup()
    audio.hideturtle()
    audio.goto(-150, 400)
    audio.write("Audio", align="center", font=("Courier", 30, "normal"))





def click_mechanic(x, y):
    print("Testing 1, clicked at", x, y)
    if starting_screen == 1:
        if -280 <= x <= -125 and 113 <= y <= 152:
            print("Debug Code 0001-1")
            start_click()
        elif -527 <= x <= -278 and -287 <= y <= -252:
            print("Debug Code 0001-2")
            settings_click()

settings_data = [
'Testing 1, clicked at -526.0 -251.0',
'Testing 1, clicked at -276.0 -254.0',
'Testing 1, clicked at -281.0 -286.0',
'Testing 1, clicked at -528.0 -287.0'
]


start_data = [
'Testing 1, clicked at -278.0 152.0',
'Testing 1, clicked at -127.0 152.0',
'Testing 1, clicked at -122.0 113.0',
'Testing 1, clicked at -281.0 113.0'
]

screen.onscreenclick(click_mechanic)
setup()
turtle.mainloop()
