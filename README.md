# UnnamedFiefdomGame

This is a little text based multiplayer game that can be hosted on a local Linux server and broadcast to your LAN
or the internet! The game takes influences from the BBC door games of the late 80s and early 90s, as well as
other text-based war games, like Kings of Chaos.

All you need to play is a browser! All you need to host the game is a basic Ubuntu Server installation.

Host your own server or play on our official website: http://unnamedfiefdomgame.com/

Please note that this game is in the super pre-alpha testing phase right now. More updates and features to 
come soon!


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

Each claimed fiefdom will generate 100 gold per hour. That gold can be spent on defense and attack upgrades as well as
additional soldiers.

Upgrade your conqured fiefdoms to keep them safe! Be careful though. Any upgraded fiefdom can still be taken, and 
your upgrades will transfer to the new ruler.

---------------------------------------------------------------------------------------------------------------

Hosting Server Installation Info:

I use a development server running Ubuntu Server 18.03 and Python 3.6. You will also need to install gotty and a GO development environment 
before running the game.

More information about goTTY can be had here: https://github.com/yudai/gotty




To run the game, first start up the backend with the following command:

python3 fiefdombackend.py &

Then, start the frontend and web server with this command:

gotty -w -p 80 python3 test.py

In your player's browser, connect using the server's IP address. For example:

http://10.4.40.15

-----------------------------------------------------------------------------------------------------------------

Enjoy! (More details coming soon!)
