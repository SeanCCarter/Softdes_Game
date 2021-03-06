				   ___  ___ _____ _  _  ___   ___  ___  _  _   _   _    
				  / _ \| _ \_   _| || |/ _ \ / __|/ _ \| \| | /_\ | |   
				 | (_) |   / | | | __ | (_) | (_ | (_) | .` |/ _ \| |__ 
				  \___/|_|_\ |_| |_||_|\___/ \___|\___/|_|\_/_/ \_\____|
						  _____ ___ ___ ___    _   ___ ___   _   
						 |_   _| __| _ \ _ \  /_\ | _ \_ _| /_\  
						   | | | _||   /   / / _ \|   /| | / _ \ 
						   |_| |___|_|_\_|_\/_/ \_\_|_\___/_/ \_\

										also known as:

  ___    ___   ___    ___    ___   ___   ___   _____     _     _____   ___    ___    _  _ 
 |   \  | __| | __|  / _ \  | _ \ | __| / __| |_   _|   /_\   |_   _| |_ _|  / _ \  | \| |
 | |) | | _|  | _|  | (_) | |   / | _|  \__ \   | |    / _ \    | |    | |  | (_) | | .` |
 |___/  |___| |_|    \___/  |_|_\ |___| |___/   |_|   /_/ \_\   |_|   |___|  \___/  |_|\_|
                __   ___   __  __   _   _   _        _     _____    ___    ___            
              / __| |_ _| |  \/  | | | | | | |      /_\   |_   _|  / _ \  | _ \           
              \__ \  | |  | |\/| | | |_| | | |__   / _ \    | |   | (_) | |   /           
              |___/ |___| |_|  |_|  \___/  |____| /_/ \_\   |_|    \___/  |_|_\     

              		 __      __   							 _____
				 	|  \    /  |  							|  __ \
				 	|   \  /   |  							| |__\ \
				 	|    \/    |  	   an interactive		|   ___/
				 	|  |\  /|  |  		 program by			|     \
				 	|  | \/ |  |  							|  |\  \
				 	|__|    |__|  							|__| \__\           
								  _____     	   ____
								 /     \		  /    \
								|   |   |		 /      |
								|	|___/		|   |  /
								 \ __   \		|   |--
								 /  |   |		|	|  \
								|   |   |		 \      |
								 \_____/ 		  \____/      
                                                                                          

"Amazing!" - Matt
"Hard-hitting social commentary!" - Matt
"Game of the century!" - Also Matt
"10/10" - IGN*
"Definitely not just top-down Minecraft!" - Anonymous (but probably Matt)
---------------------------------------------------------------------------------------------

Project Overview:
	For our project, we created a top-down version of Minecraft/Terraria (albeit with substantially limited features, when compared to those of the actual games themselves). This game creates a procedurally generated world, in which the player may move - walking around, harvesting blocks and (re-)placing them elsewhere.
	This version of the game differs in several point from the in-class demo, which was the last commit. This one has an inventory.

	Please note: game_drafting.py does NOT code for the current game. It was our prototype, so that you can examine the development of the game. The game itself is encoded in the following files:
		Orthogonal_Terraria.py
		Controller_Module.py
		World_Module.py
		Block_Module.py
		Player_Module.py
		Misc_Module.py
	Testing of various functions occured throughout development, and many of the tests we did are located in files with 'testing' in the name.


Required Python Modules:
	Pygame


To play:
	If there is not folder called 'chunks' downloaded, create it. (It should be there, though)
	Run Orthogonal_Terraria.py
	If you want to generate a new world, set loadworld to 'False' in the main section of the code. To load your previous world, don't forget to set it to true!


Controls:
	- The up and down arrow keys move your player forwards and backwards (in the direction that your character is facing), while the left and right arrow keys  rotate the player clockwise and counterclockwise
	- Space is the mine button (it eliminates everything but dirt) and left-shift is the button to place items. You can only place as many items as you have mined.
	- 'A' and 'D' move your selection in the inventory forwards and backwards (see the purple bar in the top left corner)
------------------------------------------------------------------------------

*just not about this game.
	