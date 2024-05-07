import cv2
import matplotlib.pyplot as plt

# Initialize the webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1000)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Initialize counters for color classifications
safe_count = []
not_safe_count = []

try:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Convert the frame to HSV color space
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        height, width, _ = frame.shape
        cx, cy = int(width / 2), int(height / 2)

        # Get the color of the center pixel
        pixel_center = frame[cy, cx]
        b, g, r = pixel_center
        print(b, g, r)

        # Define color ranges and check if the color is within the range
        color = "Undefind"
        if 27 <= b <= 100 and 80 <= g <= 160 and 48 <= r <= 180:
            color = "Safe for human"
            safe_count.append(1)
            not_safe_count.append(0)
        elif 7 <= b <= 180 and 72 <= g <= 123 and 11 <= r <= 177:
            color = "Not safe for human"
            safe_count.append(0)
            not_safe_count.append(1)
        else:
            safe_count.append(0)
            not_safe_count.append(0)

        # Display the detected color on the frame
        cv2.putText(frame, color, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (int(b), int(g), int(r)), 2)
        cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)

        # Show the frame
        cv2.imshow("Frame", frame)

        # Break the loop when 'Esc' key is pressed
        if cv2.waitKey(1) & 0xFF == 27:
            break
finally:
    # Release video capture and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

# Plotting the stacked line graph for color classification over time
plt.figure(figsize=(10, 5))
plt.stackplot(range(len(safe_count)), safe_count, not_safe_count, labels=['Safe for human', 'Not safe for human'])
plt.legend(loc='upper left')
plt.title('Color Classification Over Time - Stacked Line Graph')
plt.xlabel('Frame')
plt.ylabel('Count')
plt.show()

# Plotting the bar graph for total color classification
plt.figure(figsize=(10, 5))
bar_width = 0.35
index = ['Safe for human', 'Not safe for human']
counts = [sum(safe_count), sum(not_safe_count)]
plt.bar(index, counts, bar_width, color=['green', 'red'])
plt.title('Total Color Classification - Bar Graph')
plt.xlabel('Classification')
plt.ylabel('Total Count')
plt.show()
