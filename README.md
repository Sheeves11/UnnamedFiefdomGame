# UnnamedFiefdomGame

This is a little text based multiplayer game that can be hosted on a local Linux server and broadcast to your LAN
or the internet! The game takes influences from the BBS door games of the late 80s and early 90s, as well as
other text-based war games, like Kings of Chaos.

All you need to play is a browser! All you need to host the game is a basic Ubuntu Server installation.

Host your own server or play on our official website: http://unnamedfiefdomgame.com/

Please note that this game is in the super pre-alpha testing phase right now. More updates and features to 
come soon!

<p align="center">

<img width="748" alt="ufg" src="https://user-images.githubusercontent.com/3498355/149644850-ed561f5c-a28c-4687-80c7-1ffd46be5b91.png">

  
<img width="604" alt="Screenshot 2022-01-15 202147" src="https://user-images.githubusercontent.com/3498355/149644858-cf3adfe8-13b6-437e-b5ef-a0fa28ab5da9.png">

  
<img width="605" alt="Screenshot 2022-01-15 202211" src="https://user-images.githubusercontent.com/3498355/149644859-31fafd11-e42b-448d-9914-cb1d6753d713.png">


---------------------------------------------------------------------------------------------------------------

Intro:

Unnamed Fiefdome Game is a python programming project by Mike Quain (mquain@uark.edu) and Joshua Davis!

---------------------------------------------------------------------------------------------------------------

How to play:

Your goal is to control as many fiefdoms as you can manage without spreading your army too thin and leaving yourself open to attack!
Your home stronghold will never fall, but any conquered fiefdoms can be taken by opposing players. Make sure you can defend the
territory you claim!

Each claimed fiefdom will generate gold depending on the number of soldiers stationed there. That gold can be spent on defense and attack 
upgrades as well as additional soldiers.

Upgrade your conqured fiefdoms to keep them safe! Be careful though. Any upgraded fiefdom can still be taken, and 
your upgrades will transfer to the new ruler.

---------------------------------------------------------------------------------------------------------------

Hosting Server Installation Info:

I use a development server running Ubuntu Server 18.03 and Python 3.6. You will also need to install gotty and a GO development environment 
before running the game. You will also need the python package bcrypt for password encryption. Install it with the following command: (pip3 install py-bcrypt)

More information about goTTY can be had here: https://github.com/yudai/gotty




To run the game, first start up the backend with the following command:

python3 fiefdombackend.py &

Then, start the frontend and web server with this command:

gotty -w -p 80 python3 test.py

In your player's browser, connect using the server's IP address. For example:

http://10.4.40.15

(you may need to use tools like SCREEN to disown these processes if you are working via SSH sessions)

You will then need to seed some starting fiefdoms using the fieftool.py program.

-----------------------------------------------------------------------------------------------------------------

Enjoy!

-----------------------------------------------------------------------------------------------------------------

Update Log:

Since this game started, we've added almost 300 commits and 3k lines of code! Here are your latest updates:

1/2/2022:
Added password encryption using salted hashes
Added thieves for stealing from player Strongholds
Many, many bug fixes

(to be continued)
