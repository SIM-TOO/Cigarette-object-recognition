# YOLO_cigarette_classification

1. 초기 환경
- window11 (RTX4070) or Ubuntu 22.04(A5000)
- anconda
- vscode
- python 3.10

2. YOLOv5 설치
```
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
​```

- data.yaml 파일 생성

```
train: ../data/images/train
val: ../data/images/val
nc: 1
names: ['cigarette']
​```

3. 필요시 설치
- scikit-learn
- matplotlib
- moviepy

4. 데이터 확보
- 실제 학습 데이터량 약 3000장
- github에는 약 100장 정도 업로드

5. 학습데이터 확보 및 데이터 라벨링
- labelImg 프로그램 이용
- 데이터 라벨링이 완료 된 경우 train.py 실행

6. YOLOv5 학습

- 실제 사용 모델 : YOLOv5x
- 학습 환경 : Ubuntu 22.04(A5000)

​```
cd yolov5

# YOLOv5s
python train.py --img 640 --batch 16 --epochs 100 --data data.yaml --weights yolov5s.pt --patience 15 --save-period 5
# YOLOv5m
python train.py --img 640 --batch 16 --epochs 100 --data data.yaml --weights yolov5m.pt --patience 15 --save-period 5
# YOLOv5l
python train.py --img 640 --batch 16 --epochs 100 --data data.yaml --weights yolov5l.pt --patience 15 --save-period 5
​```

# 담배 개체 인식
# Cigarette-object-recognition
