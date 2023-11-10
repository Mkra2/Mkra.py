import requests
from termcolor import colored

def check_proxy(proxy):
    try:
        response = requests.get('https://www.google.com', proxies={'https': proxy}, timeout=5)
        if response.status_code == 200:
            print(colored(f'{proxy} | Sống', 'green'))
            return True
        else:
            print(colored(f'{proxy} | Chết', 'red'))
            return False
    except requests.exceptions.RequestException:
        print(colored(f'{proxy} | Chết', 'red'))
        return False

def read_proxies_from_file(file_path):
    with open(file_path) as file:
        proxies = file.readlines()
    proxies = [proxy.strip() for proxy in proxies]
    return proxies

def save_live_proxies_to_file(proxies, file_path):
    with open(file_path, 'w') as file:
        for proxy in proxies:
            file.write(proxy + '\n')

file_path = 'proxy.txt'  # Thay đổi đường dẫn tới file của bạn
proxies = read_proxies_from_file(file_path)

live_proxies = []
for proxy in proxies:
    if check_proxy(proxy):
        live_proxies.append(proxy)

live_proxies_file_path = 'live_proxies.txt'  # Thay đổi đường dẫn tới file lưu danh sách proxy sống
save_live_proxies_to_file(live_proxies, live_proxies_file_path)

print('Đã lưu danh sách proxy sống vào file live_proxies.txt')