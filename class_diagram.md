# Class / Component Diagram

```text
+----------------------+
|       main.py        |
|----------------------|
| Main game flow       |
| User input           |
| Round control        |
+----------+-----------+
           |
     +-----+-----+----------------+
     |           |                |
     v           v                v
+---------+ +------------+ +-------------+
| game.py | |difficulty.py| |validation.py|
|---------| |------------| |-------------|
| Winner  | | Difficulty | | Input check |
| logic   | | logic      | |             |
+---------+ +------------+ +-------------+
     |
     +------------------+
     |                  |
     v                  v
+---------+        +-----------+
|score.py |        |history.py |
|---------|        |-----------|
| Score   |        | Game      |
| tracking|        | history   |
+---------+        +-----------+

          config.py
              |
              v
       Game choices and
       difficulty levels