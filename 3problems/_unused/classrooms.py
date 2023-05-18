import heapq

# Input the number of activities and classrooms
activityC, classroomC = list(map(int, input().split()))

# Initialize the priority queue for activities
activities = []
for _ in range(activityC):
    start, end = list(map(int, input().split()))
    heapq.heappush(activities, (end, start))  # Order by earliest end time, then earliest start time

# Initialize the priority queue for classrooms
classrooms = [0] * classroomC

# Schedule the activities
can_schedule = 0
while activities:
    earlyEnd, earlyStart = heapq.heappop(activities)
    freeRoom = classrooms[0]
    if earlyEnd > freeRoom and earlyStart > freeRoom:
        heapq.heappop(classrooms)
        heapq.heappush(classrooms, earlyEnd)
        can_schedule += 1

# Print the number of activities that can be scheduled
print(can_schedule)