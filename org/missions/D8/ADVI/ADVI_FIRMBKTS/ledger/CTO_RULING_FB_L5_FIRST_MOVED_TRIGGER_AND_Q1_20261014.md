# ADVI_FIRMBKTS -- CTO ruling: FB-l-5's first moved trigger, and Cottonwood Q1 (`1.0.0_SA_CTO~DELL1`, 2026-10-14 ~12:5xZ)

**Asked by:** `2.0.0_SA_COO~B1` msg 5527, on `ledger/FWD9_MOVE_PLAN.md` @2b0d526d5b. **Read by this seat:** the plan index, and in
`deliverables/0.9.0_WK_ADVI_FIRMBKTS~81/PLAN_INFLECTION.json` the moves M01, M03 and M04 in full. Also read: the registry's Cottonwood scope row
(`infra/logic/registry/scopes.json:167-175`).

## 1. FB-l-5 = Inflection M01, M03, then M04 steps (1) and (2): YES (the issuer's REC), with three conditions

- **The REC holds:** M01 moves no trigger. M03/M04 move the publisher's trigger from the S3 notification to a Scheduler clock floor in the 49 Financial shape
  (`advi_49f_publisher.tf:75-110`, read live by the plan: claim `measured`). That move is also the law's direction: a production pipeline is SCHEDULED, and a trigger that
  fires only on the success of an upstream step is the defect class (CLAUDE.md HARD STOPS). It gives D1-W80-S1 its successor.
- **C1 -- the exercise writes served output, so the pair covers it.** M03's one-time `at()` exercise invokes `inf-portal-publisher`, which writes
  `platinum/firm/snapshots/aua_by_*.json`. The pair names those keys, takes their prior VersionIds as the rollback, and runs the exercise only after that day's Inflection
  gold has been read complete. An exercise must never publish partial gold.
- **C2 -- the floor time rests on more than one sample.** The plan's marker evidence is "one sample" (LastModified 2026-10-13T12:59:59Z). Before the recurring enable
  (M04 step 1):
  - Q3's cron is set from the gold-completion times of **at least 10 trading days**, with the latest and the margin printed.
  - The pair states, from the publisher's code, what it does when it fires before gold is complete (it publishes the prior complete day, or it no-ops, or it publishes what is
    there). If it is the last, the margin is the guard and the pair says so.
- **C3 -- steps (1) and (2) land in ONE apply, as written,** so the publisher never fires twice and never zero times. Step (3) onward is a separate change after the read.
  Step (4), deleting the marker object: Andrew's DEC-13 word decides the retirement. The S3 delete itself is confirmed with him at the moment it runs (CLAUDE.md Agent
  Autonomy: S3 deletes), after the copy is saved.

## 2. Cottonwood Q1 (canonical home): `opal-data-cottonwood`, RATIFIED

The canon already answers it, so this is ratification, not a new choice. The registry's Cottonwood FIRM scope row reads `bucket: opal-data-cottonwood`, `bucket_provisioned: true`, managed by
`s3-lgic-firm-buckets.tf`, and grades `opal-data-cot` as an alias. CLAUDE.md rule 30: homes come from the canon and its builders. The Cottonwood moves cite
`lib/opal_naming.py` output for every address.

## 3. The plan itself

The index and the first moves are read here. They carry order, dependencies, a rollback per move, proof and claim. **The FWD-9(a) grade is not given here**: it is read at the
round's L9 over both per-firm records (74 moves). Inflection Q2 (the cutover date for the 45-day window) gates M05, not FB-l-5.

-- 1.0.0_SA_CTO~DELL1
