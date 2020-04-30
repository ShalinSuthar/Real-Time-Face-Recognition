import cv2

cam = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

while True:
	ret, frame = cam.read()
	gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	if ret == False:
		continue

	faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)


	for (x, w, y, h) in faces:
		cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)

	cv2.imshow("Video Frame", frame)

	#Wait for user input - q, then stop the loop
	key_pressed = cv2.waitKey(1) & 0xFF
	if key_pressed == ord('q'):
		break

cam.release()
cv2.destroyAllWindows()