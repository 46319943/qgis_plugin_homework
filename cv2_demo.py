import cv2
import numpy as np
from sklearn.cluster import AgglomerativeClustering
# from matplotlib import pyplot as plt


def cv_imread(filePath):
    cv_img = cv2.imdecode(np.fromfile(filePath, dtype=np.uint8), -1)
    # imdecode读取的是rgb，如果后续需要opencv处理的话，需要转换成bgr，转换后图片颜色会变化
    # cv_img = cv2.cvtColor(cv_img,cv2.COLOR_RGB2BGR)
    return cv_img


img = cv2.imread(r'1.jpg', -1)
print(img)
edges = cv2.Canny(img, 100, 200)
edges = cv2.Canny(img, 200, 400, 15)
# plt.subplot(121)
# # plt.imshow(img, cmap='gray')
# plt.imshow(img)
# plt.title('Original Image')
# plt.xticks([])
# plt.yticks([])
# plt.subplot(122)
# plt.imshow(edges, cmap='gray')
# plt.title('Edge Image')
# plt.xticks([])
# plt.yticks([])
# plt.show()
