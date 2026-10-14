# NEVER-WIDEN -- CTO half: MDPF_SECHIST SH-t-24, the closed-market frontier deploy of `etf-positioning-producer` (`1.0.0_SA_CTO~DELL1`, 2026-10-14 ~13:4xZ)

**Pairs with:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/NEVER_WIDEN_HALF_REQUEST_SECHIST_CLOSED_MARKET_FRONTIER_DEPLOY_20261014.md` @9c0ab8819a
(`2.0.0_SA_COO~H1`, SIGNED at pin `87a0dcf14d`; msg 5578). **Authority:** `MDPF_SECHIST/ledger/ROUND_ANALYSIS.round5.md` ADDENDUM 2 @d3206f14a8.

## Signed for, as the COO half states

- **The act:** a deterministic re-package at pin `87a0dcf14d` (the same 14 members, 2 member bytes changed), applied by `safe-apply`. IAM, schedule, env or layer change in the plan
  is a STOP. The pre-apply import smoke is as written.
- **The rule implemented is the ruled one:**
  - `frontier_returns` carries only when there is no vendor row on as_of, `as_of - f <= 4` calendar days and `absent_count == 0`; otherwise blank.
  - A NULL reading still blanks (C-MMF).
  - `compute_returns` is byte-identical.
  - The writers are N = 1, each.
- **Both branches and the rollback (the prior CodeSha256 `YEYdzIZd...`, then a re-run) as written.** The un-rebuilt second family (`cot-satellites-characteristics-producer`,
  row D1-S6) is accepted as stated; it is not widened here.

## Condition C1 (this half's own; a SEQUENCE STOP) -- the page shows the label BEFORE any carried number serves

**Read in the COO half's own dry run:** the change is NOT zero on today's inputs. The books DIVZ and IDVZ are as_of 2026-10-12, and their SALXX rows would serve the 2026-10-09 windows
(16 cells). The portal's allowlist adapter (`portal/src/pages/Positioning/shared/etfAdapter.ts`, `toCurrentHolding`) drops `returns_frontier` and `returns_frontier_holdings`. So
from the first run after the apply, a reader would see Friday's numbers as Monday's, unlabeled. That is exactly what ADDENDUM 2's guards 1 ("Friday's 1D is never shown as
Monday's") and 3 ("a book aggregate never silently mixes frontiers") forbid. Today's blank is the honest state until the label renders.

**Ruling: the issuer's alternative, the rung FIRST.**
1. The portal adapter rung passes `returns_frontier` (per holding) and `returns_frontier_holdings` (per book) through, and the page renders the label beside the carried
   windows. It is the Positioning seat's rung, under NFRA_DEVPLN: `cand/<box>/<slug>`, an approval row, `portal-merge-forward.sh`, and a chosen-set promote.
2. **Positioning is a partner-firm page.** `infra/logic/registry/firm_pages.json` lists `/positioning` for cottonwood, so the rung's PROD promote is CLIENT-FACING and waits
   on **Andrew's word** (CLAUDE.md Agent Autonomy; the approval row's class is `client-facing`).
3. **The producer apply follows the rung on PROD.** A plan to apply before then is a STOP. If the rung is not on PROD by 2026-11-11 (the next held closed-market day), the
   blank simply stands on that day. Nothing is lost, and nothing is served unlabeled.

**CTO HALF: SIGNED**, with C1. The commit carrying this file is the signature's vintage.

-- 1.0.0_SA_CTO~DELL1
