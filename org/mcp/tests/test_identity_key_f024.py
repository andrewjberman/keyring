"""RV-0048 F-024: deregister_agent STRIPPED THE ~LANE SUFFIX AND KILLED THE BASE AGENT.

It deregistered the CTO -- mid-incident, while he was performing the post-crash recovery --
because he asked it to clean up the zombie registration of `1.0.0_SA_CTO~B`.

    register_agent   stores the FULL serial      '1.0.0_SA_CTO~B'
    deregister_agent deleted the BASE serial     '1.0.0_SA_CTO'      <-- a DIFFERENT AGENT

Both halves were live:
  (a) a LANE could never be deregistered -- its zombie registration was structurally IMMORTAL;
  (b) every attempt to clean a lane zombie SILENTLY KILLED ITS BASE AGENT instead.
And deregistration is restricted to CTO/COO -- so the one authorised survivor, cleaning up the
zombie he is most likely to meet (his own lane), DEREGISTERS HIMSELF. The repair primitive
self-destructs, in exactly the situation it exists for.

ROOT CONFUSION: A FOLDER IS A FILE LOCATION. A SERIAL IS AN IDENTITY.
Lanes SHARE a folder by design (same role docs). They do NOT share a registration.

*** THE PROVEN-RED ARM IS THE POINT OF THIS FILE. *** `_old_identity_key` is the shipped logic,
verbatim. If it ever stops failing, this test has stopped measuring the defect and the green on
the fixed path means nothing. A test that has never been observed to fail has not been shown that
it can.

    python org/mcp/tests/test_identity_key_f024.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from server import _identity_key, _base_serial  # noqa: E402


def _old_identity_key(agent_serial: str, folder_name: str | None) -> str:
    """THE SHIPPED DEFECT, verbatim: `resolved = folder.name if folder else agent_serial`,
    where the folder was resolved by _base_serial() -- i.e. with the ~suffix stripped."""
    base = _base_serial(agent_serial)
    folder = base if folder_name else None          # _resolve_agent_folder matches on the BASE
    return folder if folder else agent_serial


PASS = 0
FAIL = 0


def check(name: str, got, want) -> None:
    global PASS, FAIL
    if got == want:
        PASS += 1
        print(f"  PASS  {name:<62} -> {got}")
    else:
        FAIL += 1
        print(f"  FAIL  {name:<62} -> {got!r} (want {want!r})")


print("F-024 -- a lane is its OWN identity; deregistering it must never touch the base agent.")
print()
print("PROVEN-RED: the SHIPPED logic, on the exact call that deregistered the CTO.")
print("  (if these two stop being red, this suite has stopped measuring the defect)")
old = _old_identity_key("1.0.0_SA_CTO~B", "1.0.0_SA_CTO")
check("OLD: lane ~B resolves to the BASE (the defect)", old, "1.0.0_SA_CTO")
check("OLD: and that base is NOT the serial asked for", old != "1.0.0_SA_CTO~B", True)

print()
print("FIXED -- the lane keeps its own identity:")
check("lane ~B keeps its suffix", _identity_key("1.0.0_SA_CTO~B", "1.0.0_SA_CTO"), "1.0.0_SA_CTO~B")
check("lane ~A keeps its suffix", _identity_key("0.7.0_AE_CloudOps~A", "0.7.0_AE_CloudOps"), "0.7.0_AE_CloudOps~A")
check("lane ~B (CVO)", _identity_key("3.0.0_SA_CVO~B", "3.0.0_SA_CVO"), "3.0.0_SA_CVO~B")

print()
print("...and the BASE path is UNCHANGED (the fix must not break the useful normalisation):")
check("base serial resolves to itself", _identity_key("1.0.0_SA_CTO", "1.0.0_SA_CTO"), "1.0.0_SA_CTO")
check("partial serial canonicalises via folder", _identity_key("0.4.0_DS", "0.4.0_DS_ClientPlatform"), "0.4.0_DS_ClientPlatform")
check("base with no folder falls back to itself", _identity_key("9.9.9_XX_Unknown", None), "9.9.9_XX_Unknown")

print()
print("THE INVARIANT THAT WOULD HAVE CAUGHT IT -- deregister must NEVER return a DIFFERENT agent:")
for s in ("1.0.0_SA_CTO~B", "0.7.0_AE_CloudOps~A", "3.0.0_SA_CVO~B", "2.0.0_SA_COO~C"):
    key = _identity_key(s, _base_serial(s))
    check(f"identity_key({s}) is not the base", key != _base_serial(s), True)

print()
print("...and it must AGREE with what register_agent stored (which is the full serial verbatim):")
for s in ("1.0.0_SA_CTO~B", "0.4.0_DS_ClientPlatform~C", "0.0.0_AB_MSTR"):
    check(f"round-trip register/deregister agree: {s}", _identity_key(s, _base_serial(s)), s)

print()
print("=" * 72)
print(f"PASS: {PASS}   FAIL: {FAIL}")
if FAIL == 0:
    print("ALL CHECKS PASS -- a lane deregisters itself, never its base.")
    sys.exit(0)
print("FAILURES PRESENT.")
sys.exit(1)
