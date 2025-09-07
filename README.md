# Robo-Panda v1.0
<p align="center">
-=⟦ Rasberry Pi based Twitter bot that utilizes the Pimoroni Displayotron 3000 Pi Hat ⟧=-
</p>

-=[ **Created by** · [out0fstep](https://github.com/out0fstep) ]=-  

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://img.shields.io/github/downloads/out0fstep/Hack3r-T-Deck/total.svg?color=brightgreen)](https://github.com/out0fstep/Hack3r-T-Deck/releases)  
[![☕️ Buy Me a Coffee](https://img.shields.io/badge/%E2%98%95%EF%B8%8F-Buy%20Me%20a%20Coffee-yellow)](https://buymeacoffee.com/out0fstep)
[![Follow @DorkfeastTeam](https://img.shields.io/badge/follow-@DorkfeastTeam-1DA1F2?logo=x&logoColor=white)](https://x.com/DorkfeastTeam)

**Ḥą̥̥̍c̷̙̆k̘̝̰̭ T̻ȟ̔̓̀e̛̪̒̌ P̡̢̼̂l̟̑̀a̭n̨̹̖̆e̯̍ṯ̎̕!̶̐̒**

</div>
 
----------------------------------------------------------------------------------
**Current features:**
- Scans for new followers and follows them back.
- Checks for any unfollowers and unfollows them. 
- Displays updated follower count.
- Tweets every 2 hours line by line from txt file.
- Lists and numbers the tweets in terminal.
- Teminal display and LCD display for headless operation.

---------------------------------------------------------------------------------

Known bugs:
- When the script runs out of things to say in the list it will crash.
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



