#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""prd_signoff_lib -- THE ONE IMPLEMENTATION of the L4-R sign-off rules (spine v3.15).

Three consumers call these functions and none re-derives them: the L6 gate (`to-pipeline-gate.py`
LIMB 6), the L4 notifier (`prd-header-notify.py`), and the reviewer's stamp tool (`prd-signoff.py`).
A rule written in three places drifts in three directions (measured 2026-09-11: a hand-transcribed
deploy pattern, too wide then too narrow); a rule called from one place cannot.

THE MODEL. A PRD has TWO HALVES, each reviewed by one seat and each bound to the BYTES of the sections
it covers, not to `prd_version`:
    ratified-text  ENDPOINT + CONTRACTS               reviewer 3.0.0_SA_CVO, always
    brief          every other top-level section      reviewer 4.0.0_SA_CRO, or 2.0.0_SA_COO in its stead
A bump that leaves a half byte-identical keeps that half's signature (measured 2026-09-10/11: thirteen
PRD versions in one night, the CRO's half unchanged across three of them and re-signed each time
because the file was version-bound). A bump that changes a half re-opens that half only. An L10
addendum that touches ENDPOINT alone re-opens the ratified-text half alone.

Halves are hashed over the section BODIES between top-level '## ' headings outside code fences,
normalised to LF with trailing whitespace stripped per line, so a CRLF checkout or a trailing
space never re-opens a half (the autocrlf trap is banked).

Legacy files (no `half` / `half_hash`: the four written on 2026-09-10/11 before this library)
infer their half from the signer and bind to `prd_version`, so nothing already signed re-opens.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
from datetime import datetime, timezone

RATIFIED_SECTIONS = ("ENDPOINT", "CONTRACTS")          # matched on the heading's FIRST WORD, backtick-insensitive
HALVES = ("ratified-text", "brief")
REVIEWERS = {                                          # base serials permitted to sign each half, in preference order
    "ratified-text": ("3.0.0_SA_CVO",),
    "brief": ("4.0.0_SA_CRO", "2.0.0_SA_COO"),
}
PRIMARY = {"ratified-text": "3.0.0_SA_CVO", "brief": "4.0.0_SA_CRO"}
SUBSTITUTE = {"brief": "2.0.0_SA_COO"}                 # only when the primary is not live / overdue; recorded in the file
AUTHOR = "1.0.0_SA_CTO"                                # the PRD's author never signs
DESIGNATION_FIELD = "l4r_brief_signer"                 # project.json: {"serial", "authority": "<path>@<commit>", "quoted"} -- Andrew's word names the brief signer
DESIGNATION_AUTHORITY_RE = re.compile(r"^[^@\s]+@[0-9a-f]{7,40}$")
SIGNOFF_DIR = "signoff"
VERDICTS = ("SIGNED", "REFUSED")
FENCE_RE = re.compile(r"^(```|~~~)")
HEADING_RE = re.compile(r"^## +(.+?)\s*$")
HEADER_FENCE_RE = re.compile(r"```json\s*(.*?)```", re.S)


def base_serial(s):
    return str(s or "").strip().split("~", 1)[0]


def utc_now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------------------------------------------------------------- sections and halves

def top_sections(text):
    """[(title, body)] for every top-level '## ' heading OUTSIDE code fences, in order. `body` is the
    original lines after the heading up to the next such heading. Text before the first heading
    (the PRD_HEADER fence, the preamble) is returned under title None."""
    out = []
    title, buf, in_fence, fence = None, [], False, ""
    for line in text.replace("\r\n", "\n").replace("\r", "\n").split("\n"):
        m = FENCE_RE.match(line)
        if m:
            tok = m.group(1)
            if not in_fence:
                in_fence, fence = True, tok
            elif tok == fence:
                in_fence, fence = False, ""
            buf.append(line)
            continue
        h = HEADING_RE.match(line) if not in_fence else None
        if h:
            out.append((title, buf))
            title, buf = h.group(1), []
            continue
        buf.append(line)
    out.append((title, buf))
    return out


def _first_word(title):
    t = re.sub(r"[`*_]", "", title or "").strip()
    return t.split(" ", 1)[0].upper() if t else ""


def half_of_section(title):
    """Which half a top-level section belongs to; the pre-heading preamble (title None) belongs to
    neither (it carries prd_version, which must NOT re-open a half by itself)."""
    if title is None:
        return None
    return "ratified-text" if _first_word(title) in RATIFIED_SECTIONS else "brief"


def _norm(lines):
    return "\n".join(ln.rstrip() for ln in lines).strip("\n") + "\n"


def half_hashes(text):
    """{half: sha256 over the concatenated normalised bodies of that half's sections, with each
    section's first word as a separator so a section moving between halves changes both}."""
    parts = {h: [] for h in HALVES}
    for title, body in top_sections(text):
        h = half_of_section(title)
        if h:
            parts[h].append("## " + _first_word(title) + "\n" + _norm(body))
    return {h: hashlib.sha256("".join(parts[h]).encode("utf-8")).hexdigest() for h in HALVES}


def prd_header(text):
    m = HEADER_FENCE_RE.search(text)
    try:
        return json.loads(m.group(1)) if m else {}
    except Exception:  # noqa: BLE001
        return {}


# ---------------------------------------------------------------- files and verdicts

def infer_half(doc):
    """The half a sign-off file covers: its `half` field, else inferred from the signer (legacy)."""
    h = str(doc.get("half") or "").strip()
    if h in HALVES:
        return h
    b = base_serial(doc.get("signed_by"))
    for half, bases in REVIEWERS.items():
        if b in bases:
            return half
    return None


def designated_brief_signer(project_doc):
    """(serial|None, reason). A project row may DESIGNATE the brief half's signer on Andrew's word -- the one case
    in which the round-holding COO lane signs (Andrew-direct 2026-09-11 ~08:0xZ: "get the signoff from 2.0.0_SA_COO~D
    specifically"). Admitted ONLY with a `serial` whose base is a brief-half reviewer AND a pinned `authority`
    (<path>@<commit>); anything less is ignored and the reason says so -- a value carries its claim and the
    consumer rejects. The separation-of-duties default stands for every project without the field."""
    d = (project_doc or {}).get(DESIGNATION_FIELD)
    if not isinstance(d, dict):
        return None, "no designation"
    serial = str(d.get("serial") or "").strip()
    auth = str(d.get("authority") or "").strip()
    if not serial:
        return None, "designation without a serial is ignored"
    if not DESIGNATION_AUTHORITY_RE.match(auth):
        return None, "designation for %s ignored: `authority` must be <path>@<commit>, got %r" % (serial, auth)
    if base_serial(serial) not in REVIEWERS["brief"]:
        return None, "designation for %s ignored: its base is not a brief-half reviewer" % serial
    return serial, "designated by %s" % auth


def permitted_signer(half, serial, coo_lane_of_project=None, designated=None):
    """(ok, reason). The author never signs; a COO instance holding the project's round never signs
    the brief half it will decompose (separation of duties) UNLESS the project row designates it on Andrew's
    word (`designated`, from designated_brief_signer); otherwise the base must be in REVIEWERS."""
    b = base_serial(serial)
    if b == AUTHOR:
        return False, "%s is the PRD's author and cannot sign its own document" % serial
    if b not in REVIEWERS.get(half, ()):
        return False, "%s is not a permitted signer of the %s half (permitted: %s)" % (serial, half, ", ".join(REVIEWERS.get(half, ())))
    if half == "brief" and designated and str(serial).strip() == str(designated).strip():
        return True, "designated"
    if b == "2.0.0_SA_COO" and coo_lane_of_project and str(serial).strip() == str(coo_lane_of_project).strip():
        return False, "%s holds this project's round and cannot sign the brief half it decomposes" % serial
    return True, "ok"


def evaluate(prd_text, files, coo_lane_of_project=None, designated=None):
    """PURE. `files` = {basename: parsed-json-or-None}. Returns
        {"halves": {half: {"state": SIGNED|REFUSED|STALE|MISSING|UNREADABLE|NOT-PERMITTED,
                           "by": serial|None, "file": name|None, "detail": str}},
         "admitted": bool, "hashes": {half: hash}, "prd_version": str}
    A half is SIGNED when its newest CURRENT file reads SIGNED; CURRENT = half_hash equals the PRD's
    (or, legacy, prd_version equals). REFUSED wins over an older SIGNED at the same hash.
    """
    hdr = prd_header(prd_text)
    version = str(hdr.get("prd_version") or "")
    hashes = half_hashes(prd_text)
    per = {h: {"state": "MISSING", "by": None, "file": None, "detail": "no sign-off file for this half"} for h in HALVES}
    unreadable = [n for n, d in files.items() if not isinstance(d, dict)]
    for n in unreadable:
        # an unreadable file is a refusal of the whole PRD: it might be the file that would have refused
        per.setdefault("_unreadable", []).append(n)
    candidates = {h: [] for h in HALVES}
    for name, doc in sorted(files.items()):
        if not isinstance(doc, dict):
            continue
        half = infer_half(doc)
        if half is None:
            continue
        ok, why = permitted_signer(half, doc.get("signed_by"), coo_lane_of_project, designated)
        current = (str(doc.get("half_hash") or "") == hashes[half]) if doc.get("half_hash") else (str(doc.get("prd_version")) == version)
        candidates[half].append((str(doc.get("signed_at") or ""), name, doc, ok, why, current))
    for half in HALVES:
        cands = sorted(candidates[half], key=lambda c: c[0])
        if not cands:
            continue
        signed_at, name, doc, ok, why, current = cands[-1]        # newest by signed_at
        verdict = str(doc.get("verdict") or "").upper()
        if not ok:
            per[half] = {"state": "NOT-PERMITTED", "by": doc.get("signed_by"), "file": name, "detail": why}
        elif not current:
            # The STALE detail must name the COMPARISON THAT ACTUALLY RAN, not the one the reader assumes.
            # A hash-bound record went stale because the half's BYTES moved. A version-bound record (no
            # half_hash) went stale because the VERSION STRING moved -- and the bytes may be identical.
            # Claiming "bytes have changed" on the version-bound branch is a FALSE CAUSE in a gate's own
            # error text, and it sends the reader hunting the wrong artifact: measured 2026-09-12, where
            # v0.13 -> v0.14 re-opened a brief half whose sections were byte-identical, and the first
            # hypothesis chased was the header carve-out (which is implemented correctly, :94-95).
            # Routed to this gate's owner by 4.0.0_SA_CRO after hitting it live. A fail-closed gate's
            # error text is its AUTHOR'S CLAIM, never a measurement -- so it states which claim it is.
            if doc.get("half_hash"):
                detail = ("signed against half_hash %s; the %s half's BYTES have changed since (now %s)"
                          " -- re-review is owed on this half only"
                          % (str(doc.get("half_hash"))[:12], half, hashes[half][:12]))
            else:
                detail = ("signed against prd_version %s and this PRD is %s -- LEGACY VERSION-BOUND RECORD:"
                          " this record carries NO half_hash, so the comparison that ran was the VERSION"
                          " STRING, NOT the bytes. The %s half's bytes MAY BE UNCHANGED (current hash %s);"
                          " a version bump alone re-opens a version-bound half. Re-stamping WITH a"
                          " half_hash closes this permanently."
                          % (doc.get("prd_version"), version, half, hashes[half][:12]))
            per[half] = {"state": "STALE", "by": doc.get("signed_by"), "file": name, "detail": detail}
        elif verdict == "SIGNED":
            per[half] = {"state": "SIGNED", "by": doc.get("signed_by"), "file": name, "detail": "current"}
        elif verdict == "REFUSED":
            per[half] = {"state": "REFUSED", "by": doc.get("signed_by"), "file": name,
                         "detail": "review: %s" % (doc.get("review_ref") or "no review_ref")}
        else:
            per[half] = {"state": "REFUSED", "by": doc.get("signed_by"), "file": name, "detail": "verdict %r is not SIGNED" % verdict}
    admitted = all(per[h]["state"] == "SIGNED" for h in HALVES) and not unreadable
    return {"halves": {h: per[h] for h in HALVES}, "unreadable": unreadable, "admitted": admitted,
            "hashes": hashes, "prd_version": version}


def violations(rel, code, prd_rel, result):
    """The gate's refusal lines for ONE PRD from an evaluate() result (empty when admitted)."""
    out = []
    for n in result["unreadable"]:
        out.append("%s: project %s sign-off %s is not readable JSON -- an unreadable sign-off is NOT a sign-off" % (rel, code, n))
    for half in HALVES:
        st = result["halves"][half]
        if st["state"] == "SIGNED":
            continue
        who = " / ".join(REVIEWERS[half])
        if st["state"] == "MISSING":
            out.append("%s: project %s PRD %s has NO sign-off on its %s half (signers: %s) -- L4-R (spine v3.15): both halves "
                       "are signed at their current bytes before any task order is cut; `python .tools/prd-signoff.py status %s` "
                       "shows what is owed" % (rel, code, prd_rel, half, who, code))
        else:
            out.append("%s: project %s PRD %s %s half reads %s (%s, %s): %s"
                       % (rel, code, prd_rel, half, st["state"], st["by"], st["file"], st["detail"]))
    return out


def missing_halves(result):
    return [h for h in HALVES if result["halves"][h]["state"] != "SIGNED"]


def build_doc(prd_basename, prd_text, prd_pin, half, verdict, review_ref, signed_by, substitute_for=None, reason=None):
    hdr = prd_header(prd_text)
    doc = {
        "prd": prd_basename,
        "prd_version": str(hdr.get("prd_version") or ""),
        "prd_pin": prd_pin,
        "half": half,
        "half_hash": half_hashes(prd_text)[half],
        "verdict": verdict,
        "review_ref": review_ref,
        "signed_by": signed_by,
        "signed_at": utc_now(),
    }
    if substitute_for:
        doc["substitute_for"] = substitute_for
    if reason:
        doc["reason"] = reason
    return doc


def read_signoff_files(signoff_dir, ref="HEAD"):
    """{basename: parsed-json-or-None} for every *.json in the signoff dir AS COMMITTED AT `ref` (default HEAD).

    A SIGNATURE IS A COMMITTED FILE, NEVER A WORKING COPY (row LGIC_NAMING-S14, carried by C-S11 into REMEDIATION_v2).
    This used to list and open the worktree. When `prd-signoff.py refuse` exited rc=1 because a foreign commit landed
    16 s after the review commit, the new signoff JSON stayed written but uncommitted, and `status` read it: the brief
    half read REFUSED while HEAD still held the v1.4 SIGNED record. The same read serves all four callers, so each of them
    now reads the record: `prd-signoff.py` status (and its post-commit re-read after a stamp), `to-pipeline-gate.py`
    LIMB 6, `prd-header-notify.py` and `prd-stamp.py`. Their call shapes are unchanged.

    The dir is placed in its repository BY GIT: `git rev-parse --show-prefix`, run from its parent (the PRD's own dir),
    gives the repository-relative path, never os.path.relpath. A Windows 8.3 short path (`ANDREW~1`) against git's
    long `--show-toplevel` made relpath climb out of the repo, and the read silently came back empty (measured by this
    function's own self-test in a tempdir). It is then listed with `git ls-tree` and read with `git show <ref>:<path>`
    from the toplevel. A missing dir at `ref` reads {}. When git cannot
    answer, the read also returns {} -- no signature -- so it fails toward the law, never toward admission. An entry git
    lists but cannot show, or that does not parse, reads None, which evaluate() already refuses as not readable."""
    import subprocess
    files = {}
    parent = os.path.dirname(os.path.abspath(signoff_dir))
    if not os.path.isdir(parent):
        return files

    # A GIT HOOK EXPORTS ITS REPOSITORY, AND THAT MUST NOT STEER THIS READ. Inside a commit hook, git sets GIT_DIR (and
    # GIT_INDEX_FILE, and sometimes GIT_WORK_TREE), and a child git honours them over its cwd. In a LINKED worktree that
    # made --show-prefix answer for the wrong tree, and the read came back empty: to-pipeline-gate LIMB 6 refused a tree
    # issuance with "PRD has NO sign-off" while status in the same worktree read ADMITTED (2.0.0_SA_COO~G, 2026-09-15).
    # So the repository is found from the PRD's own directory, and git's location variables are removed for these reads.
    _env = {k: v for k, v in os.environ.items()
            if k not in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_PREFIX", "GIT_COMMON_DIR")}

    def _git(args, cwd):
        return subprocess.run(["git"] + args, cwd=cwd, capture_output=True, text=True, encoding="utf-8",
                              errors="replace", timeout=60, env=_env)
    try:
        top = _git(["rev-parse", "--show-toplevel"], parent)
        pre = _git(["rev-parse", "--show-prefix"], parent)
        if top.returncode != 0 or not top.stdout.strip() or pre.returncode != 0:
            return files
        root = top.stdout.strip()
        rel = pre.stdout.strip() + os.path.basename(os.path.normpath(signoff_dir))
        ls = _git(["ls-tree", "--name-only", ref, "--", rel + "/"], root)
    except Exception:  # noqa: BLE001
        return files
    if ls.returncode != 0:
        return files
    for p in sorted(x.strip() for x in ls.stdout.splitlines() if x.strip()):
        n = p.rsplit("/", 1)[-1]
        if not n.endswith(".json"):
            continue
        try:
            r = _git(["show", "%s:%s" % (ref, p)], root)
            files[n] = json.loads(r.stdout) if r.returncode == 0 else None
        except Exception:  # noqa: BLE001
            files[n] = None
    return files


# ---------------------------------------------------------------- vintage boundary

L4R_LAW_COMMIT = "f8337502a9"     # the commit that landed L4-R (spine v3.14, 2026-09-10T21:33Z)
_LAW_EPOCH = {}


def law_epoch(root):
    """Committer epoch of the L4-R law commit (read once per root). 0 if unreadable -- then NOTHING is
    grandfathered: an unreadable boundary fails toward the law, never toward exemption."""
    if root not in _LAW_EPOCH:
        import subprocess
        try:
            r = subprocess.run(["git", "show", "-s", "--format=%ct", L4R_LAW_COMMIT], cwd=root, capture_output=True, text=True)
            _LAW_EPOCH[root] = int(r.stdout.strip()) if r.returncode == 0 and r.stdout.strip().isdigit() else 0
        except Exception:  # noqa: BLE001
            _LAW_EPOCH[root] = 0
    return _LAW_EPOCH[root]


def last_commit_epoch(root, rel):
    import subprocess
    try:
        r = subprocess.run(["git", "log", "-1", "--format=%ct", "--", rel], cwd=root, capture_output=True, text=True)
        return int(r.stdout.strip()) if r.returncode == 0 and r.stdout.strip().isdigit() else 0
    except Exception:  # noqa: BLE001
        return 0


def bound_by_law(root, prd_rel):
    """(bound: bool, detail). A PRD whose last commit predates the law commit is GRANDFATHERED -- its round was
    cut under the law at its cut (spine v3.13) -- and the first bump after the law binds it."""
    law = law_epoch(root)
    last = last_commit_epoch(root, prd_rel)
    if law and last and last < law:
        return False, "last commit predates the L4-R law commit %s; grandfathered until the next prd_version bump" % L4R_LAW_COMMIT
    return True, "bound"


# ---------------------------------------------------------------- liveness and routing

LIVE_SECONDS = 120                # the broker's STALE_THRESHOLD (org/mcp/server.py): no heartbeat for 2 min = not live


def live_serials(root, now=None):
    """Serials the broker's liveness store shows as LIVE (heartbeat within LIVE_SECONDS). A missing or
    unreadable store reads as NOBODY live -- routing then falls to the primary, never to a guess."""
    import time
    p = os.path.join(root, "org", "mcp", "liveness.json")
    try:
        with open(p, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    except Exception:  # noqa: BLE001
        return set()
    now = now or time.time()
    return {s for s, info in data.items() if isinstance(info, dict) and now - float(info.get("last_seen_epoch", 0) or 0) < LIVE_SECONDS}


def route_half(half, live, coo_lane_of_project=None, overdue=False, designated=None, fabric=None):
    """(serial, reason) -- who is ASKED to sign `half` right now. The ratified-text half always goes to the
    CVO (base or its live lane). The brief half goes to the CRO when a CRO base/lane is live; else, or when the
    CRO is OVERDUE on it, to a live 2.0.0_SA_COO instance that is NOT this project's round holder; else to the
    CRO base anyway (a message to a dead base is a hole, so the reason says so and the notifier keeps re-offering).

    THE PROJECT'S FABRIC PICKS AMONG LIVE LANES FIRST (row AMGT_RESAPP-Z-S102, measured on site Z by
    0.0.0_AB_MSTR~Z). The pick used to be alphabetical after the base, so with both ~W and ~Z lanes live a site-Z
    project's sign-off went to ~W. `fabric` is the project row's field (census: 'laptop', 'site-z', or absent). A
    'site-z' project prefers a ~Z lane; any other project prefers a lane that is not ~Z. Within that, the base
    comes first, then alphabetical order, which is unchanged whenever only one fabric's lanes are live."""
    want_z = str(fabric or "").strip().lower() in ("site-z", "sitez")

    def _is_z(s):
        return ("~" in s) and s.split("~", 1)[1].upper().startswith("Z")

    def live_of(base):
        return sorted([s for s in live if base_serial(s) == base], key=lambda x: (_is_z(x) != want_z, x != base, x))
    if half == "ratified-text":
        c = live_of("3.0.0_SA_CVO")
        return (c[0] if c else "3.0.0_SA_CVO"), ("live" if c else "no live CVO session; the base is addressed, which is a hole until a session is live; re-offer continues")
    if designated:
        return str(designated), ("designated on the project row (Andrew's word); the CRO is not asked" +
                                 ("" if str(designated) in live else "; no live session, which is a hole until one is; re-offer continues"))
    cro = live_of("4.0.0_SA_CRO")
    if cro and not overdue:
        return cro[0], "live"
    coo = [s for s in live_of("2.0.0_SA_COO") if s != str(coo_lane_of_project or "")]
    if coo:
        return coo[0], ("CRO overdue; COO in its stead" if overdue and cro else "no live CRO session; COO in its stead")
    return (cro[0] if cro else "4.0.0_SA_CRO"), ("CRO overdue and no eligible COO live; CRO re-asked" if cro else "no live CRO or eligible COO; the CRO base is addressed, which is a hole until a session is live; re-offer continues")


# ---------------------------------------------------------------- self-test (pure)

def self_test():
    fails = 0
    def arm(name, ok):
        nonlocal fails
        print("  %-7s %s" % ("OK" if ok else "DEFECT", name))
        fails += int(not ok)
    prd = ('# T\n\n```json\n{"prd_version": "v0.4"}\n```\n\nPreamble.\n\n## ENDPOINT (step 2, `/endpoint --forward`)\n\n```\n  FWD-1  x\n## not a heading (in fence)\n```\n\n'
           '## CELL CANDIDATES\n\n| a |\n\n## CONTRACTS\n\n| c |\n\n## PATHS\n\n| p |\n')
    h = half_hashes(prd)
    arm("two halves hashed, distinct", len(h) == 2 and h["brief"] != h["ratified-text"])
    arm("a '## ' line inside a fence is not a heading", len([t for t, _ in top_sections(prd) if t]) == 4)
    prd_v5 = prd.replace('"v0.4"', '"v0.5"')
    arm("a version-only bump changes NEITHER half hash", half_hashes(prd_v5) == h)
    prd_ep = prd.replace("FWD-1  x", "FWD-1  y")
    arm("an ENDPOINT edit changes the ratified-text half only", half_hashes(prd_ep)["ratified-text"] != h["ratified-text"] and half_hashes(prd_ep)["brief"] == h["brief"])
    prd_cell = prd.replace("| a |", "| a2 |")
    arm("a CELL CANDIDATES edit changes the brief half only", half_hashes(prd_cell)["brief"] != h["brief"] and half_hashes(prd_cell)["ratified-text"] == h["ratified-text"])
    arm("CRLF / trailing-space noise changes no hash", half_hashes(prd.replace("\n", "\r\n").replace("| p |", "| p |   ")) == h)
    arm("backtick-wrapped heading still ratified-text", half_of_section("ENDPOINT (step 2, `/endpoint --forward`)") == "ratified-text")
    cro = build_doc("T_PRD.md", prd, "abc", "brief", "SIGNED", "r@1", "4.0.0_SA_CRO")
    cvo = build_doc("T_PRD.md", prd, "abc", "ratified-text", "SIGNED", "r@1", "3.0.0_SA_CVO~Z")
    r = evaluate(prd, {"4.0.0_SA_CRO.json": cro, "3.0.0_SA_CVO.json": cvo})
    arm("both halves SIGNED at current bytes -> admitted (CVO via ~Z lane)", r["admitted"])
    r = evaluate(prd_v5, {"4.0.0_SA_CRO.json": cro, "3.0.0_SA_CVO.json": cvo})
    arm("a version-only bump keeps BOTH signatures (half-bound, not version-bound)", r["admitted"])
    r = evaluate(prd_ep, {"4.0.0_SA_CRO.json": cro, "3.0.0_SA_CVO.json": cvo})
    arm("an ENDPOINT edit re-opens the CVO half only", r["halves"]["ratified-text"]["state"] == "STALE" and r["halves"]["brief"]["state"] == "SIGNED" and not r["admitted"])
    arm("...and violations() names that half only", len(violations("t", "X", "p", r)) == 1 and "ratified-text half reads STALE" in violations("t", "X", "p", r)[0])
    legacy_cro = {"prd": "T_PRD.md", "prd_version": "v0.4", "prd_pin": "abc", "verdict": "SIGNED", "review_ref": "r", "signed_by": "4.0.0_SA_CRO", "signed_at": "2026-09-10T21:35:52Z"}
    legacy_cvo = dict(legacy_cro, signed_by="3.0.0_SA_CVO")
    r = evaluate(prd, {"4.0.0_SA_CRO.json": legacy_cro, "3.0.0_SA_CVO.json": legacy_cvo})
    arm("LEGACY files (no half/half_hash) infer the half and bind to prd_version -> admitted at v0.4", r["admitted"])
    r = evaluate(prd_v5, {"4.0.0_SA_CRO.json": legacy_cro, "3.0.0_SA_CVO.json": legacy_cvo})
    arm("...and a bump re-opens legacy files (they are version-bound by construction)", not r["admitted"] and r["halves"]["brief"]["state"] == "STALE")
    coo = build_doc("T_PRD.md", prd, "abc", "brief", "SIGNED", "r@1", "2.0.0_SA_COO", substitute_for="4.0.0_SA_CRO")
    r = evaluate(prd, {"2.0.0_SA_COO.json": coo, "3.0.0_SA_CVO.json": cvo})
    arm("2.0.0_SA_COO may sign the BRIEF half in the CRO's stead", r["admitted"] and r["halves"]["brief"]["by"] == "2.0.0_SA_COO")
    coo_lane = build_doc("T_PRD.md", prd, "abc", "brief", "SIGNED", "r@1", "2.0.0_SA_COO~B", substitute_for="4.0.0_SA_CRO")
    r = evaluate(prd, {"2.0.0_SA_COO~B.json": coo_lane, "3.0.0_SA_CVO.json": cvo}, coo_lane_of_project="2.0.0_SA_COO~B")
    arm("the COO lane holding the project's round CANNOT sign its brief half (SoD)", not r["admitted"] and r["halves"]["brief"]["state"] == "NOT-PERMITTED")
    coo_rt = build_doc("T_PRD.md", prd, "abc", "ratified-text", "SIGNED", "r@1", "2.0.0_SA_COO")
    r = evaluate(prd, {"4.0.0_SA_CRO.json": cro, "2.0.0_SA_COO.json": coo_rt})
    arm("nobody substitutes for the CVO: a COO file on the ratified-text half is NOT-PERMITTED", not r["admitted"] and r["halves"]["ratified-text"]["state"] == "NOT-PERMITTED")
    cto = build_doc("T_PRD.md", prd, "abc", "ratified-text", "SIGNED", "r@1", "1.0.0_SA_CTO")
    r = evaluate(prd, {"4.0.0_SA_CRO.json": cro, "1.0.0_SA_CTO.json": cto})
    arm("the author cannot sign its own document", not r["admitted"])
    ref = build_doc("T_PRD.md", prd, "abc", "brief", "REFUSED", "r@2", "4.0.0_SA_CRO", reason="R1")
    ref["signed_at"] = "2099-01-01T00:00:00Z"
    r = evaluate(prd, {"4.0.0_SA_CRO.json": ref, "4.0.0_SA_CRO.old.json": cro, "3.0.0_SA_CVO.json": cvo})
    arm("the NEWEST file on a half wins: a later REFUSED beats an earlier SIGNED", not r["admitted"] and r["halves"]["brief"]["state"] == "REFUSED")
    r = evaluate(prd, {"4.0.0_SA_CRO.json": None, "3.0.0_SA_CVO.json": cvo})
    arm("an unreadable file refuses the PRD", not r["admitted"] and any("not readable" in v for v in violations("t", "X", "p", r)))
    live = {"3.0.0_SA_CVO", "4.0.0_SA_CRO~X", "2.0.0_SA_COO~B", "2.0.0_SA_COO~F"}
    arm("route: ratified-text -> the live CVO", route_half("ratified-text", live)[0] == "3.0.0_SA_CVO")
    arm("route: brief -> the live CRO lane when one is live", route_half("brief", live)[0] == "4.0.0_SA_CRO~X")
    arm("route: brief -> a live COO instance NOT holding the round when no CRO is live", route_half("brief", live - {"4.0.0_SA_CRO~X"}, coo_lane_of_project="2.0.0_SA_COO~B")[0] == "2.0.0_SA_COO~F")
    arm("route: brief -> COO when the CRO is OVERDUE", route_half("brief", live, coo_lane_of_project="2.0.0_SA_COO~B", overdue=True)[0] == "2.0.0_SA_COO~F")
    des_ok = designated_brief_signer({"l4r_brief_signer": {"serial": "2.0.0_SA_COO~D", "authority": "org/x/ANDREW_DIRECT_x.md@abc1234"}})
    des_nopin = designated_brief_signer({"l4r_brief_signer": {"serial": "2.0.0_SA_COO~D", "authority": "org/x/ANDREW_DIRECT_x.md"}})
    des_cvo = designated_brief_signer({"l4r_brief_signer": {"serial": "3.0.0_SA_CVO", "authority": "org/x/A.md@abc1234"}})
    arm("designation: serial + pinned authority is admitted", des_ok[0] == "2.0.0_SA_COO~D")
    arm("designation: an UNPINNED authority is ignored (a citation without a vintage is not a citation)", des_nopin[0] is None and "authority" in des_nopin[1])
    arm("designation: a non-brief-reviewer base is ignored", des_cvo[0] is None)
    arm("designation: absent field -> None", designated_brief_signer({})[0] is None)
    arm("permitted: the round-holding COO lane is REFUSED by default", not permitted_signer("brief", "2.0.0_SA_COO~D", coo_lane_of_project="2.0.0_SA_COO~D")[0])
    arm("permitted: the round-holding COO lane is ADMITTED when designated", permitted_signer("brief", "2.0.0_SA_COO~D", coo_lane_of_project="2.0.0_SA_COO~D", designated="2.0.0_SA_COO~D")[0])
    arm("permitted: a designation admits only THAT serial (another round holder still refused)", not permitted_signer("brief", "2.0.0_SA_COO~B", coo_lane_of_project="2.0.0_SA_COO~B", designated="2.0.0_SA_COO~D")[0])
    arm("permitted: a designation never lifts the author refusal", not permitted_signer("brief", "1.0.0_SA_CTO", designated="1.0.0_SA_CTO")[0])
    arm("permitted: a designation never reaches the ratified-text half", not permitted_signer("ratified-text", "2.0.0_SA_COO~D", designated="2.0.0_SA_COO~D")[0])
    des_doc = build_doc("T_PRD.md", prd, "abc", "brief", "SIGNED", "r@1", "2.0.0_SA_COO~D")
    arm("evaluate: designated round holder grades SIGNED", evaluate(prd, {"2.0.0_SA_COO~D.json": des_doc, "3.0.0_SA_CVO.json": cvo}, coo_lane_of_project="2.0.0_SA_COO~D", designated="2.0.0_SA_COO~D")["admitted"])
    arm("evaluate: the same file WITHOUT the designation grades NOT-PERMITTED", evaluate(prd, {"2.0.0_SA_COO~D.json": des_doc, "3.0.0_SA_CVO.json": cvo}, coo_lane_of_project="2.0.0_SA_COO~D")["halves"]["brief"]["state"] == "NOT-PERMITTED")
    arm("route: brief -> the DESIGNATED serial even with a live CRO", route_half("brief", live | {"2.0.0_SA_COO~D"}, coo_lane_of_project="2.0.0_SA_COO~D", designated="2.0.0_SA_COO~D")[0] == "2.0.0_SA_COO~D")
    arm("route: a designated serial with NO live session is named a hole", "hole" in route_half("brief", live, designated="2.0.0_SA_COO~D")[1])
    arm("route: ratified-text ignores the designation", route_half("ratified-text", live, designated="2.0.0_SA_COO~D")[0].startswith("3.0.0_SA_CVO"))
    arm("route: nobody live -> the primary base, with the hole named", route_half("brief", set())[0] == "4.0.0_SA_CRO" and "hole" in route_half("brief", set())[1])
    arm("route: the CVO is never substituted", route_half("ratified-text", {"2.0.0_SA_COO"})[0] == "3.0.0_SA_CVO")
    # FABRIC PREFERENCE (row AMGT_RESAPP-Z-S102): with both ~W and ~Z lanes live, a site-z project goes to ~Z; a project
    # with no fabric, or a laptop one, keeps the old order (alphabetical after the base), so ~W.
    two = {"4.0.0_SA_CRO~W", "4.0.0_SA_CRO~Z", "3.0.0_SA_CVO~W", "3.0.0_SA_CVO~Z"}
    arm("route FABRIC: a site-z project's brief half goes to the ~Z CRO lane, not ~W", route_half("brief", two, fabric="site-z")[0] == "4.0.0_SA_CRO~Z")
    arm("route FABRIC: a site-z project's ratified-text half goes to the ~Z CVO lane", route_half("ratified-text", two, fabric="site-z")[0] == "3.0.0_SA_CVO~Z")
    arm("route FABRIC: no fabric -> the old order (~W), so a laptop routing is unchanged", route_half("brief", two)[0] == "4.0.0_SA_CRO~W"
        and route_half("brief", two, fabric="laptop")[0] == "4.0.0_SA_CRO~W")
    arm("route FABRIC: a site-z project's COO fallback prefers a ~Z COO lane, never its own round holder",
        route_half("brief", {"2.0.0_SA_COO~A", "2.0.0_SA_COO~ZZZ", "2.0.0_SA_COO~ZZ"}, coo_lane_of_project="2.0.0_SA_COO~ZZ", fabric="site-z")[0] == "2.0.0_SA_COO~ZZZ")
    # A SIGNATURE IS A COMMITTED FILE (row LGIC_NAMING-S14). The doctored pair runs in a THROWAWAY repo, so no real signoff
    # dir is touched: a committed SIGNED file is read, the same SIGNED content left uncommitted is not, and a worktree edit
    # to a committed file is not read either.
    import shutil
    import subprocess
    import tempfile
    tmp, bare = tempfile.mkdtemp(prefix="signoff-head-"), tempfile.mkdtemp(prefix="signoff-norepo-")
    try:
        def g(*a):
            return subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", "-c", "core.autocrlf=false"] + list(a),
                                  cwd=tmp, capture_output=True, text=True)
        g("init", "-q")
        sd = os.path.join(tmp, "prd", SIGNOFF_DIR)
        os.makedirs(sd)
        os.makedirs(os.path.join(tmp, "prd2"))
        with open(os.path.join(sd, "3.0.0_SA_CVO.json"), "w", encoding="utf-8") as fh:
            json.dump(cvo, fh)
        g("add", "-A")
        committed = g("commit", "-q", "-m", "the committed signoff").returncode == 0
        with open(os.path.join(sd, "4.0.0_SA_CRO.json"), "w", encoding="utf-8") as fh:
            json.dump(cro, fh)
        at_head = read_signoff_files(sd)
        in_worktree = {n: json.load(open(os.path.join(sd, n), encoding="utf-8")) for n in sorted(os.listdir(sd))}
        arm("S14 positive control: a COMMITTED signoff is read at HEAD", committed and (at_head.get("3.0.0_SA_CVO.json") or {}).get("verdict") == "SIGNED")
        arm("S14 doctored pair: the same SIGNED content left UNCOMMITTED is NOT read", "4.0.0_SA_CRO.json" not in at_head and "4.0.0_SA_CRO.json" in in_worktree)
        arm("S14 discrimination: the HEAD read WITHHOLDS (brief owed) where the old worktree read would ADMIT",
            not evaluate(prd, at_head)["admitted"] and evaluate(prd, in_worktree)["admitted"])
        with open(os.path.join(sd, "3.0.0_SA_CVO.json"), "w", encoding="utf-8") as fh:
            json.dump(dict(cvo, verdict="REFUSED"), fh)
        arm("S14: a worktree EDIT to a committed signoff is not read -- HEAD's bytes win", (read_signoff_files(sd).get("3.0.0_SA_CVO.json") or {}).get("verdict") == "SIGNED")
        arm("S14: a signoff dir absent at HEAD reads {}", read_signoff_files(os.path.join(tmp, "prd2", SIGNOFF_DIR)) == {})
        os.makedirs(os.path.join(bare, "prd"))
        arm("S14: a dir outside any repository reads {} (no signature: fails toward the law)", read_signoff_files(os.path.join(bare, "prd", SIGNOFF_DIR)) == {})
        # THE HOOK ENVIRONMENT (2.0.0_SA_COO~G, 2026-09-15): a commit hook exports GIT_DIR/GIT_INDEX_FILE, and in a
        # LINKED worktree the read came back empty, so LIMB 6 refused a signed PRD. Both arms set the variables a hook
        # sets, pointing somewhere else, and the read must still find the PRD's own committed signoff.
        wt = os.path.join(tmp, "linked")
        g("worktree", "add", "-q", wt, "HEAD")
        wt_sd = os.path.join(wt, "prd", SIGNOFF_DIR)
        saved = {k: os.environ.get(k) for k in ("GIT_DIR", "GIT_INDEX_FILE", "GIT_WORK_TREE")}
        try:
            os.environ["GIT_DIR"] = os.path.join(bare, "not-a-repo.git")
            os.environ["GIT_INDEX_FILE"] = os.path.join(bare, "not-an-index")
            arm("S14 HOOK ENV: GIT_DIR/GIT_INDEX_FILE exported elsewhere -> the primary checkout still reads its committed signoff",
                "3.0.0_SA_CVO.json" in read_signoff_files(sd))
            arm("S14 HOOK ENV, LINKED WORKTREE: the same variables -> the linked worktree reads its committed signoff",
                "3.0.0_SA_CVO.json" in read_signoff_files(wt_sd))
        finally:
            for k, v in saved.items():
                if v is None:
                    os.environ.pop(k, None)
                else:
                    os.environ[k] = v
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        shutil.rmtree(bare, ignore_errors=True)
    live = read_signoff_files(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                           "org", "missions", "D14", "LGIC", "LGIC_NAMING", "prd", SIGNOFF_DIR))
    arm("S14 LIVE: LGIC_NAMING's real signoff dir reads its committed files at HEAD (>= 2, every one parsed)",
        len(live) >= 2 and all(v is not None for v in live.values()))
    print("prd_signoff_lib self-test: %d defect(s)" % fails)
    return fails


if __name__ == "__main__":
    import sys
    sys.exit(1 if self_test() else 0)
