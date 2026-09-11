#!/usr/bin/env python3
"""prd-header-notify -- R3 of the canonical loop (step 4 -> step 5), release condition 7 -- and, since
2026-09-02 22:4xZ, R7 (step 10 -> the loop_target's owner) on the SAME durable READ-ack machinery:
a remediation row NEW in a commit, on either channel root, is offered to ROUTE_OWNER[loop_target]
and re-offered until READ. The file keeps its R3 name; `kind` on each outstanding row says which.

WHAT IT IS. When a commit lands a step-4 PRD whose PRD_HEADER is NEW or whose `prd_version` BUMPED,
deliver the exact identity -- project, version, commit SHA, path, status -- to 2.0.0_SA_COO through
the broker, and RE-OFFER until COO's agent-side READ ack. SENT != EMITTED != READ (CLAUDE.md;
surprise-watch.sh:32-33); success is READ and nothing short of it.

WHAT IT IS NOT (CVO~A @0d272d257c R3, accepted with this exact boundary): it NOTIFIES. It never cuts a
task order, never starts a decomposition, never re-aligns an endpoint. Andrew's words were "sent to
COO immediately for decomposition"; an auto-dispatcher would be a second dispatch path no gate covers,
so the narrowing was stated (design @3814be3317 R3) rather than quietly implemented, and CVO~A
accepted it conditionally on durable delivery + recipient ACK -- which is what this file does.

AUTHORIZATION. CLAUDE.md bans building any monitor/notifier unless Andrew explicitly asks. He asked:
memo 2026-09-02, "COO has a monitor ... once it's committed, it's sent to COO immediately". Third
moratorium widening, width recorded in the design (loop-internal monitors ONLY; no SNS/SES/alarm; no
data-freshness monitor).

MODES
  post-commit   for each docs/architecture/*_PRD.md in HEAD's commit: read HEAD's header and HEAD~1's;
                new-or-bumped -> send + record. Runs from the post-commit hook, backgrounded.
  reoffer       for each outstanding notification: query /delivery-state; READ -> retire; else if older
                than REOFFER_MINUTES -> resend (new message id), attempts += 1, up to MAX_ATTEMPTS.
                Also runs at every post-commit (cheap; the estate commits constantly), so re-offer is
                commit-driven in v1 -- stated, not hidden.
  status        print the outstanding table with each row's live delivery state.
  selftest      THE RC7 CONTROL: send a probe to THIS seat, assert /delivery-state is NOT READ, ack it
                through /ack-messages as this seat, assert it IS READ -- so "delivered" and "read" are
                proven to be different states on the live broker before anyone trusts this notifier.

Identity: sends go through org/mcp/codex-send.py, which refuses unless OPAL_AGENT_SERIAL names a LIVE
seat -- a post-commit hook inherits the committing seat's env, so the notification is from the seat
that landed the PRD. State: org/mcp/.prd-notify/outstanding.jsonl (one JSON object per line).
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time
import urllib.request

# LANE-HOMED RECIPIENT (2026-09-03, 1.0.0_SA_CTO on 0.0.0_AB_MSTR~Z's site-Z finding, relay 93296 item 2): the
# default used to be the BASE serial 2.0.0_SA_COO. On site Z the base inbox is unwatched, so the L4->L5 handoff
# read QUEUED at the base and 0 rows at 2.0.0_SA_COO~Z; on the laptop the ~A fabric had to set PRD_NOTIFY_TO by
# hand for the same reason. The rule now: the recipient is the COO ON THE COMMITTER'S OWN LANE -- the ~suffix of
# $OPAL_AGENT_SERIAL (the process carrier the identity rules name first) is appended to the base serial; a base
# committer still reaches the base COO; PRD_NOTIFY_TO, when set non-empty, wins outright. The same re-homing
# applies to the route owners below (kind:route), for the same reason.
def _lane_suffix():
    s = os.environ.get("OPAL_AGENT_SERIAL", "")
    return s[s.index("~"):] if "~" in s else ""


def _seat(base):
    """A base serial re-homed onto the committer's lane ('2.0.0_SA_COO' -> '2.0.0_SA_COO~Z' under a ~Z committer)."""
    return base + _lane_suffix()


RECIPIENT = os.environ.get("PRD_NOTIFY_TO") or _seat("2.0.0_SA_COO")
# L4-R -- THE PRD SIGN-OFF GATE (Andrew-direct 2026-09-10 ~21:2xZ: "CRO and CVO should have to sign off on PRD
# before COO gets it"; spine v3.14). On every new-or-bumped header the two REVIEWERS are notified; the COO
# delivery is WITHHELD until prd/signoff/<serial>.json from EACH reviewer reads SIGNED at that prd_version, and
# a commit that lands a sign-off re-checks and releases it. The L6 gate (to-pipeline-gate.py LIMB 6) refuses a
# task order against an unsigned PRD, so this notifier withholding is the FIRST carrier and the gate the second.
SIGNOFF_REVIEWERS = ("4.0.0_SA_CRO", "3.0.0_SA_CVO")
SIGNOFF_RE = re.compile(r"^(org/missions/D(?:0|[1-9][0-9]?)/[^/]+/[^/]+/prd)/signoff/[^/]+\.json$")


def _signed_serials(files, prd_version):
    """PURE. `files` = {basename: parsed-json-or-None}. The base serials that SIGNED this exact prd_version;
    a ~lane of a reviewer signs for its base serial; REFUSED, stale or unreadable files sign nothing."""
    out = set()
    for name, doc in files.items():
        if not isinstance(doc, dict):
            continue
        base = str(doc.get("signed_by") or "").split("~", 1)[0]
        if base in SIGNOFF_REVIEWERS and str(doc.get("verdict") or "").upper() == "SIGNED" \
                and str(doc.get("prd_version")) == str(prd_version):
            out.add(base)
    return out


def _signoff_files(root, prd_rel):
    """The sign-off files beside a PRD, read from the WORKING TREE (post-commit: HEAD is checked out)."""
    import glob as _glob
    sdir = os.path.join(root, os.path.dirname(prd_rel), "signoff")
    files = {}
    for fp in sorted(_glob.glob(os.path.join(sdir, "*.json"))):
        try:
            with open(fp, "r", encoding="utf-8") as fh:
                files[os.path.basename(fp)] = json.load(fh)
        except Exception:  # noqa: BLE001
            files[os.path.basename(fp)] = None
    return files


def _missing_signoffs(root, prd_rel, prd_version):
    return [r for r in SIGNOFF_REVIEWERS if r not in _signed_serials(_signoff_files(root, prd_rel), prd_version)]
REOFFER_MINUTES = int(os.environ.get("PRD_NOTIFY_REOFFER_MINUTES", "30"))
MAX_ATTEMPTS = int(os.environ.get("PRD_NOTIFY_MAX_ATTEMPTS", "6"))
BROKER = "http://127.0.0.1:%s" % os.environ.get("OPAL_BROKER_PORT", "7800")
STATE_REL = "org/mcp/.prd-notify/outstanding.jsonl"
SCHEMA_REL = "org/standards/PRD_HEADER.schema.json"
# TWO ROOTS (project-tree spec s.7; contract prd_path prd/{project_code}_PRD.md): a PRD landing under
# org/missions/D*/<MACRO>/<PROJECT>/prd/ is a step-4 event exactly like one under docs/architecture/.
# Found by the first tree test run (NFRA_COMPEFFICACY L4, 2026-09-03 00:1xZ): without this the tree's
# first PRD would have landed and COO would never have been told.
PRD_GLOB_RE = re.compile(r"^docs/architecture/[^/]+_PRD\.md$|^org/missions/D(?:0|[1-9][0-9]?)/[^/]+/[^/]+/prd/[^/]+_PRD\.md$")
FENCE_RE = re.compile(r"```json\s*(.*?)```", re.S)

# R7 -- step 10 -> the loop_target's owner (design @3814be3317 R7; Andrew: "there's like a field
# somewhere in there where it defines if it's an L6 issue, if it's an L5 issue"). The field is
# `loop_target`, enum [2, 5, 6], gate-locked to `route` in surprise-row-gate.py ROUTE_TO_STEP
# (SPEC_ERROR -> 6, DECOMP_INVALIDATING -> 5, SCOPE_CHANGE -> 2). The owner per target is the STEP's
# owner in the canonical loop; steps 5 and 6 are COO's, step 2 is CTO's (/endpoint --forward F0
# re-entry). Same durable READ-ack machinery as R3; same boundary: it NOTIFIES, it does not act.
ROUTE_OWNER = {2: "1.0.0_SA_CTO", 5: "2.0.0_SA_COO", 6: "2.0.0_SA_COO"}
REMED_RE = re.compile(r"(^|/)org/surprise_channel/[^/]+/REMEDIATION_v[^/]*\.(md|json)$"
                      r"|(^|/)org/missions/D(?:0|[1-9][0-9]?)/[^/]+/[^/]+/surprise-channel/remediations/"
                      r"REMEDIATION_v[^/]*\.(md|json)$")


def _gate_rows(root):
    """surprise-row-gate.py's OWN row parser (_rows), imported by path. One parser for the channel,
    never a second one here: a second parser is a second carrier of what a row IS."""
    import importlib.util
    p = os.path.join(root, ".tools", "surprise-row-gate.py")
    spec = importlib.util.spec_from_file_location("srg_for_notify", p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod._rows


def route_rows(prev_text, now_text, raw, rows_fn):
    """[(owner, row, reason)] for rows NEW in now_text vs prev_text. A new row with no usable
    loop_target, or one outside ROUTE_OWNER, comes back with owner None and the reason -- printed by
    the caller, never silently dropped (an unrouted remediation is the loop degrading quietly)."""
    now_rows, _ = rows_fn(now_text, raw)
    prev_rows, _ = rows_fn(prev_text, raw) if prev_text else ([], 0)
    prev_ids = {r.get("id") for r in prev_rows if isinstance(r, dict)}
    out = []
    for r in now_rows:
        if not isinstance(r, dict) or not r.get("id") or r.get("id") in prev_ids:
            continue
        try:
            t = int(r.get("loop_target"))
        except (TypeError, ValueError):
            out.append((None, r, "no usable loop_target (%r)" % (r.get("loop_target"),)))
            continue
        owner = ROUTE_OWNER.get(t)
        if not owner:
            out.append((None, r, "loop_target %d has no owner (known: %s)" % (t, sorted(ROUTE_OWNER))))
            continue
        out.append((owner, r, ""))
    return out


def _root() -> str:
    out = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, encoding="utf-8", errors="replace")
    return out.stdout.strip() if out.returncode == 0 and out.stdout.strip() else os.getcwd()


def _git(root, *args):
    # encoding is EXPLICIT: under a git hook on Windows, text=True, encoding="utf-8", errors="replace" decodes as cp1252 and a PRD's
    # UTF-8 arrow at byte 0x90 killed the reader thread -- the first real firing then reported
    # "no valid PRD_HEADER" against a PRD the step-6 gate had just passed (2026-09-02, cf532d66c5).
    return subprocess.run(["git", *args], cwd=root, capture_output=True, encoding="utf-8",
                          errors="replace", timeout=60)


def _blob(root, ref, rel, must=False):
    """Text of ref:rel. rc!=0 is None -- a legitimate ABSENCE for HEAD~1 of a brand-new PRD -- unless
    `must`, when the caller is reading the commit's OWN file and a failure to read is a defect that
    must never be reported as 'no header'."""
    r = _git(root, "show", "%s:%s" % (ref, rel))
    if r.returncode != 0:
        if must:
            raise RuntimeError("git show %s:%s rc=%d: %s" % (ref, rel, r.returncode, (r.stderr or "").strip()[:200]))
        return None
    return r.stdout


def _header(text):
    if not text:
        return None
    m = FENCE_RE.search(text)
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except ValueError:
        return None


def _valid(root, header) -> bool:
    try:
        import jsonschema
    except ImportError:
        return False
    with open(os.path.join(root, SCHEMA_REL), encoding="utf-8") as fh:
        schema = json.load(fh)
    return not list(jsonschema.Draft7Validator(schema).iter_errors(header))


def _state_path(root):
    p = os.path.join(root, STATE_REL)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    return p


def _load_state(root):
    p = _state_path(root)
    if not os.path.exists(p):
        return []
    with open(p, encoding="utf-8") as fh:
        return [json.loads(ln) for ln in fh if ln.strip()]


def _save_state(root, rows):
    with open(_state_path(root), "w", encoding="utf-8", newline="\n") as fh:
        for r in rows:
            fh.write(json.dumps(r, sort_keys=True) + "\n")


def _post(path, payload, timeout=5.0):
    req = urllib.request.Request(BROKER + path, data=json.dumps(payload).encode("utf-8"),
                                 headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8", errors="replace"))


def _ledger_rows(payload):
    """The broker's /delivery-state answer is {"messages": [{id, from_serial, to_serial, subject,
    sent_at, state, polled_at, emitted_at, acked_at, acked_by}], "count"}. Parse the structure;
    never regex the blob (a subject can contain any of these key names)."""
    try:
        data = _post("/delivery-state", payload)
    except Exception:  # noqa: BLE001 -- broker down is UNKNOWN, never READ
        return None
    rows = data.get("messages") if isinstance(data, dict) else None
    return rows if isinstance(rows, list) else []


def delivery_state(message_id: int):
    """READ | OFFER-EXHAUSTED | EMITTED | SENT | QUEUED | UNKNOWN. Only READ is an agent-side claim.
    Vocabulary measured on the live ledger 2026-09-02 (200 rows to this seat: EMITTED 133,
    OFFER-EXHAUSTED 34, READ 33): the broker runs its OWN offer cycle and marks a message
    OFFER-EXHAUSTED when that cycle ends un-acked -- that is the state this notifier re-offers ON,
    not an unknown. A row with acked_at set is READ whatever its state string says."""
    rows = _ledger_rows({"message_id": int(message_id)})
    if rows is None:
        return "UNKNOWN"
    for row in rows:
        if not isinstance(row, dict) or row.get("id") != int(message_id):
            continue
        if row.get("acked_at"):
            return "READ"
        st = str(row.get("state") or "").upper()
        return st if st in ("READ", "OFFER-EXHAUSTED", "EMITTED", "SENT", "QUEUED") else "UNKNOWN"
    return "UNKNOWN"


def is_read(message_id: int) -> bool:
    return delivery_state(message_id) == "READ"


def send(root, to, subject, body, sender=None) -> int:
    """Deliver through the broker's HTTP /send-message and return its message_id, or raise.

    NOT codex-send.py. That path delivers through the broker LIBRARY in-process (its receipt says
    "(filesystem)"), and the ledger that /delivery-state and /ack-messages read never sees the
    message -- measured 2026-09-02, selftest runs 2 and 3: two DELIVERED probes, zero ledger rows.
    A notifier whose whole point is a READ-ack must send on the plane the ack lives on. The
    identity control codex-send carried (OPAL_AGENT_SERIAL names a live seat) is kept as the
    refusal below; the broker stamps the row's from_serial from the same value. Payload keys per
    the broker's own tests (org/mcp/test_d0_t1_delivery_clocks.py:131)."""
    # `sender` is the ROW's original author on a re-offer. The post-commit hook is device-wide: it
    # fires on every seat's commit in this worktree (measured 2026-09-02 20:51-20:56Z: three reoffer
    # firings, two on 3.0.0_SA_CVO's commits), so a re-offer that falls due during another seat's
    # commit would otherwise go out under THAT seat's serial.
    sender = sender or os.environ.get("OPAL_AGENT_SERIAL", "")
    if not sender:
        raise RuntimeError("OPAL_AGENT_SERIAL is not set; refusing to send as nobody")
    data = _post("/send-message", {"from_serial": sender, "to_serial": to, "subject": subject,
                                   "text": body}, timeout=15.0)
    mid = data.get("message_id") if isinstance(data, dict) else None
    if not isinstance(mid, int):
        raise RuntimeError("broker /send-message returned no message_id: %s" % json.dumps(data)[:300])
    return mid


_ACK_TAIL = ("\nACK this message (ack_messages) -- the notifier re-offers every %d minutes until the READ ack "
             "lands, up to %d attempts. SENT != EMITTED != READ.\n" % (REOFFER_MINUTES, MAX_ATTEMPTS))


def _compose(row):
    """(subject, body) for either kind of outstanding row: 'prd' (R3) or 'route' (R7)."""
    if row.get("kind") == "route":
        t = int(row["loop_target"])
        subject = "[ROUTE step %d] %s route=%s -> %s re-enters at step %d" % (
            t, row["id"], row.get("route"), row["project"], t)
        if t == 2:
            act = ("Step 2 re-entry: run /endpoint --forward Step F0 on outcome_ref=%s -- read THAT outcome only, "
                   "decide WRONG / RIGHT-BUT-INCOMPLETE / OBSOLETE, re-test its ACCEPT, edit the PRD's ENDPOINT "
                   "section the same turn. Never re-derive the whole list." % row.get("outcome_ref"))
        elif t == 5:
            act = "Step 5 re-entry: the decomposition is invalidated by this row; re-decompose before any TO."
        else:
            act = "Step 6 re-entry: the TO is wrong as cut; re-cut it through the step-6 gate."
        body = ("R7 ROUTER (canonical loop step 10 -> loop_target). This is a NOTIFICATION, not a dispatch: "
                "nothing is cut, decomposed or re-aligned by it.\n\n"
                "  id            %s\n  route         %s\n  loop_target   %s\n  outcome_ref   %s\n  project       %s\n"
                "  fabric        %s\n  commit        %s\n  path          %s\n  remedy        %s\n\n%s\n%s"
                % (row["id"], row.get("route"), row.get("loop_target"), row.get("outcome_ref"), row["project"],
                   row.get("fabric"), row["sha"], row["path"], row.get("remedy"), act, _ACK_TAIL))
        return subject, body
    subject = "[PRD LANDED] %s %s @%s -- step 4 done; step 5 is yours" % (row["project"], row["prd_version"], row["sha"][:10])
    body = ("R3 NOTIFIER (canonical loop step 4 -> 5). This is a NOTIFICATION, not a dispatch: no TO is cut and "
            "no decomposition is started by it.\n\n"
            "  project      %s\n  directive    %s\n  fabric       %s\n  prd_version  %s\n  status       %s\n"
            "  commit       %s\n  path         %s\n  brief_ref    %s\n  outcomes     %s\n%s"
            % (row["project"], row.get("directive"), row.get("fabric"), row["prd_version"], row.get("status"),
               row["sha"], row["path"], row.get("brief_ref"), ", ".join(row.get("outcomes") or []), _ACK_TAIL))
    return subject, body


def _label(row):
    return ("%s %s" % (row["id"], row.get("route")) if row.get("kind") == "route"
            else "%s %s" % (row["project"], row.get("prd_version")))


def _notify(root, row):
    subject, body = _compose(row)
    sender = row.get("from") or _ledger_sender(row)
    if not sender:
        raise RuntimeError("row %s %s carries no `from` and its first message is not on the ledger -- "
                           "refusing to re-offer under the committing seat's identity"
                           % (row.get("project"), row.get("prd_version")))
    row["from"] = sender
    return send(root, row["to"], subject, body, sender=sender)


def _ledger_sender(row):
    """The ORIGINAL sender of a row written before `from` was recorded: read off the ledger row of its
    first message. MEASURED 2026-09-02 21:42Z: the v0.2 row predated the `from` fix, so its first live
    re-offer (id 92780) fell back to OPAL_AGENT_SERIAL of the seat whose commit fired the hook --
    3.0.0_SA_CVO -- exactly the mis-attribution 719e73ffd3 was written to stop, one row earlier."""
    hist = row.get("history") or []
    first = hist[0].get("msg_id") if hist and isinstance(hist[0], dict) else row.get("msg_id")
    if not first:
        return None
    rows = _ledger_rows({"message_id": int(first)}) or []
    for r in rows:
        if isinstance(r, dict) and r.get("id") == int(first) and r.get("from_serial"):
            return str(r["from_serial"])
    return None


def post_commit(root, at=None):
    """`at` (optional): process THAT commit instead of HEAD -- the recovery path for a commit the wrapper
    missed (L4-R, 2026-09-11: a sign-off commit ran in reoffer mode and the release branch never fired)."""
    ref = at or "HEAD"
    sha = _git(root, "rev-parse", ref).stdout.strip()
    touched = [ln.strip().replace("\\", "/") for ln in
               _git(root, "diff-tree", "--no-commit-id", "--name-only", "-r", sha).stdout.splitlines()]
    prds = [f for f in touched if PRD_GLOB_RE.match(f)]
    state = _load_state(root)
    sent = 0
    for rel in prds:
        try:
            now_text = _blob(root, "HEAD", rel, must=True)
        except RuntimeError as exc:
            # A READ failure is not a header verdict. Say so, loudly, and do not pretend to a reason.
            print("[prd-notify] ERROR: could not read HEAD:%s (%s) -- NOT notified and NOT recorded; "
                  "re-run `prd-header-notify.py post-commit` once the cause is fixed" % (rel, exc))
            continue
        now_h = _header(now_text)
        if not now_h:
            print("[prd-notify] %s: no PRD_HEADER fence at HEAD (first ```json block absent or not JSON) "
                  "-- not notified (the step-6 gate refuses a TO against it; this notifier does not gate)" % rel)
            continue
        if not _valid(root, now_h):
            print("[prd-notify] %s: PRD_HEADER fails %s -- not notified (the step-6 gate refuses a TO "
                  "against it; this notifier does not gate)" % (rel, SCHEMA_REL))
            continue
        prev_h = _header(_blob(root, "HEAD~1", rel))
        bumped = prev_h is None or prev_h.get("prd_version") != now_h.get("prd_version")
        if not bumped:
            print("[prd-notify] %s: prd_version %s unchanged vs HEAD~1 -- not notified (bump it for a "
                  "substantive edit; an un-bumped edit is invisible to COO by design)" % (rel, now_h.get("prd_version")))
            continue
        base_row = {"kind": "prd", "project": now_h["project"], "directive": now_h.get("directive"),
                    "fabric": now_h.get("fabric"), "prd_version": now_h["prd_version"], "status": now_h.get("status"),
                    "sha": sha, "path": rel, "brief_ref": now_h.get("brief_ref"),
                    "outcomes": now_h.get("endpoint_outcomes"),
                    "from": os.environ.get("OPAL_AGENT_SERIAL", ""),
                    "attempts": 0, "msg_id": None, "sent_at": None, "history": []}
        # L4-R: the two reviewers are notified on EVERY bump, unconditionally.
        for reviewer in SIGNOFF_REVIEWERS:
            r = dict(base_row, to=_seat(reviewer), history=[], kind="prd-review")
            sent += _dispatch(root, state, r)
        # L4-R: the COO is notified ONLY when both sign-offs exist at this prd_version.
        missing = _missing_signoffs(root, rel, now_h["prd_version"])
        if missing:
            print("[prd-notify] %s @%s: COO delivery WITHHELD (L4-R) -- awaiting SIGNED sign-off at %s from %s; "
                  "the L6 gate refuses a task order against it meanwhile"
                  % (rel, sha[:10], now_h["prd_version"], ", ".join(missing)))
        else:
            sent += _dispatch(root, state, dict(base_row, to=RECIPIENT, history=[]))
    # ---- L4-R: a sign-off landed in this commit -> re-check its PRD and release the COO delivery if complete ----
    for so_rel in [f for f in touched if SIGNOFF_RE.match(f)]:
        prd_dir = SIGNOFF_RE.match(so_rel).group(1)
        try:
            so_doc = json.loads(_blob(root, sha, so_rel, must=True))
        except Exception as exc:  # noqa: BLE001
            print("[prd-notify] %s: sign-off unreadable at HEAD (%s) -- nothing released" % (so_rel, exc))
            continue
        prd_rel = prd_dir + "/" + str(so_doc.get("prd") or "")
        try:
            h = _header(_blob(root, sha, prd_rel, must=True))
        except Exception as exc:  # noqa: BLE001
            print("[prd-notify] %s: names PRD %s which is unreadable at HEAD (%s)" % (so_rel, prd_rel, exc))
            continue
        if not h:
            continue
        missing = _missing_signoffs(root, prd_rel, h.get("prd_version"))
        if missing:
            print("[prd-notify] %s: sign-off recorded; COO delivery still WITHHELD for %s at %s -- awaiting %s"
                  % (so_rel, prd_rel, h.get("prd_version"), ", ".join(missing)))
            continue
        already = [r for r in state if r.get("kind") == "prd" and r.get("path") == prd_rel
                   and r.get("prd_version") == h.get("prd_version") and r.get("to") == RECIPIENT]
        if already:
            print("[prd-notify] %s: both sign-offs present; COO delivery for %s at %s already recorded (id=%s)"
                  % (so_rel, prd_rel, h.get("prd_version"), already[-1].get("msg_id")))
            continue
        row = {"kind": "prd", "project": h["project"], "directive": h.get("directive"), "fabric": h.get("fabric"),
               "prd_version": h["prd_version"], "status": h.get("status"), "sha": sha, "path": prd_rel,
               "brief_ref": h.get("brief_ref"), "outcomes": h.get("endpoint_outcomes"), "to": RECIPIENT,
               "from": os.environ.get("OPAL_AGENT_SERIAL", ""), "attempts": 0, "msg_id": None, "sent_at": None,
               "history": [], "released_by": so_rel}
        print("[prd-notify] %s: BOTH sign-offs present at %s -> COO delivery RELEASED (L4-R)" % (so_rel, h.get("prd_version")))
        sent += _dispatch(root, state, row)
    # ---- R7: remediation rows NEW in this commit, on either root -> the loop_target's owner ----
    for rel in [f for f in touched if REMED_RE.search(f)]:
        try:
            now_text = _blob(root, "HEAD", rel, must=True)
        except RuntimeError as exc:
            print("[prd-notify] ERROR: could not read HEAD:%s (%s) -- NO route notified and NOT recorded; "
                  "re-run `prd-header-notify.py post-commit` once the cause is fixed" % (rel, exc))
            continue
        prev_text = _blob(root, "HEAD~1", rel)
        for owner, r, reason in route_rows(prev_text, now_text, rel.lower().endswith(".json"), _gate_rows(root)):
            if owner is None:
                print("[prd-notify] %s: NEW remediation row %s NOT routed -- %s (the surprise-row gate should "
                      "have refused it; this notifier does not gate)" % (rel, r.get("id"), reason))
                continue
            row = {"kind": "route", "id": r["id"], "route": r.get("route"), "loop_target": int(r["loop_target"]),
                   "outcome_ref": r.get("outcome_ref"), "project": r.get("project") or str(r["id"]).rsplit("-S", 1)[0],
                   "fabric": r.get("fabric"), "remedy": str(r.get("remedy") or "")[:400], "sha": sha, "path": rel,
                   "to": _seat(owner), "from": os.environ.get("OPAL_AGENT_SERIAL", ""),
                   "attempts": 0, "msg_id": None, "sent_at": None, "history": []}
            sent += _dispatch(root, state, row)
    _save_state(root, state)
    return sent


def _dispatch(root, state, row):
    """Send one outstanding row now and record it (attempt 1), or record it with 0 attempts for the
    re-offer to retry. Returns 1 if sent."""
    try:
        mid = _notify(root, row)
        row.update(msg_id=mid, sent_at=time.time(), attempts=1)
        row["history"].append({"msg_id": mid, "at": time.time()})
        print("[prd-notify] %s @%s -> %s id=%d (DELIVERED/QUEUED is transport; READ is the goal)"
              % (_label(row), row["sha"][:10], row["to"], mid))
        state.append(row)
        return 1
    except Exception as exc:  # noqa: BLE001
        row["last_error"] = str(exc)[:300]
        print("[prd-notify] %s: SEND FAILED (%s) -- recorded as outstanding with 0 attempts; reoffer will retry"
              % (_label(row), str(exc)[:160]))
        state.append(row)
        return 0


def route_dryrun(root, sha):
    """What post-commit WOULD route for commit `sha` (vs sha~1), sending nothing. The real-bytes
    exercise: run it on any commit that touched a remediation doc."""
    touched = [ln.strip().replace("\\", "/") for ln in
               _git(root, "diff-tree", "--no-commit-id", "--name-only", "-r", sha).stdout.splitlines()]
    rels = [f for f in touched if REMED_RE.search(f)]
    print("[prd-notify route-dryrun] %s touched %d file(s), %d remediation doc(s)" % (sha[:10], len(touched), len(rels)))
    n = 0
    for rel in rels:
        now_text = _blob(root, sha, rel)
        prev_text = _blob(root, sha + "~1", rel)
        routed = route_rows(prev_text, now_text, rel.lower().endswith(".json"), _gate_rows(root))
        for owner, r, reason in routed:
            n += 1
            print("  %s  %-28s route=%-20s loop_target=%-4s -> %s" % (
                "ROUTE " if owner else "SKIP  ", r.get("id"), r.get("route"), r.get("loop_target"), owner or reason))
        if not routed:
            print("  %s: no NEW rows vs %s~1" % (rel, sha[:10]))
    print("[prd-notify route-dryrun] %d new remediation row(s) considered" % n)
    return 0


def reoffer(root):
    state = _load_state(root)
    keep, retired, resent = [], 0, 0
    now = time.time()
    for row in state:
        mid = row.get("msg_id")
        if mid and is_read(mid):
            retired += 1
            print("[prd-notify] RETIRED %s id=%d -- READ by %s" % (_label(row), mid, row["to"]))
            continue
        due = (row.get("sent_at") is None) or (now - row["sent_at"] > REOFFER_MINUTES * 60)
        if due and row.get("attempts", 0) < MAX_ATTEMPTS:
            try:
                new_mid = _notify(root, row)
                row.update(msg_id=new_mid, sent_at=now, attempts=row.get("attempts", 0) + 1)
                row["history"].append({"msg_id": new_mid, "at": now})
                resent += 1
                print("[prd-notify] RE-OFFERED %s id=%d attempt %d/%d" % (_label(row), new_mid, row["attempts"], MAX_ATTEMPTS))
            except Exception as exc:  # noqa: BLE001
                row["last_error"] = str(exc)[:300]
        elif due:
            print("[prd-notify] EXHAUSTED %s after %d attempts -- still not READ. This is a finding for the "
                  "loop owner, not something this notifier can fix." % (_label(row), row["attempts"]))
        keep.append(row)
    _save_state(root, keep)
    return retired, resent


def status(root):
    rows = _load_state(root)
    print("[prd-notify] outstanding=%d (state file %s)" % (len(rows), STATE_REL))
    for r in rows:
        st = delivery_state(r["msg_id"]) if r.get("msg_id") else "UNSENT"
        print("  %-6s %-34s @%s -> %s id=%s attempts=%d state=%s" % (r.get("kind", "prd"), _label(r), r["sha"][:10], r.get("to"), r.get("msg_id"), r.get("attempts", 0), st))
    return 0


def selftest(root):
    """RC7 control: on the LIVE broker, prove delivered != read, then read."""
    me = os.environ.get("OPAL_AGENT_SERIAL", "")
    if not me:
        print("  DEFECT  OPAL_AGENT_SERIAL unset; cannot run the round-trip")
        return 1
    fails = 0
    # ---- R7 routing, PURE (the gate's own parser on synthetic prev/now texts; nothing sent) ----
    rows_fn = _gate_rows(root)

    def fence(*rows):
        return "".join("```json\n" + json.dumps(r) + "\n```\n" for r in rows)
    old = {"id": "P-S1", "route": "SPEC_ERROR", "loop_target": 6}
    prev = fence(old)
    now = fence(old,
                {"id": "P-S2", "route": "SPEC_ERROR", "loop_target": 6},
                {"id": "P-S3", "route": "DECOMP_INVALIDATING", "loop_target": 5},
                {"id": "P-S4", "route": "SCOPE_CHANGE", "loop_target": 2, "outcome_ref": "FWD-3"},
                {"id": "P-S5", "route": "SPEC_ERROR"},
                {"id": "P-S6", "route": "SPEC_ERROR", "loop_target": 9})
    got = {r["id"]: (o, bool(reason)) for o, r, reason in route_rows(prev, now, False, rows_fn)}
    want = {"P-S2": ("2.0.0_SA_COO", False), "P-S3": ("2.0.0_SA_COO", False), "P-S4": ("1.0.0_SA_CTO", False),
            "P-S5": (None, True), "P-S6": (None, True)}
    ok = got == want
    print("  %-7s route_rows: 6->5 rows routed as %s (P-S1 pre-existing, not re-routed; S5 no target, S6 unknown target)"
          % ("OK" if ok else "DEFECT", "expected" if ok else got))
    fails += int(not ok)
    raw_now = json.dumps([{"id": "P-S7", "route": "SCOPE_CHANGE", "loop_target": 2}])
    got_raw = [(o, r["id"]) for o, r, _ in route_rows(None, raw_now, True, rows_fn)]
    ok = got_raw == [("1.0.0_SA_CTO", "P-S7")]
    print("  %-7s route_rows on a RAW .json document with no HEAD~1 -> %s" % ("OK" if ok else "DEFECT", got_raw))
    fails += int(not ok)
    subj, body = _compose({"kind": "route", "id": "P-S4", "route": "SCOPE_CHANGE", "loop_target": 2,
                           "outcome_ref": "FWD-3", "project": "P", "fabric": "laptop", "sha": "0" * 40,
                           "path": "x", "remedy": "r"})
    ok = "[ROUTE step 2]" in subj and "F0" in body and "FWD-3" in body and "NOTIFICATION" in body
    print("  %-7s _compose(route, loop_target=2) names step 2, F0 re-entry, the outcome_ref, and the NOTIFICATION boundary"
          % ("OK" if ok else "DEFECT"))
    fails += int(not ok)
    # ---- L4-R: the sign-off predicate, pure ----
    _c = {"signed_by": "4.0.0_SA_CRO", "verdict": "SIGNED", "prd_version": "v0.4"}
    _v = {"signed_by": "3.0.0_SA_CVO~Z", "verdict": "SIGNED", "prd_version": "v0.4"}
    ok = _signed_serials({}, "v0.4") == set()
    print("  %-7s _signed_serials: no files -> nobody signed" % ("OK" if ok else "DEFECT"))
    fails += int(not ok)
    ok = _signed_serials({"a.json": _c, "b.json": _v}, "v0.4") == {"4.0.0_SA_CRO", "3.0.0_SA_CVO"}
    print("  %-7s _signed_serials: both SIGNED at v0.4, CVO via ~Z -> both (tilde signs for its base)" % ("OK" if ok else "DEFECT"))
    fails += int(not ok)
    ok = _signed_serials({"a.json": _c, "b.json": dict(_v, prd_version="v0.3")}, "v0.4") == {"4.0.0_SA_CRO"}
    print("  %-7s _signed_serials: CVO signed v0.3, PRD at v0.4 -> only CRO (version-bound)" % ("OK" if ok else "DEFECT"))
    fails += int(not ok)
    ok = _signed_serials({"a.json": _c, "b.json": dict(_v, verdict="REFUSED")}, "v0.4") == {"4.0.0_SA_CRO"}
    print("  %-7s _signed_serials: a REFUSED verdict signs nothing" % ("OK" if ok else "DEFECT"))
    fails += int(not ok)
    ok = _signed_serials({"a.json": None, "b.json": _v}, "v0.4") == {"3.0.0_SA_CVO"}
    print("  %-7s _signed_serials: an unreadable file signs nothing" % ("OK" if ok else "DEFECT"))
    fails += int(not ok)
    ok = bool(SIGNOFF_RE.match("org/missions/D9/IRPT/IRPT_BCKEND/prd/signoff/4.0.0_SA_CRO.json")) and \
        not SIGNOFF_RE.match("org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md")
    print("  %-7s SIGNOFF_RE matches prd/signoff/*.json and not the PRD itself" % ("OK" if ok else "DEFECT"))
    fails += int(not ok)
    # ---- delivery, LIVE: delivered is not read (the RC7 property) ----
    try:
        mid = send(root, me, "[prd-notify selftest] probe", "probe body -- delivered is not read")
        print("  OK      probe sent to self, id=%d" % mid)
    except Exception as exc:  # noqa: BLE001
        print("  DEFECT  probe send failed: %s" % str(exc)[:200])
        return 1
    st = delivery_state(mid)
    ok = st != "READ" and st != "UNKNOWN"
    print("  %-7s before ack: delivery_state=%s (must be a transport state, NOT READ, NOT UNKNOWN)" % ("OK" if ok else "DEFECT", st))
    fails += int(not ok)
    ok = not is_read(mid)
    print("  %-7s is_read() before ack -> %s (must be False)" % ("OK" if ok else "DEFECT", not ok))
    fails += int(not ok)
    try:
        _post("/ack-messages", {"serial": me, "ids": [mid]})  # broker key is `ids` (test_d0_t1_delivery_clocks.py:147)
        st2 = delivery_state(mid)
        ok = st2 == "READ" and is_read(mid)
        print("  %-7s after ack: delivery_state=%s, is_read()=%s (must be READ/True)" % ("OK" if ok else "DEFECT", st2, is_read(mid)))
        fails += int(not ok)
    except Exception as exc:  # noqa: BLE001
        print("  DEFECT  ack round-trip failed: %s" % str(exc)[:200])
        fails += 1
    print("selftest: %d defect(s)" % fails)
    return 1 if fails else 0


def main(argv):
    root = _root()
    mode = argv[0] if argv else "status"
    if mode == "post-commit":
        post_commit(root, argv[1] if len(argv) > 1 else None)
        reoffer(root)
        return 0
    if mode == "reoffer":
        reoffer(root)
        return 0
    if mode == "status":
        return status(root)
    if mode == "selftest":
        return selftest(root)
    if mode == "route-dryrun" and len(argv) > 1:
        return route_dryrun(root, argv[1])
    print("usage: prd-header-notify.py post-commit [<sha>]|reoffer|status|selftest|route-dryrun <sha>", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
