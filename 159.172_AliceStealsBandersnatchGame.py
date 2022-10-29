# http://programarcadegames.com/index.php?lang=en&chapter=lab_camel

#!/usr/bin/env python
# Massey U 159.172 Tutorial.01_
# Elizabeth McCready mselizabethmccready@gmail.com
# 19044241 www.mapgeek.world
# July, 2020
# _________________________
# INSTRUCTIONS
# Create  a  new  program  camel.py
# camel.py and  add  code  to  print  the  instructions  to  the  screen.
# Do  this  with  multiple  print statements.
# Don't  use  one  print statement  and  multiple
# \n\n characters  to  jam  everything  on  one  line.
# __________________________________
# [Print the following]
# Welcome to Bandersnatch!
# You have stolen the Red Queen's Bandersnatch to make your way across
# Underland to Marmoreal, the White Queen's kingdom.
# The Red Queen's Card Soldiers want their Queen's Bandersnatch back and are chasing you
# down! Survive your
# trek across Underland and out run the Card Soldiers.

# __________________________________
# prints welcome message and explains the game's goal on screen
from random import randint

print('Welcome to Underland!')
print('You have stolen the Red Queen\'s Bandersnatch to make your way across')
print('Underland to Marmoreal, the White Queen\'s kingdom.')
print('The Red Queen\'s Card Soldiers want their Queen\'s Bandersnatch back and are chasing you')
print('down! Survive your')
print('trek across Underland and out run the Card Soldiers.')
# 2. Create  a  boolean  variable  called  done and  set  to  False.

done = False
usr_choice = ('')
# 8-10.  Create variables for game and set initial values
km_traveled = 12
thirst = 0
bandersnatch_tiredness = 0
card_soliders_km_travelled = -20
tea_drinks = 4
tea_party = 42
# tea_party = 42 because D. Adams' HGTTG
find_tea_party = 0
# added level of difficulty - random chance that the Jabberwocky does a surprise attack
jabberwocky_attacks = 52
jabberwocky_finds_you = 0

# 3.  Create  a  while loop  that  will  keep  looping  while  done is  False.

while done == False:
    print('A. Drink from your tea canteen.')
    print('B. Ahead moderate speed.')
    print('C. Ahead full speed.')
    print('D. Stop for the night.' )
    print('E. Status check.')
    print('Q. Quit')
    # print blank line to make game easier to read
    print()

    usr_choice = input('What is your choice?  ')
    if usr_choice.upper() == 'Q':
        done = True

    # Player chooses to DRINK
    elif usr_choice.upper() == 'A':
        if tea_drinks >= 1:
            tea_drinks = tea_drinks - 1
            thirst = 0
            print('You had a cup of tea.')
            # uncomment line below to check number of tea drinks left for debugging/checking code
            # print(tea_drinks)
        else:
            print('TeaPartyError: You have no tea drinks left.')

    # Player chooses to MOVE AT MODERATE SPEED
    elif usr_choice.upper() == 'B':
        # add a random integer number of km travelled between 5 and 12km
        km_traveled = km_traveled + randint(5, 13)
        # increases thirst b
        thirst = thirst + 1
        # adds a random amount of 1 to how tired the Bandersnatch is (testing programmer's knowledge of ranges. ;-) )
        bandersnatch_tiredness = bandersnatch_tiredness + randint(1, 2)
        # adds random integer between 7 & 14 to the distance the card soliders have travelled
        import random
        card_soliders_km_travelled = card_soliders_km_travelled + randint(7, 15)
        print('You are travelling ahead at moderate speed and have travelled:', km_traveled, 'km.')
        print('Thirst is now:', thirst)
        print('The Bandersnatch\'s tiredness is now:', bandersnatch_tiredness)

    # Player chooses to MOVE AHEAD AT FULL SPEED
    elif usr_choice.upper() == 'C':
        # add a random integer number of km travelled between 10 and 20km
        km_traveled = km_traveled + randint(10, 21)
        # increases thirst by 1
        thirst = thirst + 1
        # adds a random amount of 1 to 3 how tired the Bandersnatch is (testing programmer's knowledge of ranges. ;-) )
        bandersnatch_tiredness = bandersnatch_tiredness + randint(1, 4)
        # adds random integer between 7 & 14 to the distance the card soliders have travelled
        card_soliders_km_travelled = card_soliders_km_travelled + randint(7, 15)
        # print statements giving player updates on their game progress
        print('You are travelling ahead at full speed and have travelled:', km_traveled,'km.')
        print('Thirst is now:', thirst)
        print('The Bandersnatch\'s tiredness is now:', bandersnatch_tiredness)

    # Player chooses to REST FOR THE NIGHT
    elif usr_choice.upper() == 'D':
        # resets Bandersnatch's tiredness to zero
        bandersnatch_tiredness = 0
        # adds random integer between 7 & 14 to the distance the card soliders have travelled
        import random
        card_soliders_km_travelled = card_soliders_km_travelled + randint(7, 15)
        # Tells user where the card soliders are - *-1 gives positive answer b/c value in system is in negative int
        print('cs travelled', card_soliders_km_travelled)
        print('The Queen\'s Card Soliders are', km_traveled - card_soliders_km_travelled, 'km behind you')
        print('The Bandersnatch is happy.')

    # Player chooses to STATUS CHECK
    elif usr_choice.upper() == 'E':
        print('km_travelled: ', km_traveled)
        print('Drinks in tea canteen:', tea_drinks)
        # Tells user where the card soliders are
        print('The card soliders are ', (km_traveled - card_soliders_km_travelled), 'km behind you.')
        print()  # prints blank line to make viewing game nicer


    # code for randomly finding tea party (aka oasis). Need to figure out random
    if not done:
        find_tea_party = randint(22, 43)
        # print('Find tea party=', find_tea_party) ## uncomment for debugging
        if find_tea_party == tea_party:
            print('***********')
            print('You found a tea party!')
            tea_drinks = 4
            thirst = 0
            bandersnatch_tiredness = 0
            print('***********')
            # continue prevents the unlikely, but possible event of finding a tea party but being surprise attacked by the Bandersnatch
            continue

    # game progress/win/loss statements

    if not done and thirst > 6:
        print('You died of thirst.')
        done = True
    if not done and thirst > 4:
        print('You are thirsty.')
    if not done and bandersnatch_tiredness > 5:
        print('The Bandersnatch is getting tired.')
    if not done and bandersnatch_tiredness > 8:
        print('The Bandersnatch is dead.')
    if not done and card_soliders_km_travelled >= km_traveled:
        print('The Queen\'s soliders have caught you.')
        print('The game is over.')
        done = True
    if not done and card_soliders_km_travelled >= km_traveled - 15:
        print('The Queen\'s soliders are getting close.')
    if not done and km_traveled >= 200:
        print('You have travelled', km_traveled,'across Underland and have won the game.')
        done = True
    print()

    # >>>>>>>>>>>
    # added code for randomly being surprise attacked by Jabberwocky
    if not done:
        jabberwocky_finds_you = randint(1, 102)

        # print(jabberwocky_finds_you) ##uncomment for debugging
        if jabberwocky_finds_you == jabberwocky_attacks:
            print('The Jabberwocky launched a surprise attack and killed you. Game over.')
            print('''
            Twas brillig, and the slithy toves
            Did gyre and gimble in the wabe;
            All mimsy were the borogoves,
            And the mome raths outgrabe.

            “Beware the Jabberwock, my son!
            The jaws that bite, the claws that catch!
            Beware the Jubjub bird, and shun
            The frumious Bandersnatch!”

            He took his vorpal sword in hand:
            Long time the manxome foe he sought–
            So rested he by the Tumtum tree,
            And stood awhile in thought.

            And, as in uffish thought he stood,
            The Jabberwock, with eyes of flame,
            Came whiffling through the tulgey wood,
            And burbled as it came!

            One two! One two! And through and through
            The vorpal blade went snicker-snack!
            He left it dead, and with its head
            He went galumphing back.

            “And hast thou slain the Jabberwock?
            Come to my arms, my beamish boy!
            O frabjous day! Callooh! Callay!”
            He chortled in his joy.

            ‘Twas brillig, and the slithy toves
            Did gyre and gimble in the wabe;
            All mimsy were the borogoves,
            And the mome raths outgrabe.''')
            done = True
