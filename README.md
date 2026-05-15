# 🧩 Maze Algorithm Learner

> A **gamified, interactive maze visualizer** built with Python and Pygame that challenges players to identify which pathfinding algorithm is being used — BFS, DFS, Dijkstra, or Greedy Best-First Search.

---

## 📖 Project Overview

**Maze Algorithm Learner** is a quiz-style educational game developed for the Design and Analysis of Algorithms (DAA) course. A randomly generated maze is displayed on screen, and one of four pathfinding algorithms silently solves it — animating the traversal step by step. The player must correctly identify which algorithm is solving the maze.

The game rewards correct answers with points and builds streaks for consecutive correct guesses, reinforcing understanding of how each algorithm explores a search space.

---

## 👥 Team Members

| Full Name | Student ID | Contribution | Main Role |
|---|---|---|---|
| Brave Juliada | 5025241140 | 33.33% | UI design and algorithm implementation |
| Indra Wahyu Tirtayasa | 5025241108 | 33.33% | Maze logic, game loop, and integration |
| Raymond Julius Pardosi | 5025241268 | 33.33% | Evaluation, testing, and report writing |

---

## 🎯 Learning Objectives

| Algorithm | Characteristic Visualized |
|---|---|
| **BFS** | Explores level by level (shortest path, uniform spread) |
| **DFS** | Dives deep first, backtracks (non-uniform, deep paths) |
| **Dijkstra** | Considers movement cost (avoids mud tiles, cost-aware) |
| **Greedy Best-First** | Rushes toward the goal using Manhattan distance heuristic |

---

## 🚀 Features

- 🗺️ **Randomly generated maze** with walls, floors, and mud tiles (mud costs more to traverse)
- 🎬 **Step-by-step animated traversal** of the solving algorithm
- 🕹️ **Interactive quiz** — guess which algorithm is running
- 🔁 **Replay button** to re-watch the current animation
- 🏆 **Score & streak system** with bonus points for consecutive correct answers
- 🖼️ **Tileset rendering** using a sprite sheet (`stone_to_void.png`)

---

## 🧠 Algorithms Implemented

### 1. Breadth-First Search (BFS)
Explores the maze **level by level** using a queue (FIFO). Guarantees the **shortest path** in terms of number of steps on unweighted graphs.

```
Complexity: O(V + E)
Data Structure: Queue (deque)
Characteristic: Wide, even spread across the grid
```

### 2. Depth-First Search (DFS)
Explores the maze by going **as deep as possible** before backtracking, using a stack (LIFO). Does **not** guarantee the shortest path.

```
Complexity: O(V + E)
Data Structure: Stack
Characteristic: Long, winding, aggressive exploration
```

### 3. Dijkstra's Algorithm
Explores nodes in order of **accumulated movement cost**, using a min-heap priority queue. Accounts for tile cost differences (mud = cost 5, floor = cost 1).

```
Complexity: O((V + E) log V)
Data Structure: Min-Heap (heapq)
Characteristic: Cost-aware, avoids mud tiles
```

### 4. Greedy Best-First Search
Uses **Manhattan distance** as a heuristic to always expand the node that looks closest to the goal. Fast, but not guaranteed to find the optimal path.

```
Complexity: O(b^m) in worst case
Data Structure: Min-Heap (heapq) with heuristic priority
Characteristic: Rushes toward the goal, ignores past cost
```

---

## 🏗️ Project Structure

```
DAA-Quiz2-DFS-BFS_Learner/
│
├── main.py           # Game loop, event handling, quiz logic, score/streak
├── maze.py           # Maze generation, tile rendering, walkability checks
├── solver.py         # BFS, DFS, Dijkstra, Greedy implementations
├── ui.py             # Button layout and HUD rendering (score, streak, message)
├── stone_to_void.png # Sprite sheet tileset for wall/floor/mud tiles
└── README.md
```

### Module Responsibilities

| File | Responsibility |
|---|---|
| `main.py` | Game entry point; manages game state, quiz logic, animation timing |
| `maze.py` | Grid generation (with solvability check), tile drawing, cost map |
| `solver.py` | Pure algorithm implementations that return traversal step sequences |
| `ui.py` | Pygame UI components — buttons (BFS, DFS, Dijkstra, Greedy, Replay) and HUD |

---

## 🎮 How to Play

1. **Watch the animation** — observe how the algorithm explores the maze from **S** (Start) to **E** (End)
2. **Identify the algorithm** based on its traversal pattern:
   - Wide, even spread → BFS
   - Deep, winding path → DFS
   - Avoids mud, cost-aware → Dijkstra
   - Rushes straight toward goal → Greedy
3. **Click the correct button** — BFS, DFS, Dijkstra, or Greedy
4. **Build your streak** — consecutive correct answers give bonus points!
5. Use **Replay** to re-watch the animation before guessing

### Scoring System

| Action | Points |
|---|---|
| Correct answer | 100 + (streak × 20) |
| Wrong answer | 0 (streak reset) |

---

## 🔧 Requirements & Setup

### Prerequisites

- Python 3.8+
- Pygame

### Installation

```bash
# Clone the repository
git clone https://github.com/Brave110705/DAA-Quiz2-DFS-BFS_Learner.git
cd DAA-Quiz2-DFS-BFS_Learner

# Install dependencies
pip install pygame

# Run the game
python main.py
```

---

## 🗺️ Maze Details

| Property | Value |
|---|---|
| Grid Size | 10 × 10 |
| Wall Probability | 25% |
| Mud Probability | 15% |
| Floor Probability | 60% |
| Start | Top-left (0, 0) |
| End | Bottom-right (9, 9) |
| Mud Movement Cost | 5 |
| Floor Movement Cost | 1 |

The maze generator guarantees a valid path exists from **S** to **E** before presenting it to the player (up to 100 regeneration attempts, with a guaranteed fallback corridor).

---

## 📊 Algorithm Comparison

| Algorithm | Guarantees Shortest Path | Considers Tile Cost | Speed (typical) |
|---|---|---|---|
| BFS | ✅ (unweighted) | ❌ | Moderate |
| DFS | ❌ | ❌ | Fast |
| Dijkstra | ✅ (weighted) | ✅ | Slower |
| Greedy | ❌ | ❌ | Fastest |

---

## 🎓 Course Context

**Course:** Design and Analysis of Algorithms (DAA)  
**Assignment:** Quiz 2 — Group Project  
**Requirement:** Implement at least one algorithm from the course (DFS, BFS, Dijkstra, etc.)

This project implements **four** graph traversal / pathfinding algorithms and presents them in an interactive educational game format that helps students intuitively understand the behavioral differences between each approach.

---

## 📚 References

- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.
- Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson.
- [Pygame Documentation](https://www.pygame.org/docs/)
- [Python heapq — Heap queue algorithm](https://docs.python.org/3/library/heapq.html)
- [Python collections.deque](https://docs.python.org/3/library/collections.html#collections.deque)
