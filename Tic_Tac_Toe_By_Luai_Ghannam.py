#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
                   \____    /____  __ __  ______    \_____  \_/ ____\     |    |__ __|__| ____  ____  
                     /     // __ \|  |  \/  ___/     /   |   \   __\      |    |  |  \  |/ ___\/ __ \ 
                    /     /\  ___/|  |  /\___ \     /    |    \  |    /\__|    |  |  /  \  \__\  ___/ 
                   /_______ \___  >____//____  >____\_______  /__|____\________|____/|__|\___  >___  >
                          \/   \/           \/_____/       \/  /_____/                      \/    \/ 
                            __________                                      __                        
                           \______   \_______   ____   ______ ____   _____/  |_  ______              
                             |     ___/\_  __ \_/ __ \ /  ___// __ \ /    \   __\/  ___/              
                             |    |     |  | \/\  ___/ \___ \\  ___/|   |  \  |  \___ \               
                             |____|     |__|    \___  >____  >\___  >___|  /__| /____  >              
                                                    \/     \/     \/     \/          \/    
                                                    
                                                    
                                                    
                       \__    ___/|__| ____   \__    ___/____    ____   \__    ___/___   ____  
                         |    |   |  |/ ___\    |    |  \__  \ _/ ___\    |    | /  _ \_/ __ \ 
                         |    |   |  \  \___    |    |   / __ \\  \___    |    |(  <_> )  ___/ 
                         |____|   |__|\___  >   |____|  (____  /\___  >   |____| \____/ \___  >
                                          \/                 \/     \/                      \/ 
'''  
from IPython.display import clear_output # Used to clear the output of each player input.
from random import randint               # Used to simulate the roll of a 60-face dice to choose who begins frst
import time
#-------------------------------------------------------------------------------------------------------------------#
''' playerX (X= 1 or 2) contains the following:
-'name': holds player name.

-'sprite': whether X or O.

-'sprite weight': used to check for winning condition. X has a weight of 10, O had a weight of 1.
the big difference of weights just to make sure no mixing up. for example if one player has three
X's in a row the score for that player of that paticular row = 30 (winning condition is reached). 
But if one of them is O, then the row score for player holding X = 20 (winning condition is not reached)
and row score for the other player holding O = 1 (winning condition is not reached).

-'winner': holds the boolean condition if a player is a winner or not.

-'wins': holds the number of wins.

-'rowX score' & 'columnX score' & 'diagonalX score': each player has its own copy of row, column, and diagonal scores.
Those will be used to check for winning condition.
''' 
player1 = {'name':'', 'sprite':' ', 'sprite weight':0, 'winner': False, 'wins':0, 'row0 score':0, 
               'row1 score':0, 'row2 score':0, 'column0 score':0,'column1 score':0, 
               'column2 score':0,'diagonal1 score':0, 'diagonal2 score':0}
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
player2 = {'name':'', 'sprite':' ',  'sprite weight':0,'winner': False,'wins':0, 'row0 score':0,
               'row1 score':0, 'row2 score':0, 'column0 score':0,'column1 score':0, 
               'column2 score':0,'diagonal1 score':0, 'diagonal2 score':0}
#-------------------------------------------------------------------------------------------------------------------#
''' game_placement holds the shape of tic tac toe game in the form of list of lists containing vacant location,
   X's and O's.
''' 
game_placement = [['1','2','3'],['4','5','6'],['7','8','9']]
#-----------------------------------------check_for_winner---------------------------------------------------------#
'''                          is called per player in the main body of the code.
   Input: 
        -a copy of playerX.
   Output:
         -boolean value to indicate for a winning condition
   notes: 
        each player has it own winning condition:
                                                   player holding X, the winning condition = 30
                                                   player holding 0, the winning condition = 3
       X|2|3
       -----
       4|X|6  In this example, diagonal! score will = 30 then a winning condition is reached and 
       -----  the player holding X sprite has won the game.
       7|8|X
   check_for_winner is called per player in the main body of the code.
''' 
def check_for_winner(player):
   for i in range(3):
       if player['row{} score'.format(i)] == (3 * player['sprite weight']):
           return True
   for i in range(3):
       if player['column{} score'.format(i)] == (3 * player['sprite weight']):
           return True
   for i in range(1,3):
       if player['diagonal{} score'.format(i)] == (3 * player['sprite weight']):
           return True
   return False    
#--------------------------------------------------reset_scores------------------------------------------------------#
'''                                 is called within "score_claculator" function.

   Input: 
        -a copy of playerX, size = the length of one side of tic tac toe game = 3
   Output: 
         -a copy of playerX with reseted scores back to zero.
   notes:
        This is done to prevent miscalculations which will give a false winning condition.
   but what will happen if we didn't use this function:
   
       X|2|3                              X|2|3
       -----                              -----
       4|5|6  here, diagonal score = 10,  4|X|6 now diagonal score = old diagonal score(10) + new diagonal score(20) = 30 
       -----                              ----- a false winning condition.
       7|8|9                              7|8|9
       
   By using this function:
   
       X|2|3                              X|2|3
       -----                              -----
       4|5|6  here, diagonal score = 10,  4|X|6 now diagonal score = old diagonal score(0) + new diagonal score(20) = 0 
       -----                              ----- still not enough to win.
       7|8|9                              7|8|9
''' 
def reset_scores(player,size):
   for i in range(size):
       for j in range(size):
               player['row{} score'.format(i)] = player['row{} score'.format(i)] * 0
               
   for i in range(size):
       for j in range(size):
               player['column{} score'.format(i)] = player['column{} score'.format(i)] * 0
               
   
   player['diagonal1 score'] = player['diagonal1 score'] * 0
   player['diagonal2 score'] = player['diagonal2 score'] * 0
   return player
#---------------------------------------score_calculator---------------------------------------------------------#
'''                                 is called in "end_game".     

  input: 
       -game placement: it is needed to calculate the score in 8 different ways:
                       row0, row1, row2, column0, column1, column2,diagonal1, diagonal2
       -player:use to update score-holding variables explained above.
  output: 
        -return an updated copy of player.
  
  how scores are calculated:
  if row0 = X|X|O (This is contained in game_placement list in form ['X','X','O'])
  the sprite store in player is fetched then game_placement [i][j] is compared to it
  if player sprite = X, then it will return 20.
  if player sprite = O, then it will return 1

''' 
def score_calculator(game_placement, player):
   player = reset_scores(player,len(game_placement))
   for i in range(len(game_placement)):
       for j in range(len(game_placement[i])):
           if game_placement[i][j] == player['sprite']:
               player['row{} score'.format(i)] += player['sprite weight']
               
           if game_placement[j][i] == player['sprite']:
               player['column{} score'.format(i)] += player['sprite weight']
                       
               
   ''' The first diagonal both indexes increment together--->[i][i] 
       But in the second diagonal the two indexes are opposite to each other, that's why an equation was used 
       in the second index
       if i = 0 -----> 2 - 0 = 2
       if i = 1 -----> 2 - 1 = 1
       if i = 2 -----> 2 - 2 = 0
   '''            
   for i in range(len(game_placement)):
       if game_placement[i][i] == player['sprite']:
           player['diagonal1 score'] += player['sprite weight']

       if game_placement[i][2-i] == player['sprite']:
           player['diagonal2 score'] += player['sprite weight']
   return player   

#------------------------------------------player_selection------------------------------------------------------#
'''                                is called within "input_decoding"
  input:
       -none
  output: 
        -integer value(from 1 to 9) represntation after validation.
  notes:
       this function will validatdate the value entered by PC num pad to be between 1 and 9 
  including 1 and 9(since this game has 9 locatoions) and digit not a character. since this value
  will be mapped to the correct location in game_placement using input_decoding function below.
    
''' 
def player_selection():
   player_input = 'waiting'
   number = 0
   while (number > 9 or number < 1) and not player_input.isdigit():
       player_input = input('choose a number that indicates your choice between 1 and 9 and make sure it is vacant:')
       if player_input.isdigit() and int(player_input) != 0:
           number = int(player_input)
   return number
#-------------------------------------------------input_decoding---------------------------------------------------#
'''                                       is called within "player_turn"
  input:
       -game_placement: used to check for vacant location on the board.
       -sprite: used to overwite vacant location with player's sprite.
  output: returns an updated version of game_placement.
       notes:
           player input is accepted after validation in "player_selection" function, and this 
       function will return a value from 1 to 9. Each value is then each player input
       is paired with a location inside game_placement list:
       1------> game_placement[0][0].
       and when the player enters a desired location (2 for example):
       the code below will check if the place is vacant, since a vacant place will be assigned a
       number from 1 to 9. And it will also check for the enter value is out of limit or not, then 
       lastly it will prevent overwriting an occupied location.
'''
def input_decoding(game_placement,sprite):
   correct_input = False
   i = 0
   j = 0
   while not correct_input:
       player_input =  player_selection()
#This equation (i = int(0.35 * player_input - 0.339999999999)) is used to convert: 1,2,3----> 0,0,0
#                                                                                  4,5,6----> 1,1,1
#                                                                                  7,8,9----> 2,2,2
       i = int(0.35 * player_input - 0.39999999999)
       if player_input in [1,4,7]:
           j = 0
       elif player_input in [2,5,8]:
           j = 1
       elif player_input in [3,6,9]:
           j = 2
       if str(player_input) == game_placement[i][j]:
           game_placement[i][j] = sprite
           correct_input = True
       elif player_input < 1 or player_input > 9:
           print('Out of limits!')
       elif game_placement[i][j] == 'X' or game_placement[i][j] == 'O':
           print('Choose a vacant place')
       if correct_input:
           break
               
   return game_placement
#--------------------------------------------------game_board----------------------------------------------------#
'''
  input:
       -game_placement.
  output:
       -prints the game board with the latest changes------>
                                                            X|2|3
                                                            -----
                                                            O|5|6
                                                            -----
                                                            7|8|9
'''
def game_board(game_placement):
   print('{}|{}|{}\n-----\n{}|{}|{}\n-----\n{}|{}|{}'.format(game_placement[0][0], game_placement[0][1], game_placement[0][2],
                                                             game_placement[1][0], game_placement[1][1], game_placement[1][2],
                                                             game_placement[2][0], game_placement[2][1], game_placement[2][2]))
#-----------------------------------------------sprite_weight------------------------------------------------------#
'''                                is called within "initialize_new_game"
 input:
      - selected sprite of the first palyer
 output:
      -for X it has a weight of 10 
      -for O it has a weight of 1
      1 & 10 was choosen to avoid possible misscalculations
'''
def sprite_weight(sprite):
   if sprite == 'X':
       return 10
   else:
       return 1
#--------------------------------------------choose_between_X_and_O------------------------------------------------#
'''                                  is called within "initialize_new_game"
 input:
      -throw: is a dictionary contains two value of random numbers to simulate a throw of 60-face dice.
      -name1: player1 name.
      -name2: player2 name.
 output:
       -a dictionary contains sprite assaignment.
 note:
     -the player with higher throw value will get to choose between X and O, the sprite assignment for the 
     second player will depend on first player choice.
'''
def choose_between_X_and_O(throw, name1, name2):
   choice = {name1:'',name2:''}
   if throw[name1] > throw[name2]:
       while choice[name1] != 'O' and choice[name1] != 'X':
           choice[name1] = input('{} choose between X and O:'.format(name1)).capitalize()
       if choice[name1] == 'X':
           choice[name2] = 'O'
       else:
           choice[name2] = 'X'
   else:
       while choice[name2] != 'O' and choice[name2] != 'X':
           choice[name2] = input('{} choose between X and O:'.format(name2)).capitalize()
       if choice[name2] == 'X':
           choice[name1] = 'O'
       else:
           choice[name1] = 'X'
   return choice
#----------------------------------------------player_naming--------------------------------------------------------#
'''                             is called within the main body of the code
 input:
      -value: it has 2 values---> A or B to vaguely indicate different players.
      -selection: contains the name of the other player to avoid using the same name for both players.
                  and it is only useful when the second player choose a name.
      -player_number: to indicate player No.1 or No.2, it is used with conjunction with selection,
      to make sure 'This name is already taken, enter a different name!' only appears to the second player.
 output:
       -player name after validation.
 note: the first character of each correct entry is capitalized to avoid scenario like: Mike and mike.
'''
def player_naming(value,selection,player_number):
   name = ''
   first_time = True
   while len(name) == 0 or name == selection:
       if name == selection and first_time == False and player_number > 1:
           print('This name is already taken, enter a different name!')# this massage can only appear to the second player
       elif len(name) == 0 and first_time == False:
           print('Enter a valid name!')
       name = input('Player {}, enter your name:'.format(value)).capitalize()
       first_time = False
       
   return name


#-----------------------------------------------random_dice---------------------------------------------------------#
'''                                    is called within "who_plays_first"
  input: NONE.
  output: 
         -player_throw: random number representing a dice throw
  notes: random_dice is generated by using for loop with random number of iterations
  and in each iteration a random number is generated to maximize randomness.
'''
def random_dice():
   value = int(randint(1,60))
   for i in range(value):
       player_throw = int(randint(1,60)) 
   return player_throw
#------------------------------------------who_plays_first----------------------------------------------------------#
'''                                        called within "initialize_new_game"
  input: player1-name and player2_name.
  output:
        a dictionary representing each player throw.
  notes:...
'''
def who_plays_first(player1_name,player2_name):
   player1_throw = 0
   player2_throw = 0
   throw_dictionary = {player1_name:player1_throw, player2_name:player2_throw}
   throw_dictionary[player1_name] = random_dice()
   throw_dictionary[player2_name] = random_dice()
                  
   if throw_dictionary[player1_name] == throw_dictionary[player2_name]:
       
       throw_dictionary[player1_name] = random_dice()
       throw_dictionary[player2_name] = random_dice()
      
   if throw_dictionary[player1_name] > throw_dictionary[player2_name]:
       print('{} throw:{}'.format(player1_name,throw_dictionary[player1_name]))
       print('{} throw:{}'.format(player2_name,throw_dictionary[player2_name]))
       print('{} will begin the game.'.format(player1_name))
       
   else:
       print('{} throw:{}'.format(player1_name,throw_dictionary[player1_name]))
       print('{} throw:{}'.format(player2_name,throw_dictionary[player2_name]))
       print('{} will begin the game.'.format(player2_name))

   return throw_dictionary
#----------------------------------------------yes_or_no-----------------------------------------------------------#
'''                    called within the main body of the code when game termination condition
                      is reached.       
 input: NONE.
 output: boolean value.
 notes: this function is used to continue playing or not. It only accepts 'Y' or 'N' as answers.
 A simple user validation messaging is implemented to help the use provide correct answer represenring 
 his decision.
'''
def yes_or_no():
   answer = 'wrong'
   while answer != 'Y' and answer != 'N':
       answer = input('Do you want to deal again?(Y/N)').capitalize()
       if answer != 'N' and answer != 'Y':
           print('Please only answer with "y" or "n"')
           time.sleep(2)
           clear_output(wait=True)
   if answer == 'N':
       return False
   else:
       return True
#---------------------------------------------------end_game--------------------------------------------------------#
'''                                     called within "player_turn"
  input:
        -player: current player.
        -enemy: the other player.
        -number_of_moves: value representing the current move number.
        -game_placement: use for "score_calculator".
  output:
        -return an updated version of the current player dictionary.
        
  notes: this function will calculate the score for the current player after he made his move
  in "player_turn" function. Then, if a winnin condition is met the boolean value "winner" in the 
  current player dictionary will be changed to True. Basid at when the player has won the game a message
  will be printed if at the end number of moves = 9 or at the middle of the game(<8).
'''

def end_game(player, enemy, number_of_moves, game_placement):
   player = score_calculator(game_placement, player)
   player['winner'] = check_for_winner(player) 
   if player['winner']:
       if number_of_moves < 8:
           print('{} is the winner!!!'.format(player['name']))
       else:
           print('What a game!!!. {} won at the end'.format(player['name']))
       player['wins'] += 1
       print('the current score between {} and {} is:\n{}:{}\n{}:{}'.format(player['name'],enemy['name'],
                                                                            player['name'], player['wins'],
                                                                            enemy['name'], enemy['wins']))
   if number_of_moves == 9 and not player['winner'] and not enemy['winner']:
       print('It is a tie!!!')
   return player
#---------------------------------------------------player_turn----------------------------------------------------#
'''                                       called within the main body of the code
  input:
        -player: the current player.
        -enemy: the other player.
        -game_placement: the last board before this turn.
        -number_of_moves: the total number of moves befor this turn.
  output:
        -update: a dictionary contianing:
        -updated player.
        -updated enemy.
        -updated game_placement.
        -updated number_of_moves.
   notes:
        -game_placement is updated after calling input_decoding.
        -player is updated after calling end_game function.
        
        
'''
def player_turn(player,enemy,game_placement,number_of_moves):
   
   update = {'player':{},'enemy':{},'game placement':[],'number of moves':0}
   print('{}, it is your turn:'.format(player['name']))
   game_placement = input_decoding(game_placement,player['sprite'])
   number_of_moves += 1
   clear_output(wait=True)
   player = end_game(player, enemy, number_of_moves, game_placement)
   game_board(game_placement)
   update['player'] = player
   update['enemy'] = enemy
   update['game placement'] = game_placement
   update['number of moves'] = number_of_moves
   
   return update
#--------------------------------------------initialize_new_game---------------------------------------------------#
'''                 called once in every game within main body of the code before each new game
  input: player1 and player2 dictionaries.
  
  output: a dictionary containing the following:
                                               -initialized player1 dictionary.
                                               -initialized player2 dictionary.
                                               -initialized game_placement list.
                                               
   notes: Here, the player who will begin the game will be decided. And sprite choid will be set alongside with it weight.
   The player with the larger throw will always be 'player1'.
                                               
'''
def initialize_new_game(player1,player2):
   initialize = {'player1':{},'player2':{},'game placement':[],'number of moves':0}
   clear_output(wait=True)
  
   player_choice = who_plays_first(player1['name'], player2['name'])

   print(player_choice)
   player_sprite = choose_between_X_and_O(player_choice,player1['name'],player2['name'])
   player1['sprite'] = player_sprite[player1['name']]
   player2['sprite'] = player_sprite[player2['name']]

   player1['sprite weight'] = sprite_weight(player1['sprite'])
   player2['sprite weight'] = sprite_weight(player2['sprite'])

#-----------------------------letting the player with higher throw have player1 designation-------------------------#
   if player_choice[player1['name']] < player_choice[player2['name']]:
       buffer = player1
       player1 = player2
       player2 = buffer
       
   initialize['player1'] = player1
   initialize['player2'] = player2
   initialize['game placement'] = [['1','2','3'],['4','5','6'],['7','8','9']]
   initialize['number of moves'] = 0
   
   return initialize
  
''' game_placement holds the shape of tic tac toe game in the form of list of lists containing vacant location for
   X's and O's.
'''      
#-------------------------------------------MAIN BODY OF THE CODE---------------------------------------------------#
#------------------------------------------------player name assignment---------------------------------------------#

player1['name'] = player_naming('A',player2['name'],1)
player2['name'] = player_naming('B',player1['name'],2)
continue_playing = True
while continue_playing:
   initialize = initialize_new_game(player1,player2)
   player1 = initialize['player1']
   player2 = initialize['player2']
   game_placement = initialize['game placement']
   number_of_moves = initialize['number of moves']
   clear_output(wait=True)
   game_board(game_placement)
   while True:
       update = player_turn(player1,player2,game_placement,number_of_moves)
       player1 = update['player']
       player2 = update['enemy']
       game_placement = update['game placement']
       number_of_moves = update['number of moves']
       if player1['winner'] or number_of_moves == 9:
           break
       update = player_turn(player2,player1,game_placement,number_of_moves)
       player2 = update['player']
       player1 = update['enemy']
       game_placement = update['game placement']
       number_of_moves = update['number of moves']
       if player2['winner'] or number_of_moves == 9:
           break
   continue_playing = yes_or_no()

