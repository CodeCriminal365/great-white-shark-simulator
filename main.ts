namespace SpriteKind {
    export const GUI = SpriteKind.create()
}
info.onScore(100, function () {
    game.gameOver(true)
})
function startUp () {
    game.setGameOverScoringType(game.ScoringType.HighScore)
    scene.setBackgroundImage(assets.image`ocean`)
    playerEntity = sprites.create(assets.image`shark`, SpriteKind.Player)
    fish = sprites.create(assets.image`fishSkin1`, SpriteKind.Food)
    playerEntity.setStayInScreen(true)
    fish.setStayInScreen(true)
    controller.moveSprite(playerEntity, 50, 50)
    MakeyMakey.setSimulatorKeymap(
    MakeyMakey.PlayerNumber.ONE,
    MakeyMakey.MakeyMakeyKey.UP,
    MakeyMakey.MakeyMakeyKey.DOWN,
    MakeyMakey.MakeyMakeyKey.LEFT,
    MakeyMakey.MakeyMakeyKey.RIGHT,
    MakeyMakey.MakeyMakeyKey.SPACE,
    MakeyMakey.MakeyMakeyKey.RIGHT_CLICK
    )
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    sprites.destroy(otherSprite)
    fish = sprites.create(assets.image`fishSkin1`, SpriteKind.Food)
    fish.setPosition(randint(0, 151), randint(0, 111))
    info.changeScoreBy(randint(1, 5))
})
let fish: Sprite = null
let playerEntity: Sprite = null
startUp()
game.showLongText("A TebiBit Studios Production", DialogLayout.Full)
game.splash("Great White Shark Simulator", "Press A To Play")
forever(function () {
    fish.setPosition(randint(0, 151), randint(0, 111))
    pause(2000)
})
