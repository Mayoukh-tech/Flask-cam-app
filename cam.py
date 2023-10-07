import cv2
# import imutils
import numpy as np
import requests
from flask import Flask, Response, render_template

app = Flask(__name__)
camera = cv2.VideoCapture("rtsp://192.168.0.100:8080/h264_pcm.sdp")

def gen_frames():  
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and showing the result
            if cv2.waitKey(1) == 27:
                break
            cv2.destroyAllWindows()
@app.route('/')
def index():
    return render_template('index.html')
'''# if in the search bar we write the 
address like this http://127.0.0.1:5000/learn 
then it will show the above wrtitten lines'''
@app.route('/video_feed')
def vid_ft():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == "__main__":
    app.run(debug=True ,port=8523)

'''running the above lines in the search bar 
will reflect the lines written in m.txt file
inside the static folder'''


'''to run a html file in the flask we have to 
return the template where we have to save the 
html file'''
