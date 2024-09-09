# Person Tracking

----------------------------------

A class TrackObjectBoxmot is created based on boxmot module .
It create a new tracking model based on the boxmot trackers.

The class uses the YOLO detection model and boxmot to track objects and perform reid.

It is compatable to any version of yolo model.
The trackers available are BoTSORT, StrongSort , Bytetrack , Deepocsort and HybridSort etc.

The detected objects are passed to the trackers in boxmot to get the id's of the objects.

A flask app is created to allow user to upload files or youtube urls to perfrom person tracking and re identification.

The model allow user to detect particular objects by choice.

The notebook example.ipynb demonstrate the model using.

-------

## User guide

1. Clone the repository
2. Download the requirements by using command "pip install -r requirements.txt"
3. Import src.templates.TrackObjectBoxMot
4. Create a new object for the class and provide the opted tracker . The default one will be the 'BoTSORT'
5. Call the function 'track' with providing the video path to be tracked and identified and also provide the save_path to save the video.

