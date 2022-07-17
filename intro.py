import time

alien = Actor('alien')
alien.pos = 100, 56

WIDTH = 300
HEIGHT = alien.height + 30

def draw():
    screen.fill((128, 0, 0))
    alien.draw()

def update():
    alien.left +=2
    if alien.left > WIDTH:
        alien.right = 0

def on_mouse_down(pos):
    #if alien.collidepoint(pos):
    #    print("Ouch!")
    #else:
    #    print("You missed me!")
    if alien.collidepoint(pos):
        set_alien_hurt()

def set_alien_hurt():
        sounds.eep.play()
        alien.image = 'alien_hurt'
        clock.schedule_unique(set_alien_normal, 1.0)

def set_alien_normal():
        alien.image = 'alien'


