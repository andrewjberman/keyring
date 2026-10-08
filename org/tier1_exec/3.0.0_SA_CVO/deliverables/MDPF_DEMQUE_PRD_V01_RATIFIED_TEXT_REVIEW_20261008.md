# MDPF_DEMQUE PRD v0.1 -- ratified-text half review (L4-R)

**Reviewer:** `3.0.0_SA_CVO` (dell1). **Object:** `org/missions/D8/MDPF/MDPF_DEMQUE/prd/MDPF_DEMQUE_PRD.md` @ac05f0256e, half_hash
`1cb624b99915` (msgs 1221, 1222). **Pins read:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_BACKFILL_DEMAND_QUEUE_20261008.md`
and `ANDREW_DIRECT_20261008_224xZ_BACKFILL_QUEUE_ENDPOINT_CONFIRMED_PRIORITY_BBG_YAHOO_ONLY.md`, both @e4f75dfd21.
**Verdict: SIGN.** Two findings in CONTRACTS / PRIOR ART; none touches the ENDPOINT bytes. F1 must land before L5 cuts the reserve.

## Checks

| Check | Result | Evidence |
|---|---|---|
| ENDPOINT verbatim vs the ratified pin | PASS | Line diff of the fenced FWD-1..9 block, PRD against the endpoint file: IDENTICAL. |
| Ratification | PASS | Record VERBATIM: "1.) Yes." |
| Andrew's operative words carried | PASS | Priority order (production incl. ETF Positioning; current clients + onboarding; rival funds on BBG in small daily jobs; research; former clients last) -> C-PRIORITY, word for word. "Only BBG and Yahoo for now" -> C-METER. Cells -> C-CELL. Gentle Yahoo, retroactive corporate actions -> C-YAHOO, C-PRICES. Unmappable process -> C-IDENTITY. |
| No annotation inside the outcome text | PASS | Annotation sits in SOURCE lines and the "Settled by Andrew" paragraph outside the fenced block; no seat serial inside it. |
| No FWD is a wait | PASS | FWD-3 and FWD-8 are "shown on purpose"; FWD-1 is one real security traced; FWD-6 is APPLIED (a rule in force). FWD-7's "multi-day run read" is the minimum that exercises stop-and-resume, not an organic wait. |
| STARTING STATE citations | PASS | Bytes printed: `bbg_budget.py:5-14` (ceiling - reserve - spent), `:95-99` (limit = ceiling - reserve); `bbg_budget.json` 150000 / 30000 / ACWI 2198 / IWM 1979; `lambda_function_v2.py:6-9` (batches of 50), `:46` (`BATCH_DELAY = 2`); line counts 740 / 838 / 1,606 match; the Yahoo caller files and the 10-05 reconstruction exist. |
| C-HOMES | PASS | Builder output cited for both ledger addresses; the `yahoo` refusal is recorded as a registry gap, not hand-typed around. |
| CONTRACTS vs counterparts | PASS with F1 | C-PRODUCERS keeps MDPF_SECHIST's pull and ADVI_COTBKF's need list as inputs; no producer absorbed. |

## Findings (for `1.0.0_SA_CTO~DELL1`)

- **F1 (C-RESERVE, substantive). The reserve is seeded with the capacity figure.** C-RESERVE: "the reserve starts from the measured floor
  (2.92M BQL cells on 2026-10-05)". The reconstruction it cites (`BBG_CELL_TRACKING_RECONSTRUCTION_20261005_BLOCK_20261008.md:98-99`) says
  that figure is a floor on the CAPACITY ("The 2026-10-05 block gives a floor: about 183,000 BQL holdings rows, 2.9 million returned
  cells ... and possibly more"), i.e. the point at which BQL refused. It is not the production load. Seeding the reserve with it sets
  reserve ~= ceiling: the BQL backfill allowance (ceiling - reserve - spent) is about zero, so FWD-4's quotes have no finish date, and
  FWD-9's tier 3 (rival funds on BQL) never draws. `bbg_budget.json` has the right shape: ceiling 150,000, reserve 30,000, with the
  reserve a fraction of the ceiling. Ask: seed the CEILING from the 2.92M floor, and seed the RESERVE from production's own measured
  daily BQL draw (open item 1 measures part of it), plus a stated margin.
- **F2 (PRIOR ART). A cited file does not exist.** `org/tier0_utility/0.0.3_BG_BBGTerminal/deliverables/MDPF_SECHIST_PACER_20261007.md`
  is in no tree: `git ls-files` is empty and `git log --all` on the path is empty. Cite the pacer by its real path, or drop the line.

-- 3.0.0_SA_CVO
