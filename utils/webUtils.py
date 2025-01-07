class WebUtils:

    @staticmethod
    def _is_valid_jpg_url(url):
        try:
            if url.startswith(('http://', 'https://')) and url.endswith('.jpg'):
                return True
            else:
                return False
        except Exception as e:
            return False

    @staticmethod
    def download_image_requests(url, file_path):
        print(url)
        if not WebUtils._is_valid_jpg_url(url):
            return False
        import requests
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
        }
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                print("图片下载成功！")
                return True
            else:
                print(f"下载失败，状态码: {response.status_code}")
                return False
            return True
        except Exception as e:
            print(f"下载失败，错误信息: {e}")
            return False
