allQuestions = [
    ["Which is the capital of Karantaka?", "Bengaluru",
        "Mysuru", "Mangaluru", "Tumkuru", 1],
    ["How many states are there in India?", "28", "30", "27", "29", 1],
    ["Which city is known as 'Silicon Valley of India'?",
        "Mysuru", "Mangaluru", "Tumkuru", "Bengaluru", 4],
    ["Which is the most useless degree in India?",
        "BCA", "BBA", "Engineering", "Diploma", 3],
    ["How many 'Jnanapeet' has Karnataka won so far(as of 2023)?",
     "7", "8", "9", "10", 2],
    ["Which state in India provide best bus service to the public?",
        "Goa", "Maharashtra", "Karnataka", "Telangana", 3],
    ["Which actor is known as 'Power Star' in Karnataka film industry?",
        "Appu", "Shivanna", "Dboss", "Rocking star", 1],
    ["Who is father of maths in India?", "Aryabhatta",
        "Govindbhatta", "SureshBhatta", "RameshBhatta", 1],
    ["Which is the capital of India?", "Mumbai", "Hyderabad", "Delhi", "Bengaluru"],
    ["Who are the founders of Microsoft?", "Bill Gates and Paul Allen", "Jeffrey Preston Bezos",
        "Steve Jobs, Steve Wozniak, and Ronald Wayne", "Shane Watson and Smith", 1],
    ["Which is the favorite movie of most of the engineering students?",
        "KGF Chapter-1", "3 idiots", "4 idiots", "KGF Chapter-2"],
    ["Who is known as 'Father of Indian Constitution'?", "Mahatma Gandhiji",
        "Dr. Rajendra Prasad", "Dr. B.R. Ambedkar", "Jawaharlal Nehru", 3],
    ["Who is the first Prime Minister of India?", "Mahatma Gandhiji",
        "Dr. Rajendra Prasad", "Dr. B.R. Ambedkar", "Jawaharlal Nehru", 4],
    ["Who is the first President of India?", "Mahatma Gandhiji",
        "Dr. Rajendra Prasad", "Dr. B.R. Ambedkar", "Jawaharlal Nehru", 2],
    ["What is the value of sin90", "1", "0.5", "0.45", "0.65", 1]
]

amount = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000,
          160000, 320000, 625000, 1250000, 2500000, 5000000, 10000000]

totalAmount = 0
i = 0
for i in range(0, len(allQuestions)):
    print(f"\n****Question for Rs. {amount[i]}**** \n{allQuestions[i][0]}")
    print(
        f"The options are\na. {allQuestions[i][1]}\nb. {allQuestions[i][2]}\nc. {allQuestions[i][3]}\nd. {allQuestions[i][4]}")
    choosedOption = ord(input("Enter your option: "))-96
    # print(choosedOption, allQuestions[i][4])
    if (choosedOption == allQuestions[i][5]):
        print("Correct answer.......!!!!!")
        print(f"You have won Rs.{amount[i]}")
        totalAmount = amount[i]
        print("Total amount won is", totalAmount)
        print("\nDo you wish to continue to play?\nEnter 'Y' if you want to continue. Otherwise enter 'N'")
        if (input("Enter your choice: ") != 'Y'):
            break
    else:
        print("You have answered wrong......!\nYou are out of quiz.....")
        if (i < 4):
            totalAmount = 0
        elif (i < 9):
            totalAmount = 10000
        else:
            totalAmount = 320000
        break

if (totalAmount > 0):
    print("\nCongratulations on winning", totalAmount)
else:
    print("Better luck next time....")
