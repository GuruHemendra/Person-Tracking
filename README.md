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
