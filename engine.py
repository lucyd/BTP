# Game Simulation Engine
# Arguments : GlobalVars, Constraints, Methods, Definitions, Declarations

import sys

if len(sys.argv) != 6:
  print'Incorrect usage: %s globalvars definitions methods declarations constraints' %(sys.argv[0])
  sys.exit(1)

constraint_delimitor = '==>'	
game = ''
while len(game.strip()) == 0:
  print 'Enter game name: ',
  game = raw_input()
  
global_vars_file = open(sys.argv[1], 'r')
definitions_file = open(sys.argv[2], 'r')
methods_file = open(sys.argv[3], 'r')
declarations_file = open(sys.argv[4], 'r')
constraints_file = open(sys.argv[5], 'r')
game_file = open(game + '.py', 'w')

game_file.write('Game: ' + game + '\n\n')
game_file.write('# Global Variables\n' + global_vars_file.read() + '\n\n')
game_file.write('# Object Definitions\n' + definitions_file.read() + '\n\n')
game_file.write('# Methods\n' + methods_file.read() + '\n\n')
game_file.write('# Object Declarations\n' + declarations_file.read() + '\n\n')
game_file.write('# Infinite game loop\nwhile True:\n')
constraints = [ x[:-1] for x in constraints_file.readlines() ]
for constraint in constraints:
  [condition, callback] = constraint.split(constraint_delimitor)
  game_file.write('  if ' + condition + ':\n' + '    ' + callback + '\n')

