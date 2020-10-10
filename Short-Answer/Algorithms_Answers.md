#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) RunTime Complexity is O(n). The total runtime of the loop is O(1).
The runtime of the while loop is O(n) because only one variable is altered.

b) RunTime Complexity is O(nlog(n)). The runtime of the for loop is O(n), but while loop is halved the distance between n and j, so the runtime of while loop is O(log(n)).

c)RunTime Complexity is O(n), because there is only one recursion call that depends on an input. Space Complexity is O(n).

## Exercise II

Since this is a building, we have a sorted array of floors.
The best way for searching in a sorted array is a Binary Search.
Time complexity for Binary search is O(log(n))

```Pseudocode:
start = first_floor
end = highest_floor
count_egg = 0
count_broken_egg = 0
while start < end
    middle_floor = (start + end) // 2
    count_egg++
    if start == end:
        return count_egg + count_broken_egg
    elif dropped egg gets broken:
        count_broken_egg++
        eliminate floors that are located higher then the middle one
        repeat search with end = middle_floor -1
    else dropped egg does not get broken
        eliminate floors that are located lower then the middle one
        repeat search with start = middle_floor +1


```
