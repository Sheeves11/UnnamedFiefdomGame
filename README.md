# UnnamedFiefdomGame

This is a little text based multiplayer game that can be hosted on a local Linux server and broadcast to your LAN
or the internet! The game takes influences from the BBC door games of the late 80s and early 90s, as well as
other text-based war games, like Kings of Chaos.

All you need to play is a browser! All you need to host the game is a basic Ubuntu Server installation.


![snip](https://user-images.githubusercontent.com/3498355/144886504-573dd8b0-dde5-489b-a229-36c5d0cf5ee2.PNG)

---------------------------------------------------------------------------------------------------------------

Intro:

Unnamed Fiefdome Game is a python programming project by Mike Quain (mquain@uark.edu)
The goal was to take on a project that was big enough to be challenging, but small enough to stay interesting.
This game looks simple, but it taught me the basics of reading and writing to a database, data persistance, and multi-user tools.

---------------------------------------------------------------------------------------------------------------

How to play:

Your goal is to control as many fiefdoms as you can manage without spreading your army too thin and leaving yourself open to attack!
Your home stronghold will never fall, but any conquered fiefdoms can be taken by opposing players. Make sure you can defend the
territory you claim!

Your Fiefdom consists of soldiers and workers. The workers earn income and the soldiers both fight and defend your fiefdoms.
Each worker produces 1 coin per hour. These coins will be used to purchace various upgrades and to recruit new fighters.

---------------------------------------------------------------------------------------------------------------

Hosting Server Installation Info:

I use a development server running Ubuntu Server 18.03 and Python 3.6. You will also need to install gotty and a GO development environment 
before running the game.

More information about goTTY can be had here: https://github.com/yudai/gotty


Start the game using the following command:

"gotty -w python3 test.py"

In your player's browser, connect using the server's IP address and the default port 8080. For example:

http://10.4.40.15:8080

-----------------------------------------------------------------------------------------------------------------

Enjoy! (More details coming soon!)
