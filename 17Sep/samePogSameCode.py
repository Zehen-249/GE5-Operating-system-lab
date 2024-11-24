import os

def main():
    pid = os.fork()
    print(f"Parent Process {os.getpid()} Created Child {pid}")
    print(sum(3,5))

def sum(a,b):
    return a+b


if __name__=="__main__":
    main()