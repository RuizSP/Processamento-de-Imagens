import cv2 as cv
import numpy as np
import time


img = cv.imread('lontra.jpeg')

num_steps = 100 #incrementos para os loops


fade_in_step = 0 #incremento para controle do fade_in
fade_out_step = 100  #decremento para controle do fade_out
step_control = 1     #tamanho do incremento ou decremento

largura = 640
altura = 480
fps = 60
codec = cv.VideoWriter_fourcc(*'XVID')  # Codec para vídeo AVI

# Crie um objeto de vídeo para gravar
saida_video = cv.VideoWriter('video_saida.avi', codec, fps, (largura, altura))

img = cv.resize(img, (largura, altura))

frame_count = 0

for i in range (num_steps):
	copyimg = cv.convertScaleAbs(img, alpha=fade_in_step/100, beta=0)
	if (frame_count >= 0 and frame_count < num_steps):	
		saida_video.write(copyimg)  	
	frame_count +=1
	fade_in_step += step_control

for i in range(num_steps):
	copyimg = cv.convertScaleAbs(img, alpha=100/100, beta=0)
	if(frame_count >= num_steps and frame_count < num_steps*2 ):
		saida_video.write(copyimg)  
	frame_count +=1

for i in range (num_steps):
	copyimg = cv.convertScaleAbs(img, alpha=fade_out_step/100, beta=0)
	if(frame_count >= num_steps*2 and frame_count <= num_steps*3):
		saida_video.write(copyimg)  	
	fade_out_step -= step_control
	frame_count +=1

saida_video.release()	
cv.destroyAllWindows()

