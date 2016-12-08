import importlib

topics = [
    "Print",
    "Variables",
    "Inputs",
    "If Statements and Indentation",
    "While and For loops"]

#advancedTopics = [
    #"Formatting",
    #"Functions"]
lentopic = len(topics)
hide = 37 - lentopic

def main():
    for x in range(lentopic):
        print(str(x+1) + ") " + topics[x])
    try:
        while True:
            userinput = input("Pick a topic number: ")
            if userinput in range(1,lentopic):
                print("\n"*39)
                userinput = topics[userinput-1]
                break
            else:
                print("Please input a number within 1 and {}".format(lentopic))
            i = importlib.import_module(topics[int(userinput)-1])
            i.lesson("lesson1")
            
    except KeyboardInterrupt:
        print("You have quit the lesson")
        print("\n"*hide)
        
if __name__ == "__main__":
    main()
