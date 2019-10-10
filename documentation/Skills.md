Battle System
======
Each turn in battle, you are given `Action Points(AP)`. The amount of `(AP)` given is determined by your chosen job, and is supplemented by your `[DEX]` attribute. You use these points to perform actions with the goal of defeating the enemy, and surviving the encounter. Once you run out of `(AP)`, the turn ends. Certain `"Skills"` can also be used to prematurely end the turn, hence conserving your remaining `(AP)` to be used the next turn.

Each action in this game does varying effects and costs differently depending on what order you used them. The first action you use in your turn is considered an `"Opening Move"`, the second action after that is then a `"Follow-up Move"`, and finally the third action is the `"Finishing Move"`

After using a `"Finishing Move"`, the next action will start over to be an `"Opening Move"`, repeating the cycle.

Legend
======
Skill Name
------
Opening Move
Follow-up Move
Finishing Move

***
***

Common
------
#### Normal Attack
```python
#Deals 75% attack damage, costs no AP
#Deals 95% attack damage, costs 1 AP
#Deals 120% attack damage, costs 2 AP
```
#### Bide
```python
#Ends turn, saving remaining AP for next turn (+4 bonus AP)
#Ends turn, saving remaining AP for next turn (+2 bonus AP)
#Ends turn, saving remaining AP for next turn (No bonus AP)
```
Warrior
------
#### Bash
#Deals 80% of attack damage, reduces enemy defense by 25-50%, costs 2 AP
#Deals 