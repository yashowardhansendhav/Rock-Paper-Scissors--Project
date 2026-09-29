# Testing

The Rock Paper Scissors game was tested using different inputs and game conditions.

## Test Cases

| Test | Input / Condition | Expected Result |
|---|---|---|
| 1 | Player enters rock | Game accepts the choice |
| 2 | Player enters paper | Game accepts the choice |
| 3 | Player enters scissors | Game accepts the choice |
| 4 | Player enters an invalid choice | Program asks for the choice again |
| 5 | Player and computer choose the same option | Result is draw |
| 6 | Player wins a round | Wins score increases |
| 7 | Computer wins a round | Losses score increases |
| 8 | Multiple rounds are played | Score and history are updated |
| 9 | Easy difficulty is selected | Computer makes a choice |
| 10 | Medium difficulty is selected | Computer uses medium difficulty logic |
| 11 | Hard difficulty is selected | Computer uses hard difficulty logic |

## Validation

The program checks the player's input before continuing the round. If the input is not rock, paper or scissors, the player is asked to enter a valid choice again.

## Result

The game was run through Command Prompt to check that the different modules work together and that the game produces the expected output.