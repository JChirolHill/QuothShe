import requests
import random
import os

fileOut = open("quote.txt", "a")
quoteList = []
fileOut = open("quote.txt", "r")
for line in fileOut:
    # print(line)
    line = line.strip()
    quoteList.append(line)

buffer = []

# # returns a random hardcoded quote
# def getRandomQuote():
#     # just for testing purposes, returns a quote
#     quotes = ["Perhaps it's impossible to wear an identity without becoming what you pretend to be.", "In the moment when I truly understand my enemy, understand him well enough to defeat him, then in that very moment I also love him. I think it’s impossible to really understand somebody, what they want, what they believe, and not love them the way they love themselves. And then, in that very moment when I love them.... I destroy them.", "If you try and lose then it isn't your fault. But if you don't try and we lose, then it's all your fault.", "I don't care if I pass your test, I don't care if I follow your rules. If you can cheat, so can I. I won't let you beat me unfairly - I'll beat you unfairly first.", "Remember, the enemy's gate is down."]
#     return random.choice(quotes)

# USES THE API VERSION OF GETTING QUOTES
def getRandomQuote():
    if(len(buffer) == 0): # get a new set of quotes if none left in buffer
        headers = {"Authorization": 'Token token=""'}
        response = requests.get("https://favqs.com/api/quotes", headers=headers)
        data = response.json()
        allQuotes = data["quotes"]
        for quoteItem in allQuotes:
            buffer.append(quoteItem["body"])

    return buffer.pop()

# Gets new quote and append to file
def newQuote():
    likeQuote = ""
    fileOut = open("quote.txt", "a")
    while likeQuote != "3":
        quote = getRandomQuote()
        print("\n" + quote)
        likeQuote = input("Do you like this quote? Please select an option:\n\t1. Go to the next quote \n\t2. Save and continue \n\t3. Return to main menu \n")
        while likeQuote != "1" and likeQuote != "2" and likeQuote != "3":
            print("Invalid input. Please try again :(")
            likeQuote = input("Do you like the quote? Please select an option:\n\t1. Go to the next quote \n\t2. Save and continue \n\t3. Return to main menu \n")
        if likeQuote == "2":
            if quote in quoteList:
                print("Already there!")
            else:
                print(quote, file = fileOut)
                quoteList.append(quote)
                print("Saved!")
    fileOut.close()

# prints one quote at a time and loops until user goes back to main menu
def viewSaved():
    fileOut = open("quote.txt", "a")
    choice = "1"
    while choice != "3":
        if choice != "1" and choice != "2":
            print("Invalid input. Please try again :(")
            choice = input("Please select an option: \n\t1. Next quote\n\t2. Delete this quote\n\t3. Return to main menu \n")
        else:
            if len(quoteList) == 0:
                print("No saved quotes, please go find some :)")
                break
            for quote in quoteList:
                print("\n" + quote)
                choice = input("Please select an option: \n\t1. Next quote\n\t2. Delete this quote\n\t3. Return to main menu \n")
                if choice == "2":
                    # deletes text file
                    os.remove("quote.txt")
                    quoteList.remove(quote)
                    # rewrite to the file based on our list
                    fileOut = open("quote.txt", "a")
                    for quote in quoteList:
                        print(quote + "\n", file = fileOut)
                    break;
                elif choice == "3":
                    break

        if choice == "3":
            break

    fileOut.close()

# displays the main menu
def main():
    mainChoice = ""
    while mainChoice != "3":
        mainChoice = input("Please select an option: \n\t1. Get New Quotes\n\t2. View Saved Quotes\n\t3. Quit \n")
        while mainChoice != "1" and mainChoice != "2" and mainChoice != "3":
            print("Invalid input. Please try again :(")
            mainChoice = input("Please select an option: \n\t1. Get New Quotes\n\t2. View Saved Quotes\n\t3.Quit \n")
        if mainChoice == "1":
            newQuote()
        elif mainChoice == "2":
            viewSaved()
    print("Bye :)")

main()
