Using the tensorflow base, I created an Object Detection model that detects Sign Language for the letters A, B, and C.

To run you need to set up a conda virtual environment, install protobuf and run the protobuff_initalizer.py script. 
Then you need to run the setup.py
Once finished, you can run the "detect_from_webcam.py" script with the command 
```python .\detect_from_webcam.py -m .\inference_graph\saved_model -l .\labelmap\labelmap.pbtxt```
