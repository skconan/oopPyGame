import arcade

SCREEN_WIDTH = 1098
SCREEN_HEIGHT = 700

class Score:

    def __init__(self):
        self.score_bot, self.score_player = 0,0
        self.src_player = "images/p0.fw.png"
        self.src_bot = "images/p0.fw.png"
        self.update_img()

    def update_img(self):
        self.src_player = "images/p"+str(self.score_player)+".fw.png"
        self.src_bot = "images/b"+str(self.score_bot)+".fw.png"  
        self.player_text = arcade.Sprite(self.src_player)
        self.bot_text = arcade.Sprite(self.src_bot)
        self.player_text.set_position(SCREEN_WIDTH - 120 ,SCREEN_HEIGHT/2 + 100)
        self.bot_text.set_position(120,SCREEN_HEIGHT/2 + 100)

    def increase(self, character):
        if character == 'p':
            self.score_player += 1
        else:
            self.score_bot += 1
        self.update_img()

    def on_draw(self):
        self.player_text.draw()
        self.bot_text.draw()