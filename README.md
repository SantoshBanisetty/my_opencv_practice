# my_opencv_practice
Installation procedure for Ubuntu 14.04

Open a ternimal on your Ubuntu desktop (Ctrl + Alt + t)

$ sudo apt-get -y install libopencv-dev build-essential cmake libdc1394-22 libdc1394-22-dev libjpeg-dev libpng12-dev libtiff4-dev libjasper-dev libavcodec-dev libavformat-dev libswscale-dev libxine-dev libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev libv4l-dev libtbb-dev libqt4-dev libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev libvorbis-dev libxvidcore-dev x264 v4l-utils python-scipy python-pip python-virtualenv

Download the latest version of OpenCV from 

Unzip it to any location on your computer.
cd opencv (Assuming that you unzipped to a directory called opencv)

mkdir release
cd release
sudo apt-get –y install cmake
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D BUILD_PYTHON_SUPPORT=ON -D WITH_XINE=ON -D WITH_OPENGL=ON -D WITH_TBB=ON -D WITH_EIGEN=ON -D BUILD_EXAMPLES=ON -D BUILD_NEW_PYTHON_SUPPORT=ON -D WITH_V4L=ON ../ 
make –j4
sudo make install

Testing your installation:
Open another terminal and type python and hit enter (You will see >>>)
>>>import cv2

If no error occured, you are good to go. 

Happy coding! 
