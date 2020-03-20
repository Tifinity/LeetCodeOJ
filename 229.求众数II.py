'''
摩尔投票法
'''
def majorityElement(nums):
	if nums == []:
		return []
	cnt = [0, 0]
	group = [0, 0]
	for i in nums:
		if i == group[0]:
			cnt[0] = cnt[0] + 1
			continue
		if i == group[1]:
			cnt[1] = cnt[1] + 1
			continue

		if cnt[0] == 0:
			group[0] = i
			cnt[0] = 1
			continue
		if cnt[1] == 0:
			group[1] = i
			cnt[1] = 1
			continue
		
		cnt[0] = cnt[0] - 1
		cnt[1] = cnt[1] - 1
		
	cnt = [0, 0]
	for i in nums:
		if i == group[0]:
			cnt[0] = cnt[0] + 1
		if i == group[1]:
			cnt[1] = cnt[1] + 1
	res = []
	if group[0] == group[1]:
		return [group[0]]
	if cnt[0]>len(nums)/3:
		res.append(group[0])
	if cnt[1]>len(nums)/3:
		res.append(group[1])
	return res

print(majorityElement(nums = [1,1,1,3,3,2,2,2]))