# UnnamedFiefdomGame

This is a text based multiplayer game that can be hosted on a local Linux server and broadcast to your LAN
or the internet! The game takes influences from the BBS door games of the late 80s and early 90s, as well as
other text-based war games, like Kings of Chaos. It is deceptively deep and a ton of fun to play with friends
or over the internet.

All you need to play is a browser! All you need to host the game is a basic Ubuntu Server installation
and a few libraries.

Host your own server or play on our official website: http://unnamedfiefdomgame.com/

If you would like to play on our development server, visit http://216.128.140.232/

Please note that this game is in the super pre-alpha testing phase right now. More updates and features to 
come soon!

If you'd like to talk to us or get real-time updates on our progress, check out our Discord! https://discord.gg/FVvMCfZ3fq

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

Each claimed fiefdom will generate gold and other resources depending on the number of soldiers stationed there. That gold can be spent 
on defense and attack upgrades as well as additional soldiers. You can also add resource outposts to your fiefdoms, which will bring
in resources that you can use with various upgrades.

Upgrade your conqured fiefdoms to keep them safe! Be careful though. Any upgraded fiefdom can be taken, and your upgrades will transfer 
to the new ruler.

---------------------------------------------------------------------------------------------------------------

Hosting Server Installation Info:

I use a development server running Ubuntu Server 18.03 and Python 3.6. You will also need to install gotty and a GO development environment 
before running the game. I've laid out some instructions below that should help you set this up on a fresh server.


To run the game, first start up the backend with the following command:

python3 fiefdombackend.py &

Then, start the frontend and web server with this command:

gotty -w -p 80 python3 test.py

In your player's browser, connect using the server's IP address. For example:

http://10.4.40.15

(you may need to use tools like SCREEN to disown these processes if you are working via SSH sessions)

You will then need to seed some starting fiefdoms using the fieftool.py program.
  
  
Installation Steps:
  
0. Do a fresh install of Ubuntu LTS 18.03 or 20.03
  
1. Install Git

  ```sudo apt-get install git-core git-gui git-doc```
  
2. Clone Our Repository
  
  ```git clone https://github.com/Sheeves11/UnnamedFiefdomGame```
  
3. Install pip3
  
  ```apt install python3-pip```
  
4. Install the bcrypt library (for our password hashing)
  
  ```pip3 install py-bcrypt```
  
5. Install a GO development environment
  
  ```apt-get golang```
  
5. Install goTTY
  
  ```go get github.com/yudai/gotty```
  More information about goTTY can be had here: https://github.com/yudai/gotty
  
6. run fiefdombackeng.py
  
  ```scrren -d -m python3 fiefdombackend.py &```
  
7. run the goTTY host
  ```screen -d -m go/bin/gotty -w -p 80 python3 fiefdomgame.py```
  
8. Connect via browser using your server's IP address!
  
-----------------------------------------------------------------------------------------------------------------

Enjoy!

-----------------------------------------------------------------------------------------------------------------
