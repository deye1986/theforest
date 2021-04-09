# team4: david ikin, nathan clarke & darren murphy
# with codenation 2021
# The forest - a text based adventure

import sys
from time import sleep


def type_writer(x): # on second thought, were gonna up the speed and use this function for long paragraphs
    '''apply a typewriter style graphic to the output in the terminal'''
    for char in str(x): # probably best to use a for loop here, leave it be.
        sleep(0.02) # speed
        sys.stdout.write(char) 
        sys.stdout.flush()

def game_loop():
    '''the game is played from within this function, mostly events are checked and updated'''
    
    def win_game():
        type_writer(f'''
    ****************   C O M P L E T E   ******************
    **  G E T   R E A D Y   F O R   T H E   S E Q U E L  **
    **                                                   **
    **             C O M I N G   S O O N . . . . .       **
    *******************************************************
    **       T E A M _ 4    2 9  /  0 3  /  2 0 2 1      **
    **                                                   **
    **                C O D E N A T I O N                **
    **                                                   **
    **                      2 0 2 1                      **
    *******************************************************
    ''')
        game_over()

    choice_1 = ''
    player_one = ''
    level1 = True # bridge
    level2_1 = False # vines
    level2_2 = False # warlock
    troll = False
    ending = False # 
    
    
    credits = '''
    programming: dave ikin, nathan clarke & darren murphy
    story and design: nathan clarke, darren murphy & dave ikin
    thanks to mike c, codenation manchester. 2021.
    '''
    type_writer(credits)

    player_one = input('Type your name to continue... ')
    if player_one == '':
        player_one = 'Player 1 ' 

    while level1 == True:
        type_writer('''
    You're walking down a winding path, trying to reach a neighbouring kingdom to 
    deliver an important message. You reach the bridge you need to cross only to 
    discover it's remains scattered across the ground below you, the only way through 
    is a dark forest, known in legend as the inescapable forest.
        ''')

        choice_1 = str(input('''
    Do you (1) enter the forest alone, or (2) wait a while, surely someone is 
    going to need to also cross the bridge.
        '''))

        if choice_1 == '1':
            type_writer('''
    ***** Welcome to The Inescapable Forest *****

    Population : Everybody stupid enough to enter      
            ''')
            level1 = False
            level2_1 = True

        elif choice_1 == '2':
            type_writer('''
    *****       You decide to wait...       *****      
            ''')
            level1 = False
            level2_2 = True        

        else:
            type_writer('''
    Invalid input, press either 1 or 2 and press enter.
            ''')
        continue


    while level2_1 == True:
        type_writer('''
    Whilst walking through the forest, your feet rapidly begin to feel more heavy,
    you look down to see dark green vines slowly growing up your feet.
        ''')

        choice_2_1 = str(input('''
    Do you pull out your sword and cut the vines and get away as fast as possible 
    (1) or ignore the vines and continue walking to not alert the 
    plant that you've noticed (2) 
            '''))
        if  choice_2_1 == '1':
            type_writer('''

    * * * * *       Slash !!       * * * * *
    
    Cutting the vines appears to alert the plant
    that you've noticed, it quickly engulfs you in thicker, stronger vines. 
    You try to fight, but are eventually crushed.
            ''')
            level2_1 = False
            game_over()                                    
        
        elif choice_2_1 =='2':
            type_writer('''
    You survive!! But, at what cost!! 
    Continuing through, pulling your feet through the vines you continue walking through 
    the brush, as you walk through you come too close to what seems to be the main plant 
    trying to attack you. Luckily, you are expecting this, so you successfully fend it off. 
    You lose a substantial portion of your hp in the struggle.
            ''')                       
            level2_1 = False
            troll = True
            
        else:
            type_writer('''
    You should press  1  or  2  at this point. HehE :p
                ''')
            continue

    
    while level2_2 == True:
        type_writer('''
    You wait around the remains of the bridge, after a few hours pass you see a horse drawn 
    cart approaching with a slender, old man at the reins. He stops and offers you to join 
    him after seeing the bridge's state. You join him at the front of the cart.
    As you are riding alongside him you hear strange thuds coming from behind you, as you 
    continue travelling the thudding intensifies.
        ''')

        choice_1 = str(input('''
    Do you confront the man, and question him what the thudding is (1) or assume it's just 
    random sounds from whatever lies in this forest and continue (2)
    
        '''))

        if  choice_1 == '1':
            type_writer('''

    * * * * *      Enquiry      * * * * *     

    The old man urges you to take a look, worrying something is attempting to enter 
    his cart. As you walk around to check you hear him following you, you turn to see hunger 
    in his eyes, his face has started to look more... dead... He murmurs \"I was hoping you 
    wouldn't notice\" and a faint green glow begins to emanate from his hands. You realise 
    what's happening, he's a warlock preparing to drain your life. 
    
    * * *       A T T A C K !        * * *

    You lunge at him, striking 
    him down !!!  But from the ground he begins to
    cast his spell ! You manage to kill 
    the warlock, but he has badly hurt you in the process...
                ''')
            level2_2 = False
            troll = True    

        elif choice_1 == '2':
            type_writer ('''
    You ignore the thudding and eventually reach a dead end in the path you are following with 
    a lit fire and a small camp, the man urges you to investigate, whilst doing that you feel a 
    sharp pain hit you from your back and are totally immobilized, you see a faint glow 
    emanating from you and realise this seemingly innocent man is a warlock, draining your 
    life force. You slowly feel your very essence being drained.

            ''')            
            level2_2 = False
            game_over()

        else:
            type_writer('''
    Invalid input, choose 1, or 2 !
        ''')
        continue

    while troll == True:
        type_writer('''
    You slowly make your way through the forest, still wary and hurt 
    from your previous encounter, you turn around a corner and see a 
    menacing troll staring down at you less than ten feet away.  As 
    you turn to attempt to flee he exclaims \"Please no go!\" in a 
    distraught voice. You turn around and he explains \"Me lonely, this 
    only path to other side, since bridge fall me unemployed.\" He hangs 
    his head in despair. \"You play game with me?\" You agree, slightly
     confused but with a forced smile on your face.'
        ''')
        type_writer('''
    With a shrewd look, he asks \"Ok what is wet and see through?\"
        ''')
        troll_response_one = input('>>  ')
        if troll_response_one == "water".lower():
            type_writer("The troll claps his hands in glee and exclaims \"You smart like me, me try another!\"")
            troll = False
            troll_2 = True
            
        else:
            type_writer('''
    He smirks and says \"That one too hard, but you get right soon. Me give hint, you drink it when no drinking blood\"
        ''')
            continue

    while troll_2 == True:
        type_writer('''
    Scratching his head he asks \"What is blue and up there?\" He references up to the sky with one large, dirty finger.    
        ''')
        troll_response_2 = input('>>  ')
        if troll_response_2 == 'SKY'.lower():
            type_writer('''
    \"Woah you get it, me starting to think you smarter than me\" Me think of another!      
            ''')
            troll_2 = False
            troll_3 = True
        else:
            type_writer('''
    \"You no so smart, me give hint, it had white poofs there and sometimes water drop from it\"        
            ''')
            continue

    while troll_3 == True:
        type_writer('''
    He thinks for a painful amount of time, and his eyes light up and 
    he asks \"Ok, ok, me know! Who is the handsomest troll in the 
    forest?\" He looks expectantly at you, a slight smile on his brutish face.     
        ''')
        troll_response_3 = input('>>  ')
        if troll_response_3 == 'YOU'.lower():
            troll_3 = False
            ending = True
            type_writer('''
    \"Yes! Me handsomest troll in whole world not just forest! You do well, you pass.\"        
            ''')
        else:
            type_writer('''
    He glares down at you, clearly enraged and thuds the ground with his large foot and 
    screams \"NO, ME THE HANDSOMEST TROLL IN THE FOREST, YOU PAY FOR STUPID\"
    The troll then smacks down with his giant club, crushing you and continues with his tantrum.       
            ''')
            game_over()

    while ending == True:
       
        type_writer('''
    You are walking down the path and see a faint blue glow in the distance
            ''')
        type_writer('''
    Upon getting closer, the blue glow intensifies as you approach a large expanse of water, small 
    flowers with petals the exact same shade of glowing blue scatter the surrounding area. 
    Hovering in the centre of the water is the silhouette of a beautiful woman, 
    her head facing down and a flow of long blonde hair trailing down to her waist. You sense danger.
            ''')
        type_writer ('''
    Do you: Sneak around the area in the brush (1), Walk through the zone quietly to not disturb 
    the seemingly sleeping woman (2), Confront the sleeping woman and ask for passage (3)
            ''')
        
        choice1 = input('''
    >>    ''')

        if choice1== "1":
            type_writer('''
    Whilst sneaking around the brush to avoid this mysterious woman, her head suddenly raises 
    and glares at the place you are hidden, in an ethereal voice she exclaims \"Foolish mortal, 
    you believe yourself hidden? Your cowardice must be punished.\"You feel your feet leave 
    the ground as you fly through the air into the lake and drown.
            ''')
            game_over()

        elif choice1== "2":
            type_writer('''
    You calmly walk around the water, as you reach around half way the mysterious woman's head 
    suddenly raises and your eyes lock, in an ethereal voice she questions \"You think me a fool? 
    That I would miss your light steps? At least you didn't cower in fear like many before you, 
    but you will be punished.\" you feel your feet leave the ground as you float in mid air, a 
    sharp stabbing pain shudders through you. \"Leave, now, before I change my mind\" she murmurs 
    and you quickly pass to the other side.
            ''')
            type_writer('''
    The remainder of your travels are uneventful, you safely reach the other side of the forest 
    and are back on track to reach your neighbouring kingdom, you are badly hurt, but you survived.
            ''')
            win_game()

        elif choice1== "3":
            type_writer ('''
    You calmly walk to the edge of the water and ask for safe passage, her head raises and she 
    calmly says in an ethereal sounding voice \"Hello, mortal. I admire your courage where 
    many have faltered, you may pass this place, but I suggest you do not return here, my 
    kindless has many bounds.\" You nod your head, and quickly walk through and pass.
            ''')
            type_writer ('''
    The remainder of your travels are uneventful, you safely reach the other side of the forest 
    and are back on track to reach your neighbouring kingdom.
            ''')
            win_game()
        else:
            type_writer('''
    Invalid input, choose 1, 2 or 3 .
            ''')
            continue
            
        
def game_over(): # offers the player a restart or exits the terminal.
    '''end the game'''
    
    game_over_str = '''
    *************      G A M E   O V E R      *************
    '''
    type_writer(game_over_str)
    again = str(input('''
    Another Game? Type YES or NO.
    '''))
    if again == 'YES' or again == 'yes' or again == 'Yes':
        game_loop()
    elif again == 'No' or again == 'NO' or again == 'no':
        sys.exit()
    else:
        type_writer('''
    You should type yes or no at this prompt.
        ''')
        game_over() # recursion

game_loop() # run the game after all game functions are declared

