import cv2
import time
import os

def take_snapshots(folder_path):
    """
    打开摄像头，每隔2秒拍摄一张照片，并将其保存在指定的文件夹中。
    按下'p'键暂停，按下'q'键继续。
    
    参数:
    - folder_path: 照片要保存到的文件夹路径。
    """
    
    # 检查指定的文件夹是否存在，如果不存在则创建它
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # 打开摄像头
    cap = cv2.VideoCapture(0)
    
    snapshot_count = 0
    while True:
        # 从摄像头捕获每一帧
        ret, frame = cap.read()
        
        # 检查是否成功捕获帧
        if not ret:
            print("无法从摄像头获取帧。")
            break
        
        # 将帧保存到指定文件夹
        snapshot_path = os.path.join(folder_path, f"snapshot_{snapshot_count}.jpg")
        cv2.imwrite(snapshot_path, frame)
        
        # 增加快照计数
        snapshot_count += 1
        
        # 显示帧
        cv2.imshow('摄像头', frame)
        
        # 检查'p'或'q'键是否被按下
        key = cv2.waitKey(2000) & 0xFF
        if key == ord('q'):
            print("已暂停。按'w'继续。")
            while True:
                key = cv2.waitKey(100) & 0xFF
                if key == ord('w'):
                    break
            continue
        elif key == ord('w'):
            break
        if key == ord('e'):
            return
    
    # 完成所有操作后，释放摄像头
    cap.release()
    cv2.destroyAllWindows()


# Example usage:
take_snapshots('./imgs')
