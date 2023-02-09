import random
class Frame:
    def __init__(self,seqNo,data=None):
        self.seqNo = seqNo
        self.data = data
def merge_sort(arr):
    if (len(arr) > 1):
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
        merge_sort(left_arr)
        merge_sort(right_arr)
        i = 0
        j = 0
        k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i].seqNo < right_arr[j].seqNo:
                arr[k] = left_arr[i]
                i+=1
            else:
                arr[k]= right_arr[j]
                j+=1
            k+=1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i+=1
            k+=1
        while j < len(right_arr):
            arr[k]=right_arr[j]
            j+=1
            k+=1
n=int(input("Enter number of frames "))
seqList = []
for _ in range(n):
    r = random.randint(1,1*100)
    for r in seqList:
        r = random.randint(1,1*100)
    seqList.append(r)
frames = []
for _ in range(n):
    ch = random.choice(seqList)
    frames.append(Frame(ch))
    seqList.remove(ch)
for i in range(n): 
    frames[i].data = input(f"Enter data for {frames[i].seqNo} ")
merge_sort(frames)
for frame in frames:
    print(f"{frame.seqNo} -- {frame.data}")
