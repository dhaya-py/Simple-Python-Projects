import pygame
import random
import math
from pathlib import Path

pygame.init()

# ——— CONFIG ———
WIDTH, HEIGHT = 1080, 1920
FPS = 60

BG_COLOR = (22, 15, 10)
DOT_COLOR = (212, 160, 23)
DOT_SIZE = 2
NUM_DOTS = 800

WORD_DURATION = 2.4   # seconds per lyric line
PAUSE_DURATION = 0.8  # seconds between lines
# ——— END CONFIG ———

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Golden Brown Reel")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 150)

center = (WIDTH // 2, HEIGHT // 2)

# ——— USER SUPPLIED LYRICS ———
# Replace the content of this list with your own copy of the lyrics.
# Each element is one line you want to animate.
LYRICS = [
    "Golden brown",
    "Texture like sun",
    "Lays me down",
    "With my mind she runs",
    "Throughout the night",
    "No need to fight",
    "Never a frown with golden brown",
    "Every time just like the last",
    "On her ship tied to the mast",
    "To distant lands",
    "Takes both my hands",
    "Never a frown with golden brown"
]
# ——— END LYRICS ———

# ——— PARTICLES ———
dots = []
for _ in range(NUM_DOTS):
    dots.append({
        "x": random.uniform(0, WIDTH),
        "y": random.uniform(0, HEIGHT),
        "vx": random.uniform(-0.5, 0.5),
        "vy": random.uniform(-0.5, 0.5),
        "tx": None,
        "ty": None,
    })

def get_text_points(text):
    surface = font.render(text, True, (255, 255, 255))
    # scale for more points
    surface = pygame.transform.scale(surface, (surface.get_width()*2, surface.get_height()*2))
    pts = []
    w, h = surface.get_size()
    surf_array = pygame.PixelArray(surface)
    for px in range(0, w, 6):
        for py in range(0, h, 6):
            if surface.unmap_rgb(surf_array[px, py])[0] > 200:
                pts.append((px - w//2 + center[0], py - h//2 + center[1]))
    del surf_array
    return pts

def assign_targets(points):
    random.shuffle(points)
    for i, dot in enumerate(dots):
        if i < len(points):
            dot["tx"], dot["ty"] = points[i]
        else:
            dot["tx"], dot["ty"] = None, None

def update_dot(d):
    if d["tx"] is not None:
        # glide toward target
        d["x"] += (d["tx"] - d["x"]) * 0.06
        d["y"] += (d["ty"] - d["y"]) * 0.06
    else:
        # drift
        d["x"] += d["vx"]
        d["y"] += d["vy"]

def draw_dots():
    for d in dots:
        pygame.draw.circle(screen, DOT_COLOR, (int(d["x"]), int(d["y"])), DOT_SIZE)

# ——— TIMELINE ———
timeline = []
t = 0.0
for line in LYRICS:
    timeline.append((t, line))
    t += WORD_DURATION + PAUSE_DURATION

total_duration = t
start_time = pygame.time.get_ticks() / 1000.0

current_line_idx = -1

running = True
while running:
    now = pygame.time.get_ticks() / 1000.0
    elapsed = now - start_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)

    # find which lyric line should be active
    new_idx = -1
    for i, (line_time, _) in enumerate(timeline):
        if elapsed >= line_time and elapsed < line_time + WORD_DURATION:
            new_idx = i
            break

    if new_idx != current_line_idx:
        current_line_idx = new_idx
        if current_line_idx != -1:
            text = timeline[current_line_idx][1]
            pts = get_text_points(text)
            assign_targets(pts)

    # update and draw
    for d in dots:
        update_dot(d)
    draw_dots()

    pygame.display.flip()
    clock.tick(FPS)

    if elapsed > total_duration + 1:
        running = False

pygame.quit()
