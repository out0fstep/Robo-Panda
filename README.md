# Robo-Panda v1.0
by out0fstep
Rasberry Pi based Twitter bot that utilizes the Pimoroni Displayotron 3000 Pi Hat 
----------------------------------------------------------------------------------
Current features:
- Scans for new followers and follows them back.
- Checks for any unfollowers and unfollows them. 
- Displays updated follower count.
- Tweets every 2 hours line by line from txt file.
- Lists and numbers the tweets in terminal.
- Teminal display and LCD display for headless operation.

Upcoming features?:
- Joystick functions - perhaps a full menu of options?
- Sweeping background animations both colors and characters?
- Display and @mentions to the bot on the LCD screen with automated replies?
- more cool stuff!? 
---------------------------------------------------------------------------------

Known bugs:
- When the scripyt runs out of things to say in the list it will crash.
- If you start and stop the script so it tried to post a dupe tweet, it will error. 
  (just alter the talk.txt so the next line is not a repeated tweet for workaround.) 

--------------------------------------------------------------------------------------
Dependancies:
- Tweepy
- All the DOT3k required dependancies 

-----------------------------------------------------------------------------------------
How to use:

1. Just put you twitter keys in keys.py
2. Add/edit talk.txt with what you want it to say
3. Run: sudo python robopanda.py talk.txt

----------------------------------------------------------------------------------------
You can find me on twitter @dorkfeastteam 
** This is still a project in the works!!**
** Please excuse my horrible scripting, i'm new at this... lol ** 



