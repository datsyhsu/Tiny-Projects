print('''
                        \
      '.                 \.
       '.                 "\
       ::                  \\
       " .                 ".\
        ""    ;.   ,        " .
        ".~   ."-  .^  .     \ \
     -.._" \   \ \  \\  \    "  \
       "."\ \._ ) \ ) \.)\-\..\  :
         ""\ ",\"_.);-.).) )) "~~).
 ~"~~.._    '  -"         ""~.)    "~,
  ""~.  ""~~)". "-,           ",."""" "~.
      " ..~"," '-'"~~...___.~""  "~.     ~.
       ."  ."      _.~~"""".,       "~.   "~~~.~.  _..._
     ."    |       '. (  () )";>       ""~.      "(.___.)..
    /      "       ..""~~~~""_.~  ....._.  "~.             ""~.
   "     ___\~-      """"""""    "       ""~~.""":==>..        "~.
 ."          \_~               .              "~((####)) ..       ".
|       _.-"", /          ..~"                  ""~~~"    ""~~~~~  :>
              /".                       .~"~~..___............~;>~""
           .~"  "~.         "-~~....--""__________,,....~~~~"""
                   "--""~~..._____,..~~"
                  ."
                  |
                  ;
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".').lower()

if choice1 == "left":
  #continue in the game
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake, Type "wait" to wait for a boat. Type "swim" to across.').lower()
  if choice2 == "wait":
    choice3 = input("You arrive the island unharmed. There is a house with 3 doors. One red, one yellow and one blue, which one do you choose?").lower()
    if choice3 == "yellow":
      print("You Win!")
    elif choice3 == "red":
      print("Burned by fire. Game Over.")
    elif choice3 == "blue":
      print("Eaten by beasts. Game Over.")
    else:
      print("Game Over.")
  else:
    print("Attack by trout. Game Over.")
else:
  print("Fall in a hole. Game Over.")