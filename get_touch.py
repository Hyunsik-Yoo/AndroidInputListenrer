import re

getevent_file = open('touch_event.txt','r')

first_time = 0
first_flag = True

touch_list = []
one_touch = []

for row in getevent_file:

    row = row.strip()
    split_list = re.split(' |\[ |\]',row)
    split_list = list(filter(lambda item: item != '', split_list))
    split_list.remove(split_list[1])
    if first_flag:
        first_time = float(split_list[0])
        first_flag = False

    split_list[0] = float(split_list[0]) - first_time
    try:
        split_list[-1] = int(split_list[-1],16)
    except:
        pass
    """
    if split_list[1] == "EV_SYN":
        touch_list.append(one_touch)
        one_touch = []
    """

    if (split_list[2] == 'BTN_TOOL_FINGER' and split_list[3] == 'DOWN'):
        one_touch.append(split_list[0])
    elif split_list[2] == 'ABS_MT_POSITION_X':
        one_touch.append(split_list[3])
    elif split_list[2] == 'ABS_MT_POSITION_Y':
        one_touch.append(split_list[3])
    elif (split_list[2] == 'BTN_TOOL_FINGER' and split_list[3] == 'UP'):
        one_touch.append(split_list[0])
        touch_list.append(one_touch)
        one_touch = []
 

result = []
for item in touch_list:
    touch_event = item[:3]
    touch_event.extend(item[-3:])
    result.append(touch_event)
    touch_event = []

print('시작시간 X1, Y1, X2, Y2, 이동시간')
for touch_event in result:
    print(touch_event)
