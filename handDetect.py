
import mediapipe as mp
import numpy as np
import cv2 as cv
import glob

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
def HandsLandmarks():
  IMAGE_FILES = []
  for image in glob.glob('BDD/*.bmp'):
      IMAGE_FILES.append(image)
  DATAS = []
  names = []
  FinalData = []
  with mp_hands.Hands(
      static_image_mode=True,
      max_num_hands=2,
      min_detection_confidence=0.8) as hands:
    for idx, file in enumerate(IMAGE_FILES):
     
      # Read an image, flip it around y-axis for correct handedness output (see
      # above).
      image = cv.flip(cv.imread(file), 1)
      # Convert the BGR image to RGB before processing.
      results = hands.process(cv.cvtColor(image, cv.COLOR_BGR2RGB))

     
      if not results.multi_hand_landmarks:
        continue
      image_height, image_width, _ = image.shape
      for hand_landmarks in results.multi_hand_landmarks:
        names.append(file)
        DATAS.append( [
            [
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x * image_width}, '
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y * image_height})' ]
        , 
          [
            
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].x * image_width}, '
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].y * image_height})'
        
          ],[
            
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].x * image_width}, '
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y * image_height})'
        
          ],[
            
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x * image_width}, '
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y * image_height})'
        
          ],[
            
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * image_width}, '
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * image_height})'
        
          ],[
            
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].x * image_width}, '
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y * image_height})'
        
          ],[
            
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].x * image_width}, '
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y * image_height})'
        
        ],[
            
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].x * image_width}, '
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y * image_height})'
        
        ],[
            
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width}, '
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height})'
        
        ],[
            
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x * image_width}, '
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y * image_height})'
        
        ]
        ,[
            
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].x * image_width}, '
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y * image_height})'
        
        ],[
            
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].x * image_width}, '
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y * image_height})'
        
        ],[
            
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x * image_width}, '
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * image_height})'
        
        ],[
            
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].x * image_width}, '
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y * image_height})'
        
        ],[
            
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].x * image_width}, '
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y * image_height})'
        
        ],[
            
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].x * image_width}, '
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y * image_height})'
        
        ],[
            
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x * image_width}, '
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y * image_height})'
        
        ],[
            
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].x * image_width}, '
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y * image_height})'
        
        ],[
            
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].x * image_width}, '
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y * image_height})'
        
        ],[
            
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].x * image_width}, '
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y * image_height})'
        ],[
            
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x * image_width}, '
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y * image_height})'
        ] ])            
        
    indexImg = 0 
    
    d = []
    
    for listImages in DATAS : 
        
        
        POINTS = []
        for listPoints in listImages : 
           
            for xy in listPoints:
                xyy = []
                indexC= 0
                for nb in xy.strip("')").split(","):
                    indexC +=1
                    xyy.append(float(nb))
                POINTS.append(xyy)
                
        d.append(POINTS) 
        indexImg+=1
        
    return names,d

def HandsLandmarksSingleIm(imagepath):
    DATAS = []
    with mp_hands.Hands(
            static_image_mode=True,
            max_num_hands=2,
            min_detection_confidence=0.8) as hands:
        image = cv.flip(cv.imread(imagepath), 1)
        # Convert the BGR image to RGB before processing.
        results = hands.process(cv.cvtColor(image, cv.COLOR_BGR2RGB))

        if not results.multi_hand_landmarks:
            return [None]*42
        image_height, image_width, _ = image.shape
        for hand_landmarks in results.multi_hand_landmarks:
            DATAS.append([
                [
                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x * image_width}, '
                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y * image_height})']
                ,
                [

                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].x * image_width}, '
                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].y * image_height})'

                ], [

                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].x * image_width}, '
                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y * image_height})'

                ], [

                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x * image_width}, '
                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y * image_height})'

                ], [

                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * image_width}, '
                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * image_height})'

                ], [

                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].x * image_width}, '
                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y * image_height})'

                ], [

                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].x * image_width}, '
                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y * image_height})'

                ], [

                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].x * image_width}, '
                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y * image_height})'

                ], [

                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width}, '
                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height})'

                ], [

                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x * image_width}, '
                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y * image_height})'

                ]
                , [

                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].x * image_width}, '
                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y * image_height})'

                ], [

                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].x * image_width}, '
                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y * image_height})'

                ], [

                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x * image_width}, '
                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * image_height})'

                ], [

                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].x * image_width}, '
                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y * image_height})'

                ], [

                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].x * image_width}, '
                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y * image_height})'

                ], [

                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].x * image_width}, '
                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y * image_height})'

                ], [

                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x * image_width}, '
                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y * image_height})'

                ], [

                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].x * image_width}, '
                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y * image_height})'

                ], [

                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].x * image_width}, '
                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y * image_height})'

                ], [

                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].x * image_width}, '
                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y * image_height})'
                ], [

                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x * image_width}, '
                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y * image_height})'
                ]])
        d = []
        for listImages in DATAS:
            for listPoints in listImages:
                for xy in listPoints:
                    xyy = []
                    indexC = 0
                    for nb in xy.strip("')").split(","):
                        indexC += 1
                        d.append(float(nb))
    return d
