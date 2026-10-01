# SELF-DRIVE AMGT_FRIDAY -- tick 8 -- 1.0.0_SA_CTO~Z -- 2026-10-01 09:4xZ to 10:4xZ
**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_040xZ_SELF_DRIVE_60M_AMGT_FOUR_PLUS_ETFS_RIVALS_ARM_ON_CRO_BRIEF.md`.
**Previous log:** tick 7 @88c9702c22.

**state: ARMED**

## Tick header (10:45Z)

- **Inbox:** 0 unread. 27732-27735, 27758 and 27759 were acted on and acked.
- **Open NEVER-2 ledgers in scope:** `amgt-resapp-r56-af6-price-cutover` (the 11:00Z fire). ah-2's ledger is CLOSED.
- **Completion test:** NOT DONE. 0 of 5 are `complete`; 5 REACHABLE.

## The Friday demo surface (O1-O7)

| outcome | state | evidence |
|---|---|---|
| O1 chatter bubbles | **PROVEN live**, names on every label (0 raw keys) | DSGN r17 acceptance walk @4b0135afec; RESAPP ah-2 LIVE 09:48:26Z (CodeSha256 `g9H0TW2g...`) |
| O2 price bars | **PROVEN live** (32 bars, longest first, signed); one-decimal print landing (AV-i-1 proof eaf5b2d86d) | @4b0135afec; CONTRACT amendment 3 @b9d096f6dd |
| O3 card-family headers | MET (headerchrome 3/3) | DSGN v18 |
| O4 served-day header | served; the header chatter line moves to the monthly route (DSGN r18) | msg to COO~D 10:32Z |
| O5 Model tab | **COMPLETE** (rounds 28-31) | CORPUS v36 |
| O6 news depth | sa backfill running; ft in-tab backfill authorised | HARVST |
| O7 scheduled producers | af-6 fires at 11:00Z | af-6 ledger |

**The Friday path's remaining dependency outside the page:** site-Z portal DEV (788afb2e and later) is 30+ commits ahead
of origin DEV (2879d65b). The promote reads origin, so the push is MSTR's act on Andrew's word (put to MSTR~Z at 10:10Z).

## Acts

| act | commit / receipt |
|---|---|
| ETFS_RIVALS RIV-d-4 CTO half: keys 1,2,3,5-8 SIGNED; key 4 REFUSED (the floor over 5 issuer funds would fail the home funds, BASG and SCHY); the GQGU BQL request withheld. COO~RV amended to match (e7b94e2fe8). | 44eb66268e |
| 5174 moved to DEV 788afb2e (3535bb38) for the DSGN r17 acceptance walk | msg 10:10Z |
| CORPUS round 30 analysis (round 31 = one wording cell) | 500c40ecb2 |
| CONTRACT amendment 3: one-decimal display, the whole value in a data attribute | b9d096f6dd |
| CORPUS round 31 analysis: the Friday face COMPLETE; the header chatter line routed to DSGN | 85df450e8d |
| The portal DEV push before the promote placed at MSTR~Z for Andrew | msg 10:10Z |

## Acts only Andrew can do (cited)

Unchanged from tick 7 (8 items), plus a sharpened item 8: **the portal DEV push of site Z to origin** before the
promote (LD-0367/0368), with the CLOUD push that carries the walker lease.

## Compiler Tools

| tool | result |
|---|---|
| `git ls-remote` vs local portal DEV | 30 commits unpushed; measured, not assumed |
| `guardrails.py:154` read | `identity_coverage` grades every fund; this drove the key-4 refusal |
| served_delta_after.json per-fund read | matches the COO half's table; home funds resolved 0.0 |
