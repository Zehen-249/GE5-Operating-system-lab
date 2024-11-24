import os

def main():
    pid = os.fork()
    if(pid==0):
        print(f"Parent Process {os.getpid()} Created Child {pid}")
        child(pid)
    else:
        print(f"Parent Process {os.getpid()} Created Child {pid}")
        parent(pid)


def sum(a,b):
    return a+b

def child(pid):
    print("Running Child",os.getpid())    
    print(f"Childprocess of parent {os.getppid()} Output is ",sum(1,3))
    print()
    
def parent(pid):
    print("Running Parent",os.getpid())    
    print("Parent Output",sum(3,5))
    print()
   
if __name__=="__main__":
    main()