import time

class Util:
    @classmethod
    def resize_capture_area(cls, frame):
        height, width = frame.shape[1::-1]
        roi = frame[int(height/3):height, int(width/3):int(width/3 + width)]
        return roi

    @classmethod
    def resize(cls, image):
      import cv2
      
      resized = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
      return resized

    @classmethod
    def screenshot(cls):
        """Take a screenshot of a particular portion of the screen."""
        import numpy as np
        import cv2
        from PIL import ImageGrab

        try:
            screen = ImageGrab.grab()
            bgr_screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
            return bgr_screen
        except Exception:
            return np.array([])

    @classmethod
    def found_kill(cls):
        import requests
    
        try:
          # REQUIRED: Replace with your lights address
          response = requests.post("http://mylightsip/", data={ "value": "Color" })
          return response

        except Exception as e:
            print("Error in sending", e)
            return False
