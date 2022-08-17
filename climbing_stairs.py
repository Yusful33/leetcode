# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
def climbStairs(n):
    full = [1] * n
    print(full)
    tries = 1
    for index, val in enumerate(full):
        if full[index] == 1 and full[index-1] == 1:
            del full[index]
            full[index-1] = 2
            tries += 1
    #What about the inverse of list???? (follow up tomorrow)
    print(full, full[::-1])
    print(f'Number of tries {tries}')

# climbStairs(3)

#Leverage Caching or Memoization to accomplish in O(n)
def NEETclimbStairs(n):
    #BottomUp Dynamic Programing Approach
    # Two variables shifted n-1 times 
    one, two = 1,1
    for i in range(n-1):
        temp_one = one
        print(f'Temp One {temp_one}')
        one = one + two 
        print(f'One {one}')
        two = temp_one
        print(f'Two {two}')
    return one
test = NEETclimbStairs(5)
print(test)