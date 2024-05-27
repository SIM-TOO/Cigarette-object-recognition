# 담배 개체 인식(Cigarette-object-recognition)

# 1. 초기 환경
  - window11 (RTX4070) or Ubuntu 22.04(A5000)
  - anconda
  - vscode
  - python 3.10
<br/> <br/>

# 2. YOLOv5 설치
```
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
```

  - data.yaml 파일 생성
```
train: ../data/images/train
val: ../data/images/val
nc: 1
names: ['cigarette']
```
<br/> <br/>

# 3. 필요시 설치
  - scikit-learn
  - matplotlib
  - moviepy
<br/> <br/>

# 4. 데이터 확보
  - 실제 학습 데이터량 약 3000장
  - github에는 약 100장 정도 업로드
<br/> <br/>

# 5. 데이터 라벨링
  - labelImg 프로그램 이용
  - 데이터 라벨링이 완료 된 경우 train.py 실행
<br/> <br/>

# 6. YOLOv5 학습
  - 실제 사용 모델 : YOLOv5l
  - 학습 환경 : Ubuntu 22.04(A5000)
```
cd yolov5

# YOLOv5s
python train.py --img 640 --batch 16 --epochs 100 --data data.yaml --weights yolov5s.pt --patience 15 --save-period 5
# YOLOv5m
python train.py --img 640 --batch 16 --epochs 100 --data data.yaml --weights yolov5m.pt --patience 15 --save-period 5
# YOLOv5l
python train.py --img 640 --batch 16 --epochs 100 --data data.yaml --weights yolov5l.pt --patience 15 --save-period 5
```
<br/> <br/>

# 7. 모델 결과
![image](https://github.com/SIM-TOO/Cigarette-object-recognition/assets/130709350/52920c61-ef5f-4b9f-99cb-6ca207966292)

https://github.com/SIM-TOO/Cigarette-object-recognition/assets/130709350/219e505a-9e64-4acf-a0e1-79ebe42806e7

https://github.com/SIM-TOO/Cigarette-object-recognition/assets/130709350/54b833bb-9f6b-44d1-a4a2-37682f50b2f5








