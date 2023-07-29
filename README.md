# zundam_orne
ROS です．Topicを受け取るとずんだもんが喋ります．</br>
クレジット　VOICEVOX:ずんだもん [VOICEVOX 公式ページ](https://voicevox.hiroshiba.jp/)</br>


## install
```
pip3 install playsound
cd ~/ws/src/
git clone https://github.com/Ryusei-Baba/zundam_orne.git
cd ~/ws/
catkin build
source devel/setup.bash
```

## run
```
rosrun zundam_orne zundam_orne_node.py
```
