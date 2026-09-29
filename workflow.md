# Game Workflow

```text
START
  |
  v
Choose Difficulty
  |
  v
Enter Number of Rounds
  |
  v
Enter Player Choice
  |
  v
Is the choice valid?
  |
  +---- NO ----> Ask for choice again
  |
 YES
  |
  v
Computer selects choice
  |
  v
Determine Winner
  |
  v
Update Score
  |
  v
Save Round in History
  |
  v
More rounds?
  |
  +---- YES ----> Next Round
  |
  NO
  |
  v
Display Final Score
  |
  v
Display Game History
  |
  v
END
