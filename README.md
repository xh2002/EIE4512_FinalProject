## EIE4512_FinalProject
This is a reqository for EIE4512 Digital Imagine Processing final project of CUHK(SZ). The topic is Handwritten Digit and Signal Recognition for Children.

Simple intro: In today's digital era, labor costs are increasingly expensive, and the digitalization of early childhood education has become an inevitable trend. To save parents and teachers from spending time on simple homework correction, this project aim to design a program that can check children's answers of simple handwritten calculation.


Instructions:  
Please notice that due to the large size of CNN trainning model, github is not able to accept it. Before running the program, you please download CNN_result.h5 from the link below and put this file in "./Code/project/backend".
  * https://cuhko365-my.sharepoint.com/:u:/g/personal/122040075_link_cuhk_edu_cn/Edz4lPUiOQFBgy5NnlrEyoABy87t7d9Z0Oi9ZbqpzYSCkg?e=0ihKHj  

If you want to run the program, run the main file with path: ""./Code/project/backend/main.py". If you have any questions, please feel free to contact me via github or email: boshixu@link.cuhk.edu.cn.



1. 分工： 
   1. Proposal & PPT 分工 due: 7月3号21点  
  徐博石 4 后端实现逻辑（Strategy）  
  黄羿玮 2 前端部分（Goal） + 5 Reference  
  黄宇航 1 Introduction + 3 Datasets （数据集就是图片来源之类的） 
  参考：  
    Proposal文档:  *需要改进的：1. Datasets需要添加说明“使用收集来的十岁以内少儿样本训练数据集” ；GUI部分需要添加 “会做得更卡哇伊一点以适应少儿要求”*
    https://docs.qq.com/doc/DRmtKdE56ZXNWdkZp  
    PPT自己完成自己的部分，模板是群里发的PPT

   2. 其余分工
   6月23号：组队
   6月26号：10点在TD3楼开会，定标题、分工
   7月3号：Proposal PPT
   7月7号中午12点：Proposal本体
   7月18号：前端、后端分别完成
   7月18号：Final Presentation 的 PPT
   7月29号：报告
   7月30号：上交作业


2. 主题选择：
  KNN算法实现手写数字识别 <br>
  参考：
  https://github.com/HistoneVon/knnDigitalDistinguish

3. 实现：
  前端：  
    手写板+输出，针对儿童优化  
  后端：  
    识别：文字切割；数字0~9，加减乘除等于号五个字符  
    计算：计算出识别的结果  
    对比：对比手写和正确结果  
  
4. 改进：
   需要提供计算范围
   需要把OpenCV的部分讲的详细一点，例如用了什么函数，要在Report里列出。

5. 报告内容：
  文档： 【腾讯文档】Report_draft： 
    https://docs.qq.com/doc/DRldkREhWZUt3Q0VF?scene=cd2f453f5d367e6f2f02d9e0k4BXs1
   包括：
   1摘要 Abstract；2引言 Intro；3相关工作 Related Work；4算法；5实验 Experiments；6准备论文的杂项 Misc for Preparing Your Paper；7参考文献 References；8附录 Appendix
   
   xbs: 1348
   hyh: 245
   hyw: 467

   
  r1. 摘要 Abstract 
      - 问题陈述及现有方法缺陷
      - 提出算法的关键步骤及动机/观察
      - 实验结果亮点

  r2. 引言 Intro 
      - 问题背景及概述
      - 潜在缺陷或关注点
      - 动机及图示例子
      - 提出解决方案及简要说明
      - 贡献列表及外部链接

  r3. 相关工作 Related Work 
      - 相关工作的综述
      - 现有方法的缺陷
      - 本文方法的差异点
      （没有专注于小朋友的）

  r4. 提出的算法 Proposed Algorithm 
      - 方法流程图
      - 子部分详述方法
      - 使用数学符号及表达
      - 图表说明

  r5. 实验 Experiments 
      - 数据集概述及评估指标
      - 各组件分析
      - 与现有方法的性能比较
      - 超长部分可放入附录

  r6. 讨论（可选） Discussions

  r7. 准备论文的杂项 Misc for Preparing Your Paper 
      - 图像
      - 表格
      - 条目和算法
      - 引用

  r8. 致谢（可选） Acknowledgments

  r9. 参考文献 References 

  r10. 附录 Appendix
      - 补充材料

   
   
   

