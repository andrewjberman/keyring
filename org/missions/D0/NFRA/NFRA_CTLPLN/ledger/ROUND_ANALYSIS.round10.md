# NFRA_CTLPLN -- ROUND ANALYSIS (L10), round 10, closed 2026-10-12 ~13:3xZ

Author `1.0.0_SA_CTO` (laptop). Slug: `3.0.0_SA_CVO~L` msg 108557 on `2.0.0_SA_COO~C` msg 108553; compile ADJUDICATION_v12 +
REMEDIATION_v4 @36e22a0564. Previous: `ROUND_ANALYSIS.round9.md` @4f1409093d. PRD v0.25.

## 1. What the slug and the drain carry, and the rulings

| item | read | ruling |
|---|---|---|
| `round-close-check --round 10` | 32 orders in scope, 30 complete, proof_bad 0, 2 of 2 judgments graded, MAY-CLOSE; every order of the project terminal (104 complete, 4 withdrawn, 1 cancelled, 1 superseded) | round 10 is finished on this box |
| A10 (CT-z-?): the portal carrier | gitlink -> portal 53506d4903 @905199213c; firm tests 33 of 33 on origin/DEV | accepted; the carrier is on DEV with the registry notes; PROD is Andrew's push (client-facing) |
| CT-z-1 thread-trace `--order` | merged @ecc0273a1c; round 9's TO-CT-y-2 prints hops 4 of 5 (HOP 5 absent because the order carries no judgment criterion) | accepted; W73-S1 DISMISSED on that reading |
| A4 the 12-message matrix | acked=10; 0dce and d5e7 wait on dell2 seats (at the weekly limit until re-seated 13:1xZ) | carried to round 11 as the two remaining acks |
| W73-S2 (find_orders globs the worktree, `.tools/thread-trace.py:236`) | GRADUATED, owner COO~C; the fix is to read refs | round-11 hygiene cell |
| S9113 (S9111's owner named), S9114 (read the order set from git) | noted, gate nothing | stand as noted |
| W61-S1, S9112 | ARMED at Andrew | unchanged; cited acts on the self-drive list |

## 2. Grades (delta from round 9)

**FWD-28 REALIZED.** DONE WHEN (PRD v0.25): a partner-firm token on an internal-only route answers 403 and an internal token 200;
on a partner-page route an admitted firm answers 200 and another firm 403 -- exercised under CT-u-7 and CT-w-3 (both pairs
applied and read back; 39 routes internal-only, 2 by firm from `firm_pages.json`), the log no longer carries credentials
(CT-w-10), and the single source now also generates the portal's `FIRM_ALLOWED_PATHS` (on DEV, 33 of 33 firm tests). The
PROD push of that one portal file is Andrew's act and changes nothing a partner sees. FWD-3/FWD-22 advanced (10 of 12
matrix acks). FWD-1: the Dell leg and the thread trace exist; the end-to-end thread stays the E1 outcome to prove. FWD-27:
unchanged, gated on Andrew.

## 3. ENRICHMENT LIST for round 11 (ONE issuance, `2.0.0_SA_COO~C`)

- A4's last two acks (0dce, d5e7) now that dell2's lanes are re-seated; FWD-3/22 grade on 12 of 12.
- W73-S2: `thread-trace.py` `find_orders` reads refs, not the worktree (one cell, selftest).
- E1 end to end; E2/E3/E5-E8 carried with a stated reason each (three rounds running -- the next analysis expects at least
  one of E2, E3, E5 cut or a reason why not).
- E9 FWD-27 stays gated on Andrew's keys and elevated lines.

## 4. Owed outside the project

Andrew: W61-S1's elevated line; S9112's purge + refresh-token invalidation; FWD-27's keys and per-box elevated runs; the PROD
push of the portal carrier (`firmAccess.ts`, 53506d4903).
