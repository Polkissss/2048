# 2048 and brief description of project

My own personal version of a game called 2048. It's one of my fist projects so it might have a lot of bugs or any different issues.
Game is playable and even though it requires many QoL changes it is still kind of enjoyable. To play version with only terminal run "2048Terminal.py"
and to play version with GUI run "2048GUI.py"

## Rules

I think everyone knows how this game works but still I'm going to describe it.

Using wasd or arrow keys you control where to "shove" values in each of 4 directions. If a value for example 2 is shoved to the right
and meets another 2 they merge into 4 and stays on next position. At the beginning of a game two values are generated (either 2 or 4) and
placed on random empty tiles. On start of each turn one more value is generated on a random empty tile. If there are no empty tiles to
generate new value, player has lost and has to go to main menu. If player is able to reach a value set to limit the game (Default is 2048)
he won. Game is pretty simple yet challenging. 

### Requirements

Game doesn't require almost anything just python interpreter and downloaded readchar library. I will change it to executable file but as for now it stays this way.

#### Controlls

Values shoving: wasd or arrows
Exit mid game: Z
Navigating menu (Terminal): Menu tells you everything, but basically you type number (or word such as yes) corresponding to choice and press enter to confirm it