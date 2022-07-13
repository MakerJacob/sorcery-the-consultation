let my_sprite: Sprite;
//  Now it's python!
//  To Do:
//  Create our own card data type
let card_background = sprites.create(assets.image`card_background`, SpriteKind.Player)
for (let i = 0; i < 4; i++) {
    my_sprite = sprites.create(assets.image`card_background`, SpriteKind.Player)
    my_sprite.setPosition(50 + i * my_sprite.width, 40)
}
function createCard(name: string, health: number, attack: number) {
    let card = sprites.create(assets.image`card_background`, SpriteKind.Player)
    card.setPosition(scene.screenWidth() / 2, scene.screenHeight() / 2)
    sprites.setDataString(card, "name", name)
    sprites.setDataNumber(card, "health", health)
    sprites.setDataNumber(card, "attack", attack)
}

createCard("Potato", 100, 35)
