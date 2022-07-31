points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

illegal = []
score2 = []
f = open("input2")

#to find illegal -> stack and unstack when end found
for l in f:
    corrupted = False
    stack = []
    for c in l.strip():
        if c in ['(', '<', '[', '{']:
            stack.append(c)
        elif len(stack) > 0 and (
          (stack[-1] == '<' and c == '>') or
          (stack[-1] == '[' and c == ']') or
          (stack[-1] == '(' and c == ')') or
          (stack[-1] == '{' and c == '}')
        ):
            stack.pop()
        else:
            corrupted = True
            illegal.append(c)
            break
    if corrupted:
        continue
    score = 0
    stack.reverse()
    for c2 in stack:
        score *= 5
        score += points[c2]
    score2.append(score)

print(sum(points[c] for c in illegal))
print(sorted(score2)[len(score2) // 2])
