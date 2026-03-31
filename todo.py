tasks=[]
while True:
    print("\n---To do list---")
    print("1.add task")
    print("2.view task")
    print("3.remove task")
    print("4.exit")
    choice=input("enter the choice:").strip()
    if choice=="1":
        task=input("enter task:")
        tasks.append(task)
        print("task added!")
    elif choice=="2":
        print("\nyour tasks:")
        for i, t in enumerate(tasks):
            print(i+1,".", t)
    elif choice=="3":
        num=int(input("enter task number to remove:"))
        if 0<num<=len(tasks):
            removed =tasks.pop(num-1)
            print("removed:", removed)
        else:
            print("invalid number")
    elif choice=="4":
        print("goodbyee")
        break
    else:
        print("invalid choice")

        

