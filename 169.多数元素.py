'''
摩尔投票法
'''
def majorityElement(nums):
	cnt = 0 
	group = -1
	for i in nums:
		print(group, cnt)
		if cnt == 0:
			group = i
			cnt = 1
		else:
			if i == group:
				cnt = cnt + 1
			else:
				cnt = cnt - 1
		
	cnt = 0
	for i in nums:
		if i == group:
			cnt = cnt + 1

	return group

print(majorityElement(nums = [8,8,7,7,7]))