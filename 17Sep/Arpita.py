'''import threading

def calculate_sum(n):
    return sum(range(1, n + 1))

def main():
    n = int(input('Enter value for n: '))


    def thread_task():
        global sum_result
        sum_result = calculate_sum(n)


    sum_thread = threading.Thread(target=thread_task)
    sum_thread.start()
    sum_thread.join()

    print('Total sum is', sum_result)
main()'''


# processes = [1, 2, 3, 4] # PIDs
# burst_time = [5, 9, 6, 3] 
# waiting_time = [0,0,0,0]
# turnaround_time = [0,0,0,0]

# for i in range(1, len(processes)):
#     waiting_time[i] = waiting_time[i - 1] + burst_time[i - 1]

# for i in range(len(processes)):
#     turnaround_time[i] = waiting_time[i] + burst_time[i]

# total_waiting_time = sum(waiting_time)
# total_turnaround_time = sum(turnaround_time)

# print("Process | Burst Time | Waiting Time | Turnaround Time")
# for i in range(len(processes)):
#     print(" {} | {} | {} | {}".format(processes[i], burst_time[i], waiting_time[i], turnaround_time[i]))


# average_waiting_time = total_waiting_time / len(processes)
# average_turnaround_time = total_turnaround_time / len(processes)
# print("Average Waiting Time",{average_waiting_time})
# print("Average Turnaround Time",{average_turnaround_time})

with open('file1.txt', 'r') as file:
    with open("file2.txt",'w') as file2:
        buffer = file.read(10)
        while(buffer):
            print(buffer,end="\n")
            file2.write(buffer)
            buffer = file.read(10)