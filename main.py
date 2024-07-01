def optimal_bst(keys, freq):
    n = len(keys)
    cost = [[0 for x in range(n)] for y in range(n)]
    root = [[0 for x in range(n)] for y in range(n)]

    # Initialize the cost and root for single keys
    for i in range(n):
        cost[i][i] = freq[i]
        root[i][i] = i

    # Compute the cost and root for larger subtrees
    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            cost[i][j] = float('inf')

            # Try making all keys in interval keys[i..j] as root
            for r in range(i, j + 1):
                c = (cost[i][r - 1] if r > i else 0) + (cost[r + 1][j] if r < j else 0) + sum(freq[i:j + 1])
                if c < cost[i][j]:
                    cost[i][j] = c
                    root[i][j] = r

    return cost, root

def print_obst(root, keys, i, j, parent, is_left):
    if i > j:
        return

    root_key = root[i][j]
    if parent is None:
        print(f"Root: {keys[root_key]}")
    else:
        direction = "left" if is_left else "right"
        print(f"{keys[parent]} -> {direction}: {keys[root_key]}")

    print_obst(root, keys, i, root_key - 1, root_key, True)
    print_obst(root, keys, root_key + 1, j, root_key, False)

if __name__ == "__main__":
    keys = list(map(int, input("Enter keys (comma-separated): ").split(',')))
    freq = list(map(int, input("Enter frequencies (comma-separated): ").split(',')))

    if len(keys) != len(freq):
        print("Error: Keys and frequencies must have the same length.")
    else:
        cost, root = optimal_bst(keys, freq)
        print(f"Optimal Cost: {cost[0][len(keys) - 1]}")
        print("OBST Structure:")
        print_obst(root, keys, 0, len(keys) - 1, None, False)
