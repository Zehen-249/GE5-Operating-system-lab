class mem_block_unit:
    def __init__(self,proc_name:str,mem_size:int):
        self.proc_name = proc_name
        self.mem_size = mem_size

class mem_alooc:
    def __init__(self,mem_block:list, proc_block:list):
        self.mem_block = mem_block
        self.proc_block = proc_block
        

