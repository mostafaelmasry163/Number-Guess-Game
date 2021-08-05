import random


class Game:

    def __init__(self, game_count):
        self.user_input = ""
        self.game_count = game_count

    def generate_random_num(self):
        x = random.randint(0, 100)
        return int(x)

    def get_user_input(self):
        self.user_input = input("Enter your guess number between 0 and 100 :   ")
        return self.user_input

    def validate_user_input(self, user_in, ran_num):
        try_count = 0
        condition = True
        while condition:
            if user_in.isdigit():
                if 0 <= int(user_in) <= 100:
                    try_count += 1
                    if int(user_in) > ran_num:
                        print(f"you are higher than the target , Number of tries is = {try_count}")
                        if try_count < 10:
                            user_in = self.get_user_input()
                        else:
                            print("that was your last try")
                            self.game_count += 1
                            condition = False
                    elif int(user_in) < ran_num:
                        print(f"you are lower than the target, Number of tries is = {try_count}")
                        if try_count < 10:
                            user_in = self.get_user_input()
                        else:
                            print("that was your last try")
                            self.game_count += 1
                            condition = False
                    elif int(user_in) == ran_num:
                        print(f"that's it, well done, Congratulation \n"
                              f"you made it in {try_count} tries")
                        self.game_count += 1
                        condition = False
                else:
                    print("your number must be between 0 and 100")
                    user_in = self.get_user_input()

            else:
                print("invalid, your input must be number")
                user_in = self.get_user_input()

new_game = Game(1)
ran_num = new_game.generate_random_num()
inp = new_game.get_user_input()
new_game.validate_user_input(inp,ran_num)