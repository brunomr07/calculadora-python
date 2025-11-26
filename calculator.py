import ast
import operator as op
import math
import sys

# Operadores permitidos
ALLOWED_OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.FloorDiv: op.floordiv,
    ast.Mod: op.mod,
    ast.Pow: op.pow,
    ast.UAdd: op.pos,
    ast.USub: op.neg,
}

# Funções permitidas
ALLOWED_FUNCTIONS = {
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'sqrt': math.sqrt,
    'log': math.log,
    'log10': math.log10,
    'exp': math.exp,
    'abs': abs,
    'round': round,
}

def safe_eval(expr: str):
    try:
        node = ast.parse(expr, mode='eval')
        return _eval_node(node.body)
    except Exception as e:
        raise ValueError(f"Expressão inválida: {e}")

def _eval_node(node):
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        else:
            raise ValueError("Constante não suportada")

    if isinstance(node, ast.BinOp):
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        op_type = type(node.op)
        if op_type in ALLOWED_OPERATORS:
            return ALLOWED_OPERATORS[op_type](left, right)
        else:
            raise ValueError("Operador não permitido")

    if isinstance(node, ast.UnaryOp):
        operand = _eval_node(node.operand)
        op_type = type(node.op)
        if op_type in ALLOWED_OPERATORS:
            return ALLOWED_OPERATORS[op_type](operand)
        else:
            raise ValueError("Operador unário não permitido")

    if isinstance(node, ast.Call):
        if isinstance(node.func, ast.Name):
            func_name = node.func.id
            if func_name in ALLOWED_FUNCTIONS:
                args = [_eval_node(a) for a in node.args]
                return ALLOWED_FUNCTIONS[func_name](*args)
        raise ValueError("Função não permitida")

    raise ValueError(f"Nó não suportado: {type(node).__name__}")

def repl():
    print("Calculadora Python — digite 'sair' para encerrar.")
    while True:
        try:
            expr = input("> ").strip()
            if expr.lower() in ("sair", "exit"):
                print("Saindo...")
                break
            print(safe_eval(expr))
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Ex: python calculator.py "2+2*3"
        print(safe_eval(sys.argv[1]))
    else:
        repl()
