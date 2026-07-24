"""comp-residue -- THE RESIDUE DETECTOR (NFRA_TOOLSTACK; ARCHETYPAL_LEARNING_LOOP shape #1).

WHAT IT ANSWERS: "what structure exists in a SOURCE that NOTHING downstream references?"
-- i.e. the surface the estate's enumerators DO NOT TRAVERSE. That is the deterministic
detector for the ORTHOGONAL-SHAPE class: a source grows a new KIND of thing, no consumer
walks it, and every presence-based parity check keeps passing because the strings it greps
for never left.

THE STRUCTURE-vs-DATA LAW (this is the whole design):
    a MAPPING KEY is STRUCTURE  -> a new key path is a NEW AXIS      -> RESIDUE / inference gate
    a LIST MEMBER  is DATA      -> new members are NEW ROWS          -> Route A, NOT residue
  So `roles:` gaining a 15th entry is NOT residue (rows on a known axis). `dynamic_rails:`
  appearing as a new section IS residue (an axis nobody enumerates). The row SCHEMA -- the
  union of keys across list members -- IS structure, so a new FIELD on existing rows is an
  axis too, and is reported as `<path>[].<field>`.

>> DECLARED BLIND SPOT, LOUD, AND IT BIASES ONE WAY ONLY:
   a key NAME appearing in a consumer file is EVIDENCE of reference, never PROOF of
   traversal -- it could be a comment, a docstring, or an unrelated string. This tool
   therefore counts a key as COVERED on any mention, and reports residue ONLY for keys with
   ZERO mentions anywhere. CONSEQUENCE: it UNDER-REPORTS residue (a key mentioned but never
   walked reads as covered) and does NOT over-report. A residue finding here is high-
   confidence; a clean run is NOT proof of full traversal. <<

CONTRACTED EXITS (comp-output-contracts):
    0  PASS     no residue over the established denominator
    2  VERDICT  RESIDUE FOUND -- an estate verdict, not a tool failure
    3  REFUSE   coverage refusal: the source or the consumer set could not be established,
                so NOTHING was compared and nothing is concluded
    1  FAIL     tool error

Read-only. Deterministic. ASCII-only.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone

try:
    import yaml
except Exception:  # pragma: no cover - environment guard
    yaml = None

# graph -> modules -> org -> <workspace root>. Four levels; a short count silently resolves
# every relative consumer spec under org/ and REFUSEs on real directories.
WS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
PIN_STORE = os.path.join(WS, "org", "modules", "graph", "residue_pins.json")

RC_PASS, RC_FAIL, RC_VERDICT, RC_REFUSE = 0, 1, 2, 3

SKIP_DIR_PARTS = (
    os.sep + "__pycache__",
    os.sep + ".git",
    os.sep + "node_modules",
    os.sep + ".ruff_cache",
)


def _utc_now() -> str:
    """Z-explicit. A timestamp without an explicit Z is ambiguous on this host (UTC-4)."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_source(path: str):
    """Parse a YAML/JSON source. Returns (obj, error_or_None)."""
    if not os.path.isfile(path):
        return None, "source not found: %s" % path
    try:
        with open(path, "r", encoding="utf-8") as fh:
            text = fh.read()
    except Exception as exc:
        return None, "unreadable: %s (%s)" % (path, exc)
    if path.endswith((".json",)):
        try:
            return json.loads(text), None
        except Exception as exc:
            return None, "json parse failed: %s" % exc
    if yaml is None:
        return None, "pyyaml unavailable; cannot parse %s" % path
    try:
        return yaml.safe_load(text), None
    except Exception as exc:
        return None, "yaml parse failed: %s" % exc


def surface(node, prefix: str = "", depth: int = 0, max_depth: int = 4) -> set:
    """STRUCTURAL key-paths only.

    dict keys      -> structure (a key path IS an axis)
    list members   -> DATA; we do NOT emit per-member paths
    list row-schema-> structure: the UNION of member keys, emitted once as `<p>[].<key>`
    """
    out = set()
    if isinstance(node, dict):
        for key, val in node.items():
            path = ("%s.%s" % (prefix, key)) if prefix else str(key)
            out.add(path)
            if depth + 1 < max_depth:
                out |= surface(val, path, depth + 1, max_depth)
    elif isinstance(node, list):
        row_keys = set()
        for member in node:
            if isinstance(member, dict):
                row_keys |= set(member.keys())
        for key in sorted(row_keys):
            path = "%s[].%s" % (prefix, key) if prefix else "[].%s" % key
            out.add(path)
    return out


def _iter_consumer_files(specs):
    """Expand file/dir specs into a concrete file list. Returns (files, unresolved)."""
    files, unresolved = [], []
    for spec in specs:
        target = spec if os.path.isabs(spec) else os.path.join(WS, spec)
        if os.path.isfile(target):
            files.append(target)
        elif os.path.isdir(target):
            for root, dirs, names in os.walk(target):
                if any(part in root for part in SKIP_DIR_PARTS):
                    continue
                dirs[:] = [d for d in dirs if d not in ("__pycache__", ".git", "node_modules")]
                for name in names:
                    if name.endswith((".py", ".yaml", ".yml", ".json", ".md", ".sh", ".mjs", ".ts", ".tsx")):
                        files.append(os.path.join(root, name))
        else:
            unresolved.append(spec)
    return sorted(set(files)), unresolved


DOC_EXTS = (".md", ".rst", ".txt")


def consumer_text(files):
    """Split consumer text into CODE and DOC blobs.

    >> WHY THE SPLIT IS STRUCTURAL, NOT COSMETIC (found by this tool contradicting a prior
       measurement, 2026-07-24): a document ABOUT an unwalked axis MENTIONS that axis, so a
       naive any-mention check reads it as covered. Two docs written into infra/system/ontology/
       to DESCRIBE the missing `dynamic_rails` axis made `dynamic_rails` read as REFERENCED --
       residue fell 77 -> 44 and the true orphan axes vanished from the report.
       WRITING ABOUT A GAP CLOSES IT IN THE INSTRUMENT, NOT IN THE ESTATE. <<

    So prose is never counted as traversal. DOC-only mentions get their own tier.
    """
    code_blob, doc_blob, read_code, read_doc = [], [], 0, 0
    for path in files:
        try:
            with open(path, "r", encoding="utf-8", errors="replace") as fh:
                text = fh.read()
        except Exception:
            continue
        if path.lower().endswith(DOC_EXTS):
            doc_blob.append(text)
            read_doc += 1
        else:
            code_blob.append(text)
            read_code += 1
    return "\n".join(code_blob), "\n".join(doc_blob), read_code, read_doc


def _mentions(path, blob) -> bool:
    leaf = path.split(".")[-1].replace("[]", "")
    if not leaf:
        return False
    return (path in blob) or (leaf in blob)


def residue(paths, code_blob, doc_blob):
    """Three tiers. A path is COVERED only by a CODE mention; prose is NOT traversal.

    returns (unreferenced, doc_only)
      unreferenced -> mentioned by NOTHING          (residue proper)
      doc_only     -> mentioned ONLY in prose       (documented, not traversed)

    Still deliberately permissive WITHIN code (any mention counts), so it under-reports
    residue and does not over-report. See the module docstring's DECLARED BLIND SPOT.
    """
    unreferenced, doc_only = [], []
    for path in sorted(paths):
        if _mentions(path, code_blob):
            continue
        if _mentions(path, doc_blob):
            doc_only.append(path)
        else:
            unreferenced.append(path)
    return unreferenced, doc_only


def classify_residue(unreferenced):
    """Split residue by MATERIALITY -- a deterministic discrimination that matters a lot.

    ORPHAN AXIS      : this path AND every ancestor is unreferenced. NOTHING downstream knows
                       this section exists at all. This is the shape-#1 signal.
    UNREFERENCED MEMBER: an ANCESTOR is referenced, this leaf is not. The section is known;
                       its members simply are not enumerated downstream -- which is very often
                       CORRECT (the estate's `cite, do not copy` discipline means /system names
                       "14 Roles" without listing them).

    >> RESIDUE IS NOT A DEFECT. An orphan axis is a strong candidate; an unreferenced member is
       usually by design. Determinism can make THIS split; it cannot judge materiality. <<
    """
    unref = set(unreferenced)
    orphans, members = [], []
    for path in unreferenced:
        parts = path.replace("[]", "").split(".")
        ancestor_referenced = False
        for i in range(1, len(parts)):
            ancestor = ".".join(parts[:i])
            if ancestor not in unref:
                ancestor_referenced = True
                break
        (members if ancestor_referenced else orphans).append(path)
    return orphans, members


def read_head(obj, head_path: str):
    """Pull the version head out of the source (dotted path). Returns str or None."""
    cur = obj
    for part in head_path.split("."):
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        else:
            return None
    return str(cur) if cur is not None else None


def _load_pins() -> dict:
    if not os.path.isfile(PIN_STORE):
        return {}
    try:
        with open(PIN_STORE, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except Exception:
        return {}


def _save_pins(pins: dict) -> None:
    with open(PIN_STORE, "w", encoding="utf-8") as fh:
        json.dump(pins, fh, indent=2, sort_keys=True)
        fh.write("\n")


def _rel(path: str) -> str:
    try:
        return os.path.relpath(path, WS).replace(os.sep, "/")
    except Exception:
        return path


def cmd_surface(args) -> int:
    obj, err = load_source(args.source)
    if err:
        print("REFUSE: %s" % err)
        print("  NOTHING was compared, so nothing is concluded.")
        return RC_REFUSE
    paths = surface(obj, max_depth=args.max_depth)
    head = read_head(obj, args.head_path) if isinstance(obj, dict) else None
    print("comp-residue surface")
    print("  SOURCE:      %s" % _rel(args.source))
    print("  HEAD:        %s" % (head or "UNKNOWN"))
    print("  DENOMINATOR: %d structural paths (max_depth=%d)" % (len(paths), args.max_depth))
    print("  STRUCTURE = dict keys + list ROW SCHEMA. List MEMBERS are DATA (rows), not axes.")
    for path in sorted(paths):
        print("    %s" % path)
    return RC_PASS


def cmd_check(args) -> int:
    obj, err = load_source(args.source)
    if err:
        print("REFUSE: %s" % err)
        print("  NOTHING was compared, so nothing is concluded.")
        return RC_REFUSE

    files, unresolved = _iter_consumer_files(args.consumers)
    if not files:
        print("REFUSE: no consumer files resolved from %r" % (args.consumers,))
        print("  A residue verdict requires an established consumer set. NOTHING was compared.")
        if unresolved:
            print("  unresolved specs: %s" % ", ".join(unresolved))
        return RC_REFUSE

    paths = surface(obj, max_depth=args.max_depth)
    code_blob, doc_blob, read_code, read_doc = consumer_text(files)
    unreferenced, doc_only = residue(paths, code_blob, doc_blob)
    head = read_head(obj, args.head_path) if isinstance(obj, dict) else None

    print("comp-residue check -- structural surface that NO consumer references")
    print("  SOURCE:      %s" % _rel(args.source))
    print("  HEAD:        %s" % (head or "UNKNOWN (no version head at %s)" % args.head_path))
    print("  DENOMINATOR: %d structural paths x %d CODE + %d DOC consumer files (%d specs, %d unresolved)"
          % (len(paths), read_code, read_doc, len(args.consumers), len(unresolved)))
    if unresolved:
        print("  UNRESOLVED consumer specs (NOT counted as covering anything): %s" % ", ".join(unresolved))
    print("  METHOD:      COVERED requires a CODE mention. PROSE IS NOT TRAVERSAL -- a doc ABOUT")
    print("               a missing axis mentions it, which would launder the gap (measured: doc")
    print("               contamination cut residue 77 -> 44 and hid every true orphan axis).")
    print("               Within code, ANY mention counts -> UNDER-reports residue, never over.")
    print("  " + "-" * 68)

    if doc_only:
        print("  DOCUMENTED-BUT-NOT-TRAVERSED (%d): prose mentions these; no code does." % len(doc_only))
        for path in doc_only:
            print("    doc-only     %s" % path)
        print("")

    if not unreferenced:
        print("PASS: 0 residue -- every one of the %d structural paths is mentioned by at least one" % len(paths))
        print("      CODE consumer. NOT a proof of traversal (see METHOD).")
        return RC_PASS

    orphans, members = classify_residue(unreferenced)
    print("VERDICT: RESIDUE FOUND -- %d of %d structural paths are referenced by NOTHING."
          % (len(unreferenced), len(paths)))
    print("  SPLIT: %d ORPHAN AXES (high signal) / %d unreferenced MEMBERS (usually by design)"
          % (len(orphans), len(members)))
    print("  >> RESIDUE IS NOT A DEFECT. Determinism LOCATES candidates; it cannot judge")
    print("     materiality -- that is the INFERENCE GATE (ARCHETYPAL_LEARNING_LOOP plane 3).")
    print("")
    print("  ORPHAN AXES -- this path AND every ancestor is unreferenced. NOTHING downstream")
    print("  knows this section exists. These are the shape-#1 candidates:")
    if orphans:
        for path in orphans:
            print("    ORPHAN AXIS  %s" % path)
    else:
        print("    (none)")
    print("")
    print("  UNREFERENCED MEMBERS -- an ancestor IS referenced; the leaf is not. Frequently")
    print("  CORRECT under the estate's `cite, do not copy` discipline (e.g. /system names")
    print("  \"14 Roles\" without enumerating them). Review, do not assume defect:")
    if members:
        for path in members:
            print("    member       %s" % path)
    else:
        print("    (none)")
    return RC_VERDICT


def cmd_pin(args) -> int:
    obj, err = load_source(args.source)
    if err:
        print("REFUSE: %s" % err)
        return RC_REFUSE
    paths = sorted(surface(obj, max_depth=args.max_depth))
    head = read_head(obj, args.head_path) if isinstance(obj, dict) else None
    pins = _load_pins()
    key = _rel(args.source)
    pins[key] = {
        "version_head": head,
        "head_path": args.head_path,
        "max_depth": args.max_depth,
        "acknowledged_surface": paths,
        "pinned_at": _utc_now(),
        "pinned_by": args.by,
    }
    _save_pins(pins)
    print("comp-residue pin -- acknowledged surface recorded")
    print("  SOURCE:      %s" % key)
    print("  HEAD:        %s" % (head or "UNKNOWN"))
    print("  ACKNOWLEDGED: %d structural paths" % len(paths))
    print("  PINNED_AT:   %s  BY: %s" % (pins[key]["pinned_at"], args.by))
    print("  Future `comp-residue drift` reports anything NOT in this set.")
    return RC_PASS


def cmd_drift(args) -> int:
    obj, err = load_source(args.source)
    if err:
        print("REFUSE: %s" % err)
        return RC_REFUSE
    pins = _load_pins()
    key = _rel(args.source)
    pin = pins.get(key)
    if not pin:
        print("REFUSE: no pin recorded for %s -- run `comp-residue pin` first." % key)
        print("  NOTHING was compared, so nothing is concluded.")
        return RC_REFUSE

    now_paths = surface(obj, max_depth=pin.get("max_depth", args.max_depth))
    ack = set(pin.get("acknowledged_surface", []))
    added = sorted(now_paths - ack)
    removed = sorted(ack - now_paths)
    head_now = read_head(obj, pin.get("head_path", args.head_path)) if isinstance(obj, dict) else None
    head_pin = pin.get("version_head")

    print("comp-residue drift -- surface vs the acknowledged pin")
    print("  SOURCE:      %s" % key)
    print("  HEAD:        pin=%s  now=%s  %s"
          % (head_pin, head_now, "MOVED" if head_now != head_pin else "unchanged"))
    print("  DENOMINATOR: %d acknowledged / %d current structural paths" % (len(ack), len(now_paths)))
    print("  PINNED_AT:   %s" % pin.get("pinned_at"))
    print("  " + "-" * 68)

    if not added and not removed:
        if head_now != head_pin:
            print("VERDICT: HEAD MOVED (%s -> %s) with ZERO structural delta." % (head_pin, head_now))
            print("  This is EITHER a pure data/content change (rows on known axes -- benign)")
            print("  OR a change no structural check can see. Determinism CANNOT distinguish these.")
            print("  Re-pin to acknowledge, or route to the INFERENCE GATE if the head moved for a")
            print("  reason the surface does not show.")
            return RC_VERDICT
        print("PASS: surface unchanged and head unchanged (%s)." % head_pin)
        return RC_PASS

    print("VERDICT: SURFACE DRIFT -- %d added, %d removed since the pin." % (len(added), len(removed)))
    for path in added:
        print("    ADDED    %s   <-- unacknowledged axis" % path)
    for path in removed:
        print("    REMOVED  %s" % path)
    print("  ADDED paths are candidate NEW AXES. Acknowledge with `comp-residue pin` only after")
    print("  a consumer actually traverses them -- pinning first would launder the gap.")
    return RC_VERDICT


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="comp-residue",
        description="structural residue: the surface of a source that NOTHING references/traverses",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    def common(sp):
        sp.add_argument("source", help="path to a YAML/JSON source of truth")
        sp.add_argument("--head-path", default="meta.version",
                        help="dotted path to the version head (default: meta.version)")
        sp.add_argument("--max-depth", type=int, default=4, help="structural depth (default 4)")

    sp = sub.add_parser("surface", help="enumerate the structural surface + denominator")
    common(sp)
    sp.set_defaults(func=cmd_surface)

    sp = sub.add_parser("check", help="residue = surface NOTHING references (the main mode)")
    common(sp)
    sp.add_argument("--consumers", nargs="+", required=True,
                    help="consumer files/dirs that SHOULD reference the source")
    sp.set_defaults(func=cmd_check)

    sp = sub.add_parser("pin", help="record the acknowledged surface + head")
    common(sp)
    sp.add_argument("--by", default=os.environ.get("AGENT_SERIAL", "unknown"), help="who acknowledged")
    sp.set_defaults(func=cmd_pin)

    sp = sub.add_parser("drift", help="surface vs pin: unacknowledged axes since the pin")
    common(sp)
    sp.set_defaults(func=cmd_drift)
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return args.func(args)
    except Exception as exc:  # tool error, NOT an estate verdict
        print("FAIL: comp-residue internal error: %s" % exc)
        return RC_FAIL


if __name__ == "__main__":
    sys.exit(main())
