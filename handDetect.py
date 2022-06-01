
import mediapipe as mp
import cv2 as cv
import glob
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
IMAGE_FILES = []
for image in glob.glob('BDD/*.bmp'):
    IMAGE_FILES.append(image)

DATAS = []
with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.8) as hands:
  for idx, file in enumerate(IMAGE_FILES):
    print(idx)
    # Read an image, flip it around y-axis for correct handedness output (see
    # above).
    image = cv.flip(cv.imread(file), 1)
    # Convert the BGR image to RGB before processing.
    results = hands.process(cv.cvtColor(image, cv.COLOR_BGR2RGB))

    # Print handedness and draw hand landmarks on the image.
    print('Handedness:', results.multi_handedness)
    if not results.multi_hand_landmarks:
      continue
    image_height, image_width, _ = image.shape
    annotated_image = image.copy()
    for hand_landmarks in results.multi_hand_landmarks:
      print('hand_landmarks:', hand_landmarks)
      print(
          f'Index finger tip coordinates: (',
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width}, '
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height})'
      ) 
      mainDATA = []
      for elem in mp_hands.HandLandmark : 
        print(elem)
        print(
          f'Index finger tip coordinates: (',
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x * image_width}, '
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y * image_height})'
      ) 
        print(
          f'Index finger tip coordinates: (',
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].x * image_width}, '
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].y * image_height})'
      ) 
        print(
          f'Index finger tip coordinates: (',
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].x * image_width}, '
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y * image_height})'
      ) 
        print(
          f'Index finger tip coordinates: (',
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x * image_width}, '
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y * image_height})'
      ) 
        print(
          f'Index finger tip coordinates: (',
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * image_width}, '
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * image_height})'
      ) 
        print(
          f'Index finger tip coordinates: (',
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].x * image_width}, '
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y * image_height})'
      ) 
        print(
          f'Index finger tip coordinates: (',
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].x * image_width}, '
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y * image_height})'
      ) 
      print(
          f'Index finger tip coordinates: (',
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].x * image_width}, '
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].y * image_height})'
      ) 
      print(
          f'Index finger tip coordinates: (',
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].x * image_width}, '
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].y * image_height})'
      ) 






HandLandmark.INDEX_FINGER_DIP
HandLandmark.INDEX_FINGER_TIP
HandLandmark.MIDDLE_FINGER_MCP
HandLandmark.MIDDLE_FINGER_PIP
HandLandmark.MIDDLE_FINGER_DIP
HandLandmark.MIDDLE_FINGER_TIP
HandLandmark.RING_FINGER_MCP
HandLandmark.RING_FINGER_PIP
HandLandmark.RING_FINGER_DIP
HandLandmark.RING_FINGER_TIP
HandLandmark.PINKY_MCP
HandLandmark.PINKY_PIP
HandLandmark.PINKY_DIP
HandLandmark.PINKY_TIP
        
      
        
      '''
    mp_drawing.draw_landmarks(
          annotated_image,
          hand_landmarks,
          mp_hands.HAND_CONNECTIONS,
          mp_drawing_styles.get_default_hand_landmarks_style(),
          mp_drawing_styles.get_default_hand_connections_style()) 
    cv.imwrite(
        "ROI/ROI_" + str(idx) + '.png', cv.flip(annotated_image, 1))
    # Draw hand world landmarks.
    print(str(idx))
    if not results.multi_hand_world_landmarks:
      continue
    for hand_world_landmarks in results.multi_hand_world_landmarks:
      """ mp_drawing.plot_landmarks(
        hand_world_landmarks, mp_hands.HAND_CONNECTIONS, azimuth=5) """
        '''