import time
from plyer import notification

nominee1 = input("Enter nominee 1 name: ")
nominee2 = input("Enter nominee 2 name: ")

nom_1_votes = 0
nom_2_votes = 0

voters_id= [21,31,41,51]
no_of_voter =len(voters_id)


while True:
    if voters_id == []:
        print("voting session over")
        if nom_1_votes > nom_2_votes:
            percentage = (nom_1_votes/no_of_voter)*100
            print(nominee1, "has won with ", percentage,"% votes")
            notification.notify(
                title = "ALERT!!!",
                message = f"{nominee1}, has won with, {percentage},% votes",
                app_name = "Voting System App",
                timeout = 10
            )
            break
        elif nom_2_votes> nom_1_votes:
            percentage = (nom_2_votes/no_of_voter)*100
            print(nominee2, "has won with ", percentage,"% votes")
            notification.notify(
                title = "ALERT!!!",
                message = f"{nominee2}, has won with , {percentage},% votes",
                app_name = "Voting System App",
                timeout = 10
            )
            break
    else:
        voter = int(input("Voter's ID:  "))
        if voter in voters_id:
            print("You are registered")
            voters_id.remove(voter)
            vote = int(input("Who are you voting for? 1 or 2 "))
            if vote == 1:
                nom_1_votes += 1
                print("successfully")
            elif vote == 2:
                nom_2_votes += 1
                print("successfully")
            else:
                print("Invalid input")
                vote = int(input("Who are you voting for? 1 or 2 "))
        else:
            print("You are not registered or you have voted")