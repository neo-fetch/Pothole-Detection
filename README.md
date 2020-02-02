# POTHOLE DETECTION FRONTEND
<h3>Created for the hardworking sih-devs to ease their burden.</h3>
<h3>Objctives: We have two frontends done by two devs: Hritik and Sakshi</h3>
<h4>◘ Frontend 1: set up an interface that will get images periodically and it verifies potholes from an object detection tensorflow.js model(Done by the backend bois) and point the source on the map(either using the image metadata/embeddata or by a gps tag)</h4>
<h4>◘ Frontend 2: set up an app interface that will get an image from the mobile camera and use our model to detect potholes. Upon clicking a pic the interface should provide an option to send the image to the server along with the gps data on the phone when it was taken. (The photo should be sent then and there. There is no need to provie an option to upload the image as live camera does that) </h4>
<h4> The objective of this repository is to successfully execute an app or a portal that uses the tensorflow model to detect potholes.</h4>

# POTHOLE DETECTION BACKEND
<h2>We shall be using an object detection model (either by tensorflow.js or YOLO(preferrred one. We will go for this in the prototype model) or render manually usng r-fcn)</h2>
<h3>We need training data of 200 simple potholes which are annotated.I have an image dataset of at least 1500 proper pothole images which I will upload</h3>

# NOTE:
The previous json files are for trial purposes only(since they classify images and not detect objects in them). Could be used by both devs  
# Links
https://teachablemachine.withgoogle.com/faq
https://towardsdatascience.com/yolo-you-only-look-once-real-time-object-detection-explained-492dc9230006
https://www.youtube.com/watch?v=oHg5SJYRHA0 
(add more links if required)
