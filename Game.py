import pygame
import random

pygame.init()

def reset():
    pygame.draw.rect(window, (255,0,0),player)
    pygame.draw.rect(window, (0,255,0),food, 10, 10, 10 ,10 ,10 ,10)
    pygame.draw.rect(window, (0,0,255),enemy1)
 




WIDTH = 1000      
HEIGHT = 800       
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Knight_Game")

player = pygame.Rect(500, 400, 40, 40)

player_speed = 5

enemy_speed= 3
bg_image = pygame.transform.scale(pygame.image.load('background0.png'),(WIDTH,HEIGHT))

food = pygame.Rect(random.randint(10, 960), random.randint(10, 760), 25, 25)


enemy1 = pygame.Rect(0, 100, 40, 40)



health = 100

score =0


font=pygame.font.SysFont("Arial",30)

clock = pygame.time.Clock()                    

game_mode = "start"
finish= False

run = True

while run:
    
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                reset()


    window.fill((0, 0, 0))
    window.blit(bg_image, (0,0))
  # player mouve
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed
    #player border
    if player.x > 960:
        player.x -= player_speed
    if player.x <0:
        player.x += player_speed
    if player.y <0:
        player.y += player_speed
    if player.y > 760:
        player.y -= player_speed

    # # enemy_mouve
    if player.x > enemy1.x :
        enemy1.x += enemy_speed 


    if player.x < enemy1.x :
        enemy1.x -= enemy_speed 



    if player.y > enemy1.y :
        enemy1.y += enemy_speed 


    if player.y < enemy1.y :
        enemy1.y -= enemy_speed 


    if pygame.Rect.colliderect(player, food):
        score += 10
        food = pygame.Rect(random.randint(10, 960), random.randint(10, 760), 25, 25)
    if pygame.Rect.colliderect(player, enemy1):
        health -= 20
        enemy1 = pygame.Rect(random.randint(30, 960), random.randint(30, 760), 40, 40)

    if health <= 0:
        finish = True

    pygame.draw.rect(window, (255,0,0),player)
# 
    pygame.draw.rect(window, (255, 215, 0),food, 10, 10, 10 ,10 ,10 ,10)
    pygame.draw.rect(window, (0,0,255),enemy1)

    if finish :
        font_over = pygame.font.SysFont("Arial", 50)
        window.fill((255, 255, 255))
        text_game_over = font.render("GAME OVER", True, (255,0,0))
        window.blit(text_game_over,(500,400))
    font = pygame.font.SysFont("Arial", 25)
    text = font.render(f"Coins: {score} | Health : {health}", True, (255,255,255))
    window.blit(text,(0,0))


    
    pygame.display.update()

pygame.quit()

