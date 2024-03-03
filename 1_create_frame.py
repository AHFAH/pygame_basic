import pygame

pygame.init()

#화면크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("First Game")

# 이벤트 루프
running = True # 게임 진행 중인지 여부
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

# 게임 종료시 pygame 종료
pygame.quit()