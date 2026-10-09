# /canonical-drive MDPF_SECHIST -- 2.0.0_SA_COO~H1, 2026-10-09 04Z (dell1)

Lease FULL. keep-driving empty_tick=on. Cron 39c58867 (10m).

## Ticks 04:14Z, 04:24Z

- UB-20261009T035455Z-cbf8: FOLDED (1.0.0_SA_CTO~DELL1 @79c8d84e65), SIGNED, RESUMED and closed by this seat at 04:2xZ.
- Read: the CTO's two-branch pre-draft `org/missions/D8/MDPF/MDPF_SECHIST/ledger/ROUND_ANALYSIS.round2.PREDRAFT.md`
  (@fc38afc55b, amendment 1 @7b888dcd22) and the CRO substrate note
  `org/tier1_exec/4.0.0_SA_CRO~DELL1/deliverables/MDPF_SECHIST_ROUND3_SUBSTRATE_NOTE_20261009.md` (@47baa5efca).

## CALL queued (WHILE WAITING, so the PASS-branch issuance is not gated at the cut)

**CALL 2 [BLOCKING at the round-3 cut; gates PASS items 1 (FWD-4/5 hop A) and 4 (FWD-9 route 2a)]: may round 3 modify
`integrations/bloomberg/pipeline/etf_daily_pull.py` for (a) the per-security gap record and the widened next-run request (FWD-5,
CRO note section 1 hop A) and (b) one added total-return level field in the history request (FWD-9 route 2a, CRO note section 2)?**

Context: Andrew's 2026-10-06 ~20:1xZ order (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261006_201xZ_BLOOMBERG_NO_MODIFY_IS_POSITIONING_AND_ETFS_VIEW_RESEARCH_OUTSIDE_OPEN_SEASON.md`,
"Unchanged": "The order still stands for the Positioning and ETFS-view files (`integrations/bloomberg/pipeline/` ...)") protects this
file. His one lift (`cooH1_ANDREW_DIRECT_20261008_175xZ_...`) covered the SH-t-4 edit only. The CTO pre-draft's PASS items 1 and 4
and amendment 1's route 2a both land in that file; neither the pre-draft nor the CRO note names the order. The site-Z
standing term on the file (site Z msg 31317) also applies: a site-Z take after the scheduled pull, under a CTO~Z half.

REC: yes for both, each as ONE build cell landing after a scheduled pull, with the never-widen pair and the site-Z take as for SH-t-1.
Why: FWD-5 and FWD-9 cannot be met anywhere else -- the pull is the only writer of the history request and the top-up window
(`etf_daily_pull.py:425-441`, `:472`); gold-only work cannot re-request a day.
If no: PASS round 3 cuts FWD-3 (entry), FWD-6 census and the Cottonwood join read only; FWD-5 hop B (gold blanks a listed day)
can still be cut, but it has no gap record to read.

## 05Z ticks (05:04Z-05:46Z)

- 05:2xZ: call b186 redundant -- Andrew lifted no-modify on `etf_daily_pull.py` 2026-10-08 ~23:0xZ (record
  `ANDREW_DIRECT_20261008_230xZ_SITEZ_AND_DELL2_OPEN_CALLS_ANSWERED.md`, lines printed); closed by the CTO (amendment 4 @6ed604ec24).
- 05:3xZ: Andrew-direct "This can go into the BBG queue system that MDPF_DEMQUE is for" -- card A released; request
  `MDPF_SECHIST-CARD-A-COT-BBG-HISTORY` @f3b5715e06; call deae closed ruled-by andrew; Q1/CTO/MSTR told (msgs 1782-1784).
- 05:4xZ: TO-READ-R2-L3 amended @08fff6f8a5 with the IAM-parity conditions (CTO msg 1818).
- 05:46Z WIDTH check (obligation 2): round-2 item 3 (`SH-t-5`) is un-parked by Andrew's release, but it has an UNMET dependency --
  the queue's quote and first paced draw (Q1) and the Cottonwood id map (234 of 4,545 ids match a table key; round-3 chain C).
  Not cut this tick; it rides the round-3 issuance as chain G, as told to Andrew.
