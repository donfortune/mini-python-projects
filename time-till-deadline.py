import datetime

user_input = input("enter your goal with a deadline separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
#calculate date to deadline
cureent_date = datetime.datetime.today()
time_till = deadline_date - cureent_date

print(f"Dear user! Time reamming for your goal: {goal} you made on: {deadline} is {time_till.days} days ")



