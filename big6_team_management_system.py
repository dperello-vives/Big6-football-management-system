#Practice project
#Big 6 football team management system

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display_info(self):
        print(f"My name is {self.name}")
        print(f"I'm {self.age} years old")

class Player(Person):
    
    def __init__(self, name, age, position, goals, assists, matches_played):
        super().__init__(name,age)
        self.position = position
        self.goals = goals
        self.assists = assists
        self.matches_played = matches_played
        
    def display_info(self):  #polymorphism (method overriding)
        super().display_info()
        print(f"I play position {self.position}, I have {self.goals} goals and {self.assists} assists in {self.matches_played} matches.")
        
class Goalkeeper(Person):
    
    def __init__(self, name, age, position, saves, clean_sheets):
        super().__init__(name,age)
        self.position = position
        self.saves = saves
        self.clean_sheets = clean_sheets


    def display_info(self):  #polymorphism (method overriding)
        super().display_info()
        print(f"I play position {self.position}, I have {self.saves} saves and {self.clean_sheets} clean sheets") 

class Coach(Person):

    def __init__(self, name, age, years_experience):
        super().__init__(name,age)
        self.years_experience = years_experience

    def display_info(self):  #polymorphism (method overriding)
        super().display_info()
        print(f"I have {self.years_experience} years of experience")

class Match:
    def __init__(self, opponent, goals_for, goals_against):
        self.opponent = opponent
        self.goals_for = goals_for
        self.goals_against = goals_against

class Team:

    def __init__(self, name):
        self.name = name
        self.players = []
        self.goalkeepers = []
        self.coaches = []
        self.matches = []
        
    def display_squad(self):
        print("-" * 80)
        print(f"{self.name.upper()} SQUAD".center(80))
        print("-" * 80)
        print(f"{self.coaches[0].name} is the coach \n")
        print("Some outfield players are:")
        for player in self.players:
            print(player.name)
        print(f"\nThe goalkeeper is {self.goalkeepers[0].name}")
        
    def calculate_and_display_result(self):
        print("-" * 80)
        print(f"{self.name.upper()} MATCHES".center(80))
        print("-" * 80)
        counter = 0
        for match in self.matches:
            counter +=1
            print(f"MATCH {counter} \n")
            if match.goals_for > match.goals_against:
                print(f"{self.name} won against {match.opponent}")
            elif match.goals_for < match.goals_against:
                print(f"{self.name} lost against {match.opponent}")
            else:
                print(f"{self.name} drew with {match.opponent}")

            print(f"The score was {self.name} {match.goals_for} - {match.goals_against} {match.opponent}\n")

    def find_top_scorer(self):
        print("-" * 80)
        print(f"{self.name.upper()} TOP SCORER".center(80))
        print("-" * 80)
        top_scorer = self.players[0]
        for player in self.players:
            if player.goals > top_scorer.goals:
                top_scorer = player
        print(f"\tThe top scorer at {self.name} is {top_scorer.name} with {top_scorer.goals} goals")

    def sort_by_assists(self):  #BUBBLE SORT DESCENDING ORDER
        print("-" * 80)
        print(f"SORTING {self.name.upper()} ASSISTS IN DESCENDING ORDER".center(80))
        print("-" * 80)
        swapped = True
        while swapped:
            swapped = False
            for counter in range(0,(len(self.players) - 1)):
                if self.players[counter].assists < self.players[counter + 1].assists:
                    temp = self.players[counter]
                    self.players[counter] = self.players[counter + 1]
                    self.players[counter + 1] = temp
                    swapped = True
        for player in self.players:
            print(f"{player.name}: Assists: {player.assists}")

    def sort_by_age(self):  #INSERTION SORT DESCENDING ORDER
    #Imagine books on a shelf, you dont keep swapping books. you pull one out, slide other books along and put the book in the empty gap
        print("-" * 80)
        print(f"SORTING {self.name.upper()} AGES IN DESCENDING ORDER".center(80))
        print("-" * 80)
        for counter in range(1,len(self.players)):
            value = self.players[counter]
            index = counter
            while index > 0 and value.age > self.players[index - 1].age:
                self.players[index] = self.players[index - 1] #Move the previous player one place to the right.This creates an empty gap one position to the left.The player stored in 'value' has not been inserted yet.
                index = index - 1 #Index represents the current empty gap. Every time a player moves right, the gap moves one position left so index follows the gap.
            self.players[index] = value #inserts the player stored in "value" into the empty gap. 

        for player in self.players:
            print(f"{player.name}: Age {player.age}")
            
    def sort_by_matches_played(self): #Insertion sort players into ascending order of matches played
        for counter in range(1,len(self.players)):
            value = self.players[counter]
            index = counter
            while index > 0 and value.matches_played < self.players[index - 1].matches_played:
                self.players[index] = self.players[index - 1] 
                index = index - 1 
            self.players[index] = value
        

    def find_player_by_matches_played(self): #BINARY SEARCH
        print("-" * 80)
        print(f"FINDING A PLAYER IN {self.name.upper()} BY MATCHES PLAYED".center(80))
        print("-" * 80)
        #Binary Search only works on sorted data so we have to run an insertion sort before
        self.sort_by_matches_played()

        #Binary search here
        print("Players in this team have made the following numbers of appearances:\n")
        for player in self.players:
            print(player.matches_played)
        print("\n")
            
        while True:
            try:
                target = int(input("Enter the number of appearances to search for: "))
                break
            except ValueError:
               print("\nPlease enter a number")

        low = 0
        high = (len(self.players) - 1)
        found = False
        while low <= high:
            middle = (low + high) // 2 #// means whole number division
            
            if target == self.players[middle].matches_played:
                print(f"{self.players[middle].name} has played {self.players[middle].matches_played} matches.")
                found = True
                break
            elif target > self.players[middle].matches_played:
                low = middle + 1
            else:
                high = middle - 1

        if not found:
            print("No player was found with that number of matches played.")
            while True:
                print("\n1. Try again")
                print("2. Return to the main menu")

                choice = input("Choose an option: ")

                if choice == "1":
                    self.find_player_by_matches_played()
                    return

                elif choice == "2":
                    return

                else:
                    print("Please choose 1 or 2.")

def get_team(filename):
    entire_file = open(filename,"r")
    lines_array = entire_file.read().splitlines()
    entire_file.close()

    team = None

    for line in lines_array: #loop checks evry line

        line_parts = line.split(",") #splits the current line
        record_type = line_parts[0] #stores the type of object (player or coach etc..)

        if record_type == "TEAM":
            team = Team(line_parts[1]) #the same as arsenal = Team("Arsenal") f.e
            #After this all players can get appended to the team so it has to be the first line in the file

        elif record_type == "COACH":
            current_coach = Coach(
                line_parts[1],
                int(line_parts[2]),
                int(line_parts[3])
            )

            team.coaches.append(current_coach)

        elif record_type == "GOALKEEPER":
            current_goalkeeper = Goalkeeper(
                line_parts[1],
                int(line_parts[2]),
                line_parts[3],
                int(line_parts[4]),
                int(line_parts[5])
            )

            team.goalkeepers.append(current_goalkeeper)

        elif record_type == "PLAYER":
            current_player = Player(
                line_parts[1],
                int(line_parts[2]),
                line_parts[3],
                int(line_parts[4]),
                int(line_parts[5]),
                int(line_parts[6])
            )  #instead of manually typing in the data it gets the data from the file

            team.players.append(current_player) #appends current player to the array of players

        elif record_type == "MATCH":
            current_match = Match(
                line_parts[1],
                int(line_parts[2]),
                int(line_parts[3])
            )

            team.matches.append(current_match)

    return team

#USER
while True:
    print("=" * 80)
    print("BIG 6 TEAM MANAGEMENT SYSTEM".center(80))
    print("=" * 80)


    print("\n")
    print("-" * 80)
    print("TEAMS".center(80))
    print("-" * 80)
    print("1. Arsenal")
    print("2. Liverpool")
    print("3. Manchester City")
    print("4. Manchester United")
    print("5. Chelsea")
    print("6. Tottenham")
    print("7. Exit")
    while True:
        try:
            team_choice = int(input("\nChoose a team (Using number): "))
            break
        except ValueError:
           print("\nPlease enter a number")

    if team_choice == 1:
        arsenal = get_team("arsenal.txt")
        team = arsenal

    elif team_choice == 2:
        liverpool = get_team("liverpool.txt")
        team = liverpool

    elif team_choice == 3:
        man_city = get_team("man_city.txt")
        team = man_city

    elif team_choice == 4:
        man_utd = get_team("man_utd.txt")
        team = man_utd

    elif team_choice == 5:
        chelsea = get_team("chelsea.txt")
        team = chelsea

    elif team_choice == 6:
        tottenham = get_team("tottenham.txt")
        team = tottenham

    elif team_choice == 7:
        print("Thank you for using the program.")
        break
    else:
        print("Invalid team choice.")
        continue

    while True:
        print("\n" + "=" * 80)
        print(f"{team.name.upper()} MENU".center(80))
        print("=" * 80)
    
        print("1. Display squad")
        print("2. Match results")
        print("3. Top scorer")
        print("4. Sort players by assists (Bubble sort)")
        print("5. Sort players by age (Insertion sort)")
        print("6. Sort players by matches played (Insertion sort)")
        print("7. Find a player by their matches played (Binary Search)")
        print("8. Swap team")
        print("9. Exit")
        while True:  #keeps going until a break
            try:
                choice = int(input("\nChoose a option (Using number): "))
                break
            except ValueError:
                print("\nPlease enter a number")


        if choice == 1:
            team.display_squad()
            input("\nPress Enter to return to the menu.")
        elif choice == 2:
            team.calculate_and_display_result()
            input("\nPress Enter to return to the menu.")
        elif choice == 3:
            team.find_top_scorer()
            input("\nPress Enter to return to the menu.")
        elif choice == 4:
            team.sort_by_assists()
            input("\nPress Enter to return to the menu.")
        elif choice == 5:
            team.sort_by_age()
            input("\nPress Enter to return to the menu.")
        elif choice == 6:
            print("-" * 80)
            print(f"SORTING {team.name.upper()} BY MATCHES PLAYED IN ASCENDING ORDER".center(80))
            print("-" * 80)
            team.sort_by_matches_played()
            for player in team.players:
                print(f"{player.name}: Matches played: {player.matches_played}")
            input("\nPress Enter to return to the menu.")
        elif choice == 7:
            team.find_player_by_matches_played()
            input("\nPress Enter to return to the menu.")
        elif choice == 8:
            break
        elif choice == 9:
            print("Thank you for using the program.")
            quit()
        else:
            print("Invalid option.")


    
