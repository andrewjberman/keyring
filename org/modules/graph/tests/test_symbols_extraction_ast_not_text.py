#!/usr/bin/env python3
"""comp-symbols standing correctness+discrimination test: the value is AST, not text.

Author: 3.0.0_SA_CVO~A. NFRA_TOOLPASS comp-symbols (CTO GO 20260711T000520Z).

comp-symbols (org/modules/graph/comp_symbols.py) is a deterministic ast.parse symbol inventory:
module-level functions (incl async), classes+methods, module-level bindings (UPPER-tagged), and
imports, each with a 1-based line number. It front-passed CLEAN but had NO committed test. The
LOAD-BEARING property -- the whole reason it beats a raw grep -- is that it parses an AST and
iterates `tree.body` (module-level nodes ONLY), so a `def` that lives in a STRING, a COMMENT, or
NESTED inside another function is NOT surfaced as a module-level function. A naive line-grep
counts all three; the AST does not. This is the standing guard for that discrimination, plus the
edge-case correctness CTO asked to confirm.

bd-CLEAN: the fixture is an in-memory source STRING (parse_python(text)); the one file-based case
uses pytest tmp_path. NEVER reads a real data/black_diamond file (comp-symbols requires an explicit
file arg -- no default/bd auto-scan; CTO ruling, same disposition accepted on comp-shell). Hermetic:
imports the module directly, no CLI subprocess -> no pytest.ini bd-pythonpath landmine.

NOTE (source-confirmed, accepted-as-property by CTO, not a defect): imports capture the CANONICAL
name only (`a.name` / `mod.a.name`, comp_symbols.py:81-86) -- the ASNAME is dropped. So
`import numpy as np` -> "numpy", `from x import y as z` -> "x.y". Documented + asserted below.
"""
from __future__ import annotations

import importlib.util
import json
import re
import sys
from pathlib import Path

_GRAPH = Path(__file__).resolve().parents[4] / "org" / "modules" / "graph"
sys.path.insert(0, str(_GRAPH))


def _load():
    spec = importlib.util.spec_from_file_location("comp_symbols_sut", _GRAPH / "comp_symbols.py")
    m = importlib.util.module_from_spec(spec)
    sys.modules["comp_symbols_sut"] = m
    spec.loader.exec_module(m)
    return m


M = _load()

# A source with, at module level: an async def, a plain def with a NESTED def, a DECORATED class
# with methods + a class-body const, module consts (UPPER + non-UPPER + annotated), aliased imports,
# and THREE decoy defs that only a text scanner would count (module string / comment / string value).
_SRC = '''\
"module string decoy: def docstring_fake(): pass  -- MUST NOT be a function"
from __future__ import annotations
import os
import numpy as np
from collections import OrderedDict as OD
from x.y import zsym as zz

MAX_LAG = 2
threshold = 5
_PRIVATE = 9
annotated_count: int = 0

# def commented_out():  a comment decoy, MUST NOT be a function
_S = "def string_literal_fake(): pass"

async def fetch_it(url, *, retries=3):
    def inner_helper(x):
        return x
    return inner_helper(url)

def outer_plain(a, b=1):
    return a + b

@some_decorator
class Widget:
    CLASS_CONST = 7
    def method_one(self, z):
        return z
    async def amethod(self):
        return None
'''

# names a naive `\bdef\s+NAME` text scan sees but the AST must NOT surface as module functions:
_TEXT_ONLY_DEFS = {"docstring_fake", "commented_out", "string_literal_fake", "inner_helper",
                   "method_one", "amethod"}


def _parsed():
    return M.parse_python(_SRC)


def _fn_names(p):
    return {f["name"] for f in p["functions"]}


# ---------------------------------------------------------------------------------------------
# THE LOAD-BEARING DISCRIMINATION: ast, not text.
# ---------------------------------------------------------------------------------------------
def test_string_and_comment_defs_are_not_counted():
    """A `def` inside the module docstring, a comment, and a string VALUE must NOT be functions.
    This is the entire value of ast over grep -- if it fails, the tool is a glorified line-grep."""
    names = _fn_names(_parsed())
    for decoy in ("docstring_fake", "commented_out", "string_literal_fake"):
        assert decoy not in names, f"a text-only `def {decoy}` was miscounted as a function -- ast defeated"


def test_nested_function_is_not_module_level():
    """A def NESTED in another function is not in tree.body -> not a module-level function.
    (Correctly EXCLUDED, never mislabeled module-level -- the FUNCTIONS list is [module-level].)"""
    names = _fn_names(_parsed())
    assert "outer_plain" in names, "the enclosing module-level def must be listed"
    assert "inner_helper" not in names, "a NESTED def leaked into the module-level function list"


def test_ast_excludes_exactly_what_a_naive_grep_would_include():
    """STANDING NEUTER-AUDIT / non-vacuity proof: every text-only def IS visible to a `\\bdef` grep
    but MUST be absent from the ast module-function names. If parse_python ever regresses to a text
    scan, these names leak into ast_fn_names and this test (+ the two above) flip RED."""
    grep_names = set(re.findall(r"\bdef\s+(\w+)", _SRC))
    assert _TEXT_ONLY_DEFS <= grep_names, (
        f"fixture invariant broken: {_TEXT_ONLY_DEFS - grep_names} are not even grep-visible")
    leaked = _TEXT_ONLY_DEFS & _fn_names(_parsed())
    assert not leaked, f"ast leaked text-only/nested/method defs into module functions: {leaked}"


# ---------------------------------------------------------------------------------------------
# EDGE-CASE CORRECTNESS (CTO's confirm list).
# ---------------------------------------------------------------------------------------------
def test_async_def_is_indexed_as_a_function_and_flagged():
    fns = {f["name"]: f for f in _parsed()["functions"]}
    assert "fetch_it" in fns, "async def must be indexed as a function"
    assert fns["fetch_it"]["async"] is True, "async def must carry async=True"
    assert fns["outer_plain"]["async"] is False, "a plain def must be async=False"
    assert isinstance(fns["fetch_it"]["line"], int) and fns["fetch_it"]["line"] > 0, "line must be tracked"


def test_decorated_class_is_found_with_scoped_methods():
    p = _parsed()
    classes = {c["name"]: c for c in p["classes"]}
    assert "Widget" in classes, "a DECORATED class must still be found (decorators != ClassDef change)"
    method_names = {m["name"] for m in classes["Widget"]["methods"]}
    assert method_names == {"method_one", "amethod"}, f"class methods wrong: {method_names}"
    amethod = next(m for m in classes["Widget"]["methods"] if m["name"] == "amethod")
    assert amethod["async"] is True, "an async method must carry async=True"
    # methods are scoped to the class, NOT promoted to module-level functions:
    assert not ({"method_one", "amethod"} & _fn_names(p)), "class methods leaked into module functions"
    # a class-body assignment is NOT a module-level constant:
    assert "CLASS_CONST" not in {c["name"] for c in p["constants"]}, "class-body const leaked to module scope"


def test_const_upper_heuristic_does_not_misclassify():
    consts = {c["name"]: c["upper"] for c in _parsed()["constants"]}
    assert consts.get("MAX_LAG") is True, "an UPPER const must be tagged upper"
    assert consts.get("_PRIVATE") is True, "a leading-underscore UPPER const must be tagged upper"
    assert consts.get("threshold") is False, "a lowercase binding must NOT be misclassified UPPER"
    assert consts.get("annotated_count") is False, "an annotated lowercase binding must NOT be UPPER"


def test_imports_capture_canonical_name_asname_dropped():
    """Documents+guards the accepted property: canonical module path is captured, asname dropped."""
    names = {i["name"] for i in _parsed()["imports"]}
    assert {"os", "numpy", "collections.OrderedDict", "x.y.zsym", "__future__.annotations"} <= names, (
        f"canonical import names missing: {names}")
    assert not ({"np", "OD", "zz"} & names), (
        "an asname was surfaced -- comp_symbols.py:81-86 captures a.name only; update this test AND "
        "the docstring NOTE if that behavior is intentionally changed")


# ---------------------------------------------------------------------------------------------
# PUBLIC ENTRY + JSON ROUND-TRIP (file path via tmp_path; still bd-clean).
# ---------------------------------------------------------------------------------------------
def test_analyze_and_json_round_trip(tmp_path):
    f = tmp_path / "fixture_symbols.py"
    f.write_text(_SRC, encoding="utf-8")
    a = M.analyze(str(f))
    assert "error" not in a, f"analyze errored on a valid file: {a.get('error')}"
    assert a["lang"] == "py" and a["path"].endswith("fixture_symbols.py")
    for key in ("functions", "classes", "constants", "imports", "path", "lang"):
        assert key in a, f"analyze output missing key {key}"
    round_tripped = json.loads(json.dumps(a))
    assert round_tripped == a, "analyze output did not survive a json round-trip"


def test_not_found_file_is_a_clean_error_not_a_crash():
    """NEGATIVE CONTROL: a missing file yields an error dict (rc-1 path), never an exception."""
    a = M.analyze("org/modules/graph/__nonexistent_zzz__.py")
    assert a.get("error", "").startswith("file not found"), f"missing file must be a clean error: {a}"
    assert "functions" not in a, "an error result must not carry a symbol table"
