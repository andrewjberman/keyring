# Deploy Completion Record
**Date opened:** 2026-08-27T15:38:58.998550+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260827T154430Z
**Deploy:** ANDREW-DIRECT 2026-08-27: ad-hoc rerun of the MDPF path for cottonwood today -- close the 24h mirror floor by hand so 08-26 reaches MDPF today instead of tomorrow. Writes a CLIENT-FACING served artifact.
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | opal-assets-ingest-mirror {firm:cot} | assets bronze holdings/_complete/2026-08-26.json goes 404 -> 200 on head-object (live), plus a BEFORE/AFTER diff naming any OTHER day restated | opal-assets-ingest-mirror {firm:cot} StatusCode=200 FunctionError=None; self-report 695 enumerated / 682 already_landed / 13 written / 0 missing / 0 failed. VERIFIED ON LIVE OBJECTS, not rc=0: head-object blackdiamond/cottonwood/bronze/holdings/_complete/2026-08-26.json went 404 -> 200, LastModified 2026-08-27T15:39:29Z, 233 B. ROLLING-WINDOW RESTATEMENT WATCH (CTO's ask) -- ANSWER: NOTHING SETTLED WAS RESTATED. BEFORE/AFTER over holdings/_complete: 47 -> 48 objects, NEW=[2026-08-26.json] only, REMOVED=none, ETag CHANGED=NONE, LastModified-moved-with-same-ETag=NONE. Wider sweep over all 3,633 objects under blackdiamond/cottonwood/ found 29 written at >=15:39:00Z, and EVERY dated write is either 2026-08-26 (SNAPSHOT tables: holdings, allocations, unrealized, account_attributes -- D-1 as designed) or 2026-08-27 (PERIOD tables: transactions, realized -- D-0 as designed). No pre-08-26 key was touched. The 08-27 keys are NOT a restatement; they are the documented snapshot-vs-period split (cot_bronze_ingest.py SNAPSHOT_TABLES). | CLOSED 20260827T154045Z |
| L2 | activation | opal-assets-silver-blackdiamond {mode:sweep} | silver fact_holdings_s2/date=2026-08-26/ AND fact_allocations_s2/date=2026-08-26/ exist on live S3 | SATISFIED WITHOUT A SEPARATE INVOKE -- opal-assets-ingest-mirror produces silver itself as part of its own run, so opal-assets-silver-blackdiamond {mode:sweep} was NOT fired. Live S3 verify: blackdiamond/cottonwood/silver/fact_holdings_s2/ = 60 partitions, newest date=2026-08-26 (data.parquet 4,565 B, written 15:39:37Z); fact_allocations_s2/ = 111 partitions, newest date=2026-08-26 (4,612 B, 15:39:38Z). Both required partitions PRESENT. The wider sweep also shows fact_holdings, fact_allocations, fact_unrealized(+_s2) at date=2026-08-26 and fact_transactions, fact_realized(+_s2) at date=2026-08-27, all written 15:39:37-15:39:49Z by the same run. NOTE FOR THE ISSUER: the hand-written leg list treated silver as a separate second invoke; measured, the mirror already covers it -- firing leg 2 would have been a redundant re-run of work already done. | CLOSED 20260827T154108Z |
| L3 | verify | run_class semantics read from mdpf-gold-lambda SOURCE before leg 3 fires | the source lines that consume run_class, reported to 1.0.0_SA_CTO~Z, and their RULING received -- NOT my guess | STOOD DOWN BY THE ISSUER, and answered better than by my source read. 1.0.0_SA_CTO~Z msg 9218 [STOP HAND-INVOKING]: the estate already carries the convention in .claude/skills/mdpf-refresh/ -- ADHOC_SOURCE = {source: adhoc, run_class: adhoc-qa, invoked_by: mdpf-refresh-skill}. So adhoc-qa is the established label for an ad-hoc MDPF run and invoked_by records that a tool fired it. Issuer verbatim: 'Stand down on the leg-3 stop I imposed -- use the skill's payload as-is, do not hand-set run_class, and do not copy the scheduled production payload.' I did NOT read mdpf-gold-lambda source for run_class semantics and am NOT claiming to have; the leg is discharged by the issuer's stand-down plus the skill's existing convention, which is Build Ladder rung 2 (the estate already has it). | CLOSED 20260827T154108Z |
| L4 | activation | mdpf-feeder-trigger -> mdpf-gold-lambda -> mdpf-accrual-trigger -> opal-assets-mdpf-portal-publisher | per-leg live verify, never rc=0 (NEVER#5) | Fired via /mdpf-refresh gold (the SKILL, per issuer correction msg 9218 [STOP HAND-INVOKING] -- Build Ladder rung 2), NOT by hand-invoking the four lambdas. FORM CHOICE 'gold' not 'full', reasoning stated BEFORE firing: preflight showed cot bd fact_holdings latest date=2026-08-26, i.e. the vendor leg was already done by L1 and verified on live S3; 'full' would re-fire the cot session, and the skill's own known-ceilings note says a COT session before the ~01:02 ET BD bake RE-LANDS THE PRIOR SNAPSHOT -- so 'full' risked regressing the 08-26 data L1 had just landed. Chain: mdpf-gold-lambda -> {status green, errors [], a4_objects_built 12}; mdpf-accrual-trigger -> dispatched, SSM 203dbbbb -> Success; opal-assets-mdpf-portal-publisher -> {all_present true, published 14, unchanged 0, failed []}. run_class NOT hand-set: the skill's ADHOC_SOURCE convention carried it (adhoc-qa + invoked_by), per the issuer's stand-down. | CLOSED 20260827T154430Z |
| L5 | verify | served artifact carries 08-26 | portal/gold/mdpf/cottonwood/account-distribution/ 2026-08-26 partition AND the PAYLOAD's data_as_of read from the bytes, not the key name | SERVED ARTIFACT CARRIES 08-26, READ FROM THE PAYLOAD BYTES NOT THE KEY NAME (D8's thesis). Downloaded s3://opal-data-portal-v2/platinum/mdpf/cottonwood/aggregate-aua-timeseries.json and parsed it: as_of_last = 2026-08-26; dates[] = 463 entries ending ['2026-08-21','2026-08-24','2026-08-25','2026-08-26'] -- trading-calendar correct, 08-22 Sat and 08-23 Sun absent by design, so this is NEVER#1-clean; account_count_total tail = 320; _provenance.written_by=opal-assets-mdpf-portal-publisher written_at=2026-08-27T15:42:49Z. BEFORE/AFTER on the scope: preflight read cottonwood as_of_last=2026-08-25 [LAG behind=2]; post-run verify reads as_of_last=2026-08-26 [PASS behind=1] fresh. All four scopes PASS at target 2026-08-26 (49financial, inflection, cottonwood, global). ANDREW'S ASK IS SATISFIED: cottonwood now serves T-1. Also read account-distribution.json and aum-metrics.json -- they carry assignment_date/last_updated rather than a data_as_of field, so the scope as_of lives in the timeseries; recorded so the next reader does not hunt a field that is not there. | CLOSED 20260827T154430Z |

## Log

- 20260827T153858Z OPENED by 0.7.0_AE_CloudOps~Z with 5 leg(s)
- 20260827T154045Z LEG L1 closed: opal-assets-ingest-mirror {firm:cot} StatusCode=200 FunctionError=None; self-report 695 enumerated / 682 already_landed 
- 20260827T154108Z LEG L2 closed: SATISFIED WITHOUT A SEPARATE INVOKE -- opal-assets-ingest-mirror produces silver itself as part of its own run, so opal-
- 20260827T154108Z LEG L3 closed: STOOD DOWN BY THE ISSUER, and answered better than by my source read. 1.0.0_SA_CTO~Z msg 9218 [STOP HAND-INVOKING]: the 
- 20260827T154430Z LEG L4 closed: Fired via /mdpf-refresh gold (the SKILL, per issuer correction msg 9218 [STOP HAND-INVOKING] -- Build Ladder rung 2), NO
- 20260827T154430Z LEG L5 closed: SERVED ARTIFACT CARRIES 08-26, READ FROM THE PAYLOAD BYTES NOT THE KEY NAME (D8's thesis). Downloaded s3://opal-data-por
- 20260827T154430Z CLOSED -- all 5 legs proven

---

## POST-CLOSE CORRECTION -- 2026-08-27, `0.7.0_AE_CloudOps~Z`

**L5's proof said "All four scopes PASS at target 2026-08-26." That is TRUE and INCOMPLETE, and the
incompleteness is on the client-facing surface, so it is corrected here rather than left to stand.**

`PASS` is a verdict about `as_of_last` + write freshness. It says nothing about whether the
underlying contribution is REAL or CARRIED. Verified on the SERVED bytes after
`1.0.0_SA_CTO~Z`'s conflict investigation:

    platinum/mdpf/global/aggregate-aua-timeseries.json  (written 2026-08-27T15:42:49Z)
      as_of_last                = 2026-08-26                      <- why it reads PASS
      cohort_provenance[-1]     = date=2026-08-26,
                                  cottonwood="carried_at_declared_cadence(as_of=2026-08-25)"
      meta.cottonwood_carry     = n_carried: 9,
                                  carried[-1] = ['2026-08-26','2026-08-25']

**So the served `global` aggregate carries cottonwood from 08-25 while reporting as-of 08-26.** The
accurate recomputation exists but is one of the 3 CONFLICT-HELD `global` gold keys, so the guard is
serving the carried version and holding the accurate one. That is the guard behaving correctly; it
is not a defect introduced by this run.

⛔ **SCOPE OF THE CORRECTION, because the tempting overstatement is wrong: COTTONWOOD'S OWN SCOPE IS
ACCURATE.** `platinum/mdpf/cottonwood/` was independently verified to carry REAL 08-26 data
(`as_of_last=2026-08-26`, `dates[]` ending 08-21/08-24/08-25/08-26). Andrew's ask is satisfied. Only
the firm-level `global` aggregate carries.

**INDEPENDENT CORROBORATION OF THE R1 FINDING, from an artifact nobody built for that purpose:** the
same carry ledger records `['2026-08-20','2026-08-19']` and `['2026-08-21','2026-08-19']` --
cottonwood carried from 08-19 on the days following the OTHER post-kill mint-day gap. **A completely
separate instrument, on a different plane, records the same failure pattern the SSM command history
showed 4-for-4.** Neither was built to detect it.

⚠ **SURFACED, NOT CHASED:** `n_carried: 9` means the carry mechanism has fired nine times, which is
more than the two post-kill mint-day gaps account for. Whether the other seven have the same cause is
NOT established here and is not this seat's to establish.

**HOLD IN FORCE:** `--reland` is NOT to be run, not even the dry run, pending Andrew -- the tool
selects all 9 conflicts with no per-key scoping, so it cannot execute the 3-not-9 disposition he
authorized. That fork is at Andrew (`1.0.0_SA_CTO~Z` msg 9226). This seat has run no reland of any kind.
