import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os

def get_favicon(url):
    """
    获取指定网址的图标
    
    参数:
        url (str): 要获取图标的网址
        
    返回:
        str: 成功时返回下载的文件路径，失败时返回 None
    """
    try:
        # 确保 url 包含协议
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
            
        # 发送请求获取网页内容
        response = requests.get(url)
        response.raise_for_status()
        
        # 解析 HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 查找所有可能的图标链接
        favicon_url = None
        
        # 1. 先检查 link 标签中的图标
        icon_links = soup.find_all('link', rel=lambda x: x and ('icon' in x.lower() or 'shortcut' in x.lower()))
        if icon_links:
            favicon_url = icon_links[0].get('href')
            
        # 2. 如果没找到，尝试默认路径 /favicon.ico
        if not favicon_url:
            favicon_url = urljoin(url, '/favicon.ico')
            
        # 确保图标 URL 是完整的
        if favicon_url:
            favicon_url = urljoin(url, favicon_url)
            
            # 下载图标
            icon_response = requests.get(favicon_url)
            icon_response.raise_for_status()
            
            # 创建保存目录
            if not os.path.exists('favicons'):
                os.makedirs('favicons')
                
            # 生成文件名
            domain = urlparse(url).netloc
            file_path = os.path.join('favicons', f'{domain}_favicon.ico')
            
            # 保存文件
            with open(file_path, 'wb') as f:
                f.write(icon_response.content)
                
            return file_path
                
    except Exception as e:
        print(f"获取图标时出错: {str(e)}")
        return None

def main():
    # 使用示例
    url = input("请输入要获取图标的网址: ")
    result = get_favicon(url)
    
    if result:
        print(f"图标已成功下载到: {result}")
    else:
        print("获取图标失败")

if __name__ == "__main__":
    main()