import os

# multiple forks
# pid = os.fork()
# print(f"Parent Process {os.getpid()} Created Child {pid}")
# pid = os.fork()
# print(f"Parent Process {os.getpid()} Created Child {pid}")
# pid = os.fork()
# print(f"Parent Process {os.getpid()} Created Child {pid}")

# different code for parent and child

# def child():
#     print("Child is running")
    
# def parent():
#     print("Parent is running")
#     pid,status = os.wait()
#     print("Child Completed")
    

# def main():
#     pid=os.fork()
#     if(pid==0):
#         child()
        
#     else:
#         parent()
        
# if __name__=="__main__":
#     main()


def child():
    os.execl('/bin/ls','ls','-l')
    
def parent():
    print("Parent is running")
    pid,status = os.wait()
    print("Child Completed")
    

def main():
    pid=os.fork()
    if(pid==0):
        print("Child is Running")
        child()
        
    else:
        parent()
        
if __name__=="__main__":
    main()