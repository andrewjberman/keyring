#!/usr/bin/env python3
"""prd-stamp -- the spine's STAMP instrument (Andrew-direct 2026-09-11, 1.0.0_SA_CTO~Z terminal,
VERBATIM: "The spine should not rely on CVO talking to you, it should simply mark the PRD with an
edit, same for COO, they should both run a script that signs it with their serial and a timestamp
somehow. that is the stronger mechanism, they run a script that stamps the PRD.").

WHAT IT IS. Each stage owner, on finishing their limb, runs this script. It records a SIGNED,
TIMESTAMPED stamp in the PRD's own tree. The NEXT owner reads the stamps (`status`) instead of
waiting for a broker message. The artifact carries the handoff; the inbox no longer has to.

WHY A SIDECAR FILE AND NOT AN EDIT TO THE .md. The PRD .md is lane ANY_CTO (owned-paths): the COO
and the CVO CANNOT commit an edit to it -- the lane gate refuses it, which is exactly why the L4-R
sign-off is already a sidecar file the CTO cannot write. So "mark the PRD" by a non-CTO owner is
STRUCTURALLY a sidecar in a lane they own. The stamp keeps every property Andrew named -- signed by
serial, timestamped, inside the PRD's tree, read by the next owner, no message -- while staying
lane-clean and contention-free (each owner writes its OWN file; two owners never edit one file).

  prd/stamps/<STAGE>[.r<N>].json   handoff-progression stamps (this file's new surface); lane
                                   TREE_PRD_STAMP (owned-paths); STAGE in L4/L5/L6/L8/L9/L10.
  prd/signoff/<base-serial>.json   the EXISTING L4-R review sign-off (spine v3.14); `sign` writes it
                                   in the format to-pipeline-gate.py LIMB 6 already validates, so a
                                   reviewer "signs by running a script" without a format change.

VERBS
  stamp <prd.md> --stage L10 [--round N] [--note "..."]
        Write prd/stamps/<STAGE>[.rN].json signed by $OPAL_AGENT_SERIAL. HARD-refuses if the signer
        is not the stage's canonical owner or the PRD/header cannot be read. Order (predecessor
        present) is ADVISORY -- it WARNs and proceeds; the stamp is a signal, not a gate (CLAUDE.md:
        do not manufacture an approval gate). Prints the safe-commit line to land it.
  sign  <prd.md> --verdict SIGNED|REFUSED [--review-ref <path@sha>]
        Write prd/signoff/<base>.json for the L4-R review. Only 4.0.0_SA_CRO / 3.0.0_SA_CVO may.
        prd_pin is the PRD's last-touching commit (what LIMB 6 checks); a REFUSED needs a review_ref.
  status <prd.md> [--json]
        Render the L4->L10 ladder from the stamp + sign-off files and name the NEXT stage, its owner,
        and what it waits on. THIS is what a downstream owner runs in place of a delivered message.
  --self-test
        Pure arms over ownership, ordering, pins and rendering. No writes, no git, no broker.

Identity is $OPAL_AGENT_SERIAL (the process carrier the identity rules name first), same as the
notifier; a stamp/sign is committed under the owner's own --author line, so the git author is the
signature and the file's signed_by must equal it (a downstream reader can compare the two).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

# --- the canonical ladder (Rule 27 / spine s.1 owners) ------------------------------------------
STAGE_OWNER = {
    "L4": "1.0.0_SA_CTO",    # PRD authored
    "L5": "2.0.0_SA_COO",    # decomposition + battery
    "L6": "2.0.0_SA_COO",    # task orders issued
    "L8": "3.0.0_SA_CVO",    # compilation
    "L9": "3.0.0_SA_CVO",    # adjudication
    "L10": "3.0.0_SA_CVO",   # slug
}
STAGE_ORDER = ["L4", "L5", "L6", "L8", "L9", "L10"]
STAGE_LABEL = {"L4": "authored", "L5": "decomposed", "L6": "issued",
               "L8": "compiled", "L9": "adjudicated", "L10": "slug"}
RECURRING = {"L8", "L9", "L10"}       # per-round; require --round
SIGNOFF_REVIEWERS = ("4.0.0_SA_CRO", "3.0.0_SA_CVO")
FENCE_RE = re.compile(r"```json\s*(.*?)```", re.S)
# the sha the stamp attests to: the PRD .md BYTES (git-independent, deterministic, moves iff the
# bytes move -- stronger than a commit pin, which can move on a no-op recommit).
PIN_LEN = 12


def base_serial(s: str) -> str:
    return str(s or "").strip().split("~", 1)[0]


def utc_now() -> str:
    # real clock, minute grain, matches the COMPLETION_GRADES graded_utc pattern (...:MMZ).
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")


def content_pin(md_bytes: bytes) -> str:
    return hashlib.sha256(md_bytes).hexdigest()[:PIN_LEN]


def read_header(text: str):
    """The PRD_HEADER dict (first ```json fence), or None."""
    m = FENCE_RE.search(text or "")
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except ValueError:
        return None


def stamp_name(stage: str, rnd) -> str:
    return "%s.r%d.json" % (stage, int(rnd)) if stage in RECURRING and rnd is not None else "%s.json" % stage


def predecessor(stage: str):
    """The stage that must precede `stage` in STAGE_ORDER, or None for L4."""
    i = STAGE_ORDER.index(stage)
    return STAGE_ORDER[i - 1] if i > 0 else None


# --- filesystem helpers (impure; the pure core above is what the self-test drives) --------------
def _root() -> str:
    out = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True,
                         text=True, encoding="utf-8", errors="replace")
    return out.stdout.strip() if out.returncode == 0 and out.stdout.strip() else os.getcwd()


def _rel(root: str, path: str) -> str:
    ap = os.path.abspath(path)
    return os.path.relpath(ap, root).replace("\\", "/")


def _prd_dirs(prd_abs: str):
    d = os.path.dirname(prd_abs)
    return os.path.join(d, "stamps"), os.path.join(d, "signoff")


def _load_json_dir(d: str) -> dict:
    """{basename: parsed-json-or-None} for every *.json in d (missing dir -> {})."""
    import glob as _glob
    out = {}
    for fp in sorted(_glob.glob(os.path.join(d, "*.json"))):
        try:
            with open(fp, "r", encoding="utf-8") as fh:
                out[os.path.basename(fp)] = json.load(fh)
        except Exception:  # noqa: BLE001 -- an unreadable stamp is not a stamp; the reader flags it
            out[os.path.basename(fp)] = None
    return out


def _prd_last_commit(root: str, prd_rel: str) -> str:
    try:
        r = subprocess.run(["git", "log", "-1", "--format=%H", "--", prd_rel], cwd=root,
                           capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=30)
        return (r.stdout or "").strip()
    except Exception:  # noqa: BLE001
        return ""


def _read_prd(prd_abs: str):
    with open(prd_abs, "rb") as fh:
        raw = fh.read()
    header = read_header(raw.decode("utf-8", errors="replace"))
    return raw, header


def _dep_stage(root: str, code):
    """The register's dep_stage for `code`, read from the flat index (covers both tree and
    docs/architecture PRDs). None when unknown -- render_status then behaves as before."""
    if not code:
        return None
    p = os.path.join(root, "org", "projects", "%s.json" % code)
    try:
        with open(p, encoding="utf-8") as fh:
            return json.load(fh).get("dep_stage")
    except Exception:  # noqa: BLE001
        return None


def _signer():
    me = os.environ.get("OPAL_AGENT_SERIAL", "").strip()
    if not me:
        sys.exit("ERROR: OPAL_AGENT_SERIAL is not set; refusing to stamp/sign as nobody "
                 "(the stamp's signed_by must equal the committing seat).")
    return me


def _commit_hint(rel_path: str, me: str, what: str) -> str:
    return ("  land it:  .tools/safe-commit.sh --author \"%s <%s@opal.agent>\" -F <msg> -- %s\n"
            "            (%s; the commit author IS the signature -- it must be this serial)"
            % (me, me, rel_path, what))


# --- verbs --------------------------------------------------------------------------------------
def cmd_stamp(args) -> int:
    root = _root()
    prd_abs = os.path.abspath(args.prd)
    if not os.path.isfile(prd_abs):
        sys.exit("ERROR: no PRD at %s" % args.prd)
    stage = args.stage.upper()
    if stage not in STAGE_OWNER:
        sys.exit("ERROR: --stage %s is not one of %s" % (stage, "/".join(STAGE_ORDER)))
    if stage in RECURRING and args.round is None:
        sys.exit("ERROR: %s recurs per round; pass --round N" % stage)
    if stage not in RECURRING and args.round is not None:
        sys.exit("ERROR: %s is per-version, not per-round; drop --round" % stage)

    me = _signer()
    if base_serial(me) != STAGE_OWNER[stage]:
        sys.exit("ERROR: %s is owned by %s; %s cannot stamp it (Rule 27 / spine s.1). "
                 "A stamp signs your OWN limb." % (stage, STAGE_OWNER[stage], me))

    raw, header = _read_prd(prd_abs)
    if not header or not header.get("prd_version"):
        sys.exit("ERROR: %s has no PRD_HEADER fence with a prd_version -- cannot stamp a document "
                 "that is not a step-4 PRD." % args.prd)

    stamps_dir, signoff_dir = _prd_dirs(prd_abs)
    existing = _load_json_dir(stamps_dir)
    # ADVISORY order check -- WARN, never refuse (a stamp is a signal; CLAUDE.md forbids an agent-made gate).
    pred = predecessor(stage)
    if pred:
        want = stamp_name(pred, args.round if pred in RECURRING else None)
        if want not in existing:
            print("WARN: predecessor %s (%s) is not stamped yet -- proceeding, but the ladder is out of order."
                  % (pred, want))
    if stage == "L5":
        signed = _signed_reviewers(_load_json_dir(signoff_dir), header["prd_version"])
        missing = [r for r in SIGNOFF_REVIEWERS if r not in signed]
        if missing:
            print("WARN: L4-R sign-off not complete at %s (missing %s) -- the L6 gate will still refuse a "
                  "task order until both sign; proceeding to record the L5 stamp." % (header["prd_version"], ", ".join(missing)))

    doc = {
        "stage": stage,
        "signed_by": me,
        "utc": utc_now(),
        "prd_version": header["prd_version"],
        "prd_pin": content_pin(raw),
        "project": header.get("project"),
    }
    if stage in RECURRING:
        doc["round"] = int(args.round)
    if args.note:
        doc["note"] = args.note

    os.makedirs(stamps_dir, exist_ok=True)
    out_path = os.path.join(stamps_dir, stamp_name(stage, args.round))
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(doc, fh, indent=1, sort_keys=True)
        fh.write("\n")
    rel = _rel(root, out_path)
    print("OK: stamped %s %s by %s at %s (pin %s, %s)"
          % (stage, STAGE_LABEL[stage], me, doc["utc"], doc["prd_pin"], header["prd_version"]))
    print("    %s" % rel)
    print(_commit_hint(rel, me, "the %s handoff stamp" % stage))
    return 0


def cmd_sign(args) -> int:
    root = _root()
    prd_abs = os.path.abspath(args.prd)
    if not os.path.isfile(prd_abs):
        sys.exit("ERROR: no PRD at %s" % args.prd)
    me = _signer()
    if base_serial(me) not in SIGNOFF_REVIEWERS:
        sys.exit("ERROR: L4-R sign-off is %s only; %s cannot sign (the CTO cannot sign its own PRD)."
                 % (" / ".join(SIGNOFF_REVIEWERS), me))
    verdict = args.verdict.upper()
    if verdict not in ("SIGNED", "REFUSED"):
        sys.exit("ERROR: --verdict must be SIGNED or REFUSED")
    if verdict == "REFUSED" and not args.review_ref:
        sys.exit("ERROR: a REFUSED sign-off must name --review-ref <path@sha> (what the refusal points at).")

    raw, header = _read_prd(prd_abs)
    if not header or not header.get("prd_version"):
        sys.exit("ERROR: %s has no PRD_HEADER fence with a prd_version." % args.prd)
    prd_rel = _rel(root, prd_abs)
    last = _prd_last_commit(root, prd_rel)

    doc = {"signed_by": me, "verdict": verdict, "prd_version": header["prd_version"]}
    if last:
        doc["prd_pin"] = last[:PIN_LEN]     # LIMB 6 checks a prefix match against the PRD's last commit
    if args.review_ref:
        doc["review_ref"] = args.review_ref

    _, signoff_dir = _prd_dirs(prd_abs)
    os.makedirs(signoff_dir, exist_ok=True)
    out_path = os.path.join(signoff_dir, "%s.json" % base_serial(me))
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(doc, fh, indent=1, sort_keys=True)
        fh.write("\n")
    rel = _rel(root, out_path)
    if not last:
        print("WARN: could not read the PRD's last commit -- prd_pin omitted; LIMB 6 accepts an absent pin, "
              "but a later reader cannot tell the reviewed bytes from the current bytes.")
    print("OK: %s %s at %s%s" % (verdict, prd_rel, header["prd_version"],
                                 (" pin %s" % doc["prd_pin"]) if last else ""))
    print("    %s" % rel)
    print(_commit_hint(rel, me, "the L4-R %s sign-off" % verdict))
    return 0


def _signed_reviewers(signoff_files: dict, prd_version: str) -> set:
    """The base serials that SIGNED this exact prd_version (mirrors LIMB 6 / the notifier's predicate)."""
    out = set()
    for _name, doc in signoff_files.items():
        if not isinstance(doc, dict):
            continue
        b = base_serial(doc.get("signed_by"))
        if (b in SIGNOFF_REVIEWERS and str(doc.get("verdict") or "").upper() == "SIGNED"
                and str(doc.get("prd_version")) == str(prd_version)):
            out.add(b)
    return out


def render_status(header, cur_pin, stamps, signoffs, dep_stage=None):
    """PURE. -> (lines, next_stage_or_None). `stamps`/`signoffs` = {basename: doc}. `cur_pin` is the
    PRD's current content pin; a stamp whose prd_pin != cur_pin is STALE (PRD changed after stamping).
    `dep_stage` is the register's own state (REGISTERED/EXECUTING/CLOSED) -- an instrument the stamp
    ladder shares nothing with -- used ONLY to keep the NEXT line from asserting a start on a project
    the register says is already under way or done (see the pre-mechanism block below)."""
    ver = header.get("prd_version") if header else None
    lines = ["PRD STAMP LEDGER -- %s %s" % (header.get("project") if header else "?", ver or "?"),
             "  current content pin: %s" % cur_pin]
    # index stamps by (stage, round)
    by_key = {}
    for name, doc in stamps.items():
        if not isinstance(doc, dict) or doc.get("stage") not in STAGE_OWNER:
            lines.append("  ?? unreadable/foreign stamp file: %s" % name)
            continue
        by_key[(doc["stage"], doc.get("round"))] = doc
    signed_now = _signed_reviewers(signoffs, ver)
    next_stage = None
    for stage in STAGE_ORDER:
        # for recurring stages, show the highest round present (or absent)
        rounds = sorted([k[1] for k in by_key if k[0] == stage and k[1] is not None])
        keys = [(stage, r) for r in rounds] if stage in RECURRING else [(stage, None)]
        shown = False
        for key in keys:
            doc = by_key.get(key)
            if not doc:
                continue
            shown = True
            stale = doc.get("prd_pin") and doc.get("prd_pin") != cur_pin
            rlabel = " r%d" % key[1] if key[1] is not None else ""
            lines.append("  %-4s%-3s %-11s %-18s %s  %s  %s"
                         % (stage, rlabel, STAGE_LABEL[stage], doc.get("signed_by"), doc.get("utc"),
                            doc.get("prd_version"), "STALE-PIN" if stale else "pin OK"))
        if not shown:
            lines.append("  %-7s %-11s -- not stamped (owner %s)" % (stage, STAGE_LABEL[stage], STAGE_OWNER[stage]))
            if next_stage is None:
                next_stage = stage
        # sign-off ladder sits right after L4
        if stage == "L4":
            for who in SIGNOFF_REVIEWERS:
                got = [d for d in signoffs.values() if isinstance(d, dict) and base_serial(d.get("signed_by")) == who]
                cur = [d for d in got if str(d.get("prd_version")) == str(ver)]
                if cur:
                    d = cur[-1]
                    lines.append("  sign-off %-14s %-18s %s %s"
                                 % (who.split("_")[-1], d.get("signed_by"), d.get("verdict"), d.get("prd_version")))
                else:
                    lines.append("  sign-off %-14s -- not signed at %s (owner %s)" % (who.split("_")[-1], ver, who))
    # a NEXT that is L5 is really gated on the sign-offs
    # --- PRE-MECHANISM REGIME (found by 3.0.0_SA_CVO~Z + 2.0.0_SA_COO~Z on the read plane) ---------
    # A stamp can only exist from the mechanism's birth (@510ca8fe46) forward, so an UNSTAMPED limb on
    # a project the register says is already under way -- or closed -- is NOT "pending", it predates
    # the ledger. Without this, `status` on a CLOSED 19/19-REALIZED project printed "NEXT: L4, start
    # here", the render lying in the one output every seat is told to route off. dep_stage (the
    # register) is the discriminator; it shares nothing with the stamp ladder, which is why it can see
    # the defect the ladder cannot. Andrew-direct 2026-09-11: "you cant judge things on other fabrics
    # at other time based on a tool that was just created" -- so this does NOT backfill and does NOT
    # treat an empty ledger as a defect; it makes the RENDER DECLINE TO ASSERT a NEXT it cannot know.
    ds = str(dep_stage or "").upper()
    pre_mech = False
    if ds == "CLOSED":
        pre_mech = True
        next_stage = None
        lines.append("  register: CLOSED -- unstamped limbs predate the stamp mechanism; they are NOT pending")
    elif ds == "EXECUTING" and not by_key:
        pre_mech = True
        next_stage = None
        lines.append("  register: EXECUTING but ZERO stamps -- this PRD predates the stamp mechanism; the ladder "
                     "state before the first stamp is NOT CAPTURED (consult the register / dispatch, not this NEXT)")
    waits = ""
    if next_stage == "L5":
        missing = [r for r in SIGNOFF_REVIEWERS if r not in signed_now]
        waits = (" -- waiting on sign-off from %s" % ", ".join(missing)) if missing else " -- sign-offs complete; COO may decompose"
    if next_stage:
        lines.append("NEXT: %s (%s) -- owner %s%s" % (next_stage, STAGE_LABEL[next_stage], STAGE_OWNER[next_stage], waits))
    elif pre_mech:
        lines.append("NEXT: not asserted -- see the register line above (this PRD predates the stamp ledger).")
    else:
        lines.append("NEXT: ladder complete through L10 (round stamps recur per round).")
    return lines, next_stage


def cmd_status(args) -> int:
    prd_abs = os.path.abspath(args.prd)
    if not os.path.isfile(prd_abs):
        sys.exit("ERROR: no PRD at %s" % args.prd)
    raw, header = _read_prd(prd_abs)
    stamps_dir, signoff_dir = _prd_dirs(prd_abs)
    stamps = _load_json_dir(stamps_dir)
    signoffs = _load_json_dir(signoff_dir)
    cur_pin = content_pin(raw)
    dep = _dep_stage(_root(), (header or {}).get("project"))
    lines, nxt = render_status(header or {}, cur_pin, stamps, signoffs, dep)
    if args.json:
        print(json.dumps({"project": (header or {}).get("project"),
                          "prd_version": (header or {}).get("prd_version"),
                          "current_pin": cur_pin, "next_stage": nxt, "dep_stage": dep,
                          "stamps": stamps, "signoffs": signoffs}, indent=1, sort_keys=True))
    else:
        print("\n".join(lines))
    return 0


# --- self-test (pure; no writes, no git, no broker) ---------------------------------------------
def _self_test() -> int:
    fails = 0

    def check(name, cond):
        nonlocal fails
        ok = False
        try:
            ok = bool(cond())
        except Exception as exc:  # noqa: BLE001
            name += " (raised %s: %s)" % (type(exc).__name__, exc)
        print("  %s  %s" % ("PASS" if ok else "FAIL", name))
        fails += 0 if ok else 1

    check("base_serial strips the tilde lane", lambda: base_serial("3.0.0_SA_CVO~Z") == "3.0.0_SA_CVO")
    check("utc_now matches the minute-grain Z pattern",
          lambda: re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}Z$", utc_now()))
    check("content_pin is deterministic and 12 hex", lambda: content_pin(b"abc") == content_pin(b"abc")
          and len(content_pin(b"abc")) == 12 and re.match(r"^[0-9a-f]{12}$", content_pin(b"abc")))
    check("content_pin moves with the bytes", lambda: content_pin(b"abc") != content_pin(b"abd"))
    check("stamp_name: recurring stage carries the round", lambda: stamp_name("L10", 3) == "L10.r3.json")
    check("stamp_name: per-version stage has no round", lambda: stamp_name("L4", None) == "L4.json")
    check("predecessor: L4 has none, L5<-L4, L8<-L6, L10<-L9",
          lambda: predecessor("L4") is None and predecessor("L5") == "L4"
          and predecessor("L8") == "L6" and predecessor("L10") == "L9")
    check("STAGE_OWNER matches spine s.1 (L4 CTO, L5/L6 COO, L8/L9/L10 CVO)",
          lambda: STAGE_OWNER["L4"] == "1.0.0_SA_CTO" and STAGE_OWNER["L6"] == "2.0.0_SA_COO"
          and STAGE_OWNER["L10"] == "3.0.0_SA_CVO")
    # _signed_reviewers mirrors LIMB 6's predicate
    cro = {"signed_by": "4.0.0_SA_CRO", "verdict": "SIGNED", "prd_version": "v0.4"}
    cvo = {"signed_by": "3.0.0_SA_CVO~Z", "verdict": "SIGNED", "prd_version": "v0.4"}
    check("_signed_reviewers: both SIGNED at v0.4 (CVO via ~Z) -> both",
          lambda: _signed_reviewers({"a.json": cro, "b.json": cvo}, "v0.4") == {"4.0.0_SA_CRO", "3.0.0_SA_CVO"})
    check("_signed_reviewers: version-bound -- CVO signed v0.3 -> only CRO",
          lambda: _signed_reviewers({"a.json": cro, "b.json": dict(cvo, prd_version="v0.3")}, "v0.4") == {"4.0.0_SA_CRO"})
    check("_signed_reviewers: a REFUSED verdict signs nothing",
          lambda: _signed_reviewers({"b.json": dict(cvo, verdict="REFUSED")}, "v0.4") == set())
    check("_signed_reviewers: an unreadable file signs nothing",
          lambda: _signed_reviewers({"b.json": None}, "v0.4") == set())
    # render_status: a fresh PRD with only L4 stamped and no sign-offs -> NEXT is L5, waiting on both
    hdr = {"project": "P", "prd_version": "v0.4"}
    pin = "abc123abc123"
    l4 = {"stage": "L4", "signed_by": "1.0.0_SA_CTO~Z", "utc": "2026-09-11T01:00Z", "prd_version": "v0.4", "prd_pin": pin}
    lines, nxt = render_status(hdr, pin, {"L4.json": l4}, {})
    check("render_status: only L4 stamped, no sign-offs -> NEXT L5 waiting on both reviewers",
          lambda: nxt == "L5" and any("waiting on sign-off from 4.0.0_SA_CRO, 3.0.0_SA_CVO" in x for x in lines))
    # a stale pin is flagged
    lines2, _ = render_status(hdr, "deadbeefdead", {"L4.json": l4}, {})
    check("render_status: a stamp whose pin != current -> STALE-PIN",
          lambda: any("STALE-PIN" in x for x in lines2))
    # sign-offs complete -> NEXT L5 says COO may decompose
    lines3, nxt3 = render_status(hdr, pin, {"L4.json": l4}, {"a.json": cro, "b.json": cvo})
    check("render_status: both signed -> NEXT L5 'sign-offs complete; COO may decompose'",
          lambda: nxt3 == "L5" and any("COO may decompose" in x for x in lines3))
    # ladder complete through L10 (round 1) -> no NEXT
    full = {"L4.json": l4,
            "L5.json": dict(l4, stage="L5", signed_by="2.0.0_SA_COO~Z"),
            "L6.json": dict(l4, stage="L6", signed_by="2.0.0_SA_COO~Z"),
            "L8.r1.json": dict(l4, stage="L8", signed_by="3.0.0_SA_CVO~Z", round=1),
            "L9.r1.json": dict(l4, stage="L9", signed_by="3.0.0_SA_CVO~Z", round=1),
            "L10.r1.json": dict(l4, stage="L10", signed_by="3.0.0_SA_CVO~Z", round=1)}
    _, nxt4 = render_status(hdr, pin, full, {"a.json": cro, "b.json": cvo})
    check("render_status: full ladder through L10 -> no NEXT", lambda: nxt4 is None)
    # PRE-MECHANISM REGIME (the CVO/COO finding): a CLOSED project with no stamps must NOT say "start at L4"
    lc, nc = render_status(hdr, pin, {}, {}, dep_stage="CLOSED")
    check("render_status: CLOSED + no stamps -> NEXT suppressed, register:CLOSED line, no 'NEXT: L4'",
          lambda: nc is None and any("register: CLOSED" in x for x in lc) and not any(x.startswith("NEXT: L4") for x in lc))
    le, ne = render_status(hdr, pin, {}, {}, dep_stage="EXECUTING")
    check("render_status: EXECUTING + no stamps -> pre-mechanism, NEXT not asserted",
          lambda: ne is None and any("predates the stamp mechanism" in x for x in le))
    lr, nr = render_status(hdr, pin, {}, {}, dep_stage="REGISTERED")
    check("render_status: REGISTERED + no stamps -> NEXT L4 (correct; genuinely pre-PRD)", lambda: nr == "L4")
    lx, nx = render_status(hdr, pin, {"L4.json": l4}, {"a.json": cro, "b.json": cvo}, dep_stage="EXECUTING")
    check("render_status: EXECUTING WITH an L4 stamp -> mechanism in use, NEXT L5 (not suppressed)", lambda: nx == "L5")
    lu, nu = render_status(hdr, pin, {"L4.json": l4}, {}, dep_stage=None)
    check("render_status: dep_stage None + a stamp -> unchanged from pre-fix behavior (NEXT L5)", lambda: nu == "L5")
    print("prd-stamp self-test: %d fail(s) of the arms above" % fails)
    return 1 if fails else 0


def main(argv) -> int:
    ap = argparse.ArgumentParser(prog="prd-stamp", description="Stamp a PRD's spine handoffs (Andrew-direct 2026-09-11).")
    sub = ap.add_subparsers(dest="cmd")
    ap.add_argument("--self-test", action="store_true", help="run pure arms and exit")

    p_stamp = sub.add_parser("stamp", help="record a stage-completion stamp")
    p_stamp.add_argument("prd")
    p_stamp.add_argument("--stage", required=True)
    p_stamp.add_argument("--round", type=int, default=None)
    p_stamp.add_argument("--note", default=None)

    p_sign = sub.add_parser("sign", help="record an L4-R reviewer sign-off (CRO/CVO)")
    p_sign.add_argument("prd")
    p_sign.add_argument("--verdict", required=True)
    p_sign.add_argument("--review-ref", dest="review_ref", default=None)

    p_status = sub.add_parser("status", help="render the L4->L10 ladder and the next owner")
    p_status.add_argument("prd")
    p_status.add_argument("--json", action="store_true")

    args = ap.parse_args(argv)
    if args.self_test:
        return _self_test()
    if args.cmd == "stamp":
        return cmd_stamp(args)
    if args.cmd == "sign":
        return cmd_sign(args)
    if args.cmd == "status":
        return cmd_status(args)
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
