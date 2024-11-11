import os

# print(dir(os))    #print all functions
# print(os.getcwd())  #print current working directory

#make directory 
# dir = "abc"
# path=os.path.join(os.getcwd(),dir)
# os.mkdir(path)

#make directory and set mode
# mode = 0o666
# dir ="def"
# path = os.path.join(os.getcwd(),dir)
# os.mkdir(path,mode)


# make subfolders
# dir = 'mno/pqr'
# path  = os.path.join(os.getcwd(),dir)
# os.makedirs(path)


# list directory
# print(os.listdir())

# create child process
# pid = os.fork()
# print(pid)
# if(pid>0):
#     print(f"Parent Process: My PID is {os.getpid()}, and i created child process {pid}.")
# elif(pid==0):
#     print(f"Child  Process: My PID is {os.getpid()}, and my parent's PID is {os.getppid()}" )
# else:
#     print("No PID")

#multiple child processes

# for i in range(2):
#     pid = os.fork()
#     print(pid)
#     if(pid>0):
#         print(f"Parent Process: My PID is {os.getpid()}, and i created child process {pid}.")
#     elif(pid==0):
#         print(f"Child  Process: My PID is {os.getpid()}, and my parent's PID is {os.getppid()}" )
#     else:
#         print("No PID")
