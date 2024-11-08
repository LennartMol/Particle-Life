# Particle-Life
Python based simulation of Particle Life that uses OpenCL and OpenGL.  

## Dependencies
Particle-Life uses Pyopencl to calculate forces between particles, thus OpenCL needs to be installed on your system.  
Rendering the particles is done with OpenGL. An older version (OpenGL 2.0) is used for this.   

## Example images & video

![Capture9](https://github.com/user-attachments/assets/4816cf37-45c6-4d78-9dc6-99697a3a87b1)
![Capture5](https://github.com/user-attachments/assets/2f2e9a65-7faf-458b-8bc3-11080449597c)
<video src="https://github.com/user-attachments/assets/a6c8b7cb-4d23-474f-bbe3-b1b91518d09a"/>

## Python packages

numpy (1.24.3)  

    pip install numpy  
  
pynput (1.7.6)  

    pip install pynput
  
pyopencl (2023.1)

    pip install pyopencl

pyglet (1.5.27 - an older maintenance version)

      git clone https://github.com/pyglet/pyglet.git  
      
      cd pyglet  
      
      git checkout pyglet-1.5-maintenance  
      
      python setup.py install --user  
