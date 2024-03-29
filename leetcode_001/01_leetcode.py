

if __name__ == '__main__':
    print("LeetCode 01 Running")

nums = [2,7,11,15]
target = 9
index = []
for num in nums:
    #print(target - num)
    if target - num in nums:
        #print(num)
        index.append(nums.index(num))

print(index)