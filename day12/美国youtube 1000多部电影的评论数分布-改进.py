import matplotlib.pyplot as plt
import numpy as np

us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"

# t1 = np.loadtxt(us_file_path, delimiter=",", dtype="int", unpack=True)
t_us = np.loadtxt(us_file_path, delimiter=",", dtype="int")

# 取美国的电影的评论的数据
t_us_comments = t_us[:, -1]

# 选择比5000小的数据
t_us_comments = t_us_comments[t_us_comments <=5000]

print(t_us_comments.shape)

# 所有最小值和最大值
print(t_us_comments.max(), t_us_comments.min())

# 有多少数据
print(t_us_comments.shape)