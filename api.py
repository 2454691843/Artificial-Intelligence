import requests
import json
def get_response(input_text):
    API_KEY='sk-hbeeihtusuvqoarvsnookqxdxcxfrpyyxhaipvscxuqtxyeo'

    # 配置API参数
    API_URL = "https://api.siliconflow.cn/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "model": "deepseek-ai/DeepSeek-R1",  # 硅基流动支持的模型名
        "messages": [
            {"role": "system", "content": "你是一个专业的助手"},
            {"role": "user", "content": input_text}
        ],
        "temperature": 0.7,  # 控制生成随机性（0-2）
        "max_tokens": 500     # 限制生成文本长度
    }

# 发送请求并处理响应
    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()  # 检查HTTP错误
        result = response.json()
        return result['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        return f"请求失败: {e}"
    except KeyError as e:
        return f"响应解析错误: {e}"

if __name__ == '__main__':
    while True:
        input_text = input('>>>')
        print(get_response(input_text))
