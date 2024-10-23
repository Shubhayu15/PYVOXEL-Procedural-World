import pygame
import sys
import subprocess  # Import subprocess to run the external script

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PYVOXEL")

# Load background image (ensure bg.png is in the same directory)
background_image = pygame.image.load("images/bg.png")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (96, 96, 96)

# Load custom font (ensure "myfont.ttf" is in the same directory)
font_path = "font/Filepile.otf"  # Replace with the path to your font file
font_large = pygame.font.Font(font_path, 100)  # Large font for the title
font_medium = pygame.font.Font(font_path, 30)  # Medium font for buttons
font_small = pygame.font.Font(font_path, 20)   # Small font for the version

# Button class
class Button:
    def __init__(self, text, pos, width, height, action=None):
        self.text = text
        self.pos = pos
        self.width = width
        self.height = height
        self.action = action
        self.rect = pygame.Rect(pos[0], pos[1], width, height)
        self.color = GRAY

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = font_medium.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if self.action:
                    self.action()

# Button actions
def play_game():
    print("Launching the game...")
    pygame.quit()  # Quit the menu
    subprocess.Popen(["python", "main.py"])  # Launch main.py in a new process
    sys.exit()  # Ensure the menu is closed after launching the game

def exit_game():
    pygame.quit()
    sys.exit()

# Create buttons
play_button = Button("Play", (WIDTH // 2 - 100, HEIGHT // 2 - 50), 200, 60, play_game)
exit_button = Button("Exit", (WIDTH // 2 - 100, HEIGHT // 2 + 30), 200, 60, exit_game)

# Main loop
running = True
while running:
    # Draw background image
    screen.blit(background_image, (0, 0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        play_button.check_click(event)
        exit_button.check_click(event)

    # Draw title "PYVOXEL"
    title_surface = font_large.render("PYVOXEL", True, WHITE)
    title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(title_surface, title_rect)

    # Draw buttons
    play_button.draw(screen)
    exit_button.draw(screen)

    # Draw version label "version alpha 1.0" at bottom right
    version_surface = font_small.render("version alpha 1.0", True, WHITE)
    version_rect = version_surface.get_rect(bottomright=(WIDTH - 20, HEIGHT - 20))
    screen.blit(version_surface, version_rect)

    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()
