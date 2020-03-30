import random

'''
Callisto Hess 03/30/20

Command Line Tool for studying classification of lifeforms.
Accepts a file, "answers.csv" in the same directory as input.
"answers.csv" must be in following format:

Scientific Classification,Common Name,Requires Fields

'''
file = open('answers.csv', 'r')

# pre-defining lists
answers = []
incorrect_answers = []

for line in file:
    # adds the rows to the incorrect answers list after removing newline characters
    line = line.strip('\n').split(',')
    # adds items to incorrect answers list
    answers.append(line)

while len(answers) != 0:
    # shuffles contents of incorrect answers each iteration
    random.shuffle(answers)
    # creates display message which informs user of requirements
    input_message = input("{} for {}: ".format(
        answers[0][2], answers[0][1]))
    # checks input against provided answer. Is not case sensitive. If they are the same, pop answer from list.
    if input_message.lower().strip() == answers[0][0].lower():
        print()
        print("=============== Correct! ===============")
        print("{} was removed from the list.".format(answers[0][0]))
        answers.pop(0)
    else:
        print()
        print("============== Incorrect! ==============".format(
            answers[0][0]))
        print("The correct answer is: {}.".format(answers[0][0]))
        if answers[0] not in incorrect_answers:
            incorrect_answers.append(answers[0])

    print("============ {:02d} remaining. =============\n".format(
        len(answers)))

print()
print("=============== Finished! ===============")
print("You got the following incorrect, study up:")
for item in incorrect_answers:
    print("{} : {}".format(item[1], item[0]))
