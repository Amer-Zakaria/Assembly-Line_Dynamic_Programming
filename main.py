"""
Assembly Line Scheduling - Test Suite
=====================================

This test suite demonstrates the Dynamic Programming solution to the
Assembly Line Scheduling problem with various test cases.
"""

from solve_assembly_line import solve_assembly_line


def print_solution(min_time, path, test_name):
    """Helper function to print solution nicely"""
    print(f"\n{test_name}")
    print("=" * len(test_name))
    print(f"Minimum Time: {min_time}")
    print(f"Optimal Path: {' -> '.join([f'Line {line}' for line in path])}")
    print(
        f"Station Path: {' -> '.join([f'S{path[i]},{i+1}' for i in range(len(path))])}"
    )


def test_assembly_line():
    print("🏭 Assembly Line Scheduling - Test Suite")
    print("=" * 50)

    # Test Case 2: Simple case - stay on one line
    print("\n🧪 Test Case 1: Simple Case - Stay on One Line")
    a1 = [4, 5, 3]
    a2 = [10, 6, 2]
    t1 = [2, 3]
    t2 = [1, 1]
    e1, e2 = 1, 2
    x1, x2 = 1, 1

    min_time, path = solve_assembly_line(a1, a2, t1, t2, e1, e2, x1, x2)
    print_solution(min_time, path, "Expected: Time=14, Path=[1,1,1]")

    # Test Case 3: Single station
    print("\n🧪 Test Case 2: Single Station")
    a1 = [5]
    a2 = [3]
    t1, t2 = [], []
    e1, e2 = 2, 1
    x1, x2 = 1, 2

    min_time, path = solve_assembly_line(a1, a2, t1, t2, e1, e2, x1, x2)
    print_solution(min_time, path, "Expected: Time=6, Path=[2]")

    # Test Case 4: Transfer beneficial
    print("\n🧪 Test Case 3: Transfer is Beneficial")
    a1 = [2, 10]
    a2 = [5, 3]
    t1 = [1]  # cheap transfer from line 1 to line 2
    t2 = [5]  # expensive transfer from line 2 to line 1
    e1, e2 = 1, 1
    x1, x2 = 1, 1

    min_time, path = solve_assembly_line(a1, a2, t1, t2, e1, e2, x1, x2)
    print_solution(min_time, path, "Expected: Time=8, Path=[1,2]")

    # Test Case 1: Example from the diagram
    print("\n🧪 Test Case 4: Diagram Example")
    a1 = [7, 9, 3, 4, 8]
    a2 = [8, 5, 6, 4, 5]
    t1 = [2, 3, 1, 3]  # transfer from line 1 to line 2
    t2 = [2, 1, 2, 2]  # transfer from line 2 to line 1
    e1, e2 = 2, 4
    x1, x2 = 3, 6

    min_time, path = solve_assembly_line(a1, a2, t1, t2, e1, e2, x1, x2)
    print_solution(min_time, path, "Expected: Time=35, Path=[1,2,1,1,1]")

    # Test Case 0: Counter-intuitive path example
    print("\n🧪 Test Case 5: Counter-intuitive Path Example")
    print("This case demonstrates that the optimal path is NOT found by greedily")
    print("choosing the faster line at each station. Instead, we must consider")
    print("the global optimal path through backtracking.")
    print()
    print(
        "At station 4, Line 1 is faster (S1=[9, 18, 20, [24], 32]) than Line 2 (S2=[12, 16, 22, [25], 30])"
    )
    print("yet the optimal path goes through Line 2 at station 4 because it")
    print("enables a better outcome at subsequent stations. This shows why we need")
    print("dynamic programming with backtracking.")

    a1 = [7, 9, 3, 4, 8]
    a2 = [8, 5, 6, 4, 5]
    t1 = [2, 3, 1, 10]  # transfer from line 1 to line 2 (expensive at station 4)
    t2 = [2, 1, 2, 0]  # transfer from line 2 to line 1 (free at station 4)
    e1, e2 = 2, 4
    x1, x2 = 0, 0

    min_time, path = solve_assembly_line(a1, a2, t1, t2, e1, e2, x1, x2)
    print_solution(min_time, path, "Expected: Time=30, Path=[1,2,1,2,2]")


if __name__ == "__main__":
    test_assembly_line()
