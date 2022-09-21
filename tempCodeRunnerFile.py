def update_score():
    global score
    if p.colliderect(c):
        score+=1
        c.pos=(randint(64,WIDTH-64),randint(64,HEIGHT-64))