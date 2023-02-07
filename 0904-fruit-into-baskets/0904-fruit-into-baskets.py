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
    
    # ANOTHER APPROCH
    
    def totalFruit(fruits):
    n = len(fruits)
    c1, c2 = 0, 0  # Counter variables to keep track of the count of fruits in the two baskets
    t1, t2 = -1, -1  # Variables to keep track of the two types of fruits in the baskets
    ans = i = 0  # ans variable to store the maximum number of fruits picked, and i variable to keep track of the left pointer
    
    for j in range(n):
        # If the current fruit is the same as the first type of fruit in the baskets
        if fruits[j] == t1 or t1 == -1:
            c1 += 1
        # If the current fruit is the same as the second type of fruit in the baskets
        elif fruits[j] == t2 or t2 == -1:
            c2 += 1
        # If the current fruit is different from both types of fruits in the baskets
        else:
            ans = max(ans, j - i)  # Update the maximum number of fruits picked
            i = j - 1  # Move the left pointer back to the previous tree
            
            # Move the left pointer back until it is pointing to the first tree with the second type of fruit
            while fruits[i] == t2:
                i -= 1
                c2 -= 1
                
            # Update the two types of fruits in the baskets and their count
            t1, t2 = t2, fruits[j]
            c1, c2 = c2, 1
            
    # Update the final answer after processing all the trees
    ans = max(ans, n - i)
    return ans
