import random


class Game:

    def __init__(self, game_count, winning_count, lost_count):
        self.user_input = ""
        self.game_count = game_count
        self.winning_count = winning_count
        self.lost_count = lost_count
        self.max_tries = 10

    def generate_random_num(self):
        x = random.randint(0, 100)
        return int(x)

    def get_user_input(self):
        self.user_input = input("Enter your guess number between 0 and 100 :   ")
        return self.user_input

    def validate_and_play(self, user_in, ran_num):
        inputs_list = []
        try_count = 0
        condition = True
        while condition:
            if user_in.isdigit():
                if (0 <= int(user_in) <= 100) and int(user_in) not in inputs_list:
                    try_count += 1
                    inputs_list.append(int(user_in))
                    if int(user_in) > ran_num:
                        print(f"you are higher than the target , Number of tries is = {try_count}")

                        if try_count <= self.max_tries:
                            user_in = self.get_user_input()
                        else:
                            print("that was your last try")
                            self.game_count += 1
                            self.lost_count += 1
                            condition = False
                    elif int(user_in) < ran_num:
                        print(f"you are lower than the target, Number of tries is = {try_count}")
                        if try_count <= self.max_tries:
                            user_in = self.get_user_input()
                        else:
                            print("that was your last try")
                            self.game_count += 1
                            self.lost_count += 1
                            condition = False
                    elif int(user_in) == ran_num:
                        print(f"that's it, well done, Congratulation \n"
                              f"you made it in {try_count} tries")
                        self.game_count += 1
                        self.winning_count += 1
                        condition = False
                elif int(user_in) in inputs_list:
                    print("you entered this number before, try again")
                    user_in = self.get_user_input()
                elif (int(user_in) > 100) or (int(user_in) < 0):
                    print("your number must be between 0 and 100")
                    user_in = self.get_user_input()

            else:
                print("invalid, your input must be number and between 0 and 100")
                user_in = self.get_user_input()

    def winner_play_again(self):  # toka
        print("")

    def loser_play_again(self):  # mostafa
        print("")

    def welcome_and_print(self):  # Nour
        print("")

    def save_player_data(self):  # Nour
        print("")


new_game = Game(1, 1, 1)
ran_num = new_game.generate_random_num()
inp = new_game.get_user_input()
new_game.validate_and_play(inp, ran_num)
