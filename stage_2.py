import pygame
import random
from io import BytesIO
import matplotlib.pyplot as plt


SPAWN_SCREEN_WIDTH = 980
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 1100
CREATURE_SIZE = 20
CREATURE_COLOR = (141, 191, 169)
INITIAL_FPS = 30


class Creature:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)
        self.color = CREATURE_COLOR

    def move(self):
        self.x += self.vx
        self.y += self.vy

        if self.x < 0 or self.x > SPAWN_SCREEN_WIDTH - CREATURE_SIZE:
            self.vx = -self.vx
        if self.y < 0 or self.y > SCREEN_HEIGHT - CREATURE_SIZE:
            self.vy = -self.vy

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, (self.x, self.y, CREATURE_SIZE, CREATURE_SIZE))


def plot_graph_1(frame_count, num_creatures):
    plt.figure(figsize=(6, 4))
    plt.plot(frame_count, num_creatures, color='blue')
    plt.xlabel('Temps (frames)')
    plt.ylabel('Nombre de créatures')
    plt.title('Évolution du nombre de créatures')
    plt.grid(False)
    plt.xlim(0, max(frame_count))
    plt.ylim(0, max(num_creatures))
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().get_xaxis().tick_bottom()
    plt.gca().get_yaxis().tick_left()

    if len(frame_count) > 1:
        new_index = len(frame_count) - 1
        plt.scatter(frame_count[new_index], num_creatures[new_index], color='green', marker='o', s=50, zorder=5)

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return pygame.image.load(buf)


def plot_graph_2(num_creatures, delta_values):
    plt.figure(figsize=(6, 4))
    plt.plot(num_creatures, delta_values, color='red')
    plt.xlabel('Nombre de créatures')
    plt.ylabel('Equilibre (delta)')
    plt.title('Évolution de l\'équilibre (delta)')
    plt.grid(False)
    plt.xlim(0, max(num_creatures))
    plt.ylim(min(delta_values), max(delta_values))
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().get_xaxis().tick_bottom()
    plt.gca().get_yaxis().tick_left()

    plt.axhline(0, color='black', linewidth=0.5)

    if len(num_creatures) > 1:
        new_index = len(num_creatures) - 1
        plt.scatter(num_creatures[new_index], delta_values[new_index], color='green', marker='o', s=50, zorder=5)

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return pygame.image.load(buf)


def run_simulation():
    global BIRTH_CHANCE, DEATH_CHANCE, REPRODUCTION_CHANCE
    creatures = []
    frame_count = []
    num_creatures = []
    delta_values = []
    fps = INITIAL_FPS

    for _ in range(int(2)):
        new_creature = Creature(random.randint(0, SPAWN_SCREEN_WIDTH - CREATURE_SIZE), random.randint(0, SCREEN_HEIGHT - CREATURE_SIZE))
        creatures.append(new_creature)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    fps += 10
                elif event.key == pygame.K_DOWN:
                    fps = max(10, fps - 10)
                elif event.key == pygame.K_b:
                    BIRTH_CHANCE += 0.01 if BIRTH_CHANCE < 1.0 else 0
                elif event.key == pygame.K_v:
                    BIRTH_CHANCE -= 0.01 if BIRTH_CHANCE > 0.0 else 0
                elif event.key == pygame.K_d:
                    DEATH_CHANCE += 0.01 if DEATH_CHANCE < 1.0 else 0
                elif event.key == pygame.K_s:
                    DEATH_CHANCE -= 0.01 if DEATH_CHANCE > 0.0 else 0
                elif event.key == pygame.K_j:
                    REPRODUCTION_CHANCE += 0.01 if REPRODUCTION_CHANCE < 1.0 else 0
                elif event.key == pygame.K_h:
                    REPRODUCTION_CHANCE -= 0.01 if REPRODUCTION_CHANCE > 0.0 else 0
                elif event.key == pygame.K_r:
                    return True

        for creature in creatures[:]:
            if random.random() < DEATH_CHANCE:
                creatures.remove(creature)
            else:
                creature.move()

        for creature in creatures[:]:
            if random.random() < REPRODUCTION_CHANCE:
                new_creature = Creature(creature.x, creature.y)
                creatures.append(new_creature)

        if random.random() < BIRTH_CHANCE:
            new_creature = Creature(random.randint(0, SPAWN_SCREEN_WIDTH - CREATURE_SIZE), random.randint(0, SCREEN_HEIGHT - CREATURE_SIZE))
            creatures.append(new_creature)

        num_creature_current = len(creatures)
        delta = BIRTH_CHANCE + num_creature_current * (REPRODUCTION_CHANCE - DEATH_CHANCE)
        delta_values.append(delta)

        frame_count.append(len(frame_count) + 1)
        num_creatures.append(len(creatures))

        screen.fill((255, 255, 255))

        pygame.draw.rect(screen, (240, 230, 215), (0, 0, SPAWN_SCREEN_WIDTH, SCREEN_HEIGHT))

        for creature in creatures:
            creature.draw(screen)

        num_creatures_text = font.render(f'Creatures: {len(creatures)}', True, (0, 0, 0))
        avg_creatures_text = font.render(f'Average: {sum(num_creatures) / len(num_creatures):.2f}', True, (0, 0, 0))
        num_fps_text = font.render(f'FPS: {fps}', True, (0, 0, 0))
        birth_rate_text = font.render(f'Birth chance B(+) / V(-): {BIRTH_CHANCE:.2f}', True, (0, 0, 0))
        death_rate_text = font.render(f'Death chance D(+) / S(-): {DEATH_CHANCE:.2f}', True, (0, 0, 0))
        replication_rate_text = font.render(f'Replication chance J(+) / H(-): {REPRODUCTION_CHANCE:.2f}', True, (0, 0, 0))

        screen.blit(num_creatures_text, (1050, 860))
        screen.blit(avg_creatures_text, (1050, 900))
        screen.blit(num_fps_text, (1050, 940))
        screen.blit(birth_rate_text, (1050, 980))
        screen.blit(death_rate_text, (1050, 1020))
        screen.blit(replication_rate_text, (1050, 1060))

        graph_1_surface = pygame.transform.scale(plot_graph_1(frame_count, num_creatures), (600, 400))
        graph_2_surface = pygame.transform.scale(plot_graph_2(num_creatures, delta_values), (600, 400))
        screen.blit(graph_1_surface, (SCREEN_WIDTH - 620, 20))
        screen.blit(graph_2_surface, (SCREEN_WIDTH - 620, 450))

        print(f'Delta: {delta:.2f} - Num creatures: {num_creature_current} - FPS: {fps} - Average: {sum(num_creatures) / len(num_creatures):.2f} - Creatures: {len(creatures)}')

        pygame.display.flip()
        clock.tick(fps)

    return False


def main():
    pygame.init()
    global screen, clock, font, BIRTH_CHANCE, DEATH_CHANCE, REPRODUCTION_CHANCE
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Simulation de l'évolution")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)

    BIRTH_CHANCE = 1.0
    DEATH_CHANCE = 0.2
    REPRODUCTION_CHANCE = 0.2

    while run_simulation():
        pass

    pygame.quit()


if __name__ == "__main__":
    main()
