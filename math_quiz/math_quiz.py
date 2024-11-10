import random


def function_A(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)


def function_B():
    return random.choice(['+', '-', '*'])


def function_C(n1, n2, o):
    p = f"{n1} {o} {n2}"
    if o == '+': 
        a = n1 + n2
    elif o == '-': 
        a = n1 - n2
    else: 
        a = n1 * n2
    return p, a

def math_quiz():
    s = 0
    q = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(q):
        n1 = function_A(1, 10); n2 = function_A(1, 5); o = function_B()

        PROBLEM, ANSWER = function_C(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")

        while True:
            try:
                useranswer = int(input("Your answer:"))
                break
            except ValueError:
                print("Please type your answer in integer")

        # useranswer = input("Your answer: ") #takes user's answer
        # useranswer = int(useranswer) #converts to integer
        

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{q}")

if __name__ == "__main__":
    math_quiz()
