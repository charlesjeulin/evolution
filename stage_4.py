import pygame
import random
from io import BytesIO
import matplotlib.pyplot as plt


SPAWN_SCREEN_WIDTH = 980
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 1100
CREATURE_SIZE = 20
BLUE_COLOR = (70, 130, 180)
GREEN_COLOR = (34, 139, 34)
RED_COLOR = (220, 20, 60)
ORANGE_COLOR = (255, 140, 0)
INITIAL_FPS = 30

# GEN 1 - BLUE
B1 = 1.0
D1 = 0.1
R1 = 0.05
M12 = 0.1
M13 = 0.1

# GEN 2-1 - GREEN
B2 = 0.0
D2 = 0.1
R2 = 0.05

# GEN 2-2 - RED
B3 = 0.0
D3 = 0.05
R3 = 0.05
M34 = 0.05

# GEN 3 - ORANGE
B4 = 0.0
D4 = 0.05
R4 = 0.1


class Creature:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)
        self.color = color

    def move(self):
        self.x += self.vx
        self.y += self.vy

        if self.x < 0 or self.x > SPAWN_SCREEN_WIDTH - CREATURE_SIZE:
            self.vx = -self.vx
        if self.y < 0 or self.y > SCREEN_HEIGHT - CREATURE_SIZE:
            self.vy = -self.vy

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, (self.x, self.y, CREATURE_SIZE, CREATURE_SIZE))


def plot_graph(frame_count, num_creatures_gen_1_blue, num_creatures_gen_21_green, num_creatures_gen_22_red,
               num_creatures_gen_3_orange):
    plt.figure(figsize=(6, 4))
    plt.plot(frame_count, num_creatures_gen_1_blue, color='steelblue', label='Blue Population')
    plt.plot(frame_count, num_creatures_gen_21_green, color='forestgreen', label='Green Population')
    plt.plot(frame_count, num_creatures_gen_22_red, color='crimson', label='Red Population')
    plt.plot(frame_count, num_creatures_gen_3_orange, color='darkorange', label='Orange Population')

    plt.xlabel('Time (frames)')
    plt.ylabel('Number of Creatures')
    plt.title('Evolution of Creature Populations')
    plt.legend()
    plt.grid(False)
    plt.xlim(0, max(frame_count))
    plt.ylim(0, max(max(num_creatures_gen_1_blue), max(num_creatures_gen_21_green), max(num_creatures_gen_22_red),
                    max(num_creatures_gen_3_orange)))
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().get_xaxis().tick_bottom()
    plt.gca().get_yaxis().tick_left()

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return pygame.image.load(buf)


def run_simulation():
    creatures_gen_1_blue = []
    creatures_gen_21_green = []
    creatures_gen_22_red = []
    creatures_gen_3_orange = []
    num_creatures_gen_1_blue = []
    num_creatures_gen_21_green = []
    num_creatures_gen_22_red = []
    num_creatures_gen_3_orange = []
    frame_count = []
    fps = INITIAL_FPS

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
                elif event.key == pygame.K_r:
                    return True

        # Death
        for creature in creatures_gen_1_blue[:]:
            if random.random() < D1:
                creatures_gen_1_blue.remove(creature)
            else:
                creature.move()
        for creature in creatures_gen_21_green[:]:
            if random.random() < D2:
                creatures_gen_21_green.remove(creature)
            else:
                creature.move()
        for creature in creatures_gen_22_red[:]:
            if random.random() < D3:
                creatures_gen_22_red.remove(creature)
            else:
                creature.move()
        for creature in creatures_gen_3_orange[:]:
            if random.random() < D4:
                creatures_gen_3_orange.remove(creature)
            else:
                creature.move()

        # Reproduction and Mutation
        for creature in creatures_gen_1_blue[:]:
            if random.random() < R1:
                if random.random() < M12:
                    new_creature = Creature(creature.x, creature.y, GREEN_COLOR)
                    creatures_gen_21_green.append(new_creature)
                elif random.random() < M13:
                    new_creature = Creature(creature.x, creature.y, RED_COLOR)
                    creatures_gen_22_red.append(new_creature)
                else:
                    new_creature = Creature(creature.x, creature.y, BLUE_COLOR)
                    creatures_gen_1_blue.append(new_creature)
        for creature in creatures_gen_21_green[:]:
            if random.random() < R2:
                new_creature = Creature(creature.x, creature.y, GREEN_COLOR)
                creatures_gen_21_green.append(new_creature)
        for creature in creatures_gen_22_red[:]:
            if random.random() < R3:
                if random.random() < M34:
                    new_creature = Creature(creature.x, creature.y, ORANGE_COLOR)
                    creatures_gen_3_orange.append(new_creature)
                else:
                    new_creature = Creature(creature.x, creature.y, RED_COLOR)
                    creatures_gen_22_red.append(new_creature)
        for creature in creatures_gen_3_orange[:]:
            if random.random() < R4:
                new_creature = Creature(creature.x, creature.y, ORANGE_COLOR)
                creatures_gen_3_orange.append(new_creature)

        # Birth
        if random.random() < B1:
            new_creature = Creature(random.randint(0, SPAWN_SCREEN_WIDTH - CREATURE_SIZE), random.randint(0, SCREEN_HEIGHT - CREATURE_SIZE), BLUE_COLOR)
            creatures_gen_1_blue.append(new_creature)
        if random.random() < B2:
            new_creature = Creature(random.randint(0, SPAWN_SCREEN_WIDTH - CREATURE_SIZE), random.randint(0, SCREEN_HEIGHT - CREATURE_SIZE), GREEN_COLOR)
            creatures_gen_21_green.append(new_creature)
        if random.random() < B3:
            new_creature = Creature(random.randint(0, SPAWN_SCREEN_WIDTH - CREATURE_SIZE), random.randint(0, SCREEN_HEIGHT - CREATURE_SIZE), RED_COLOR)
            creatures_gen_22_red.append(new_creature)
        if random.random() < B4:
            new_creature = Creature(random.randint(0, SPAWN_SCREEN_WIDTH - CREATURE_SIZE), random.randint(0, SCREEN_HEIGHT - CREATURE_SIZE), ORANGE_COLOR)
            creatures_gen_3_orange.append(new_creature)

        frame_count.append(len(frame_count) + 1)
        num_creatures_gen_1_blue.append(len(creatures_gen_1_blue))
        num_creatures_gen_21_green.append(len(creatures_gen_21_green))
        num_creatures_gen_22_red.append(len(creatures_gen_22_red))
        num_creatures_gen_3_orange.append(len(creatures_gen_3_orange))

        screen.fill((255, 255, 255))

        pygame.draw.rect(screen, (240, 230, 215), (0, 0, SPAWN_SCREEN_WIDTH, SCREEN_HEIGHT))

        for creature in creatures_gen_1_blue:
            creature.draw(screen)
        for creature in creatures_gen_21_green:
            creature.draw(screen)
        for creature in creatures_gen_22_red:
            creature.draw(screen)
        for creature in creatures_gen_3_orange:
            creature.draw(screen)

        num_fps_text = font.render(f'FPS: {fps}', True, (0, 0, 0))
        graph_surface = pygame.transform.scale(
            plot_graph(frame_count, num_creatures_gen_1_blue, num_creatures_gen_21_green, num_creatures_gen_22_red,
                       num_creatures_gen_3_orange),
            (600, 400)
        )
        screen.blit(num_fps_text, (1050, 940))
        screen.blit(graph_surface, (SCREEN_WIDTH - 620, 20))

        pygame.display.flip()
        clock.tick(fps)

    return False


def main():
    pygame.init()
    global screen, clock, font
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Simulation de l'évolution")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)

    while run_simulation():
        pass

    pygame.quit()


if __name__ == "__main__":
    main()
