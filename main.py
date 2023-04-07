@namespace
class SpriteKind:
    GUI = SpriteKind.create()

def on_on_score():
    game.game_over(True)
info.on_score(100, on_on_score)

def startUp():
    global playerEntity, fish
    game.set_game_over_scoring_type(game.ScoringType.HIGH_SCORE)
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
    MakeyMakey.set_simulator_keymap(MakeyMakey.PlayerNumber.ONE,
        MakeyMakey.MakeyMakeyKey.UP,
        MakeyMakey.MakeyMakeyKey.DOWN,
        MakeyMakey.MakeyMakeyKey.LEFT,
        MakeyMakey.MakeyMakeyKey.RIGHT,
        MakeyMakey.MakeyMakeyKey.SPACE,
        MakeyMakey.MakeyMakeyKey.RIGHT_CLICK)

def on_on_overlap(sprite, otherSprite):
    global fish
    sprites.destroy(otherSprite)
    fish = sprites.create(assets.image("""
        fishSkin1
    """), SpriteKind.food)
    fish.set_position(randint(0, 151), randint(0, 111))
    info.change_score_by(randint(1, 5))
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

fish: Sprite = None
playerEntity: Sprite = None
startUp()
music.play(music.melody_playable(music.ba_ding),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)
game.show_long_text("A TebiBit Studios Production", DialogLayout.FULL)
game.splash("Great White Shark Simulator", "Press A To Play")

def on_forever():
    fish.set_position(randint(0, 151), randint(0, 111))
    pause(2000)
forever(on_forever)
