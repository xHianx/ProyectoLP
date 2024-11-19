
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEleftANDORrightNOTALIAS AND ARRAY ASSIGNATION BEGIN BIGGER BIGGEREQUAL BREAK CASE CLASS COLON COMMA DECREMENT DEF DEFINED DIVIDE DO ELSE ELSIF END ENSURE EQUAL FALSE FLOAT FOR GETS HASH IF IN INCREMENT INTEGER LBRACE LBRACKET LPAREN MINUS MODULE MULTI_LINE_COMMENT NEXT NIL NOT NOTEQUAL OR PLUS POWER PUTS RBRACE RBRACKET REDO RESCUE RETRY RETURN RPAREN SELF SEMICOLON SINGLE_LINE_COMMENT SMALLER SMALLEREQUAL STRING SUPER TIMES TRUE UNLESS UNTIL VARIABLE_CLASE VARIABLE_GLOBAL VARIABLE_INSTANCIA VARIABLE_LOCAL WHEN WHILE YIELDprogram : statement_liststatement_list : statement\n                     | statement statement_liststatement : function_def\n                | assignment\n                | if_statement\n                | while_statement\n                | puts_statement\n                | gets_statement\n                | expressionvariable : VARIABLE_LOCAL\n                | VARIABLE_GLOBAL\n                | VARIABLE_INSTANCIA\n                | VARIABLE_CLASEfunction_def : DEF VARIABLE_LOCAL LPAREN param_list RPAREN expression ENDparam_list : VARIABLE_LOCAL COMMA VARIABLE_LOCAL\n                 | VARIABLE_LOCAL\n                 | emptyassignment : variable ASSIGNATION expressionwhile_statement : WHILE expression DO statement_list ENDif_statement : IF expression statement_list ENDputs_statement : PUTS arg_listgets_statement : VARIABLE_LOCAL ASSIGNATION GETSexpression : expression AND expression\n                  | expression OR expression\n                  | NOT expressionexpression : INTEGER\n                 | STRING\n                 | variable\n                 | array\n                 | array_access\n                 | function_call\n                 | binary_operation\n                 | GETS\n                 | hasharray : LBRACKET array_elements RBRACKETarray_elements : INTEGER\n                     | INTEGER COMMA array_elementsarray_access : VARIABLE_LOCAL LBRACKET INTEGER RBRACKEThash : LBRACE hash_elements RBRACEhash_elements : hash_element\n                     | hash_element COMMA hash_elements\n                     | emptyhash_element : VARIABLE_LOCAL COLON STRINGfunction_call : VARIABLE_LOCAL LPAREN arg_list RPARENarg_list : expression\n                | expression COMMA arg_list\n                | emptybinary_operation : expression TIMES expression\n                       | expression BIGGER expressionempty :'
    
_lr_action_items = {'DEF':([0,3,4,5,6,7,8,9,10,12,13,16,17,19,20,21,22,23,24,25,26,27,28,41,42,43,45,46,47,48,55,56,57,58,60,63,65,66,67,69,75,76,77,79,85,88,],[11,11,-4,-5,-6,-7,-8,-9,-10,-11,-29,-51,-34,-27,-28,-30,-31,-32,-33,-35,-12,-13,-14,11,-29,-11,-22,-46,-48,-26,-24,-25,-49,-50,-23,-19,11,-51,-36,-40,-39,-45,-21,-47,-20,-15,]),'IF':([0,3,4,5,6,7,8,9,10,12,13,16,17,19,20,21,22,23,24,25,26,27,28,41,42,43,45,46,47,48,55,56,57,58,60,63,65,66,67,69,75,76,77,79,85,88,],[14,14,-4,-5,-6,-7,-8,-9,-10,-11,-29,-51,-34,-27,-28,-30,-31,-32,-33,-35,-12,-13,-14,14,-29,-11,-22,-46,-48,-26,-24,-25,-49,-50,-23,-19,14,-51,-36,-40,-39,-45,-21,-47,-20,-15,]),'WHILE':([0,3,4,5,6,7,8,9,10,12,13,16,17,19,20,21,22,23,24,25,26,27,28,41,42,43,45,46,47,48,55,56,57,58,60,63,65,66,67,69,75,76,77,79,85,88,],[15,15,-4,-5,-6,-7,-8,-9,-10,-11,-29,-51,-34,-27,-28,-30,-31,-32,-33,-35,-12,-13,-14,15,-29,-11,-22,-46,-48,-26,-24,-25,-49,-50,-23,-19,15,-51,-36,-40,-39,-45,-21,-47,-20,-15,]),'PUTS':([0,3,4,5,6,7,8,9,10,12,13,16,17,19,20,21,22,23,24,25,26,27,28,41,42,43,45,46,47,48,55,56,57,58,60,63,65,66,67,69,75,76,77,79,85,88,],[16,16,-4,-5,-6,-7,-8,-9,-10,-11,-29,-51,-34,-27,-28,-30,-31,-32,-33,-35,-12,-13,-14,16,-29,-11,-22,-46,-48,-26,-24,-25,-49,-50,-23,-19,16,-51,-36,-40,-39,-45,-21,-47,-20,-15,]),'VARIABLE_LOCAL':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,32,33,34,35,39,40,41,42,43,45,46,47,48,55,56,57,58,59,60,63,65,66,67,69,70,75,76,77,79,83,84,85,88,],[12,12,-4,-5,-6,-7,-8,-9,-10,36,-11,-29,43,43,43,-34,43,-27,-28,-30,-31,-32,-33,-35,-12,-13,-14,54,43,43,43,43,43,43,12,-29,-11,-22,-46,-48,-26,-24,-25,-49,-50,72,-23,-19,12,43,-36,-40,54,-39,-45,-21,-47,86,43,-20,-15,]),'NOT':([0,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,32,33,34,35,39,40,41,42,43,45,46,47,48,55,56,57,58,60,63,65,66,67,69,75,76,77,79,84,85,88,],[18,18,-4,-5,-6,-7,-8,-9,-10,-11,-29,18,18,18,-34,18,-27,-28,-30,-31,-32,-33,-35,-12,-13,-14,18,18,18,18,18,18,18,-29,-11,-22,-46,-48,-26,-24,-25,-49,-50,-23,-19,18,18,-36,-40,-39,-45,-21,-47,18,-20,-15,]),'INTEGER':([0,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,32,33,34,35,38,39,40,41,42,43,45,46,47,48,55,56,57,58,60,63,65,66,67,68,69,75,76,77,79,84,85,88,],[19,19,-4,-5,-6,-7,-8,-9,-10,-11,-29,19,19,19,-34,19,-27,-28,-30,-31,-32,-33,-35,-12,-13,-14,50,19,19,19,19,61,19,19,19,-29,-11,-22,-46,-48,-26,-24,-25,-49,-50,-23,-19,19,19,-36,50,-40,-39,-45,-21,-47,19,-20,-15,]),'STRING':([0,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,32,33,34,35,39,40,41,42,43,45,46,47,48,55,56,57,58,60,63,65,66,67,69,71,75,76,77,79,84,85,88,],[20,20,-4,-5,-6,-7,-8,-9,-10,-11,-29,20,20,20,-34,20,-27,-28,-30,-31,-32,-33,-35,-12,-13,-14,20,20,20,20,20,20,20,-29,-11,-22,-46,-48,-26,-24,-25,-49,-50,-23,-19,20,20,-36,-40,82,-39,-45,-21,-47,20,-20,-15,]),'GETS':([0,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,32,33,34,35,37,39,40,41,42,43,45,46,47,48,55,56,57,58,60,63,65,66,67,69,75,76,77,79,84,85,88,],[17,17,-4,-5,-6,-7,-8,-9,-10,-11,-29,17,17,17,-34,17,-27,-28,-30,-31,-32,-33,-35,-12,-13,-14,17,17,17,17,60,17,17,17,-29,-11,-22,-46,-48,-26,-24,-25,-49,-50,-23,-19,17,17,-36,-40,-39,-45,-21,-47,17,-20,-15,]),'VARIABLE_GLOBAL':([0,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,32,33,34,35,39,40,41,42,43,45,46,47,48,55,56,57,58,60,63,65,66,67,69,75,76,77,79,84,85,88,],[26,26,-4,-5,-6,-7,-8,-9,-10,-11,-29,26,26,26,-34,26,-27,-28,-30,-31,-32,-33,-35,-12,-13,-14,26,26,26,26,26,26,26,-29,-11,-22,-46,-48,-26,-24,-25,-49,-50,-23,-19,26,26,-36,-40,-39,-45,-21,-47,26,-20,-15,]),'VARIABLE_INSTANCIA':([0,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,32,33,34,35,39,40,41,42,43,45,46,47,48,55,56,57,58,60,63,65,66,67,69,75,76,77,79,84,85,88,],[27,27,-4,-5,-6,-7,-8,-9,-10,-11,-29,27,27,27,-34,27,-27,-28,-30,-31,-32,-33,-35,-12,-13,-14,27,27,27,27,27,27,27,-29,-11,-22,-46,-48,-26,-24,-25,-49,-50,-23,-19,27,27,-36,-40,-39,-45,-21,-47,27,-20,-15,]),'VARIABLE_CLASE':([0,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,32,33,34,35,39,40,41,42,43,45,46,47,48,55,56,57,58,60,63,65,66,67,69,75,76,77,79,84,85,88,],[28,28,-4,-5,-6,-7,-8,-9,-10,-11,-29,28,28,28,-34,28,-27,-28,-30,-31,-32,-33,-35,-12,-13,-14,28,28,28,28,28,28,28,-29,-11,-22,-46,-48,-26,-24,-25,-49,-50,-23,-19,28,28,-36,-40,-39,-45,-21,-47,28,-20,-15,]),'LBRACKET':([0,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,32,33,34,35,39,40,41,42,43,45,46,47,48,55,56,57,58,60,63,65,66,67,69,75,76,77,79,84,85,88,],[29,29,-4,-5,-6,-7,-8,-9,-10,38,-29,29,29,29,-34,29,-27,-28,-30,-31,-32,-33,-35,-12,-13,-14,29,29,29,29,29,29,29,-29,38,-22,-46,-48,-26,-24,-25,-49,-50,-23,-19,29,29,-36,-40,-39,-45,-21,-47,29,-20,-15,]),'LBRACE':([0,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,32,33,34,35,39,40,41,42,43,45,46,47,48,55,56,57,58,60,63,65,66,67,69,75,76,77,79,84,85,88,],[30,30,-4,-5,-6,-7,-8,-9,-10,-11,-29,30,30,30,-34,30,-27,-28,-30,-31,-32,-33,-35,-12,-13,-14,30,30,30,30,30,30,30,-29,-11,-22,-46,-48,-26,-24,-25,-49,-50,-23,-19,30,30,-36,-40,-39,-45,-21,-47,30,-20,-15,]),'$end':([1,2,3,4,5,6,7,8,9,10,12,13,16,17,19,20,21,22,23,24,25,26,27,28,31,42,43,45,46,47,48,55,56,57,58,60,63,66,67,69,75,76,77,79,85,88,],[0,-1,-2,-4,-5,-6,-7,-8,-9,-10,-11,-29,-51,-34,-27,-28,-30,-31,-32,-33,-35,-12,-13,-14,-3,-29,-11,-22,-46,-48,-26,-24,-25,-49,-50,-23,-19,-51,-36,-40,-39,-45,-21,-47,-20,-15,]),'END':([3,4,5,6,7,8,9,10,12,13,16,17,19,20,21,22,23,24,25,26,27,28,31,42,43,45,46,47,48,55,56,57,58,60,63,64,66,67,69,75,76,77,78,79,85,87,88,],[-2,-4,-5,-6,-7,-8,-9,-10,-11,-29,-51,-34,-27,-28,-30,-31,-32,-33,-35,-12,-13,-14,-3,-29,-11,-22,-46,-48,-26,-24,-25,-49,-50,-23,-19,77,-51,-36,-40,-39,-45,-21,85,-47,-20,88,-15,]),'AND':([10,12,13,17,19,20,21,22,23,24,25,26,27,28,41,42,43,44,46,48,55,56,57,58,63,67,69,75,76,87,],[32,-11,-29,-34,-27,-28,-30,-31,-32,-33,-35,-12,-13,-14,32,-29,-11,32,32,-26,-24,-25,32,32,32,-36,-40,-39,-45,32,]),'OR':([10,12,13,17,19,20,21,22,23,24,25,26,27,28,41,42,43,44,46,48,55,56,57,58,63,67,69,75,76,87,],[33,-11,-29,-34,-27,-28,-30,-31,-32,-33,-35,-12,-13,-14,33,-29,-11,33,33,-26,-24,-25,33,33,33,-36,-40,-39,-45,33,]),'TIMES':([10,12,13,17,19,20,21,22,23,24,25,26,27,28,41,42,43,44,46,48,55,56,57,58,63,67,69,75,76,87,],[34,-11,-29,-34,-27,-28,-30,-31,-32,-33,-35,-12,-13,-14,34,-29,-11,34,34,-26,-24,-25,-49,34,34,-36,-40,-39,-45,34,]),'BIGGER':([10,12,13,17,19,20,21,22,23,24,25,26,27,28,41,42,43,44,46,48,55,56,57,58,63,67,69,75,76,87,],[35,-11,-29,-34,-27,-28,-30,-31,-32,-33,-35,-12,-13,-14,35,-29,-11,35,35,-26,-24,-25,-49,35,35,-36,-40,-39,-45,35,]),'ASSIGNATION':([12,13,26,27,28,],[37,40,-12,-13,-14,]),'LPAREN':([12,36,43,],[39,59,39,]),'DO':([17,19,20,21,22,23,24,25,26,27,28,42,43,44,48,55,56,57,58,67,69,75,76,],[-34,-27,-28,-30,-31,-32,-33,-35,-12,-13,-14,-29,-11,65,-26,-24,-25,-49,-50,-36,-40,-39,-45,]),'COMMA':([17,19,20,21,22,23,24,25,26,27,28,42,43,46,48,50,52,55,56,57,58,67,69,72,75,76,82,],[-34,-27,-28,-30,-31,-32,-33,-35,-12,-13,-14,-29,-11,66,-26,68,70,-24,-25,-49,-50,-36,-40,83,-39,-45,-44,]),'RPAREN':([17,19,20,21,22,23,24,25,26,27,28,39,42,43,46,47,48,55,56,57,58,59,62,66,67,69,72,73,74,75,76,79,86,],[-34,-27,-28,-30,-31,-32,-33,-35,-12,-13,-14,-51,-29,-11,-46,-48,-26,-24,-25,-49,-50,-51,76,-51,-36,-40,-17,84,-18,-39,-45,-47,-16,]),'RBRACE':([30,51,52,53,70,81,82,],[-51,69,-41,-43,-51,-42,-44,]),'RBRACKET':([49,50,61,80,],[67,-37,75,-38,]),'COLON':([54,],[71,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([0,3,41,65,],[2,31,64,78,]),'statement':([0,3,41,65,],[3,3,3,3,]),'function_def':([0,3,41,65,],[4,4,4,4,]),'assignment':([0,3,41,65,],[5,5,5,5,]),'if_statement':([0,3,41,65,],[6,6,6,6,]),'while_statement':([0,3,41,65,],[7,7,7,7,]),'puts_statement':([0,3,41,65,],[8,8,8,8,]),'gets_statement':([0,3,41,65,],[9,9,9,9,]),'expression':([0,3,14,15,16,18,32,33,34,35,39,40,41,65,66,84,],[10,10,41,44,46,48,55,56,57,58,46,63,10,10,46,87,]),'variable':([0,3,14,15,16,18,32,33,34,35,39,40,41,65,66,84,],[13,13,42,42,42,42,42,42,42,42,42,42,13,13,42,42,]),'array':([0,3,14,15,16,18,32,33,34,35,39,40,41,65,66,84,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'array_access':([0,3,14,15,16,18,32,33,34,35,39,40,41,65,66,84,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'function_call':([0,3,14,15,16,18,32,33,34,35,39,40,41,65,66,84,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'binary_operation':([0,3,14,15,16,18,32,33,34,35,39,40,41,65,66,84,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'hash':([0,3,14,15,16,18,32,33,34,35,39,40,41,65,66,84,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'arg_list':([16,39,66,],[45,62,79,]),'empty':([16,30,39,59,66,70,],[47,53,47,74,47,53,]),'array_elements':([29,68,],[49,80,]),'hash_elements':([30,70,],[51,81,]),'hash_element':([30,70,],[52,52,]),'param_list':([59,],[73,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program','proyectolpsintactico.py',15),
  ('statement_list -> statement','statement_list',1,'p_statement_list','proyectolpsintactico.py',19),
  ('statement_list -> statement statement_list','statement_list',2,'p_statement_list','proyectolpsintactico.py',20),
  ('statement -> function_def','statement',1,'p_statement','proyectolpsintactico.py',27),
  ('statement -> assignment','statement',1,'p_statement','proyectolpsintactico.py',28),
  ('statement -> if_statement','statement',1,'p_statement','proyectolpsintactico.py',29),
  ('statement -> while_statement','statement',1,'p_statement','proyectolpsintactico.py',30),
  ('statement -> puts_statement','statement',1,'p_statement','proyectolpsintactico.py',31),
  ('statement -> gets_statement','statement',1,'p_statement','proyectolpsintactico.py',32),
  ('statement -> expression','statement',1,'p_statement','proyectolpsintactico.py',33),
  ('variable -> VARIABLE_LOCAL','variable',1,'p_variable','proyectolpsintactico.py',37),
  ('variable -> VARIABLE_GLOBAL','variable',1,'p_variable','proyectolpsintactico.py',38),
  ('variable -> VARIABLE_INSTANCIA','variable',1,'p_variable','proyectolpsintactico.py',39),
  ('variable -> VARIABLE_CLASE','variable',1,'p_variable','proyectolpsintactico.py',40),
  ('function_def -> DEF VARIABLE_LOCAL LPAREN param_list RPAREN expression END','function_def',7,'p_function_def','proyectolpsintactico.py',44),
  ('param_list -> VARIABLE_LOCAL COMMA VARIABLE_LOCAL','param_list',3,'p_param_list','proyectolpsintactico.py',48),
  ('param_list -> VARIABLE_LOCAL','param_list',1,'p_param_list','proyectolpsintactico.py',49),
  ('param_list -> empty','param_list',1,'p_param_list','proyectolpsintactico.py',50),
  ('assignment -> variable ASSIGNATION expression','assignment',3,'p_assignment','proyectolpsintactico.py',57),
  ('while_statement -> WHILE expression DO statement_list END','while_statement',5,'p_while_statement','proyectolpsintactico.py',62),
  ('if_statement -> IF expression statement_list END','if_statement',4,'p_if_statement','proyectolpsintactico.py',66),
  ('puts_statement -> PUTS arg_list','puts_statement',2,'p_puts_statement','proyectolpsintactico.py',71),
  ('gets_statement -> VARIABLE_LOCAL ASSIGNATION GETS','gets_statement',3,'p_gets_statement','proyectolpsintactico.py',76),
  ('expression -> expression AND expression','expression',3,'p_expression_boolean','proyectolpsintactico.py',81),
  ('expression -> expression OR expression','expression',3,'p_expression_boolean','proyectolpsintactico.py',82),
  ('expression -> NOT expression','expression',2,'p_expression_boolean','proyectolpsintactico.py',83),
  ('expression -> INTEGER','expression',1,'p_expression','proyectolpsintactico.py',91),
  ('expression -> STRING','expression',1,'p_expression','proyectolpsintactico.py',92),
  ('expression -> variable','expression',1,'p_expression','proyectolpsintactico.py',93),
  ('expression -> array','expression',1,'p_expression','proyectolpsintactico.py',94),
  ('expression -> array_access','expression',1,'p_expression','proyectolpsintactico.py',95),
  ('expression -> function_call','expression',1,'p_expression','proyectolpsintactico.py',96),
  ('expression -> binary_operation','expression',1,'p_expression','proyectolpsintactico.py',97),
  ('expression -> GETS','expression',1,'p_expression','proyectolpsintactico.py',98),
  ('expression -> hash','expression',1,'p_expression','proyectolpsintactico.py',99),
  ('array -> LBRACKET array_elements RBRACKET','array',3,'p_array','proyectolpsintactico.py',103),
  ('array_elements -> INTEGER','array_elements',1,'p_array_elements','proyectolpsintactico.py',107),
  ('array_elements -> INTEGER COMMA array_elements','array_elements',3,'p_array_elements','proyectolpsintactico.py',108),
  ('array_access -> VARIABLE_LOCAL LBRACKET INTEGER RBRACKET','array_access',4,'p_array_access','proyectolpsintactico.py',115),
  ('hash -> LBRACE hash_elements RBRACE','hash',3,'p_hash','proyectolpsintactico.py',119),
  ('hash_elements -> hash_element','hash_elements',1,'p_hash_elements','proyectolpsintactico.py',123),
  ('hash_elements -> hash_element COMMA hash_elements','hash_elements',3,'p_hash_elements','proyectolpsintactico.py',124),
  ('hash_elements -> empty','hash_elements',1,'p_hash_elements','proyectolpsintactico.py',125),
  ('hash_element -> VARIABLE_LOCAL COLON STRING','hash_element',3,'p_hash_element','proyectolpsintactico.py',136),
  ('function_call -> VARIABLE_LOCAL LPAREN arg_list RPAREN','function_call',4,'p_function_call','proyectolpsintactico.py',140),
  ('arg_list -> expression','arg_list',1,'p_arg_list','proyectolpsintactico.py',144),
  ('arg_list -> expression COMMA arg_list','arg_list',3,'p_arg_list','proyectolpsintactico.py',145),
  ('arg_list -> empty','arg_list',1,'p_arg_list','proyectolpsintactico.py',146),
  ('binary_operation -> expression TIMES expression','binary_operation',3,'p_binary_operation','proyectolpsintactico.py',153),
  ('binary_operation -> expression BIGGER expression','binary_operation',3,'p_binary_operation','proyectolpsintactico.py',154),
  ('empty -> <empty>','empty',0,'p_empty','proyectolpsintactico.py',158),
]
