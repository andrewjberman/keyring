#!/usr/bin/env python3
"""
comp-cache -- React Query cache key analysis across components.

Detects:
  - Cache key collisions (same key used by multiple components)
  - Type mismatches (same key, different response types)  <- the real bug-signal
  - Shared cache dependencies (components that legitimately share a key + type)

Usage:
    comp-cache map          # all cache keys -> components (+ capture denominator)
    comp-cache collisions   # keys shared by multiple components, typed
    comp-cache key <substr> # find all uses of a cache key substring

SCOPE + HONESTY (rebuilt 2026-07-10, NFRA_TOOLPASS tool-5):
  The prior tool was ONE regex over portal/src/pages/**/*.tsx that (a) read ONLY pages/*.tsx
  -- missing pages/*.ts, components/, hooks/ (56% of call-sites), (b) required a `() => fn`
  queryFn and a single-word `<Word>` type, so a bare-ref queryFn, an async queryFn, or a
  complex type `<Foo | null>` / `<Foo[]>` was DROPPED ENTIRELY (not just its type lost), and
  (c) printed "45 keys" with NO denominator -- a collision detector blind to 56% of the
  call-sites reading as authoritative. This rebuild:
    - scans ALL of portal/src (.ts + .tsx), not pages/*.tsx;
    - uses string-aware BALANCED-DELIMITER extraction (not a `[^}]*?` regex), so nested
      braces, multi-line calls, complex generic types, and every queryFn shape parse;
    - identifies a component by FILE PATH, never file.stem (four partner index.tsx no longer
      collapse to one "index" and mask a cross-partner collision);
    - DISCLOSES THE DENOMINATOR on every run: "captured X of Y useQuery call-sites; Z
      unparseable -- listed". A number without its denominator is the defect this tool WAS.
  Read-only. No writes, no manifest. Authoritative source: portal/src (on DEV).

  Adjacent hooks NOT in scope (flagged, not folded): useQueries / useInfiniteQuery also carry
  queryKeys, and useAutoSaveQuery (a local PortfolioManagement wrapper that constructs
  portfolioKeys.* keys around an inner useQuery) is un-audited key-bearing surface at its call
  sites (L1a sensor-2 finding, 2026-07-25 -- disclosure-first disposition; walk-extension is a
  separate banked follow-on). This tool audits useQuery only, and SAYS SO in the denominator
  line. The caveat deliberately carries NO call-site count -- counts drift; the sensor
  (org/tier2_senior/0.8.0_AE_CloudComp/deliverables/l1a_sensor2/) is the counting instrument.
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_WORKSPACE = _THIS_DIR.parent.parent.parent
_PORTAL_SRC = _WORKSPACE / "portal" / "src"
_TOOLS = _WORKSPACE / ".tools"
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))
import _compbudget  # noqa: E402 -- Rule T shared carrier (NFRA_COMPEFFICACY T-23)

# useQuery, not useQueryClient / useQueries / useInfiniteQuery. Word-boundary before, and the
# next char is `<` (generic) or `(` (call) -- which excludes the longer identifiers.
_USEQUERY = re.compile(r"(?<![A-Za-z0-9_])useQuery(?=\s*[<(])")


@dataclass
class CacheEntry:
    key_str: str              # the queryKey array text, verbatim
    key_parts: list[str]      # parsed key parts (literals + identifiers)
    response_type: str        # FULL generic type text ('Foo | null', 'Foo[]', ''), not one word
    fetch_function: str       # queryFn target (fn name for `() => fn(...)`/`fn`, else raw shape)
    file_path: str            # source file (relative) -- THIS is component identity, not stem
    line_number: int


@dataclass
class Unparseable:
    file_path: str
    line_number: int
    reason: str


@dataclass
class SkippedFile:
    file_path: str
    reason: str


@dataclass
class ScanResult:
    entries: list[CacheEntry]
    unparseable: list[Unparseable]
    total_call_sites: int
    total_files: int
    scanned_files: int
    skipped_files: list[SkippedFile]
    source_exists: bool
    last_cursor: str
    budget_reached: bool


# ---- string-aware balanced-delimiter scanning ---------------------------------------------

def _skip_string(s: str, i: int) -> int:
    """If s[i] opens a JS string ('/"/`), return the index just past its close; else i."""
    q = s[i]
    if q not in "'\"`":
        return i
    j = i + 1
    while j < len(s):
        if s[j] == "\\":
            j += 2
            continue
        if s[j] == q:
            return j + 1
        j += 1
    return j


def _blank_comments(s: str) -> str:
    """Replace // and /* */ comment CONTENT with spaces, string-aware, PRESERVING length and
    newlines (so reported line numbers stay exact). Without this, an apostrophe in a comment
    (`don't`) opens a phantom string and a paren in a comment (`(401/403)`) unbalances the
    call -- the two 'runaway call' residuals on the live portal were exactly this."""
    out = list(s)
    i, n = 0, len(s)
    while i < n:
        c = s[i]
        if c in "'\"`":
            j = _skip_string(s, i)
            i = j
            continue
        if c == "/" and i + 1 < n and s[i + 1] == "/":
            while i < n and s[i] != "\n":
                out[i] = " "
                i += 1
            continue
        if c == "/" and i + 1 < n and s[i + 1] == "*":
            while i < n and not (s[i] == "*" and i + 1 < n and s[i + 1] == "/"):
                if s[i] != "\n":
                    out[i] = " "
                i += 1
            if i + 1 < n:
                out[i] = out[i + 1] = " "
                i += 2
            continue
        i += 1
    return "".join(out)


def _match_balanced(s: str, open_idx: int, open_ch: str, close_ch: str) -> int | None:
    """Index just past the close delimiter matching s[open_idx]==open_ch, string-aware.
    Returns None if unbalanced (runaway)."""
    depth = 0
    i = open_idx
    n = len(s)
    while i < n:
        c = s[i]
        if c in "'\"`":
            i = _skip_string(s, i)
            continue
        if c == open_ch:
            depth += 1
        elif c == close_ch:
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    return None


def _split_top_level(obj_inner: str) -> list[str]:
    """Split an object body on top-level commas, string- and nesting-aware."""
    parts, depth, i, start = [], 0, 0, 0
    n = len(obj_inner)
    while i < n:
        c = obj_inner[i]
        if c in "'\"`":
            i = _skip_string(obj_inner, i)
            continue
        if c in "{[(":
            depth += 1
        elif c in "}])":
            depth -= 1
        elif c == "," and depth == 0:
            parts.append(obj_inner[start:i])
            start = i + 1
        i += 1
    parts.append(obj_inner[start:])
    return parts


def _parse_key_parts(key_text: str) -> list[str]:
    parts = []
    for m in re.findall(r"'([^']*)'|\"([^\"]*)\"|`([^`]*)`|([A-Za-z_$][\w$.]*)", key_text):
        val = next((g for g in m if g), "")
        if val:
            parts.append(val)
    return parts


def _normalize_queryfn(raw: str) -> str:
    """Best-effort target name from a queryFn value of any shape; else a shape tag."""
    raw = raw.strip()
    m = re.match(r"\(\s*[^)]*\)\s*=>\s*(?:async\s*)?([A-Za-z_$][\w$.]*)", raw)  # () => fn / (a)=>fn
    if m:
        return m.group(1)
    m = re.match(r"async\s*\(\s*[^)]*\)\s*=>\s*([A-Za-z_$][\w$.]*)", raw)        # async () => fn
    if m:
        return m.group(1)
    if re.match(r"(async\s*)?\(\s*[^)]*\)\s*=>\s*\{", raw):                       # arrow with block body
        return "<inline-block>"
    m = re.match(r"([A-Za-z_$][\w$.]*)\s*$", raw)                                  # bare reference
    if m:
        return m.group(1)
    return "<expr>"


def _extract_from_content(content: str, rel_path: str,
                          entries: list[CacheEntry], unparseable: list[Unparseable]) -> int:
    """Append entries; return the number of useQuery CALL-SITES seen (the denominator)."""
    seen = 0
    for hook in _USEQUERY.finditer(content):
        seen += 1
        line_no = content.count("\n", 0, hook.start()) + 1
        i = hook.end()
        n = len(content)
        while i < n and content[i].isspace():
            i += 1

        # optional balanced <Type ...>
        resp_type = ""
        if i < n and content[i] == "<":
            end = _match_balanced(content, i, "<", ">")
            if end is None:
                unparseable.append(Unparseable(rel_path, line_no, "runaway generic <...>"))
                continue
            resp_type = content[i + 1:end - 1].strip()
            i = end
            while i < n and content[i].isspace():
                i += 1

        # expect ( ... )
        if i >= n or content[i] != "(":
            unparseable.append(Unparseable(rel_path, line_no, "no '(' after useQuery"))
            continue
        call_end = _match_balanced(content, i, "(", ")")
        if call_end is None:
            unparseable.append(Unparseable(rel_path, line_no, "runaway call (...)"))
            continue
        call_inner = content[i + 1:call_end - 1]

        # the options object {...}
        brace = call_inner.find("{")
        if brace == -1:
            unparseable.append(Unparseable(rel_path, line_no, "no options object {}"))
            continue
        obj_end = _match_balanced(call_inner, brace, "{", "}")
        if obj_end is None:
            unparseable.append(Unparseable(rel_path, line_no, "runaway options object {}"))
            continue
        obj_inner = call_inner[brace + 1:obj_end - 1]

        key_text = fn_text = None
        for field in _split_top_level(obj_inner):
            km = re.match(r"\s*queryKey\s*:", field)
            if km:
                key_text = field[km.end():].strip()
                continue
            fm = re.match(r"\s*queryFn\s*:", field)
            if fm:
                fn_text = field[fm.end():].strip()

        if key_text is None:
            unparseable.append(Unparseable(rel_path, line_no, "no queryKey field"))
            continue

        # queryKey may be [ ... ] or a variable/spread -- keep either as identity
        if key_text.startswith("["):
            arr_end = _match_balanced(key_text, 0, "[", "]")
            key_body = key_text[1:arr_end - 1] if arr_end else key_text.strip("[]")
        else:
            key_body = key_text  # variable key (still an identity)
        key_parts = _parse_key_parts(key_body)

        entries.append(CacheEntry(
            key_str=key_body.strip(),
            key_parts=key_parts,
            response_type=resp_type,
            fetch_function=_normalize_queryfn(fn_text) if fn_text else "<none>",
            file_path=rel_path,
            line_number=line_no,
        ))
    return seen


def _file_label(path: Path, portal_src: Path) -> str:
    """A deterministic cursor/file label, even for an explicit fixture outside the workspace."""
    try:
        return str(path.relative_to(_WORKSPACE)).replace("\\", "/")
    except ValueError:
        return "portal/src/" + str(path.relative_to(portal_src)).replace("\\", "/")


def _is_generated(content: str, path: Path) -> bool:
    """Generated TS is an explicit blind spot, never silently parsed as source-of-record."""
    return ("@generated" in content[:512].lower()
            or path.name.endswith(".generated.ts")
            or path.name.endswith(".generated.tsx"))


def scan(portal_src: Path | None = None, cursor: str | None = None,
         clock: _compbudget.Clock | None = None) -> ScanResult:
    """Scan the deterministic TS/TSX corpus once, preserving every partial-scan denominator."""
    portal_src = portal_src if portal_src is not None else _PORTAL_SRC
    entries: list[CacheEntry] = []
    unparseable: list[Unparseable] = []
    skipped: list[SkippedFile] = []
    total = 0
    if not portal_src.exists():
        return ScanResult(entries, unparseable, total, 0, 0, skipped, False, "START", False)

    files = sorted(list(portal_src.rglob("*.tsx")) + list(portal_src.rglob("*.ts")),
                   key=lambda p: _file_label(p, portal_src))
    labels = [_file_label(f, portal_src) for f in files]
    start_at = 0
    if cursor and cursor != "START":
        if cursor not in labels:
            raise ValueError(f"cursor is not a portal source unit: {cursor}")
        start_at = labels.index(cursor) + 1

    scanned = 0
    last_cursor = cursor or "START"
    budget_reached = False
    for f, rel in zip(files[start_at:], labels[start_at:]):
        if clock is not None and clock.remaining() is not None and clock.remaining() <= 0:
            budget_reached = True
            break
        try:
            content = f.read_text(encoding="utf-8", errors="strict")
        except Exception as exc:
            skipped.append(SkippedFile(rel, f"unreadable: {type(exc).__name__}"))
            last_cursor = rel
            continue
        if _is_generated(content, f):
            skipped.append(SkippedFile(rel, "generated source is outside the parser's declared corpus"))
            last_cursor = rel
            continue
        scanned += 1
        if "useQuery" in content:
            total += _extract_from_content(_blank_comments(content), rel, entries, unparseable)
        last_cursor = rel

    return ScanResult(entries, unparseable, total, len(files), scanned, skipped, True,
                      last_cursor, budget_reached)


def extract(portal_src: Path | None = None):
    """Compatibility surface: (entries, unparseable, total_call_sites) over portal/src."""
    result = scan(portal_src)
    return result.entries, result.unparseable, result.total_call_sites


def _denominator_line(result: ScanResult) -> str:
    return (f"scanned {result.scanned_files} of {result.total_files} portal source file(s); "
            f"skipped {len(result.skipped_files)} file(s); captured {len(result.entries)} of "
            f"{result.total_call_sites} useQuery call-site(s); {len(result.unparseable)} unparseable "
            f"(useQueries / useInfiniteQuery / useAutoSaveQuery are NOT audited by this tool)")


def _print_unparseable(unparseable):
    if unparseable:
        print("  UNPARSEABLE (listed, not silently dropped):")
        for u in unparseable:
            print(f"    {u.file_path}:{u.line_number} -- {u.reason}")
        print()


def _print_skipped(skipped):
    if skipped:
        print("  SKIPPED FILES (listed, not silently read as clean):")
        for item in skipped:
            print(f"    {item.file_path} -- {item.reason}")
        print()


def _base_answer_state(result: ScanResult) -> str | None:
    if not result.source_exists:
        return "SUBJECT_ABSENT_FROM_CORPUS"
    if result.budget_reached or result.skipped_files or result.unparseable:
        return "PARTIAL_OR_BLIND"
    if result.total_call_sites == 0:
        return "NOT_APPLICABLE"
    return None


def _print_answer_state(state: str | None):
    if state:
        print(f"ANSWER_STATE: {state}")


def _run_context(args):
    budget_s = getattr(args, "_budget_s", None)
    source = getattr(args, "_budget_source", None)
    clock = getattr(args, "_clock", None)
    if budget_s is None:
        budget_s, source = _compbudget.resolve_budget(getattr(args, "budget", None))
    if clock is None:
        clock = _compbudget.Clock(budget_s)
    portal_arg = getattr(args, "portal_src", None)
    portal_src = Path(portal_arg).resolve() if portal_arg else None
    return scan(portal_src, getattr(args, "cursor", None), clock), budget_s, source, clock


def _print_budget(result: ScanResult, args, budget_s: float, source: str,
                  clock: _compbudget.Clock):
    if result.budget_reached:
        print(_compbudget.budget_reached_line(
            budget_s, source, result.scanned_files + len(result.skipped_files), result.total_files,
            "file", f"comp-cache {args.command}", result.last_cursor))
    else:
        print(_compbudget.within_budget_line(
            result.scanned_files + len(result.skipped_files), result.total_files, "file",
            budget_s, source, clock.elapsed()))


# ---- commands ------------------------------------------------------------------------------

def cmd_map(args):
    result, budget_s, source, clock = _run_context(args)
    entries = result.entries
    print(f"REACT QUERY CACHE MAP -- {_denominator_line(result)}")
    _print_answer_state(_base_answer_state(result))
    distinct = {str(e.key_parts) for e in entries}
    print(f"  {len(entries)} entries -> {len(distinct)} distinct keys "
          f"across {len({e.file_path for e in entries})} files")
    print()
    _print_skipped(result.skipped_files)
    _print_unparseable(result.unparseable)

    by_key: dict[str, list[CacheEntry]] = {}
    for e in entries:
        by_key.setdefault(str(e.key_parts), []).append(e)

    for key, group in sorted(by_key.items()):
        files = sorted({e.file_path for e in group})
        types = sorted({e.response_type for e in group if e.response_type})
        fns = sorted({e.fetch_function for e in group})
        shared = " ** SHARED **" if len(files) > 1 else ""
        mismatch = " ** TYPE MISMATCH **" if len(types) > 1 else ""
        print(f"  {key}{shared}{mismatch}")
        print(f"    files: {', '.join(files)}")
        if types:
            print(f"    types: {', '.join(types)}")
        print(f"    fns:   {', '.join(fns)}")
        print()
    _print_budget(result, args, budget_s, source, clock)


def cmd_collisions(args):
    result, budget_s, source, clock = _run_context(args)
    entries = result.entries
    state = _base_answer_state(result)
    print(f"CACHE KEY COLLISIONS -- {_denominator_line(result)}")
    _print_answer_state(state)
    print()
    _print_skipped(result.skipped_files)
    _print_unparseable(result.unparseable)

    by_key: dict[str, list[CacheEntry]] = {}
    for e in entries:
        by_key.setdefault(str(e.key_parts), []).append(e)
    # a collision = same key across >1 distinct FILE (not stem)
    shared = {k: v for k, v in by_key.items() if len({e.file_path for e in v}) > 1}

    if state == "PARTIAL_OR_BLIND":
        print("COLLISION VERDICT: INCOMPLETE -- skipped/unparseable source means this prefix is not clean.")
        _print_budget(result, args, budget_s, source, clock)
        return

    if state in {"SUBJECT_ABSENT_FROM_CORPUS", "NOT_APPLICABLE"}:
        print("COLLISION VERDICT: NOT EVALUATED -- no clean collision claim is made.")
        _print_budget(result, args, budget_s, source, clock)
        return

    if not shared:
        print("No cross-file cache-key collisions among the captured call-sites.")
        print("  (The completed denominator above is the scope of this execution-only result.)")
        _print_budget(result, args, budget_s, source, clock)
        return

    mismatches = [k for k, v in shared.items() if len({e.response_type for e in v if e.response_type}) > 1]
    print(f"{len(shared)} shared key(s); {len(mismatches)} with a TYPE MISMATCH (the bug-class).\n")
    for key, group in sorted(shared.items()):
        types = {e.response_type for e in group if e.response_type}
        warn = " !! TYPE MISMATCH !!" if len(types) > 1 else ""
        print(f"  Key: {key}{warn}")
        for e in group:
            t = f" <{e.response_type}>" if e.response_type else ""
            print(f"    {e.file_path}:{e.line_number}  {e.fetch_function}(){t}")
        if len(types) > 1:
            print(f"    WARNING: different response types share this key: {', '.join(sorted(types))}")
        print()
    _print_budget(result, args, budget_s, source, clock)


def cmd_key(args):
    result, budget_s, source, clock = _run_context(args)
    entries = result.entries
    q = args.query.lower()
    matches = [e for e in entries
               if q in e.key_str.lower() or q in e.fetch_function.lower()
               or any(q in p.lower() for p in e.key_parts)]
    print(f"CACHE KEYS matching '{args.query}' ({len(matches)} hit(s)) -- "
          f"{_denominator_line(result)}")
    state = _base_answer_state(result)
    if state is None and not matches:
        state = "PRESENT_WITH_ZERO_RESULTS"
    _print_answer_state(state)
    print()
    _print_skipped(result.skipped_files)
    _print_unparseable(result.unparseable)
    for e in matches:
        t = f" <{e.response_type}>" if e.response_type else ""
        print(f"  {e.file_path}:{e.line_number}")
        print(f"    key: [{e.key_str}]")
        print(f"    fn:  {e.fetch_function}(){t}")
        print()
    _print_budget(result, args, budget_s, source, clock)


def main():
    parser = argparse.ArgumentParser(
        prog="comp-cache",
        description="React Query cache key analysis across portal/src (useQuery).",
        epilog=("Rule T carrier: --budget SECONDS (flag > COMP_BUDGET_S > default 90); "
                "--budget 0 is unbounded. --cursor resumes after the stated source-file unit."),
    )
    parser.add_argument("--budget", type=float, default=None,
                        help="Rule T work ceiling in seconds (0 = unbounded)")
    parser.add_argument("--cursor", default=None,
                        help="Resume after this deterministic portal source-file cursor")
    parser.add_argument("--portal-src", default=None,
                        help="Read-only source root (defaults to portal/src; useful for a fixture)")
    sub = parser.add_subparsers(dest="command")
    def add_common(command_parser):
        command_parser.add_argument("--budget", type=float, default=argparse.SUPPRESS,
                                    help="Rule T work ceiling in seconds (0 = unbounded)")
        command_parser.add_argument("--cursor", default=argparse.SUPPRESS,
                                    help="Resume after this deterministic portal source-file cursor")
        command_parser.add_argument("--portal-src", default=argparse.SUPPRESS,
                                    help="Read-only source root (defaults to portal/src; useful for a fixture)")

    pm = sub.add_parser("map", help="All cache keys -> files (+ capture denominator)")
    pc = sub.add_parser("collisions", help="Keys shared across files, typed")
    pk = sub.add_parser("key", help="Find uses of a cache-key substring")
    add_common(pm)
    add_common(pc)
    add_common(pk)
    pk.add_argument("query", help="Key substring to search")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)
    try:
        args._budget_s, args._budget_source = _compbudget.resolve_budget(args.budget)
        args._clock = _compbudget.Clock(args._budget_s)
        {"map": cmd_map, "collisions": cmd_collisions, "key": cmd_key}[args.command](args)
    except ValueError as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
