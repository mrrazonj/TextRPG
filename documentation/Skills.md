Battle System
======
Every character can learn a finite amount of skills, and equip a maximum of 5 `techniques` and 3 `magic` to be used in an encounter.


Each turn in battle, you are given `Action Points(AP)`. 
The amount of `AP` given is determined by your chosen job, and is supplemented by your `DEX` attribute.
You use these points to perform actions with the goal of defeating the enemy, and surviving the encounter.
Once you run out of `AP`, the turn ends.
Certain skills can also be used to prematurely end the turn, hence conserving your remaining `AP` to be used the next turn.

Each action in this game does varying effects and costs differently depending on what order you used them.
The first action you use in your turn is considered an `Opening Move`,
the second action after that is then a `Follow-up Move`,
and finally the third action is the `Finishing Move`

After using a `Finishing Move`, the next action will start over to be an `Opening Move`, repeating the cycle.

A word of warning, if you end a turn with negative AP, you will incur penalties for the following turn 
aside from the reduced AP allowance.

Legend
======
#### Skill Name
```
1. Opening Move
2. Follow-up Move
3. Finishing Move
```

Techniques
======

Common Techniques
------
#### Normal Attack (Lv 1)
```
1. Deals 75% attack damage, costs no AP
2. Deals 95% attack damage, costs 1 AP
3. Deals 120% attack damage, costs 2 AP
```
#### Bide (Lv 1)
```
1. Ends turn, saving remaining AP for next turn (+4 bonus AP)
2. Ends turn, saving remaining AP for next turn (+2 bonus AP)
3. Ends turn, saving remaining AP for next turn (No bonus AP)
```
Warrior Techniques
------
#### Bash (Lv 1-10)
```
1. Deals 80% attack damage, reduces enemy defense by 25-40% for the current turn, costs 1 AP
2. Deals 125% attack damage, reduces enemy AP by 1 for every 80 damage dealt, costs 2 AP
3. Deals 150% attack damage, 2% + [STR * 0.20] chance to nullify enemy AP income for its following turn, costs 4 AP
```
#### Rush (Lv 11-20)
```
1. Deals 50% attack damage 2x, 30% + [DEX] chance to attack for a third time for 75% attack damage, costs 1 AP
2. Deals 70% attack damage 2x, 45% + [DEX] chance to attack for a third time for 75% attack damage
   and another 20% + [DEX] chance to attack for a fourth time for 80% attack damage, costs 3 AP
3. Deals absolute 90% attack damage 4x, costs 5 AP
```
#### Execute (Lv 21-30)
```
1. Deals 120% attack damage, and 30% (half for bosses) of enemy missing HP as absolute damage, costs 3 AP, ends turn
2. Deals 180% attack damage, and 50% (half for bosses) of enemy missing HP as absolute damage, costs 6 AP, ends turn
3. Deals 240% attack damage, and 100% (half for bosses) of enemy missing HP as absolute damage, costs 10 AP, ends turn

Note: Damage is dealt first before computing for missing health damage
```
#### Reckless Onslaught Lv(31-40)
```
1. Deals 200% attack damage to enemy and absolute half to self, empowers Follow-up Move damage by 50%, costs 2 AP
2. Deals 350% attack damage to enemy and absolute half to self, empowers Finishing Move damage by 100%, costs 5 AP
3. Deals 500% attack damage to enemy and absolute half to self, increase all damage dealt by 100% until end of
   encounter, costs 8 AP
   
Note 1: You can't die from the self damage.
Note 2: Doesn't increase missing health damage from skills.
```
#### Chaotic Drive Lv(40)
```
1. Deals 300% absolute attack damage, 10% + [STR * 0.125 + DEX * 0.1] chance to nullify enemy defense
   for the entire encounter, costs 4 AP and 30% of maximum health
2. Deals 500% absolute attack damage, 10% + [STR * 0.125 + DEX * 0.1] chance to halve enemy attack
   for the entire encounter, costs 4 AP and 50% of maximum health
3. Deals 700% absolute attack damage, 5% + [STR * 0.15 + DEX * 0.15] chance to instantly kill enemy,
   costs 6 AP and 80% of maximum health
   
Note: Bosses can't be instantly killed, but they will instead be dealt an additional 400% damage,
      and nullifying their AP income for 2 turns