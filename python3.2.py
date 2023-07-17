input = input("Enter Input : ")
sound_stack = []
weight_stack = []
list = [st for st in input.split(",")]

if input:
    for st in list:
        if len(st.split()) != 2:
            exit()

    for st in list:
        weight, sound = st.split()
        weight = int(weight)

        if weight_stack != []:
            while weight_stack and weight > weight_stack[-1]:
                print(sound_stack.pop())
                weight_stack.pop()
                
            weight_stack.append(weight)
            sound_stack.append(sound)
        else:
            weight_stack.append(weight)
            sound_stack.append(sound)