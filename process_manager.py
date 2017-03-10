class ProcessManager:
    
    def __init__(self):
        self.process_list = dict()

    def start_app(self, package_name, start_time):
        # 앱이 종료되고 다시 시작되면 어떻게 처리 ?
        
        process = dict()
        process['package_name'] = package_name
        process['start_time'] = start_time

    def add_activity
