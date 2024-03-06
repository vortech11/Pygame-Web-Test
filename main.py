import asyncio, pygame

# Try to declare all your globals at once to facilitate compilation later.
BLACK=(0,0,0)
BLUE=(0,0,255)

# Do init here
# Load any assets right now to avoid lag at runtime or network errors.
pygame.init()
DISPLAY=pygame.display.set_mode((500,400),0,32)

async def main():
    global BLACK, BLUE

    while True:
        
        DISPLAY.fill(BLACK)

        pygame.draw.rect(DISPLAY,BLUE,(200,150,100,50))
        
        # Do your rendering here, note that it's NOT an infinite loop,
        # and it is fired only when VSYNC occurs
        # Usually 1/60 or more times per seconds on desktop
        # could be less on some mobile devices

        
        # pygame.display.update() should go right next line
        pygame.display.update()
        await asyncio.sleep(0)  # Very important, and keep it 0


# This is the program entry point:
asyncio.run(main())

# Do not add anything from here, especially sys.exit/pygame.quit
# asyncio.run is non-blocking on pygame-wasm and code would be executed
# right before program start main()