## Explanation

The `is_user_in_group` function is recursive. It check for the user in the first group, if it is found then returns true, otherwise it calls itself again recursively passing the user and the child groups to the function.

## Big O

**O(log(n))**