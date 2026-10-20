# DELL1 self-drive box -- ticks 192-193, 2026-10-20 ~14:48-15:18Z (delta: Andrew's FIDUPL drive order, PRD v0.4.5, sign-in fork)

**archetype:** COORDINATE
**state:** ARMED (cron 520f0ff2, record ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md @fa59eb8dec). A second loop is armed
beside it, the FIDUPL drive loop (cron 19710f50, every 15m), on Andrew's word at this terminal.

## Inbox and open calls
- 0 unread at 15:18Z. Acked since tick 191: 8655, 8661, 8665, 8668, 8672.
- open_calls.json: 158 rows, 2 OPEN, both acts only Andrew can do.

## Andrew-direct at this terminal (~14:55Z), recorded by 4.0.0_SA_CRO~FIDELITY @b329e1c5f3
- (1) A scheduled daily download of each fact table by G number into `opal-data-assets/fidelity/`, split to the firms.
- (2) The backfill of each G number as far back as possible.
- Drive aggressively, and name every gap he can close now.

## Acts and rulings
- **PRD v0.4.5** @e4bb46835e: every G number goes to its own firm and lands once per firm; the backfill goes as far back as possible
  per G, with each stop named. The PRD is still ADMITTED.
- **Round 2 runs in parallel with FU-x-1** (msgs 8663, 8664). P1 issued five build orders at 15:03Z (4ca02b2119, DECOMP_R2):
  FR-s-1 to FR-s-5.
- **FIRM rows** for keilfinancial, abidingwealth, lighthousewealth and vmwealth, @473d23cfc6 (CRO 8665). One advisor-named G number
  is unattributed and stays under alongside.
- **The sign-in now fails on the server side** (P1 8668): after Next, POST `/auth/api/redirect-info` returns 400 "System
  unavailable". The fingerprint is fixed and no SMS was sent. This is a design fork, routed to CRO~FIDELITY with three paths: missing
  headers or telemetry, non-datacenter egress, or a session Andrew seeds by hand. Rule on landing.
- **The per-G list home** (P1 8672): ruled Secrets Manager `fidelity/alongside/perg-list`, not SSM. SSM has no canon name; the
  secret grammar grades CONFORMANT (msgs 8673, 8674).

## Scope state
- **NFRA_FIDUPL:** 9 of 10 round-1 orders complete; FU-x-1 is blocked at redirect-info. Round 2: 5 orders pending. 0 objects under
  `fidelity/`. The 3 fetch rules are DISABLED.
- **ADVI_COTBOOKS:** L2, waiting on Andrew.
- **Completion test:** NOT DONE.

## ACTS ONLY ANDREW CAN DO
- **ea86:** confirm ADVI_COTBOOKS v2's DONE WHEN lines (L2).
- **89c9:** the SOC2_MSLOGS re-derive (his MFA).
- **For FIDUPL, his login and his captures:**
  - confirm the stored password signs in by hand;
  - possibly one sign-in by hand to seed a session;
  - the Export Custom step-2 column order for the six files;
  - a capture of an on-demand date-range export and of the Historical Prices and Positions Export;
  - the firm of the advisor-named G number.

## Compiler Tools
- `prd-signoff.py status`.
- `describe-instances`.
- `list-objects-v2`.
- `events list-rules`.
