# Task 1

def alp_bt_pruning(depth, node_index, is_playerMX, values, alp, bt):
    # Base case: If the depth is the max depth (5), return the value of the leaf node
    if depth == 5:
        return values[node_index]

    if is_playerMX:
        evalMX = float('-inf')
        for i in range(2):  # Two branches
            eval = alp_bt_pruning(depth + 1, node_index * 2 + i, False, values, alp, bt)
            evalMX = max(evalMX, eval)
            alp = max(alp, eval)
            if bt <= alp:
                break  # bt cut-off
        return evalMX
    else:
        evalMN = float('inf')
        for i in range(2):  # Two branches
            eval = alp_bt_pruning(depth + 1, node_index * 2 + i, True, values, alp, bt)
            evalMN = min(evalMN, eval)
            bt = min(bt, eval)
            if bt <= alp:
                break  # alp cut-off
        return evalMN

def mortal_kombatPLAY(playerST):
    # Generate values for all 2^5 = 32 leaf nodes
    values = [-1, 1] * 16  # Alternating wins for Scorpion (-1) and Sub-Zero (1)

    rounds = []
    playerCNT = playerST
    roundsT = 0

    # Simulate rounds until one player wins
    while True:
        winner_value = alp_bt_pruning(0, 0, playerCNT == 0, values, float('-inf'), float('inf'))
        winner = "Scorpion" if winner_value == -1 else "Sub-Zero"
        rounds.append(winner)

        roundsT += 1

        # Check if there is an overall winner (best of 3)
        if rounds.count("Scorpion") == 2 or rounds.count("Sub-Zero") == 2:
            break

        # Alternate starting player for the next round
        playerCNT = 1 - playerCNT

    # Determine the overall game winner
    winR = "Scorpion" if rounds.count("Scorpion") > rounds.count("Sub-Zero") else "Sub-Zero"

    # Print
    print(f"Game Winner: {winR}")
    print(f"Total Rounds Played: {roundsT}")
    for i, winnerRnd in enumerate(rounds, 1):
        print(f"Winner of Round {i}: {winnerRnd}")


# Input: Starting player
playerST = int(input("Enter starting player (0 for Scorpion, 1 for Sub-Zero): "))
mortal_kombatPLAY(playerST)

# -------------------------------------------0----------------------------------------------------
# Task 2

def pacman_game(values, depth, is_max_player, alp, bt):
    # Base case: If depth reaches 3 (leaf nodes), return the first value
    if len(values) == 1 or depth == 3:
        return values[0]
    
    if is_max_player:
        evalMX = float('-inf')
        for i in range(2):  # Two branches
            eval = pacman_game(values[i * len(values)//2:(i + 1) * len(values)//2],
                               depth + 1, False, alp, bt)
            evalMX = max(evalMX, eval)
            alp = max(alp, eval)
            if bt <= alp:
                break  # beta cut-off
        return evalMX
    else:
        evalMN = float('inf')
        for i in range(2):  # Two branches
            eval = pacman_game(values[i * len(values)//2:(i + 1) * len(values)//2],
                               depth + 1, True, alp, bt)
            evalMN = min(evalMN, eval)
            bt = min(bt, eval)
            if bt <= alp:
                break  # alpha cut-off
        return evalMN

def pacman_gamePLAY(cost):
    # Leaf nodes for the game tree
    values = [3, 6, 2, 3, 7, 1, 2, 0]

    # Without using dark magic
    rootNoMagic = pacman_game(values, 0, True, float('-inf'), float('inf'))
    print(f"The minimax value without using dark magic: {rootNoMagic}")

    # With dark magic on both branches
    maxL = max(values[:4]) - cost  # dark magic on the left subtree is applied by pacman
    maxR = max(values[4:]) - cost  # dark magic on the right subtree is applied by pacman
    rootMagic = max(maxL, maxR)

    # Determine optimal strategy
    print(f"The minimax value with using dark magic: {rootMagic}")

    if rootMagic > rootNoMagic:
        if maxL > maxR:
            print(f"Pacman goes left and uses dark magic. New value: {maxL}")
        else:
            print(f"Pacman goes right and uses dark magic. New value: {maxR}")
    else:
        print(f"Pacman does not use dark magic. Optimal value: {rootNoMagic}")


# Input: Cost of using dark magic
cost = int(input("Enter the cost of using dark magic: "))
pacman_gamePLAY(cost)