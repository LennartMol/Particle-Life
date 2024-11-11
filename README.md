# Particle-Life
Python based simulation of Particle Life that uses OpenCL and OpenGL.  

## Example images & video

![Capture9](https://github.com/user-attachments/assets/4816cf37-45c6-4d78-9dc6-99697a3a87b1)
![Capture5](https://github.com/user-attachments/assets/2f2e9a65-7faf-458b-8bc3-11080449597c)
<video src="https://github.com/user-attachments/assets/a6c8b7cb-4d23-474f-bbe3-b1b91518d09a"/>

## Dependencies
Particle-Life uses Pyopencl to calculate forces between particles, thus OpenCL needs to be installed on your system.  
Rendering the particles is done with OpenGL. An older version (OpenGL 2.0) is used for this.   

## Requirements

numpy==1.24.3, pynput==1.7.6, pyopencl==2023.1, pyglet==1.5.27

    pip install -r requirements.txt  
  
## Usage
Run the main.py file to start the simulation.

    python main.py
