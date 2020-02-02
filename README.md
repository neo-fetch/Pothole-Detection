<h1>Created for the hardworking sih-devs to ease their burden.</h1>
<br>
<h1>POTHOLE DETECTION FRONTEND</h1>
<br>
<h3>Objctives: We have two frontends done by two devs: Hritik and Sakshi</h3>
<h4>◘ Frontend 1: set up an interface that will get images periodically and it verifies potholes from an object detection tensorflow.js model(Done by the backend bois) and point the source on the map(either using the image metadata/embeddata or by a gps tag)</h4>
<h4>◘ Frontend 2: set up an app interface that will get an image from the mobile camera and use our model to detect potholes. Upon clicking a pic the interface should provide an option to send the image to the server along with the gps data on the phone when it was taken. (The photo should be sent then and there. There is no need to provie an option to upload the image as live camera does that) </h4>
<h4>Hritik has agreed on frontend #1 while Sakshi has agreed on frontend #2 </h4>

# POTHOLE DETECTION BACKEND
<h2>We shall be using an object detection model (either by tensorflow.js or YOLO(YOLO is chosen one for the prototype model) or render manually usng r-fcn)</h2>
<h3>We need training data of 200 simple potholes which are annotated.I have an image dataset of at least 1200 proper pothole images which I will upload below</h3>
<br>
<h4>https://drive.google.com/open?id=1TeqOhl8XdiBdkJOr72Q6mMvQ_WG2IzV5</h4>
<br>
<h5> Take any 30 simple potholes from your assigned 317 and annotate them
Mayank: First 317 <br>
Raghvesh: 318-634 <br>
prabhu: 635 to 951 <br>
Imma(HBD!):remaining 317 <br> 
# Note <br>
The previous json files are for trial purposes only(since they classify images and not detect objects in them). Could be used by both devs 
<br>
# Links <br>
https://teachablemachine.withgoogle.com/faq <br>
https://towardsdatascience.com/yolo-you-only-look-once-real-time-object-detection-explained-492dc9230006 <br>
https://www.youtube.com/watch?v=oHg5SJYRHA0 <br>
(add more links if required)
