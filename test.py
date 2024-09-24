T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    strings = []
    for _ in range(M):
        string = input()
        strings.append(string)

    # Count the number of 1s and 0s at each position
    counts = [0] * N
    for string in strings:
        for i, char in enumerate(string):
            if char == '1':
                counts[i] += 1

    # Determine the optimal replacements
    replacements = [0] * N
    for i in range(N):
        diff = abs(counts[i] - (M - counts[i]))
        replacements[i] = diff // 2

    # Replace '?' characters
    for i in range(M):
        for j in range(N):
            if strings[i][j] == '?':
                if replacements[j] > 0:
                    strings[i][j] = '1' if counts[j] < (M - counts[j]) else '0'
                    replacements[j] -= 1

    # Print the modified strings
    for string in strings:
        print(''.join(string))