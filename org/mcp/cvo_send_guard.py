#!/usr/bin/env python3
"""cvo_send_guard -- the L8 correspondence guard of the canonical fabric workflow.

Spine (org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md v3.1, L8 and section 2): the CVO sends nothing to anyone
during a round; its findings travel up in the slug at L10, to 1.0.0_SA_CTO and to no one else, and reach
2.0.0_SA_COO through the CTO's round-N analysis. A worker never hears from the CVO. So the CVO's ONE admitted
send is to the CTO, at EVERY dep_stage -- the v2.1 rule (refuse CVO -> Tier-2 only while a tree project reads
EXECUTING; admit CVO -> COO) had two holes the round-1 step logs measured: the CVO -> COO stream of findings
mid-round, and the ROUND_CLOSE window in which a CVO -> Tier-2 send was admitted. Both close by removing the
stage condition rather than adding a stage (CRO v3 spec s.5 / s.8; Andrew-direct 2026-09-03 ~22:2xZ at the
CRO terminal, "the mechanisms right now", item 7).

WHY A REFUSAL: an announced message still reaches the recipient, and the harm is the recipient acting on it.
WHY THE WHOLE SEND: a per-recipient partial delivery would let a "cc" to the CTO carry the same body to the
COO or a worker; either every recipient is lawful or the seat did not send, and nothing is written.

Two halves, kept apart so a harness exercises the decision without a repo:
  executing_tree_projects(repo_root)      the ONE I/O read -- every org/missions/D*/*/*/project.json and its
                                          dep_stage; (None, note) when the census cannot run. Under v3 it
                                          DECIDES nothing (the rule is stage-free); it is read for the refusal
                                          text's context and kept for the daemon's health line.
  cvo_worker_send_refusal(from, to, exe)  PURE decision -- the refusal text, or None to admit. Signature unchanged
                                          so both callers keep working: org/mcp/server.py send_message (the MCP
                                          tool, which codex-send.py also uses) and org/mcp/broker.py /send-message
                                          (the daemon's HTTP path). APPLIED on the MCP path at each session's
                                          server load and on the daemon path at the broker's restart -- a
                                          running process holds the module it imported.
THE ONE OTHER ADMITTED CLASS (3.0.0_SA_CVO's constitutional review of spine v3.2-v3.5, F1, 94134; ruled by the
gate's owner 1.0.0_SA_CTO 2026-09-04 ~07:5xZ): the same-turn BROADCAST of an Andrew-direct spoken at the CVO's
terminal, which CLAUDE.md's law-edit clause and org/XXX.md require of every seat -- a relay of his verbatim word is
not an engagement with a limb, and it is the class the "engagement by message" exclusion was never aimed at. The
guard admits such a send to any recipient iff BOTH: the subject opens with the ANDREW-DIRECT marker AND the body
names the record's path under the CVO's OWN home (org/tier1_exec/3.0.0_SA_CVO[~lane]/deliverables/ANDREW_DIRECT_*.md).
The marker alone is a word; the path alone is a citation; together they are the record the law names. Callers pass
subject and body as keywords; a caller that passes neither gets the v3.1 verdict unchanged.
Self-test: python org/mcp/cvo_send_guard.py --self-test (red and green arms, plus one live census).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

CVO_SERIAL = "3.0.0_SA_CVO"
CTO_SERIAL = "1.0.0_SA_CTO"
LOOP_STAGE = "EXECUTING"
UP_ROUTE = "1.0.0_SA_CTO, in the slug at L10 (spine v3.1 L8: the CVO's one send of a round)"
# The same expression as .tools/to-pipeline-gate.py TIER01_RE: Tier-0 is 0.0.<n>_<XX>_..., Tier-1 is <n>.0.0_SA_...;
# a serial that resolves in org and matches neither is a Tier-2 worker for this guard's purpose.
TIER01_RE = re.compile(r"^(?:0\.0\.\d+_[A-Z]{2}_|\d+\.\d+\.\d+_SA_)")
PROJECT_GLOB = "D*/*/*/project.json"
ANDREW_DIRECT_MARKER_RE = re.compile(r"^\s*ANDREW[- _]DIRECT\b", re.I)
ANDREW_DIRECT_RECORD_RE = re.compile(
    r"org/tier1_exec/3\.0\.0_SA_CVO(?:~[A-Za-z0-9]+)?/deliverables/ANDREW_DIRECT_[A-Za-z0-9_.-]*\.md")


def andrew_direct_relay(subject, body) -> bool:
    """PURE. True iff the send is the CVO's same-turn broadcast of an Andrew-direct RECORD: the subject opens with
    the ANDREW-DIRECT marker and the body names the record's path under the CVO's own deliverables home."""
    return bool(ANDREW_DIRECT_MARKER_RE.match(subject or "")) and bool(ANDREW_DIRECT_RECORD_RE.search(body or ""))


def base_serial(serial: str) -> str:
    """The serial without its ~lane suffix; '' for an empty input."""
    return (serial or "").strip().split("~", 1)[0]


def is_tier2(serial: str) -> bool:
    b = base_serial(serial)
    return bool(b) and not TIER01_RE.match(b)


def executing_tree_projects(repo_root) -> tuple[list[str] | None, str]:
    """(codes, note): the tree projects whose project.json reads dep_stage == EXECUTING, with the denominator
    in the note. codes is None when the census could not run (missing tree, unreadable or unparseable file)."""
    missions = Path(repo_root) / "org" / "missions"
    if not missions.is_dir():
        return None, "org/missions/ not found under %s" % repo_root
    codes: list[str] = []
    n = 0
    for pj in sorted(missions.glob(PROJECT_GLOB)):
        n += 1
        try:
            d = json.loads(pj.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            return None, "%s unreadable or unparseable (%s: %s)" % (pj.as_posix(), type(exc).__name__, exc)
        if isinstance(d, dict) and d.get("dep_stage") == LOOP_STAGE:
            codes.append(pj.parent.name)
    return codes, "%d tree project(s) read" % n


def cvo_worker_send_refusal(from_agent: str, recipients, executing: tuple, subject=None, body=None) -> str | None:
    """PURE. spine v3.1 L8: a send from the CVO (any ~lane) is admitted only when EVERY recipient is the CTO
    (any ~lane), at every dep_stage. Any other recipient -- the COO, a Tier-2 seat, MSTR, the CRO -- refuses the
    WHOLE send. `executing` is read for context only; a census that cannot run does not change the verdict,
    because the verdict no longer depends on the stage."""
    if base_serial(from_agent) != CVO_SERIAL:
        return None
    recips = [r for r in (recipients or []) if (r or "").strip()]
    others = [r for r in recips if base_serial(r) != CTO_SERIAL]
    if not others:
        return None
    if andrew_direct_relay(subject, body):
        return None  # the law's own carrier: the same-turn broadcast of his recorded word (F1, 94134)
    codes, note = executing
    stage_word = ("census did not run (%s)" % note) if codes is None else (
        ("%d tree project(s) EXECUTING: %s" % (len(codes), ", ".join(codes))) if codes else "no tree project EXECUTING")
    return ("SEND REFUSED (spine v3.1 L8: the CVO's one send of a round is the slug to the CTO): %s -> %s. The CVO sends "
            "to %s and to no one else, at every dep_stage [%s; %s]. A finding for the COO reaches it through the CTO's "
            "round-N analysis; a worker never hears from the CVO. Nothing was written for ANY recipient of this send "
            "(%d named). Andrew-direct 2026-09-03 ~22:2xZ at the CRO terminal (item 7 of the eight v3 carriers)."
            % (from_agent, ", ".join(others), UP_ROUTE, stage_word, note, len(recips)))


# ---------------------------------------------------------------------------------------------------------------
# THE GENERALISED GUARD -- Andrew-direct ~13:1xZ-13:2xZ at the MSTR terminal, 2026-09-03 (LD-0529, "Mechanism works"):
# "why the fuck is a tier 2 agent Investigating? Not their fucking job. Their job is do task that was asked of them.
# Second, no open calls from tier2 agents anymore. That should be impossible, they should be on their orders and
# running that up to mgmt." ROOT, measured on the message record: three Tier-0/Tier-1 -> Tier-2 sends (93516, 93528,
# 93636) carried ACTS in their bodies -- "opens a change-management ledger entry NOW", "writes the rebuildability
# statement ... THEN the owner applies", "THE DECISION IS YOURS: apply the rule" -- and none was a task order: no face,
# no issuer, no acceptance, no bound. A worker that receives an ask with no order does exactly what followed.
#
# THE RULE: a send from a Tier-0 or Tier-1 seat to a Tier-2 seat whose text CARRIES AN ACT is REFUSED unless the text
# CITES A TASK ORDER ASSIGNED TO THAT RECIPIENT. The issuer's own dispatch passes (it cites its order); an ack or
# act-free information passes; a Tier-2 sender is never in scope here (its route UP is the point).
#   ACT   = a prescription naming the recipient or "the owner / steward / worker / assignee / seat" followed within a
#           clause by an act verb; or a sentence-initial imperative from the act-verb lexicon; or the ask markers
#           ("the decision is yours", "your act", "you must/should/need to/are to", "THE ASK", "RAVC", a bare "NOW").
#           This IS prose parsing, so it is bounded by the falsifier the record fixed: the three messages above must
#           refuse, a COO dispatch citing its order and a worker ack must pass; the battery below carries them as
#           real bytes read from the worker's inbox where present.
#   CITE  = a token <PROJECT>.TO-<id> whose task-order file exists under either root and whose <issued_to> is the
#           recipient (base serial). A citation of an order assigned to SOMEONE ELSE does not admit the send.
# Not decided by his words and NOT built here: a Tier-2 seat refusing an actless ask itself (item 1) and /open-calls
# refusing a Tier-2 serial at Step 0 (item 3) -- both stay proposals at Andrew.
TO_ID_RE = re.compile(r"\b([A-Z][A-Z0-9_]*\.TO-[A-Za-z0-9][A-Za-z0-9-]*)")
ISSUED_TO_RE = re.compile(r"<issued_to>\s*([^<\n]+?)\s*</issued_to>", re.I)
_ACT_VERBS = ("open", "write", "apply", "run", "cut", "fix", "revert", "investigate", "measure", "file", "commit",
              "deploy", "land", "remove", "add", "re-run", "rerun", "state", "seat", "spawn", "dispatch", "build",
              "update", "edit", "delete", "migrate", "rebuild", "verify", "confirm", "report", "send", "amend",
              "resolve", "disarm", "retire", "restart", "install", "scope", "re-plan", "replan", "grade", "close")
_VERB_ALT = "|".join(re.escape(v) for v in _ACT_VERBS)
# a present-tense prescription: "<who> ... opens|writes|applies" (3rd person -s), the recipient or an owner word
_PRESCRIBE_RE = re.compile(r"\b(the\s+(owner|steward|worker|assignee|seat)|%s)\b[^.\n:;]{0,60}?\b(%s)(s|es)\b",
                           re.I)
# a sentence-initial imperative (base form), optionally after a list marker or "please"
_IMPERATIVE_RE = re.compile(r"(?:^|[.:;!?]\s+|\n\s*)(?:\(?\d+\)?\.?\s*)?(?:please\s+)?(%s)\b(?!\s+(?:state|of|by|is|was|reads|read)\b)"
                            % _VERB_ALT, re.I | re.M)
_ASK_MARKER_RE = re.compile(r"\b(the decision is yours|your act|you (must|should|need to|are to|will)|THE ASK|RAVC|"
                            r"nothing is built until you|until you answer)\b|(?<![A-Za-z-])NOW(?![A-Za-z-])", re.I)


def carries_act(recipient: str, subject: str, body: str) -> list:
    """PURE. The act markers found in subject+body for this recipient ([] = act-free)."""
    text = "%s\n%s" % (subject or "", body or "")
    hits = []
    who = re.escape(base_serial(recipient))
    pres = re.compile(_PRESCRIBE_RE.pattern % (who, _VERB_ALT), re.I) if who else None
    if pres:
        for m in pres.finditer(text):
            hits.append("prescription: %r" % text[m.start():min(m.end(), m.start() + 90)].replace("\n", " "))
            if len(hits) >= 3:
                break
    for m in _IMPERATIVE_RE.finditer(text):
        hits.append("imperative: %r" % text[m.start():min(m.end() + 40, len(text))].strip().replace("\n", " "))
        if len(hits) >= 5:
            break
    for m in _ASK_MARKER_RE.finditer(text):
        hits.append("ask marker: %r" % m.group(0))
        if len(hits) >= 6:
            break
    return hits


def cited_orders_for(recipient: str, subject: str, body: str, repo_root) -> tuple:
    """(assigned, cited): the task-order ids the text cites that resolve to a file whose <issued_to> is the
    recipient, and every id cited. Reads the two roots; a file that cannot be read counts as not assigned."""
    text = "%s\n%s" % (subject or "", body or "")
    cited = sorted(set(TO_ID_RE.findall(text)))
    assigned = []
    root = Path(repo_root)
    for tok in cited:
        code = tok.split(".", 1)[0]
        hits = list(root.glob("org/*/*/task_orders/%s*.md" % tok)) + list(root.glob("org/*/task_orders/%s*.md" % tok)) \
            + list(root.glob("org/missions/D*/*/%s/task-orders/%s*.md" % (code, tok)))
        for p in hits:
            try:
                m = ISSUED_TO_RE.search(p.read_text(encoding="utf-8", errors="replace"))
            except OSError:
                continue
            if m and base_serial(m.group(1)) == base_serial(recipient):
                assigned.append(tok)
                break
    return assigned, cited


def tier2_act_send_refusal(from_agent: str, recipients, subject: str, body: str, repo_root) -> str | None:
    """The generalised guard. None admits; a refusal text refuses the WHOLE send (nothing written for anyone)."""
    sender = base_serial(from_agent)
    if not sender or not TIER01_RE.match(sender):
        return None  # a Tier-2 sender is out of scope: its route up is the point
    workers = [r for r in (recipients or []) if is_tier2(r)]
    if not workers:
        return None
    problems = []
    for r in workers:
        acts = carries_act(r, subject, body)
        if not acts:
            continue
        assigned, cited = cited_orders_for(r, subject, body, repo_root)
        if assigned:
            continue
        problems.append((r, acts, cited))
    if not problems:
        return None
    lines = []
    for r, acts, cited in problems:
        lines.append("  -> %s: act(s) found [%s]%s" % (
            r, "; ".join(acts[:3]),
            (" -- cites %s but none is assigned to this recipient" % ", ".join(cited)) if cited else " -- cites NO task order"))
    return ("SEND REFUSED (LD-0529, Andrew-direct 2026-09-03: a Tier-2 seat acts only on a task order in its own home): "
            "%s -> a Tier-2 seat with an ACT in the body and no task order assigned to that recipient cited.\n%s\n"
            "A worker hears an act only as a task order from its issuer: cut the order (2.0.0_SA_COO, L6) and cite its id "
            "(<PROJECT>.TO-<id>) in the GO; information with no act, and acks, pass as they are. Nothing was written for "
            "ANY recipient of this send (%d named)." % (from_agent, "\n".join(lines), len(recipients or [])))


def _self_test() -> int:
    exe = (["NFRA_COMPEFFICACY"], "1 tree project(s) read")
    idle = ([], "1 tree project(s) read")
    closing = (["NFRA_COMPEFFICACY"], "1 tree project(s) read; ROUND_CLOSE elsewhere")  # the window v2.1 left open
    dead = (None, "git ls-files rc=128")
    ref = cvo_worker_send_refusal
    arms = [
        # ---- spine v3.1 L8: the CVO's one send is the slug to the CTO, at every stage ----
        ("CVO -> CTO while EXECUTING: admitted (the slug)", lambda: ref("3.0.0_SA_CVO", ["1.0.0_SA_CTO"], exe) is None),
        ("CVO -> CTO with no project EXECUTING: admitted", lambda: ref("3.0.0_SA_CVO", ["1.0.0_SA_CTO"], idle) is None),
        ("CVO~A -> CTO~Z: admitted (tilde-blind on both ends)", lambda: ref("3.0.0_SA_CVO~A", ["1.0.0_SA_CTO~Z"], exe) is None),
        ("CVO -> COO while EXECUTING: REFUSED (v2.1 admitted this; the round-1 finding stream)",
         lambda: (lambda r: r is not None and "2.0.0_SA_COO" in r and "one send" in r)(ref("3.0.0_SA_CVO", ["2.0.0_SA_COO"], exe))),
        ("CVO -> COO at ROUND_CLOSE: REFUSED (stage-free)", lambda: ref("3.0.0_SA_CVO", ["2.0.0_SA_COO"], closing) is not None),
        ("CVO -> COO with no project EXECUTING: REFUSED (stage-free)", lambda: ref("3.0.0_SA_CVO", ["2.0.0_SA_COO"], idle) is not None),
        ("CVO -> Tier-2 while EXECUTING: REFUSED, names the recipient",
         lambda: (lambda r: r is not None and "0.8.0_AE_CloudComp" in r)(ref("3.0.0_SA_CVO", ["0.8.0_AE_CloudComp"], exe))),
        ("CVO -> Tier-2 at ROUND_CLOSE: REFUSED (the window v2.1 left open)", lambda: ref("3.0.0_SA_CVO", ["0.7.0_AE_CloudOps"], closing) is not None),
        ("CVO -> Tier-2 with no project EXECUTING: REFUSED (v2.1 admitted this)", lambda: ref("3.0.0_SA_CVO", ["0.8.0_AE_CloudComp"], idle) is not None),
        ("CVO~A -> Tier-2~B: REFUSED", lambda: ref("3.0.0_SA_CVO~A", ["0.8.0_AE_CloudComp~B"], exe) is not None),
        ("CVO -> [CTO, COO]: the WHOLE send refused (a cc does not launder)", lambda: ref("3.0.0_SA_CVO", ["1.0.0_SA_CTO", "2.0.0_SA_COO"], exe) is not None),
        ("CVO -> [CTO, Tier-2]: the WHOLE send refused", lambda: ref("3.0.0_SA_CVO", ["1.0.0_SA_CTO", "0.7.0_AE_CloudOps"], exe) is not None),
        ("CVO -> MSTR: REFUSED (not the CTO)", lambda: ref("3.0.0_SA_CVO", ["0.0.0_AB_MSTR"], idle) is not None),
        ("CVO -> CRO: REFUSED (not the CTO)", lambda: ref("3.0.0_SA_CVO", ["4.0.0_SA_CRO"], idle) is not None),
        ("CVO -> COO, census could not run: still REFUSED (the verdict is stage-free, not fail-closed-by-census)",
         lambda: ref("3.0.0_SA_CVO", ["2.0.0_SA_COO"], dead) is not None),
        ("CVO -> CTO, census could not run: admitted (the census decides nothing under v3)",
         lambda: ref("3.0.0_SA_CVO", ["1.0.0_SA_CTO"], dead) is None),
        ("MSTR -> Tier-2 while EXECUTING: admitted here (not the CVO; LD-0529's guard below owns it)",
         lambda: ref("0.0.0_AB_MSTR", ["0.8.0_AE_CloudComp"], exe) is None),
        ("COO -> CVO: admitted here (the sender is not the CVO)", lambda: ref("2.0.0_SA_COO", ["3.0.0_SA_CVO"], exe) is None),
        ("CVO -> nobody (empty recipients): admitted (nothing to refuse)", lambda: ref("3.0.0_SA_CVO", [], exe) is None),
        # ---- F1 (94134): the same-turn broadcast of an Andrew-direct record is the law's own carrier ----
        ("CVO -> [COO, CRO, MSTR], subject ANDREW-DIRECT + the record path under the CVO's home: ADMITTED",
         lambda: ref("3.0.0_SA_CVO", ["2.0.0_SA_COO", "4.0.0_SA_CRO", "0.0.0_AB_MSTR"], exe,
                     subject="ANDREW-DIRECT at the 3.0.0_SA_CVO terminal ~05:0xZ, VERBATIM 'a for both'",
                     body="Record: org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_DIRECT_20260904_050xZ_A_FOR_BOTH.md @92af61a111.") is None),
        ("CVO~A with the record under its lane home: ADMITTED",
         lambda: ref("3.0.0_SA_CVO~A", ["2.0.0_SA_COO~A"], exe, subject="ANDREW-DIRECT at the CVO~A terminal",
                     body="org/tier1_exec/3.0.0_SA_CVO~A/deliverables/ANDREW_DIRECT_20260904_X.md") is None),
        ("MUTANT: the marker without a record path -> REFUSED (a word is not a record)",
         lambda: ref("3.0.0_SA_CVO", ["2.0.0_SA_COO"], exe, subject="ANDREW-DIRECT: he said so", body="no record") is not None),
        ("MUTANT: a record path without the marker -> REFUSED (a citation is not a broadcast)",
         lambda: ref("3.0.0_SA_CVO", ["2.0.0_SA_COO"], exe, subject="round-6 findings",
                     body="see org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_DIRECT_20260904_050xZ_A_FOR_BOTH.md") is not None),
        ("MUTANT: the marker + a record under ANOTHER seat's home -> REFUSED (the CVO relays its own terminal's word)",
         lambda: ref("3.0.0_SA_CVO", ["2.0.0_SA_COO"], exe, subject="ANDREW-DIRECT relay",
                     body="org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260904_0458Z_X.md") is not None),
        ("MUTANT: the marker mid-subject, not opening it -> REFUSED",
         lambda: ref("3.0.0_SA_CVO", ["2.0.0_SA_COO"], exe, subject="slug and ANDREW-DIRECT",
                     body="org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_DIRECT_20260904_X.md") is not None),
        ("a caller passing no subject/body: the v3.1 verdict unchanged (CVO -> COO refused)",
         lambda: ref("3.0.0_SA_CVO", ["2.0.0_SA_COO"], exe) is not None),
    ]
    # ---- the generalised guard: the falsifier the record fixed (LD-0529) ----
    root = Path(__file__).resolve().parents[2]
    inbox = root / "org" / "mcp" / "inbox" / "0.8.0_AE_CloudComp" / "read"

    def _msg(mid):
        for p in inbox.glob("*.md"):
            try:
                t = p.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            m = re.search(r"\*\*Msg-ID:\*\*\s*(\d+)", t)
            if m and m.group(1) == mid:
                subj = re.search(r"\*\*Subject:\*\*\s*(.*)", t)
                return (subj.group(1) if subj else ""), (t.split("\n\n", 1)[1] if "\n\n" in t else t)
        return None

    for mid, sender in (("93516", "0.0.0_AB_MSTR"), ("93528", "1.0.0_SA_CTO"), ("93636", "1.0.0_SA_CTO")):
        got = _msg(mid)
        if got is None:
            arms.append(("falsifier %s: message not on this device (arm skipped, stated)" % mid, lambda: True))
            continue
        s_, b_ = got
        arms.append(("falsifier %s (%s -> 0.8.0_AE_CloudComp, an act, no order) -> REFUSED" % (mid, sender),
                     lambda s_=s_, b_=b_, sender=sender: tier2_act_send_refusal(sender, ["0.8.0_AE_CloudComp"], s_, b_, root) is not None))
    go = _msg("92913")
    if go is not None:
        arms.append(("the COO's GO dispatch 92913 (cites NFRA_COMPEFFICACY.TO-CE-T-1, issued to the recipient) -> admitted",
                     lambda: tier2_act_send_refusal("2.0.0_SA_COO", ["0.8.0_AE_CloudComp"], go[0], go[1], root) is None))
    else:
        arms.append(("GO dispatch 92913 not on this device (arm skipped, stated)", lambda: True))
    arms += [
        ("an ack from a Tier-1 to a Tier-2 (no act) -> admitted",
         lambda: tier2_act_send_refusal("1.0.0_SA_CTO", ["0.8.0_AE_CloudComp"], "RE 93641: READ-acked",
                                        "1.0.0_SA_CTO -> 0.8.0_AE_CloudComp. 93641 READ-acked. For information only: the round-5 stamp landed. Nothing owed.", root) is None),
        ("an act citing an order assigned to ANOTHER recipient -> refused",
         lambda: tier2_act_send_refusal("1.0.0_SA_CTO", ["0.7.0_AE_CloudOps"], "x",
                                        "0.7.0_AE_CloudOps opens the ledger entry NOW; see NFRA_COMPEFFICACY.TO-CE-T-1.", root) is not None),
        ("a Tier-2 sender with an act -> out of scope (its route up is the point)",
         lambda: tier2_act_send_refusal("0.8.0_AE_CloudComp", ["0.7.0_AE_CloudOps"], "x", "Please apply the fix now.", root) is None),
        ("a Tier-1 -> Tier-1 act -> out of scope",
         lambda: tier2_act_send_refusal("1.0.0_SA_CTO", ["2.0.0_SA_COO"], "x", "2.0.0_SA_COO cuts the order NOW.", root) is None),
    ]
    failed = 0
    for name, fn in arms:
        ok = False
        try:
            ok = bool(fn())
        except Exception as exc:  # noqa: BLE001
            name += " (raised %s: %s)" % (type(exc).__name__, exc)
        print("  %s  %s" % ("PASS" if ok else "FAIL", name))
        failed += 0 if ok else 1
    root = Path(__file__).resolve().parents[2]
    codes, note = executing_tree_projects(root)
    print("  LIVE  executing_tree_projects(%s) -> %r (%s)" % (root.as_posix(), codes, note))
    print("RESULT: %d arm(s) failed of %d; live census %s" % (failed, len(arms), "ran" if codes is not None else "DID NOT RUN"))
    return 1 if failed or codes is None else 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(_self_test())
    print(__doc__)
