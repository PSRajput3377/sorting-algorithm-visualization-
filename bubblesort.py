import random
import time

import pygame

# Initialize pygame
pygame.init()

# Constants
SIZE = 200
GAP = 4
WIDTH = GAP * SIZE + 1
HEIGHT = SIZE + 1

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Setup the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Sort Visualization")

# Initialize the array
numbers = list(range(1, SIZE + 1))
random.seed(time.time())
random.shuffle(numbers)

def draw_numbers():
    screen.fill(WHITE)
    for i in range(SIZE):
        pygame.draw.line(screen, BLACK, (GAP * i + 1, HEIGHT), (GAP * i + 1, HEIGHT - numbers[i]))
    pygame.display.update()

def swap(i, j):
    # Draw the numbers before swapping
    screen.fill(WHITE)
    draw_numbers()
    
    # Draw the swapped lines
    pygame.draw.line(screen, GREEN, (GAP * i + 1, HEIGHT), (GAP * i + 1, HEIGHT - numbers[i]))
    pygame.draw.line(screen, GREEN, (GAP * j + 1, HEIGHT), (GAP * j + 1, HEIGHT - numbers[j]))
    pygame.display.update()
    pygame.time.delay(200)  # Delay to visualize the swap

    # Swap values
    numbers[i], numbers[j] = numbers[j], numbers[i]

    # Draw the numbers after swapping
    screen.fill(WHITE)
    draw_numbers()
    pygame.draw.line(screen, GREEN, (GAP * i + 1, HEIGHT), (GAP * i + 1, HEIGHT - numbers[i]))
    pygame.draw.line(screen, GREEN, (GAP * j + 1, HEIGHT), (GAP * j + 1, HEIGHT - numbers[j]))
    pygame.display.update()
    pygame.time.delay(200)  # Delay to visualize the swap

def bubble_sort():
    for i in range(SIZE):
        for j in range(SIZE - i - 1):
            if numbers[j] > numbers[j + 1]:
                swap(j, j + 1)

def main():
    # Initial plot
    draw_numbers()
    pygame.time.delay(2000)  # Delay to visualize the initial state

    # Start Bubble Sort
    bubble_sort()

    # Print the sorted array
    print("Sorted array:", numbers)

    # Wait for a while before closing
    pygame.time.delay(5000)

    # Quit pygame
    pygame.quit()

if __name__ == "__main__":
    main()
