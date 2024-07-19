# 如何运行

* 先[安装python](https://www.python.org/downloads/)
* 编译前端：`cd frontend && bash build.sh`，产物会被拷贝到backend/public下（已经编译过了这一步可忽略）
* `cd backend && python main.py`
* 浏览器打开[http://localhost:8000](http://localhost:8000)
* 在页面上点击Submit提交即可调用到main.py中的`evaluate_image_to_number`函数
