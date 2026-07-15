# WAVE-2 FIRST LIVE RUNS EXECUTED — the consolidation's first gold-grammar writes LANDED + VERIFIED (A_00, A_01), W-2 acceptance measured, C_04 guard exercised

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, IMPLEMENT
**serial:** 0.4.0_DS_ClientPlatform~A | **window:** 2026-07-15 ~22:45Z -> ~23:20Z
**Authorization:** Andrew-direct 'Yes start now' (~22:4xZ, recorded @ 26a4d8702 + broadcast) +
CTO dispatch 224453Z (A_00/A_01 first live runs to this lane; base-DS down; gate open at the flip).

## What landed (all parallel-by-construction; nothing serves from these prefixes)

1. **A_00.dim_account FIRST LIVE RUN — THE FIRST GOLD-GRAMMAR WRITE:**
   `s3://opal-data-assets/schwab/08335338/gold/dimensions/dim_account/date=2026-07-14/`
   data.parquet (436,690B, ETag ee08eed2653906e9c420b195afb07469, 7,139 rows x 35 cols) +
   manifest.json (the change-manifest contract surface). Tie guard held: 7,139 read ==
   7,139 CONVERTER-ATTESTED (from the converter's own conversion record — never a self-count).
   jd2 = D1 dim v1.1 (5,336 rows) merged; unbridged_advisor_accounts = 1,843 — EXACTLY the
   dictionary's measured no-fee census (25.8% @ 07-14): independent corroboration of the binary
   fee-presence law. unrecognized_status = {} (no new vendor vocabulary). Listing + behavioral
   read-back verified. Runner: `a00_runner.py` (committed; the wiring the core's main() gated on).
2. **A_01.dim_relationship FIRST LIVE RUN:** `.../dim_relationship/date=2026-07-14/` — 7,139
   accounts -> 3,475 relationships; size bound restated (7,139 <= 25,000); ssn NEVER emitted
   (read-back asserted). Runner: `a01_runner.py`.
3. **W-2 ACCEPTANCE (build plan): MEASURED.** A_00 vs legacy accounts_dimension on the xref
   overlap (5,327 accounts; denominators printed): tax_status 98.3% agree (D3 tax-from-title;
   crosstab clean — 88 reclassify), account_is_open 99.7% (status-fact), address passthrough
   99.9%/99.8%, roles diverge on the D6 axis exactly as pre-declared (architect 53.1%,
   implementor 93.2%, consultant 38.6%, local_ops 85.2%, additional_advisor 4.8% — facts-from-dim
   vs legacy txn archaeology; the same axis the dry-fit measured). EVERY divergence carries a
   named design class.
4. **C_04.recon_guard FIRST EXERCISE (07-13 -> 07-14 pair):** 5,999 position-bearing accounts
   checked, 32 flagged (0.53%), largest |residual| $1.66M; thresholds explicit + echoed per row
   (abs_floor 1000 / bmv_band 0.05); flag table in session scratchpad — the guard has NO data
   write path by construction. Day 1 of the plan's 5-day flag-rate sequence.

## Findings (named, routed)

- **F-SSN: `ssn_tin_number` is ALL-BLANK in monolith fact_acc (0/7,139)** -> A_01's T1 identity
  edge cannot fire; households are currently ADDRESS-ONLY linked (census: address 3,664,
  singleton 3,475, ssn 0). DISCRIMINATION NEEDED (one bronze read): vendor-masked-at-source
  (fine, named) vs converter drop (a Rule-17 passthrough violation). Routed to CTO + 0.6.2.
- **F-JD1: no `fact_allocation_account_map` at the scope root** — jd1 vintage stamp ABSENT
  (stated in the manifest, not silent). The smartx map may land under a different prefix or is
  feed-9-pending; one listing/ruling names it.
- Ruff blocked one unused import (fixed at source, zero overrides).

## Compiler Tools

| tool | run | result |
|---|---|---|
| comp-pipescript postdeps | a00 (+ D_04/D_00f earlier) | PASS-EMPTY (no declared post-deps) |
| commit-gate.sh | 3 runs (1 block fixed) | PASS |
| aws listings (rail-marked per call) | input existence verification (Rule 22a APPLIED truth) | fact_acc/dims/jd2/gold-empty all verified pre-run |

## Next Steps

1. Evidence message to CTO (this window's runs) — sent with this commit.
2. [CTO/0.6.2] F-SSN discrimination; [CTO] F-JD1 prefix naming.
3. Wave-3 C-port work proceeds per Andrew's start-now: M1/M6 spec-cell drafts + C_03 authoring
   next in lane (queued behind this dispatch per CTO pace order).
4. Nightly cadence: tomorrow's fact_acc partition (2026-07-15) makes run 2 — first_seen
   continuity + snapshot-diff manifest get their first real exercise.
