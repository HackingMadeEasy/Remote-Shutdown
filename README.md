# Remote-Shutdown
Remote Shutdown any pc

**---------------SETUP INSTRUCTIONS---------------**\
**1.** Download target.py and client.py to your downloads folder.\
**2.** Open target.py and change the password to whatever you want and close the file (save it).\
**3.** Open client.py (this is what shuts down the other pc) and change the password to the same thing you put in target.py\
**4.** Now you need to get the **IPv4 (private ip)** of the target, this can be received from opening **CMD** and typing *ipconfig*, look for a line that says **IPv4 Address. . . . . . . . . . . : 12.345.678.90** (those are fake numbers not my real ip).\
**5.** Copy the 10 digit IPv4 and paste it into the client.py line that says *SERVER_IP* (should be towards the top of the code).\
Now you are all setup.\
\
If you want to make this an **exe file** then:\
**1.** Make sure you have pyinstaller installed on your pc.\
Pyinstaller download tutorial I **found**: https://www.youtube.com/watch?v=DP5aRpMNJG8 \
**2.** Open CMD and type *cd downloads* and press enter.\
**!IMPORTANT. MAKE SURE YOU SAVED THE client.py AND target.py TO YOUR DOWNLOADS FOLDER**\
**3.** Then type *pyinstaller target.py --onefile --noconsole --noupx*\
**WAIT ABOUT 1 MINUTE**\
**4.** Do the same thing again but replace *target.py* with *client.py*.\
**WAIT ABOUT 1 MINUTE**\
**5.** In your *Downloads* Folder look for a folder named **Dist**.\
**6.** Open **Dist** and if you followed all the steps **Corectly** then you should see *client.exe* and *target.exe*.\
**Now all you need to do is get the target.exe to run on another pc**\
*Once target.exe is running on the pc you want to turn off (can be your own) you can now run the client.exe on the pc you want to use to shutdown the target pc.*\
\
**---------------------------------------------------------------------------------------------------------------------------------**
**THIS IS FOR EDUCATIONAL PURPOSES ONLY AND IN NO WAY DO I ENDORSE HACKING OTHERS OR SENDING MALICOUS FILES TO OTHERS WITHOUT THEIR CONSENT** \
\
Everything here was coded by CrystalPT\
Link To Main Github: https://github.com/CrystalPT \
Link To Discord: https://discord.gg/6PEhT4u8WD
