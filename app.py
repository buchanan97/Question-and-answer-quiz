from Question import Question # import the class in order to creat the object 
question_prompts = [ # I named this question prompt because this will 
    #prompt the user to choose an answer to a question

    "What is the capital of the United States? \n(a) Birmingham \n Las Vegas (b)\n Albany (c) \n New York (d) \n\n",
    "What year did the first iphone come out?  \n(a) 2006 \n (b) 2008 \n (c) 2009 \n (d) 2007  \n \n",
    "What year did the python language come out? \n (a) 2008 \n (b) 1980 \n (c) 1991 \n (d) 2000 \n \n "
]

questions = [
    Question(question_prompts[0], "d"), #objects first letter should always be capitalized
    Question(question_prompts[1], "d"),#A selection criteria made in order for the end user to choose from
    Question(question_prompts[2], "c"),
]

def run_test(questions): #running a function to continuously loop through questionaries
    score = 0 # will hold the score of the questions answered corrctly for the user
    for question in questions: #for loop to run the questions out from 1 to 3
        #the objects being called
        answer = input(question.prompt)#prompting the user to answer the question with input
        if answer == question.answer: #using the if conditional to determine if the answer
            #is correct or not correct to recieve points
            score+= 1 #the plus 1 operator will score the correct answer or the 
            #-operator will decrease the score
        print("You got a score of " + str(score) + "/" + str(len(questions)) + "Correct" )
#The print statemtent will show if you got a 100 or below depending on the input
run_test(questions) #this will run the test function, which in turn corresponds to the
#object program