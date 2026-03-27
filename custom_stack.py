def is_valid_parentheses(s: str) -> bool:
    # stack to track opening brackets
    stack = []
    
    # map closing brackets to their opening pair
    bracket_map = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    for char in s:
        if char in bracket_map:
            # it's a closing bracket - check if it matches top of stack
            if stack and stack[-1] == bracket_map[char]:
                stack.pop()
            else:
                return False
        elif char in '({[':
            # it's an opening bracket - push to stack
            stack.append(char)
    
    # valid if stack is empty (all brackets matched)
    return len(stack) == 0