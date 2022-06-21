#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random

state='''AndhraPradesh	Amaravati
ArunachalPradesh	Itanagar
Assam	Dispur
Bihar	Patna
Chhattisgarh	Raipur
Goa	Panaji
Gujarat	Gandhinagar
Haryana	Chandigarh
HimachalPradesh	Shimla
Jharkhand	Ranchi
Karnataka	Bengaluru
Kerala	Thiruvananthapuram
MadhyaPradesh	Bhopal
Maharashtra	Mumbai
Manipur	Imphal
Meghalaya	Shillong
Mizoram	Aizawl
Nagaland	Kohima
Odisha	Bhubaneswar
Punjab	Chandigarh
Rajasthan	Jaipur
Sikkim	Gangtok
TamilNadu	Chennai
Telangana	Hyderabad
Tripura	Agartala
UttarPradesh	Lucknow
Uttarakhand	Dehradun
WestBengal	Kolkata'''
state_list=state.split()
state_dict={}
for i in range(0,len(state_list)-1,2):
    state_dict[state_list[i]]=state_list[i+1]
capitals=state_dict

n=int(input('Enter number of question paper required: '))
for quizNum in range(n):
    # TODO: Create the quiz and answer key files.
    quizFile = open(f'capitalsquiz{quizNum + 1}.txt', 'w')
    answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w')

    # TODO: Write out the header for the quiz.
    quizFile.write('Name:\nRoll:\nDate:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form{quizNum + 1})')
    quizFile.write('\n\n')

    # TODO: Shuffle the order of the states.
    states=list(capitals.keys())
    random.shuffle(states)

    # TODO: Loop through all 28 states, making a question for each.
    for questionNum in range(28):
        correctAnswer=capitals[states[questionNum]]
        wrongAnswer=list(capitals.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrongAnswer = random.sample(wrongAnswer, 3)
        answerOptions = wrongAnswer + [correctAnswer]
        random.shuffle(answerOptions)
        # Write the question and the answer options to the quiz file.
        quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f" {'ABCD'[i]}. {answerOptions[i]}\n")
        quizFile.write('\n')
        # Write the answer key to a file.
        answerKeyFile.write(f"{questionNum + 1}.{'ABCD'[answerOptions.index(correctAnswer)]}\n")
quizFile.close()
answerKeyFile.close()