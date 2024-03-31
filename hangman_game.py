'''Hangman Test'''
import random
cities='minsk paris boston toulouse agra jaipur beijing seoul egypt dublin edinburgh'.split()       
countries='iceland ireland india china nigeria yemen tibet bhutan australia france'.split()
flowers="bouganvillea orchid jasmine peony oleander laurel chrysanthemum".split()
languages="french english greek latin spanish japanese chinese korean arabic urdu".split()
        # split() creates a list of the words in the the string and stores it in wordlist
l1=len(cities)
l2=len(countries)
l3=len(flowers)
l4=len(languages)
# for picking out a random word using indexing, we get random index value within the range of the length of wordlist
hanguy=["""
     +------+
            |
            |
            |
       ======""","""
     +------+
     O      |
            |
            |
       ======""", """
     +------+
     O       |
     |       |
             |
        ======""", """ 
     +------+
     O      |
   / |      |
            |
       ======""","""
     +------+
     O      |
   / | \    |
            |
       ======""","""
     +------+
     O      |
   / | \    |
    /       |
       ======""", """ 
     +------+
     O      |
   / | \    |
    / \     |
       ======"""]

print("Let's Play HANGMAN!!!!")
print("""Word categories:
         1.Countries
         2.Cities
         3.Flowers
         4.Languages """)
i=1
while i>0:
 choice=input("Enter your choice(1/2/3/4):")
 if choice=='1':
   rand_index=random.randint(0,l2-1) 
   word=countries[rand_index]
   i-=1
 elif choice=='2':
   rand_index=random.randint(0,l1-1) 
   word=cities[rand_index]
   i-=1
 elif choice=='3':
   rand_index=random.randint(0,l3-1) 
   word=flowers[rand_index]
   i-=1
 elif choice=='4':
   rand_index=random.randint(0,l4-1) 
   word=languages[rand_index]
   i-=1
 else:
   print('Please enter a valid choice.')


guessed,incorrect,correct=[], [], []
guessed1=''


print('START!!')
print(hanguy[0])
print()
i=6
while i>0:
  c=""
  for l in word:
    if l in guessed:
      c=c+l
    else:
      c=c+'_ '
  if c==word:
    print("You guessed the word!")

    print("""
         +------+
                |    
                |    O
                |  / | \\
           ======   / \\
                         """)
    for m in range(len(word)):
     if word[m] not in correct:
       print('You have LOST!!')
     else:
       print("You have WON!!!")
       break
    break
  print(c)
  print()
  print(i, "lives left!")
  guess=input("Guess any letter:")
  guess=guess.lower()
  print()

  if guess.isalpha()==True:
    if len(guess)>1:
      print("ERROR!Enter one letter at a time!")
      print()
    elif guess in guessed:
      print('This letter has already been guessed!')
      print("The letters you have guessed until now are:",guessed1)
    elif guess in word:
      print("You guessed that right! Keep going!")
      guessed.append(guess)
      correct.append(guess)
      guessed1+=guess+', '
    else:
      print("Oops! You got that wrong.")
      i-=1
      print(hanguy[6-i])
      incorrect.append(guess)
      guessed.append(guess)
      guessed1+=guess+', '
  else:
    print("ERROR!Enter a letter!")
    print()

print('The word is:',word)
print("GAME OVER")
