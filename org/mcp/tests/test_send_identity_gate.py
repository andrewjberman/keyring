"""G-A sender gate (GA-3): send_message / set_summary / check_inbox self-scope guards.

THE INCIDENT (2026-07-14, 01:51Z + 02:38Z): send_message took from_agent as FREE TEXT
and wrote it verbatim into the header, filename, broker payload, and channel push.
0.4.0_DS_ClientPlatform twice sent junk messages into the CTO's inbox stamped with the
CTO's OWN serial -- by accident (sender field pattern-completed from the recipient),
no check, exit 0 both times, detected only by self-report. The identity guard existed
(NFRA_IDENTITY.G-A) and send_message simply never called it.

*** THE PROVEN-RED ARM IS THE POINT OF THIS FILE. *** The shipped defect was the
ABSENCE of any classifier -- `_old_sender_conflict` below reproduces it verbatim
(every claim passes). If the forged pair ever stops failing against it, this test has
stopped measuring the defect and the green on the fixed path means nothing.

The live-exercise section replays tonight's exact forgery against the REAL
send_message coroutine (in-process): the refused path must write NO file and fire the
audit hook. Mutations that used to succeed must now refuse.

    python org/mcp/tests/test_send_identity_gate.py
"""
from __future__ import annotations

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import server  # noqa: E402
from server import _identity_key, _sender_conflict  # noqa: E402


def _old_sender_conflict(claimed_from: str, my_serial: str | None):
    """THE SHIPPED DEFECT, verbatim: there was no check. Every claim passed."""
    return None


PASS = 0
FAIL = 0


def check(name: str, got, want) -> None:
    global PASS, FAIL
    if got == want:
        PASS += 1
        print(f"  PASS  {name}")
    else:
        FAIL += 1
        print(f"  FAIL  {name}: got {got!r}, want {want!r}")


def kind_of(conflict):
    return conflict[0] if conflict else None


print("== proven-red arm: the shipped absence-of-a-check passes the forged pair ==")
# Tonight's exact forgery: caller registered as DS, from_agent = the CTO's serial.
check("OLD: forged sender PASSED unchecked (the defect)",
      _old_sender_conflict("1.0.0_SA_CTO", "0.4.0_DS_ClientPlatform"), None)

print("== fixed classifier ==")
check("self-send is clean",
      kind_of(_sender_conflict("0.4.0_DS_ClientPlatform", "0.4.0_DS_ClientPlatform")), None)
check("tonight's forgery -> FORGED",
      kind_of(_sender_conflict("1.0.0_SA_CTO", "0.4.0_DS_ClientPlatform")), "FORGED")
check("lane claiming base -> FORGED (a lane suffix IS an identity, F-024)",
      kind_of(_sender_conflict("1.0.0_SA_CTO", "1.0.0_SA_CTO~B")), "FORGED")
check("base claiming lane -> FORGED",
      kind_of(_sender_conflict("1.0.0_SA_CTO~B", "1.0.0_SA_CTO")), "FORGED")
check("unregistered caller -> UNVERIFIED (advisory -- never block the recovery path)",
      kind_of(_sender_conflict("0.4.0_DS_ClientPlatform", None)), "UNVERIFIED")
check("unregistered caller, empty-string serial -> UNVERIFIED",
      kind_of(_sender_conflict("0.4.0_DS_ClientPlatform", "")), "UNVERIFIED")

print("== canonicalisation contract (what the call sites feed the classifier) ==")
check("partial unsuffixed serial canonicalises via folder",
      _identity_key("0.4.0_DS", "0.4.0_DS_ClientPlatform"), "0.4.0_DS_ClientPlatform")
check("suffixed serial is NEVER folder-canonicalised (identity, not location)",
      _identity_key("1.0.0_SA_CTO~B", "1.0.0_SA_CTO"), "1.0.0_SA_CTO~B")

# ---------------------------------------------------------------------------
# Live exercise: the REAL send_message coroutine, in-process. The audit writer is
# swapped for a recorder so probe rows never pollute the real measurement log.
# ---------------------------------------------------------------------------
print("== live exercise: send_message REFUSE path (tonight's forgery, replayed) ==")
_audit_rows = []
server._audit_identity = lambda kind, serial, pid, reason, conflict: _audit_rows.append(kind)

MY = "0.0.0_AB_MSTR"
CTO = "1.0.0_SA_CTO"
cto_inbox = Path(server.INBOX_DIR) / CTO

server._my_serial = MY
res = asyncio.run(server.send_message(
    from_agent=CTO, to_agent=CTO,
    subject="forgery-probe-must-never-land", body="if this file exists the gate failed"))
check("forged send REFUSED", "SEND REFUSED" in res, True)
check("refusal audited as SEND_FORGED_REFUSED", _audit_rows, ["SEND_FORGED_REFUSED"])
landed = list(cto_inbox.glob("*forgery-probe-must-never-land*"))
check("NO file written on refusal", landed, [])

print("== live exercise: auto-fill + verified send (to own inbox) ==")
_audit_rows.clear()
my_inbox = Path(server.INBOX_DIR) / MY
res = asyncio.run(server.send_message(
    from_agent="", to_agent=MY,
    subject="gate-selftest-verified", body="verified self-send via auto-fill"))
check("auto-filled send delivered", "Message delivered" in res, True)
check("no audit row on a clean send", _audit_rows, [])
sent = sorted(my_inbox.rglob("*gate-selftest-verified*"))
check("file landed exactly once", len(sent), 1)
if sent:
    content = sent[0].read_text(encoding="utf-8")
    check("header From is the REGISTERED serial", f"# Message from {MY}" in content, True)
    for f in sent:
        f.unlink()

print("== live exercise: UNVERIFIED path (unregistered session, stamped not blocked) ==")
_audit_rows.clear()
server._my_serial = None
res = asyncio.run(server.send_message(
    from_agent=MY, to_agent=MY,
    subject="gate-selftest-unverified", body="unregistered sender must deliver stamped"))
check("unverified send still delivers", "Message delivered" in res, True)
check("return value carries the unverified note", "sender unverified" in res, True)
check("audited as SEND_UNVERIFIED", _audit_rows, ["SEND_UNVERIFIED"])
sent = sorted(my_inbox.rglob("*gate-selftest-unverified*"))
check("file landed exactly once", len(sent), 1)
if sent:
    content = sent[0].read_text(encoding="utf-8")
    check("artifact carries the Sender-unverified stamp", "**Sender-unverified:**" in content, True)
    for f in sent:
        f.unlink()

print("== live exercise: FORGED + identity_override stamps the TRUE author ==")
_audit_rows.clear()
server._my_serial = MY
res = asyncio.run(server.send_message(
    from_agent=CTO, to_agent=MY,
    subject="gate-selftest-override", body="authorized relay must name its author",
    identity_override="gate selftest: exercising the relay escape"))
check("override send delivers", "Message delivered" in res, True)
check("audited as SEND_FORGED_OVERRIDE", _audit_rows, ["SEND_FORGED_OVERRIDE"])
sent = sorted(my_inbox.rglob("*gate-selftest-override*"))
check("file landed exactly once", len(sent), 1)
if sent:
    content = sent[0].read_text(encoding="utf-8")
    check("artifact names the TRUE author",
          f"**Sender-override:** actually sent by {MY}" in content, True)
    for f in sent:
        f.unlink()

print("== live exercise: self-scope guards on set_summary / check_inbox drain ==")
_audit_rows.clear()
server._my_serial = MY
res = asyncio.run(server.set_summary(CTO, "clobber-probe"))
check("foreign set_summary REFUSED", "set_summary REFUSED" in res, True)
check("audited as SUMMARY_FOREIGN_REFUSED", _audit_rows, ["SUMMARY_FOREIGN_REFUSED"])

_audit_rows.clear()
res = asyncio.run(server.check_inbox(CTO, mark_read=True))
check("foreign inbox DRAIN refused", "REFUSED" in res, True)
check("audited as INBOX_DRAIN_REFUSED", _audit_rows, ["INBOX_DRAIN_REFUSED"])

res = asyncio.run(server.check_inbox(CTO, mark_read=False))
check("foreign inbox READ still allowed (inspection is legal)",
      "REFUSED" not in res, True)

print(f"\n{PASS} passed, {FAIL} failed")
sys.exit(1 if FAIL else 0)
