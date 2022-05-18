# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT  / 2]
ball_vel = [6,0]
time = 0
score1 = 0
score2 = 0
paddles2_vel = 0
paddles1_vel = 0
re_start = [WIDTH / 2, HEIGHT  / 2]
paddle2_pos = HEIGHT / 2
paddle1_pos = HEIGHT / 2

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left

def spawn_ball(direction):
    global ball_pos, ball_vel, re_start # these are vectors stored as lists
    
    # THI CODE IS TO PUT THE BALL BACK TO THE MIDDLE
    ball_pos[0] = WIDTH /2 
    ball_pos[1] = HEIGHT / 2
    
    #adding random to the start
    x = random.randrange(1, 6) #pixels 
    y = random.randrange(-6, 6)
    
    if direction == "LEFT":
        x = -x
        ball_vel = [x,y]
        
        
    elif direction == "RIGHT":
        ball_vel = [x,y]    
        
    # define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel # these are numbers
    global score1, score2  # these are ints 
    rand = random.randrange(0,2)
    print rand
    if rand == 0:
        spawn_ball("LEFT")
        
    else: 
        spawn_ball("RIGHT")
  
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddles1_vel, paddles2_vel
  
   # draw mid line and gutters (TABLE)
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White") # middle line
    L = canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")  # left line
    R = canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White") # rigth line
    
   # update ball
   
    global ball_pos, ball_vel
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
  
    #bottom wall 
    
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
        
    #uper wall
    
    if ball_pos[1] <= 0 + BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
        
  
    #left wall 
    
    if ball_pos[0] <= BALL_RADIUS:
        if ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT - BALL_RADIUS and ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT - BALL_RADIUS:
            ball_vel[0] = - ball_vel[0]
            print "yes!!!"
        else:
            new_game()
            print "no!!!!"
   
     #right wall
    
    if ball_pos[0] >= WIDTH - BALL_RADIUS:
        #new_game()
        #if ball_pos[0] >= paddle2_pos and ball_pos[1] <= paddle2_pos:
        ball_vel[0] = - ball_vel[0]
        #    print "hit paddle"
        #else:
        #    new_game()
 
   #keep paddle on the screen
            
    if paddle2_pos >= HALF_PAD_HEIGHT:
        if paddle2_pos + paddles2_vel <= HALF_PAD_HEIGHT:
            paddle2_pos = HALF_PAD_HEIGHT
        else:
            if paddle2_pos + HALF_PAD_HEIGHT + paddles2_vel <= HEIGHT:
                paddle2_pos += paddles2_vel
            

            
    if paddle1_pos >= HALF_PAD_HEIGHT:
        if paddle1_pos + paddles1_vel <= HALF_PAD_HEIGHT:
            paddle1_pos = HALF_PAD_HEIGHT
        else:    
            if paddle1_pos + HALF_PAD_HEIGHT + paddles1_vel <= HEIGHT:
                paddle1_pos += paddles1_vel
             
            
   # draw ball
    canvas.draw_circle((ball_pos), BALL_RADIUS, 2, 'RED', 'White')

   # draw paddles
    
   # paddle1 left
    canvas.draw_line((HALF_PAD_WIDTH,paddle1_pos-HALF_PAD_HEIGHT),(HALF_PAD_WIDTH,paddle1_pos+HALF_PAD_HEIGHT), PAD_WIDTH, "White")  
    
   # paddle2 right
    canvas.draw_line((WIDTH-HALF_PAD_WIDTH,paddle2_pos-HALF_PAD_HEIGHT),(WIDTH-HALF_PAD_WIDTH,paddle2_pos+HALF_PAD_HEIGHT),PAD_WIDTH,"White")
                    
   # determine whether paddle and ball collide    
    
   # draw scores
    canvas.draw_text(str(score2), (140, 100), 50, 'blue') #left
    canvas.draw_text(str(score1), (425, 100), 50, 'red')  #right
        
    
def keydown(key):
    global paddle1_pos, paddle2_pos, paddles1_vel, paddles2_vel
    
    # update paddle's_vel
    if key == simplegui.KEY_MAP["down"]:
        paddles2_vel = 5           
        
    elif key == simplegui.KEY_MAP["up"]:
        paddles2_vel =  -5
            
    elif key == simplegui.KEY_MAP["w"]:
        paddles1_vel = -5
            
    elif key == simplegui.KEY_MAP["s"]:
        paddles1_vel = 5
            
def keyup(key):
    global paddles1_vel, paddles2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddles1_vel = 0
            
    elif key == simplegui.KEY_MAP["s"]:
        paddles1_vel = 0
        
    elif key == simplegui.KEY_MAP["up"]:
        paddles2_vel = 0
        
    elif key == simplegui.KEY_MAP["down"]:
        paddles2_vel = 0
    
 #score ######################
 
def poits():
    global paddle1_pos, paddle2_pos,  paddle1_vel,  paddle2_vel, score1, score2
       
# Restart button
def restart():
    new_game()
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button('new game', restart)
# start frame'
new_game()
frame.start()