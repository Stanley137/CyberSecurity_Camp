# writeup 

GOT hijacking is the key point of this lab, 
if there are some protection on the stack, we can use some ways to bypass the protection.
such as format_string to leak the canary, or change the GOT table like this lab's technique,
brute force is our last resort to solve the problem,
and I also have to make a self-criticism, **I didn't checksec first**, 
I didn't inspect the assembly code carefully, so that I miss the oppertunity to 
break this lab. I will keep motivating myself.

- In ghidra, if the function was loaded, we can see the GOT.