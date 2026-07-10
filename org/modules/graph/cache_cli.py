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
  queryKeys; this tool audits useQuery only, and SAYS SO in the denominator line.
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


def extract(portal_src: Path | None = None):
    """(entries, unparseable, total_call_sites) over ALL of portal/src (.ts + .tsx).

    portal_src defaults to the module global _PORTAL_SRC RESOLVED AT CALL TIME (not bound at
    def time), so a caller/test that reassigns _PORTAL_SRC is honored.
    """
    portal_src = portal_src if portal_src is not None else _PORTAL_SRC
    entries: list[CacheEntry] = []
    unparseable: list[Unparseable] = []
    total = 0
    if not portal_src.exists():
        return entries, unparseable, total
    for f in sorted(list(portal_src.rglob("*.tsx")) + list(portal_src.rglob("*.ts"))):
        try:
            content = f.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        if "useQuery" not in content:
            continue
        rel = str(f.relative_to(_WORKSPACE)).replace("\\", "/")
        total += _extract_from_content(_blank_comments(content), rel, entries, unparseable)
    return entries, unparseable, total


def _denominator_line(entries, unparseable, total) -> str:
    return (f"captured {len(entries)} of {total} useQuery call-site(s); "
            f"{len(unparseable)} unparseable "
            f"(useQueries / useInfiniteQuery are NOT audited by this tool)")


def _print_unparseable(unparseable):
    if unparseable:
        print("  UNPARSEABLE (listed, not silently dropped):")
        for u in unparseable:
            print(f"    {u.file_path}:{u.line_number} -- {u.reason}")
        print()


# ---- commands ------------------------------------------------------------------------------

def cmd_map(args):
    entries, unparseable, total = extract()
    print(f"REACT QUERY CACHE MAP -- {_denominator_line(entries, unparseable, total)}")
    distinct = {str(e.key_parts) for e in entries}
    print(f"  {len(entries)} entries -> {len(distinct)} distinct keys "
          f"across {len({e.file_path for e in entries})} files")
    print()
    _print_unparseable(unparseable)

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


def cmd_collisions(args):
    entries, unparseable, total = extract()
    print(f"CACHE KEY COLLISIONS -- {_denominator_line(entries, unparseable, total)}")
    print()
    _print_unparseable(unparseable)

    by_key: dict[str, list[CacheEntry]] = {}
    for e in entries:
        by_key.setdefault(str(e.key_parts), []).append(e)
    # a collision = same key across >1 distinct FILE (not stem)
    shared = {k: v for k, v in by_key.items() if len({e.file_path for e in v}) > 1}

    if not shared:
        print("No cross-file cache-key collisions among the captured call-sites.")
        print("  (NOT 'no collisions': see the denominator above -- unparseable/uncaptured")
        print("   call-sites are not asserted collision-free.)")
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


def cmd_key(args):
    entries, unparseable, total = extract()
    q = args.query.lower()
    matches = [e for e in entries
               if q in e.key_str.lower() or q in e.fetch_function.lower()
               or any(q in p.lower() for p in e.key_parts)]
    print(f"CACHE KEYS matching '{args.query}' ({len(matches)} hit(s)) -- "
          f"{_denominator_line(entries, unparseable, total)}")
    print()
    for e in matches:
        t = f" <{e.response_type}>" if e.response_type else ""
        print(f"  {e.file_path}:{e.line_number}")
        print(f"    key: [{e.key_str}]")
        print(f"    fn:  {e.fetch_function}(){t}")
        print()


def main():
    parser = argparse.ArgumentParser(
        prog="comp-cache",
        description="React Query cache key analysis across portal/src (useQuery).",
    )
    sub = parser.add_subparsers(dest="command")
    sub.add_parser("map", help="All cache keys -> files (+ capture denominator)")
    sub.add_parser("collisions", help="Keys shared across files, typed")
    pk = sub.add_parser("key", help="Find uses of a cache-key substring")
    pk.add_argument("query", help="Key substring to search")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)
    {"map": cmd_map, "collisions": cmd_collisions, "key": cmd_key}[args.command](args)


if __name__ == "__main__":
    main()
