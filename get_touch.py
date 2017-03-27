import re


def get_touch(getevent_file_name):

    getevent_file = open(getevent_file_name,'r')

    # 상대시간을 구하기 위해 설정하는 변수 (첫 번째 row의 시간을 저장)
    first_time = 0
    first_flag = True

    touch_list = []

    # 한줄씩 파싱 시작
    for row in getevent_file:

        one_touch = []
        # TODO: 첫번째 라인 삭제해야 함
        # TODO: 마지막라인에 잘리는것 확인해야 한다.

        row = row.strip()
        split_list = re.split(' |\[ |\]',row)
        split_list = list(filter(lambda item: item != '', split_list))

        try:
            split_list.remove(split_list[1])
        except Exception as e:
            print(split_list)
            raise e

        # 첫번째 줄에서만 시간 저장하고 flog 변경
        if first_flag:
            first_time = float(split_list[0])
            first_flag = False

        split_list[0] = float(split_list[0]) - first_time
        try:
            split_list[-1] = int(split_list[-1],16)
        except:
            pass

        if (split_list[2] == 'BTN_TOOL_FINGER' and split_list[3] == 'DOWN'):
            one_touch.append(split_list[0])
        elif split_list[2] == 'ABS_MT_POSITION_X':
            one_touch.append(split_list[3])
        elif split_list[2] == 'ABS_MT_POSITION_Y':
            one_touch.append(split_list[3])
        elif (split_list[2] == 'BTN_TOOL_FINGER' and split_list[3] == 'UP'):
            one_touch.append(split_list[0])
            touch_list.append(one_touch)

    result = []
    for item in touch_list:
        touch_event = item[:3]
        touch_event.extend(item[-3:])
        result.append(touch_event)

    return result
