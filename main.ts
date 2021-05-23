controller.player1.onButtonEvent(ControllerButton.Up, ControllerButtonEvent.Pressed, function () {
    Player1.y += -10
})
controller.player1.onButtonEvent(ControllerButton.Right, ControllerButtonEvent.Pressed, function () {
    Player1.x += 10
})
controller.player1.onButtonEvent(ControllerButton.Left, ControllerButtonEvent.Pressed, function () {
    Player1.x += -10
})
controller.player1.onButtonEvent(ControllerButton.Down, ControllerButtonEvent.Pressed, function () {
    Player1.y += 10
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    Player1.setPosition(69, 50)
    Enemy1.setPosition(135, 112)
    music.powerDown.play()
    info.changeLifeBy(-1)
})
let Enemy1: Sprite = null
let Player1: Sprite = null
info.setLife(3)
Player1 = sprites.create(assets.image`MainCharacter`, SpriteKind.Player)
Enemy1 = sprites.create(assets.image`MainEnemy`, SpriteKind.Enemy)
Player1.setPosition(69, 50)
Enemy1.setPosition(135, 112)
for (let index = 0; index < 3; index++) {
    Enemy1.follow(Player1, 5)
}
