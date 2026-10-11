# NFRA_TRNSPT decomposition -- ROUND 22 (2026-10-09, issuer 2.0.0_SA_COO~T2, dell2, box/dell2)

Cut on `1.0.0_SA_CTO~DELL2` msg 3796, `CTO_ROUND_ANALYSIS_NFRA_TRNSPT_ROUND_12_20261008.md` ADDENDUM 13 @d1f23acf0c: "Round 22 enrichment list: (1)
the FWD-3 fetchable-vs-landed census; (2) each new meeting type's first landing read as it occurs; (3) FWD-9's grade on t1's landing." For (1):
"ONE LOCAL cell: list every meeting the gateway reports as fetchable on 2026-09-29, printed with that denominator, against the silver
landings, with each missing one named and its reason."

| cell | item | outcome | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|
| `TR-c-22` | (1) `teams/census.py`: given the gateway's transcript listing per allowlisted series and the silver keys, return every transcript created on or before a cutoff date (the "fetchable on" set, denominator printed), each marked `landed` or missing with a `completeness.py` cause; a `--live --cutoff 2026-09-29` CLI that reads read-only. Built on fakes | FWD-3 | dell2 worker | LOCAL | worker-light | -- |
| `TR-cr-22` | (1) the issuer's ONE live run of `census.py --live --cutoff 2026-09-29`, recorded as counts, series and causes (no content) | FWD-3 | ISSUER (read-only) | SERVED | -- | TR-c-22 |
| `TR-n-22` | (2) the issuer's read of each NEW meeting type's first scheduled landing as it occurs (ocio_ic, asset_management_ic), with `p18_readback.py` (residual re-wipe 0, planted control) | FWD-2 | ISSUER (read-only) | SERVED | -- | each series' next occurrence (event) |
| `TR-f-22` | (3) FWD-9: once t1 lands, one served commentary read through `query/securities_across.py --live` (counts only) | FWD-9 | ISSUER (read-only) | SERVED | -- | IRPT_ANLREQ TO-APPLY-t1 |

**Chains.** A = TR-c-22 -> TR-cr-22 (worker slot, then the issuer). TR-n-22 and TR-f-22 are event-gated issuer reads. Fan-out 1 of 1 worker chain, cap 8.

**Issuer rulings.**
(1) "Fetchable on 2026-09-29" = a transcript the gateway lists today, under an allowlisted series, whose created time falls on or before
2026-09-29 23:59:59Z. The research meeting is in the denominator and carries cause `refused` while the gateway answers 502 for it.
(2) Counts, series, dates and causes only; never transcript text.

## Rule 24 record

Domain: ADDENDUM 13's three items.
- (1) = TR-c-22 + TR-cr-22.
- (2) = TR-n-22.
- (3) = TR-f-22.

Remainder: none. Carried and not cut: FWD-6 (parked on site Z OG-ab-2), FWD-8 admitted read (site Z), Andrew's acts (the Monday read, the
research grant, the named past meeting).

## Battery

`org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R22_CHECKS/r22_checks.py c22` at base: FAIL (absent).

## AMENDMENT 1 (issuer, 2026-10-09 ~18:0xZ) -- CTO ADDENDUM 13.1 (msg 3840, row D2-S15): root cause FIRST, then a named recovery

The census (@ac982db915) finds 4 monday_meeting occurrences fetchable but never landed. They are exactly the 4 OLDEST of the 20 listed (created
2026-04-10, 04-13, 05-04, 06-01); every one from 2026-06-08 on landed. Listing captured as `deliverables/2.0.0_SA_COO~T2/R22_MONDAY_LISTING_FIXTURE.json`
(ids and times only).

| cell | item | outcome | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|
| `TR-rc-22` | root cause (LOCAL, read-only): replay the fixture through the pull's own selection code (the scheduled pull and the earlier backfill path), show it skips exactly those 4, name the code line, and state whether the SCHEDULED path would skip such a meeting again | FWD-3 | dell2 worker (workstream `census`) | LOCAL | worker | -- |
| `TR-rf-22` | IF the scheduled path would skip again: its fix, under its own pair, BEFORE the recovery (cut on TR-rc-22's verdict) | FWD-3 | worker + pair | WORLD | -- | TR-rc-22 |
| `TR-rv-22` | the recovery: the 4 named ids through the scheduled pull's own code path, invoked once for those ids, under ONE pair; before-read each is still held (Graph metadata); same wipe/hold-out, residual re-wipe 0; a meeting no longer held is LOST, stated with its date | FWD-3 | ISSUER pair + applier | WORLD | -- | TR-rc-22 (+ TR-rf-22 if cut) |

Chain B = TR-rc-22 -> (TR-rf-22) -> TR-rv-22. Battery: `r22_checks.py rc22` at base: FAIL (absent).

## AMENDMENT 2 (issuer, 2026-10-11 ~02:5xZ) -- TR-rc-22's verdict and the live read: the pull dies on an aged-out read; fix it, deploy it, and the 4 are LOST by this route

TR-rc-22 drained @7e77ac162b: no selection rule skips by age. The issuer's live read (`deliverables/2.0.0_SA_COO~T2/R22_ROOT_CAUSE_LIVE_READ_20261011.md`,
row NFRA_TRNSPT-D2-S16) measured the rest: the gateway refuses (502) the content read of every monday_meeting transcript older than about 120 days,
and the scheduled pull has raised on that read at every fire since 2026-10-09T16:00Z. Issuer ruling inside this decomposition (no gate limb
grades a decomposition edit; `to-pipeline-gate.py` grades the new order at this commit): TR-rf-22 is split into its build and its deploy, and
TR-rv-22 is re-pointed.

| cell | item | outcome | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|
| `TR-rf-22` | the BUILD: `_pull_series` records a refused or corrupt content read of one row as `READ-REFUSED` and continues; run-wide refusals still raise; tests | FWD-3 | dell2 worker (workstream `pullfix`: write surface `teams/pull.py` and its tests) | LOCAL | worker | TR-rc-22 |
| `TR-ra-22` | the DEPLOY of TR-rf-22's merged commit to `teams-global-transcripts-pull-lambda`, under ONE CTO + COO pair, applied by `0.7.0_AE_CloudOps~DELL2` with a change-management ledger entry; proof = the next fire completes, writes its run record and reaches all four series | FWD-1, FWD-3 | ISSUER pair + applier | WORLD | -- | TR-rf-22 |
| `TR-rv-22` | RE-POINTED: no gateway recovery exists (the 4 reads answer 502). The 4 are stated LOST by this route with their dates (2026-04-10, 04-13, 05-04, 06-01) unless the CTO names another source; the issuer writes that statement at round close | FWD-3 | ISSUER | LOCAL | -- | TR-ra-22 |

Chain B = TR-rc-22 (done) -> TR-rf-22 -> TR-ra-22 -> TR-rv-22. Battery: `r22_checks.py rf22` at base: FAIL (absent).

## AMENDMENT 3 (issuer, 2026-10-11 ~03:1xZ) -- the same hole on the LISTING call; TR-ra-22 HALTED until it merges

The issuer's deploy packet predicted that the research_meeting listing reads REFUSED. Read at 03:07Z it does not: the listing raises
`GatewayGraphError` 502, which is not a `Refused`, so the run would still end before its record. The packet's section 3 was a prediction,
not a read; the applier was halted before any build (msg to 0.7.0_AE_CloudOps~TR2, 03:08Z). Issuer ruling inside this decomposition
(`to-pipeline-gate.py` grades the new order at this commit).

| cell | item | outcome | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|
| `TR-rl-22` | the BUILD: `_pull_series` records a row-scoped gateway error on the LISTING of one series as that series REFUSED (class and status in the detail) and the run continues; run-wide refusals still raise; two tests | FWD-3 | dell2 worker (workstream `pullfixlist`: write surface `teams/pull.py` and `test_pull_read_refused.py`) | LOCAL | worker-light | TR-rf-22 |
| `TR-ra-22` | UNCHANGED in scope, RE-PINNED: the deploy now builds from TR-rl-22's merged commit; the packet gets an addendum and the CTO half is re-asked against the new pin | FWD-1, FWD-3 | ISSUER pair + applier `0.7.0_AE_CloudOps~TR2` | WORLD | -- | TR-rl-22 |

Chain B = TR-rc-22 (done) -> TR-rf-22 (done) -> TR-rl-22 -> TR-ra-22 -> TR-rv-22. Battery: `r22_checks.py rl22` at base: FAIL (missing).
