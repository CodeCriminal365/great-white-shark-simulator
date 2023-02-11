def on_on_score():
    game.game_over(True)
info.on_score(100, on_on_score)

def on_on_overlap(sprite, otherSprite):
    global fish
    sprites.destroy(otherSprite)
    info.change_score_by(randint(1, 5))
    fish = sprites.create(assets.image("""
        fishSkin1
    """), SpriteKind.food)
    fish.set_position(randint(0, 151), randint(0, 111))
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

fish: Sprite = None
game.set_game_over_scoring_type(game.ScoringType.HIGH_SCORE)
game.splash("Great White Shark Simulator", "Press A To Play")
scene.set_background_image(assets.image("""
    ocean
"""))
playerEntity = sprites.create(assets.image("""
    shark
"""), SpriteKind.player)
fish = sprites.create(assets.image("""
    fishSkin1
"""), SpriteKind.food)
playerEntity.set_stay_in_screen(True)
fish.set_stay_in_screen(True)
controller.move_sprite(playerEntity, 50, 50)

def on_forever():
    fish.set_position(randint(0, 151), randint(0, 111))
    pause(2000)
forever(on_forever)
