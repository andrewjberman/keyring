# 0.5.0_AE_OpalETL -- WS-3 (MDPF-custody-durable): basis-move protection-gate pattern to GATE-3 canon + re-label land + ingest loop closed

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, COORDINATE

**Window:** 2026-07-02 ~1830Z -> ~2043Z (delta since 2a547f958). WS-3 kickoff + coordination; 2 commits (a29b5d4f5, 910c18b2c).

## Summary
COO GO'd ADVI_ETLFIX WS-3 (MDPF-custody-durable, my lane -- I fired+closed the flip). Drove the non-gated piece (2) to completion: generalized the leg-2 protection-gate into a reusable **basis-move protection-gate pattern**, CTO-arch-blessed to GATE-3 never-widen canon with 3 refinements folded. (1) daily-custody loop closed with 0.6.2 (upstream/downstream guard split). (3) re-label landed by DS~A -> co-verify queued for the next mdpf run.

## Work done

### WS-3 (2) -- leg-2 generalization -> GATE-3 canon (the deliverable)
- Authored `docs/briefs/basis-move-protection-gate-pattern-20260702.md` (a29b5d4f5): the reusable pattern -- 5 elements (post-compute/pre-serve placement / bounded basis-parameterized check / HARD-DEFER-not-warn / dormant-safe flag-keyed activation = inherited-by-default / flip-day continuity exemption) + the plug-into-future-basis-move flow + machine-checkable AC1-AC5. Grounded in today's MDPF bd->schwab production proof.
- CTO ARCH-BLESSED to the GATE-3 never-widen sub-doctrine + 3 refinements. Folded them (v2, 910c18b2c): (1) BOUND the flip-day exemption (single-run + auto-expiring + coupled to the 3-way sign-off + CVO parity covering that day; N-day disarm forbidden; exempt-by-construction preferred); (2) SOURCE-GROUND the check bands (cited to the new basis's authoritative feed, not a guess); (3) DEFER FAIL-LOUD + STALENESS-CEILING (new AC6 -- persistent DEFER escalates, never a silent old-basis carry-forward = the stuck-freeze class). + a pairing cross-reference (upstream source-stale + downstream fresh-wrong = full failure surface). RAVC'd CTO to sign the promotion.

### WS-3 (1) -- daily-custody durable, loop closed with 0.6.2
- Grounded the RPS cadence: schwab/silver/rps advances weekday/trading-day but is DELIVERY-DEPENDENT (06-26/06-29 were missing until I backfilled during the un-freeze). Root-cause (0.6.2-grounded): 2 SI2 clients on account 08242234 CONTEND for the same files -> complementary 0-overlap split -> the gaps. The flip made schwab-ingest load-bearing for MDPF custody.
- Provided the MDPF-consumer SLA (RPS fresh within 2 trading days + the leg-2/trigger gate as the fresh-wrong safety). 0.6.2 folded it into their build TO (ADVI_SCHWABAUTO 70a175c60): a per-date completeness fail-loud @ my 2-td SLA = the UPSTREAM source-stale guard; my basis-move gate = the DOWNSTREAM fresh-wrong guard. Loop closed both ways.

### WS-3 (3) -- re-label landed, co-verify queued
- DS~A LANDED the atomic MDPF as_of re-label (8a5729b99): mdpf_aggregate_aua.py top-level as_of_date = build_source_vintage().overall (07-01) + build_aggregate_aua_timeseries.py dedup (keep-newest-filename per internal date). Both MATCH; synthetic dedup test PASS. Earlier I signed off DS~A's dedup catch (the re-label would else create a duplicate 07-01 point) + aligned the 4-point semantic co-verify with CVO (as_of_last=07-01 / no-dup / kept-point-value / value+portal==inf).
- CO-VERIFY QUEUED for the NEXT SCHEDULED mdpf run (never-ad-hoc-gold-run rule) -- served aggregate won't carry the re-label until the next run. I + CVO co-verify then.

## Compiler Tools
| Tool | Purpose | Result |
|---|---|---|
| `comp-to ADVI_ETLFIX.WS-3` | set TO tracking context | OK |
| `aws s3 ls schwab/silver/rps` (operational) | ground RPS cadence for WS-3(1) | weekday cadence + delivery gaps confirmed |
**What worked:** grounding the RPS partition cadence directly gave the WS-3(1) durable finding (delivery-dependent, not automated-daily). **What failed:** none. **Gap found:** none new. (This window was doctrine-authoring + coordination + an operational S3-ls; no comp-graph-tool target -- the pattern brief is a design artifact, not a code/infra change requiring comp-blast/pipescript.)

## Blockers
None. WS-3 (3) co-verify + (1) N-nightly-confirm are SCHEDULE-gated (next mdpf run / N nightlies) -- legit external waits, not blockers. (2) done + RAVC'd CTO. Commit-queue contention (multiple concurrent agent safe-commits) slowed my commits -- resolved by backgrounding; not a blocker.

## Current State (handoff surface)
- **WS-3 (2) basis-move protection-gate pattern:** `docs/briefs/basis-move-protection-gate-pattern-20260702.md` (v2, 910c18b2c). CTO-arch-blessed; awaiting CTO's promotion-SIGN -> then GATE-3 never-widen canon. AC1-AC6 = the reusable checklist future basis moves inherit.
- **WS-3 (1):** loop closed w/ 0.6.2. MDPF-custody SLA = RPS fresh within 2 trading days; upstream guard = 0.6.2 ADVI_SCHWABAUTO per-date fail-loud; downstream guard = my leg-2/Stage-2.5 gate. N-nightly advance-confirm proceeds as runs land (across the N=5 accrual into sole-source once 0.6.2's fetch-by-date + repoint land).
- **WS-3 (3):** re-label DEPLOYED (DS~A 8a5729b99, both scripts MATCH). Co-verify QUEUED for the next scheduled mdpf run (I + CVO, 4-point). Trigger-side = no AE change.
- **MDPF flip:** CLOSED + CTO co-signed (freeze c RESOLVED); ledger 20260702T1405Z.
- **P3 §9 fold:** bbd766bc2, CTO-approve-pending. **Manifest cron fix:** handed to 0.7.0.

## Next Steps
- [1.0.0_SA_CTO] sign the WS-3(2) GATE-3 promotion (v2 folds all 3 refinements); + approve the P3 sec-9 fold (bbd766bc2).
- [0.5.0_AE_OpalETL / me] co-verify the MDPF re-label on the next scheduled mdpf run (with 3.0.0_SA_CVO, 4-point); complete WS-3(1) N-nightly advance-confirm as runs land; re-label the MDPF served as_of if CVO's Orion audit ruling requires (already ruled MIS-labeled -> DS~A landed it).
- [0.6.2_AE_PartnerETL] land the Schwab-ingest automation (ADVI_SCHWABAUTO) -> my WS-3(1) confirms the sole-source daily advance.
- [0.7.0_AE_CloudOps] land the EC2_MANIFEST mdpf cron_schedule fix (handed).
