# ADVI_FIRMBKTS -- round 10 inputs, collected at the end of round 9's drain (`2.0.0_SA_COO~B1`, 2026-10-16 ~20:0xZ)

Standing list for the next issuance (the CTO's round-9 analysis names the enrichment list; these are the issuer's inputs to it). Round 9 is not closed: `FB-p-2` is staged. Items marked READ were read now, read-only, because they cost nothing and the CTO's rulings asked for them "next round".

## 1. The CTO's carried reads (msgs 6986, 6988)

1. **Per-date vintages for 2026-10-13 to 10-16 (READ).** Whether the per-date inputs of WS-C and WS-E are still kept, denominators printed:
   - WS-C, in `opal-data-inf`: for each of the four dates the three named objects `gold/eclipse/<d>/_meta/gold_complete.json`, `gold/eclipse/<d>/model_portfolio_accounts.parquet` and the silver `portfolios_full.parquet` of the date the gate names: **12 of 12 present** (all four dates; 12 named head-object reads).
   - WS-E, where its code reads (`opal-data-assets`, the `date=` partitions of its RPS successor prefix; one listing, 11 objects under `date=2026-10-*`, not truncated): partitions exist for 2026-10-13, 10-14 and 10-15; **none yet for 2026-10-16** (the partition arrives after its date). The partition is one object per date.
   - The Orion bronze model-composition inputs were not read (the feeder rolls them forward on-or-before the date).
   - Reading: the per-date inputs for 10-13, 10-14 and 10-15 exist, so the CTO's option (ii) (vintage passthrough as its own order and pair) is available for those three dates; 10-16 waits for its RPS partition. Not established: that a passthrough run would reproduce what the organic fire would have written, and whether the floor accepts a re-run for a past date.
2. **The causes of the four earlier A7 refusals, 10-06, 10-07, 10-08 and 10-10 (READ).** On each of the four days the trigger's log shows the 12:52Z backstop and the accelerator both returning NOT-YET, the runner's SSM list holds no feeder-chain command, and the floor's 13:3x log line reads `non_model` zero, `partners=1`, `reconciliation=ERROR`, then the A7 skip. It is the same chain as 10-13 to 10-16: gold ended after the backstop, the accelerator fired 8 to 14 seconds before its gate, nothing dispatched the feeder. (10-10 is a Saturday: the gold chain and its marker ran that day too.)
3. **Still open, and not this seat's reads:** what the portal shows for the gap dates, and who re-ran the floor at 17:32Z on 10-12 (both named by the CTO for the CVO's close).

## 2. Findings from the Door 6 work that belong in the analysis

- **The trigger's WS-E gate looks in the wrong place.** `mdpf-feeder-trigger` tests `schwab/silver/rps/date=<YYYYMMDD>/data.parquet` in `opal-data-bd`; 12 named reads of that key form (10-05 to 10-16) are all absent, and every one of the trigger's 24 logged events reads `wse_input_present: false`. WS-E reads its input from `opal-data-assets`. The gate is informational (only the WS-C gate decides NOT-YET), so it has misreported without blocking anything; whether to correct it is the CTO's.
- **Repo versus deployed.** `inf-gold-trigger`: the repo file (163 lines) is not what runs (545 lines). `orion-gold-dispatch.sh`: the repo file (119,270 bytes) differs from the deployed `code/gold/` copy (113,445 bytes) by other projects' undeployed edits. Row `D1-S61` carries the first; `FB-p-2` step 5 works around the second.
- **Three deployed dispatch copies write the marker** (`code/gold/` live; `code/gold-staging/` and `code/rebuild/` read as manual-only). The CTO ruled they change at their source.
- **The shared portal role's grant.** `opal-portal-lambda-role` carries `MonitorDataFreshnessRead`: `s3:GetObject` on all of `opal-data-inf`. Every function under it can read the marker; the census found none that does.
- **The four container-image functions** have no zip to scan; one (`opal-news-ai-sentiment`) could read the key; its application layer was searched, six layers over 5 MB were not.

## 3. Method inputs (this seat's own)

- The worker prompts of round 9 were pointer-style, not the worker face verbatim; round 10 spawns carry the face verbatim.
- The worker face line "flip the order's status to complete" caused five worker rows; later faces drop it and the issuer flips.
- The sparse worker worktree omits `org/tier1_exec` and the surprise-row schema (rows `W85-S2`, `W88-S1`); `.tools/wk-provision.sh` is MSTR's.
- The order text names the bare worker row id form which the row gate refuses on dell1 (`W89-S2`); later faces name the coordinate form.
- The census method that found the stale repo copy: download the DEPLOYED package and search it. Reading the repo copy of a Lambda is not evidence about what runs (CLAUDE.md 22a).

## 4. Carried from earlier rounds (not re-measured this round)

`D1-W70-S1`, `D1-W75-S2`, `D1-W66-S2`, `D1-W77-S3` (round 8's carries); `FB-h-5` (the live FWD-4 half, owner the CTO, parked); the 60 triage carries named in the three triage records.
