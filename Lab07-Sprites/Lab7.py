import random
import arcade
import os 

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.1
SPRITE_SCALING_ROCKS = 0.1
COIN_COUNT = 40
ROCK_COUNT = 70

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800


class Coin(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0
        self.angle = 0 

    def update(self):

        # Move the coin
        self.center_y -= 2
        self.angle += 2
        if self.center_y < -20 :
            self.center_y = SCREEN_HEIGHT + 20 
        if self.angle > 359:
            self.angle -= 360
class Rock(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.angle += 2
        self.center_x -= 2 
        if self.center_x < -20 :
            self.center_x = SCREEN_WIDTH + 20 
        if self.angle > 359:
            self.angle -= 360


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Prueba-sprites.py")

        os.chdir("d:/COSAS/UNIVERSIDAD/Segundo-Cuatri/Videojuegos/Prueba-sprites")

        self.player_list = None
        self.coin_list = None
        self.rock_list = None

        
        self.player_sprite = None
        self.score = 2

        
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.rock_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range(COIN_COUNT):

            
            coin = Coin("coin.png", SPRITE_SCALING_COIN)

            
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            coin.change_x = 0
            coin.change_y = -3

            
            self.coin_list.append(coin)
        for i in range(ROCK_COUNT):

            rock = Rock("rock.png", SPRITE_SCALING_COIN)

            rock.center_x = random.randrange(SCREEN_WIDTH)
            rock.center_y = random.randrange(SCREEN_HEIGHT)
            rock.change_x = -3
            rock.change_y = 0

            self.rock_list.append(rock)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()
        self.rock_list.draw()
        if self.score >=0 and self.score < 30:
            output = f"Score: {self.score}"
            arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        elif self.score >= 30:
            arcade.draw_text("YOU WIN THE GAME ", 50, 20, arcade.color.WHITE, 32)
        else:
            arcade.draw_text("GAME OVER ", 50, 20, arcade.color.WHITE, 32)
        

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """

    
        if self.score >= 0 and self.score < 30 :
            self.coin_list.update()
            self.rock_list.update()

            hit_list = arcade.check_for_collision_with_list(self.player_sprite,self.coin_list)
            hit_list1 = arcade.check_for_collision_with_list(self.player_sprite,self.rock_list)
            for coin in hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1
            for rock in hit_list1:
                rock.remove_from_sprite_lists()
                self.score -= 1
        





def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()