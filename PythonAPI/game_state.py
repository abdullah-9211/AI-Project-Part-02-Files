from player import Player

class GameState:

    def __init__(self, input_dict):

        self.dict_to_object(input_dict)

    def dict_to_object(self, input_dict):

        self.player1 = Player(input_dict['p1'])
        self.player2 = Player(input_dict['p2'])
        self.timer = input_dict['timer']
        self.fight_result = input_dict['result']
        self.has_round_started = input_dict['round_started']
        self.is_round_over = input_dict['round_over']
        
    def to_tuple(self):
        return (self.timer, self.fight_result, self.has_round_started, self.is_round_over, self.player1.player_id, self.player1.health, self.player1.x_coord, self.player1.y_coord, self.player1.is_jumping, self.player1.is_crouching, self.player1.is_player_in_move,  self.player1.move_id, self.player1.player_buttons.up, self.player1.player_buttons.down, self.player1.player_buttons.right, self.player1.player_buttons.left, self.player1.player_buttons.Y, self.player1.player_buttons.B, self.player1.player_buttons.X, self.player1.player_buttons.A, self.player1.player_buttons.L, self.player1.player_buttons.R, self.player2.player_id, self.player2.health, self.player2.x_coord, self.player2.y_coord, self.player2.is_jumping, self.player2.is_crouching, self.player2.is_player_in_move,  self.player2.move_id, self.player2.player_buttons.up, self.player2.player_buttons.down, self.player2.player_buttons.right, self.player2.player_buttons.left, self.player2.player_buttons.Y, self.player2.player_buttons.B, self.player2.player_buttons.X, self.player2.player_buttons.A, self.player2.player_buttons.L, self.player2.player_buttons.R)
    
    def tuple_without_p1Buttons(self):
        if self.fight_result == 'NOT_OVER':
            self.fight_result = 0
        elif self.fight_result == 'P1':
            self.fight_result = 1
        else:
            self.fight_result = -1
        
        return (self.timer, self.fight_result, self.has_round_started, self.is_round_over, self.player1.player_id, self.player1.health, self.player1.x_coord, self.player1.y_coord, self.player1.is_jumping, self.player1.is_crouching, self.player1.is_player_in_move,  self.player1.move_id, self.player2.player_id, self.player2.health, self.player2.x_coord, self.player2.y_coord, self.player2.is_jumping, self.player2.is_crouching, self.player2.is_player_in_move,  self.player2.move_id, self.player2.player_buttons.up, self.player2.player_buttons.down, self.player2.player_buttons.right, self.player2.player_buttons.left, self.player2.player_buttons.Y, self.player2.player_buttons.B, self.player2.player_buttons.X, self.player2.player_buttons.A, self.player2.player_buttons.L, self.player2.player_buttons.R)
    
    def tuple_without_p1Buttons2(self):
        if self.fight_result == 'NOT_OVER':
            self.fight_result = 0
        elif self.fight_result == 'P1':
            self.fight_result = 1
        else:
            self.fight_result = -1
        
        return (self.player1.player_id, self.player1.health, self.player1.is_crouching, self.player1.is_jumping, self.player1.is_player_in_move, self.player1.move_id, self.player1.x_coord, self.player1.y_coord, self.player2.player_id, self.player2.health, self.player2.is_crouching, self.player2.is_jumping, self.player2.is_player_in_move, self.player2.move_id, self.player2.x_coord, self.player2.y_coord, self.player2.player_buttons.up, self.player2.player_buttons.down, self.player2.player_buttons.right, self.player2.player_buttons.left, self.player2.player_buttons.select, self.player2.player_buttons.start, self.player2.player_buttons.Y, self.player2.player_buttons.B, self.player2.player_buttons.X, self.player2.player_buttons.A, self.player2.player_buttons.L, self.player2.player_buttons.R, self.timer, self.fight_result, self.has_round_started, self.is_round_over)
    