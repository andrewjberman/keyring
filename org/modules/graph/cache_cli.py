#!/usr/bin/env python3
"""
comp-cache -- React Query cache key analysis across components.

Detects:
  - Cache key collisions (same key used by multiple components)
  - Type mismatches (same key, different response types)
  - Shared cache dependencies (components that invalidate each other)

Usage:
    comp-cache map          # all cache keys -> components
    comp-cache collisions   # keys shared by multiple components with type info
    comp-cache key advisor-intelligence  # find all uses of a cache key substring

Authoritative source: portal/src/pages/**/*.tsx (useQuery hooks)
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_WORKSPACE = _THIS_DIR.parent.parent.parent

sys.path.insert(0, str(_WORKSPACE))


@dataclass
class CacheEntry:
    """A React Query cache key usage."""
    query_key: str           # the key array as string
    key_parts: list[str]     # individual key parts
    response_type: str       # generic type param
    fetch_function: str      # queryFn target
    component: str           # component that uses it
    file_path: str           # source file
    line_number: int = 0


def _extract_cache_keys(workspace_root: Path) -> list[CacheEntry]:
    """Extract all useQuery cache keys from portal components."""
    entries: list[CacheEntry] = []
    pages_dir = workspace_root / "portal" / "src" / "pages"
    if not pages_dir.exists():
        return entries

    # Pattern: useQuery<ResponseType>({ queryKey: ['key1', 'key2', ...], queryFn: () => fetchFn(...)
    use_query_pattern = re.compile(
        r'useQuery'
        r'(?:<(\w+)>)?'                    # optional <ResponseType>
        r'\s*\(\s*\{'
        r'[^}]*?'                          # non-greedy content
        r'queryKey\s*:\s*\[([^\]]+)\]'     # queryKey: [...]
        r'[^}]*?'                          # non-greedy content
        r'queryFn\s*:\s*\(\)\s*=>\s*(\w+)', # queryFn: () => fetchFn
        re.DOTALL
    )

    for tsx_file in sorted(pages_dir.rglob("*.tsx")):
        try:
            content = tsx_file.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue

        rel_path = str(tsx_file.relative_to(workspace_root)).replace("\\", "/")
        component = tsx_file.stem

        for m in use_query_pattern.finditer(content):
            resp_type = m.group(1) or ""
            key_str = m.group(2).strip()
            fetch_fn = m.group(3)
            line_no = content[:m.start()].count('\n') + 1

            # Parse key parts (remove quotes, keep variable names)
            key_parts = []
            for part in re.findall(r"'([^']+)'|\"([^\"]+)\"|(\w+)", key_str):
                val = part[0] or part[1] or part[2]
                if val:
                    key_parts.append(val)

            entries.append(CacheEntry(
                query_key=key_str,
                key_parts=key_parts,
                response_type=resp_type,
                fetch_function=fetch_fn,
                component=component,
                file_path=rel_path,
                line_number=line_no,
            ))

    return entries


def cmd_map(args):
    entries = _extract_cache_keys(_WORKSPACE)
    if not entries:
        print("No useQuery cache keys found.")
        return

    # Group by static key prefix (first N string literal parts)
    by_key: dict[str, list[CacheEntry]] = {}
    for e in entries:
        # Use string literal parts only for grouping
        static_parts = [p for p in e.key_parts if not p[0].islower() or "'" in e.query_key.split(p)[0][-5:]]
        key = str(e.key_parts)
        by_key.setdefault(key, []).append(e)

    print(f"REACT QUERY CACHE MAP ({len(entries)} keys across {len(set(e.component for e in entries))} components)")
    print()

    for key, group in sorted(by_key.items()):
        components = sorted(set(e.component for e in group))
        types = sorted(set(e.response_type for e in group if e.response_type))
        fns = sorted(set(e.fetch_function for e in group))
        collision = " ** SHARED **" if len(components) > 1 else ""
        type_mismatch = " ** TYPE MISMATCH **" if len(types) > 1 else ""

        print(f"  {key}{collision}{type_mismatch}")
        print(f"    components: {', '.join(components)}")
        if types:
            print(f"    types:      {', '.join(types)}")
        print(f"    fetches:    {', '.join(fns)}")
        print()


def cmd_collisions(args):
    entries = _extract_cache_keys(_WORKSPACE)

    # Group by key
    by_key: dict[str, list[CacheEntry]] = {}
    for e in entries:
        key = str(e.key_parts)
        by_key.setdefault(key, []).append(e)

    # Filter to shared keys only
    shared = {k: v for k, v in by_key.items() if len(set(e.component for e in v)) > 1}

    if not shared:
        print("No cache key collisions detected. Each key is used by exactly one component.")
        return

    print(f"CACHE KEY COLLISIONS ({len(shared)} shared keys)")
    print()

    for key, group in sorted(shared.items()):
        types = set(e.response_type for e in group if e.response_type)
        type_warning = " !! TYPE MISMATCH !!" if len(types) > 1 else ""
        print(f"  Key: {key}{type_warning}")
        for e in group:
            type_str = f" <{e.response_type}>" if e.response_type else ""
            print(f"    {e.component} L{e.line_number}: {e.fetch_function}(){type_str}")
            print(f"      {e.file_path}")
        if len(types) > 1:
            print(f"    WARNING: Different response types share this cache key!")
            print(f"    Types: {', '.join(sorted(types))}")
        print()


def cmd_key(args):
    entries = _extract_cache_keys(_WORKSPACE)
    query = args.query.lower()

    matches = [e for e in entries
               if query in e.query_key.lower()
               or query in e.fetch_function.lower()
               or any(query in p.lower() for p in e.key_parts)]

    if not matches:
        print(f"No cache keys matching: {args.query}")
        return

    print(f"CACHE KEYS matching '{args.query}' ({len(matches)} hits)")
    print()
    for e in matches:
        type_str = f" <{e.response_type}>" if e.response_type else ""
        print(f"  {e.component} L{e.line_number}")
        print(f"    key: [{e.query_key}]")
        print(f"    fn:  {e.fetch_function}(){type_str}")
        print(f"    file: {e.file_path}")
        print()


def main():
    parser = argparse.ArgumentParser(
        prog='comp-cache',
        description='React Query cache key analysis across components.',
    )
    sub = parser.add_subparsers(dest='command')

    sub.add_parser('map', help='All cache keys -> components')
    sub.add_parser('collisions', help='Keys shared by multiple components')

    p_key = sub.add_parser('key', help='Find all uses of a cache key substring')
    p_key.add_argument('query', help='Key substring to search')

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)

    commands = {
        'map': cmd_map,
        'collisions': cmd_collisions,
        'key': cmd_key,
    }
    commands[args.command](args)


if __name__ == '__main__':
    main()
