# MAFIA-game
Group Members:
Misbah Noor Awan
Alina Nasir
Mydah Nasir
Hafsa Imran

                                                                          Project Description

Storyline of Mafia Game:
The Mafia consists of two phases; the day and the night. 
A village of distressed civilians have their people killed every night by mysterious imposters among themselves. So, the village council decides that daily voting will be held through discussion of the civilians and every day 1 spectated mafia member will be hanged to death for the betterment of the village and its people.
During Day time, a gathering is held where people are suspected of their actions and are given some time to clear themselves off that blame, else they are hanged. During the Night time, THE MAFIA comes into actions and kills one innocent civilian.
The game ends in two ways:
The civilians win; They are successful in taking out the mafia members.
Mafia wins; This set of people kills civilians or has them voted out of false accusations until the number of civilians becomes less than the number of Mafia alive.

Our Project Idea:
Mafia is a multiplayer role play game that is usually played at sleepovers and over campfires. It usually consists of a large number of players with minimum 4 players.
In the original game, the number of players is divided into two or more categories, The uninformed innocents fearing for their lives and the informed evil spawns of Satan, THE MAFIA. Our group decided to make a computer version of this game that basically plays the role of the Narrator in the game.The Narrator in the real game has the tireless work of assigning rules to other players,explaining them the rules,giving them a storyline with the situation,recieving the count of votes from the players to reveal the person to be executed during daytime and secretly asking the Mafia members of who they want to kill during night time and then revealing this to other players. All of this hassle will now be done by our game providing each and every member to take part in this intriguing game.

Support:
The best part of this project/game is that its code is entirely made by our group members and we have not used any help from internet. There is no such code available by far and each step of the game is intricately designed by our own logic and knowledge.
                                                                       
                                                                       Features of the Game
Main Menu:
Allowing user to select options from one of the following:
1)Rules
2)Edit Discussion time
3)Start Game
Number of Player Selection:
It allows user to select the number of players that want to play the game from 4,6 or 8 players
Role Assignment:
The game then assign the role to each player yet assuring the complete confidentiality of the role assigned
 Voting System:
The game displays the options of all players to each player turn by turn. The options are displayed in form of radiobuttons and the data thereafter is compiled.For the civilians the game asks to vote for who they are suspicious of and for the Mafia the players the game asks them to select the player they are planning to kill tonight.
Result Display:
The game then reveals the person for which the majority had voted and also reveals whether the person was a civilian or Mafia memeber. After displaying the daytime result the game also reveals the civilian whom Mafia killed during the night time and that player is then consequently removed from game.
End Result:
The game continues to take votes from civilian and Mafia until the game ends in one of the two ways indicated above in the storyline.

                                                                        Technical Architecture:
The game Mafia is made using Tkinter module and Pygame module of Python. The game’s start screen has two options displayed:
1)	Menu
2)	Exit
Menu:
The menu module displays the following options to the user:
1)	Rules
2)	Edit discussion time
3)	Go back button
4)	Start
Rules:
This module allows the players to view the rules and regulations for the mafia game. The rules are written in the text file which is opened and the rules are displayed in the form of label to the user.
Edit discussion time:
This feature allows the users to change the discussion time for their village meeting in which they have to decide who they want to render guilty as Mafia member. The user enters the time they want to keep for discussion. The time entered by the user is saved to be used in the game and is also configured on the window for the user. If the user accidently enters a non-integer value a message is displayed to enter an integer number.
Go back button:
 This button appears in form of an arrow at the bottom left corner of the screen. It allows   the user to go back from the options displayed in the menu to the start screen. It also allows the user to go back from the ‘Rules’ and ‘Edit discussion time’ modules to the start screen.
Start:
This button allows users to start playing the game. It further gives the option to the user to select the number of players. The following options are given to the user:
1)	Four Players
2)	Six Players
3)	Eight Players
Once, the user has selected the number of players the game begins with displaying the ‘Start the Game’ option to the user.
Roles and Characters:
 When the user starts the game it allows all the players to view their roles and characters assigned to them. The ‘Next’ button which appears in form of an arrow allows user to end viewing so that game can be proceeded to the next player. After all the players have viewed their roles and characters the ‘FINISH’ button allows them to proceed to next part of the game. This part of the game is run on role display module in which two lists, one the list of roles that is Mafia and civilian is stored and the next list of characters contain roles such as housemaid, hair dresser etc. The roles and characters assigned to the users are then stored in form of a dictionary. 

Storyline:
The next part of the game consists of narrating the story that how the innocent civilians are killed and a need arises for figuring out the Mafia members. This part also contains a ‘Skip intro’ option in case the users already know the storyline and wish to proceed the game. This part of game is made using labels that are continuously configured on the screen after a fixed interval of time set in the program. At the end of the labels the players can proceed to the discussion time.
Discussion time:
The players are given a time in which they have to discuss their observations with each other. The ‘Start discussion’ option starts the timer. The time left is shown to the players on the screen at the interval of one second. As soon as the timer ends the user have to start the voting. This module is made using time module of Tkinter.
Voting:
This module allows civilians to vote out the members they are suspicious of and allows Mafia members to vote who they want to kill at the night. The options for voting are displayed in the form of radio buttons. The votes of the users are stored in a text file. From there, the results are calculated based on the majority of the votes. The results are displayed to the user in form of labels and also reveals the identity of the person voted out that whether it was a Mafia member or civilian. The module also displays whom the Mafia have killed at night.
End Game:
The game ends in two ways:
1)	The civilians become less than Mafia then the Mafia wins.
2)	 All the Mafia members are killed then the civilians win
The voting modules and discussion modules are run again and again until the results have been decided. When the game ends the user has the option to go back to the start screen again.

                                                                     Code Documentation
Pre-requisites for running the code:
1) Install pygame module in python since it is not inbuilt. This a very simple procedure simply go to command line and write pip install pygame. This will start installing      pygame provided that python is recognized on the command prompt of your computer.
2) Download all the files available in the source code and keep them in the same directory as that of where you want to run the main python program. Otherwise the program        will give error if all the files are not present in the same directory as that of the code.
3)The code also contains an executable file that would require a visual c++ redistributable for opening. The visual c++ redistributable can be downloaded using the link https://www.microsoft.com/en-pk/download/confirmation.aspx?id=48145
How to run the code:
Download the python file provided in the source code and open it with option edit with IDLE. Now press F5 to run the code. The game window will appear and the code will start to run.
                 



