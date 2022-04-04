from collections import deque

def isBalanced(s):
    
    a = set([('[', '(', '{')])
    pairs = set([('{','}'), ('[',']'), ('(',')')])
    stack = deque()
    
    for i in range(len(s)):
        if(len(stack) == 0):
            stack.append(s[i])
        else:
            if((stack[-1], s[i]) in pairs):
                stack.pop()
            else:
                stack.append(s[i])
                
    if(len(stack) == 0):
        return "YES"
    return "NO"
            
    
s = "{{[[(()]]}}"
print(isBalanced(s))
