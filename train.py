import os
import shutil
from sklearn.model_selection import train_test_split

# 원본 데이터 디렉토리 경로
smoking_images_dir = 'data/smoking'

# 새로운 데이터 디렉토리 경로
images_train_dir = 'data/images/train'
images_val_dir = 'data/images/val'
labels_train_dir = 'data/labels/train'
labels_val_dir = 'data/labels/val'

# 디렉토리 생성
os.makedirs(images_train_dir, exist_ok=True)
os.makedirs(images_val_dir, exist_ok=True)
os.makedirs(labels_train_dir, exist_ok=True)
os.makedirs(labels_val_dir, exist_ok=True)

# 이미지 파일 리스트 가져오기
smoking_images = [f for f in os.listdir(smoking_images_dir) if f.endswith('.jpg')]

# 라벨 파일 리스트 가져오기
smoking_labels = [f.replace('.jpg', '.txt') for f in smoking_images if os.path.exists(os.path.join(smoking_images_dir, f.replace('.jpg', '.txt')))]

# 라벨이 있는 이미지 파일 리스트 가져오기
smoking_images = [f for f in smoking_images if f.replace('.jpg', '.txt') in smoking_labels]

# 학습용과 검증용 데이터로 분리
train_smoking_images, val_smoking_images = train_test_split(smoking_images, test_size=0.2, random_state=42)
train_smoking_labels, val_smoking_labels = train_test_split(smoking_labels, test_size=0.2, random_state=42)

# 파일 이동
def copy_files(images, labels, img_dest, lbl_dest, src_dir):
    for img, lbl in zip(images, labels):
        shutil.copy(os.path.join(src_dir, img), img_dest)
        shutil.copy(os.path.join(src_dir, lbl), lbl_dest)

# 파일 복사
copy_files(train_smoking_images, train_smoking_labels, images_train_dir, labels_train_dir, smoking_images_dir)
copy_files(val_smoking_images, val_smoking_labels, images_val_dir, labels_val_dir, smoking_images_dir)
