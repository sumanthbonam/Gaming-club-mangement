# File: main.py
from team_management import TeamManagement
from match_scheduling import MatchScheduling

def main():
    team_manager = TeamManagement()
    match_scheduler = MatchScheduling()

    while True:
        print("\n=== Gaming Club Management System ===")
        print("1. Create a Team")
        print("2. Delete a Team")
        print("3. View Teams")
        print("4. Schedule a Match")
        print("5. View Upcoming Matches")
        print("6. View Past Matches")
        print("7. View Live Matches")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")
        if choice == "1":
            team_name = input("Enter team name: ")
            print(team_manager.create_team(team_name))
        elif choice == "2":
            team_name = input("Enter team name to delete: ")
            print(team_manager.delete_team(team_name))
        elif choice == "3":
            teams = team_manager.view_teams()
            print("Teams:", teams)
            if teams:
                print("\nSelect an option:")
                print("1. Add Team Members")
                print("2. Update Team Member Details")
                print("3. Delete Team Member")
                team_choice = input("Enter your choice (1-3): ")
                team_name = input("Enter team name: ")
                if team_choice == "1":
                    num_members = int(input("How many members do you want to add? "))
                    for _ in range(num_members):
                        member_name = input("Enter member name: ")
                        member_id = input("Enter member ID: ")
                        print(team_manager.add_team_member(team_name, member_name, member_id))
                elif team_choice == "2":
                    member_id = input("Enter member ID: ")
                    new_name = input("Enter new member name: ")
                    print(team_manager.update_member_details(team_name, member_id, new_name))
                elif team_choice == "3":
                    member_id = input("Enter member ID to delete: ")
                    print(team_manager.delete_team_member(team_name, member_id))
                else:
                    print("Invalid choice.")
        elif choice == "4":
            team1 = input("Enter first team name: ")
            team2 = input("Enter second team name: ")
            match_date = input("Enter match date (YYYY-MM-DD): ")
            print(match_scheduler.create_match(team1, team2, match_date))
        elif choice == "5":
            print("Upcoming Matches:", match_scheduler.view_upcoming_matches())
        elif choice == "6":
            print("Past Matches:", match_scheduler.view_past_matches())
        elif choice == "7":
            print("Live Matches:", match_scheduler.view_live_matches())
        elif choice == "8":
            print("Khatam!...tata!.... Bye Bye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-8.")

if __name__ == "__main__":
    main()
