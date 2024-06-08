import csv
import cv2
import mediapipe as mp

# Initialize MediaPipe Pose model
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

def extract_pose_landmarks(video_path, window_name):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Create a window for the video
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 610, 1080)
    
    # Initialize a list to store landmark locations
    landmarks_list = []
    
    while True:
        # Read a frame from the video
        ret, frame = cap.read()
        
        # Check if frame reading was successful
        if not ret:
            break
        
        # Convert the image to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Perform pose estimation
        results = pose.process(frame_rgb)
        
        # Record landmark locations
        landmarks_frame = []
        if results.pose_landmarks:
            for landmark in results.pose_landmarks.landmark:
                landmarks_frame.append((landmark.x, landmark.y))
        landmarks_list.append(landmarks_frame)
        
        # Draw the pose landmarks on the frame
        if results.pose_landmarks:
            mp_drawing = mp.solutions.drawing_utils
            mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        
        # Display the frame in the window
        cv2.imshow(window_name, frame)
        
        # Check for key press
        key = cv2.waitKey(1)
        
        # Break the loop if 'q' is pressed
        if key == ord('q'):
            break
    
    # Release the video capture object
    cap.release()
    cv2.destroyAllWindows()
    
    return landmarks_list

def save_landmarks_to_csv(landmarks_list, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Frame'] + [f'Landmark_{i}' for i in range(len(landmarks_list[0]))])
        for idx, landmarks_frame in enumerate(landmarks_list):
            writer.writerow([idx + 1] + [f'{x},{y}' for x, y in landmarks_frame])

# Path to the video files
video_path_1 = 'ref.mp4'
video_path_2 = 'bad.mp4'
video_path_3 = 'ok.mp4'
video_path_4 = 'good.mp4'
video_path_5 = 'ok2.mp4'
video_path_6 = 'ok3.mp4'

# Extract pose landmarks from the first video
landmarks_list_1 = extract_pose_landmarks(video_path_1, 'Video 1')

# Save landmark locations to a CSV file
save_landmarks_to_csv(landmarks_list_1, 'landmarks_video_ref.csv')
print("Landmark locations for Video 1 saved to a CSV file.")

# # Extract pose landmarks from the second video
# landmarks_list_2 = extract_pose_landmarks(video_path_2, 'Video 2')

# # Save landmark locations to a CSV file
# save_landmarks_to_csv(landmarks_list_2, 'landmarks_video_bad.csv')
# print("Landmark locations for Video 2 saved to a CSV file.")

# # Extract pose landmarks from the first video
# landmarks_list_3 = extract_pose_landmarks(video_path_3, 'Video 3')

# # Save landmark locations to a CSV file
# save_landmarks_to_csv(landmarks_list_3, 'landmarks_video_ok.csv')
# print("Landmark locations for Video 3 saved to a CSV file.")

# # Extract pose landmarks from the second video
# landmarks_list_4 = extract_pose_landmarks(video_path_4, 'Video 4')

# # Save landmark locations to a CSV file
# save_landmarks_to_csv(landmarks_list_4, 'landmarks_video_good.csv')
# print("Landmark locations for Video 4 saved to a CSV file.")

# # Extract pose landmarks from the first video
# landmarks_list_5 = extract_pose_landmarks(video_path_5, 'Video 5')

# # Save landmark locations to a CSV file
# save_landmarks_to_csv(landmarks_list_5, 'landmarks_video_ok2.csv')
# print("Landmark locations for Video 5 saved to a CSV file.")

# # Extract pose landmarks from the second video
# landmarks_list_6 = extract_pose_landmarks(video_path_6, 'Video 6')

# # Save landmark locations to a CSV file
# save_landmarks_to_csv(landmarks_list_6, 'landmarks_video_ok3.csv')
# print("Landmark locations for Video 6 saved to a CSV file.")