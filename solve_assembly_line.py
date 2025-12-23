def solve_assembly_line(a1, a2, t1, t2, e1, e2, x1, x2):
    """
    Plan: Assembly Line Scheduling via Dynamic Programming

    1. PRE-PROCESSING:
       Integrate entry (e) and exit (x) times into the first and last stations.
       That would simplify the problem.
       a1[0] = e1 + a1[0], a1[n] = a1[n] + x1 (likewise for line 2)

    2. FORWARD PASS (DP):
       Compute the minimum time to reach each station S[line, station].
       S1[i] = min(S1[i-1] + a1[i], S2[i-1] + t2[i-1] + a1[i])
       S2[i] = min(S2[i-1] + a2[i], S1[i-1] + t1[i-1] + a2[i])

       Logic breakdown for S1[i]:
       - Option A (Stay): S1[i-1] + a1[i]
       - Option B (Switch): S2[i-1] + t2[i-1] (transfer cost) + a1[i]

    3. PATH RECONSTRUCTION (Backtracking):
       Start from the end and work backwards to find which decisions were made.

       A. Determine final line (L_final):
          if S1[n] <= S2[n]: L_final = 1 else: L_final = 2

       B. Trace back from station i = n down to 1:
          If current_line is 1:
             Check if we stayed: is S1[i] == S1[i-1] + a1[i]?
             - Yes: previous_line = 1
             - No:  previous_line = 2 (must have switched from line 2)
          If current_line is 2:
             Check if we stayed: is S2[i] == S2[i-1] + a2[i]?
             - Yes: previous_line = 2
             - No:  previous_line = 1 (must have switched from line 1)

    4. FINAL OUTPUT:
       Return (min_time, reconstructed_path)
    """

    # 1. PRE-PROCESSING:
    n = len(a1)  # assembly line stations length
    a1[0], a2[0] = a1[0] + e1, a2[0] + e2
    a1[n - 1], a2[n - 1] = a1[n - 1] + x1, a2[n - 1] + x2

    # FORWARD PASS (DP):
    S1 = [0] * n  # Minimum time out of the 1st line for each station
    S2 = [0] * n  # Minimum time out of the 2nd line for each station

    S1[0] = a1[0]
    S2[0] = a2[0]
    for i in range(1, n):
        S1[i] = min(S1[i - 1] + a1[i], S2[i - 1] + t2[i - 1] + a1[i])
        S2[i] = min(S2[i - 1] + a2[i], S1[i - 1] + t1[i - 1] + a2[i])

    print(S1, S2)

    # 3. PATH RECONSTRUCTION (Backtracking):
    min_time = float("inf")
    path = [0] * n

    path[n - 1] = 1 if S1[n - 1] <= S2[n - 1] else 2

    for i in reversed(range(1, n)):  # n, n-1, ..., 1
        if path[i] == 1:
            path[i - 1] = 1 if (S1[i] == (S1[i - 1] + a1[i])) else 2
        else:
            path[i - 1] = 2 if (S2[i] == (S2[i - 1] + a2[i])) else 1

    # 4. FINAL OUTPUT:
    min_time = S1[n - 1] if path[n - 1] == 1 else S2[n - 1]
    return min_time, path


def print_solution(min_time, path, test_name):
    """Helper function to print solution nicely"""
    print(f"\n{test_name}")
    print("=" * len(test_name))
    print(f"Minimum Time: {min_time}")
    print(f"Optimal Path: {' -> '.join([f'Line {line}' for line in path])}")
    print(
        f"Station Path: {' -> '.join([f'S{path[i]},{i+1}' for i in range(len(path))])}"
    )
