from tkinter import Tk, Canvas, Label, StringVar

class Window():
    
    def __init__(self, particle_canvas, title='Particle Life', size = {'Width': 1200, 'Height': 1200}, background='black'):
        self.size = size
        self.title = title
        self.backgrond = background

        # Create window
        self.window=Tk()
        self.window.title(title)

        # Create canvas 
        self.canvas = Canvas(width=size['Width'], height=size['Height'], bg=background)
        self.canvas.pack()

        # Create FPS text
        self.fps_label = Label(self.canvas, text = "FPS: 000", font=('serif', 10, 'bold'))
        self.fps_label.config(bg='black', fg='white')
        self.fps_label.pack()
        self.canvas.create_window(32, 13, window=self.fps_label)

        # Particle canvas
        self.particleCanvas = particle_canvas

    def updateFPS(self, fps):
        if fps < 10:
            self.fps_label.config(text="FPS: 00" + str(fps))
        elif fps < 100:
            self.fps_label.config(text="FPS: 0" + str(fps))
        else:
            self.fps_label.config(text="FPS: " + str(fps))
    
    def updateParticlePositions(self):
        object = 2 # 1 is fps text
        for prtcl in self.particleCanvas.particles:
            
            if(self.particleCanvas.border):
                # revert velocity if particle is out of bounds
                prtcl.posX += prtcl.velX
                if prtcl.posX > self.particleCanvas.canvasSize['Width'] or prtcl.posX < 0:
                    prtcl.posX -= prtcl.velX

                prtcl.posY += prtcl.velY
                if prtcl.posY > self.particleCanvas.canvasSize['Height'] or prtcl.posY < 0:
                    prtcl.posY -= prtcl.velY
            else:
                # wrap particle around canvas if out of bounds
                prtcl.posX += prtcl.velX
                if prtcl.posX > self.particleCanvas.canvasSize['Width']:
                    prtcl.posX = 0
                
                if prtcl.posX < 0:
                    prtcl.posX = self.particleCanvas.canvasSize['Width']

                prtcl.posY += prtcl.velY
                if prtcl.posY > self.particleCanvas.canvasSize['Height']:
                    prtcl.posY = 0

                if prtcl.posY < 0:
                    prtcl.posY = self.particleCanvas.canvasSize['Height']

            self.canvas.moveto(object, prtcl.posX, prtcl.posY)
            object += 1
        
    def DrawParticles(self):
        for prtcl in self.particleCanvas.particles:
            self.canvas.create_oval(prtcl.posX, prtcl.posY, prtcl.posX + prtcl.size, prtcl.posY + prtcl.size, fill=prtcl.color)