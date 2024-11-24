namespace SpriteKind {
    export const snasobject = SpriteKind.create()
    export const papyrusobject = SpriteKind.create()
    export const duskyobject = SpriteKind.create()
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`Fnaf 4`, function (sprite, location) {
    music.stopAllSounds()
    music.setVolume(30)
    music.play(music.createSong(assets.song`Overworld Theme`), music.PlaybackMode.LoopingInBackground)
    Animatronic = sprites.create(assets.image`Chica`, SpriteKind.Player)
    controller.moveSprite(Animatronic)
    scene.cameraFollowSprite(Animatronic)
    fnaf13()
    if (Dusky) {
        sprites.destroy(Dusky)
        music.stopAllSounds()
        music.setVolume(30)
        music.play(music.createSong(assets.song`Overworld Theme`), music.PlaybackMode.LoopingInBackground)
        Dusky = sprites.create(assets.image`Dusky-Cat`, SpriteKind.Player)
        controller.moveSprite(Dusky)
        scene.cameraFollowSprite(Dusky)
        fnaf13()
    }
})
function Summon_camera () {
    Camera = sprites.create(assets.image`Camera`, SpriteKind.Enemy)
    tiles.placeOnRandomTile(Camera, assets.tile`Camera Spawner`)
    for (let index = 0; index < 4; index++) {
        Camera_Projectile = sprites.createProjectileFromSprite(assets.image`Camera Projectile`, Camera, -70, 0)
        pause(2000)
    }
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile94`, function (sprite2, location2) {
    game.showLongText("Missing children Five children now reported missing. Suspect Convicted. Five children are now linked to the incident at Freddy Fazbear’s Pizza, where a man dressed as a cartoon mascot lured them into a back room. While the suspect has been charged, the bodies themselves were never found.", DialogLayout.Full)
    if (Truth_ending_game_1 == 1) {
        game.showLongText("I've Already read this", DialogLayout.Bottom)
    }
    if (Truth_ending_game_1 == 0 && Animatronic) {
        Truth_ending_game_1 += 1
        music.stopAllSounds()
        music.play(music.createSong(assets.song`Eisoptrophobia`), music.PlaybackMode.InBackground)
        game.setDialogCursor(assets.image`Dialogue Chica`)
        game.showLongText("... I remember that...", DialogLayout.Bottom)
        game.setDialogCursor(assets.image`Dialogue Chica`)
        game.showLongText("I was the FIRST... I'VE. SEEN. EVERYTHING. I'm so sorry, friends, I couldn't stop him...", DialogLayout.Bottom)
        if (Dusky) {
            Truth_ending_game_1 += 1
            music.stopAllSounds()
            music.play(music.createSong(assets.song`Just a Burning Memory`), music.PlaybackMode.LoopingInBackground)
            game.setDialogCursor(assets.image`Dialogue Dusky`)
            game.showLongText("A mascot costume, huh? That sounds like...huh, I'm having trouble remembering...it was big, gold, and had big ears? What am I even saying???", DialogLayout.Bottom)
        }
    }
})
function Summon_endo () {
    Endo_enemy = sprites.create(assets.image`Endo dark`, SpriteKind.Enemy)
    tiles.placeOnRandomTile(Endo_enemy, assets.tile`myTile101`)
    Endo_enemy.follow(Animatronic, 30)
    Endo_enemy.follow(Dusky, 30)
}
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.doorClosedEast, function (sprite, location) {
    tiles.setCurrentTilemap(tilemap`Whole map fnaf1 night 2 power out`)
    tiles.placeOnRandomTile(sprite, assets.tile`transparency16`)
})
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Animatronic) {
        characterAnimations.loopFrames(
        Animatronic,
        assets.animation`Chica Walking up`,
        500,
        characterAnimations.rule(Predicate.MovingUp)
        )
    }
    if (Foxy) {
        characterAnimations.loopFrames(
        Foxy,
        assets.animation`Foxy Walking down0`,
        200,
        characterAnimations.rule(Predicate.MovingUp)
        )
    }
    if (Dusky) {
        characterAnimations.loopFrames(
        Dusky,
        assets.animation`Dusky Walking up Proto`,
        500,
        characterAnimations.rule(Predicate.MovingUp)
        )
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`Fangames left`, function (sprite5, location5) {
    tiles.setCurrentTilemap(tilemap`Character select Undertale`)
    tiles.placeOnRandomTile(Spirit, sprites.skillmap.islandTile4)
    Duskyobject = sprites.create(assets.image`Dusky-Cat`, SpriteKind.duskyobject)
    tiles.placeOnRandomTile(Duskyobject, assets.tile`myTile6`)
    tiles.setTileAt(Duskyobject.tilemapLocation(), assets.tile`myTile11`)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile57`, function (sprite8, location7) {
    if (Dusky) {
        game.setDialogCursor(assets.image`Dialogue Dusky`)
        game.showLongText("Dangnadit, he locked the door, I think I might have to turn the power off from the basement", DialogLayout.Bottom)
    }
    game.setDialogCursor(assets.image`Dialogue Chica`)
    game.showLongText("Dang. Nightguard locked the doors. I'll have to go and turn off power...", DialogLayout.Bottom)
})
function world_select_menu () {
    music.stopAllSounds()
    music.setVolume(20)
    music.play(music.createSong(assets.song`Midnight motorist`), music.PlaybackMode.LoopingInBackground)
    sprites.destroyAllSpritesOfKind(SpriteKind.Player)
    Spirit = sprites.create(assets.image`Spirit`, SpriteKind.Player)
    tiles.setCurrentTilemap(tilemap`Level Select Menu`)
    sprites.destroyAllSpritesOfKind(SpriteKind.Enemy)
    tiles.placeOnRandomTile(Spirit, assets.tile`Crying spirit spawn`)
    controller.moveSprite(Spirit)
    scene.cameraFollowSprite(Spirit)
    if (Dusky) {
        sprites.destroyAllSpritesOfKind(SpriteKind.Player)
        Dusky = sprites.create(assets.image`Dusky-Cat`, SpriteKind.Player)
        tiles.setCurrentTilemap(tilemap`Level Select Menu`)
        tiles.placeOnRandomTile(Dusky, assets.tile`Crying spirit spawn`)
        controller.moveSprite(Dusky)
        scene.cameraFollowSprite(Dusky)
    }
}
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite6, otherSprite) {
    sprites.destroy(Endo_enemy)
    sprites.destroyAllSpritesOfKind(SpriteKind.Enemy)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile68`, function (sprite9, location8) {
    Night += 1
    game.showLongText("would you like to continue? B= No, A= Yes", DialogLayout.Center)
    pauseUntil(() => controller.A.isPressed() || controller.B.isPressed())
    if (controller.B.isPressed()) {
        world_select_menu()
    } else {
        if (controller.A.isPressed()) {
            _continue += 1
        }
        if (Night == 4 && _continue == 1) {
            sprites.destroy(Animatronic)
            Foxy = sprites.create(assets.image`Foxy`, SpriteKind.Player)
            scene.cameraFollowSprite(Foxy)
            controller.moveSprite(Foxy, 125, 125)
            fnaf14powered()
            if (Night == 4 && _continue == 1 && Dusky) {
                Dusky = sprites.create(assets.image`Dusky-Cat`, SpriteKind.Player)
                scene.cameraFollowSprite(Dusky)
                controller.moveSprite(Dusky)
                fnaf14powered()
            }
        }
    }
    if (demo_end == 1) {
        if (Dusky || Foxy) {
            game.setDialogCursor(assets.image`Freddy hat`)
            music.stopAllSounds()
            music.play(music.createSong(assets.song`Music box demo`), music.PlaybackMode.LoopingInBackground)
            music.setVolume(50)
            game.showLongText("Hello! Nice Job Getting to the end!", DialogLayout.Full)
        }
    }
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Animatronic) {
        projectile = sprites.createProjectileFromSprite(assets.image`Chica projectile`, Animatronic, -70, 0)
        projectile = sprites.createProjectileFromSprite(assets.image`Chica projectile`, Animatronic, 70, 0)
        projectile = sprites.createProjectileFromSprite(assets.image`Chica projectile`, Animatronic, 0, 70)
        projectile = sprites.createProjectileFromSprite(assets.image`Chica projectile`, Animatronic, 0, -70)
    }
    if (Dusky) {
        projectile = sprites.createProjectileFromSprite(assets.image`Dusky projectile`, Dusky, -70, 0)
        projectile = sprites.createProjectileFromSprite(assets.image`Dusky projectile`, Dusky, 70, 0)
        projectile = sprites.createProjectileFromSprite(assets.image`Dusky projectile`, Dusky, 0, 70)
        projectile = sprites.createProjectileFromSprite(assets.image`Dusky projectile`, Dusky, 0, -70)
    }
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Animatronic) {
        characterAnimations.loopFrames(
        Animatronic,
        assets.animation`Chica Walking sideways0`,
        500,
        characterAnimations.rule(Predicate.MovingLeft)
        )
    }
    if (Foxy) {
        characterAnimations.loopFrames(
        Foxy,
        assets.animation`Foxy Walking Side0`,
        200,
        characterAnimations.rule(Predicate.MovingLeft)
        )
    }
    if (Dusky) {
        characterAnimations.loopFrames(
        Dusky,
        assets.animation`Dusky walking sideways proto`,
        500,
        characterAnimations.rule(Predicate.MovingLeft)
        )
    }
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Animatronic) {
        characterAnimations.loopFrames(
        Animatronic,
        assets.animation`Chica Walking sideways`,
        500,
        characterAnimations.rule(Predicate.MovingRight)
        )
    }
    if (Foxy) {
        characterAnimations.loopFrames(
        Foxy,
        assets.animation`Foxy Walking Side`,
        200,
        characterAnimations.rule(Predicate.MovingRight)
        )
    }
    if (Dusky) {
        characterAnimations.loopFrames(
        Dusky,
        assets.animation`Dusky walking sideways proto0`,
        500,
        characterAnimations.rule(Predicate.MovingRight)
        )
    }
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.stairNorth, function (sprite7, location6) {
    if (Night == 3) {
        tiles.setCurrentTilemap(tilemap`Basement`)
        tiles.placeOnRandomTile(Animatronic, sprites.dungeon.floorDark0)
        if (Dusky) {
            tiles.setCurrentTilemap(tilemap`Basement`)
            tiles.placeOnRandomTile(Dusky, sprites.dungeon.floorDark0)
            scene.cameraFollowSprite(Dusky)
        }
    }
})
function fnaf13 () {
    tiles.setCurrentTilemap(tilemap`Whole map fnaf1 night 3`)
    sprites.destroy(Spirit)
    tiles.placeOnRandomTile(Animatronic, assets.tile`myTile16`)
    Night = 3
    info.setLife(3)
    if (Dusky) {
        tiles.setCurrentTilemap(tilemap`Whole map fnaf1 night 3`)
        sprites.destroy(Spirit)
        sprites.destroy(Animatronic)
        tiles.placeOnRandomTile(Dusky, assets.tile`myTile16`)
        Night = 3
        info.setLife(3)
    }
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile8`, function (sprite, location) {
    tiles.setCurrentTilemap(tilemap`level2`)
    game.showLongText("Switch to Anomaly Disk 01. How to get disk? Email me your screen :)", DialogLayout.Bottom)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.duskyobject, function (sprite, otherSprite) {
    Dusky = sprites.create(assets.image`Dusky-Cat`, SpriteKind.Player)
    sprites.destroy(Duskyobject)
    sprites.destroy(Spirit)
    tiles.placeOnRandomTile(Dusky, sprites.skillmap.islandTile4)
    controller.moveSprite(Dusky)
    scene.cameraFollowSprite(Dusky)
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Animatronic) {
        characterAnimations.loopFrames(
        Animatronic,
        assets.animation`Chica Walking Down`,
        500,
        characterAnimations.rule(Predicate.MovingDown)
        )
    }
    if (Foxy) {
        characterAnimations.loopFrames(
        Foxy,
        assets.animation`Foxy Walking down`,
        200,
        characterAnimations.rule(Predicate.MovingDown)
        )
    }
    if (Dusky) {
        characterAnimations.loopFrames(
        Dusky,
        assets.animation`Dusky Walking`,
        100,
        characterAnimations.rule(Predicate.MovingDown)
        )
    }
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.hazardSpike, function (sprite, location) {
    info.changeLifeBy(-1)
    sprite.setVelocity(0, -20)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`Portal proto`, function (sprite4, location4) {
    world_select_menu()
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.stairWest, function (sprite7, location6) {
    tiles.setCurrentTilemap(tilemap`Whole map fnaf1 night 2 power out`)
    tiles.placeOnRandomTile(Animatronic, sprites.dungeon.floorLightMoss)
    Summon_endo()
    if (Dusky) {
        tiles.setCurrentTilemap(tilemap`Whole map fnaf1 night 2 power out`)
        tiles.placeOnRandomTile(Dusky, sprites.dungeon.floorLightMoss)
        Summon_endo()
    }
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.hazardHole, function (sprite, location) {
    tiles.setCurrentTilemap(tilemap`Underground escape fnaf1 night 3 blackout mode`)
    tiles.placeOnRandomTile(Animatronic, sprites.dungeon.floorDark3)
    music.stopAllSounds()
    music.play(music.createSong(assets.song`PIZZA TIME`), music.PlaybackMode.InBackground)
    demo_end = 1
    Summon_endo()
    if (Dusky) {
        tiles.setCurrentTilemap(tilemap`Underground escape fnaf1 night 3 blackout mode`)
        tiles.placeOnRandomTile(Dusky, sprites.dungeon.floorDark3)
        music.stopAllSounds()
        music.play(music.createSong(assets.song`PIZZA TIME`), music.PlaybackMode.InBackground)
        demo_end = 1
        Summon_endo()
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile49`, function (sprite7, location6) {
    if (Night == 3) {
        tiles.setCurrentTilemap(tilemap`Basement power out`)
        tiles.placeOnRandomTile(Animatronic, sprites.dungeon.floorDark0)
        if (Dusky) {
            tiles.setCurrentTilemap(tilemap`Basement power out`)
            tiles.placeOnRandomTile(Dusky, sprites.dungeon.floorDark0)
        }
    }
})
function fnaf14powered () {
    if (Dusky) {
        tiles.setCurrentTilemap(tilemap`Whole map fnaf1 night 4`)
        tiles.placeOnRandomTile(Dusky, assets.tile`myTile16`)
        demo_end = 1
        sprites.destroy(Foxy)
    }
    if (Foxy) {
        sprites.destroy(Animatronic)
        tiles.setCurrentTilemap(tilemap`fnaf night 4`)
        tiles.placeOnRandomTile(Foxy, assets.tile`myTile62`)
        Summon_camera()
        demo_end = 1
    }
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile56`, function (sprite, location) {
    game.showLongText("Hello! Before I tell you what I added, i'd just like to say: I replaced sans with Dusky-Cat. Now Who's Dusky you're asking? an OC of my friend, loria, loria also wrote the script for Dusky, and now to what I added: night 3-4, foxy, Chica, and more tile-maps.", DialogLayout.Full)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    info.changeLifeBy(-1)
    sprite.setVelocity(-50, 0)
})
let projectile: Sprite = null
let demo_end = 0
let _continue = 0
let Night = 0
let Duskyobject: Sprite = null
let Foxy: Sprite = null
let Endo_enemy: Sprite = null
let Camera_Projectile: Sprite = null
let Camera: Sprite = null
let Dusky: Sprite = null
let Animatronic: Sprite = null
let Truth_ending_game_1 = 0
let Spirit: Sprite = null
Spirit = sprites.create(assets.image`Spirit`, SpriteKind.Player)
scene.cameraFollowSprite(Spirit)
controller.moveSprite(Spirit, 100, 100)
music.setVolume(30)
music.play(music.createSong(assets.song`Midnight motorist`), music.PlaybackMode.LoopingInBackground)
tiles.setCurrentTilemap(tilemap`Level Select Menu`)
Render.setViewMode(ViewMode.tilemapView)
tiles.placeOnRandomTile(Spirit, assets.tile`Crying spirit spawn`)
Truth_ending_game_1 = 0
let dungeon_escape_fnaf_1_2_2 = 0
let World_select_Menu = 0
game.setDialogTextColor(1)
game.setDialogFrame(assets.image`text box border`)
game.showLongText("* Hey Hey! Nice job getting to disk 2!", DialogLayout.Bottom)
game.showLongText("Objective: go to night 3", DialogLayout.Top)
info.setLife(3)
