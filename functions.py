"""A collection of function for doing my project."""

lst = []

name = ""

counter = 0

def start():
    """This is the introduction to the Joke Machine, which will allow the user to input their name 
    and current mood, which will then allow the Joke Machine to asses the useres name modd and 
    recomend a corresponding level of laughter for the jokes, the participant will ultimamtly 
    decide the level of laughter for the jokes they wish to hear.
    
    PARAMETERS
    ----------
    none
    
    RETURNS
    -------
    none
    """
    
    # input name and age to print out a custom message.
    
    global name
    name = input("What is your name kind human? ")
    day = input("How is your day going so far? (use adjectives)") 
    print("\nHello {}, and WELCOME to the Joke Machine!!!\n"
          "I've noticed you've mentioned your day is {}. What a great time it is to be alive!\n"
          "I hope you're ready to laugh and make your day ten times better!\n"
          "This Joke Machine will recomend types of jokes for you,\n"
          "however, you will ultimately decide what makes you laugh.\n".format(name, day))
    
    # assesses current mood and recomends level of laughter.
    
    mood =  input("Considering your current mood, how would you describe it? (Happy, Indifferent, or Sad): ")
    if mood == "Happy":
        statement = ("I am so happy you're happy! Let's keep you in this great mood!\n"
                     "I recomend a joke from the Snicker Level of Laughter!\n"
                     "However, please feel free to choose any Level of Laughter you'd like!\n")
    elif mood == "Indifferent": 
        statement = ("Glad to hear your doing ok! Let's see if we can improve this mood some!\n"
                     "I recomend a joke from the Laughing Out Loud Level of Laughter!\n"
                     "However, please feel free to choose any Level of Laughter you'd like!\n")
            
    else: 
        statement = ("Sorry to hear you're not in the best mood. Let's try to brighten your day!\n"
                     "I recomend a joke from the Rolling On The Floor Level of Laughter!\n"
                     "However, please feel free to choose any Level of Laughter you'd like!\n")
    print(statement)
    
    # code allows user to imput desired level of laughter and runs code from level of laughter specified.
    
    select_lol = input("What Level of Laughter would you like (Snicker, Laughing Out Loud, or Rolling On The Floor)?: ")
    
    if select_lol == "Snicker":
        snicker()
    
    elif select_lol == "Laughing Out Loud":
        laughing_out_loud()
    
    else:  
        rolling_on_floor()

    satisfaction()
        
def snicker():
    """Three jokes from the Snicker Level of Laughter category will be provided for the user to enjoy, 
    the user will have the chance to guess the answer to the joke, then the correct answer to the 
    joke will be returned.
    
    PARAMETERS
    ----------
    none 
    
    RETURNS
    -------
    none 
    """
    # print out jokes and allow user imput for answer.
    
    print("\nJoke: What did the fish say when he swam into the wall?")
    input("Guess the answer to the joke: ")
    print("Answer: Damn!\n")
    print("Joke: What is Forrest Gump's email password?")
    input("Guess the answer to the joke: ")
    print("Answer: 1forrest1!\n")
    print("Joke: What do you call a fake noodle?")
    input("Guess the answer to the joke: ")
    print("Answer: an impasta!")
            
            
def laughing_out_loud():
    """Three jokes from the Laughing Out Loud Level of Laughter category will be provided for the 
    user to enjoy,  the user will have the chance to guess the answer to the joke, then the correct 
    answer to the joke will be returned.
    
    PARAMETERS
    ----------
    none
    
    RETURNS
    -------
    none
    """
   
    # print out jokes and allow user imput for answer.
    
    print("\nJoke: What did the the drummer call his twin daughters?")
    input("Guess the answer to the joke: ")
    print("Answer: Anna one, Anna two!\n")
    print("Joke: What does a nosey pepper do?")
    input("Guess the answer to the joke: ")
    print("Answer: It gets jalapeño business!\n")
    print("Joke: Why don’t they play poker in the jungle?")
    input("Guess the answer to the joke: ")
    print("Answer: Too many cheetahs!")

def rolling_on_floor():
    """Three jokes from the Rolling On The FLoor Level of Laughter category will be provided for the 
    user to enjoy,  the user will have the chance to guess the answer to the joke, then the correct 
    answer to the joke will be returned.
    
    PARAMETERS
    ----------
    none 
    
    RETURNS
    -------
    none 
    """      
    
    # print out jokes and allow user imput for answer.
    
    print("\nJoke: Why did Adele cross the road?")
    input("Guess the answer to the joke: ")
    print("Answer: To say hello from the other side.\n")
    print("Joke: How does a penguin build it’s house?")
    input("Guess the answer to the joke: ")
    print("Answer: Igloos it together.\n")
    print("Joke: Why do cow-milking stools only have three legs")
    input("Guess the answer to the joke: ")
    print("Answer: Cause the cow’s got the udders")
                    
                    
def satisfaction():
    """This part of the fucntion askes for a user satisfaction rating (int 1-10) based off of jokes given.
    If satisfaction rating is less than or equan to three code will return apology print 
    statement and ask for suggestions on how to make jokes funnier. If satisfaction rating is greater than
    three acknolwdgement print statements are returned.
    
    PARAMETERS
    ----------
    none
    
    RETURNS
    -------
    none
    """      
    
    # takes satisfation rating and returns corresponding print staments.
    
    global name, counter, lst
    num = ""
    
    while not num.isnumeric():
        num = input("\nOn a scale of 1-10 (1 meaning not satisfied at all and 10 meaning completly satisfied),\n"
        "how satisfied are you with the jokes you given, based off of the\n" 
        "level of funniness you chose?: ")
        
        if not num.isnumeric(): 
            print("\nplease input only int.")
    
    if int(num) >= 7 : 
        print("\nAmazing, I am so very glad to hear that you were satisfied with the jokes!\n"
               "I hope you have a great rest of your day " + name + "!")
        
    elif int(num) >= 4: 
        print("\nAwesome, " + name + " I am happy to hear the jokes provided to you did the job!\n"
               "Enjoy the rest of your day!")
        
    else: 
        print("\n" + name + ", I am so sorry the jokes were not satisfactory! I will try better next time!\n"
               "Make the rest of your day a good one!\n")
        sug = input("Please provide a suggestion on how I can be funnier: ") 
        lst.append(sug)
        
        for elm in lst:
            print(elm)
            
    counter += 1
    
    if counter != 10: 
    
        start()
