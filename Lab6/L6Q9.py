def run_length_encode(nums):
    if nums == []:
        return []
    cur_num = nums[0]
    cur_run = 1
    out_lst = []
    for i in range(1, len(nums)):
        if nums[i] == cur_num:
            cur_run += 1
        else:
            out_lst.append((cur_num, cur_run))
            cur_num = nums[i]
            cur_run = 1
            
    out_lst.append((cur_num, cur_run))
    return out_lst

data = [5, 5, 5, 10, 10]
print(run_length_encode(data))
data = [10, 20, 30, 30, 30, 30]
print(run_length_encode(data))
print(run_length_encode([1]))
print(run_length_encode([]))

	




        
        