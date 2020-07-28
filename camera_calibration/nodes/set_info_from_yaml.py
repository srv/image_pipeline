#!/usr/bin/python
import sys
import yaml
import roslib
from sensor_msgs.msg import CameraInfo
import rospy
import rospkg
import sensor_msgs.srv

class CameraInfoUploader: 

    def __init__(self):
        left_file_name  = '/home/miguel/Desktop/left.yaml'
        right_file_name = '/home/miguel/Desktop/right.yaml'
        self.left_cam_info = yaml_to_CameraInfo(left_file_name)
        self.right_cam_info = yaml_to_CameraInfo(right_file_name)
        self.set_left_camera_info_service = rospy.ServiceProxy("%s/set_camera_info" % rospy.remap_name("left_camera"),  # left_optical?
                                                               sensor_msgs.srv.SetCameraInfo)
        self.set_right_camera_info_service = rospy.ServiceProxy("%s/set_camera_info" % rospy.remap_name("right_camera"),  # right_optical?
                                                                sensor_msgs.srv.SetCameraInfo)

    def do_upload(self):

        rv = True
        response = self.set_left_camera_info_service(self.left_cam_info) 
        rv = rv and self.check_set_camera_info(response)
        response = self.set_right_camera_info_service(self.right_cam_info) 
        rv = rv and self.check_set_camera_info(response)
        return rv

def yaml_to_CameraInfo(yaml_fname):

    """
    Parse a yaml file containing camera calibration data (as produced by rosrun camera_calibration cameracalibrator.py) into a 
    sensor_msgs/CameraInfo msg.
    
    Parameters
    ----------
    yaml_fname : str
        Path to yaml file containing camera calibration data

    Returns
    -------
    camera_info_msg : sensor_msgs.msg.CameraInfo
        A sensor_msgs.msg.CameraInfo message containing the camera calibration data
    """

    # Load data from file
    with open(yaml_fname, "r") as file_handle:
        calib_data = yaml.load(file_handle)
    # Parse
    camera_info_msg = CameraInfo()
    camera_info_msg.width = calib_data["image_width"]
    camera_info_msg.height = calib_data["image_height"]
    camera_info_msg.K = calib_data["camera_matrix"]["data"]
    camera_info_msg.D = calib_data["distortion_coefficients"]["data"]
    camera_info_msg.R = calib_data["rectification_matrix"]["data"]
    camera_info_msg.P = calib_data["projection_matrix"]["data"]
    camera_info_msg.distortion_model = calib_data["distortion_model"]

    return camera_info_msg
    

if __name__ == '__main__': 

    if CameraInfoUploader().do_upload():
        print('camera info updated')

    

    z = 1