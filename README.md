image_pipeline
==============

[![](https://github.com/ros-perception/image_pipeline/workflows/Basic%20Build%20Workflow/badge.svg?branch=melodic)](https://github.com/ros-perception/image_pipeline/actions)

This package fills the gap between getting raw images from a camera driver and higher-level vision processing.

For more information on this metapackage and underlying packages, please see [the ROS wiki entry](http://wiki.ros.org/image_pipeline).

For examples, see the [image_pipeline tutorials entry](http://wiki.ros.org/image_pipeline/Tutorials) on the ROS Wiki.

CALIBRATION
===========

open gui call example: 

roslaunch camera_calibration stereo_calibration.launch

rosrun camera_calibration cameracalibrator.py --approximate 0.1 --size 8x6 --square 0.04 right:=/stereo_down/right/image_raw left:=/stereo_down/left/image_raw right_camera:=/stereo_down/right left_camera:=/stereo_down/left


load config from yaml file:

- open gui
- click on upload button -> it will load left/right yaml from the path indecated in /image_pipeline/camera_calibration/src/camera_calibration/camera_calibrator.py at function "def do_upload(self)"
