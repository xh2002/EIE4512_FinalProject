#!/usr/bin/env python
# coding: utf-8

# In[47]:


'''
输入：
    同目录下的模型文件 digit_and_symbol_classifier.h5
    同目录下的一组图片，1[字母].jpg
输出：
    同目录下 output.jpg 
计算：
    接受2个最多2位数的输入
    只能输出正数，小孩没学过负数

'''


# In[1]:


import os
import re
import cv2
import numpy as np
from keras.api.models import load_model
from keras.api.preprocessing.image import load_img, img_to_array
from PIL import Image,ImageDraw,ImageFont

new_dir = "./backend"  # 替换为你想要切换到的目录路径
os.chdir(new_dir)

# In[2]:


# 加载模型 需要更改目录就在这里改
model = load_model('CNN_result.h5')
print(model.input_shape)


# In[3]:


# 定义字符类别（与训练时使用的顺序一致）
characters = '0123456789+-x÷'
num_classes = len(characters)


# In[4]:


# 映射类别索引到字符
char_to_index = {char: i for i, char in enumerate(characters)}
index_to_char = {i: char for char, i in char_to_index.items()}


# In[5]:


# 图像预处理函数
def preprocess_image(image_path, target_size=(150, 150)):  # 修改为模型的输入尺寸
    image = load_img(image_path, color_mode='rgb', target_size=target_size)  # 修改为RGB格式
    image = img_to_array(image)
    image = image.astype('float32') / 255
    image = np.expand_dims(image, axis=0)  # 添加批次维度
    
    # 保存处理后的图像用于调试
    processed_image_path = f'processed_{os.path.basename(image_path)}'
    Image.fromarray((image[0] * 255).astype(np.uint8)).save(processed_image_path)
    print(f"Processed image saved as {processed_image_path}")
    
    return image


# In[6]:


# 识别图像内的字符
def recognize_character(image_path):
    image = preprocess_image(image_path)
    predictions = model.predict(image)
    predicted_index = np.argmax(predictions)
    predicted_char = index_to_char[predicted_index]
    return predicted_char


# In[7]:


# # 测试识别函数
# image_path = 'a1.png' 

# predicted_char = recognize_character(image_path)
# print(f"Image a1.png: Predicted Character - {predicted_char}")

# image_path = 'a2.png' 

# predicted_char = recognize_character(image_path)
# print(f"Image a1.png: Predicted Character - {predicted_char}")


# In[8]:


# 获取当前目录下所有文件
# 需要更改目录就在这里改
files = os.listdir('.')

# 正则表达式匹配以a开头，数字命名，jpg格式的文件
image_files = sorted([f for f in files if re.match(r'a\d+\.png$', f)])

# 获取所有识别出的字符
recognized_characters = [recognize_character(image_file) for image_file in image_files]


# In[9]:


print(recognized_characters)


# In[10]:


import array


# In[11]:


# 验证程序
# characters = '0123456789+-x÷'
num1_str = ""
num2_str = ""
num3_str = ""

sig_pos = []
s = 0

pos = 0
for char in recognized_characters:
    if char == "+" or char == "-" or char == "x" or char == "÷":
        sig_pos.append(pos)
    pos = pos + 1
#print(sig_pos)

# numbers
for i in range(s, sig_pos[0]):
    num1_str += recognized_characters[i]
    num1 = int(num1_str)
print(num1)
for i in range(sig_pos[0] + 1, sig_pos[1]):
    num2_str += recognized_characters[i]
    num2 = int(num2_str)
print(num2)
for i in range(sig_pos[1] + 1, len(recognized_characters)):
    num3_str += recognized_characters[i]
    num3 = int(num3_str)
print(num3)

char = recognized_characters[sig_pos[0]]
#print(char)
if char == "+":
    result = num1 + num2
elif char == "-":
    result = num1 - num2
elif char == "*":
    result = num1 * num2
else:
    result = num1 / num2
print(result)


# In[12]:


if result == num3:
    judge = "CORRECT!"
else:
    judge = "T_T WRONG"
    num3 = round(result)
    print(result)
    
p_info = str(num1) + " " + char + " " + str(num2) + " = " + str(num3)
print(p_info)      


# In[13]:


# 创建一个白色背景的空白画布
canvas = np.ones((150, 300, 3), dtype="uint8") * 255

# 转换为 PIL 图像
pil_img = Image.fromarray(cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB))

# 创建一个绘图对象
draw = ImageDraw.Draw(pil_img)

# 定义字体
font = ImageFont.truetype("arial.ttf", 40)

position1 = (10, 25)
position2 = (10, 80)

# 定义文本颜色
font_color_info = (0, 0, 0)  # 黑色
if judge == "CORRECT!":
    font_color_judge = (0, 255, 0)  # 绿色
else:
    font_color_judge = (255, 0, 0)  # 红色

# 绘制文本
draw.text(position1, judge, font=font, fill=font_color_judge)
draw.text(position2, p_info, font=font, fill=font_color_info)

# 转换回 OpenCV 图像
canvas = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

# 保存图像
output_image_path = 'output.jpg'
cv2.imwrite(output_image_path, canvas)


# In[ ]:



