scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile72`, function (sprite, location) {
    tiles.setCurrentTilemap(tilemap`Parts and service dinning area`)
    tiles.placeOnRandomTile(Animatronic, assets.tile`myTile34`)
})
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    Animatronic.setImage(assets.image`freddy 2`)
    pause(500)
    Animatronic.setImage(assets.image`freddy 5`)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile60`, function (sprite, location) {
    tiles.setCurrentTilemap(tilemap`kitchen 2`)
    tiles.placeOnRandomTile(Animatronic, assets.tile`myTile34`)
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    Animatronic.setImage(assets.image`freddy side 2`)
    pause(500)
    Animatronic.setImage(assets.image`freddy side 3`)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile29`, function (sprite, location) {
    tiles.setCurrentTilemap(tilemap`level18`)
    tiles.placeOnRandomTile(Animatronic, assets.tile`myTile34`)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile97`, function (sprite, location) {
    tiles.setCurrentTilemap(tilemap`Parts And Service`)
    tiles.placeOnRandomTile(Animatronic, assets.tile`myTile34`)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile54`, function (sprite, location) {
    game.splash("These are the rules:\"Don't run. Don't yell. Don't scream. Don't poop on floor. Stay close to Mom. Don't touch Freddy. Don't hit. Leave before dark\" ")
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    Animatronic.setImage(assets.image`freddy side 1`)
    pause(500)
    Animatronic.setImage(assets.image`freddy side 0`)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile66`, function (sprite, location) {
    tiles.setCurrentTilemap(tilemap`right hallway0`)
    tiles.placeOnRandomTile(Animatronic, assets.tile`myTile34`)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile50`, function (sprite, location) {
    tiles.setCurrentTilemap(tilemap`right hallway`)
    tiles.placeOnRandomTile(Animatronic, assets.tile`myTile34`)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile57`, function (sprite, location) {
    game.splash("Huh, It's a poster of me. And I'm tearing my face off? odd.")
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    Animatronic.setImage(assets.image`freddy 0`)
    pause(500)
    Animatronic.setImage(assets.image`freddy 3`)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile101`, function (sprite, location) {
    tiles.setCurrentTilemap(tilemap`Parts And Service`)
    tiles.placeOnRandomTile(Animatronic, assets.tile`myTile102`)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile68`, function (sprite, location) {
	
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile99`, function (sprite, location) {
    tiles.setCurrentTilemap(tilemap`Parts and service dinning area`)
    tiles.placeOnRandomTile(Animatronic, assets.tile`Dinning area from pas trigger`)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile51`, function (sprite, location) {
    tiles.setCurrentTilemap(tilemap`office0`)
    tiles.placeOnRandomTile(Animatronic, assets.tile`myTile34`)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile56`, function (sprite, location) {
    game.splash("Huh, It's a poster of me. I look... Good!")
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile48`, function (sprite, location) {
    tiles.setCurrentTilemap(tilemap`Bathrooms`)
    tiles.placeOnRandomTile(Animatronic, assets.tile`myTile34`)
})
let Animatronic: Sprite = null
Animatronic = sprites.create(assets.image`freddy 1`, SpriteKind.Player)
scene.cameraFollowSprite(Animatronic)
controller.moveSprite(Animatronic)
tiles.setCurrentTilemap(tilemap`Whole map fnaf 1 not including vents`)
tiles.placeOnRandomTile(Animatronic, assets.tile`myTile16`)
