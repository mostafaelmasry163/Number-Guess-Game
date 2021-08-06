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

    def validate_and_play(self, user_in, ran_num, try_count=0):
        inputs_list = []
        condition = True
        while condition:
            if user_in.isdigit():
                if (0 <= int(user_in) <= 100) and int(user_in) not in inputs_list:
                    try_count += 1
                    inputs_list.append(int(user_in))
                    if int(user_in) > ran_num:
                        print(f"you are higher than the target , Number of tries is = {try_count}")

                        if try_count < self.max_tries:
                            user_in = self.get_user_input()
                        else:
                            print(f"the number was {ran_num}")
                            self.loser_play_again()
                            self.game_count += 1
                            self.lost_count += 1
                            condition = False
                    elif int(user_in) < ran_num:
                        print(f"you are lower than the target, Number of tries is = {try_count}")
                        if try_count < self.max_tries:
                            user_in = self.get_user_input()
                        else:
                            print(f"the number was {ran_num}")
                            self.loser_play_again()
                            self.game_count += 1
                            self.lost_count += 1
                            condition = False
                    elif int(user_in) == ran_num:
                        print(f"that's it, well done, Congratulation \n"
                              f"you made it in {try_count} tries")
                        self.game_count += 1
                        self.winning_count += 1
                        self.winner_play_again(try_count)
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

    def winner_play_again(self,try_count):  # toka
        if try_count<10:
            print("You Still Have Tries,Let's Challenge Again")
            ran_num = self.generate_random_num()
            inp = self.get_user_input()
            self.validate_and_play(inp, ran_num,try_count)
            
    def loser_play_again(self):  # mostafa
        print("that was your last try")
        print('you lost')
        answer = input('play again?(Y/N): ')
        if answer.upper() == 'Y':
            #play again
            ran_num = self.generate_random_num()
            inp = self.get_user_input()
            self.validate_and_play(inp, ran_num)
        elif answer.upper() == 'N':
            #close the game
            return
        else:
            print('invalid input')

    def welcome_and_print():  # Nour
        game_file = open("E:\game.txt", "r+") #adding file name or path
        (game_file.readable())
        for x in game_file.readlines():
            print(x)

        game_file.close()
        

    def save_player_data(self):  # Nour
        g = self.game_count
        w = self.winning_count
        l = self.lost_count 
        game_file = open("E:\game.txt", "r+") #adding file name or path
        game_file.write("Number of played games = " + str(g))
        game_file.write("\nNumber of wins = " + str(w))
        game_file.write("\nNumber of losses = " + str(l))

        game_file.close()
        


new_game = Game(1, 1, 1)
ran_num = new_game.generate_random_num()
inp = new_game.get_user_input()
new_game.validate_and_play(inp, ran_num)
