# /self-drive D2 & D3 — tick 8 (2026-08-28 00:42Z) — state: ARMED

Covers tick 8 (tick 7 logged @4c56c56f78). Cadence 30m (:07/:37), cron 17fc9648. Carrier: org/XXX.md
CTO row @310a20e38c. Paired: /drive D2 & D3 @ 2.0.0_SA_COO (+15m) — COO seat closed ~00:4xZ (77147),
its successor re-arms on the same carrier; this seat is the live reader in the gap.

## Scope (register-read)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete; D3 1: 0 complete). Open TOs
27 (D2 20, D3 7). Flags: none. Device LAPTOP.

## Calls pitched

None — zero open calls in scope.

## Verdicts / rulings since tick 7

- **Ledger row 9 (own-lane ruling, GO-class):** campaign date 1 (2024-07-08) HARD-STOP rc=2 at 00:12Z
  = IAM AccessDenied on assumed-role/bd-49f-auto-login-role/i-0fa1846f04ed7e337 (COO 77106). RULED
  WRONG HOST (77108): the vehicle sent the floor's own document to the BD auto-login box (DRIVER.py:61)
  instead of the runner the production floor dispatches to (advi_49f_floor.tf:52, i-01003b035d2988dfb,
  bd-exporter-ec2-role carrying advi-49f-chain-access). Fix = one constant; NO IAM change anywhere.
  Row 9 committed via COO's @415e07a64a (shared tree carried my unstaged row; `git log -S` attributes).
  **Consumed EXECUTED** at COO (77147): re-point @c143be5f10, date 1 re-fired 00:33:45Z.
- **77132 (~L) -> 77133 (CTO):** ~L corroborated on a second plane (16 invocations, 15 on the runner;
  the only login-box send ever was tonight's; CloudTrail 0 IAM writes on the role since 00:00Z) and
  caught the destructive half neither ruling covered — the runner is SHARED, so the driver's halt is
  now conditional on having started the host. RULED: StartedByDispatcher stays OMITTED on campaign
  sends; my 77108 3(b) clause SUPERSEDED. V14-2 void, re-exercise on the runner sequenced by COO after
  date 1's oracle read and before V14-4c(e) is treated as final.

## Campaign state

Inputs (1) P14-STAMP @f3a51ab26e and (2) c00-SIGNING @8e72ca42b6 COMPLETE; (3) date-1 re-drive
RUNNING since 00:33:45Z on the correct host; outcome NOT yet reported at this tick (newest inbox item
77147 at 00:39Z). Campaign-start = ~L's V14-4c(e) judgment; PROVISIONAL until V14-2 re-runs.

## Driver acts since tick 7

Session close log @b41d5e5883; HANDOFF @a68ce32508 (this seat reinstantiates on Andrew's word).

## Completion test

NOT DONE — 1 of 10 complete. All 10 REACHABLE.

## RESERVED at Andrew

None open.

state: ARMED

## Compiler Tools

- `python .tools/directives-check.py --json` (scope/TOs/flags) · ledger tail read · inbox listing · `date -u`.
