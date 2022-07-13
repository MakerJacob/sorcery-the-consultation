# Now it's python!


# To Do:
# Create our own card data type


card_background = sprites.create(assets.image("""card_background"""), SpriteKind.player)


for i in range(4):
    my_sprite = sprites.create(assets.image("""card_background"""), SpriteKind.player)
    my_sprite.set_position(50 + i * my_sprite.width, 40)
