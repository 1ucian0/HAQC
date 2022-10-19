# Feasible solutions for 3 node flat
FEASIBLE_SOLUTIONS = [
    [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0],  # 1 -> 2 -> 3
    [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0],  # 1 -> 3 -> 2
    [0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0],  # 2 -> 1 -> 3
    [0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0],  # 2 -> 3 -> 1
    [0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0],  # 3 -> 1 -> 2
    [0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0],  # 3 -> 2 -> 1
]
