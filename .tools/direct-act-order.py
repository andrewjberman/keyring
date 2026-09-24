#!/usr/bin/env python3
"""direct-act-order.py -- mints a task order for a co-signed DIRECT act.

Closes AMGT_RESAPP-Z-W34-S2: a co-signed direct act (an act spawned off a signed never-widen pair
with an inline worker face and no companion task-order file) is invisible to the owned-paths lane
gate, because that gate reads grants from task-order files only. This tool mints the missing order
from the signed pair, bounded to the paths the pair names, and REFUSES to leave behind an order the
L6 gate (.tools/to-pipeline-gate.py) would itself refuse.

THE SINGLE GRANT SOURCE STANDS: this tool never widens .tools/owned-paths-validate.py; it produces
the one artifact that gate already reads (a task-order file), so the mechanical gate needs no new
code and no second grant source.

Verbs: `mint` and `--self-test`. Plain ASCII output only (OK:/REFUSED:/MINTED:/FAIL:/RESULT:).
stdlib only. Python 3.9-compatible.
"""
import argparse
import glob
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys

PREFLIGHT_TOOLS = ("comp-schedule", "comp-iam", "comp-adversary")

PREFLIGHT_LINE_RE = re.compile(r"^(comp-schedule|comp-iam|comp-adversary):\s*(.*)$", re.M)
HEADING_RE = re.compile(r"^#+.*$", re.M)
CRITERION_BLOCK_RE = re.compile(r"<criterion\b([^>]*)>(.*?)</criterion>", re.S)
CRITERION_SELF_RE = re.compile(r"<criterion\b([^>]*)/>")
ATTR_RE = re.compile(r'(\w+)\s*=\s*"([^"]*)"')

WORKER_FACE_MARKER = (
    "<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context "
    "===================== -->"
)
RECORD_FACE_MARKER = (
    "<!-- ===================== RECORD FACE -- never travels to a worker "
    "===================== -->"
)


# ---------------------------------------------------------------------------
# PURE FUNCTIONS -- self-tested directly, no I/O.
# ---------------------------------------------------------------------------

def validate_path_grammar(path):
    """(ok, reason) -- the <paths> grammar the two gates read: no leading slash, no '..'
    segment, glob metacharacters limited to *?[]; anything else (a brace, a paren) is a
    'bracket that is not a glob'."""
    if not path:
        return False, "empty path"
    if path.startswith("/"):
        return False, "leading slash"
    if "\\" in path:
        return False, "backslash, not a repo-relative path"
    parts = path.split("/")
    if ".." in parts:
        return False, "parent traversal (..)"
    for ch in path:
        if ch.isalnum() or ch in "_-./":
            continue
        if ch in "*?[]":
            continue
        return False, "bracket that is not a glob (%r)" % ch
    return True, ""


def path_named_by_either(path, coo_text, cto_text):
    return (path in (coo_text or "")) or (path in (cto_text or ""))


def section_heading_present(text, section):
    for m in HEADING_RE.finditer(text or ""):
        if section in m.group(0):
            return True
    return False


def extract_section(text, section):
    """The first heading line containing `section`, through the next heading of the same-or-
    fewer leading '#' characters (or end of text). None if no such heading exists."""
    lines = (text or "").splitlines()
    start = None
    start_level = None
    for i, line in enumerate(lines):
        hm = re.match(r"^#+", line)
        if hm and section in line:
            start = i
            start_level = len(hm.group(0))
            break
    if start is None:
        return None
    end = len(lines)
    for j in range(start + 1, len(lines)):
        hm = re.match(r"^#+", lines[j])
        if hm and len(hm.group(0)) <= start_level:
            end = j
            break
    return "\n".join(lines[start:end])


def issuer_is_coo(serial):
    return bool(serial) and serial.startswith("2.0.0_SA_COO")


def check_preflight_text(text):
    """[] of violation strings -- all three PREFLIGHT_TOOLS present, each 'RUN -- (' with a
    digit somewhere on its line, or 'DECLARED-NOT-APPLICABLE' followed by a non-empty reason."""
    found = {}
    for m in PREFLIGHT_LINE_RE.finditer(text or ""):
        found[m.group(1)] = m.group(2)
    v = []
    for tool in PREFLIGHT_TOOLS:
        if tool not in found:
            v.append("preflight missing tool %s" % tool)
            continue
        rest = found[tool]
        if rest.startswith("RUN -- ("):
            if not any(c.isdigit() for c in rest):
                v.append("preflight %s: RUN line carries no digit" % tool)
        elif rest.startswith("DECLARED-NOT-APPLICABLE"):
            reason = rest[len("DECLARED-NOT-APPLICABLE"):].strip()
            if not reason:
                v.append("preflight %s: DECLARED-NOT-APPLICABLE with no reason" % tool)
        else:
            v.append("preflight %s: neither 'RUN -- (' nor 'DECLARED-NOT-APPLICABLE'" % tool)
    return v


def check_criteria_text(text, cell):
    """([] violations, [] ids) over every <criterion> element in `text`. A judgment="true"
    criterion carries no <invocation>/<expect> children; every other criterion carries exactly
    one of each. Every criterion's cell_refs must equal `cell` exactly."""
    v = []
    ids = []
    for m in CRITERION_SELF_RE.finditer(text or ""):
        attrs = dict(ATTR_RE.findall(m.group(1)))
        cid = attrs.get("id", "<no id>")
        ids.append(cid)
        if attrs.get("judgment", "").strip().lower() != "true":
            v.append("criterion %s is self-closing without judgment=\"true\"" % cid)
        if attrs.get("cell_refs", "").strip() != cell:
            v.append("criterion %s cell_refs %r != %r" % (cid, attrs.get("cell_refs", ""), cell))
    for m in CRITERION_BLOCK_RE.finditer(text or ""):
        attrs = dict(ATTR_RE.findall(m.group(1)))
        cid = attrs.get("id", "<no id>")
        ids.append(cid)
        body = m.group(2)
        n_inv = len(re.findall(r"<invocation\b", body))
        n_exp = len(re.findall(r"<expect\b", body))
        is_judgment = attrs.get("judgment", "").strip().lower() == "true"
        if is_judgment:
            if n_inv or n_exp:
                v.append("criterion %s is judgment=\"true\" but carries %d invocation(s)/%d expect(s)"
                         % (cid, n_inv, n_exp))
        else:
            if n_inv != 1 or n_exp != 1:
                v.append("criterion %s carries %d invocation(s) and %d expect(s); needs exactly one of each"
                         % (cid, n_inv, n_exp))
        if attrs.get("cell_refs", "").strip() != cell:
            v.append("criterion %s cell_refs %r != %r" % (cid, attrs.get("cell_refs", ""), cell))
    if not ids:
        v.append("no <criterion> elements found in criteria file")
    return v, ids


def make_slug(title):
    words = re.findall(r"[a-z0-9]+", (title or "").lower())
    if len(words) > 5:
        words = words[:5]
    if len(words) == 1:
        words = words * 2
    return "-".join(words) if words else "direct-act"


def render_order(code, slot, cell, title, coo_text, cto_text, section, paths, preflight_text,
                  criteria_text, round_n, fabric, decomp_doc, order_path, d, macro,
                  investigation_path):
    coo_section = extract_section(coo_text, section)
    if coo_section is None:
        coo_section = coo_text or ""
    cto_section = extract_section(cto_text, section)
    if cto_section is None:
        cto_section = cto_text or ""
    issued_to = "0.9.0_WK_%s~%s" % (code, slot)
    deliverables = "org/missions/%s/%s/%s/deliverables/%s/" % (d, macro, code, issued_to)
    all_paths = list(paths) + [
        deliverables,
        investigation_path,
        order_path,
        "org/critical_paths/change_management/",
        "org/critical_paths/.open_deploys/",
    ]
    issued_by = os.environ.get("OPAL_AGENT_SERIAL", "").strip() or "2.0.0_SA_COO"
    lines = []
    lines.append("# %s task order -- `%s` -- DIRECT ACT: %s" % (code, cell, title))
    lines.append("")
    lines.append(WORKER_FACE_MARKER)
    lines.append("")
    lines.append("<decomp_ref>")
    lines.append("<decomp_doc>%s</decomp_doc>" % decomp_doc)
    lines.append("<owned_cells>%s</owned_cells>" % cell)
    lines.append("</decomp_ref>")
    lines.append("<issued_to>%s</issued_to>" % issued_to)
    lines.append("<issued_by>%s</issued_by>" % issued_by)
    lines.append("<placeholders>NONE</placeholders>")
    lines.append("<preflight>")
    lines.append((preflight_text or "").rstrip("\n"))
    lines.append("</preflight>")
    lines.append("")
    lines.append("## 1. THE SIGNED SECTION -- inlined verbatim from both halves of the never-widen pair")
    lines.append("")
    lines.append("### COO HALF")
    lines.append(coo_section)
    lines.append("")
    lines.append("### CTO HALF")
    lines.append(cto_section)
    lines.append("")
    lines.append("## 2. WHERE THIS CAME FROM")
    lines.append("")
    lines.append("Minted by `python .tools/direct-act-order.py mint` from the signed never-widen pair "
                 "bounding this DIRECT act; round %s." % round_n)
    lines.append("")
    lines.append("## 3. SURFACES -- what you may read and write")
    lines.append("")
    lines.append("<paths>")
    for p in all_paths:
        lines.append(p)
    lines.append("</paths>")
    lines.append("")
    lines.append("## 4. BOUNDS")
    lines.append("")
    lines.append("Bounded to the paths the signed pair names -- the pair bounds, the order grants. "
                 "No path outside the <paths> block above is a write surface.")
    lines.append("")
    lines.append("## 5. PROOF OF SPEC")
    lines.append("")
    lines.append((criteria_text or "").rstrip("\n"))
    lines.append("")
    lines.append("## 6. WHEN YOU ARE DONE")
    lines.append("")
    lines.append("Write the proof_of_spec instance, flip <status> to complete, commit under the "
                 "granted <paths> only.")
    lines.append("")
    lines.append(RECORD_FACE_MARKER)
    lines.append("")
    lines.append("<status>pending</status>")
    lines.append("<direct_act>true</direct_act>")
    lines.append("<slot>~%s</slot>" % slot)
    lines.append("<fabric>%s</fabric>" % fabric)
    lines.append("")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# I/O HELPERS
# ---------------------------------------------------------------------------

def repo_root():
    try:
        r = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True,
                            text=True, encoding="utf-8", errors="replace", timeout=20)
    except Exception:  # noqa: BLE001
        return os.getcwd()
    if r.returncode != 0:
        return os.getcwd()
    return r.stdout.strip()


def fetch_head(path):
    """(raw_bytes_or_None, text_or_None) for `git show HEAD:<path>`."""
    try:
        r = subprocess.run(["git", "show", "HEAD:%s" % path], capture_output=True, timeout=30)
    except Exception:  # noqa: BLE001
        return None, None
    if r.returncode != 0:
        return None, None
    raw = r.stdout
    return raw, raw.decode("utf-8", errors="replace")


def resolve_tree_root(code):
    pattern = "org/missions/D*/*/%s" % code
    matches = sorted(set(p.replace("\\", "/").rstrip("/") for p in glob.glob(pattern)
                          if os.path.isdir(p)))
    if len(matches) != 1:
        return None, ("REFUSED: tree root resolution found %d match(es) for project %s (need "
                       "exactly 1): %s" % (len(matches), code, matches))
    return matches[0], None


def read_fabric(root):
    p = os.path.join(root, "project.json")
    try:
        with open(p, "r", encoding="utf-8") as fh:
            doc = json.load(fh)
    except Exception as exc:  # noqa: BLE001
        return None, "REFUSED: cannot read %s (%s)" % (p, exc)
    fabric = doc.get("fabric")
    if not fabric:
        return None, "REFUSED: %s carries no fabric" % p
    return fabric, None


def decomp_doc_path(root, code):
    return "%s/decompositions/%s_DECOMP.md" % (root, code)


def newest_investigation(root):
    pattern = os.path.join(root, "surprise-channel", "investigations", "INVESTIGATION_v*.md")
    best_n, best_path = 0, None
    for p in glob.glob(pattern):
        m = re.search(r"INVESTIGATION_v(\d+)\.md$", p)
        if m:
            n = int(m.group(1))
            if n > best_n:
                best_n, best_path = n, p
    if best_path is None:
        return "%s/surprise-channel/investigations/INVESTIGATION_v1.md" % root
    return best_path.replace("\\", "/")


# ---------------------------------------------------------------------------
# mint
# ---------------------------------------------------------------------------

def build_mint_parser():
    p = argparse.ArgumentParser(prog="direct-act-order.py mint")
    p.add_argument("--code", required=True)
    p.add_argument("--slot", required=True)
    p.add_argument("--cell", required=True)
    p.add_argument("--title", required=True)
    p.add_argument("--coo-half", required=True)
    p.add_argument("--cto-half", required=True)
    p.add_argument("--section", required=True)
    p.add_argument("--path", action="append", default=[], required=True)
    p.add_argument("--preflight-file", required=True)
    p.add_argument("--criteria-file", required=True)
    p.add_argument("--round", required=True)
    p.add_argument("--dry-run", action="store_true")
    return p


def cmd_mint(argv):
    args = build_mint_parser().parse_args(argv)
    refusals = []

    serial = os.environ.get("OPAL_AGENT_SERIAL", "")
    if not issuer_is_coo(serial):
        refusals.append("REFUSED: issuer OPAL_AGENT_SERIAL=%r does not start with 2.0.0_SA_COO" % serial)

    root, err = resolve_tree_root(args.code)
    if err:
        print(err)
        return 2
    fabric, ferr = read_fabric(root)
    if ferr:
        print(ferr)
        return 2

    parts = root.split("/")
    if len(parts) < 4:
        print("REFUSED: tree root %s does not have the D<n>/MACRO/CODE shape" % root)
        return 2
    d, macro = parts[2], parts[3]

    decomp_path = decomp_doc_path(root, args.code)
    try:
        with open(decomp_path, "r", encoding="utf-8", errors="replace") as fh:
            decomp_text = fh.read()
    except OSError as exc:
        print("REFUSED: cannot read decomposition %s (%s)" % (decomp_path, exc))
        return 2
    if args.cell not in decomp_text:
        refusals.append("REFUSED: decomposition %s does not carry cell token %s" % (decomp_path, args.cell))

    coo_raw, coo_text = fetch_head(args.coo_half)
    if coo_raw is None:
        refusals.append("REFUSED: COO half %s absent at HEAD" % args.coo_half)
    cto_raw, cto_text = fetch_head(args.cto_half)
    if cto_raw is None:
        refusals.append("REFUSED: CTO half %s absent at HEAD" % args.cto_half)

    if coo_raw is not None and not section_heading_present(coo_text, args.section):
        refusals.append("REFUSED: COO half %s carries no heading line containing %r" % (args.coo_half, args.section))
    if cto_raw is not None and not section_heading_present(cto_text, args.section):
        refusals.append("REFUSED: CTO half %s carries no heading line containing %r" % (args.cto_half, args.section))

    for p in args.path:
        ok, reason = validate_path_grammar(p)
        if not ok:
            refusals.append("REFUSED: path %s fails the grammar (%s)" % (p, reason))
            continue
        if not path_named_by_either(p, coo_text or "", cto_text or ""):
            refusals.append("REFUSED: path not named by either half: %s" % p)

    try:
        with open(args.preflight_file, "r", encoding="utf-8", errors="replace") as fh:
            preflight_text = fh.read()
    except OSError as exc:
        print("REFUSED: cannot read preflight file %s (%s)" % (args.preflight_file, exc))
        return 2
    refusals.extend("REFUSED: %s" % v for v in check_preflight_text(preflight_text))

    try:
        with open(args.criteria_file, "r", encoding="utf-8", errors="replace") as fh:
            criteria_text = fh.read()
    except OSError as exc:
        print("REFUSED: cannot read criteria file %s (%s)" % (args.criteria_file, exc))
        return 2
    crit_v, _crit_ids = check_criteria_text(criteria_text, args.cell)
    refusals.extend("REFUSED: %s" % v for v in crit_v)

    if refusals:
        for r in refusals:
            print(r)
        return 2

    coo_hash = hashlib.sha256(coo_raw).hexdigest()
    cto_hash = hashlib.sha256(cto_raw).hexdigest()
    print("PAIR: COO sha256=%s CTO sha256=%s" % (coo_hash, cto_hash))

    inv_path = newest_investigation(root)
    slug = make_slug(args.title)
    order_path = "%s/task-orders/%s.TO-%s.%s.md" % (root, args.code, args.cell, slug)

    rendered = render_order(code=args.code, slot=args.slot, cell=args.cell, title=args.title,
                             coo_text=coo_text, cto_text=cto_text, section=args.section,
                             paths=list(args.path), preflight_text=preflight_text,
                             criteria_text=criteria_text, round_n=args.round, fabric=fabric,
                             decomp_doc=decomp_path, order_path=order_path, d=d, macro=macro,
                             investigation_path=inv_path)

    if args.dry_run:
        print("---BEGIN ORDER---")
        print(rendered)
        print("---END ORDER---")
        print("DRY-RUN: nothing written")
        return 0

    os.makedirs(os.path.dirname(order_path), exist_ok=True)
    with open(order_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(rendered)

    gate_root = repo_root()
    violations = []
    try:
        spec = importlib.util.spec_from_file_location(
            "to_pipeline_gate_direct_act", os.path.join(gate_root, ".tools", "to-pipeline-gate.py"))
        gate = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(gate)
        rel = os.path.relpath(order_path, gate_root).replace("\\", "/")
        violations, _notes = gate.check_file(gate_root, rel)
    except Exception as exc:  # noqa: BLE001
        violations = ["gate import/execution failed: %s" % exc]

    if violations:
        try:
            os.remove(order_path)
        except OSError:
            pass
        print("REFUSED: minted order failed the L6 gate; deleted. Violations:")
        for v in violations:
            print("  V: %s" % v)
        return 3

    print("MINTED: %s sha256=%s gate_violations 0" % (order_path, hashlib.sha256(rendered.encode("utf-8")).hexdigest()))
    return 0


# ---------------------------------------------------------------------------
# self-test
# ---------------------------------------------------------------------------

def _self_test_positive_render():
    coo_text = "# NEVER-WIDEN CO-SIGN -- COO HALF. The `fixture/path.py` grant.\nbody coo fixture/path.py\n"
    cto_text = "# NEVER-WIDEN CO-SIGN -- CTO HALF. The `fixture/path.py` grant.\nbody cto fixture/path.py\n"
    section = "fixture/path.py"
    preflight_text = ("comp-schedule: DECLARED-NOT-APPLICABLE fixture\n"
                       "comp-iam: RUN -- (fixture: 1 of 1)\n"
                       "comp-adversary: DECLARED-NOT-APPLICABLE fixture\n")
    criteria_text = ("<proof_of_spec>\n"
                      "  <criterion id=\"AC1\" cell_refs=\"C-1\"><invocation>echo hi</invocation>"
                      "<expect>prints hi</expect></criterion>\n"
                      "</proof_of_spec>\n")
    order_path = "org/missions/D9/FIX/FIXPRJ/task-orders/FIXPRJ.TO-C-1.fixture-render.md"
    inv_path = "org/missions/D9/FIX/FIXPRJ/surprise-channel/investigations/INVESTIGATION_v1.md"
    rendered = render_order(code="FIXPRJ", slot="9", cell="C-1", title="fixture render",
                             coo_text=coo_text, cto_text=cto_text, section=section,
                             paths=["fixture/path.py"], preflight_text=preflight_text,
                             criteria_text=criteria_text, round_n="1", fabric="site-z",
                             decomp_doc="org/missions/D9/FIX/FIXPRJ/decompositions/FIXPRJ_DECOMP.md",
                             order_path=order_path, d="D9", macro="FIX", investigation_path=inv_path)
    n_inv = rendered.count("<invocation>")
    n_exp = rendered.count("<expect>")
    standing = [
        "org/missions/D9/FIX/FIXPRJ/deliverables/0.9.0_WK_FIXPRJ~9/",
        inv_path,
        order_path,
        "org/critical_paths/change_management/",
        "org/critical_paths/.open_deploys/",
    ]
    ok = (n_inv == 1 and n_exp == 1) and ("fixture/path.py" in rendered)
    for s in standing:
        if s not in rendered:
            ok = False
    return ok


def _self_test_no_round_element():
    """A DIRECT act is UNROUNDED (row AMGT_RESAPP-Z-W58-S1 repair, GATE (x) one-issuer-per-round):
    the render must carry no line-anchored <round>N</round> element at all -- not merely a
    different value. --round is still accepted on the CLI (it names WHICH pair/round bounds the
    act for the humans reading section 2's prose) but never reaches the RECORD FACE as a tag."""
    coo_text = "# NEVER-WIDEN CO-SIGN -- COO HALF. The `fixture/path.py` grant.\nbody coo fixture/path.py\n"
    cto_text = "# NEVER-WIDEN CO-SIGN -- CTO HALF. The `fixture/path.py` grant.\nbody cto fixture/path.py\n"
    section = "fixture/path.py"
    preflight_text = ("comp-schedule: DECLARED-NOT-APPLICABLE fixture\n"
                       "comp-iam: RUN -- (fixture: 1 of 1)\n"
                       "comp-adversary: DECLARED-NOT-APPLICABLE fixture\n")
    criteria_text = ("<proof_of_spec>\n"
                      "  <criterion id=\"AC1\" cell_refs=\"C-1\"><invocation>echo hi</invocation>"
                      "<expect>prints hi</expect></criterion>\n"
                      "</proof_of_spec>\n")
    order_path = "org/missions/D9/FIX/FIXPRJ/task-orders/FIXPRJ.TO-C-1.fixture-unrounded.md"
    inv_path = "org/missions/D9/FIX/FIXPRJ/surprise-channel/investigations/INVESTIGATION_v1.md"
    rendered = render_order(code="FIXPRJ", slot="9", cell="C-1", title="fixture unrounded",
                             coo_text=coo_text, cto_text=cto_text, section=section,
                             paths=["fixture/path.py"], preflight_text=preflight_text,
                             criteria_text=criteria_text, round_n="14", fabric="site-z",
                             decomp_doc="org/missions/D9/FIX/FIXPRJ/decompositions/FIXPRJ_DECOMP.md",
                             order_path=order_path, d="D9", macro="FIX", investigation_path=inv_path)
    return "<round>" not in rendered and "</round>" not in rendered


def _self_test_direct_act_element():
    """Row AMGT_RESAPP-Z-W58-S2's repair (GATE (x)'s narrow exemption): a DIRECT act's render must now carry a
    line-anchored <direct_act>true</direct_act> element on its own line, so GATE (x)'s missing-<round> branch
    can read it as an explicit round-less declaration rather than an omission."""
    coo_text = "# NEVER-WIDEN CO-SIGN -- COO HALF. The `fixture/path.py` grant.\nbody coo fixture/path.py\n"
    cto_text = "# NEVER-WIDEN CO-SIGN -- CTO HALF. The `fixture/path.py` grant.\nbody cto fixture/path.py\n"
    section = "fixture/path.py"
    preflight_text = ("comp-schedule: DECLARED-NOT-APPLICABLE fixture\n"
                       "comp-iam: RUN -- (fixture: 1 of 1)\n"
                       "comp-adversary: DECLARED-NOT-APPLICABLE fixture\n")
    criteria_text = ("<proof_of_spec>\n"
                      "  <criterion id=\"AC1\" cell_refs=\"C-1\"><invocation>echo hi</invocation>"
                      "<expect>prints hi</expect></criterion>\n"
                      "</proof_of_spec>\n")
    order_path = "org/missions/D9/FIX/FIXPRJ/task-orders/FIXPRJ.TO-C-1.fixture-unrounded.md"
    inv_path = "org/missions/D9/FIX/FIXPRJ/surprise-channel/investigations/INVESTIGATION_v1.md"
    rendered = render_order(code="FIXPRJ", slot="9", cell="C-1", title="fixture unrounded",
                             coo_text=coo_text, cto_text=cto_text, section=section,
                             paths=["fixture/path.py"], preflight_text=preflight_text,
                             criteria_text=criteria_text, round_n="14", fabric="site-z",
                             decomp_doc="org/missions/D9/FIX/FIXPRJ/decompositions/FIXPRJ_DECOMP.md",
                             order_path=order_path, d="D9", macro="FIX", investigation_path=inv_path)
    return "\n<direct_act>true</direct_act>\n" in rendered or rendered.count("<direct_act>true</direct_act>") == 1


def self_test():
    arms = []

    ok, _reason = validate_path_grammar("/abs/path")
    arms.append(("leading-slash refusal", ok is False))

    ok, _reason = validate_path_grammar("a/../b")
    arms.append(("'..' refusal", ok is False))

    ok, _reason = validate_path_grammar("a/{b,c}/d")
    arms.append(("bracket-that-is-not-a-glob refusal", ok is False))

    named = path_named_by_either("zzz/not/here.py", "alpha beta gamma", "delta epsilon")
    arms.append(("path-not-named-by-either-half refusal", named is False))

    text_no_heading = "some prose\nmore prose\n# a heading about something else\n"
    present = section_heading_present(text_no_heading, "scores/v1/")
    arms.append(("missing-section-heading refusal", present is False))

    arms.append(("non-COO-issuer refusal", issuer_is_coo("0.9.0_WK_FOO~1") is False))

    bad_pre = ("comp-schedule: RUN -- (no digit here)\n"
               "comp-iam: DECLARED-NOT-APPLICABLE fine\n"
               "comp-adversary: DECLARED-NOT-APPLICABLE fine\n")
    v = check_preflight_text(bad_pre)
    arms.append(("preflight RUN line with no digit refused", len(v) >= 1))

    bad_crit = ("<criterion id=\"X1\" cell_refs=\"C-1\"><invocation>a</invocation>"
                "<invocation>b</invocation><expect>c</expect></criterion>")
    v2, _ids = check_criteria_text(bad_crit, "C-1")
    arms.append(("two-invocation criterion refused", len(v2) >= 1))

    arms.append(("positive render arm: one invocation, one expect per criterion, five standing paths",
                 _self_test_positive_render()))

    arms.append(("a DIRECT act is UNROUNDED -- the render emits no <round> element",
                 _self_test_no_round_element()))

    arms.append(("a DIRECT act declares itself round-less -- the render emits <direct_act>true</direct_act> (row AMGT_RESAPP-Z-W58-S2)",
                _self_test_direct_act_element()))

    failed = 0
    for name, passed in arms:
        if passed:
            print("OK: arm %r" % name)
        else:
            failed += 1
            print("FAIL: arm %r" % name)
    print("RESULT: %d arm(s) failed of %d" % (failed, len(arms)))
    return 0 if failed == 0 else 1


def main(argv):
    if not argv:
        print("ERROR: no command given (mint | --self-test)")
        return 2
    if argv[0] == "--self-test":
        return self_test()
    if argv[0] == "mint":
        return cmd_mint(argv[1:])
    print("ERROR: unknown command %r (mint | --self-test)" % argv[0])
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
