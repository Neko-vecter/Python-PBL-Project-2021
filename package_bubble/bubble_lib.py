class bubble_lib:
    def __init__(self, arr):
        self.arr = arr
        self.all_arr = []

    def change_arr(self, arr):
        self.arr = arr
        self.all_arr = []
    
    def bubble(self):
        nums = self.arr
        for i in range(len(nums) - 1): 
            for j in range(len(nums) - i - 1): 
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
            test = list(nums)
            self.all_arr.append(test)
        print("finish sort")

    def get_list(self):
        return self.arr

    def get_finish(self):
        if(self.all_arr == []):
            return "Plz use bubble method to sort"
        else:
            return self.all_arr
