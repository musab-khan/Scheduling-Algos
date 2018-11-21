file = open("processes.txt", 'r')
processes = {}
queue = []
#copy = {}
wt_time = {}
turn_time = {}
avg_turn = 0
avg_wait = 0

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
        n = len(queue)
        for i in range(n):
            for j in range(0, n - i - 1):
                if processes.get(queue[j])[1] < processes.get(queue[j + 1])[1]:
                    queue[j], queue[j + 1] = queue[j + 1], queue[j]

        cpu = queue[len(queue)-1]
        start_time = clock

    clock = clock + 1
    if cpu != 'free':
        processes.get(cpu)[1] = processes.get(queue[len(queue) - 1])[1] - 1

    if queue != [] and processes.get(cpu)[1] == 0:
        wt_time[cpu] = clock - processes.get(cpu)[0] - processes.get(cpu)[1]
        avg_wait = avg_wait + wt_time[cpu]
        turn_time[cpu] = clock - processes.get(cpu)[0]
        avg_turn = avg_turn + turn_time[cpu]
        #copy.get(cpu).append(clock)
        print(str(start_time) + "____" + cpu + "____" + str(clock))
        del processes[cpu]
        queue.pop()
        start_time = clock
        cpu = "free"

print ("\nWaiting time")
print (wt_time)
print ("Average wait time = " + str(avg_wait / len(wt_time.keys())))
print ("\nTurnaround time")
print (turn_time)
print ("Average turnaround time = " + str(avg_turn / len(turn_time.keys())))
# print ("\n\n" + "process" + '\t' + "waiting time" + '\t' + "turnaround time")
#
# for key in copy:
#      print (key + "\t\t\t" + str((copy.get(key)[2] - copy.get(key)[0]) - copy.get(key)[1]) + "\t\t\t" + str(copy.get(key)[2] - copy.get(key)[0]))
#print (copy)