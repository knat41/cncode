import ast
from difflib import SequenceMatcher

def ast_similarity(code1, code2):
    """ เปรียบเทียบโครงสร้าง AST ของโค้ด 2 ชุด """
    tree1 = ast.dump(ast.parse(code1))
    tree2 = ast.dump(ast.parse(code2))
    return SequenceMatcher(None, tree1, tree2).ratio()

# ตัวอย่างโค้ดที่ใช้เปรียบเทียบ
code_a = """def add(a, b):
    return a + b"""

code_b = """def sum_numbers(x, y):
    return x + y"""

similarity = ast_similarity(code_a, code_b)
print(f"Code Similarity (AST): {similarity * 100:.2f}%")

