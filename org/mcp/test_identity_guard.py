"""NFRA_IDENTITY.G-A -- replay falsifier + no-regression + SEVERITY exercise for the broker PID guard.

Exercises the REAL guard (`server._identity_conflict` / `_identity_decide` / `_pid_alive`)
against the liveness shapes the broker actually stores. Rule 22a: acceptance rests on the
guard FIRING/PASSING, not on reading the code.

Built by 0.7.0_AE_CloudOps~A; severity split + the mutant bar added by 1.0.0_SA_CTO on the
arch-gate (2026-07-13).

  AC1 REPLAY FALSIFIER -- the 2026-07-12/13 SEV, replayed: a session live+registered
       as 1.0.0_SA_CTO (PID 2508) claims 0.8.0_AE_CloudComp -> MUST hard-REFUSE and name
       the conflict. Falsifier: it registers silently (the pre-guard behaviour).
  AC2 NO-REGRESSION -- (a) same serial + same PID (routine re-register/heartbeat) and
       (b) same serial + FRESH PID after a restart, incumbent process DEAD -> MUST pass.
       Falsifier: the guard refuses a legitimate re-registration (would break every
       agent's startup fabric-wide).
  AC3 SEVERITY (the CTO ruling) -- CROSS is HARD, SERIAL_HELD is ADVISORY.
       CROSS is a LOGICAL impossibility (one process, two identities) -> no false-positive
       branch exists -> refusing is risk-free. SERIAL_HELD is an EMPIRICAL claim resting on
       _pid_alive(), a probe COARSER than the claim it would license: it answers "does SOME
       process hold this PID", never "is THAT AGENT alive" -- it cannot separate a real
       incumbent from a lingering orphan MCP process or a RECYCLED OS pid. A hard refuse
       there would block a legitimate RESPAWN, and the agents most exposed are the ones
       recovering from a death -- turning a transient failure into a permanent one.
  AC4 FAIL-OPEN -- an incumbent whose PID is dead must NOT block (covered by AC2b).
  AC5 MUTANT BAR -- a test that only asserts "some conflict fired" passes under BOTH
       policies and therefore tests NOTHING about the ruling. These assert the ACTION.

Safe to run in a live fabric: pure over (serial, liveness-dict, pid). Writes nothing.

Run: python org/mcp/test_identity_guard.py
"""
from __future__ import annotations

import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import server  # noqa: E402  (the real broker module)

NOW = time.time()
MY_PID = os.getpid()          # a PID that is definitely ALIVE (this process)
DEAD_PID = 999999             # a PID that is definitely not running


def live(pid, secs_ago=3):
    return {"pid": pid, "last_seen_epoch": NOW - secs_ago, "summary": ""}


def act(claimed, data, pid, override=""):
    """Run the guard end-to-end: classify, then apply the severity policy."""
    conflict = server._identity_conflict(claimed, data, pid)
    return server._identity_decide(conflict, override)


def check(name, got_action, want_action, detail=""):
    ok = got_action == want_action
    print(("  PASS " if ok else "  FAIL ") + f"{name}")
    print(f"        action={got_action}  (want {want_action})" + (f"  -- {detail}" if detail else ""))
    return ok


def main():
    results = []
    print("NFRA_IDENTITY.G-A -- broker PID identity guard, exercised\n")

    # --- AC1: THE REPLAY FALSIFIER (the actual SEV) ---------------------------
    # A session running as 1.0.0_SA_CTO at THIS pid claims 0.8.0_AE_CloudComp.
    print("AC1 REPLAY FALSIFIER (the 07-12/13 SEV):")
    sev = {"1.0.0_SA_CTO": live(MY_PID, 3), "0.8.0_AE_CloudComp": live(20004, 5)}
    action, msg = act("0.8.0_AE_CloudComp", sev, MY_PID)
    results.append(check("PID live as 1.0.0_SA_CTO claims 0.8.0 -> REFUSE",
                         action, "REFUSE", "the phantom's FIRST registration dies here"))
    results.append(check("  ...and the refusal NAMES the true holder",
                         "1.0.0_SA_CTO" in msg and "NOT REGISTERED" in msg, True))

    # --- AC2: NO-REGRESSION (the load-bearing one) ---------------------------
    print("\nAC2 NO-REGRESSION (must NOT block legitimate registrations):")
    same = {"0.7.0_AE_CloudOps~A": live(MY_PID, 2)}
    results.append(check("same serial + same PID (routine re-register/heartbeat)",
                         act("0.7.0_AE_CloudOps~A", same, MY_PID)[0], "ALLOW"))

    # restart: same serial, FRESH pid; the incumbent entry is still fresh BUT its
    # process is DEAD. A freshness-only guard would refuse this and break the fabric.
    restart = {"0.7.0_AE_CloudOps~A": live(DEAD_PID, 5)}
    results.append(check("same serial + fresh PID after restart (incumbent DEAD)",
                         act("0.7.0_AE_CloudOps~A", restart, MY_PID)[0], "ALLOW",
                         "discriminator: incumbent process is gone"))

    results.append(check("first registration, empty liveness",
                         act("0.7.0_AE_CloudOps~A", {}, MY_PID)[0], "ALLOW"))

    stale = {"0.7.0_AE_CloudOps~A": live(DEAD_PID, server.STALE_THRESHOLD + 60)}
    results.append(check("stale incumbent under same serial",
                         act("0.7.0_AE_CloudOps~A", stale, MY_PID)[0], "ALLOW"))

    # --- AC3: THE SEVERITY RULING (CTO, 2026-07-13) --------------------------
    print("\nAC3 SEVERITY -- CROSS is HARD, SERIAL_HELD is ADVISORY:")

    # CROSS with an explicit override -> proceeds, but AUDITED.
    results.append(check("CROSS + identity_override -> OVERRIDE (proceeds, audited)",
                         act("0.8.0_AE_CloudComp", sev, MY_PID, "operator: confirmed phantom reaped")[0],
                         "OVERRIDE"))

    # SERIAL_HELD: claimed serial held by a different, live-resolving PID.
    # THE RULING: this WARNS and PROCEEDS. It must NOT block.
    held = {"0.8.0_AE_CloudComp": live(MY_PID, 2)}   # MY_PID resolves alive
    action, msg = act("0.8.0_AE_CloudComp", held, 424242)
    results.append(check("claimed serial held by a LIVE different PID -> WARN (not REFUSE)",
                         action, "WARN", "advisory: the probe cannot prove the incumbent is real"))
    results.append(check("  ...and the warning says it registered ANYWAY",
                         "REGISTERED ANYWAY" in msg, True))

    # THE RESPAWN CASE THE RULING PROTECTS -- this is the regression that a hard
    # direction-2 would have introduced: an agent dies, its MCP process LINGERS as an
    # orphan (fabric-demonstrated) or its PID is RECYCLED, and the agent respawns
    # inside the 120s window. Under a hard rule it could not re-register AT ALL and
    # would be invisible to every liveness scan -- the exact "unresponsive agent"
    # churn the SEV already cost us 9h on. It MUST proceed.
    linger = {"0.7.0_AE_CloudOps~A": live(MY_PID, 30)}  # MY_PID stands in for the lingering proc
    results.append(check("RESPAWN inside 120s w/ lingering orphan proc -> WARN (agent recovers)",
                         act("0.7.0_AE_CloudOps~A", linger, 555555)[0], "WARN",
                         "a guard that blocks recovery makes a transient failure permanent"))

    # --- AC5: MUTANT BAR -----------------------------------------------------
    # If someone flips the ruling (SERIAL_HELD -> hard refuse), the two checks above
    # go RED. This one asserts the two directions are DISTINGUISHABLE at all -- a
    # guard that collapsed them would pass every "did a conflict fire?" assertion.
    print("\nAC5 MUTANT BAR (the ruling is asserted, not merely implied):")
    cross_kind = server._identity_conflict("0.8.0_AE_CloudComp", sev, MY_PID)[0]
    held_kind = server._identity_conflict("0.8.0_AE_CloudComp", held, 424242)[0]
    distinct = (cross_kind == "CROSS" and held_kind == "SERIAL_HELD")
    print(("  PASS " if distinct else "  FAIL ")
          + f"the two directions are distinguishable (CROSS={cross_kind}, HELD={held_kind})")
    print("        a test asserting only 'a conflict fired' passes under BOTH policies")
    results.append(distinct)

    # --- AC4: the pid-liveness primitive itself ------------------------------
    print("\nAC4 _pid_alive primitive (the discriminator that saves restarts):")
    alive_ok = server._pid_alive(MY_PID) is True
    dead_ok = server._pid_alive(DEAD_PID) is False
    print(("  PASS " if alive_ok else "  FAIL ") + f"_pid_alive(self={MY_PID}) is True")
    print(("  PASS " if dead_ok else "  FAIL ") + f"_pid_alive({DEAD_PID}) is False")
    print("        NOTE: this probe answers 'does SOME process hold this PID', NOT")
    print("        'is THAT AGENT alive'. That gap IS why direction 2 is advisory.")
    results.extend([alive_ok, dead_ok])

    print("\n" + "=" * 70)
    if all(results):
        print(f"ALL {len(results)} CHECKS PASS -- hard-refuses the cross, never blocks a respawn.")
        return 0
    print(f"FAILURES: {results.count(False)} of {len(results)}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
