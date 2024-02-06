import sys


def start_quiz():
    print("****BASIC QUIZ GAME****")
    score = 0
    print("")
    print("Q.1 When was the third battle of Panipat fought?")
    print("A. 1761    B. 1736")
    print("C. 1757    D. 1710")
    a = input("Enter your answer(A,B,C or D):")
    if a == 'A':
        print("Correct Answer")
        score = score + 1
    else:
        print("Wrong Answer")
    print(" ")
    print("Q.2 Which is the capital of Australia?")
    print("A. Melbourne    B. Sydney")
    print("C. Canberra     D.Brisbane")
    b = input("Enter your answer(A,B,C or D):")
    if b == 'C':
        print("Correct Answer")
        score = score + 1
    else:
        print("Wrong Answer")
    print(" ")
    print("Q.3 When was the Khalsa Panth established?")
    print("A. 1699    B. 1695")
    print("C. 1709    D. 1689")
    c = input("Enter your answer(A,B,C or D):")
    if c == 'A':
        print("Correct Answer")
        score = score + 1
    else:
        print("Wrong Answer")
    print(" ")
    print("Your total score is:", score, "/3")
    print(" ")
    print("****THANK YOU FOR PLAYING****")
    print(" ")
    print("1. Play Again")
    print("2. Exit")
    i = int(input("Enter your choice(1 or 2):"))
    if i == 1:
        modified_quiz()
    elif i == 2:
        exit(1)


def modified_quiz():
    print("****BASIC QUIZ GAME****")
    score = 0
    print("")
    print("Q.1 Where are the headquarters of Samsung?")
    print("A. South Korea    B. Japan")
    print("C. China          D. U.S.A")
    a = input("Enter your answer(A,B,C or D):")
    if a == 'A':
        print("Correct Answer")
        score = score + 1
    else:
        print("Wrong Answer")
    print(" ")
    print("Q.2 Who is the C.E.O of Google?")
    print("A.Larry Page     B. Satya Nandela")
    print("C. Elon Musk     D. Sundar Pichai")
    b = input("Enter your answer(A,B,C or D):")
    if b == 'D':
        print("Correct Answer")
        score = score + 1
    else:
        print("Wrong Answer")
    print(" ")
    print("Q.3 When the Second World War ended?")
    print("A. 1945    B. 1946")
    print("C. 1944    D. 1947")
    c = input("Enter your answer(A,B,C or D):")
    if c == 'A':
        print("Correct Answer")
        score = score + 1
    else:
        print("Wrong Answer")
    print(" ")
    print("Your total score is:", score, "/3")
    print(" ")
    print("****THANK YOU FOR PLAYING****")
    print(" ")
    x = int(input("Enter 0 to exit:"))
    if x == 0:
        exit(1)



start_quiz()
