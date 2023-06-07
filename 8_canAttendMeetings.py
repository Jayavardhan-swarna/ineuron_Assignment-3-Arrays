def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort the intervals based on start time

    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i + 1][0]:
            return False  # Overlapping intervals found

    return True  # No overlapping intervals found

intervals = [[0, 30], [5, 10], [15, 20]]
result = canAttendMeetings(intervals)
print(result)
