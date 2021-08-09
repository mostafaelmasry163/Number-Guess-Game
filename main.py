from Game_module import Game

new_game = Game()
ran_num = new_game.generate_random_num()
inp = new_game.get_user_input()
new_game.validate_and_play(inp, ran_num)
new_game.save_player_data()