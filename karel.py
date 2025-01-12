# place contents of animation.txt up here

i = 0
f = 0
running = 1

# replace "FRAMES" with the number of the final "a(number)", plus one.
while running == 1 and i < 256 and f < FRAMES:
    paint('rgb({0})'.format(str(globals().get('a%d' % f)[i])[1:-1]))
    move()
    i += 1
    if facing_east() and front_is_blocked():
        paint('rgb({0})'.format(str(globals().get('a%d' % f)[i])[1:-1]))
        turn_right()
        if front_is_clear():
            move()
            i += 1
            turn_right()
            while front_is_clear():
                move()
            turn_around()
        else:
            turn_right()
    if i == 255:
        f += 1
        i = 0
        while front_is_clear():
            move()
        turn_right()
        while front_is_clear():
            move()
        turn_right()
