class Quiz:
    def __init__(self, ask, answer):
        self.ask = ask
        self.answer = answer


question_asked = [
    "\n1) who was the first ottoman sultan?"
    "\n(the answer should be exactly like this: Name(first letter capitalized) order in numbers)  ",
    "\n2) In football, which team has won the Champions League (formerly the European Cup) the most?"
    "\n(the answer should be exactly like this: The team's full name with the first letters capitalized capitalized) ",
    "\n3) What is the middle name of Angela Merkel?"
    "\n(the answer should be exactly like this: The middle name with the first letters  capitalized) ",
    "\n4) Which vitamin is the only one that you will not find in an egg?"
    "\n(the answer should be exactly like this: Vitamin the vitamin's name in capital letter) ",
    "\n5) Who played Queen Elizabeth II in the first two seasons of The Crown (Netflix)?"
    "\n(the answer should be exactly like this: Full name with the first letters  capitalized) ",
    "\n6) Who is the only musician ever to have been awarded the Nobel prize for literature?"
    "\n(the answer should be exactly like this: Full name with the first letters capitalized) ",
    "\n7) Who said this famous quote if you can dream it you can do it?"
    "\n(the answer should be exactly like this: Full name with the first letters  capitalized) ",
    "\n8) In which year did ww2 begin?"
    "\n(the answer should be exactly like this: the year in numbers) ",
    "\n9) who is the richest person in the world 2021?"
    "\n(the answer should be exactly like this: Full name with the first letters capitalized) ",
    "\n10) Who is known as the first programmer of the world?"
    "\n(the answer should be exactly like this: Full name with the first letters capitalized) "

]

questions = [
    Quiz(question_asked[0], "Osman 1"),
    Quiz(question_asked[1], "Real Madrid"),
    Quiz(question_asked[2], "Dorothea"),
    Quiz(question_asked[3], "Vitamin C"),
    Quiz(question_asked[4], "Claire Foy"),
    Quiz(question_asked[5], "Bob Dylan"),
    Quiz(question_asked[6], "Walt Disney"),
    Quiz(question_asked[7], "1939"),
    Quiz(question_asked[8], "Jeff Bezos"),
    Quiz(question_asked[9], "Ada Lovelace"),
]


def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.ask)
        if answer == question.answer:
            score += 10
    print("\nyou got", score, "out of", len(questions)*10)
    if score <= 50:
        print("Unsuccessful! Try again.")
    else:
        print("Successful. Congrats!")


run_quiz(questions)