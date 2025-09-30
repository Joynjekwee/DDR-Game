import pygame
import librosa
import numpy as np
import scipy
import random

pygame.init()
pygame.mixer.init()
"Don't.mp3"
"Fetty Wap - Trap Queen (Lyrics).mp3"
audio_file ="Fetty Wap - Trap Queen (Lyrics).mp3"


def bandpass_filter(signal, lowcut, highcut, fs, order=5):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    sos = scipy.signal.butter(order, [low, high], btype='band', output='sos')
    return scipy.signal.sosfilt(sos, signal)


def extract_beats(audio_file):
    y, sr = librosa.load(audio_file)

    lowcut = 40.0
    highcut = 190.0
    y_filtered = bandpass_filter(y, lowcut, highcut, sr)
    # Remove non-finite values
    y_filtered = y_filtered[np.isfinite(y_filtered)]

    hop_length = 128
    onset_env = librosa.onset.onset_strength(y=y_filtered, sr=sr, hop_length=hop_length)
    tempo, beats = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr, hop_length=hop_length)
    return beats, sr


beats, sr = extract_beats(audio_file)

# Save beats into a text file with the updated function
def save_beats_to_file(beats, beats_filename):
    with open(beats_filename, 'w') as f:
        for i in range(len(beats) - 1):
            f.write(f"{beats[i- 7 ]}\n")
           # if (beats[i+1] - beats[i]) > 10:
              ##  new_beat = (beats[i] + beats[i+1]) // 2
                #f.write(f"{new_beat}\n")
        #f.write(f"{beats[-1]}\n")

beats_filename = 'beatmap1.txt'
save_beats_to_file(beats, beats_filename)



#load the beats from the file
def load_beats_from_file(beats_filename):
    with open(beats_filename, 'r') as f:
        beats = [int(line.strip()) for line in f.readlines()]
    return beats

beats = load_beats_from_file(beats_filename)

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("DDR Rhythm Game")

clock = pygame.time.Clock()

key_mapping = {
    pygame.K_UP: "arrow-up.svg",
    pygame.K_DOWN: "arrow-down.svg",
    pygame.K_LEFT: "arrow-left.svg",
    pygame.K_RIGHT: "arrow-right.svg"
}


class Arrow(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, speed, key):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (100, 100))  # Add this line to scale the image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.key = key

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > screen_height:
            self.kill()

def generate_arrow(arrow_images, arrow_speed):
    arrow_image, arrow_key = random.choice(arrow_images)
    x = random.choice([screen_width // 2 - 75, screen_width // 2 - 25, screen_width // 2 + 25, screen_width // 2 + 75])
    return Arrow(arrow_image, x, 0, arrow_speed, arrow_key)

# Update arrow_images to include arrow keys
arrow_images = [
    ('arrow-up.svg', pygame.K_UP),
    ('arrow-down.svg', pygame.K_DOWN),
    ('arrow-left.svg', pygame.K_LEFT),
    ('arrow-right.svg', pygame.K_RIGHT)
]

arrow_speed = 9
arrows = pygame.sprite.Group()

# for the game
score = 0
pygame.mixer.music.load(audio_file)

def get_song_duration(audio_file):
    y, sr = librosa.load(audio_file)
    duration = librosa.get_duration(y=y, sr=sr)
    return duration

# Get the duration of the song (in seconds)
song_duration = get_song_duration(audio_file)

pygame.mixer.music.play(-1)
running = pygame.mixer.music.get_busy()
current_beat_index = 0

while running and pygame.mixer.music.get_busy():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            for arrow in arrows:
                if arrow.rect.y > 500 and arrow.rect.y < 600 and event.key == arrow.key:
                    score += 1
                    arrow.kill()

    screen.fill((50, 99, 145))

    current_time = pygame.time.get_ticks()
    if current_beat_index < len(beats) and current_time > beats[current_beat_index] * 1000 / sr:
        # Generate a new arrow only if there are no arrows on the screen
        if len(arrows) == 0:
            arrow = generate_arrow(arrow_images, arrow_speed)
            arrows.add(arrow)
            current_beat_index += 1

    arrows.update()
    arrows.draw(screen)

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(100)

    if pygame.time.get_ticks() / 1000 >= song_duration:
        running = False

pygame.mixer.music.stop()
pygame.quit()

def save_score_to_file(name, score, filename):
    with open(filename, 'a') as f:
        f.write(f"{name}: {score}\n")


def sort_scores_file(filename):
    scores = []

    with open(filename, 'r') as f:
        for line in f:
            name, score_str = line.strip().split(': ')
            score = int(score_str)
            scores.append((name, score))

    scores.sort(key=lambda x: x[1], reverse=True)

    with open(filename, 'w') as f:
        for name, score in scores:
            f.write(f"{name}: {score}\n")


name = input("Please enter your name: ")

# Replace this with the actual score from your game

# Save the score to a text file with the user's name
filename = "Score_Sheet.txt"
save_score_to_file(name, score, filename)
sort_scores_file(filename)