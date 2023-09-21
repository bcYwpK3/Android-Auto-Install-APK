import os
import subprocess

GREEN = "\033[1;32m"
RED = "\033[1;31m"
RESET = "\033[0m"

try:
    current_path = os.path.dirname(os.path.realpath(__file__))
    print(f"获取当前脚本的路径=========> {GREEN}SUCCESS{RESET}")
except Exception as e:
    print(f"获取当前脚本的路径=========> {RED}FAIL{RESET}\n{e}")

try:
    apk_dir = os.path.join(current_path, 'apk')
    print(f"定义APK文件的路径=========> {GREEN}SUCCESS{RESET}")
except Exception as e:
    print(f"定义APK文件的路径=========> {RED}FAIL{RESET}\n{e}")

try:
    apk_files = [f for f in os.listdir(apk_dir) if f.endswith('.apk')]
    print(f"获取所有的APK文件=========> {GREEN}SUCCESS{RESET}")
except Exception as e:
    print(f"获取所有的APK文件=========> {RED}FAIL{RESET}\n{e}")

try:
    result = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE)
    devices = result.stdout.decode('utf-8')
    print(f"获取设备列表=========> {GREEN}SUCCESS{RESET}")
except Exception as e:
    print(f"获取设备列表=========> {RED}FAIL{RESET}\n{e}")

try:
    device_ids = [line.split()[0] for line in devices.splitlines() if line and not line.startswith('List')]
    print(f"从设备列表中解析出设备ID=========> {GREEN}SUCCESS{RESET}")
except Exception as e:
    print(f"从设备列表中解析出设备ID=========> {RED}FAIL{RESET}\n{e}")

for device_id in device_ids:
    for apk_file in apk_files:
        apk_path = os.path.join(apk_dir, apk_file)
        try:
            print(f'Installing {apk_file} to device {device_id}')
            subprocess.run(['adb', '-s', device_id, 'install', apk_path])
            # subprocess.run(['adb','shell', '-s', device_id, 'reboot','-p'])
            print(f'安装 {apk_file} 到设备 {device_id} =====> {GREEN}SUCCESS{RESET}')
        except Exception as e:
            print(f'安装 {apk_file} 到设备 {device_id} =====> {RED}FAIL{RESET}\n{e}')