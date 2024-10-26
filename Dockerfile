FROM python:3.9.5

# 设置工作目录并复制代码
WORKDIR /app

# 复制项目代码到容器
COPY . .

# 安装项目依赖
RUN pip install --no-cache-dir -r requirements.txt


# 启动命令
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]