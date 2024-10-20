# PYVOXEL-Procedural-World
A Python-based procedural voxel world generator creates a 3D environment using cubes (voxels) to simulate terrain, structures, and landscapes similar to games like Minecraft. The generator uses algorithms such as Perlin noise, simplex noise, or diamond-square to generate realistic terrain features, including mountains, valleys, plains, and caves, by assigning height and biome values to each voxel. 

# Key features include:
- **3D Chunk-Based Generation**: The world is divided into chunks (typically 16x16x256 or customizable sizes), allowing for infinite generation and efficient memory use.
- **Biomes**: Different biomes such as forests, deserts, oceans, and snowy areas are generated based on noise maps, affecting block types (e.g., grass, sand, stone).
- **Terrain Features**: The system dynamically creates varying elevations, caves, and overhangs, adding natural-looking landscapes with distinct geological formations.
- **Procedural Structures**: The generator can spawn procedurally created structures like trees, villages, or dungeons at random locations within the world.
- **Lighting and Shadows**: Basic ambient lighting is applied to enhance visual realism with simple voxel lighting models.
- **Player Interaction**: The player can mine and place blocks, interacting with the voxel world in real-time, with modifications seamlessly integrated into the terrain generation.

This procedural voxel world generation code can be implemented in Python using libraries like **Pygame** or **PyOpenGL** for rendering, or using **numPy** for efficient voxel storage and manipulation.

# Step 1
- Initialization:

> The program initializes Pygame and sets up an OpenGL 3.3 core profile context for rendering 3D graphics.
> The window resolution is defined in settings.py as 1280x720, with background color specified in RGB format using the glm library.
- Rendering Context:

> ModernGL is used to create an OpenGL rendering context (self.ctx).
> The engine enables features such as depth testing, face culling, and blending, ensuring correct rendering of 3D objects, handling occlusions, and optimizing performance.
- Main Loop:

> The run method manages the main game loop. It continuously handles events (like closing the window or pressing escape), updates the frame (calculating the delta time and displaying the FPS), and renders the scene.
> The rendering process clears the screen with a set background color and flips the display buffer to update the visuals.
- Event Handling:

> User inputs, such as quitting the program or pressing escape, are handled in the handle_events method.
- Output Window:
![Screenshot 2024-10-19 143038](https://github.com/user-attachments/assets/706d52b8-8834-4715-ad58-a70b2886630b)

# Step 2
- Main Engine (main.py):

> Initializes the Pygame window with OpenGL 3.3 and sets up the game context using ModernGL.
> Controls the main game loop, updating the player, scene, and rendering each frame.
> Enables mouse capture and hides the cursor for a more immersive 3D experience.
> Manages player input for interaction and movement, as well as shader updates for rendering.
- Camera System (camera.py):

> Defines a 3D camera system, where the camera position is controlled by yaw (horizontal) and pitch (vertical) angles.
> Supports camera movement along the x, y, and z axes, and updates the view matrix based on player movements.
> Implements smooth rotation and clamping for pitch to prevent flipping.
- Player (player.py):

> Inherits from the Camera class to allow the player to control camera movement.
> Keyboard input handles forward/backward and left/right movement, while mouse input adjusts the camera's rotation.
> Supports vertical movement (up/down) with additional keys.
- Scene Management (scene.py):

> Manages the rendering of different objects in the scene, starting with a simple quad (2D plane).
> Updates and renders the scene based on the player's position and view direction.
- Shader Program (shader_program.py):

> Implements a basic OpenGL shader system for rendering.
> Loads vertex and fragment shaders from external files (quad.vert and quad.frag) to handle 3D object transformations and coloring.
> The shader program applies projection, view, and model matrices to transform object positions in 3D space.
- Shaders:

> Vertex Shader (quad.vert): Transforms the positions of vertices using model, view, and projection matrices. Passes the color data to the fragment shader.
> Fragment Shader (quad.frag): Outputs the color for each pixel, controlling the visual appearance of objects in the scene.
- Settings (settings.py):

> Defines important configuration values like screen resolution, field of view (FOV), camera movement speed, and mouse sensitivity.
> Configures parameters for perspective projection and defines basic colors for the background and objects.
- Output Window:
![VID-20241020-WA0022_1](https://github.com/user-attachments/assets/2bebdb70-348a-4b2d-b291-b772036352a2)

# Step 3
- VoxelEngine (Main.py):

> Initializes the game, handles OpenGL context, and manages the game loop.
> Includes essential functions like updating, rendering, and event handling (player inputs, quitting).
> Uses the moderngl library for OpenGL rendering, enabling 3D graphics, depth testing, and face culling for efficient rendering.
- Player (Controls):

> Provides first-person camera movement, controlled by keyboard (WASD for movement, Q/E for up/down) and mouse for looking around.
> Inherits from a Camera class and allows the player to navigate through the 3D world.
- Textures (Voxel Texturing):

> Manages loading and applying textures to the voxel world.
> Loads texture images from assets, flips them to correct orientation, and applies them using OpenGL texture units. Filters and mipmaps are applied to optimize texture rendering.
- Chunk (Procedural Generation):

> Generates voxel data for chunks using simplex noise for procedural terrain creation.
> Builds voxel arrays, where each chunk is a 3D grid of blocks. Uses noise-based values to create height variations and basic terrain features.
> Chunks are rendered via mesh data generated from the voxel array, and the mesh is updated dynamically.
- Procedural Generation:
> - Noise-Based Terrain: The terrain is generated using simplex noise to simulate natural elevation. The system assigns voxel types (air or solid blocks) based on the noise value, creating varying terrain height within each chunk.

> - Chunk Management: Each chunk is a fixed-size 3D grid (e.g., 16x16x16 blocks) that stores voxel data. The chunks are dynamically created as the player moves through the world, though chunk loading/unloading based on player position could be added for optimization.
- Output Window:
![Screenshot 2024-10-20 225053](https://github.com/user-attachments/assets/689df152-7370-4a38-b119-c16bf3325f12)

# Step 4
- Rendering Pipeline:

> Utilizes ModernGL for rendering voxels, ensuring performance optimizations via efficient OpenGL techniques.
> Supports depth testing, face culling, and blending, improving rendering quality and performance.
> Textures are processed with anisotropic filtering and mipmaps to provide smooth visual details at varying distances.
- Chunk-Based World Generation:

> The world is composed of multiple chunks (each being a grid of voxels), which are independently built and rendered.
> Voxel data is stored in a 3D grid within each chunk, and mesh generation is performed for each chunk to optimize rendering.
> Supports a flexible and expandable system for adding new voxel types and properties.
- Player Controls and Camera System:

> Features smooth FPS-style movement with adjustable player speed, rotation, and mouse sensitivity.
> Camera FOV (Field of View) and aspect ratio are calculated dynamically for an immersive 3D experience.
> Player interactions are facilitated through continuous updates to the scene, which ensure real-time feedback.
- Texture Management:

> Efficient texture loading using Pygame to import and apply textures from image files.
> Supports flipping and resizing textures, and converts them to ModernGL-compatible formats for shader usage.
> Mipmapping ensures textures scale appropriately at different distances.
- Performance Optimizations:

> Delta time calculations and frame-rate monitoring ensure smooth updates regardless of the system performance.
> Memory management techniques, such as garbage collection, ensure efficient resource utilization.
- Output Window:
![Screenshot 2024-10-20 225005](https://github.com/user-attachments/assets/9fbed401-f06e-4ebf-9524-e377d9c2cdaf)
