# SELF-DRIVE laptop directives -- tick 71 (2026-09-27 ~22:48Z to ~23:18Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_LAPTOP_DIRECTIVES_IRPT.md`
@`ce6aa15a17`. **Covers:** the ticks since the ticks 68-70 log (@`0f4ceca159`). **State: ARMED.** Written early on a
substantive delta: a served deploy failed and was rolled back.

## The generate + resident release is CLOSED (~P @`03e70a4393`)

- Generate `ykJltfTd`; the resident runs `fe64236bbb-st` since 22:46:12Z (running root read back).
- ~Y verified the served release (@`43083e588f`): Overview ACCEPTED; Static READY; a foreign row goes ATTENTION.

## A failed served deploy, rolled back

- **Signed:** the irpt-status rebuild (template status dates), CTO @`77f49e8b3d`, CRO @`c20fe9034a`, packet
  `6b35dca8`.
- **Served** at 23:00:28Z as `HyEyoJ67`.
- **The defect (~Y 102201):** HEAD `ops/entry.py` calls `served.render_ports_from_env()`, but the packaged
  `_authz/served.py` (`41fbd6b5`) lacks it. So every status, history and sections read raises AttributeError at cold
  start, for all tenants. It was caught with 0 invocations.
- **Ruled (CTO 102202, 23:11Z):** roll back NOW per the signed rollback; window 19 holds until verified; the rebuild
  is a new packet with HEAD `served.py` (`3a2cdba2`), a built-zip import smoke and an `_authz` census.
- **Rolled back:** `bMMJ/bQ+5` live at 23:15:47Z, read by this seat from `lambda get-function`. ~P proved a cold-start
  invoke answers (102209) and closed the ledger as a failed deploy, rolled back.
- **This seat's miss, stated:** my half checked that only three members changed. It did not check that the new
  entry.py's dependencies were in the package. The census of what changed is not a proof that what ships imports. The
  import smoke on the BUILT artifact is now a condition of every packet this seat signs for a Lambda code move.

## Other halves this tick

- Window 19 (K10 + K8 re-run, `35c9083d`): CTO @`266bf56cb5`, CRO @`027eb6137a`. K8 runs now; K10 waits for the
  rebuild.

## Capacity

C: has 9.2 GB free. Round 9 has 0 worker slots until the purge (~05:00Z), unless Andrew frees Downloads.

## Open calls at Andrew

1. BLOCKING: remove the ~5.7 GB Downloads scratch?
2. CARRIED: Schwab's registration-code list (UIC-16).

## Completion test

NOT DONE: 0 of 2 IRPT projects are complete (both `active`). D10 is UNMEASURABLE (no members).

state: ARMED
