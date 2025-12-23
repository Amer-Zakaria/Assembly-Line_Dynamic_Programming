# Assembly Line Scheduling Problem

## Problem Description

The Assembly Line Scheduling problem is a classic dynamic programming optimization problem where we need to find the minimum time to complete production through two parallel assembly lines. Here's a visual representation of the problem: Line_assembly_visulization.png
(Parllel stations do the same thing)

### Problem Setup

- **Two parallel assembly lines**, each with **n stations**
- Each station **S<sub>i,j</sub>** (line i, station j) has a processing time **a<sub>i,j</sub>**
- **Entry times**: e₁ and e₂ (time to enter each line)
- **Exit times**: x₁ and x₂ (time to exit each line)
- **Transfer costs**: t<sub>i,j</sub> (cost to switch from line i to the other line after station j)

### Goal

Find the **minimum total time** to complete assembly and the **optimal path** through the stations.

### Constraints

- You must start at station 1 and proceed sequentially through all n stations
- At each station, you can either:
  - Continue on the same line (no transfer cost)
  - Switch to the other line (incurs transfer cost)
- You can only transfer between lines after completing a station

### Visual Example

![Assembly Line Diagram](Line_assembly_visulization.png)

In the diagram above:

- Blue circles represent stations with their processing times
- Pink circles represent transfer costs
- Green circles represent entry and exit times
- Numbers on edges show the costs/times

For this example:

- Line 1: a₁ = [7, 9, 3, 4, 8], e₁ = 2, x₁ = 3
- Line 2: a₂ = [8, 5, 6, 4, 5], e₂ = 4, x₂ = 6
- Transfer from line 1→2: t₁ = [2, 3, 1, 3]
- Transfer from line 2→1: t₂ = [2, 1, 2, 2]

**Optimal solution**: Time = 35, Path = [Line 1 → Line 2 → Line 1 → Line 1 → Line 1]

---

## Usage

Run the test suite:

```bash
python main.py
```

This will execute multiple test cases demonstrating different scenarios.
