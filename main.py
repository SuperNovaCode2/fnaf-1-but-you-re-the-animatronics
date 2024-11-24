@namespace
class SpriteKind:
    snasobject = SpriteKind.create()
    papyrusobject = SpriteKind.create()

def on_overlap_tile(sprite, location):
    global Animatronic, Sans, Papyrus
    music.stop_all_sounds()
    music.set_volume(30)
    music.play(music.create_song(assets.song("""
            overworld song
        """)),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
    Animatronic = sprites.create(assets.image("""
        freddy 1
    """), SpriteKind.player)
    controller.move_sprite(Animatronic)
    scene.camera_follow_sprite(Animatronic)
    fnaf11()
    if Sans:
        sprites.destroy(Sans)
        music.stop_all_sounds()
        music.set_volume(30)
        music.play(music.create_song(assets.song("""
                overworld song
            """)),
            music.PlaybackMode.LOOPING_IN_BACKGROUND)
        Sans = sprites.create(assets.image("""
            Sans
        """), SpriteKind.player)
        controller.move_sprite(Sans)
        scene.camera_follow_sprite(Sans)
        fnaf11()
    if Papyrus:
        sprites.destroy(Papyrus)
        music.stop_all_sounds()
        music.set_volume(30)
        music.play(music.create_song(assets.song("""
                overworld song
            """)),
            music.PlaybackMode.LOOPING_IN_BACKGROUND)
        Papyrus = sprites.create(assets.image("""
            Papyrus
        """), SpriteKind.player)
        controller.move_sprite(Papyrus)
        scene.camera_follow_sprite(Papyrus)
        fnaf11()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        Fnaf 4
    """),
    on_overlap_tile)

def Summon_endo():
    global Endo_enemy
    Endo_enemy = sprites.create(assets.image("""
        Endo dark
    """), SpriteKind.enemy)
    tiles.place_on_random_tile(Endo_enemy, assets.tile("""
        myTile101
    """))
    Endo_enemy.follow(Bonnie, 30)
    Endo_enemy.follow(Sans, 30)
    Endo_enemy.follow(Papyrus, 30)

def on_overlap_tile2(sprite2, location2):
    tiles.set_current_tilemap(tilemap("""
        Whole map fnaf1 night 2 power out
    """))
    tiles.place_on_random_tile(sprite2, assets.tile("""
        transparency16
    """))
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.door_closed_east,
    on_overlap_tile2)

def on_up_pressed():
    if Animatronic:
        Animatronic.set_image(assets.image("""
            freddy 5
        """))
        pause(500)
        Animatronic.set_image(assets.image("""
            freddy 2
        """))
        if Bonnie:
            Bonnie.set_image(assets.image("""
                bonnie back walk cycle 1
            """))
            pause(500)
            Bonnie.set_image(assets.image("""
                bonnie walk 2
            """))
    if Sans:
        Sans.set_image(assets.image("""
            Sans back1
        """))
        pause(500)
        Sans.set_image(assets.image("""
            Sans back0
        """))
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_overlap_tile3(sprite5, location5):
    global Undertale_Character_Select_Tilemap, sansobject, Papyrusobject
    tiles.set_current_tilemap(tilemap("""
        Character select Undertale
    """))
    tiles.place_on_random_tile(Spirit, sprites.skillmap.island_tile4)
    Undertale_Character_Select_Tilemap = 1
    sansobject = sprites.create(assets.image("""
        Sans
    """), SpriteKind.snasobject)
    tiles.place_on_random_tile(sansobject, assets.tile("""
        myTile6
    """))
    tiles.set_tile_at(sansobject.tilemap_location(),
        assets.tile("""
            myTile11
        """))
    Papyrusobject = sprites.create(assets.image("""
        Papyrus
    """), SpriteKind.papyrusobject)
    tiles.place_on_random_tile(Papyrusobject, assets.tile("""
        myTile60
    """))
    tiles.set_tile_at(Papyrusobject.tilemap_location(),
        assets.tile("""
            myTile11
        """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        Fangames left
    """),
    on_overlap_tile3)

def on_overlap_tile4(sprite8, location7):
    game.set_dialog_cursor(assets.image("""
        Dialogue Freddy distressed
    """))
    game.show_long_text("Dang, Doors locked. If only there was a vent nearby... I should check the party room above me...",
        DialogLayout.BOTTOM)
    if Sans:
        game.set_dialog_cursor(assets.image("""
            sans dialogue sprite
        """))
        game.show_long_text("* Huh. Some weirdo locked the doors.", DialogLayout.BOTTOM)
        game.set_dialog_cursor(assets.image("""
            sans dialogue smug
        """))
        game.show_long_text("* I should find a small vent on the floor and Vent. I need to be SUS.",
            DialogLayout.BOTTOM)
    if Papyrus:
        game.set_dialog_cursor(assets.image("""
            Papyrus dialogue sprite mad
        """))
        game.show_long_text("* Oh, Boondoggle! Someone locked the door!",
            DialogLayout.BOTTOM)
        game.set_dialog_cursor(assets.image("""
            Papyrus dialogue sprite
        """))
        game.show_long_text("* Maybe I could find a vent to crawl through!",
            DialogLayout.BOTTOM)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile57
    """),
    on_overlap_tile4)

def on_overlap_tile5(sprite7, location6):
    game.set_dialog_cursor(assets.image("""
        Puppet dialogue box 1
    """))
    game.show_long_text("greetings, I am the puppet", DialogLayout.BOTTOM)
    game.set_dialog_cursor(assets.image("""
        Spirit talking sprite
    """))
    game.show_long_text("Where am I?", DialogLayout.BOTTOM)
    game.set_dialog_cursor(assets.image("""
        Puppet dialogue box 1
    """))
    game.show_long_text("All will be revealed. but now, walk into the portal on the far wall, I will see you soon.",
        DialogLayout.BOTTOM)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        music box 1
    """),
    on_overlap_tile5)

def on_overlap_tile6(sprite72, location62):
    if Phone_Guy_message == 0:
        game.set_dialog_cursor(assets.image("""
            Phone Guy
        """))
        game.show_long_text("Hello? Hello, Hello? Uhh Welcome to the tutorial! uh, I've been informed by one of the... animatronics... that you are stuck here, so uh... let me help you! the controls are wasd for movement, and a for attacking, and also press the menu button for settings (this doesn't work right now) this is used for all skins and machines. and uh... just make it to the end of this place and uhh i'll meet you there, and uhh... yeah. oh uhh one more thing, the puppet need to see you and uhh... i'm sorry, Afton will be stopped.",
            DialogLayout.BOTTOM)
        game.set_dialog_cursor(assets.image("""
            Spirit talking sprite
        """))
        game.show_long_text("Who's the puppet? and who's Afton?", DialogLayout.BOTTOM)
        game.set_dialog_cursor(assets.image("""
            Phone Guy
        """))
        game.show_long_text("... *click*", DialogLayout.BOTTOM)
        tiles.place_on_random_tile(Spirit, assets.tile("""
            myTile14
        """))
    if Phone_Guy_message == 2:
        music.stop_all_sounds()
        music.play(music.create_song(assets.song("""
                Eisoptrophobia
            """)),
            music.PlaybackMode.LOOPING_IN_BACKGROUND)
        game.set_dialog_cursor(assets.image("""
            Phone Guy
        """))
        game.show_long_text("The uh box in front of us belongs to the uhh puppet. h-he's the guide for you uhh \"Lost Souls\"",
            DialogLayout.BOTTOM)
        game.set_dialog_cursor(assets.image("""
            Spirit talking sprite
        """))
        game.show_long_text("What's a lost soul?", DialogLayout.BOTTOM)
        game.set_dialog_cursor(assets.image("""
            Phone Guy
        """))
        game.show_long_text("I-uh... don't know. Just uh.. talk to charlotte.",
            DialogLayout.BOTTOM)
        game.set_dialog_cursor(assets.image("""
            Spirit talking sprite
        """))
        game.show_long_text("Charlotte?", DialogLayout.BOTTOM)
        game.set_dialog_cursor(assets.image("""
            Phone Guy
        """))
        game.show_long_text("The uhh Puppet. Right in front of you... *Click*",
            DialogLayout.BOTTOM)
        tiles.place_on_random_tile(Spirit, assets.tile("""
            myTile34
        """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        Phone guy guide
    """),
    on_overlap_tile6)

def on_on_overlap(sprite6, otherSprite):
    sprites.destroy(Enemy_prototype)
    sprites.destroy(Endo_enemy)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_overlap_tile7(sprite9, location8):
    global Night, World_select_Menu, _continue, Bonnie, Sans, Papyrus
    Night += 1
    game.show_long_text("would you like to continue? B= No, A= Yes",
        DialogLayout.CENTER)
    
    def on_pause_until():
        pass
    pause_until(on_pause_until)
    
    if controller.B.is_pressed():
        World_select_Menu = 1
    else:
        if controller.A.is_pressed():
            _continue += 1
        if Night == 2 and _continue == 1:
            sprites.destroy(Animatronic)
            Bonnie = sprites.create(assets.image("""
                Bonnie 1
            """), SpriteKind.player)
            scene.camera_follow_sprite(Bonnie)
            controller.move_sprite(Bonnie)
            fnaf12powered()
            if Night == 2 and _continue == 1 and Sans:
                sprites.destroy(Sans)
                Sans = sprites.create(assets.image("""
                    Sans
                """), SpriteKind.player)
                scene.camera_follow_sprite(Sans)
                controller.move_sprite(Sans)
                fnaf12powered()
                if Night == 2 and _continue == 1 and Papyrus:
                    sprites.destroy(Papyrus)
                    Papyrus = sprites.create(assets.image("""
                        Papyrus
                    """), SpriteKind.player)
                    scene.camera_follow_sprite(Papyrus)
                    controller.move_sprite(Papyrus)
                    fnaf12powered()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile68
    """),
    on_overlap_tile7)

def on_a_pressed():
    global projectile
    if Spirit:
        projectile = sprites.create_projectile_from_sprite(assets.image("""
            tear
        """), Spirit, -70, 0)
        projectile = sprites.create_projectile_from_sprite(assets.image("""
            tear
        """), Spirit, 70, 0)
        projectile = sprites.create_projectile_from_sprite(assets.image("""
            tear
        """), Spirit, 0, 70)
        projectile = sprites.create_projectile_from_sprite(assets.image("""
            tear
        """), Spirit, 0, -70)
        if Bonnie:
            projectile = sprites.create_projectile_from_sprite(assets.image("""
                    Bonnie proto projectile
                """),
                Bonnie,
                -70,
                0)
            projectile = sprites.create_projectile_from_sprite(assets.image("""
                    Bonnie proto projectile
                """),
                Bonnie,
                70,
                0)
            projectile = sprites.create_projectile_from_sprite(assets.image("""
                    Bonnie proto projectile
                """),
                Bonnie,
                0,
                70)
            projectile = sprites.create_projectile_from_sprite(assets.image("""
                    Bonnie proto projectile
                """),
                Bonnie,
                0,
                -70)
    if Sans:
        projectile = sprites.create_projectile_from_sprite(assets.image("""
            Sans Hot dog attack
        """), Sans, -70, 0)
        projectile = sprites.create_projectile_from_sprite(assets.image("""
            Sans bone Attack
        """), Sans, 70, 0)
        projectile = sprites.create_projectile_from_sprite(assets.image("""
            Sans Ketchup attack
        """), Sans, 0, 70)
        projectile = sprites.create_projectile_from_sprite(assets.image("""
                Sans Ice Cream Attack
            """),
            Sans,
            0,
            -70)
    if Papyrus:
        projectile = sprites.create_projectile_from_sprite(assets.image("""
            Sans bone Attack
        """), Papyrus, -70, 0)
        projectile = sprites.create_projectile_from_sprite(assets.image("""
            Sans bone Attack
        """), Papyrus, 70, 0)
        projectile = sprites.create_projectile_from_sprite(assets.image("""
            Sans bone Attack
        """), Papyrus, 0, 70)
        projectile = sprites.create_projectile_from_sprite(assets.image("""
            Sans bone Attack
        """), Papyrus, 0, -70)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap2(sprite3, otherSprite2):
    global Sans
    Sans = sprites.create(assets.image("""
        Sans
    """), SpriteKind.player)
    sprites.destroy(sansobject)
    sprites.destroy(Spirit)
    tiles.place_on_random_tile(Sans, sprites.skillmap.island_tile4)
    controller.move_sprite(Sans)
    scene.camera_follow_sprite(Sans)
sprites.on_overlap(SpriteKind.player, SpriteKind.snasobject, on_on_overlap2)

def on_overlap_tile8(sprite92, location82):
    global demo_end
    if Papyrus or (Sans or Bonnie):
        scene.set_background_image(assets.image("""
            myImage4
        """))
        game.set_dialog_text_color(1)
        game.set_dialog_frame(assets.image("""
            text box border
        """))
        game.set_dialog_cursor(assets.image("""
            Freddy hat
        """))
        music.stop_all_sounds()
        music.play(music.create_song(assets.song("""
                Music box demo
            """)),
            music.PlaybackMode.LOOPING_IN_BACKGROUND)
        music.set_volume(50)
        game.show_long_text("Hello! you've reached the current end of the game, by some miracle of patience, I'm assuming, you know the drill, not done yet, yadda yadda; so please switch over to disc 2, if you will.",
            DialogLayout.FULL)
        game.show_long_text("oh, and you cant explore anymore =)", DialogLayout.FULL)
        demo_end += 1
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        Night 2 Nightguard
    """),
    on_overlap_tile8)

def on_left_pressed():
    if Animatronic:
        Animatronic.set_image(assets.image("""
            freddy side 2
        """))
        pause(500)
        Animatronic.set_image(assets.image("""
            freddy side 3
        """))
        if Bonnie:
            Bonnie.set_image(assets.image("""
                Bonnie side1
            """))
            pause(500)
            Bonnie.set_image(assets.image("""
                Bonnie side2
            """))
    if Sans:
        Sans.set_image(assets.image("""
            Sans side3
        """))
        pause(500)
        Sans.set_image(assets.image("""
            Sans side2
        """))
        pause(500)
        Sans.set_image(assets.image("""
            Sans side4
        """))
        pause(500)
        Sans.set_image(assets.image("""
            Sans side2
        """))
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def fnaf11():
    global Night
    tiles.set_current_tilemap(tilemap("""
        Whole map fnaf 1
    """))
    sprites.destroy(Spirit)
    tiles.place_on_random_tile(Animatronic, assets.tile("""
        myTile16
    """))
    Night = 1
    info.set_life(3)
    if Sans:
        tiles.set_current_tilemap(tilemap("""
            Whole map fnaf 1
        """))
        sprites.destroy(Spirit)
        sprites.destroy(Animatronic)
        sprites.destroy(projectile)
        tiles.place_on_random_tile(Sans, assets.tile("""
            myTile16
        """))
        Night = 1
        info.set_life(3)
    if Papyrus:
        tiles.set_current_tilemap(tilemap("""
            Whole map fnaf 1
        """))
        sprites.destroy(Spirit)
        sprites.destroy(Animatronic)
        sprites.destroy(projectile)
        tiles.place_on_random_tile(Papyrus, assets.tile("""
            myTile16
        """))
        Night = 1
        info.set_life(3)

def on_right_pressed():
    if Animatronic:
        Animatronic.set_image(assets.image("""
            freddy side 1
        """))
        pause(500)
        Animatronic.set_image(assets.image("""
            freddy side 0
        """))
        if Bonnie:
            Bonnie.set_image(assets.image("""
                Bonnie side0
            """))
            pause(500)
            Bonnie.set_image(assets.image("""
                Bonnie side
            """))
    if Sans:
        Sans.set_image(assets.image("""
            Sans side1
        """))
        pause(500)
        Sans.set_image(assets.image("""
            Sans side
        """))
        pause(500)
        Sans.set_image(assets.image("""
            Sans side0
        """))
        pause(500)
        Sans.set_image(assets.image("""
            Sans side
        """))
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_overlap_tile9(sprite73, location63):
    tiles.set_current_tilemap(tilemap("""
        Basement
    """))
    tiles.place_on_random_tile(Bonnie, sprites.dungeon.floor_dark0)
    if Sans:
        tiles.set_current_tilemap(tilemap("""
            Basement
        """))
        tiles.place_on_random_tile(Sans, sprites.dungeon.floor_dark0)
        scene.camera_follow_sprite(Sans)
    if Papyrus:
        tiles.set_current_tilemap(tilemap("""
            Basement
        """))
        tiles.place_on_random_tile(Papyrus, sprites.dungeon.floor_dark0)
        scene.camera_follow_sprite(Papyrus)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.stair_north,
    on_overlap_tile9)

def on_down_pressed():
    if Animatronic:
        Animatronic.set_image(assets.image("""
            freddy 3
        """))
        pause(500)
        Animatronic.set_image(assets.image("""
            freddy 0
        """))
        if Bonnie:
            Bonnie.set_image(assets.image("""
                Bonnie 1
            """))
            pause(500)
            Bonnie.set_image(assets.image("""
                Bonnie 1
            """))
    if Sans:
        Sans.set_image(assets.image("""
            Sans0
        """))
        pause(500)
        Sans.set_image(assets.image("""
            Sans1
        """))
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_overlap_tile10(sprite4, location3):
    info.change_life_by(-1)
    sprite4.set_velocity(0, -20)
    effects.clear_particles(sprite4)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_spike,
    on_overlap_tile10)

def on_overlap_tile11(sprite52, location52):
    global Enemy_prototype, Phone_Guy_message
    tiles.place_on_random_tile(Enemy_prototype,
        assets.tile("""
            enemy spawner NOT COKE
        """))
    Enemy_prototype = sprites.create(assets.image("""
            Enemy PQ prototype
        """),
        SpriteKind.enemy)
    Enemy_prototype.follow(Spirit, 30)
    Phone_Guy_message = 2
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile124
    """),
    on_overlap_tile11)

def on_overlap_tile12(sprite22, location22):
    global Truth_ending_game_1
    if Truth_ending_game_1 == 1:
        game.show_long_text("I've Already read this", DialogLayout.BOTTOM)
    if Truth_ending_game_1 == 0 and Animatronic:
        Truth_ending_game_1 += 1
        music.stop_all_sounds()
        music.play(music.create_song(assets.song("""
                Eisoptrophobia
            """)),
            music.PlaybackMode.IN_BACKGROUND)
        game.show_long_text("--Missing Children-- Kids vanish at local pizzeria- bodies not found. Two local children were reportedly lured into a back room during the late hours of operation at Freddy Fazbear's Pizza on the night of June 26th. While video surveillence identified the man responsible and led to his capture the following morning, the children themselves were never found and are presumed dead. Police think that the suspect dressed as a company mascot to earn their trust.",
            DialogLayout.FULL)
        game.set_dialog_cursor(assets.image("""
            Dialogue Freddy distressed
        """))
        game.show_long_text("...tha- that was... me... i... he... ", DialogLayout.BOTTOM)
        game.set_dialog_cursor(assets.image("""
            Dialogue Freddy dark
        """))
        game.show_long_text("HE KILLED me! My Family doesn't even know I'm Dead! It's HIS fault! HE will pay!",
            DialogLayout.BOTTOM)
        if Sans:
            Truth_ending_game_1 += 1
            music.stop_all_sounds()
            music.play(music.create_song(assets.song("""
                    Eisoptrophobia
                """)),
                music.PlaybackMode.IN_BACKGROUND)
            game.show_long_text("--Missing Children-- Kids vanish at local pizzeria- bodies not found. Two local children were reportedly lured into a back room during the late hours of operation at Freddy Fazbear's Pizza on the night of June 26th. While video surveillence identified the man responsible and led to his capture the following morning, the children themselves were never found and are presumed dead. Police think that the suspect dressed as a company mascot to earn their trust.",
                DialogLayout.FULL)
            music.stop_all_sounds()
            game.set_dialog_cursor(assets.image("""
                sans dialogue sprite serious
            """))
            music.play(music.create_song(assets.song("""
                    Minorlovania
                """)),
                music.PlaybackMode.LOOPING_IN_BACKGROUND)
            game.show_long_text("* oh-ho-ho. that little peice of...", DialogLayout.BOTTOM)
            game.set_dialog_cursor(assets.image("""
                sans dialogue sprite Megalovania 1
            """))
            game.show_long_text("* Sh1t!", DialogLayout.BOTTOM)
            game.set_dialog_cursor(assets.image("""
                sans dialogue sprite closed eyes
            """))
            game.show_long_text("* Heh. Afton,if you continue down this path,",
                DialogLayout.BOTTOM)
            game.set_dialog_cursor(assets.image("""
                sans dialogue sprite Megalovania 2
            """))
            game.show_long_text("* You're Gonna Have A Bad Time.", DialogLayout.BOTTOM)
            if Papyrus:
                Truth_ending_game_1 += 1
                music.stop_all_sounds()
                music.play(music.create_song(assets.song("""
                        Eisoptrophobia
                    """)),
                    music.PlaybackMode.IN_BACKGROUND)
                game.show_long_text("--Missing Children-- Kids vanish at local pizzeria- bodies not found. Two local children were reportedly lured into a back room during the late hours of operation at Freddy Fazbear's Pizza on the night of June 26th. While video surveillence identified the man responsible and led to his capture the following morning, the children themselves were never found and are presumed dead. Police think that the suspect dressed as a company mascot to earn their trust.",
                    DialogLayout.FULL)
                music.stop_all_sounds()
                game.set_dialog_cursor(assets.image("""
                    Papyrus dialogue sprite sad
                """))
                music.play(music.create_song(assets.song("""
                        Oh One true Love
                    """)),
                    music.PlaybackMode.LOOPING_IN_BACKGROUND)
                game.show_long_text("* How could anyone do such a thing?", DialogLayout.BOTTOM)
                game.set_dialog_cursor(assets.image("""
                    Papyrus dialogue sprite
                """))
                game.show_long_text("*its okay, I'll find him", DialogLayout.BOTTOM)
                game.set_dialog_cursor(assets.image("""
                    Papyrus dialogue sprite
                """))
                game.show_long_text("* and I'll help him be better!", DialogLayout.BOTTOM)
                game.set_dialog_cursor(assets.image("""
                    Papyrus dialogue sprite0
                """))
                game.show_long_text("* Nyeh Heh heh!", DialogLayout.BOTTOM)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile72
    """),
    on_overlap_tile12)

def on_overlap_tile13(sprite42, location4):
    global Spirit, Sans, Papyrus
    music.stop_all_sounds()
    music.set_volume(20)
    music.play(music.create_song(assets.song("""
            Tutorial
        """)),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
    sprites.destroy_all_sprites_of_kind(SpriteKind.player)
    Spirit = sprites.create(assets.image("""
        Spirit
    """), SpriteKind.player)
    tiles.set_current_tilemap(tilemap("""
        Level Select Menu
    """))
    sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
    tiles.place_on_random_tile(Spirit, assets.tile("""
        Crying spirit spawn
    """))
    controller.move_sprite(Spirit, 100, 100)
    scene.camera_follow_sprite(Spirit)
    if Sans:
        sprites.destroy_all_sprites_of_kind(SpriteKind.player)
        Sans = sprites.create(assets.image("""
            Sans
        """), SpriteKind.player)
        tiles.set_current_tilemap(tilemap("""
            Level Select Menu
        """))
        sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
        tiles.place_on_random_tile(Sans, assets.tile("""
            Crying spirit spawn
        """))
        controller.move_sprite(Sans, 100, 100)
        scene.camera_follow_sprite(Sans)
    if Papyrus:
        sprites.destroy_all_sprites_of_kind(SpriteKind.player)
        Papyrus = sprites.create(assets.image("""
            Papyrus
        """), SpriteKind.player)
        tiles.set_current_tilemap(tilemap("""
            Level Select Menu
        """))
        sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
        tiles.place_on_random_tile(Papyrus, assets.tile("""
            Crying spirit spawn
        """))
        controller.move_sprite(Papyrus, 100, 100)
        scene.camera_follow_sprite(Papyrus)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        Portal proto
    """),
    on_overlap_tile13)

def on_overlap_tile14(sprite74, location64):
    tiles.set_current_tilemap(tilemap("""
        Whole map fnaf1 night 2 power out
    """))
    tiles.place_on_random_tile(Bonnie, sprites.dungeon.floor_light_moss)
    Summon_endo()
    if Sans:
        tiles.set_current_tilemap(tilemap("""
            Whole map fnaf1 night 2 power out
        """))
        tiles.place_on_random_tile(Sans, sprites.dungeon.floor_light_moss)
        tiles.place_on_random_tile(Papyrus, sprites.dungeon.floor_light_moss)
        Summon_endo()
    if Papyrus:
        tiles.set_current_tilemap(tilemap("""
            Whole map fnaf1 night 2 power out
        """))
        tiles.place_on_random_tile(Papyrus, sprites.dungeon.floor_light_moss)
        Summon_endo()
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.stair_west,
    on_overlap_tile14)

def on_overlap_tile15(sprite10, location9):
    Summon_endo()
    tiles.set_current_tilemap(tilemap("""
        Underground escape fnaf1 night 2 blackout mode
    """))
    tiles.place_on_random_tile(Bonnie, sprites.dungeon.floor_dark3)
    music.stop_all_sounds()
    music.play(music.create_song(assets.song("""
            Blackout Mode theme beta
        """)),
        music.PlaybackMode.IN_BACKGROUND)
    if Sans:
        tiles.set_current_tilemap(tilemap("""
            Underground escape fnaf1 night 2 blackout mode
        """))
        tiles.place_on_random_tile(Sans, sprites.dungeon.floor_dark3)
        music.stop_all_sounds()
        music.play(music.create_song(assets.song("""
                Song That Might Play When You Fight Sans
            """)),
            music.PlaybackMode.IN_BACKGROUND)
    if Papyrus:
        tiles.set_current_tilemap(tilemap("""
            Underground escape fnaf1 night 2 blackout mode
        """))
        tiles.place_on_random_tile(Papyrus, sprites.dungeon.floor_dark3)
        music.stop_all_sounds()
        music.play(music.create_song(assets.song("""
                Bonetrousle demo Version
            """)),
            music.PlaybackMode.IN_BACKGROUND)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_hole,
    on_overlap_tile15)

def on_overlap_tile16(sprite75, location65):
    tiles.set_current_tilemap(tilemap("""
        Basement power out
    """))
    tiles.place_on_random_tile(Bonnie, sprites.dungeon.floor_dark0)
    if Sans:
        tiles.set_current_tilemap(tilemap("""
            Basement power out
        """))
        tiles.place_on_random_tile(Sans, sprites.dungeon.floor_dark0)
    if Papyrus:
        tiles.set_current_tilemap(tilemap("""
            Basement power out
        """))
        tiles.place_on_random_tile(Papyrus, sprites.dungeon.floor_dark0)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile49
    """),
    on_overlap_tile16)

def on_on_overlap3(sprite11, otherSprite3):
    global Papyrus
    Papyrus = sprites.create(assets.image("""
        Papyrus
    """), SpriteKind.player)
    sprites.destroy(Papyrusobject)
    sprites.destroy(Spirit)
    tiles.place_on_random_tile(Papyrus, sprites.skillmap.island_tile4)
    controller.move_sprite(Papyrus)
    scene.camera_follow_sprite(Papyrus)
sprites.on_overlap(SpriteKind.player, SpriteKind.papyrusobject, on_on_overlap3)

def fnaf12powered():
    tiles.place_on_random_tile(Bonnie, assets.tile("""
        myTile16
    """))
    tiles.set_current_tilemap(tilemap("""
        Whole map fnaf1 night 2
    """))
    if Sans:
        sprites.destroy(Bonnie)
        tiles.place_on_random_tile(Sans, assets.tile("""
            myTile16
        """))
        tiles.set_current_tilemap(tilemap("""
            Whole map fnaf1 night 2
        """))
    if Papyrus:
        sprites.destroy(Bonnie)
        tiles.place_on_random_tile(Papyrus, assets.tile("""
            myTile16
        """))
        tiles.set_current_tilemap(tilemap("""
            Whole map fnaf1 night 2
        """))

def on_overlap_tile17(sprite76, location66):
    if Bonnie:
        game.set_dialog_cursor(assets.image("""
            Dialogue Chica
        """))
        game.show_long_text("ugh, The doors are locked!", DialogLayout.BOTTOM)
        game.set_dialog_cursor(assets.image("""
            Dialogue Bonnie
        """))
        game.show_long_text("Any ideas?", DialogLayout.BOTTOM)
        game.set_dialog_cursor(assets.image("""
            Dialogue Chica
        """))
        game.show_long_text("There's A power box downstairs to turn off the power.",
            DialogLayout.BOTTOM)
        game.set_dialog_cursor(assets.image("""
            Dialogue Bonnie
        """))
        game.show_long_text("On it.", DialogLayout.BOTTOM)
    if Sans:
        game.set_dialog_cursor(assets.image("""
            Dialogue Chica
        """))
        game.show_long_text("ugh, The doors are locked!", DialogLayout.BOTTOM)
        game.set_dialog_cursor(assets.image("""
            sans dialogue sprite looking around
        """))
        game.show_long_text("* what do I do?", DialogLayout.BOTTOM)
        game.set_dialog_cursor(assets.image("""
            Dialogue Chica
        """))
        game.show_long_text("There's A power box downstairs to turn off the power.",
            DialogLayout.BOTTOM)
        game.set_dialog_cursor(assets.image("""
            sans dialogue sprite winking
        """))
        game.show_long_text("* Ehh, you got it.", DialogLayout.BOTTOM)
    if Papyrus:
        game.set_dialog_cursor(assets.image("""
            Dialogue Chica
        """))
        game.show_long_text("ugh, The doors are locked!", DialogLayout.BOTTOM)
        game.set_dialog_cursor(assets.image("""
            Papyrus dialogue sprite
        """))
        game.show_long_text("* what do I do?", DialogLayout.BOTTOM)
        game.set_dialog_cursor(assets.image("""
            Dialogue Chica
        """))
        game.show_long_text("There's A power box downstairs to turn off the power.",
            DialogLayout.BOTTOM)
        game.set_dialog_cursor(assets.image("""
            Papyrus dialogue sprite
        """))
        game.show_long_text("*okay, i'll find it! Ney Heh heh!", DialogLayout.BOTTOM)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile29
    """),
    on_overlap_tile17)

def on_overlap_tile18(sprite12, location10):
    if Spirit:
        game.show_long_text("Hello! this is the feature board! things added this update: Implemented Sans and papyrus, Added night 3 and 4, Added songs like Megalovania, Minorlovania, Sans, bonetrousel, Science blaster, and song that might play when you fight sans",
            DialogLayout.FULL)
    if Papyrus:
        game.show_long_text("Hello! this is the feature board! things added this update: Implemented Sans and papyrus, Added night 3 and 4, Added songs like Megalovania, Minorlovania, Sans, bonetrousel, Science blaster, and song that might play when you fight sans",
            DialogLayout.FULL)
        game.set_dialog_cursor(assets.image("""
            Papyrus dialogue sprite bro what
        """))
        game.show_long_text("I don't understand any of this...", DialogLayout.BOTTOM)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile56
    """),
    on_overlap_tile18)

def on_overlap_tile19(sprite77, location67):
    game.splash("These are the rules:\"Don't run. Don't yell. Don't scream. Don't poop on floor. Stay close to Mom. Don't touch Freddy. Don't hit. Leave before dark\" ")
    if Sans:
        game.splash("These are the rules:\"Don't run. Don't yell. Don't scream. Don't poop on floor. Stay close to Mom. Don't touch Freddy. Don't hit. Leave before dark\" ")
        game.set_dialog_cursor(assets.image("""
            sans dialogue sprite looking around
        """))
        game.splash("* Those are some weird ahh rules, not gonna lie")
    if Papyrus:
        game.show_long_text("These are the rules:\"Don't run. Don't yell. Don't scream. Don't poop on the floor. Stay close to Mom. Don't touch Freddy. Don't hit. Leave before dark\" ",
            DialogLayout.BOTTOM)
        game.set_dialog_cursor(assets.image("""
            Papyrus dialogue sprite0
        """))
        game.show_long_text("* Those are a lot of rules to follow, And I, THE GREAT PAPYRUS! Will follow them all! Nyeh Heh Heh!!!",
            DialogLayout.BOTTOM)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile54
    """),
    on_overlap_tile19)

def on_on_overlap4(sprite13, otherSprite4):
    info.change_life_by(-1)
    sprite13.set_velocity(-50, 0)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap4)

demo_end = 0
projectile: Sprite = None
_continue = 0
Night = 0
Enemy_prototype: Sprite = None
Papyrusobject: Sprite = None
sansobject: Sprite = None
Undertale_Character_Select_Tilemap = 0
Bonnie: Sprite = None
Endo_enemy: Sprite = None
Animatronic: Sprite = None
Papyrus: Sprite = None
Sans: Sprite = None
World_select_Menu = 0
Phone_Guy_message = 0
Truth_ending_game_1 = 0
Spirit: Sprite = None
Spirit = sprites.create(assets.image("""
    Spirit
"""), SpriteKind.player)
scene.camera_follow_sprite(Spirit)
controller.move_sprite(Spirit, 100, 100)
music.set_volume(30)
music.play(music.create_song(assets.song("""
        Tutorial
    """)),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)
tiles.set_current_tilemap(tilemap("""
    Tutorial
"""))
tiles.place_on_random_tile(Spirit, assets.tile("""
    myTile12
"""))
Truth_ending_game_1 = 0
Phone_Guy_message = 0
dungeon_escape_fnaf_1_2_2 = 0
World_select_Menu = 0
game.set_dialog_text_color(1)
game.set_dialog_frame(assets.image("""
    text box border
"""))
game.show_long_text("* Welcome! the controls right now are wasd",
    DialogLayout.BOTTOM)
game.show_long_text("Objective: Talk to the phone.", DialogLayout.TOP)
info.set_life(3)
if World_select_Menu == 1:
    music.stop_all_sounds()
    music.set_volume(20)
    music.play(music.create_song(assets.song("""
            Tutorial
        """)),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
    sprites.destroy_all_sprites_of_kind(SpriteKind.player)
    Spirit = sprites.create(assets.image("""
        Spirit
    """), SpriteKind.player)
    tiles.set_current_tilemap(tilemap("""
        Level Select Menu
    """))
    sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
    tiles.place_on_random_tile(Spirit, assets.tile("""
        Crying spirit spawn
    """))
    controller.move_sprite(Spirit, 100, 100)
    scene.camera_follow_sprite(Spirit)
    World_select_Menu = 0
    if Sans:
        sprites.destroy_all_sprites_of_kind(SpriteKind.player)
        Sans = sprites.create(assets.image("""
            Sans
        """), SpriteKind.player)
        tiles.set_current_tilemap(tilemap("""
            Level Select Menu
        """))
        sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
        tiles.place_on_random_tile(Sans, assets.tile("""
            Crying spirit spawn
        """))
        controller.move_sprite(Sans, 100, 100)
        scene.camera_follow_sprite(Sans)
        World_select_Menu = 0
    if Papyrus:
        sprites.destroy_all_sprites_of_kind(SpriteKind.player)
        Papyrus = sprites.create(assets.image("""
            Papyrus
        """), SpriteKind.player)
        tiles.set_current_tilemap(tilemap("""
            Level Select Menu
        """))
        sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
        tiles.place_on_random_tile(Papyrus, assets.tile("""
            Crying spirit spawn
        """))
        controller.move_sprite(Papyrus, 100, 100)
        scene.camera_follow_sprite(Papyrus)
        World_select_Menu = 0