file = open("processes.txt", 'r')
processes = {}
queue = []
wait = {}
wait_help = []
wt_time = {}
turn_time = {}
avg_turn = 0
avg_wait = 0
#copy = {}

for lines in file:
    this_line = lines.split(" ")
    processes[this_line[0]] = [int(this_line[1]), int(this_line[2]), int(this_line[3]), int(this_line[4].strip('\n'))]
file.close()

#copy = processes.copy()

time_slice = 5
clock = 0
trap = 0
cpu = "free"
each_IO_after = 2

while processes != {}:
    for key in processes:
        if processes.get(key)[0] == clock:
            queue.insert(0, key)

    if wait != {}:
        for key in wait:
            if wait.get(key) == clock:
                queue.insert(0, key)
                #del wait[key] gives runtime error
                wait_help.append(key)
        for i in wait_help:
            del wait[i]
        wait_help.clear()

    if queue != []:
        for proc in queue:
            if processes.get(proc)[2] > 0:
                processes.get(proc)[3] = processes.get(proc)[3] + 1
                if processes.get(proc)[3] == each_IO_after:
                    if proc == cpu:
                        processes.get(proc)[3] = 0
                        print(str(start_time) + "____" + cpu + "____" + str(clock + 1))
                        poped = queue.pop(queue.index(proc))
                        wait[poped] = (clock + 1) + (processes.get(proc)[2])
                        start_time = clock
                        cpu = "free"
                        trap = 0
                    else:
                        processes.get(proc)[3] = 0
                        poped = queue.pop(queue.index(proc))
                        wait[poped] = (clock + 1) + (processes.get(proc)[2])

    if cpu == "free" and queue != []:
        cpu = queue[len(queue) - 1]
        start_time = clock

    clock = clock + 1

    if cpu != 'free':
        processes.get(cpu)[1] = processes.get(queue[len(queue) - 1])[1] - 1
        trap = trap + 1
    if queue != [] and processes.get(cpu)[1] == 0:
        #copy.get(cpu).append(clock)
        wt_time[cpu] = clock - processes.get(cpu)[0] - processes.get(cpu)[1]
        avg_wait = avg_wait + wt_time[cpu]
        turn_time[cpu] = clock - processes.get(cpu)[0]
        avg_turn = avg_turn + turn_time[cpu]
        print(str(start_time) + "____" + cpu + "____" + str(clock))
        del processes[cpu]
        queue.pop()
        start_time = clock
        cpu = "free"
        trap = 0

    elif queue != [] and trap == time_slice:
        print(str(start_time) + "____" + cpu + "____" + str(clock))
        poped = queue.pop()
        queue.insert(0, poped)
        start_time = clock
        trap = 0
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
#      print (key + "\t\t\t" + str((copy.get(key)[4] - copy.get(key)[0]) - copy.get(key)[1]) + "\t\t\t" + str(copy.get(key)[4] - copy.get(key)[0]))
#print (copy)