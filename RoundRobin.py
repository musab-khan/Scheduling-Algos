file = open("processes.txt", 'r')
processes = {}
queue = []

for lines in file:
    this_line = lines.split(" ")
    processes [this_line[0]] = [int(this_line[1]), int(this_line[2].strip('\n'))]
file.close()

time_slice = 5
clock = 0
trap = 0
cpu = "free"

while processes != {}:
    for key in processes:
        if processes.get(key)[0] == clock:
            queue.insert(0, key)

    if cpu == "free" and queue != []:
        cpu = queue[len(queue)-1]
        start_time = clock

    clock = clock + 1
    #trap = trap + 1

    if cpu != 'free':
        processes.get(cpu)[1] = processes.get(queue[len(queue) - 1])[1] - 1
        trap = trap + 1
    # processes.get(queue[len(queue)-1])[1] = processes.get(queue[len(queue)-1])[1] -1
    if queue != [] and processes.get(cpu)[1] == 0:
    #if processes.get(queue[len(queue)-1])[1] == 0:
        #print(str(start_time) + "____" + queue[len(queue) - 1] + "____" + str(clock))
        print(str(start_time) + "____" + cpu + "____" + str(clock))
        del processes[cpu]
        queue.pop()
        start_time = clock
        cpu = "free"
        trap = 0

    elif queue != [] and trap == time_slice:
        #print(str(start_time) + "____" + queue[len(queue) - 1] + "____" + str(clock))
        print(str(start_time) + "____" + cpu + "____" + str(clock))
        poped = queue.pop()
        queue.insert(0, poped)
        start_time = clock
        trap = 0
        cpu = "free"
