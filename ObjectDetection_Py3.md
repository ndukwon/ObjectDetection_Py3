# Realtime Object Detection with Python3, Mac

### 목차
1. 환경구성
2. Webcam
3. Face Detection with Haar Classifier
4. Face Landmark Detection with dlib

### 1. 환경 구성
- Python3 (virtualenv 환경이면)
- OpenCV

1.1. Python3 가상환경 구성
```
$ virtualenv -p python3 [가상환경 이름]
$ virtualenv -p python3 py3_env
```

1.2. OpenCV
- 인터넷에 여러 방법이 나와있는데 아래 두 사이트를 주로 참조하였음
    - https://www.pyimagesearch.com/2016/12/19/install-opencv-3-on-macos-with-homebrew-the-easy-way/
    - https://bitbyte.postype.com/post/816722
    ```
    $ brew install opencv
    ==> Installing dependencies for opencv: python, numpy, ilmbase, openexr and tbb
    ==> Installing opencv dependency: python
    Error: Xcode alone is not sufficient on High Sierra.
    Install the Command Line Tools:
      xcode-select --install

    ```
- Xcode 업데이트
- Command Line Tool
- python용 opencv


1.2.1. Xcode 업데이트
- Command Line Tool을 위해서 업데이트가 필요한 것 같다.
- App store에서 업데이트

1.2.2. Command Line Tool
- make, gcc, clang 등의 명령을 위해 필요하다고 한다.
- sudo 명령을 추가해야 정상설치 가능, 다운받는데 시간이 좀 걸리고 잘 실패함
```
$ sudo xcode-select --install
```

1.2.3. python용 opencv
- "brew" 명령 대신에 이 방법을 사용함
```
$ python3.6 -m pip install --upgrade pip setuptools wheel
$ pip3 install opencv-python
```


### 2. Webcam
- Realtime을 위해서 webcam이 필요
- opencv 튜토리얼에 나와있어서 매우 쉬움
    - https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html

### 3. Face Detection with Haar Classifier
- opencv 튜토리얼에 나와있어서 매우 쉬움
    - https://docs.opencv.org/3.4.3/d7/d8b/tutorial_py_face_detection.html
- webcam의 코드를 base 시작
- classifier 부분을 추가: 찾으려고 하는 face, eye의 학습된 weight을 로딩
- 감별은 회색으로 하지만 표기는 컬러로 나오게 함
