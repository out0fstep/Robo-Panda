<div align="center">
🤖🐼 Robo-Panda v1.0  
-=⟦ Raspberry Pi–based Twitter bot using the Pimoroni Displayotron 3000 Pi Hat ⟧=-

-=[ **Created by** · [out0fstep](https://github.com/out0fstep) ]=-  

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://img.shields.io/github/downloads/out0fstep/Hack3r-T-Deck/total.svg?color=brightgreen)](https://github.com/out0fstep/Hack3r-T-Deck/releases)  
[![☕️ Buy Me a Coffee](https://img.shields.io/badge/%E2%98%95%EF%B8%8F-Buy%20Me%20a%20Coffee-yellow)](https://buymeacoffee.com/out0fstep)
[![Follow @DorkfeastTeam](https://img.shields.io/badge/follow-@DorkfeastTeam-1DA1F2?logo=x&logoColor=white)](https://x.com/DorkfeastTeam)

**Ḥą̥̥̍c̷̙̆k̘̝̰̭ T̻ȟ̔̓̀e̛̪̒̌ P̡̢̼̂l̟̑̀a̭n̨̹̖̆e̯̍ṯ̎̕!̶̐̒**

</div>  

---

## 🚀 Current Features
- ✅ Scans for new followers and follows them back  
- ✅ Detects unfollowers and unfollows them  
- ✅ Displays updated follower count  
- ✅ Tweets every 2 hours (line by line from `talk.txt`)  
- ✅ Lists and numbers tweets in the terminal  
- ✅ Works with both terminal & LCD for headless operation  

---

## 🐞 Known Bugs
- ❌ Script will **crash** when it runs out of lines in `talk.txt`  
- ❌ If restarted and a duplicate tweet is attempted, it will error  
  - **Workaround:** edit `talk.txt` so the next line is unique  

---

## 📦 Dependencies
- [Tweepy](https://www.tweepy.org/)  
- Pimoroni DOT3k libraries & dependencies  

---

## 🛠️ How to Use
1. Add your Twitter API keys in `keys.py`  
2. Edit `talk.txt` with the lines you want Robo-Panda to tweet  
3. Run the bot:  

   ```bash
   sudo python robopanda.py talk.txt
