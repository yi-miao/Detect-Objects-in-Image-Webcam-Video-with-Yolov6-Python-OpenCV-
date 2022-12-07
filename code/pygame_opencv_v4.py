import pygame
import cv2
import numpy
from yolov6_vc.imageInference import Inferer

weights = 'cfg/yolov6n.pt'
device = 'cpu'
class_names = 'data/coco.yaml'
img_size = 640
half = False
conf_thres = 0.40
iou_thres = 0.45
classes = None
agnostic_nms = False
max_det = 1000

inferer = Inferer(
    '',
    weights,
    device,
    class_names,
    img_size,
    half,
    conf_thres,
    iou_thres,
    classes,
    agnostic_nms,
    max_det
)

stride = inferer.model.stride 

pygame.init()

source = 'data/images/test2.mp4'

(ww, wh) = (400, 400)
screen = pygame.display.set_mode((ww, wh))
pygame.display.set_caption("Scene Sim")

img0 = pygame.image.load("data/images/d.png").convert_alpha()
sf = img0
sfw, sfh = sf.get_size()

#(bgw, bgh) = (640, 360) 
(bgw, bgh) = (1280, 720) 
x0 = -(bgw-ww)/2    # Initial x
x1 = -(bgw-ww)      # maximum x value
y0 = -(bgh-wh)/2    # Initial y
y1 = -(bgh-wh)      # maximum y value
x = x0              # Initial x
y = y0              # Initial y

t = 0.05            # minimum change to the axis required
joysticks = {}

done = False
while not done:            
    cap = cv2.VideoCapture(source)
    while cap.isOpened() and not done:
        ret, img_src = cap.read()
        if ret:
            image, img_src = inferer.precess_image(img_src)    
            detection = inferer.infer(image, img_src)
            for *xyxy, conf, cls in reversed(detection):
                class_num = int(cls)
                label = f'{inferer.class_names[class_num]} {conf:.2f}'
                inferer.plot_box_and_label(img_src, max(round(sum(img_src.shape) / 2 * 0.003), 2), xyxy, label,
                                           color=inferer.generate_colors(class_num, True), fps=None)

            frame = numpy.asarray(img_src)        
        
            frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            frame=numpy.rot90(frame)
            sf=pygame.surfarray.make_surface(frame) 
            screen.blit(sf, (x, y)) 
            screen.blit(img0, (180, 180))            
            pygame.display.update()
        else:
            break
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                vw  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
                vh = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
                print("video size w-h: ", str(vw) + ' - ' + str(vh))            
                done = True
                break
            if event.type == pygame.JOYDEVICEADDED:
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks[joy.get_instance_id()] = joy
                
        for joystick in joysticks.values():
            axes = joystick.get_numaxes()
            for i in range(axes):
                axis = joystick.get_axis(i)
                if i == 0:
                    if axis < -t:
                        if x < 0:
                            x -= axis
                        else:
                            x = x1
                    if axis > t:
                        if x > x1:
                            x -= axis
                        else:
                            x = 0  
                if i == 1:
                    if axis < -t:                 
                        if y < 0:
                            y -= axis
                        else:
                            y = y1
                    if axis > t:
                        if y > y1:
                            y -= axis
                        else:
                            y = 0                        

cap.release()
pygame.quit()