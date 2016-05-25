hourEnd = "19:30"
# def x(hourEnd):
hourEnd = list(hourEnd)
if hourEnd[3] == '0':
    hourEnd[3] = '3'
elif hourEnd[3] == '3':
    if hourEnd[1] == '9' and hourEnd[0] == "0":
        hourEnd[0] = "1"
        hourEnd[1] = "0"
        hourEnd[3] = '0'
    elif hourEnd[1] == '9' and hourEnd[0] == "1":
        hourEnd[0] = "2"
        hourEnd[1] = "0"
        hourEnd[3] = '0'
    else:
        hourEnd[1] = str(int(hourEnd[1]) + 1)
print hourEnd

# print x("09:00")
# print x("09:30")
# print x("10:00")
# print x("19:30")
# print x("21:30")