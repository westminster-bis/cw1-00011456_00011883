# On time? Yes - Output
# On time? No - Within 24 hours? Yes - Late submission? Is there a valid reason? No - Output
# On time? No - Within 24 hours? Yes - Late submission? Is there a valid reason? Yes - Accepted MC? Output
# On time? No - Within 24 hours? No - Submitted within 5 days? No - Is there a valid reason with MC non submission? No | Yes - Output
# On time? No - Within 24 hours? No - Submitted within 5 days? Yes - Is there a valid reason with MC submission? No - Output
# On time? No - Within 24 hours? No - Submitted within 5 days? Yes - Is there a valid reason with MC submission? Accepted? No | Yes - Output

outputs = ["Full Mark", "Mark = 0", "Minus 10 marks from overall mark but not below 40"]
questions = [
    "Course work submitted on time? ",
    "Within 24 hours? ",
    "Is there a valid reason? ",
    "Accepted MC Claim for within 24 hour? ",
    "Submitted within 5 days? ",
    "Is there a valid reason? ",
    "Is there a valid reason? ",
    "Accepted MC Claim? ",
    "Accepted MC Claim? ",
]

# the first value in each tuple is the value corresponding to a True answer,
# the second value in each tuple corresponds to a False answer
outcomes = [
    ("Full Mark", 1),
    (2, 4),
    (3, "Minus 10 marks from overall marks but not below 40"),
    ("Full Mark", "Minus 10 marks from overall marks but not below 40"),
    (5, 6),
    (7, "Mark = 0"),
    (8, "Mark = 0"),
    ("Full Mark", "Mark = 0"),
    ("Deferral reassessment", "Mark = 0"),
]

question_num = 0

def change(i):
    return outcomes[question_num][i]

# Ask till one of the outputs will not be printed
def run():
    global question_num
    while True:
        print(f"\n# {questions[question_num]} #")

        while True:
            answer = input("Any charachter - Yes | Just Click Enter Button - No: ").lower().strip()
            if answer in ("yes", "no"):
                break

        if answer == "yes":
            outcome = change(0)
        elif answer == "no":
            outcome = change(1)

        # Print the output according to the story and stop asking
        if type(outcome) == str:
            print(outcome)
            if input("Do you want to try again? ").strip() == "yes":
                question_num = 0
                run()
            break
        else:
            question_num = outcome

run()