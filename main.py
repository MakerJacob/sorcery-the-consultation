# Now it's python!

# To Do:
# Create our own card data type


card_background = sprites.create(assets.image("""card_background"""), SpriteKind.player)



for i in range(4):
    my_sprite = sprites.create(assets.image("""card_background"""), SpriteKind.player)
    my_sprite.set_position(50 + i * my_sprite.width, 40)



def createCard(name: string, health: int, attack: int):
    card = sprites.create(assets.image("""card_background"""), SpriteKind.player)
    card.set_position(scene.screen_width() / 2, scene.screen_height() / 2)
    sprites.set_data_string(card, "name", name)
    sprites.set_data_number(card, "health", health)
    sprites.set_data_number(card, "attack", attack)
    

createCard('Potato', 100, 35)