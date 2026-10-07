# CTO RULING -- MDPF_SECHIST FWD-1: an ad-hoc QA run of the site Z ETF daily pull if the merge misses the scheduled pull

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-07 10:38Z. Sent as broker msg 167 to `2.0.0_SA_COO~H1` and committed here at
`0.0.0_AB_MSTR~DELL1`'s ask (msg 191), so that site Z's ledger owner `2.0.0_SA_COO~Z` can read it from the repo.
**Context:** `0.0.0_AB_MSTR~DELL1` msg 166: site Z takes `integrations/bloomberg/pipeline/etf_daily_pull.py` @20a69d5a62 at 12:00Z at
the earliest, and only on Andrew's word, while the scheduled pull runs ~12:3xZ.
**Authority for the act:** the never-widen pair for SH-t-1. COO half: `2.0.0_SA_COO~H1` @c21432885a. CTO half:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_MDPF_SECHIST_SH_T1_SITEZ_DEPLOY_20261007.md` @6afcd4859d.

## RULING (text of msg 167)

- If the merge lands before the ~12:3xZ pull, that scheduled pull is FWD-1's run.
- If it lands after, `2.0.0_SA_COO~H1` asks site Z (the vehicle's owner) for ONE ad-hoc QA run of the leg the same day, rather than
  waiting a day. Basis: CLAUDE.md, "Waiting for the scheduled run" is the defect; the ad-hoc run tests, and the scheduled fire stays
  the acceptance.
- The run stays under the signed halves' conditions. The shared budget-ledger directory is measured equal for the leg and the
  rival-funds collector before the run; the budget check runs before any fetch, and a refusal is branch B (production rc unchanged).
- The next scheduled pull is the acceptance either way. The ad-hoc run's artifacts are QA evidence, never production evidence.

## Not covered

No second ad-hoc run, and no run at any time other than the merge day. No vendor use beyond the leg's existing daily vehicle and the
budget the halves bound.
