#first part
print('welcome to my quiz!') #welcome the player

playing = input('do you want to play the quiz? (yes/no): ') #ask the player if they wanna play -- the input is stored in the variable playing

if playing.lower() != 'yes': #if the player chooses anything other than yes, the game will quit
    quit()

print("okay let's play!")


points = 0
#question 1
answer = input('what does CPU stand for? ') #ask the player the question and store the answer in the variable
if answer.lower() == 'central processing unit': #check if the answer is correct
    print('correct!')
    points += 1
else:
    print('incorrect!')

#question 2
answer = input('what does GPU stand for? ') 
if answer.lower() == 'graphics processing unit':
    print('correct!')
    points += 1
else:
    print('incorrect!')

#question 3
answer = input('what does RAM stand for? ') 
if answer.lower() == 'random access memory': 
    print('correct!')
    points += 1
else:
    print('incorrect!')

#question 4
answer = input('what does PSU stand for? ') 
if answer.lower() == 'power supply unit':
    print('correct!')
    points += 1
else:
    print('incorrect!')

#question 5
answer = input('what does SD stand for? ') 
if answer.lower() == 'secure digital':
    print('correct!')
    points += 1
else:
    print('incorrect!')

#question 6
answer = input('what does USB stand for? ')
if answer.lower() == 'universal serial bus':
    print('correct!')
    points += 1
else:
    print('incorrect!')

#question 7
answer = input('what does SSD stand for? ') 
if answer.lower() == 'solid state drive': 
    print('correct!')
    points += 1
else:
    print('incorrect!')

#question 8
answer = input('what does hd stand for? ') 
if answer.lower() == 'hard drive': 
    print('correct!')
    points += 1
else:
    print('incorrect!')


print("you got " + str(points) + " questions correct! thats " + str(round(points/8*100)) + "%") #print the number of questions the player got correct, str() is used to convert the integer points into a string so it can be concatenated with the other strings
