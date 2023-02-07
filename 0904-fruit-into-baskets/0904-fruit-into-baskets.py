class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        curr_max = 0
        max_picked = 0
        last_fruit = 0
        second_last_fruit = 0 
        last_fruit_count = 0

        for fruit in range(len(fruits)):

            if fruits[fruit] == fruits[last_fruit] or fruits[fruit] == fruits[second_last_fruit]:
                curr_max += 1
            else:
                curr_max = last_fruit_count+1           # it updates the curr_max by removing count of 2nd last fruit and adding count of new fruit discovered

            if (fruits[fruit]==fruits[last_fruit]):
                last_fruit_count += 1                   # it means the last fruit is repeated
            else:
                last_fruit_count = 1                    # it means that new fruit is discovered and it updates the last_fruit_count of it
            
            if (fruits[fruit]!=fruits[last_fruit]):          # if new fruit is discovered and it updates the last_fruit to cuurent fruit and 2nd last fruit to last_fruit we discovered
                second_last_fruit = last_fruit
                last_fruit = fruit
            

            max_picked = max(max_picked, curr_max)          # it always gives the maximum subarray we found up untill now
        return max_picked