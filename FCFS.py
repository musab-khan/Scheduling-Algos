file = open("processes.txt", 'r')
processes = {}
queue = []
#copy = {}

for lines in file:
    this_line = lines.split(" ")
    processes[this_line[0]] = [int(this_line[1]), int(this_line[2].strip('\n'))]

file.close()

#copy = processes.copy()

clock = 0
cpu = "free"

while processes != {}:
    for key in processes:
        if processes.get(key)[0] == clock:
            queue.insert(0, key)

    if cpu == "free" and queue != []:
        cpu = queue[len(queue) - 1]
        start_time = clock

    clock = clock + 1
    if cpu != 'free':
        processes.get(cpu)[1] = processes.get(queue[len(queue) - 1])[1] - 1

    if queue != [] and processes.get(cpu)[1] == 0:
        # copy.get(cpu).append(clock)
        print(str(start_time) + "____" + cpu + "____" + str(clock))
        del processes[cpu]
        queue.pop()
        start_time = clock
        cpu = "free"

# print ("\n\n" + "process" + '\t' + "waiting time" + '\t' + "turnaround time")
#
# for key in copy:
#      print (key + "\t\t\t" + str((copy.get(key)[2] - copy.get(key)[0]) - copy.get(key)[1]) + "\t\t\t" + str(copy.get(key)[2] - copy.get(key)[0]))
# print (copy)