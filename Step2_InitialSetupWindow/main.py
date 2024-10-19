from settings import *
import moderngl as mgl
import pygame as pg
import sys
from shader_program import ShaderProgram
from scene import Scene
from player import Player

class VoxelEngine:
    def __init__(self):
        # Initialize Pygame and set up the OpenGL context
        pg.init()
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24)
        pg.display.set_mode(WIN_RES, flags=pg.OPENGL | pg.DOUBLEBUF)
        self.ctx = mgl.create_context()

        # Enable various OpenGL features
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE | mgl.BLEND)
        self.ctx.gc_mode = 'auto'

        # Set up the game clock and timing
        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.time = 0

        # Grab the mouse and hide it
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)

        # Initialize the game state
        self.is_running = True
        self.on_init()

    def on_init(self):
        # Initialize the player, shader program, and scene
        self.player = Player(self)
        self.shader_program = ShaderProgram(self)
        self.scene = Scene(self)

    def update(self):
        # Update the player, shader program, and scene
        self.player.update()
        self.shader_program.update()
        self.scene.update()

        # Update the delta time and time
        self.delta_time = self.clock.tick()
        self.time = pg.time.get_ticks() * 0.001
        pg.display.set_caption(f'{self.clock.get_fps() :.0f}')

    def render(self):
        # Clear the screen and render the scene
        self.ctx.clear(color=BG_COLOR)
        self.scene.render()
        pg.display.flip()

    def handle_events(self):
        # Handle user input and quit events
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_running = False

    def run(self):
        # Main game loop
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
        pg.quit()
        sys.exit()

if __name__ == '__main__':
    app = VoxelEngine()
    app.run()