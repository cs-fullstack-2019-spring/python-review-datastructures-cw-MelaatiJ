def main():
#   problem1()
#   problem2()




def problem1():
    nameList= []
    userInput = ""
    while userInput.lower() != "quit":
        nameList.append(userInput)
        userInput = input("What are your favorite Pokeman? If you dont like Pokeman or just dont have anymore enter 'quit\n'")
        print(nameList)




# * Create a function that has a loop that quits with ```q```
#     * Allow the User to enter names until ```q``` is entered
# * Add each name entered to a List
# * When the User enters ```q``` print the list of names
#
# ADDITIONAL REQUIREMENTS:
# * Your code should be able to process the quit command (q) the User enters regardless of case











def problem2():
    userInput = ""
    myDictionaryList = [
        {
            "name": "Kelvin",
            "age": 30
        },
        {
            "name": "Bob",
            "age": 50
        },
        {
            "name": "Alex",
            "age": 21
        }
    ]
    for elememnt in myDictionaryList:
        print(elememnt)

    print(myDictionaryList[0])
    print(myDictionaryList[1])
    print(myDictionaryList[2])
        (e)
    returnllen(e)
    def getSortkey
    while userInput.lower() != "age" or userInput.lower() != "name":
        userInput = ("Enter 'age' or 'name' on how you want to sort the dictionary")
    if userInput == "age":
        myDictionaryList.sort(key=getsortkey)





# 1. Prints a formatted list of names and ages
# 2. Prompts the User for which property they want to use to sort the list (e.g. ```AGE``` or ```NAME```).
# Print the formatted list of names and ages sorted by the specified sort criteria.
#
# 3. Continue prompting the User for the sort criteria and print a sorted list until the User enters ```q``` then exit.
#
# ADDITIONAL REQUIREMENTS:
# * Your code should be able to process the sort criteria the User enters regardless of case
# * Your code should be able to process the quit command (q) the User enters regardless of case
# * If the User enters something other than ```q``` or a valid sort criteria (e.g. ```AGE``` or ```NAME```)
# your code should display ```INVALID ENTRY. PLEASE TRY AGAIN``` and continue the process.










if __name__ == '__main__':
    main()