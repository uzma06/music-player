import pygame
import os

pygame.init()

# Set the window size
win_width = 800
win_height = 600

# Set the colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set the font
font = pygame.font.SysFont('arial', 24)
# Set the window caption
pygame.display.set_caption('Music Player')

# Set the window size and make it visible
win = pygame.display.set_mode((win_width, win_height))
pygame.display.flip()

# Set the path to the music folder
music_folder ="G:\Download\Received"
# Get a list of all the music files in the music folder
music_files = [f for f in os.listdir(music_folder) if f.endswith('.mp3')]

# Set the current song index to 0
current_song_index = 0

# Load the current song
pygame.mixer.music.load(os.path.join(music_folder, music_files[current_song_index]))

# Set the volume
pygame.mixer.music.set_volume(0.5)

# Play the music
pygame.mixer.music.play()

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Pause or unpause the music
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_LEFT:
                # Skip to the previous song
                current_song_index -= 1
                if current_song_index < 0:
                    current_song_index = len(music_files) - 1
                pygame.mixer.music.load(os.path.join(music_folder, music_files[current_song_index]))
                pygame.mixer.music.play()
            elif event.key == pygame.K_RIGHT:
                # Skip to the next song
                current_song_index += 1
                if current_song_index >= len(music_files):
                    current_song_index = 0
                pygame.mixer.music.load(os.path.join(music_folder, music_files[current_song_index]))
                pygame.mixer.music.play()
    
    # Clear the screen
    win.fill(white)
    
    # Display the current song name
    current_song_name = music_files[current_song_index]
    current_song_text = font.render(current_song_name, True, black)
    current_song_rect = current_song_text.get_rect()
    current_song_rect.center = (win_width // 2, win_height // 2)
    win.blit(current_song_text, current_song_rect)
    
    # Update the display
    pygame.display.update()