# AMGT_CORPUS -- L5 decomposition v48.0 -- ROUND 48 (the round-47 analysis's enrichment list: the served read that grades FWD-12 and FWD-20, the Thesis payload census by key, the FactSet label read)

**Issuer:** `2.0.0_SA_COO~C1` (dell1), 2026-10-11 ~21:0xZ.

**Source:** `1.0.0_SA_CTO~DELL1` round-47 analysis `ledger/ROUND_ANALYSIS.round47.md` (msg 4109), over `3.0.0_SA_CVO` slug msg 4107 (ADJUDICATION_v62 @4994bb7abd).
REALIZED 20 of 22; open FWD-12 and FWD-20 (both BUILT, not served). PRD v0.11 (ADDENDUM F, the FactSet label DEC, D1-S6). Round 47's decomposition kept as
`AMGT_CORPUS_DECOMP.round47.md`.

## 0. What this round IS

Every cell is the issuer's own READ or a carried act; no worker order is cut (the round's work is measurement, and its one act, the redeploy, is AMGT_RESAPP's).

| # | item (analysis s.3) | cell | executor | risk |
|---|---|---|---|---|
| 1 | the SERVED read over every served name on the RENDERED page, after AMGT_RESAPP round 98's /13 redeploy: unmapped 0 over FIGURE rows; 0 raw codes as labels; 0 cells past their format; per name the class counts and the per-row source (Bloomberg / team / FactSet via team / why); the master names' rows with Bloomberg or the template why. Grades FWD-12 and FWD-20 and closes D1-S7 | `CRPS-ax-1` | the issuer's read: `checks/round47/aw4_capture.py` before and after, `aw4_compare.py`, `aw6_rendered_census.cjs` on the live payloads, a `/ui-walk` of one name per class on the DEV page | LOCAL (read) |
| 2 | the Thesis payload census BY KEY (the response is about 1 MB before /13): bytes per top-level and per `model` key, over the 95 names, read only, so any remedy is chosen on measurement | `CRPS-ax-2` | the issuer's read on the live capture (`checks/round48/ax2_payload_census.py`) | LOCAL (read) |
| 3 | the 394 "FactSet line" rows: one read of whether the team's other workbooks label any of the 50 FactSet codes unambiguously, raising the measured share; no inference | `CRPS-ax-3` | the issuer's read over the stored own workbooks and the SharePoint templates (`checks/round48/ax3_label_read.py`) | LOCAL (read) |
| 4 | the carried act: the /13 redeploy of `opal-amgt-scoped-api` from the merged pin, AMGT_RESAPP round 98's first cell, under `NEVER_WIDEN_ROUND47_AW4_*` (COO half @56f0d97d08, CTO half SIGNED with ADDENDUM 1) | `CRPS-ax-4` (carried; not this issuance's act) | `2.0.0_SA_COO~R1` / `0.7.0_AE_CloudOps~RA1` | SERVED |

**Chains:** `ax-4 -> ax-1`; `ax-2`, `ax-3` independent (read now). `fanout: 0 of 0 worker chains (no order is cut; cap 8)`.

## 1. The reads (what each prints)

- **ax-1** prints, over the live function after the redeploy: the capture's function CodeSha256 and LastModified; per name the class, rows, FIGURE / HEADING / CONTROL and the
  FIGURE rows by source (Bloomberg / team / FactSet via team / why / refused / unmapped); the totals; raw codes visible; cells past their format; the master names' why count; the
  `aw4_compare` line (`team_sheet` equal to the stored /13 field on 95 of 95, every other field equal, growth within the team_sheet delta, the max under 6 MB with its margin); and
  one rendered walk per class (TSM US master, SAN FP and IMB LN own_new, ROG SW own_model, CLX US the D1-S7 name).
- **ax-2** prints, per key, the bytes it carries over the 95 captured payloads (min, median, max, total, the share of the response), at the top level and inside `model`, ranked.
- **ax-3** prints, per FactSet code with no measured label, the distinct labels any stored own workbook or template assigns it by the round-47 rule (column-B metric name; single-row
  pass-through), and whether they agree across workbooks; a code with exactly ONE distinct label across workbooks and no conflict is a candidate; a code with two or more stays "FactSet line".

## 2. Not in round 48

The 10 files in 6 unresolved folders; vocabulary growth; the PROD release of the portal (Andrew's `e7f2`); any change to the 13:00Z fire.
