# Advent of Code 2020 Solutions
 My hacky, time-consuming AoC 2020 solutions
 
 ## Day 18 - Regex Bootcamp
 
 I found today's problem (Day 18) really enjoyable. The task was to create a program to calculate
 mathematical equations based on different rules of precedence - first from left-to-right (ignoring
 traditional operator precedence) and then for the second task, with addition > multiplication.
 
 I recreated the built-in eval() function in two very different ways. It took me quite a while to figure
 out the correct Regex pattern to grab the bracketed expressions, but then realised you could just repeat
 the same pattern in a loop, like a two-pass assembler sort of system. Fun!
