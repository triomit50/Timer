from code import timer

print("Hello!! Welcome to TrioTimer !!!\nKindly enter the time in the format of:\nhr,mins,secs ; separated with a space (such as: 2 3 4).")
timee=input("Enter the time for the timer countdown:")
hrs,mins,secs = timee.split(' ')
hrs = int(hrs)
mins = int(mins)
secs = int(secs)
time_in_secs = (((hrs*60)+mins)*60)+secs
print("Time left: ")
timer(time_in_secs)
print("Time over !!!!!")