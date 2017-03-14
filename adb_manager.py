# 단말기가 전부 무선 adb로 연결되어있다는 전제하에 진행
# 1. adb로 연결된 단말기 탐색
# 2. 단말기마다 다른 디렉토리를 생성하고 디렉토리에 logcat, getevent 파일 생기도록 프로세스 실행
# 3. 디렉토리명은 IP주소로?
# 4. 특정 단위시간 설정하여 파일쓰기 끊고 새로운 파일로 만들어야 하는 과정?
import subprocess

adb_directory = '/Users/macgongmon/Downloads/android-sdk/platform-tools/'

def detect_devices():
    """
    무선 adb로 연결된 단말기들 찾아서 출력
    연결된 단말기들의 내부IP주소를 리스트로 연결하여 반환
    """
    list_device = []

    command = adb_directory + "adb devices"
    proc_devices = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE)
    devices,err = proc_devices.communicate()
    devices = devices.decode('utf-8').split('\n')[1:-2] # 첫row (제목), 마지막2 row (빈칸) 제거
    
    for device in devices:
        device_ip = device.split(':5555')[0]
        list_device.append(device_ip)

    return list_device


def run_logcat():
    command = "adb shell logcat |grep ActivityManger:"


if __name__ == '__main__':
    detect_devices()


