import re
from process_manager import ProcessManager
from datetime import datetime


def get_process(logcat_file_name):

    # 파일 읽기 및 ProcessManager 객체 생성
    logcat_file = open(logcat_file_name,'r')
    process_manager = ProcessManager()

    # 상대시간을 구하기 위해 첫번째 시간읽기
    first_flag = True
    start_time = ''

    # logcat한줄씩 읽으며 파싱
    for row in logcat_file:

        row = row.strip()
        split_list = row.split('ActivityManager: ')

        time = split_list[0]
        contents = split_list[1]

        # time파트에서 원하는 부분 (시:분:초.초) 형태만 가져오기
        time_slice = time.split(' ')
        time_slice = list(filter(lambda item : item != '', time_slice))
        time = time_slice[1]

        # 상대시간을 구하기위해 첫번째 loop에서만 시간 저장 (나중에 시간 - 첫시간 으로 상대시간 구함)
        if(first_flag):
            start_time = time
            first_flag = False



        # datetime를 사용해 시간빼기 (time delta) -> 이후 초로 변경
        time_format = '%H:%M:%S.%f'
        relative_time = datetime.strptime(time, time_format)- datetime.strptime(start_time, time_format)
        relative_time = relative_time.total_seconds()


        # Displayed일 경우 앱의 새로운 activity가 뜬경우이다.
        if 'Displayed' in contents:
            package_activity = contents.split(' ')[1].split('/')
            package =  package_activity[0]

            #activity = package_activity[1] #Activity 구분까지 할필요 없으므로 주석처리
            #activity = activity[:-1]
            process_manager.start_app(package, relative_time) # 패키지 이름과 시작시간 저장

        # Killing일 경우 종료되었음을 의미.
        elif 'Killing' in contents:
            package = contents.split(' ')[1]
            package = re.split('\:|\/', package)[1]
            process_manager.kill_app(package, relative_time) # 패키지 이름과 종료시간 저장(상대시간)

    # logcat을 주기적으로 실행, 종료를 반복하기 때문에 중간에 잘리는 경우도 존재.
    # 이때 로그상의 종료되지 않은 프로세스는 오류처리시켜 제외한다.
    process_manager.delete_not_killed()

    return process_manager