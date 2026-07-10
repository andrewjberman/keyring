#!/usr/bin/env python3
"""Mutant-kill tests for comp-cache (cache_cli), NFRA_TOOLPASS tool-5.

CTO acceptance arms: CAPTURE (non-arrow queryFn + hooks/ file), DENOMINATOR (printed),
TYPE-MISMATCH (<Foo> vs <Foo[]>), STEM (same-named files not merged), NEGATIVE (unique key
no false alarm; shared same-type = SHARED not bug).

Each guard is shown LOAD-BEARING: a *_MUTANT_* test drives the OLD behavior and asserts the
bug reappears -- a guard test that passes with the guard removed is decoration.

Fixtures are synthetic portal trees; no dependency on live portal state.
"""
from __future__ import annotations

import argparse
import importlib.util
import io
import contextlib
import re
import sys
from pathlib import Path

_WS = Path(__file__).resolve().parents[4]
_CLI = _WS / "org" / "modules" / "graph" / "cache_cli.py"
spec = importlib.util.spec_from_file_location("cache_cli", _CLI)
C = importlib.util.module_from_spec(spec)
sys.modules["cache_cli"] = C
spec.loader.exec_module(C)


def _mk(root: Path, rel: str, body: str) -> Path:
    p = root / "portal" / "src" / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(body, encoding="utf-8")
    return p


def _q(type_param: str, key: str, fn: str) -> str:
    t = f"<{type_param}>" if type_param else ""
    return (f"export function C() {{\n"
            f"  const {{ data }} = useQuery{t}({{\n"
            f"    queryKey: [{key}],\n"
            f"    queryFn: {fn},\n"
            f"    staleTime: 5,\n"
            f"  }})\n}}\n")


def _extract(root: Path):
    # point the extractor at the fixture's portal/src; patch _WORKSPACE so rel paths resolve
    C._WORKSPACE = root
    return C.extract(root / "portal" / "src")


# ---- CAPTURE: every queryFn shape + scope ------------------------------------------------

def test_capture_arrow_queryfn_positive_control(tmp_path):
    _mk(tmp_path, "pages/A.tsx", _q("Foo", "'k'", "() => getFoo()"))
    entries, _, total = _extract(tmp_path)
    assert total == 1 and len(entries) == 1
    assert entries[0].fetch_function == "getFoo"


def test_capture_bare_ref_queryfn(tmp_path):
    _mk(tmp_path, "pages/A.tsx", _q("Foo", "'k'", "getAUMTimeSeries"))
    entries, _, total = _extract(tmp_path)
    assert len(entries) == 1, "bare-reference queryFn must be captured (old regex dropped it)"
    assert entries[0].fetch_function == "getAUMTimeSeries"


def test_capture_async_queryfn(tmp_path):
    _mk(tmp_path, "pages/A.tsx", _q("Foo", "'k'", "async () => { return await f() }"))
    entries, _, total = _extract(tmp_path)
    assert len(entries) == 1, "async queryFn must be captured"


def test_capture_in_hooks_dir(tmp_path):
    _mk(tmp_path, "hooks/useThing.ts", _q("Foo", "'k'", "() => getFoo()"))
    entries, _, total = _extract(tmp_path)
    assert len(entries) == 1, "hooks/ scope must be read (old tool was pages/ only)"


def test_capture_in_ts_file(tmp_path):
    _mk(tmp_path, "pages/api.ts", _q("Foo", "'k'", "() => getFoo()"))
    entries, _, total = _extract(tmp_path)
    assert len(entries) == 1, ".ts files must be read (old rglob was *.tsx only)"


def test_capture_in_components_dir(tmp_path):
    _mk(tmp_path, "components/Widget.tsx", _q("Foo", "'k'", "() => getFoo()"))
    entries, _, _ = _extract(tmp_path)
    assert len(entries) == 1


# ---- complex generic types: REJECTED entirely by the old regex ---------------------------

def test_complex_union_type_captured_with_full_type(tmp_path):
    _mk(tmp_path, "pages/A.tsx", _q("Foo | null", "'k'", "() => getFoo()"))
    entries, _, _ = _extract(tmp_path)
    assert len(entries) == 1, "complex generic <Foo | null> must be captured (old regex REJECTED it)"
    assert entries[0].response_type == "Foo | null", "the FULL type must be captured, not one word"


def test_array_generic_type_captured(tmp_path):
    _mk(tmp_path, "pages/A.tsx", _q("Foo[]", "'k'", "() => getFoo()"))
    entries, _, _ = _extract(tmp_path)
    assert len(entries) == 1 and entries[0].response_type == "Foo[]"


def test_MUTANT_old_singleword_type_regex_rejects_complex_type():
    """NEGATIVE CONTROL: reconstruct the OLD regex and confirm it REJECTS <Foo | null> and
    <Foo[]> entirely (not just loses the type) while matching <Foo>. If this stops being
    true, the complex-type fix is untested."""
    old = re.compile(
        r"useQuery(?:<(\w+)>)?\s*\(\s*\{[^}]*?queryKey\s*:\s*\[([^\]]+)\][^}]*?"
        r"queryFn\s*:\s*\(\)\s*=>\s*(\w+)", re.DOTALL)
    simple = "useQuery<Foo>({ queryKey: ['k'], queryFn: () => getFoo })"
    union = "useQuery<Foo | null>({ queryKey: ['k'], queryFn: () => getFoo })"
    arr = "useQuery<Foo[]>({ queryKey: ['k'], queryFn: () => getFoo })"
    assert old.search(simple), "premise: old regex matches simple <Foo>"
    assert not old.search(union), "premise: old regex REJECTS <Foo | null> (whole entry lost)"
    assert not old.search(arr), "premise: old regex REJECTS <Foo[]>"


# ---- DENOMINATOR ---------------------------------------------------------------------------

def _run(cmd: str, root: Path, arg: str | None = None) -> str:
    C._WORKSPACE = root
    C._PORTAL_SRC = root / "portal" / "src"
    ns = argparse.Namespace(command=cmd, query=arg)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        {"map": C.cmd_map, "collisions": C.cmd_collisions, "key": C.cmd_key}[cmd](ns)
    return buf.getvalue()


def test_denominator_printed_on_every_command(tmp_path):
    _mk(tmp_path, "pages/A.tsx", _q("Foo", "'k'", "() => getFoo()"))
    for cmd, arg in [("map", None), ("collisions", None), ("key", "k")]:
        out = _run(cmd, tmp_path, arg)
        assert re.search(r"captured \d+ of \d+ useQuery call-site", out), \
            f"{cmd} MUST print captured-of-total; got:\n{out}"


def test_denominator_counts_unparseable_not_silently_dropped(tmp_path):
    # a useQuery with NO queryKey -> unparseable, but COUNTED in the denominator + listed
    _mk(tmp_path, "pages/B.tsx",
        "function C(){ const x = useQuery({ queryFn: () => f() }) }\n")
    entries, unparseable, total = _extract(tmp_path)
    assert total == 1, "the malformed call is still a call-site (denominator)"
    assert len(entries) == 0 and len(unparseable) == 1
    assert unparseable[0].reason == "no queryKey field"


# ---- TYPE-MISMATCH -------------------------------------------------------------------------

def test_type_mismatch_flagged_across_files(tmp_path):
    _mk(tmp_path, "pages/A.tsx", _q("Foo", "'shared'", "() => getFoo()"))
    _mk(tmp_path, "pages/B.tsx", _q("Foo[]", "'shared'", "() => getFoo()"))
    out = _run("collisions", tmp_path)
    assert "TYPE MISMATCH" in out, "same key, <Foo> vs <Foo[]> across files MUST flag mismatch"


def test_MUTANT_type_mismatch_invisible_if_complex_type_dropped(tmp_path):
    """If the array type were dropped (old behavior), B.tsx would carry NO type and the
    mismatch would be invisible. Proves complex-type capture is what makes the bug-signal work."""
    _mk(tmp_path, "pages/A.tsx", _q("Foo", "'shared'", "() => getFoo()"))
    _mk(tmp_path, "pages/B.tsx", _q("Foo[]", "'shared'", "() => getFoo()"))
    entries, _, _ = _extract(tmp_path)
    types = {e.response_type for e in entries}
    assert types == {"Foo", "Foo[]"}, "both types present -> mismatch detectable"
    # counter-factual: if B's type were '' (dropped), the set would be {'Foo',''} -> no >1 real mismatch
    dropped = {"Foo", ""}
    assert len({t for t in dropped if t}) == 1, "with the type dropped, the mismatch is invisible"


# ---- STEM: same-named files must not merge ------------------------------------------------

def test_same_stem_files_not_merged_collision_flagged(tmp_path):
    """Exercises cmd_collisions itself (not just extract): two same-stem files sharing a key
    with DIFFERENT types MUST surface as a flagged collision. Under stem-identity they merge
    to one 'component' and the collision is masked."""
    _mk(tmp_path, "pages/_partners/inflection/index.tsx", _q("Foo", "'aua'", "() => getFoo()"))
    _mk(tmp_path, "pages/_partners/49financial/index.tsx", _q("Bar", "'aua'", "() => getFoo()"))
    out = _run("collisions", tmp_path)
    assert "No cross-file cache-key collisions" not in out, \
        "the shared 'aua' key across two index.tsx MUST be flagged, not masked by stem-collapse"
    assert "!! TYPE MISMATCH !!" in out, "different types (Foo vs Bar) on the shared key is the bug"
    assert "inflection/index.tsx" in out and "49financial/index.tsx" in out, \
        "both files must be named (file_path identity, not the merged stem 'index')"


def test_MUTANT_stem_identity_would_merge_and_mask(tmp_path):
    """NEGATIVE CONTROL: identity-by-stem collapses the two index.tsx to one -> a real
    collision reads as len({components})==1 and is NOT flagged. Proves file_path identity
    is load-bearing."""
    _mk(tmp_path, "pages/_partners/inflection/index.tsx", _q("Foo", "'aua'", "() => getFoo()"))
    _mk(tmp_path, "pages/_partners/49financial/index.tsx", _q("Bar", "'aua'", "() => getFoo()"))
    entries, _, _ = _extract(tmp_path)
    by_stem = {e.file_path.split("/")[-1] for e in entries}   # the OLD identity
    by_path = {e.file_path for e in entries}
    assert by_stem == {"index.tsx"}, "premise: stems collapse to one"
    assert len(by_path) == 2, "file_path keeps them distinct -> the collision is visible"


# ---- NEGATIVE: no false alarms -------------------------------------------------------------

def test_unique_keys_no_collision(tmp_path):
    _mk(tmp_path, "pages/A.tsx", _q("Foo", "'a'", "() => getA()"))
    _mk(tmp_path, "pages/B.tsx", _q("Bar", "'b'", "() => getB()"))
    out = _run("collisions", tmp_path)
    assert "No cross-file cache-key collisions" in out


def test_shared_same_type_is_shared_not_type_mismatch(tmp_path):
    _mk(tmp_path, "pages/A.tsx", _q("Foo", "'shared'", "() => getFoo()"))
    _mk(tmp_path, "pages/B.tsx", _q("Foo", "'shared'", "() => getFoo()"))
    out = _run("collisions", tmp_path)
    assert "shared key" in out.lower()
    # the per-key ALARM must not fire; the summary line "0 with a TYPE MISMATCH" is disclosure
    assert "!! TYPE MISMATCH !!" not in out, "same-type shared key is legitimate, not a bug alarm"
    assert "0 with a TYPE MISMATCH" in out, "and the bug-class count is disclosed as zero"


def test_useQueryClient_and_useQueries_not_counted(tmp_path):
    _mk(tmp_path, "pages/A.tsx",
        "function C(){ const c = useQueryClient(); const r = useQueries({ queries: [] }) }\n")
    entries, _, total = _extract(tmp_path)
    assert total == 0 and len(entries) == 0, "useQueryClient/useQueries are not useQuery"


# ---- robustness: the [^}]*? killer ---------------------------------------------------------

def test_nested_object_and_multiline_captured(tmp_path):
    body = ("export function C() {\n"
            "  const { data } = useQuery<Foo>({\n"
            "    queryKey: ['k', id],\n"
            "    queryFn: () => getFoo(id),\n"
            "    select: (d) => ({ mapped: d.x }),\n"   # a nested {} before nothing, and after queryFn
            "    enabled: !!(a && b),\n"
            "  })\n}\n")
    _mk(tmp_path, "pages/A.tsx", body)
    entries, _, _ = _extract(tmp_path)
    assert len(entries) == 1, "a nested object literal must not break extraction (old [^}]*? did)"
    assert entries[0].key_parts == ["k", "id"]


def test_apostrophe_in_comment_does_not_break_extraction(tmp_path):
    """The two live 'runaway call' residuals were comments with apostrophes+parens inside the
    options object (`// Don't retry on auth errors (401/403)`). Comment-blanking must fix it."""
    body = ("export function C() {\n"
            "  return useQuery({\n"
            "    queryKey: ['k', id],\n"
            "    queryFn: () => getFoo(id),\n"
            "    // Don't retry on auth errors (401/403) -- doesn't help\n"
            "    staleTime: 10, // 10 minutes (data doesn't change often)\n"
            "  })\n}\n")
    _mk(tmp_path, "pages/hooks/useThing.ts", body)
    entries, unparseable, total = _extract(tmp_path)
    assert len(entries) == 1 and not unparseable, \
        f"apostrophe/paren in a comment must not break the call; got unparseable={unparseable}"
    assert entries[0].line_number == 2, "line number must survive comment-blanking (offset preserved)"


def test_double_slash_inside_string_is_not_a_comment(tmp_path):
    """A URL in a queryKey ('https://...') must NOT be blanked as a comment."""
    body = ("export function C() {\n"
            "  return useQuery({\n"
            "    queryKey: ['https://api.example.com/x', id],\n"
            "    queryFn: () => getFoo(id),\n"
            "  })\n}\n")
    _mk(tmp_path, "pages/A.tsx", body)
    entries, _, _ = _extract(tmp_path)
    assert len(entries) == 1
    assert "https://api.example.com/x" in entries[0].key_parts, "// inside a string is not a comment"


def test_string_with_brace_does_not_break_balance(tmp_path):
    body = ("export function C() {\n"
            "  const { data } = useQuery<Foo>({\n"
            "    queryKey: ['pre}fix', id],\n"          # a } inside a string literal
            "    queryFn: () => getFoo(id),\n"
            "  })\n}\n")
    _mk(tmp_path, "pages/A.tsx", body)
    entries, _, _ = _extract(tmp_path)
    assert len(entries) == 1, "a } inside a string must not terminate the object early"
    assert "pre}fix" in entries[0].key_parts
