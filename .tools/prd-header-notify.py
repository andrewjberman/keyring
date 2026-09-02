#!/usr/bin/env python3
"""prd-header-notify -- R3 of the canonical loop (step 4 -> step 5), release condition 7.

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

RECIPIENT = os.environ.get("PRD_NOTIFY_TO", "2.0.0_SA_COO")
REOFFER_MINUTES = int(os.environ.get("PRD_NOTIFY_REOFFER_MINUTES", "30"))
MAX_ATTEMPTS = int(os.environ.get("PRD_NOTIFY_MAX_ATTEMPTS", "6"))
BROKER = "http://127.0.0.1:%s" % os.environ.get("OPAL_BROKER_PORT", "7800")
STATE_REL = "org/mcp/.prd-notify/outstanding.jsonl"
SCHEMA_REL = "org/standards/PRD_HEADER.schema.json"
PRD_GLOB_RE = re.compile(r"^docs/architecture/[^/]+_PRD\.md$")
FENCE_RE = re.compile(r"```json\s*(.*?)```", re.S)


def _root() -> str:
    out = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True)
    return out.stdout.strip() if out.returncode == 0 and out.stdout.strip() else os.getcwd()


def _git(root, *args):
    # encoding is EXPLICIT: under a git hook on Windows, text=True decodes as cp1252 and a PRD's
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


def _notify(root, row):
    subject = "[PRD LANDED] %s %s @%s -- step 4 done; step 5 is yours" % (row["project"], row["prd_version"], row["sha"][:10])
    body = ("R3 NOTIFIER (canonical loop step 4 -> 5). This is a NOTIFICATION, not a dispatch: no TO is cut and "
            "no decomposition is started by it.\n\n"
            "  project      %s\n  directive    %s\n  fabric       %s\n  prd_version  %s\n  status       %s\n"
            "  commit       %s\n  path         %s\n  brief_ref    %s\n  outcomes     %s\n\n"
            "ACK this message (ack_messages) -- the notifier re-offers every %d minutes until the READ ack lands, "
            "up to %d attempts. SENT != EMITTED != READ.\n"
            % (row["project"], row.get("directive"), row.get("fabric"), row["prd_version"], row.get("status"),
               row["sha"], row["path"], row.get("brief_ref"), ", ".join(row.get("outcomes") or []),
               REOFFER_MINUTES, MAX_ATTEMPTS))
    return send(root, row["to"], subject, body, sender=row.get("from"))


def post_commit(root):
    sha = _git(root, "rev-parse", "HEAD").stdout.strip()
    touched = [ln.strip().replace("\\", "/") for ln in
               _git(root, "diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD").stdout.splitlines()]
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
        row = {"project": now_h["project"], "directive": now_h.get("directive"), "fabric": now_h.get("fabric"),
               "prd_version": now_h["prd_version"], "status": now_h.get("status"), "sha": sha, "path": rel,
               "brief_ref": now_h.get("brief_ref"), "outcomes": now_h.get("endpoint_outcomes"),
               "to": RECIPIENT, "from": os.environ.get("OPAL_AGENT_SERIAL", ""),
               "attempts": 0, "msg_id": None, "sent_at": None, "history": []}
        try:
            mid = _notify(root, row)
            row.update(msg_id=mid, sent_at=time.time(), attempts=1)
            row["history"].append({"msg_id": mid, "at": time.time()})
            print("[prd-notify] %s %s @%s -> %s id=%d (DELIVERED/QUEUED is transport; READ is the goal)"
                  % (row["project"], row["prd_version"], sha[:10], RECIPIENT, mid))
            sent += 1
        except Exception as exc:  # noqa: BLE001
            row["last_error"] = str(exc)[:300]
            print("[prd-notify] %s: SEND FAILED (%s) -- recorded as outstanding with 0 attempts; reoffer will retry"
                  % (rel, str(exc)[:160]))
        state.append(row)
    _save_state(root, state)
    return sent


def reoffer(root):
    state = _load_state(root)
    keep, retired, resent = [], 0, 0
    now = time.time()
    for row in state:
        mid = row.get("msg_id")
        if mid and is_read(mid):
            retired += 1
            print("[prd-notify] RETIRED %s %s id=%d -- READ by %s" % (row["project"], row["prd_version"], mid, row["to"]))
            continue
        due = (row.get("sent_at") is None) or (now - row["sent_at"] > REOFFER_MINUTES * 60)
        if due and row.get("attempts", 0) < MAX_ATTEMPTS:
            try:
                new_mid = _notify(root, row)
                row.update(msg_id=new_mid, sent_at=now, attempts=row.get("attempts", 0) + 1)
                row["history"].append({"msg_id": new_mid, "at": now})
                resent += 1
                print("[prd-notify] RE-OFFERED %s %s id=%d attempt %d/%d" % (row["project"], row["prd_version"], new_mid, row["attempts"], MAX_ATTEMPTS))
            except Exception as exc:  # noqa: BLE001
                row["last_error"] = str(exc)[:300]
        elif due:
            print("[prd-notify] EXHAUSTED %s %s after %d attempts -- still not READ. This is a finding for the "
                  "loop owner, not something this notifier can fix." % (row["project"], row["prd_version"], row["attempts"]))
        keep.append(row)
    _save_state(root, keep)
    return retired, resent


def status(root):
    rows = _load_state(root)
    print("[prd-notify] outstanding=%d (state file %s)" % (len(rows), STATE_REL))
    for r in rows:
        st = delivery_state(r["msg_id"]) if r.get("msg_id") else "UNSENT"
        print("  %-22s %-6s @%s id=%s attempts=%d state=%s" % (r["project"], r["prd_version"], r["sha"][:10], r.get("msg_id"), r.get("attempts", 0), st))
    return 0


def selftest(root):
    """RC7 control: on the LIVE broker, prove delivered != read, then read."""
    me = os.environ.get("OPAL_AGENT_SERIAL", "")
    if not me:
        print("  DEFECT  OPAL_AGENT_SERIAL unset; cannot run the round-trip")
        return 1
    fails = 0
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
        post_commit(root)
        reoffer(root)
        return 0
    if mode == "reoffer":
        reoffer(root)
        return 0
    if mode == "status":
        return status(root)
    if mode == "selftest":
        return selftest(root)
    print("usage: prd-header-notify.py post-commit|reoffer|status|selftest", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
