# MegaTraveller_Trade_Commerce.py
Automating Trade and Commerce for the MegaTraveller game

I am a massive gamer nerd.  I've been playing games my entire life, and one of my favorites has been MegaTraveller,
a science fiction roleplaying game I played in high school.  

MegaTraveller is a science fiction role-play game that uses a lot of charts and randomness to execute gameplay
functions.  I've always been interested in the economic concept of the game, having been influenced heavily by C.J. 
Cherryh's Merchanter's Luck book.  MegaTraveller has a LOT of charts and random dice rolls.  I'd always wanted to 
automate the Trade and Commerce section, create an in-game ship and crew, and solo play trade and commerce to see
if I could keep afloat.

One of the problems with the charts is that they are not uniform, so many boolean checks are required to determine
correct output.

A few weeks into semester and I am now dangerous, in that I know a few things but I don't know how to do them
efficiently!  Basically I know print(), input(), if...else, and how to copy things from Google searches.  This
current version is very much akin to a BASIC program, but I'm looking at a few things and I think there are
ways to define functions and such we will get into later that would clean up my if...else monoliths.

Step One is to get everything working right at the most basic level.  Input is not being error-checked, etc.

Step Two is to change information input to entering full Universal World Profiles, to include using hex values.
I'm pretty sure how to do the input for the UWPs (example below) and how to step through the string to get 
specific values as I did this in BASIC, but I don't know how to turn the alphanumeric codes into their hexidecimal
values.  I may just convert them to integers and use if...else to convert to aphanumerics.
This will probably include refactoring the software with new data structures later on.

UWP:  Roup 0407 C77A9A9-6 S Hi In Wa A323 Im

Step Three would be to have a graphic user interface, sector map data, etc.  I don't know if we will get to this
during the current semester, but I think it may.
