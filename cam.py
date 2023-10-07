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


# *************************************************************#
    # @app.route('/')
# def hello_world():
#     return 'Hello, World!'


# def learn():
    # Import essential libraries  
# Replace the below URL with your own. Make sure to add "/shot.jpg" at last.
# url = "http://192.168.0.102:8080/shot.jpg"
  
# # While loop to continuously fetching data from the Url
# while True:
#     img_resp = requests.get(url)
#     img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
#     img = cv2.imdecode(img_arr, -1)
#     img = imutils.resize(img, width=1000, height=1800)
#     cv2.imshow(" ",img)

#         # Press Esc key to exit
#     if cv2.waitKey(1) == 27:
#         break
   
#     cv2.destroyAllWindows()
# port can be changed by below line
# app.run(debug=True, port=1000) instead of 1000 any number can be used
# by default port will be choosen by flask python itself so to change it you must use above line of code

# here we have to make 2 files mainly templates and static and both should be in the same path where flask app is made
# http://127.0.0.1:5000/static/m.txt
'''running the above lines in the search bar 
will reflect the lines written in m.txt file
inside the static folder'''


'''to run a html file in the flask we have to 
return the template where we have to save the 
html file'''