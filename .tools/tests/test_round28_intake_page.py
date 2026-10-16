#!/usr/bin/env python3
"""test_round28_intake_page.py -- CTax1-AC1: the intake page carries its five sections, and every example block is graded by
the intake tools' OWN gate function (named by the comment line directly above the block's fence).

Grading. A line-level gate (intake_fetch.approval_gate, intake_check.check_2, intake_check.parse_waivers) grades each non-empty
line of the block. A document-level gate (intake_check.check_8) grades each document of the block; documents are separated by
a line of three dashes. An `accepted` example must pass its gate; a `refused` example must fail it. A positive control proves
the fixture passes the pinned line, so a refusal is the line's and not the fixture's. A control arm plants a refused form
into an accepted block of a temporary copy of the page and requires the grade to fail.

Standard library plus the intake tools; temporary folders only; no network; no record is written. ASCII output.
Last line: INTAKE-PAGE blocks=<k> accepted=<a> refused=<r> ok=<True|False>
"""
import pathlib
import re
import shutil
import sys
import tempfile

REPO = pathlib.Path(__file__).resolve().parents[2]
INTAKE_DIR = REPO / "org" / "devices" / "intake"
PAGE = INTAKE_DIR / "APPROVAL_AND_SIGNED_FILE_DEMANDS.md"
sys.path.insert(0, str(INTAKE_DIR))
import intake_check as ic  # noqa: E402  (the real tool, imported in place)
import intake_fetch  # noqa: E402

FILE = "examplepkg-1.2.3-py3-none-any.whl"
BATCH = "intake-20261016-example"
PINNED = "examplepkg==1.2.3"
SECTIONS = [
    "## 1. The approval-file line",
    "## 2. The signed check-8 file",
    "## 3. The `WAIVE` line",
    "## 4. The order of the batch route",
    "## 5. The dry-run commands",
]
BLOCK_RE = re.compile(r"^```text (accepted|refused)\s*$")
GATE_RE = re.compile(r"^<!-- gate: ([A-Za-z_][A-Za-z0-9_.]*) -->\s*$")


def _approval_file(tmp, text):
    path = tmp / "approved.txt"
    path.write_text(text + "\n", encoding="utf-8")
    return path


def gate_approval_gate(fn, text, tmp):
    """intake_fetch.approval_gate: the fetch reader. True when it raises nothing."""
    try:
        fn(str(_approval_file(tmp, text)), [PINNED])
    except intake_fetch.Refuse:
        return False
    return True


def _check2_context(tmp, text):
    wheel = ic.build_synthetic_wheel(tmp / FILE, name="examplepkg", version="1.2.3", tags=("py3", "none", "any"))
    req = {"name": "examplepkg", "version": "1.2.3", "python_tag": "py3", "abi_tag": "none", "platform_tag": "any",
           "file_name": FILE}
    return {"fetch": {"requested": req}, "path": wheel, "file_name": FILE,
            "approved_by": str(_approval_file(tmp, text))}


def gate_check_2(fn, text, tmp):
    """intake_check.check_2 on a synthetic wheel: True when its verdict is passed."""
    verdict, _ev = fn(_check2_context(tmp, text))
    return verdict == "passed"


def gate_check_8(fn, doc, tmp):
    """intake_check.check_8 on one signed-file document, the signer directory being a temporary folder."""
    signer = tmp / "signer"
    signer.mkdir()
    signed = signer / "signed.md"
    signed.write_text(doc + "\n", encoding="utf-8")
    cfg = ic.Cfg(root=tmp / "root", records=tmp / "records", av_json=str(tmp / "av.json"), sites=[], signer_dir=signer)
    ctx = {"cfg": cfg, "batch": BATCH, "file_name": FILE, "signed_by": str(signed), "approved_by": None}
    verdict, _ev = fn(ctx)
    return verdict == "passed"


def gate_parse_waivers(fn, text, tmp):
    """intake_check.parse_waivers for this file: True when exactly one waiver is read."""
    waivers, _refused, _ignored = fn(text, FILE)
    return len(waivers) == 1


# gate name -> (granularity, adapter). The adapter calls the real function; a name not listed here fails the page.
GATES = {
    "intake_fetch.approval_gate": ("line", gate_approval_gate),
    "intake_check.check_2": ("line", gate_check_2),
    "intake_check.check_8": ("document", gate_check_8),
    "intake_check.parse_waivers": ("line", gate_parse_waivers),
}


def resolve(name):
    module_name, _, func = name.partition(".")
    module = {"intake_fetch": intake_fetch, "intake_check": ic}.get(module_name)
    fn = getattr(module, func, None) if module is not None else None
    return fn if callable(fn) else None


def run_one(gate_name, item):
    granularity, adapter = GATES[gate_name]
    fn = resolve(gate_name)
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="intake_page_"))
    try:
        return adapter(fn, item, tmp)
    finally:
        shutil.rmtree(str(tmp), ignore_errors=True)


def parse_blocks(text):
    lines = text.splitlines()
    blocks = []
    i = 0
    while i < len(lines):
        m = BLOCK_RE.match(lines[i])
        if not m:
            i += 1
            continue
        g = GATE_RE.match(lines[i - 1]) if i > 0 else None
        k = i + 1
        while k < len(lines) and lines[k].strip() != "```":
            k += 1
        if k >= len(lines):
            blocks.append({"kind": m.group(1), "gate": None, "body": None, "line": i + 1})
            break
        blocks.append({"kind": m.group(1), "gate": g.group(1) if g else None, "body": lines[i + 1:k], "line": i + 1})
        i = k + 1
    return blocks


def grade_text(text, quiet=False):
    """Grade every example block of a page text. Returns (blocks, accepted, refused, fails)."""
    fails = []
    accepted = refused = 0
    blocks = parse_blocks(text)
    for b in blocks:
        tag = "block line=%d gate=%s kind=%s" % (b["line"], b["gate"], b["kind"])
        if b["body"] is None:
            fails.append("%s: unclosed fence" % tag)
            continue
        if b["gate"] not in GATES:
            fails.append("%s: no known gate comment directly above the fence" % tag)
            continue
        if resolve(b["gate"]) is None:
            fails.append("%s: the named function does not exist in the tool" % tag)
            continue
        granularity = GATES[b["gate"]][0]
        if granularity == "line":
            items = [ln for ln in b["body"] if ln.strip()]
        else:
            items, cur = [], []
            for ln in b["body"] + ["---"]:
                if ln.strip() == "---":
                    if any(x.strip() for x in cur):
                        items.append("\n".join(cur))
                    cur = []
                else:
                    cur.append(ln)
        if not items:
            fails.append("%s: no example in the block" % tag)
            continue
        want = b["kind"] == "accepted"
        ok_n = 0
        for item in items:
            got = run_one(b["gate"], item)
            if got == want:
                ok_n += 1
            else:
                first = item.splitlines()[0] if item.strip() else "(empty)"
                fails.append("%s: example %r graded %s, expected %s" % (
                    tag, first[:70], "accepted" if got else "refused", b["kind"]))
            if want:
                accepted += 1
            else:
                refused += 1
        if not quiet:
            print("BLOCK line=%d gate=%s kind=%s examples=%d as_expected=%d" % (
                b["line"], b["gate"], b["kind"], len(items), ok_n))
    return blocks, accepted, refused, fails


def headings_ok(text):
    heads = [ln.rstrip() for ln in text.splitlines() if ln.startswith("## ")]
    return heads == SECTIONS


def positive_control():
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="intake_page_pc_"))
    try:
        return gate_check_2(ic.check_2, PINNED, tmp)
    finally:
        shutil.rmtree(str(tmp), ignore_errors=True)


def main():
    text = PAGE.read_text(encoding="utf-8")
    ascii_ok = all(ord(c) < 128 for c in text)
    sections = headings_ok(text)
    print("SECTIONS five=%s ascii=%s" % (sections, ascii_ok))
    pc = positive_control()
    print("POSITIVE-CONTROL check_2 accepts %s on the fixture: %s" % (PINNED, pc))
    blocks, accepted, refused, fails = grade_text(text)
    for f in fails:
        print("FAIL: " + f)
    main_ok = sections and ascii_ok and pc and not fails and accepted > 0 and refused > 0

    # control arm: plant a refused form into the first accepted approval-file block of a temporary copy of the page
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="intake_page_ctl_"))
    try:
        planted_form = "examplepkg[socks]==1.2.3"
        head = "```text accepted\n" + PINNED + "\n"
        planted_text = text.replace(head, "```text accepted\n" + planted_form + "\n" + PINNED + "\n", 1)
        planted_ok = planted_text != text
        copy = tmp / "APPROVAL_AND_SIGNED_FILE_DEMANDS.copy.md"
        copy.write_text(planted_text, encoding="utf-8")
        _b, _a, _r, cfails = grade_text(copy.read_text(encoding="utf-8"), quiet=True)
    finally:
        shutil.rmtree(str(tmp), ignore_errors=True)
    detected = planted_ok and bool(cfails)
    print("CONTROL planted=%s into an accepted block of a temporary copy: fails=%d detected=%s" % (
        planted_form, len(cfails), detected))
    ok = bool(main_ok and detected)
    print("INTAKE-PAGE blocks=%d accepted=%d refused=%d ok=%s" % (len(blocks), accepted, refused, ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
