import operator

class ProcessManager:

    def __init__(self):
        self.process_list = list()

    def get_process_list(self):
        """
        :return: 프로세스 정보가 담긴 리스트 
        """
        return self.process_list

    def is_app_killed(self, package_name):
        """
        가장 최근에 실행된 프로세스가 kill되었는지 확인하는 함수
        """
        for process in reversed(self.process_list):
            if process['package_name'] == package_name:
                if process['kill_time'] is None:
                    return False
                else:
                    return True
        return True # 처음으로 삽입되는 경우

    def start_app(self, package_name, start_time):
        """
        새로운 앱이 실행되었을때 새로운 process dictionary를 생성하여 process_list에 삽입
        """
        
        if not(self.is_app_killed(package_name)):
            return # 종료되지 않은 동일한 프로세스가 있으니 무시

        process = dict()
        process['package_name'] = package_name
        process['start_time'] = start_time
        process['touch'] = list()
        process['kill_time'] = None

        self.process_list.append(process)

    def kill_app(self, package_name, kill_time):
        """
        시작된 프로세스가 없다면 무시한다.
        시작된 프로세스가 있다면 해당 프로세스의 dictonary kill_time입력한다.
        """

        for process in reversed(self.process_list):
            if process['package_name'] == package_name:
                if process['kill_time'] == None:
                    process['kill_time'] = kill_time
                    return

    def delete_not_killed(self):
        """
        전체 리스트를 순회하면서 kill_time이 없는(아직 종료되지 않은 프로세스)들을 제거해버린다.
        종료되지 않은 프로세스들의 kill_time은 None으로 되어있다.
        """
        for process in self.process_list:
            if process['kill_time'] == None:
                self.process_list.remove(process)

    def put_touch_event(self, list_event):
        self.process_list = self.sort_by_time()
        for event in list_event:
            start_time = event[0]

            for process in self.process_list:
                if start_time > process['start_time']:
                    process['touch'].append(event)
                    break


    def sort_by_time(self):
        """
        process_list를 start_time을 기준으로 오름차준 정렬하여 반환해 준다.
        :return start_time으로 정렬된 process_list: 
        """
        sorted_list = sorted(self.process_list, key=operator.itemgetter('start_time'))

        return sorted_list



    
