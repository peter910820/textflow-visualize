import bext, random, shutil, sys, time

SPEED = float(input("Please input speed: "))
DENSITY = float(input("Please input density: "))

WIDTH = shutil.get_terminal_size()[0] - 1
columns = [0] * WIDTH

MIN_FLOW_LENGTH, MAX_FLOW_LENGTH = 5, 10
FLOW_CHARS = ['0', '1']

try:
    bext.fg('green')
    while True:
        for i in range(WIDTH):
            if columns[i] == 0:
                if random.random() <= DENSITY:
                    columns[i] = random.randint(MIN_FLOW_LENGTH, MAX_FLOW_LENGTH)
            if columns[i] > 0:
                print(random.choice(FLOW_CHARS), end='')
                columns[i] -= 1
            else:
                print(' ', end='')
        print(end='\n')	
        sys.stdout.flush()	
        time.sleep(SPEED)

except KeyboardInterrupt:
    sys.exit()