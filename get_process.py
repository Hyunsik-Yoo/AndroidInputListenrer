import re
from process_manager import ProcessManager

logcat_file = open('test.txt','r')
process_manager = ProcessManager()

# TODO: 프로세스 시작시간 알아야 한다. adb프로세스 시작하면서 시작시간을 저장해놓는 방법!

for row in logcat_file:
    
    row = row.strip()
    split_list = row.split('ActivityManager: ')

    time = split_list[0]
    contents = split_list[1]
    
    time_slice = time.split(' ')
    time_slice = list(filter(lambda item : item != '', time_slice))
    time = time_slice[:2]
    time = ' '.join(time)

    if 'Displayed' in contents:
        package_activity = contents.split(' ')[1].split('/')
        package =  package_activity[0]
        activity = package_activity[1]
        activity = activity[:-1]
        # print('displayed package name : ' + package + '\t activity name : ' + activity)
        process_manager.start_app(package, time)
    elif 'Killing' in contents:
        package = contents.split(' ')[1]
        package = re.split('\:|\/', package)[1]
        process_manager.kill_app(package, time)
        # print('killing package name : ' + str(package))

process_manager.delete_not_killed()
process_list = process_manager.get_process_list()
for process in process_list:
    print(process)

