import mouse

# Move the mouse to (200, 200)
mouse.move(200, 200, absolute=True, duration=2)

# Drag the mouse from (200, 200) to (300, 300)
mouse.drag(200, 200, 300, 300, absolute=True, duration=1)

# Click the left mouse button
mouse.click('left')
