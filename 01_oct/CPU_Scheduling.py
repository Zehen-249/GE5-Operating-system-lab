class Process:
    def __init__(self,count):
        self.processes = []
        self.process_count = count

        for i in range(self.process_count):
            pid = int(input(f"Enter  process {i+1} pid: "))

            for i in self.processes:
                if pid ==i[0]:
                    print("Process with this id Already exists")
                    break

            arr_time = int(input("Enter Arrival time: "))
            burst_time = int(input("Enter Burst time: "))
            self.processes.append([pid,arr_time,burst_time])
            print("\n")


    def apply_FCFS(self):
        print(f"Process Queue before: {self.processes}")
        scheduled_processes =  self.processes

        for i in range(self.process_count):
            min_index = i 
            for j in range(i+1,self.process_count):
                if scheduled_processes[j][1]<scheduled_processes[min_index][1]:
                    min_index = j
            temp = scheduled_processes[i]
            scheduled_processes[i] = scheduled_processes[min_index]
            scheduled_processes[min_index] = temp
        self.processes = scheduled_processes
        return self.processes 

    def apply_SJF(self):

        print(f"\nProcess Queue before: {self.processes}\n")
        processes = self.processes
        processes.sort(key=lambda x: (x[1], x[2]))  
        
        curr_time = 0  
        scheduled_processes = []

        for i in range(self.process_count):
            
            available_processes = [p for p in processes if p[1] <= curr_time and p not in scheduled_processes]
  
            if available_processes:
                next_process = min(available_processes, key=lambda x: x[2])  
                scheduled_processes.append(next_process)  
                curr_time += next_process[2]  
            else:
                next_process = min([p for p in processes if p not in scheduled_processes], key=lambda x: x[1])
                scheduled_processes.append(next_process)
                curr_time = next_process[1] + next_process[2]
        self.processes = scheduled_processes
        return self.processes 

    def apply_RR(self):
        pass
    
    def get_scheduling_props(self):
        curr = 0
        avg_wait = 0
        avg_turn =0
        avg_sub = 0
        avg_comp =0
        avg_idle = 0
        for i in self.processes:
            print(f"\nProcess {i[0]}")
            idle = 0
            if(curr<i[1]):
                idle = i[1] - curr
                avg_idle+=idle
                curr = i[1]
            sub = curr
            avg_sub+=sub

            wait = curr - i[1]
            avg_wait+=wait

            turn = wait + i[2]
            avg_turn+=turn

            comp = curr + i[2]
            avg_comp+=comp

            avg_idle+=idle
            curr = comp

            print(f"Waiting time: {wait}\nTurn Around time {turn}\nSubmision time {sub}\nComplition time {comp}\nIdeal time {idle}")
        print(f"\nAvg Waiting time: {avg_wait/self.process_count}\nAvg Turn Around time {avg_turn/self.process_count}\nAvg Submision time {avg_sub/self.process_count}\nAvg Complition time {avg_comp/self.process_count}\nAvg Ideal time {avg_idle/self.process_count}")

N = int(input("Enter Number of Processes: "))

process = Process(N)
print(f"After FCFS apllied: {process.apply_FCFS()}")
process.get_scheduling_props()
print("")
print(f"After SJF apllied: {process.apply_SJF()}")
process.get_scheduling_props()