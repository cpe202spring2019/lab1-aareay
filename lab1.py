

def max_list_iter(int_list):  # must use iteration not recursion
    
    if int_list == None:
        raise ValueError
    if int_list == []:
        return None # I wanted to build this into the for loop's logic, but can't do int > None
    
    max_int = int_list[0] # doesn't work for negatives
    
    for i in int_list:
        if i > max_int:
            max_int = i

    return max_int


print(max_list_iter([-12321, -123, -1]))

def reverse_rec(int_list):   # must use recursion

    if int_list == None:
        raise ValueError

    if len(int_list) <= 1:
        return int_list
    index = len(int_list) - 1
    
    return int_list[index:] + reverse_rec(int_list[:index])


#print(reverse_rec([1, 2, 3, 4, 5]))
#print(reverse_rec([]))
#print(reverse_rec(None))
#print(reverse_rec([5, 4, 3, 2, 1]))


def bin_search(target, low, high, int_list):  # must use recursion
    # is low and high referring to the index or element?
    if int_list == None:
        raise ValueError
    if int_list == [] or target < int_list[low] or (target > 
            int_list[high]):   #  or int_list.count(target) == 0:
        return None
    
    # is there a more efficient way to do these? regardless, the program will need a return 
        # none, whether it be here or later in the loop/recursive return statement
    # i think it makes more sense to put the out of bounds or not in list conditions here, as they only
        # need to be evaluated once. They will be true regardless of what the ceiling or floor is. 
    # Also, this would need to be another condition the while addresses below, so all of this HAS to get
        # written (i think) at some point
    # how does python evaluate what int_list[high] is and int_list.count(x)? is there some sort of linear
        # mapping that goes into this, or can the progam just instantly jump to the last index 
        # I think count() would be the most likely offender here


    ## if count() is linear...can't include i
        # solution: if top == bottom and top/bottom/middle (which will all be the same at this point)
            # ...and t/b/m != target, then return none
                # only prob is, func() will have to run its full course to achieve this state, so it is the 
                # worst possible runtime, but idk how i'd detect this without count() or in at an earlier
                # stage in the program's runtime

    # OPTIONS:
    # list.count(target): O(n) every time, as every element must be scanned
    # target in list: O(n) in worst case, varies depending on first(if any) occurence of target
    # binary search: O(logn)  if top == bottom and list[midpoint/top/bot] != target 





    # search starts, weeding done earlier
    # ask about seeing if its higher or lower than top/bot, doesn't seem like O(n)
    # we'll know if the target isn't in the list far quicker if we do binary search
    # since we're calling it a ton of times, def don't want linear shit inside


    midpoint = (low + high) // 2

    # should i have a return condition that returns if target is found at int_list[high] or [low]
    # does it make sense to include an if list[low] == target return low? bc if its bin search 
        # if target is either low or high it takes a few more passes to find that out. Is this faster? 
    if int_list[midpoint] == target:
        return midpoint
    
    elif int_list[midpoint] < target:
        return bin_search(target, midpoint + 1, high, int_list)
    else:
        return bin_search(target, low, midpoint, int_list)
        
   
print(bin_search(0, 0, 5, [0, 1, 2, 3, 4, 5]))
print(bin_search(7, 0, 7, [0, 1, 4, 7, 12, 13, 13, 16]))

        





