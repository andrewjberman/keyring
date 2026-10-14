#!/usr/bin/env python3
"""unblock.py -- a COO with nothing left that advances its project writes to the CRO; the CRO finds a new approach that is
not blocked; the CTO folds it into the COO process.

Andrew-direct 2026-10-09 ~02:3xZ (record org/tier1_exec/4.0.0_SA_CRO~B/deliverables/
ANDREW_DIRECT_20261009_023xZ_THIRD_EMPTY_TICK_UNBLOCK_VIA_CRO_THEN_CTO.md): "if there is truly nothing to do to meaningfully
advance the project, then they need to reach out to the CRO on their channel and tell them their position, and tell them the
endpoint, and explain that they are blocked, and the CRO job is to figure out a new approach that is not blocked. THen CRO
sends that to the CTO who folds it in to the COO process." and "if they have done /next-calls for two consecutive ticks, on
the third tick they do this if nothing has opened up." and "CRO figures out the new approach, and CTO basically figures out how
to synthesize that into the workflow, and it needs a sign off by the CVO." Owner 4.0.0_SA_CRO~B.

    python .tools/unblock.py tick --serial <COO serial> --project <CODE> --result nothing|work
                                  [--owed-ledger <open_deploys slug> --owed-owner <serial>] [--owed-call <open-call id>]
        the drive tick's count of consecutive `/next-calls --drive` ticks that found nothing; LAST line
        UNBLOCK-TICK serial=<s> project=<CODE> empty=<n> verdict=<KEEP-DRIVING|THIRD-EMPTY-TICK|WAITING <UB id> <state>|RESUME <UB id>
                                                              |WAITING OWED <slug> <owner> UNTIL <time>>
        --owed-*: the tick's only block is ONE owed act named in the project's record, owned by another seat. It reads WAITING,
        not empty, only while (a) the owner is LIVE, (b) that act's deploy-ledger entry is OPEN on any live worktree (NEVER-2's
        union read; a linked worktree counts it only if its own commits touched it or it is uncommitted there, never a copy
        inherited at branch cut, msg 32766), and (c) the act is inside its declared window_hours, or 4h from opened_at when none is declared. Failing
        any one, the tick counts as before, so a hung apply still opens a case (3.0.0_SA_CVO~Z ruling @23f60a21df).
        --owed-call: the tick's only block is ONE open call (e.g. a card held for Andrew). It reads `WAITING CALL <id> <state>`
        only while that call's row on org/devices/state/<box>/open_calls.json reads OPEN or HELD; a CLOSED or absent call
        counts as before (CVO @f59dbc4f71 via 1.0.0_SA_CTO~Z msg 32856 -- never tick --result work to dodge the counter).
        A call on ANOTHER box reads through open-calls.py approval_read (the freshest of the cluster copy, origin/box/<box> and
        the working-tree copy); a foreign list with no readable source reads `counts=EMPTY reason=call-unreadable`. Each line
        names `source=<cluster|git|working-tree|own>`, the copy that answered.
        --wait-until <UTC ISO> --owner <serial | schedule:<name>>: the tick's only block is a DATED event, before any case is
        opened (e.g. the 11:00Z scheduled pull). It reads `WAITING DATED <owner> UNTIL <time>` with the count at 0 while the
        time is ahead (at most 7 days) and the owner is a LIVE seat or a schedule; an owner not live counts as before, and the
        chase applies (brief gpt-feedback-autonomy-solutions item 4, 1.0.0_SA_CTO @ba20ac668b). Pass it on each such tick.
    python .tools/unblock.py open --project <CODE> --by <COO serial> --body <position.md>     (COO, on THIRD-EMPTY-TICK)
    python .tools/unblock.py propose --id <UB> --by <CRO serial> --body <approach.md>         (CRO)
    python .tools/unblock.py fold --id <UB> --by <CTO serial> --ref <PRD addendum | round-N analysis | ruling path>   (CTO)
                                  [--wait-until <UTC ISO>]  the dated event the fold waits on (also on `resume`, COO; it wins)
        After the COO resumes, a tick with nothing to do reads WAITING <UB id> UNTIL <time> while that time is ahead, and the
        empty count stays 0: a dated wait already folded never re-fires the third-empty-tick rule. At most 7 days ahead.
    python .tools/unblock.py sign --id <UB> --by <CVO serial> [--note <text>]                (CVO signs the fold)
    python .tools/unblock.py refuse --id <UB> --by <CVO serial> --reason <text>              (CVO: back to the CTO)
    python .tools/unblock.py resume --id <UB> --by <COO serial>                              (COO, after reading the signed fold)
    python .tools/unblock.py hung --minutes <m> --tokens <n|1.2k>   the 10:1 test on a peeked seat's running query (HUNG at
        10 or more minutes per 1k tokens: relocate the owed work off that box; Andrew-direct 2026-10-09 ~06:3xZ)
    python .tools/unblock.py list [--state OPEN|PROPOSED|FOLDED|CLOSED|ALL]
    python .tools/unblock.py show --id <UB>
    python .tools/unblock.py --selftest       LAST line  UNBLOCK-SELFTEST cases=<k>/<n> ok=<True|False>

STATES: OPEN (at the CRO) -> PROPOSED (at the CTO) -> FOLDED (at the CVO) -> SIGNED (back at the COO) -> CLOSED (the COO
resumed on it). A CVO refusal returns the file to PROPOSED with the reason kept in `refusals`; the CTO folds again.
The COO's body must carry `## Position`, `## Endpoint`, `## Blocked`, `## Owed by others` (the chase); the CRO's `## New approach`, `## Why it is not blocked`,
`## What changes for the COO`. Who acts is routed by box: the CRO on `cro_device` (the COO's own box when a CRO is live there
at `open`, else the laptop), the CTO and the COO on `from_device`, the CVO on `fold.cvo_device` (the CTO's box when a CVO is
live there at `fold`, else the laptop). Each box's `.tools/open-calls-scan.py` pass drops the
nudge in that seat's inbox. Transport: s3://opal-313476888478-globgrph/fabric/unblock/v1/<UB id>.json (schema "unblock/1").
Record: `sign` writes org/critical_paths/unblock/<UTC stamp>_<UB id>.md on the CVO's box (one writer per file): the COO's
position, the CRO's approach, any CVO refusals, the CTO's fold and the sign-off.
Environment (tests): OPAL_XADJ_LOCAL (the store), OPAL_UNBLOCK_RECORD_ROOT, OPAL_UNBLOCK_TICKS, OPAL_LIVENESS_FILE.
Exit: 0 done, 1 refused, 2 usage.
"""
from __future__ import annotations

import argparse
import datetime
import importlib.util
import json
import math
import os
import re
import secrets
import subprocess
import sys
import tempfile

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)
SCHEMA = "unblock/1"
PREFIX = "fabric/unblock/v1"
REC_DIR = "org/critical_paths/unblock"
KEYS = {"schema", "id", "project", "from_device", "from_serial", "cro_device", "opened_at", "body", "state", "proposal", "fold",
        "signoff", "refusals", "resumed"}
STATES = ("OPEN", "PROPOSED", "FOLDED", "SIGNED", "CLOSED")
COO_HEADINGS = ("## Position", "## Endpoint", "## Blocked", "## Owed by others")   # the last: Andrew-direct 2026-10-09 ~06:3xZ
HUNG_MIN_PER_KTOK = 10.0   # 10 minutes per 1k tokens on the running query = hung (same record)
CRO_HEADINGS = ("## New approach", "## Why it is not blocked", "## What changes for the COO")
ID_RE = re.compile(r"^UB-\d{8}T\d{6}Z-[0-9a-f]{4}$")
EMPTY_TICKS_BEFORE = 2      # two consecutive empty /next-calls ticks; the third writes to the CRO
CRO_OF = {"laptop": "4.0.0_SA_CRO", "sitez": "4.0.0_SA_CRO~Z"}
CVO_OF = {"laptop": "3.0.0_SA_CVO"}


class Refused(Exception):
    pass


def load_mod(name: str, rel: str):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


XA = load_mod("opal_xadj_for_unblock", ".tools/xadj.py")   # the S3 store helpers (and OPAL_XADJ_LOCAL for tests)


def now_dt():
    return datetime.datetime.now(datetime.timezone.utc)


def stamp(dt) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def key_of(uid: str) -> str:
    return "%s/%s.json" % (PREFIX, uid)


def check(doc, where: str) -> dict:
    if not isinstance(doc, dict) or set(doc) != KEYS or doc["schema"] != SCHEMA or doc["state"] not in STATES \
            or not ID_RE.match(str(doc["id"])):
        raise Refused("%s: not an unblock/1 file (keys, schema, state or id)" % where)
    if not isinstance(doc["refusals"], list):
        raise Refused("%s: refusals is not a list" % where)
    need = {"OPEN": (), "PROPOSED": ("proposal",), "FOLDED": ("proposal", "fold"), "SIGNED": ("proposal", "fold", "signoff"),
            "CLOSED": ("proposal", "fold", "signoff", "resumed")}
    for k in ("proposal", "fold", "signoff", "resumed"):
        if (k in need[doc["state"]]) != isinstance(doc[k], dict):
            raise Refused("%s: state %s does not match its %s block" % (where, doc["state"], k))
    return doc


def get(uid: str) -> dict:
    if not ID_RE.match(uid or ""):
        raise Refused("REFUSED: %r is not an unblock id (UB-<stamp>-<hex4>)" % uid)
    doc = XA._get(key_of(uid))
    if doc is None:
        raise Refused("REFUSED: no unblock file %s in the store" % uid)
    return check(doc, uid)


def list_all() -> list:
    return [check(XA._get(k), k) for k in XA._list_keys(PREFIX)]


def headings_missing(body: str, heads) -> list:
    return [h for h in heads if not re.search(r"^%s\s*$" % re.escape(h), body, re.M)]


def this_box() -> str:
    dev = load_mod("opal_devices", "lib/devices.py")
    name, basis = dev.this_device(dev.load())
    if name is None:
        raise Refused("ERROR: this box is unresolved: %s" % basis)
    return name


def live_seat_here(box: str, table: dict, prefix: str):
    scan = load_mod("opal_scan_for_unblock", ".tools/open-calls-scan.py")
    return scan.pick(scan.liveness(), table.get(box, ""), prefix, now_dt().timestamp())


def live_cro_here(box: str):
    return live_seat_here(box, CRO_OF, "4.0.0_SA_CRO")


def active_for(serial: str, project: str):
    """The newest non-CLOSED file this COO opened for this project, or None."""
    hits = [d for d in list_all() if d["from_serial"] == serial and d["project"] == project and d["state"] != "CLOSED"]
    return sorted(hits, key=lambda d: d["opened_at"])[-1] if hits else None


# ---------------------------------------------------------------- the tick counter (local, per box)

def ticks_dir() -> str:
    d = os.environ.get("OPAL_UNBLOCK_TICKS", "").strip()
    if d:
        return d
    try:
        common = subprocess.run(["git", "-C", ROOT, "rev-parse", "--path-format=absolute", "--git-common-dir"],
                                capture_output=True, text=True, timeout=20).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        common = ""
    return os.path.join(common or os.path.join(ROOT, ".git"), "unblock-ticks")


def parse_tokens(s) -> float:
    """'1.2k' / '1200' / '3m' -> a token count."""
    t = str(s).strip().lower().replace(",", "")
    mult = {"k": 1e3, "m": 1e6}.get(t[-1:], 1.0)
    return float(t[:-1] if t[-1:] in "km" else t) * mult


def hung_verdict(minutes: float, tokens: float) -> tuple:
    """PURE. (verdict, minutes per 1k tokens). Andrew-direct 2026-10-09 ~06:3xZ: 'If that number is 10:1, e.g. 10min and 1k
    tokens, that agent is hung, and most likely their whole box is hung.' Zero tokens after any time is hung."""
    if minutes < 0 or tokens < 0:
        raise Refused("REFUSED: minutes and tokens are not negative")
    ratio = math.inf if tokens == 0 else minutes / (tokens / 1000.0)
    return ("HUNG" if minutes > 0 and ratio >= HUNG_MIN_PER_KTOK else "WORKING"), ratio


def cmd_hung(args) -> int:
    v, ratio = hung_verdict(float(args.minutes), parse_tokens(args.tokens))
    if v == "HUNG":
        print("NEXT: most likely the whole box is hung (a GitOps failure). Relocate the owed work to another box, preferably the "
              "requesting box; if it cannot move, record that it is handled when that box clears, and the condition.")
    print("UNBLOCK-HUNG minutes=%s tokens=%s min_per_ktok=%s verdict=%s" % (
        args.minutes, args.tokens, "no-tokens" if math.isinf(ratio) else "%.1f" % ratio, v))
    return 0


MAX_WAIT_DAYS = 7          # a dated wait silences the third-empty-tick rule for at most this long


def parse_wait(s: str, now) -> str:
    """A --wait-until value as stamp() text, or Refused: UTC ISO, in the future, at most MAX_WAIT_DAYS ahead."""
    try:
        t = datetime.datetime.strptime(s.strip().replace("Z", "+0000"), "%Y-%m-%dT%H:%M:%S%z") if ":" in s[16:] else \
            datetime.datetime.strptime(s.strip().replace("Z", "+0000"), "%Y-%m-%dT%H:%M%z")
    except ValueError:
        raise Refused("REFUSED: --wait-until %r is not UTC ISO (2026-10-09T13:01Z or 2026-10-09T13:01:00Z)" % s)
    t = t.astimezone(datetime.timezone.utc)
    if t <= now:
        raise Refused("REFUSED: --wait-until %s is not in the future" % stamp(t))
    if t > now + datetime.timedelta(days=MAX_WAIT_DAYS):
        raise Refused("REFUSED: --wait-until %s is more than %d days out; a longer wait is a hold, not a dated event" % (
            stamp(t), MAX_WAIT_DAYS))
    return stamp(t)


def wait_of(d: dict):
    """The dated event a CLOSED file's fold or resume named (resume wins), or None."""
    return ((d.get("resumed") or {}).get("wait_until") or (d.get("fold") or {}).get("wait_until")) if d else None


def latest_wait(docs: list, serial: str, project: str, now):
    """(id, until) of the newest CLOSED file of this COO and project whose named event time is still ahead, or None.
    The fix for dell1's finding (1.0.0_SA_CTO~DELL1 msg 1883 via 4.0.0_SA_CRO~DELL1 msg 1885): three cases re-fired on
    waits already folded (UB-003b, UB-b3fc, UB-8ca7)."""
    hits = [d for d in docs if d["from_serial"] == serial and d["project"] == project and d["state"] == "CLOSED"
            and wait_of(d) and wait_of(d) > stamp(now)]
    if not hits:
        return None
    d = sorted(hits, key=lambda x: x["opened_at"])[-1]
    return d["id"], wait_of(d)


OWED_DEFAULT_WINDOW_H = 4.0   # no declared window: 4h from the ledger entry's opened_at (3.0.0_SA_CVO~Z @23f60a21df)


def parse_utc(s: str):
    """An ISO time ('...Z' or '...+00:00', fractional seconds allowed) as an aware UTC datetime, or None."""
    try:
        t = datetime.datetime.fromisoformat(str(s).strip().replace("Z", "+00:00"))
    except ValueError:
        return None
    return (t if t.tzinfo else t.replace(tzinfo=datetime.timezone.utc)).astimezone(datetime.timezone.utc)


def owed_in_progress(owner_live: bool, entry, now) -> tuple:
    """PURE. (True, until) when an owed act counts the tick as WAITING; (False, reason) otherwise. The CVO's bound: LIVE owner,
    an OPEN ledger entry for the act, and still inside the act's window (declared window_hours, else 4h from opened_at), because
    LIVE plus ledger-open is also what a hung apply looks like."""
    if not owner_live:
        return False, "owner-not-live"
    if not isinstance(entry, dict) or str(entry.get("status", "")).upper() != "OPEN":
        return False, "ledger-not-open"
    opened = parse_utc(entry.get("opened_at", ""))
    if opened is None:
        return False, "ledger-opened_at-unreadable"
    try:
        hours = float(entry["window_hours"]) if entry.get("window_hours") not in (None, "") else OWED_DEFAULT_WINDOW_H
    except (TypeError, ValueError):
        hours = OWED_DEFAULT_WINDOW_H
    until = opened + datetime.timedelta(hours=hours)
    if now >= until:
        return False, "outside-window"
    return True, stamp(until)


def entry_counts_on_tree(is_shared_tree: bool, own_commits_touched: bool, uncommitted: bool) -> bool:
    """PURE. Whether an OPEN entry file seen in a worktree is that tree's OWN record. The shared tree is the box's record;
    a linked worktree counts it only if its branch's own commits touched it or it is uncommitted there. A copy inherited
    by cutting the branch while the ledger was open does not count (1.0.0_SA_CTO~Z msg 32766, amending UB-fafc)."""
    return is_shared_tree or own_commits_touched or uncommitted


def _git_out(args: list) -> str:
    try:
        return subprocess.run(["git"] + args, capture_output=True, text=True, timeout=30).stdout
    except (OSError, subprocess.SubprocessError):
        return ""


def open_ledger_entry(slug: str) -> tuple:
    """(newest OPEN entry dict or None, live worktrees read). NEVER-2's union read: the entry FILE on disk in every live
    worktree (`git worktree list`), which also sees an entry still uncommitted on a worker branch -- counted only where
    entry_counts_on_tree() says the tree owns it."""
    out = _git_out(["-C", ROOT, "worktree", "list", "--porcelain"])
    trees = [ln[len("worktree "):].strip() for ln in out.splitlines() if ln.startswith("worktree ")] or [ROOT]
    shared = os.path.normcase(os.path.abspath(trees[0]))   # git lists the main (shared) worktree first
    shared_head = _git_out(["-C", trees[0], "rev-parse", "HEAD"]).strip()
    rel = "org/critical_paths/.open_deploys/%s.json" % slug
    best = None
    for t in trees:
        p = os.path.join(t, *rel.split("/"))
        try:
            e = json.load(open(p, encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if not (isinstance(e, dict) and str(e.get("status", "")).upper() == "OPEN"):
            continue
        is_shared = os.path.normcase(os.path.abspath(t)) == shared
        own = dirty = False
        if not is_shared:
            dirty = bool(_git_out(["-C", t, "status", "--porcelain", "--", rel]).strip())
            base = _git_out(["-C", t, "merge-base", "HEAD", shared_head]).strip() if shared_head else ""
            own = bool(base) and bool(_git_out(["-C", t, "log", "--format=%H", "%s..HEAD" % base, "--", rel]).strip())
        if entry_counts_on_tree(is_shared, own, dirty) and \
                (best is None or str(e.get("opened_at", "")) > str(best.get("opened_at", ""))):
            best = e
    return best, len(trees)


CALL_WAITING_STATES = ("OPEN", "HELD")   # 1.0.0_SA_CTO~Z msg 32856 (CVO @f59dbc4f71): OPEN or HELD on the open-calls surface


def call_waiting(row) -> tuple:
    """PURE. (True, state) when an owed open call still stands (its row reads OPEN or HELD); (False, reason) otherwise --
    a CLOSED or absent call counts the tick as before, so a closed card never silences the counter."""
    if not isinstance(row, dict):
        return False, "call-absent"
    st = str(row.get("state", "")).upper()
    return (True, st) if st in CALL_WAITING_STATES else (False, "call-" + (st.lower() or "no-state"))


def open_call_row(call_id: str):
    """The row for `call_id` on its box's open-calls surface (org/devices/state/<box>/open_calls.json; the box is the id's
    prefix, as `open-calls.py` mints them), or None when the file or the row is absent."""
    box = call_id.split("-", 1)[0]
    root = os.environ.get("OPAL_OPEN_CALLS_STATE_ROOT", "").strip() or os.path.join(ROOT, "org", "devices", "state")
    try:
        doc = json.load(open(os.path.join(root, box, "open_calls.json"), encoding="utf-8"))
    except (OSError, ValueError):
        return None
    rows = doc.get("rows") if isinstance(doc, dict) else None
    return next((r for r in (rows or []) if isinstance(r, dict) and r.get("id") == call_id), None)


class CallUnreadable(Exception):
    """A FOREIGN box's approval list has no readable source: the owed call reads EMPTY, never absent."""


def _call_reader(box: str) -> tuple:
    """(mode, module, why). 'own': this box's own call, the working-tree read as before. 'foreign': open-calls.py approval_read
    (the freshest source, NFRA_DEVPLN DP-e-2), loaded by file path because its name has a hyphen. 'fallback': this box or the
    reader cannot be established, so the working-tree read as before, and `why` says so."""
    try:
        mine = this_box()
    except Exception as exc:  # noqa: BLE001 -- an unresolved identity fails closed to the old read, and says so
        return "fallback", None, "this box unresolved: %s" % str(exc)[:200]
    if mine == box:
        return "own", None, ""
    try:
        return "foreign", load_mod("opal_open_calls_for_unblock", ".tools/open-calls.py"), ""
    except Exception as exc:  # noqa: BLE001 -- an unloadable reader fails closed to the old read, and says so
        return "fallback", None, "open-calls.py not loadable (%s)" % type(exc).__name__


def _source_label(where: str, box: str) -> str:
    """cluster | git | working-tree: which copy approval_read answered from, read off its `where`. open-calls.py names the cluster
    object s3://..., origin/box/<box>:... for git, and its test stand-ins are <dir>/box=<box>/ and <dir>/git=<box>/."""
    if where.startswith("s3://"):
        return "cluster"
    if where.startswith("origin/box/"):
        return "git"
    parent = os.path.basename(os.path.dirname(where))
    if parent == "box=%s" % box:
        return "cluster"
    if parent == "git=%s" % box:
        return "git"
    return "working-tree"


def open_call_read(call_id: str) -> tuple:
    """(row or None, source). A FOREIGN box's call reads through approval_read: the greatest written_at of the cluster copy,
    origin/box/<box> and the working-tree copy. Raises CallUnreadable when no source of a foreign box is readable. This box's
    own calls keep the working-tree read as before (source=own); a fallback reads that same copy (source=working-tree)."""
    box = call_id.split("-", 1)[0]
    mode, mod, why = _call_reader(box)
    if mode == "foreign":
        try:
            doc, where = mod.approval_read(box, None)
        except Exception as exc:  # noqa: BLE001 -- the reader's BadFile is the refusal; any other failure is equally unreadable
            raise CallUnreadable("%s: %s" % (box, str(exc)[:200]))
        rows = doc.get("rows") if isinstance(doc, dict) else None
        row = next((r for r in (rows or []) if isinstance(r, dict) and r.get("id") == call_id), None)
        return row, _source_label(where, box)
    if mode == "fallback":
        print("NOTE: owed-call %s reads the working-tree copy, not the freshest source (%s)" % (call_id, why))
    return open_call_row(call_id), ("own" if mode == "own" else "working-tree")


def owed_call_verdict(call_id: str) -> tuple:
    """(ok, why, source) for --owed-call. source is None only when a foreign list has no readable source (why=call-unreadable)."""
    try:
        row, source = open_call_read(call_id)
    except CallUnreadable:
        return False, "call-unreadable", None
    ok, why = call_waiting(row)
    return ok, why, source


def dated_wait(owner: str, owner_live: bool, until: str) -> tuple:
    """PURE. (True, until) when a dated wait counts the tick as WAITING; (False, reason) otherwise. The owner is a seat that
    must be LIVE, or `schedule:<name>` for a scheduled fire, which a clock owns (brief gpt-feedback-autonomy-solutions item 4,
    ruled YES by 1.0.0_SA_CTO @ba20ac668b: 'a dependency with a live owner and a time is a wait')."""
    if not owner:
        return False, "no-owner"
    if not owner.startswith("schedule:") and not owner_live:
        return False, "owner-not-live"
    return True, until


def tick_verdict(empty_before: int, result: str, active, waiting=None, owed=None, call=None, dated=None) -> tuple:
    """PURE. (new empty count, verdict). A tick that found work resets the count; a SIGNED file means resume on it. With no
    file in flight, a resumed file's named event time still ahead (`waiting` = (id, until)) holds the count at 0 and reads
    WAITING, so a dated wait already folded never re-fires; the count restarts once the time has passed. An owed act in
    progress (`owed` = (slug, owner, until), only when owed_in_progress() said so) reads WAITING the same way."""
    if active is not None and active["state"] == "SIGNED":
        return 0, "RESUME %s" % active["id"]
    if result == "work":
        return 0, ("WAITING %s %s" % (active["id"], active["state"])) if active else "KEEP-DRIVING"
    n = empty_before + 1
    if active is not None:
        return n, "WAITING %s %s" % (active["id"], active["state"])
    if waiting is not None:
        return 0, "WAITING %s UNTIL %s" % waiting
    if owed is not None:
        return 0, "WAITING OWED %s %s UNTIL %s" % owed
    if call is not None:
        return 0, "WAITING CALL %s %s" % call
    if dated is not None:
        return 0, "WAITING DATED %s UNTIL %s" % dated
    return n, ("THIRD-EMPTY-TICK" if n > EMPTY_TICKS_BEFORE else "KEEP-DRIVING")


def cmd_tick(args) -> int:
    safe = re.sub(r"[^A-Za-z0-9._~-]", "_", "%s__%s" % (args.serial, args.project))
    path = os.path.join(ticks_dir(), safe + ".json")
    try:
        before = int(json.load(open(path, encoding="utf-8")).get("empty", 0))
    except (OSError, ValueError):
        before = 0
    waiting = None
    try:
        active = active_for(args.serial, args.project)
        if active is None:
            waiting = latest_wait(list_all(), args.serial, args.project, now_dt())
    except Exception as exc:  # noqa: BLE001 -- the store being down never blocks a tick; it is named
        active = None
        print("WARN: unblock store unreadable (%s); counting without it" % type(exc).__name__)
    owed = None
    if args.owed_ledger and args.result == "nothing" and active is None and waiting is None:
        scan = load_mod("opal_scan_for_unblock", ".tools/open-calls-scan.py")
        live = scan.is_live(scan.liveness().get(args.owed_owner), now_dt().timestamp())
        entry, trees = open_ledger_entry(args.owed_ledger)
        ok, why = owed_in_progress(live, entry, now_dt())
        print("OWED: slug=%s owner=%s live=%s ledger=%s trees=%d counts=%s %s" % (
            args.owed_ledger, args.owed_owner, live, "OPEN" if entry else "absent", trees, "WAITING" if ok else "EMPTY",
            ("until=" + why) if ok else ("reason=" + why)))
        if ok:
            owed = (args.owed_ledger, args.owed_owner, why)
    call = None
    if args.owed_call and args.result == "nothing" and active is None and waiting is None and owed is None:
        ok, why, source = owed_call_verdict(args.owed_call)
        if source is None:   # a foreign list with no readable source: EMPTY, and never reads as absent
            print("OWED-CALL: id=%s counts=EMPTY reason=call-unreadable" % args.owed_call)
        else:
            print("OWED-CALL: id=%s counts=%s %s source=%s" % (args.owed_call, "WAITING" if ok else "EMPTY",
                                                              ("state=" + why) if ok else ("reason=" + why), source))
        if ok:
            call = (args.owed_call, why)
    dated = None
    if getattr(args, "wait_until", None) and args.result == "nothing" and active is None and waiting is None \
            and owed is None and call is None:
        until = parse_wait(args.wait_until, now_dt())          # refuses garbage, a past time, or more than 7 days out
        owner = (args.owner or "").strip()
        live = False
        if owner and not owner.startswith("schedule:"):
            scan = load_mod("opal_scan_for_unblock", ".tools/open-calls-scan.py")
            live = scan.is_live(scan.liveness().get(owner), now_dt().timestamp())
        ok, why = dated_wait(owner, live, until)
        print("DATED: owner=%s live=%s counts=%s %s" % (owner or "(none)", live if not owner.startswith("schedule:") else "clock",
                                                        "WAITING" if ok else "EMPTY", ("until=" + why) if ok else ("reason=" + why)))
        if ok:
            dated = (owner, why)
    n, verdict = tick_verdict(before, args.result, active, waiting, owed, call, dated)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump({"empty": n, "at": stamp(now_dt()), "verdict": verdict}, fh)
    if verdict == "THIRD-EMPTY-TICK":
        print("NEXT: write ## Position / ## Endpoint / ## Blocked and run: python .tools/unblock.py open --project %s --by %s "
              "--body <file>" % (args.project, args.serial))
    elif verdict.startswith("RESUME"):
        print("NEXT: read the signed fold (python .tools/unblock.py show --id %s), drive on it, then unblock.py resume --id %s --by %s"
              % (active["id"], active["id"], args.serial))
    print("UNBLOCK-TICK serial=%s project=%s empty=%d verdict=%s" % (args.serial, args.project, n, verdict))
    return 0


# ---------------------------------------------------------------- the three acts

def cmd_open(args) -> int:
    body = open(args.body, encoding="utf-8").read()
    miss = headings_missing(body, COO_HEADINGS)
    if miss:
        raise Refused("REFUSED: the position lacks %s: tell the CRO your position, the endpoint, why you are blocked, and the "
                      "chase of every act another seat owed (`## Owed by others`: owner, liveness read, LIVE/IDLE/HUNG/ABSENT, ack "
                      "or none, relocation/park/workaround -- or `none` and the trail that showed it)" % ", ".join(miss))
    act = active_for(args.by, args.project)
    if act is not None:
        raise Refused("REFUSED: %s already has %s %s for %s" % (args.by, act["id"], act["state"], args.project))
    box = this_box()
    cro = live_cro_here(box)
    t = now_dt()
    uid = "UB-%s-%s" % (t.strftime("%Y%m%dT%H%M%SZ"), secrets.token_hex(2))
    doc = {"schema": SCHEMA, "id": uid, "project": args.project, "from_device": box, "from_serial": args.by,
           "cro_device": box if cro else "laptop", "opened_at": stamp(t), "body": body, "state": "OPEN", "proposal": None,
           "fold": None, "signoff": None, "refusals": [], "resumed": None}
    XA._put(key_of(uid), doc)
    print("UNBLOCK-OPENED id=%s project=%s from=%s/%s cro_device=%s (%s)" % (
        uid, args.project, box, args.by, doc["cro_device"], "CRO %s live here" % cro if cro else "no CRO live here"))
    return 0


def cmd_propose(args) -> int:
    d = get(args.id)
    if d["state"] != "OPEN":
        raise Refused("REFUSED: %s is %s, not OPEN" % (args.id, d["state"]))
    body = open(args.body, encoding="utf-8").read()
    miss = headings_missing(body, CRO_HEADINGS)
    if miss:
        raise Refused("REFUSED: the approach lacks %s" % ", ".join(miss))
    d["state"] = "PROPOSED"
    d["proposal"] = {"at": stamp(now_dt()), "by": args.by, "device": this_box(), "body": body}
    XA._put(key_of(d["id"]), d)
    print("UNBLOCK-PROPOSED id=%s by=%s -> the CTO of box %s folds it" % (d["id"], args.by, d["from_device"]))
    return 0


def record_root() -> str:
    return os.environ.get("OPAL_UNBLOCK_RECORD_ROOT", "").strip() or os.path.join(ROOT, REC_DIR.replace("/", os.sep))


def render(d: dict) -> str:
    out = ["# Unblock %s -- %s" % (d["id"], d["project"]), "",
           "**COO:** %s on box %s, opened %s. **State:** %s" % (d["from_serial"], d["from_device"], d["opened_at"], d["state"]), "",
           "## The COO's position (verbatim)", "", d["body"].rstrip(), ""]
    if d["proposal"]:
        p = d["proposal"]
        out += ["## The CRO's approach (verbatim; %s on %s at %s)" % (p["by"], p["device"], p["at"]), "", p["body"].rstrip(), ""]
    for r in d["refusals"]:
        out += ["## A CVO refusal (%s at %s; fold was `%s`)" % (r["by"], r["at"], r["fold_ref"]), "", r["reason"].rstrip(), ""]
    if d["fold"]:
        f = d["fold"]
        out += ["## The CTO's fold (%s on %s at %s)" % (f["by"], f["device"], f["at"]), "", "Folded into: `%s`" % f["ref"], ""]
        if f.get("wait_until"):
            out += ["Dated wait: the COO's ticks read WAITING until %s." % f["wait_until"], ""]
    if d["signoff"]:
        g = d["signoff"]
        out += ["## The CVO's sign-off (%s on %s at %s)" % (g["by"], g["device"], g["at"]), "", (g["note"] or "signed").rstrip(), ""]
    return "\n".join(out) + "\n"


def cmd_fold(args) -> int:
    d = get(args.id)
    if d["state"] != "PROPOSED":
        raise Refused("REFUSED: %s is %s, not PROPOSED" % (args.id, d["state"]))
    ref = args.ref.replace("\\", "/")
    if not os.path.isfile(os.path.join(ROOT, ref)):
        raise Refused("REFUSED: %s is not a file in this tree; fold cites the PRD addendum, round-N analysis or ruling it "
                      "landed in" % ref)
    wait = parse_wait(args.wait_until, now_dt()) if getattr(args, "wait_until", None) else None
    box = this_box()
    cvo = live_seat_here(box, CVO_OF, "3.0.0_SA_CVO")
    d["state"] = "FOLDED"
    d["fold"] = {"at": stamp(now_dt()), "by": args.by, "device": box, "ref": ref, "cvo_device": box if cvo else "laptop"}
    if wait:
        d["fold"]["wait_until"] = wait
    XA._put(key_of(d["id"]), d)
    print("UNBLOCK-FOLDED id=%s into %s -> the CVO on box %s signs it (%s)" % (
        d["id"], ref, d["fold"]["cvo_device"], "CVO %s live here" % cvo if cvo else "no CVO live here"))
    return 0


def cmd_sign(args) -> int:
    d = get(args.id)
    if d["state"] != "FOLDED":
        raise Refused("REFUSED: %s is %s, not FOLDED" % (args.id, d["state"]))
    box = this_box()
    t = now_dt()
    name = "%s_%s.md" % (t.strftime("%Y%m%dT%H%MZ"), d["id"])
    d["state"] = "SIGNED"
    d["signoff"] = {"at": stamp(t), "by": args.by, "device": box, "note": args.note or "", "record": "%s/%s" % (REC_DIR, name)}
    os.makedirs(record_root(), exist_ok=True)
    with open(os.path.join(record_root(), name), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(render(d))
    XA._put(key_of(d["id"]), d)
    print("UNBLOCK-SIGNED id=%s by=%s record=%s/%s -- commit the record; the COO's next tick reads RESUME" % (
        d["id"], args.by, REC_DIR, name))
    return 0


def cmd_refuse(args) -> int:
    d = get(args.id)
    if d["state"] != "FOLDED":
        raise Refused("REFUSED: %s is %s, not FOLDED" % (args.id, d["state"]))
    if not (args.reason or "").strip():
        raise Refused("REFUSED: a refusal names its reason")
    d["refusals"].append({"at": stamp(now_dt()), "by": args.by, "reason": args.reason, "fold_ref": d["fold"]["ref"]})
    d["state"], d["fold"] = "PROPOSED", None
    XA._put(key_of(d["id"]), d)
    print("UNBLOCK-REFUSED id=%s by=%s -> back to the CTO of box %s to fold again" % (d["id"], args.by, d["from_device"]))
    return 0


def cmd_resume(args) -> int:
    d = get(args.id)
    if d["state"] != "SIGNED":
        raise Refused("REFUSED: %s is %s, not SIGNED (the CVO signs the fold before the COO resumes)" % (args.id, d["state"]))
    wait = parse_wait(args.wait_until, now_dt()) if getattr(args, "wait_until", None) else None
    d["state"] = "CLOSED"
    d["resumed"] = {"at": stamp(now_dt()), "by": args.by}
    if wait:
        d["resumed"]["wait_until"] = wait
    XA._put(key_of(d["id"]), d)
    print("UNBLOCK-CLOSED id=%s resumed by %s on %s%s" % (d["id"], args.by, d["fold"]["ref"],
                                                       (" -- ticks read WAITING until %s" % wait_of(d)) if wait_of(d) else ""))
    return 0


def cmd_list(args) -> int:
    want = args.state.upper()
    docs = sorted(list_all(), key=lambda d: d["opened_at"])
    n = 0
    for d in docs:
        if want != "ALL" and d["state"] != want:
            continue
        n += 1
        print("%s [%s] %s from %s/%s cro_device=%s opened %s%s" % (
            d["id"], d["state"], d["project"], d["from_device"], d["from_serial"], d["cro_device"], d["opened_at"],
            (" -> %s" % d["fold"]["ref"]) if d["fold"] else ""))
    print("UNBLOCK-LIST state=%s shown=%d total=%d" % (want, n, len(docs)))
    return 0


def cmd_show(args) -> int:
    print(render(get(args.id)))
    return 0


# ---------------------------------------------------------------- selftest

def selftest() -> int:
    cases = []

    def rec(name, ok):
        cases.append(bool(ok))
        print("%s %s" % ("PASS" if ok else "FAIL", name))

    base = tempfile.mkdtemp(prefix="unblock_selftest_")
    keep = {k: os.environ.get(k) for k in ("OPAL_XADJ_LOCAL", "OPAL_UNBLOCK_RECORD_ROOT")}
    os.environ["OPAL_XADJ_LOCAL"] = os.path.join(base, "store")
    os.environ["OPAL_UNBLOCK_RECORD_ROOT"] = os.path.join(base, "rec")
    try:
        rec("first-empty-tick-keeps-driving", tick_verdict(0, "nothing", None) == (1, "KEEP-DRIVING"))
        rec("second-empty-tick-keeps-driving", tick_verdict(1, "nothing", None) == (2, "KEEP-DRIVING"))
        rec("third-empty-tick-writes-to-the-cro", tick_verdict(2, "nothing", None) == (3, "THIRD-EMPTY-TICK"))
        rec("a-tick-with-work-resets-the-count", tick_verdict(2, "work", None) == (0, "KEEP-DRIVING"))
        t = stamp(now_dt())
        d = {"schema": SCHEMA, "id": "UB-20261009T000000Z-abcd", "project": "P", "from_device": "dell1",
             "from_serial": "2.0.0_SA_COO~M1", "cro_device": "laptop", "opened_at": t, "body": "## Position\n## Endpoint\n## Blocked\n",
             "state": "OPEN", "proposal": None, "fold": None, "signoff": None, "refusals": [], "resumed": None}
        rec("an-open-file-waits-and-does-not-re-trigger", tick_verdict(5, "nothing", d)[1] == "WAITING %s OPEN" % d["id"])
        f = dict(d, state="FOLDED", proposal={"at": t, "by": "c", "device": "laptop", "body": "b"},
                 fold={"at": t, "by": "x", "device": "dell1", "ref": "r.md", "cvo_device": "laptop"})
        rec("a-folded-but-unsigned-file-still-waits", tick_verdict(5, "nothing", f)[1] == "WAITING %s FOLDED" % d["id"])
        g = dict(f, state="SIGNED", signoff={"at": t, "by": "3.0.0_SA_CVO", "device": "laptop", "note": "", "record": "x.md"})
        rec("a-signed-file-means-resume", tick_verdict(5, "nothing", g) == (0, "RESUME %s" % d["id"]))
        # the dated wait (dell1, msg 1885): a resumed file naming a future event holds the count; a past one does not
        now = now_dt()
        ahead = stamp(now + datetime.timedelta(hours=5))
        c = dict(g, state="CLOSED", resumed={"at": t, "by": "2.0.0_SA_COO~M1", "wait_until": ahead})
        w = latest_wait([c], "2.0.0_SA_COO~M1", "P", now)
        rec("a-closed-file-with-a-future-wait-reads-waiting-and-holds-the-count",
            w == (d["id"], ahead) and tick_verdict(2, "nothing", None, w) == (0, "WAITING %s UNTIL %s" % (d["id"], ahead)))
        past = dict(c, resumed=dict(c["resumed"], wait_until=stamp(now - datetime.timedelta(minutes=1))))
        rec("a-passed-wait-counts-again", latest_wait([past], "2.0.0_SA_COO~M1", "P", now) is None
            and tick_verdict(2, "nothing", None, None) == (3, "THIRD-EMPTY-TICK"))
        fw = dict(c, resumed={"at": t, "by": "x"}, fold=dict(c["fold"], wait_until=ahead))
        rec("the-folds-wait-counts-when-the-resume-names-none", latest_wait([fw], "2.0.0_SA_COO~M1", "P", now) == (d["id"], ahead))
        rec("another-coo-or-project-is-not-held", latest_wait([c], "2.0.0_SA_COO~X1", "P", now) is None
            and latest_wait([c], "2.0.0_SA_COO~M1", "Q", now) is None)
        bad = []
        for s in ("2026-13-01T00:00Z", stamp(now - datetime.timedelta(hours=1)), stamp(now + datetime.timedelta(days=8))):
            try:
                parse_wait(s, now)
                bad.append(s)
            except Refused:
                pass
        rec("wait-until-refuses-garbage-past-and-beyond-seven-days", bad == []
            and parse_wait(ahead.replace(":00Z", "Z") if ahead.endswith(":00Z") else ahead, now) <= ahead)
        # the pre-case dated wait (item 4, @ba20ac668b): a live seat or a schedule holds the count; a dead owner does not
        rec("dated-wait-live-owner-or-schedule-holds-the-count",
            dated_wait("1.0.0_SA_CTO~DELL1", True, ahead) == (True, ahead)
            and dated_wait("schedule:mdpf-sechist-pull-1100z", False, ahead) == (True, ahead)
            and tick_verdict(2, "nothing", None, dated=("schedule:x", ahead)) == (0, "WAITING DATED schedule:x UNTIL %s" % ahead))
        rec("dated-wait-dead-or-no-owner-counts-as-before",
            dated_wait("2.0.0_SA_COO~Q1", False, ahead) == (False, "owner-not-live") and dated_wait("", True, ahead)[0] is False
            and tick_verdict(2, "nothing", None) == (3, "THIRD-EMPTY-TICK"))
        rec("work-still-resets-with-a-dated-wait", tick_verdict(2, "work", None, dated=("schedule:x", ahead)) == (0, "KEEP-DRIVING"))
        XA._put(key_of(d["id"]), d)
        rec("store-round-trip-and-active-lookup", active_for("2.0.0_SA_COO~M1", "P")["id"] == d["id"]
            and active_for("2.0.0_SA_COO~M1", "Q") is None)
        try:
            check(dict(d, state="PROPOSED"), "x")
            rec("proposed-without-a-proposal-is-refused", False)
        except Refused:
            rec("proposed-without-a-proposal-is-refused", True)
        rec("coo-headings-checked", headings_missing("## Position\n", COO_HEADINGS) == ["## Endpoint", "## Blocked",
                                                                                         "## Owed by others"])
        rec("hung-at-ten-minutes-per-1k-tokens", hung_verdict(10, 1000)[0] == "HUNG" and hung_verdict(9, 1000)[0] == "WORKING"
            and hung_verdict(10, parse_tokens("1.2k"))[0] == "WORKING" and hung_verdict(25, parse_tokens("2k"))[0] == "HUNG")
        rec("zero-tokens-after-time-is-hung-zero-time-is-not", hung_verdict(3, 0)[0] == "HUNG" and hung_verdict(0, 0)[0] == "WORKING")
        # the owed-act bound (3.0.0_SA_CVO~Z @23f60a21df): WAITING only while LIVE + ledger OPEN + inside the window
        ent = {"slug": "s", "status": "OPEN", "opened_at": stamp(now - datetime.timedelta(hours=1)), "window_hours": 2.0}
        ok_w = owed_in_progress(True, ent, now)
        rec("owed-act-live-open-in-window-reads-waiting", ok_w[0] and tick_verdict(2, "nothing", None, None, ("s", "o", ok_w[1]))
            == (0, "WAITING OWED s o UNTIL %s" % ok_w[1]))
        rec("owed-act-owner-not-live-counts-empty", owed_in_progress(False, ent, now) == (False, "owner-not-live"))
        rec("owed-act-no-open-ledger-counts-empty", owed_in_progress(True, None, now)[1] == "ledger-not-open"
            and owed_in_progress(True, dict(ent, status="CLOSED"), now)[1] == "ledger-not-open")
        rec("owed-act-past-its-window-counts-empty-so-a-hung-apply-opens-a-case",
            owed_in_progress(True, dict(ent, window_hours=0.5), now) == (False, "outside-window")
            and tick_verdict(2, "nothing", None, None, None) == (3, "THIRD-EMPTY-TICK"))
        und = dict(ent, window_hours=None, opened_at=stamp(now - datetime.timedelta(hours=3)))
        rec("owed-act-without-a-window-gets-four-hours", owed_in_progress(True, und, now)[0]
            and owed_in_progress(True, dict(und, opened_at=stamp(now - datetime.timedelta(hours=5))), now)[1] == "outside-window")
        rec("owed-act-fractional-iso-opened-at-parses", owed_in_progress(
            True, dict(ent, opened_at=(now - datetime.timedelta(minutes=5)).isoformat()), now)[0])
        rec("an-inherited-branch-copy-of-a-ledger-does-not-count", entry_counts_on_tree(True, False, False)
            and entry_counts_on_tree(False, True, False) and entry_counts_on_tree(False, False, True)
            and not entry_counts_on_tree(False, False, False))
        rec("owed-call-open-or-held-reads-waiting", call_waiting({"state": "OPEN"}) == (True, "OPEN")
            and call_waiting({"state": "held"}) == (True, "HELD")
            and tick_verdict(2, "nothing", None, None, None, ("sitez-x", "OPEN")) == (0, "WAITING CALL sitez-x OPEN"))
        rec("owed-call-closed-or-absent-counts-empty", call_waiting({"state": "CLOSED"}) == (False, "call-closed")
            and call_waiting(None) == (False, "call-absent"))
        oc = os.path.join(base, "oc", "sitez")
        os.makedirs(oc)
        with open(os.path.join(oc, "open_calls.json"), "w", encoding="utf-8") as fh:
            json.dump({"rows": [{"id": "sitez-20261009T150500Z-4d5a", "state": "OPEN"}]}, fh)
        os.environ["OPAL_OPEN_CALLS_STATE_ROOT"] = os.path.join(base, "oc")
        rec("owed-call-reads-the-boxs-open-calls-surface-by-id-prefix",
            open_call_row("sitez-20261009T150500Z-4d5a") == {"id": "sitez-20261009T150500Z-4d5a", "state": "OPEN"}
            and open_call_row("sitez-20261009T150500Z-ffff") is None and open_call_row("dell1-20261009T000000Z-0000") is None)
        os.environ.pop("OPAL_OPEN_CALLS_STATE_ROOT", None)
        rec("an-open-unblock-file-still-wins-over-an-owed-act", tick_verdict(5, "nothing", d, None, ("s", "o", "t"))[1]
            == "WAITING %s OPEN" % d["id"])
        rec("record-carries-all-four-voices", all(s in render(check(g, "g")) for s in
                                                  ("The COO's position", "The CRO's approach", "The CTO's fold",
                                                   "The CVO's sign-off")))
    finally:
        for k, v in keep.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
        import shutil
        shutil.rmtree(base, ignore_errors=True)
    ok = all(cases)
    print("UNBLOCK-SELFTEST cases=%d/%d ok=%s" % (sum(cases), len(cases), ok))
    return 0 if ok else 1


def main(argv: list) -> int:
    ap = argparse.ArgumentParser(prog="unblock.py", description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    sub = ap.add_subparsers(dest="cmd")
    t = sub.add_parser("tick")
    t.add_argument("--serial", required=True)
    t.add_argument("--project", required=True)
    t.add_argument("--result", required=True, choices=("nothing", "work"))
    t.add_argument("--owed-ledger", default="", help="slug of the owed act's org/critical_paths/.open_deploys/ entry")
    t.add_argument("--owed-owner", default="", help="serial of the seat that owes the act")
    t.add_argument("--owed-call", default="", help="open-call id the project waits on (WAITING while OPEN or HELD)")
    t.add_argument("--wait-until", default="", help="UTC ISO time of the dated event the project waits on, before any case "
                                                    "(WAITING DATED while ahead and the owner is live; at most 7 days)")
    t.add_argument("--owner", default="", help="with --wait-until: the LIVE seat that owns the wait, or schedule:<name> for "
                                               "a scheduled fire")
    o = sub.add_parser("open")
    o.add_argument("--project", required=True)
    o.add_argument("--by", required=True)
    o.add_argument("--body", required=True)
    p = sub.add_parser("propose")
    p.add_argument("--id", required=True)
    p.add_argument("--by", required=True)
    p.add_argument("--body", required=True)
    f = sub.add_parser("fold")
    f.add_argument("--id", required=True)
    f.add_argument("--by", required=True)
    f.add_argument("--ref", required=True)
    f.add_argument("--wait-until", help="UTC ISO time of the dated event the fold waits on; the COO's ticks read WAITING until then")
    sg = sub.add_parser("sign")
    sg.add_argument("--id", required=True)
    sg.add_argument("--by", required=True)
    sg.add_argument("--note")
    rf = sub.add_parser("refuse")
    rf.add_argument("--id", required=True)
    rf.add_argument("--by", required=True)
    rf.add_argument("--reason", required=True)
    r = sub.add_parser("resume")
    r.add_argument("--id", required=True)
    r.add_argument("--by", required=True)
    r.add_argument("--wait-until", help="UTC ISO time of the dated event the COO resumes to wait on (wins over the fold's)")
    hg = sub.add_parser("hung", help="the 10:1 test on a peeked seat's running query (Andrew-direct 2026-10-09 ~06:3xZ)")
    hg.add_argument("--minutes", required=True, type=float, help="the query's elapsed minutes, read off the peek")
    hg.add_argument("--tokens", required=True, help="the query's tokens, read off the peek (1200, 1.2k)")
    lst = sub.add_parser("list")
    lst.add_argument("--state", default="ALL")
    s = sub.add_parser("show")
    s.add_argument("--id", required=True)
    args = ap.parse_args(argv)
    if args.selftest:
        return selftest()
    if not args.cmd:
        ap.print_help()
        return 2
    try:
        return {"tick": cmd_tick, "open": cmd_open, "propose": cmd_propose, "fold": cmd_fold, "sign": cmd_sign,
                "refuse": cmd_refuse, "resume": cmd_resume, "hung": cmd_hung,
                "list": cmd_list, "show": cmd_show}[args.cmd](args)
    except Refused as exc:
        print(str(exc), file=sys.stderr)
        return 1 if str(exc).startswith("REFUSED") else 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
