# coding=utf-8
from threading import Timer, Thread, Event
from PIL import Image, ImageGrab
import datetime
import cv2


class perpetualTimer():
    def __init__(self, t, hFunction):
        self.t = t
        self.hFunction = hFunction
        self.thread = Timer(self.t, self.handle_function)

    def handle_function(self):
        self.hFunction()
        self.thread = Timer(self.t, self.handle_function)
        self.thread.start()

    def start(self):
        self.thread.start()

    def cancel(self):
        self.thread.cancel()


def do_screen():
    img = ImageGrab.grab()
    cap = cv2.VideoCapture(0)
    log_filename = '{0:%m.%d.%Y %H-%M-%S}'.format(datetime.datetime.now())
    img.save(log_filename + ".png", "PNG")
    for i in range(30):
        cap.read()
    ret, frame = cap.read()
    cv2.imwrite(log_filename+"--cam.png", frame)
    cap.release()


t = perpetualTimer(5, do_screen)
t.start()
