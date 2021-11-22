from py_expression_eval import Parser

def Evaluar(funcion,x):
    parser = Parser()
    return parser.parse(funcion).evaluate({'x': x}) 
