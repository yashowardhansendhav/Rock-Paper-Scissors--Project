# System Architecture

```text
                 USER
                  |
                  v
              main.py
                  |
        +---------+---------+
        |         |         |
        v         v         v
     game.py  difficulty.py validation.py
        |         |         |
        +---------+---------+
                  |
          +-------+-------+
          |               |
          v               v
      score.py       history.py
          |               |
          +-------+-------+
                  |
                  v
              GAME RESULT