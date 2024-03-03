import pygame

pygame.init()

#화면크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("First Game")

# FPS 설정
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\jiyou\\OneDrive\\Desktop\\MyCoding\\AHFAH\\파이썬 게임\\pygame_basic\\background.png")

# 캐릭터 불러오기 
character = pygame.image.load("C:\\Users\\jiyou\\OneDrive\\Desktop\\MyCoding\\AHFAH\\파이썬 게임\\pygame_basic\\character.png")
character_size = character.get_rect().size # 이미지의 크기
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.5

# 적 캐릭터 생성
enemy = pygame.image.load("C:\\Users\\jiyou\\OneDrive\\Desktop\\MyCoding\\AHFAH\\파이썬 게임\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size # 이미지의 크기
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)

# 이벤트 루프
running = True # 게임 진행 중인지 여부
while running:
  dt = clock.tick(60)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        to_x -= character_speed
      elif event.key == pygame.K_RIGHT:
        to_x += character_speed
      elif event.key == pygame.K_UP:
        to_y -= character_speed
      elif event.key == pygame.K_DOWN:
        to_y += character_speed
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        to_x = 0
      elif event.key == pygame.K_UP or event.key == pygame.K_DOWN: 
        to_y = 0

  character_x_pos += to_x * dt
  character_y_pos += to_y * dt

# 가로 경계값 처리
  if character_x_pos < 0:
    character_x_pos = 0
  elif character_x_pos > screen_width - character_width:
    character_x_pos = screen_width - character_width

# 세로 경계값 처리
  if character_y_pos < 0:
    character_y_pos = 0
  elif character_y_pos > screen_height - character_height:
    character_y_pos = screen_height - character_height

# 충돌 처리를 위한 rect 업데이트
  character_rect = character.get_rect() # rect값은 계속 고정되어 있기 때문에 달라지는 캐릭터의 좌표를 반영함
  character_rect.left = character_x_pos
  character_rect.top = character_y_pos

  enemy_rect = enemy.get_rect()
  enemy_rect.left = enemy_x_pos
  enemy_rect.top = enemy_y_pos

# 충돌 체크
  if character_rect.colliderect(enemy_rect):
    print("충돌 감지")
    running = False

# 배경 그리기
  screen.blit(background, (0, 0))
  screen.blit(character, (character_x_pos, character_y_pos))
  screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
  pygame.display.update() # 게임화면을 프레임마다 다시 그리기

# 게임 종료시 pygame 종료
pygame.quit()