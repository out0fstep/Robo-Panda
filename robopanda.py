#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by out0fstep 2016

import tweepy, time, sys
from dot3k import joystick
from random import random
import dot3k.lcd as lcd
import dot3k.backlight as backlight
from keys import keys 
argfile = str(sys.argv[1])
 
#enter the corresponding information from your Twitter application:
SCREEN_NAME = keys['screen_name']
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token_key']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

###########################################################################

print('.')
print('''========================================================''')
print('''ooooooooo.              .o8                             ''')
print('''`888   `Y88.           "888                             ''')
print(''' 888   .d88'  .ooooo.   888oooo.   .ooooo.              ''')
print(''' 888ooo88P'  d88' `88b  d88' `88b d88' `88b             ''')
print(''' 888`88b.    888   888  888   888 888   888 8888888     ''')
print(''' 888  `88b.  888   888  888   888 888   888             ''')
print('''o888o  o888o `Y8bod8P'  `Y8bod8P' `Y8bod8P'             ''')
print('''ooooooooo.                               .o8            ''')
print('''`888   `Y88.                            "888            ''')
print(''' 888   .d88'  .oooo.   ooo. .oo.    .oooo888   .oooo.   ''')
print(''' 888ooo88P'  `P  )88b  `888P"Y88b  d88' `888  `P  )88b  ''')
print(''' 888          .oP"888   888   888  888   888   .oP"888  ''')
print(''' 888         d8(  888   888   888  888   888  d8(  888  ''')
print('''o888o        `Y888""8o o888o o888o `Y8bod88P" `Y888""8o ''')
print('''========================================================''')
print('''          -=[ Robo-Panda v1.0 by out0fstep ]=-          ''')

lcd.set_cursor_position(1, 0)
lcd.write('Robo-Panda 1.0    Created by       out0fstep')
time.sleep(3)

time.sleep(0.01)
print('.')
time.sleep(0.01)
print('.')
time.sleep(0.01)
print('.')
time.sleep(0.01)


############################################################################

#LED flash for headless display 

backlight.sweep(random())
time.sleep(0.01)
lcd.set_cursor_position(1, 0)
lcd.write(' Drink all the  booze Hack all   the things!')
time.sleep(3)

backlight.set_bar(0,255)
backlight.set_bar(0,0)
time.sleep(0.01)
backlight.set_bar(1,255)
backlight.set_bar(1,0)
time.sleep(0.01)
backlight.set_bar(2,255)
backlight.set_bar(2,0)
time.sleep(0.01)
backlight.set_bar(3,255)
backlight.set_bar(3,0)
time.sleep(0.01)
backlight.set_bar(4,255)
backlight.set_bar(4,0)
time.sleep(0.01)
backlight.set_bar(5,255)
backlight.set_bar(5,0)
time.sleep(0.01)
backlight.set_bar(6,255)
backlight.set_bar(6,0)
time.sleep(0.01)
backlight.set_bar(7,255)
backlight.set_bar(7,0)
time.sleep(0.01)
backlight.set_bar(8,255)
backlight.set_bar(8,0)
time.sleep(0.01)
backlight.set_bar(7,255)
backlight.set_bar(7,0)
time.sleep(0.01)
backlight.set_bar(6,255)
backlight.set_bar(6,0)
time.sleep(0.01)
backlight.set_bar(5,255)
backlight.set_bar(5,0)
time.sleep(0.01)
backlight.set_bar(4,255)
backlight.set_bar(4,0)
time.sleep(0.01)
backlight.set_bar(3,255)
backlight.set_bar(3,0)
time.sleep(0.01)
backlight.set_bar(2,255)
backlight.set_bar(2,0)
time.sleep(0.01)
backlight.set_bar(1,255)
backlight.set_bar(1,0)
time.sleep(0.01)
backlight.set_bar(0,255)
backlight.set_bar(0,0)
time.sleep(0.01)
backlight.set_bar(1,255)
backlight.set_bar(1,0)
time.sleep(0.01)
backlight.set_bar(2,255)
backlight.set_bar(2,0)
time.sleep(0.01)
backlight.set_bar(3,255)
backlight.set_bar(3,0)
time.sleep(0.01)
backlight.set_bar(4,255)
backlight.set_bar(4,0)
time.sleep(0.01)
backlight.set_bar(5,255)
backlight.set_bar(5,0)
time.sleep(0.01)
backlight.set_bar(6,255)
backlight.set_bar(6,0)
time.sleep(0.01)
backlight.set_bar(7,255)
backlight.set_bar(7,0)
time.sleep(0.01)
backlight.set_bar(8,255)
backlight.set_bar(8,0)
time.sleep(0.01)
backlight.set_bar(7,255)
backlight.set_bar(7,0)
time.sleep(0.01)
backlight.set_bar(6,255)
backlight.set_bar(6,0)
time.sleep(0.01)
backlight.set_bar(5,255)
backlight.set_bar(5,0)
time.sleep(0.01)
backlight.set_bar(4,255)
backlight.set_bar(4,0)
time.sleep(0.01)
backlight.set_bar(3,255)
backlight.set_bar(3,0)
time.sleep(0.01)
backlight.set_bar(2,255)
backlight.set_bar(2,0)
time.sleep(0.01)
backlight.set_bar(1,255)
backlight.set_bar(1,0)
time.sleep(0.01)

lcd.set_cursor_position(1, 0)
lcd.clear()

print('Bot is running!')
lcd.set_cursor_position(1, 0)
lcd.write('  The bot is       running!')
time.sleep(3)

backlight.sweep(random())
print('Starting follow/unfollow session')
lcd.set_cursor_position(1, 0)
lcd.write('Starting followunfollow session Please wait...')
time.sleep(3)

#followback followers
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()

backlight.sweep(random())
lcd.clear()
print('Follow back scan complete!')
lcd.set_cursor_position(1, 0)
lcd.write('Follow back    scan completed!')
time.sleep(3)

backlight.sweep(random())
print('Deleting unfollowers!')
lcd.set_cursor_position(1, 0)
lcd.write('Deleting        unfollowers....')
time.sleep(3)

#unfollowing unfollowers
followers = api.followers_ids(SCREEN_NAME)
friends = api.friends_ids(SCREEN_NAME)
 
for f in friends:
    if f not in followers:
        print "Unfollow {0}?".format(api.get_user(f).screen_name)
        if raw_input("Y/N?") == 'y' or 'Y':
            api.destroy_friendship(f)

backlight.sweep(random())
print('Unfollowers deleted - get rekt!')
lcd.set_cursor_position(1, 0)
lcd.write('Unfollowers     deleted...      Get Rekt!')
time.sleep(3)


#Find out how many followers you have
def follower_count():
    followers = api.followers_ids()

    return len(followers)

def main():
    followers = follower_count()
    
    backlight.sweep(random())
    print("You have %-6i followers now!" % followers)
    lcd.set_cursor_position(1, 0)
    lcd.clear()
    lcd.write("You have %-6i followers now!" % followers)
    time.sleep(3)

if __name__ == '__main__':
    main()

lcd.set_cursor_position(1, 0)
lcd.clear()

##############################################################################

#open talk file and tweet loop
lcd.set_cursor_position(1, 0)
lcd.clear()
time.sleep(0.05)
print('Activating tweet mode!')
lcd.set_cursor_position(1, 0)
lcd.write(' Activating       tweet mode!')
time.sleep(3) 


def read_file(argfile):
    with open(argfile, 'r') as f:
        lines = f.readlines()
        return len(lines), lines
    
total_lines, lines = read_file(argfile)
line_num = 0
while True:
    api.update_status(status=lines[line_num])
    
    backlight.sweep(random())
    print('Just tweeted {}: {}'.format(line_num, lines[line_num]))
    lcd.set_cursor_position(3, 2)
    lcd.clear()
    time.sleep(0.05)
    lcd.write('Just tweeted!')
    
    backlight.set_bar(0,255)
    backlight.set_bar(0,0)
    time.sleep(0.01)
    backlight.set_bar(1,255)
    backlight.set_bar(1,0)
    time.sleep(0.01)
    backlight.set_bar(2,255)
    backlight.set_bar(2,0)
    time.sleep(0.01)
    backlight.set_bar(3,255)
    backlight.set_bar(3,0)
    time.sleep(0.01)
    backlight.set_bar(4,255)
    backlight.set_bar(4,0)
    time.sleep(0.01)
    backlight.set_bar(5,255)
    backlight.set_bar(5,0)
    time.sleep(0.01)
    backlight.set_bar(6,255)
    backlight.set_bar(6,0)
    time.sleep(0.01)
    backlight.set_bar(7,255)
    backlight.set_bar(7,0)
    time.sleep(0.01)
    backlight.set_bar(8,255)
    backlight.set_bar(8,0)
    time.sleep(0.01)
    backlight.set_bar(7,255)
    backlight.set_bar(7,0)
    time.sleep(0.01)
    backlight.set_bar(6,255)
    backlight.set_bar(6,0)
    time.sleep(0.01)
    backlight.set_bar(5,255)
    backlight.set_bar(5,0)
    time.sleep(0.01)
    backlight.set_bar(4,255)
    backlight.set_bar(4,0)
    time.sleep(0.01)
    backlight.set_bar(3,255)
    backlight.set_bar(3,0)
    time.sleep(0.01)
    backlight.set_bar(2,255)
    backlight.set_bar(2,0)
    time.sleep(0.01)
    backlight.set_bar(1,255)
    backlight.set_bar(1,0)
    time.sleep(0.01)
    backlight.set_bar(0,255)
    backlight.set_bar(0,0)
    time.sleep(0.01)
    backlight.set_bar(1,255)
    backlight.set_bar(1,0)
    time.sleep(0.01)
    backlight.set_bar(2,255)
    backlight.set_bar(2,0)
    time.sleep(0.01)
    backlight.set_bar(3,255)
    backlight.set_bar(3,0)
    time.sleep(0.01)
    backlight.set_bar(4,255)
    backlight.set_bar(4,0)
    time.sleep(0.01)
    backlight.set_bar(5,255)
    backlight.set_bar(5,0)
    time.sleep(0.01)
    backlight.set_bar(6,255)
    backlight.set_bar(6,0)
    time.sleep(0.01)
    backlight.set_bar(7,255)
    backlight.set_bar(7,0)
    time.sleep(0.01)
    backlight.set_bar(8,255)
    backlight.set_bar(8,0)
    time.sleep(0.01)
    backlight.set_bar(7,255)
    backlight.set_bar(7,0)
    time.sleep(0.01)
    backlight.set_bar(6,255)
    backlight.set_bar(6,0)
    time.sleep(0.01)
    backlight.set_bar(5,255)
    backlight.set_bar(5,0)
    time.sleep(0.01)
    backlight.set_bar(4,255)
    backlight.set_bar(4,0)
    time.sleep(0.01)
    backlight.set_bar(3,255)
    backlight.set_bar(3,0)
    time.sleep(0.01)
    backlight.set_bar(2,255)
    backlight.set_bar(2,0)
    time.sleep(0.01)
    backlight.set_bar(1,255)
    backlight.set_bar(1,0)
    time.sleep(1)
    lcd.clear()    
    lcd.set_cursor_position(1, 0)
    lcd.write('Robo-Panda 1.0    Created by       out0fstep')
    time.sleep(7200) 
    backlight.sweep(random())
    line_num += 1
    
    if line_num == total_lines:
        total_lines, lines = read_file(argfile)
        line_num = 0
        
     


