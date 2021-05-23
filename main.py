def on_player1_button_up_pressed():
    Player1.y += -10
controller.player1.on_button_event(ControllerButton.UP,
    ControllerButtonEvent.PRESSED,
    on_player1_button_up_pressed)

def on_player1_button_right_pressed():
    Player1.x += 10
controller.player1.on_button_event(ControllerButton.RIGHT,
    ControllerButtonEvent.PRESSED,
    on_player1_button_right_pressed)

def on_player1_button_left_pressed():
    Player1.x += -10
controller.player1.on_button_event(ControllerButton.LEFT,
    ControllerButtonEvent.PRESSED,
    on_player1_button_left_pressed)

def on_player1_button_down_pressed():
    Player1.y += 10
controller.player1.on_button_event(ControllerButton.DOWN,
    ControllerButtonEvent.PRESSED,
    on_player1_button_down_pressed)

def on_on_overlap(sprite, otherSprite):
    Player1.set_position(0, 0)
    Enemy1.set_position(135, 112)
    music.power_down.play()
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

Enemy1: Sprite = None
Player1: Sprite = None
info.set_life(3)
Player1 = sprites.create(assets.image("""
    MainCharacter
"""), SpriteKind.player)
Enemy1 = sprites.create(assets.image("""
    MainEnemy
"""), SpriteKind.enemy)
Player1.set_position(0, 0)
Enemy1.set_position(135, 112)
for index in range(3):
    Enemy1.follow(Player1, 5)