import random
from datetime import datetime

def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
       s_nums = []
       m_nums = []
       e_nums = []
       for n in nums:
           if n < q:
               s_nums.append(n)
           elif n > q:
               m_nums.append(n)
           else:
               e_nums.append(n)
       return quicksort(s_nums) + e_nums + quicksort(m_nums)

def main():
    r = random.randint(1, 1000000)
    arr = [0] * r
    for i in range(len(arr) - 1):
        arr[i] = random.randint(1, 1000000)

    start_time = datetime.now()
    quicksort(arr)
    print(f"Qsort {r} elements {datetime.now() - start_time}")



if __name__ == '__main__':
    main()