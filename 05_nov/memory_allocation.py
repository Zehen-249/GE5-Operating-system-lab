class Proc_Block:
    def __init__(self):
        self.proc_block = []

    def add_process(self,proc_name:str, mem_size:int):
        proc = Proc_Block_Unit(proc_name,mem_size)
        self.proc_block.append(proc)
    
    def show_proc_block(self):
        for i in self.proc_block:
            print(f"procname {i.proc_name}, mem size {i.mem_size}")

class Proc_Block_Unit:
    def __init__(self,proc_name:str,mem_size:int):
        self.proc_name = proc_name
        self.mem_size = mem_size
        
class Mem_Block:
    def __init__(self):
        self.mem_block = []
        self.copy=[]

    def add_mem_block(self,mem_loc:str, mem_size:int):
        mem_block = Mem_Block_Unit(mem_loc,mem_size)
        self.mem_block.append(mem_block)
        self.copy= self.mem_block

    def show_mem_block(self):
        for i in self.mem_block:
            if(not i.free):
                print(f"mem loc {i.mem_loc} of size {i.mem_size} is allocated with proc {i.aloc_proc.proc_name} of size {i.aloc_proc.mem_size}")
            else:
                print(f"mem loc {i.mem_loc} of size {i.mem_size} is unallocated ")

   
class Mem_Block_Unit:
    def __init__(self,mem_loc:str,mem_size:int):
        self.mem_loc = mem_loc
        self.mem_size = mem_size
        self.free = True
        self.aloc_proc = None
        


class Mem_Alloc:
    def __init__(self,proc_block,mem_block):
        self.proc_block = proc_block
        self.mem_block = mem_block

    def first_fit(self):
        for i in proc_block.proc_block:
            for j in mem_block.mem_block:
                if j.free & (i.mem_size<=j.mem_size):
                    j.aloc_proc = i
                    j.free = False
                    break
        
        # for i in mem_block.mem_block:
        #     if(not i.free):
        #         print(f"mem loc {i.mem_loc} of size {i.mem_size} is allocated with proc {i.aloc_proc.proc_name} of size {i.aloc_proc.mem_size}")
        #     else:
        #         print(f"mem loc {i.mem_loc} of size {i.mem_size} is unallocated ")

    def best_fit(self):
        self.mem_block.mem_block = sorted(self.mem_block.mem_block, key = lambda mem_block:mem_block.mem_size)
        # for i in self.mem_block.mem_block:
        #     if(not i.free):
        #         print(f"mem loc {i.mem_loc} of size {i.mem_size} is allocated with proc {i.aloc_proc.proc_name} of size {i.aloc_proc.mem_size}")
        #     else:
        #         print(f"mem loc {i.mem_loc} of size {i.mem_size} is unallocated ")
        self.first_fit()
        
    def clear_alloc(self):
        self.mem_block.mem_block = self.mem_block.copy
        for i in mem_block.mem_block:
            if(not i.free):
                i.aloc_proc = None
                i.free = True

proc_block = Proc_Block()
proc_block.add_process('1',200)
proc_block.add_process('2',100)
proc_block.add_process('3',150)

mem_block = Mem_Block()
mem_block.add_mem_block('1',500)
mem_block.add_mem_block('2',40)
mem_block.add_mem_block('3',300)

alloc_mem = Mem_Alloc(proc_block,mem_block)

mem_block.show_mem_block()

alloc_mem.first_fit()
print()
mem_block.show_mem_block()
alloc_mem.clear_alloc()

alloc_mem.best_fit()
print()
mem_block.show_mem_block()
alloc_mem.clear_alloc()

