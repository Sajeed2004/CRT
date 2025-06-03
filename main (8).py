def push(value):
    top=-1
    if(top==4):
        return "stack is full"
    else:
        top=top+1
        return stack.append(value)
stack=[10]
push(20)
push(30)
push(40)
print(stack)