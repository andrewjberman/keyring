"""Fingerprints of a file's behaviour, blind to comments, docstrings and the project name (SOC2_MSLOGS round 1, cell SM-x-1)."""
import ast
import hashlib
import re


def py_fp(text):
    tree = ast.parse(text)
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            body = getattr(node, "body", [])
            if body and isinstance(body[0], ast.Expr) and isinstance(getattr(body[0], "value", None), ast.Constant) and isinstance(body[0].value.value, str):
                node.body = body[1:] or [ast.Pass()]
    return hashlib.sha256(ast.dump(tree).encode("utf-8")).hexdigest()[:16]


def tf_fp(text):
    out = []
    for line in text.replace("TCKT_MTADTA", "SOC2_MSLOGS").splitlines():
        s = re.sub(r"\s+#.*$", "", line) if not line.lstrip().startswith("#") else ""
        s = s.strip()
        if s:
            out.append(re.sub(r"\s+", " ", s))
    return hashlib.sha256("\n".join(out).encode("utf-8")).hexdigest()[:16]
