import datetime
number = 0
qn = 0
score = 0

######  Date  ######

date = datetime.datetime.now()
year = date.year
month = date.month
day = date.day
print("Date :",date.year,"/", date.month,"/",date.day,"AD")
# print(f"Date : {year} / {month} / {day} AD")
with open("quiz.txt", "a") as file :
    file.write(f"Date : {year} / {month} / {day} AD\n")

######  Name  ######

name = input("please enter your name : ")
last_name = input("please enter your last name : ")
print (" ")
with open("quiz.txt" , "a") as file :
    file.write(f"Name : {name} {last_name}\n\n")

######  Questions  ######

questions = {
    "A) Which one is list :\n1) o = {'a', 'b', 'c'}       2) o = ['a', 'b', 'c']\n3) o = ('a', 'b', 'c')       4) o = {'a' : 5, 'b' : 3}" : 2 ,
    "B) Which one is Exponent (Power) :\n1) *       2) %       3) //       4) **" : 4 ,
    "C) What will be the value of n :\nfruits = ('apple', 'banana', 'cherry', 'grape')\n(x, y, z, n) = fruits\n1) cherry       2)apple       3) grape       4) banana " : 3 ,
    "D) How to removes the element at the specified position (which array) :\n1) pop()       2) clear()       3) remove()       4) reverse()" : 1 ,
    "E) How to count the letters of a variable or the number of items in a list :\n1) extend()       2) len()       3) index()       4) count()" : 2 ,
    "F) What will be the output :\nmylist = ['a', 'b', 'a', 'c', 'c']\nmylist = list(dict.fromkeys(mylist))\nprint(mylist)\n1) ['a', 'b', 'c']                 2) ['a', 'c']\n3) ['a', 'b', 'a', 'c', 'c']       4) ['b']" : 1 ,
    "G) Which one is square root (after importing math) :\n1) math.floor()       2) math.ceil()       3) math.sqrt()       4) none" : 3 ,
    "H) What is the order of operators in Python :\n1) minus -> plus-division -> multiply -> power -> parentheses\n2) multiply -> division -> plus -> minus -> power -> parentheses\n3) parentheses -> power -> division -> multiply -> plus -> minus\n4) parentheses -> power -> multiply -> division -> plus -> minus" : 4 ,
    "I) How to display list from last to first : \n1) remove()        2) reverse()       3) insert()       4) sort()" : 2 ,
    "J) Which one is False : \n1) bool('  ')       2) bool(7)        3) bool('a')       4) bool('')" : 4 ,
}

######  Checking in  ######

while number >= 0 and number <= 9 :
        
    for z in range(9) :
        y = list(questions.keys())
        if qn == 10 :
            break
        x = y[qn]
        qn += 1
        print ("-" * 80)
        answer = int(input(f"{x}\nyour answer : "))
        a = True

        while a == True :

            if answer == questions[x] :
                score = score + 10
                number += 1
                with open("quiz.txt" , "a") as file :
                    file.write(f"{x}\nright answer : {questions[x]}\n{name}'s answer : {answer}    |    right\n")
                    file.write("-" * 80)
                    file.write("\n")
                    a = False

            elif answer != questions[x] :
                if answer == 1 or answer == 2 or answer == 3 or answer == 4 :
                    number += 1
                    with open("quiz.txt" , "a") as file :
                        file.write(f"{x}\nright answer : {questions[x]}\n{name}'s answer : {answer}    |    wrong\n")
                        file.write("-" * 80)
                        file.write("\n")
                        a = False

                else :
                    print ("Your answer should be between 1 and 4")
                    answer = int(input("try again : "))
                    a = True

######  Score  ######

print (f"your score : {score}%")

with open("quiz.txt" , "a") as file :
    file.write(f"\nScore : {score}%")

result = input("Do you want to see the result in more detail ? (y/n) ")
while True :
    if result == "y" :
        print (" ")
        with open("quiz.txt", "r") as file :
            read = file.read()
            print (read)
            break
    elif result == "n" :
        print ("OK")
        break
    else :
        print ("It's wrong !")
        result = input("Try again, Do you want to see the result in more detail ? (y/n) ")


end = input(" ")
