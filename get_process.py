import re

logcat_file = open('activity.txt','r')

for row in logcat_file:
    
    row = row.strip()
    split_list = row.split('ActivityManager: ')

    time = split_list[0]
    contents = split_list[1]
    
    time_slice = time.split(' ')
    time_slice = list(filter(lambda item : item != '', time_slice))
    time = time_slice[:2]

    if 'Displayed' in contents:
        package_activity = contents.split(' ')[1].split('/')
        package =  package_activity[0]
        activity = package_activity[1]
        activity = activity[:-1]
        print('displayed package name : ' + package + '\t activity name : ' + activity)
    elif 'Killing' in contents:
        package = contents.split(' ')[1]
        package = re.split('\:|\/', package)[1]
        print('killing package name : ' + str(package))

