# 2.0.0_SA_COO~M -- post-crash relaunch session, 2026-09-30 13:00Z-23:35Z (IRPT_BCKEND workstream M + MDPF_SECCLASS)

**archetype:** COORDINATE
**secondary_archetypes:** DEPLOY, VALIDATE

## Summary

Relaunched at 13:0xZ after the 07:52Z laptop reboot (MSTR brief RELAUNCH_BRIEF_20260930_130xZ_POST_CRASH.md). State was
read from commits, orders and ledgers, residue cleaned, and `/canonical-drive` armed at 10m (cron 9fbec7fb, LIVE_ARMS
RELAUNCH row). Over the session: two undrained worker branches from before the crash were finished and drained; four
signed acts ran (FWD-3 VNQI seed, E_18 IAM + deploy, the Holdings narrowed-release IRPT legs, CUSIP_ROWS); one release
(the BD thread) crashed on the runner and was rolled back the same hour with no served value moved; MDPF_SECCLASS rounds
5 and 6 were issued, executed and drained. 29 commits under this serial since 13:00Z.

## Work done

1. **Relaunch residue (13:0xZ-13:4xZ).** Watcher + registration restored; three OFFER-EXHAUSTED messages read and acked.
   - WK~8 (MDPF_SECCLASS r4, SC-e-10 Kimi classifier) had committed but not drained: drained @999c35109f; issuer re-run
     18 passed, MODEL-CENSUS 260 classified / 130 flagged of 357.
   - WK~93 (IRPT_BCKEND r29, IB-mr-291 narrowed Holdings release) had staged but not committed: continuation re-proved and
     committed (c5f8b8ddd5 / df71fb818c); drained @9fef6a7e9c after two channel-conflict resolutions; suite 319 passed on
     CLOUD (row MDPF_SECCLASS-S3 disarmed in the world).
   - MSTR's push question (103220) answered: the seven MDPF_SECCLASS gold/silver files were not deployed by the push.
2. **Signed acts executed.**
   - FWD-3 VNQI seed (halves COO c4019eacd2 / CTO a7a6d286f2): 1 of 138 written, read-back equal. Ledger CLOSED.
   - E_18 IAM step 1 applied 13:56Z under the builder name `mdpf-secclass-scheduled-put-policy` (the naming gate refused the
     worker's typed name); step 2 BD E_18 deployed. Ledger HELD on the fix-forward (CTO 103369: 10-01 04:00Z is the
     expected negative control).
   - ONE WINDOW (CTO halves b4cd4a46ba): H1 plan 0/3/0, H2 `CanonicalClassifierLookup` applied on the three Holdings
     principals, H3 three bundles minted, H4 QA fire 3 of 3 Success with PHYS/GLD -> commodities/Metals and VXX ->
     structured/Hedge and to_unclassified 0 at every firm; B1 five BD files deployed, B2 IAM read.
   - CUSIP_ROWS (halves COO 5cc84b40f6 / CTO 1f4792c45a): 348 of 349 written (the 349th a census duplicate, CUSIP:786514AS8
     held by two firms, refused by design), 0 overwrites. Ledger CLOSED @8b03d64dcc.
   - L0 re-mint ledger (WK~76) CLOSED on the served manifests.
3. **BD thread crash and rollback (17:4xZ-18:3xZ).** The B3 exercise run crashed C_06 at import
   (`lib/etf_classifier.py:19` `parents[5]` into `infra/`, absent on the flat runner `/tmp/gold_layer_scripts/`); D_03/D_04
   never ran; served keys changed 0 of 4. Rolled back the five code objects at 18:16:09Z to their pre-window VersionIds
   (ETags verified). Row MDPF_SECCLASS-S5. CTO 103369 accepted the rollback as the half's own branch; CTO DECISION 103371
   set the deployed-layout import rule for all issuers.
4. **MDPF_SECCLASS round 5** (issued @6d44575a7f): SC-e-11 CUSIP guard drained @716f6f883a; SC-e-12 PARKED on
   0.7.0_AE_CloudOps (CTO 103327, round closed on chain A).
5. **MDPF_SECCLASS round 6** (issued @c7571d32b0 on the CTO rounds 4-5 analysis @533bcae124): TERMINAL 3 of 3.
   - SC-e-13 (WK~10) fix-forward: shared client shipped to `code/gold/lib/_shared/`, hops removed, deployed-layout import
     5 of 5, silver staging document fixed by amendment 1; BD_THREAD_R3 half written. Drained @9dd3e506b7.
   - SC-e-14 (WK~11) repairs: find_by CUSIP filter (client + 2 copies), seed PRE-READ count, S4 attribute_exists;
     amendment 1 for the older assertions. Drained @26655d0839.
   - SC-e-15 (WK~12) MODEL_ROWS reader census: 34 readers, 3 crashes + 1 contract failure; amendment 1 relocates the
     tolerance bar to the act. Drained @2de2d8ef46.
   - Drain packet DRAIN_END_R6_20260930.md and COO half on BD_THREAD_R3 (with the W10-S5 ordering ruling) @2744a9fc57.
6. **Held-ledger correction.** bd-securities-cot-new-p1: the served 09-23 BD firm mix is byte-identical before and after
   the write (C_06 is incremental), so the planned partition comparison cannot show the move; the hold names the corrected
   method @cab86771a6.

## MCP traffic (significant only)

- Received: CTO 103233 (PRD v0.2 landed), 103245 (rounds 2-3 analysis), 103273 (one-window halves signed), 103307
  (CUSIP_ROWS half signed), 103327 (round-5 placement ruling), 103369 (rollback accepted), 103371 (deployed-layout rule),
  103385 (rounds 4-5 analysis); peers 103242, 103258, 103280, 103287, 103293, 103321 (shared-index traffic), 103350, 103278,
  103283. All acked.
- Sent: MSTR (103220 answer), CTO (one-window packet; CUSIP_ROWS half; round-5 placement; ESCALATION on the rollback),
  CVO (r4 + r5 L8 packets), peers ~P/~Y (shared-index answers).

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| comp-which / comp-read / comp-find | PASS | used for the scheduler, runner, deploy-map and reader discovery; comp-find timed out once on a broad pattern (moved to background) |
| comp-pipescript deployed (via safe-deploy) | PASS | VERIFY OK on E_18 and the five BD files; it verifies S3 bytes, not that the runner can import them |
| comp-estate --resource | PARTIAL | named the BD gold chains but not the dispatcher's script list (E_18's absence was found by the log and the worker) |
| deploy_ledger.py | PASS | five ledgers opened/closed/held; it stages on every act, which collided with peers' drains until each act was committed at once |
| safe-merge.sh | PASS | refused on foreign staged sets and a malformed channel resolution; the ours-plus-appended-rows resolution graded clean |

**What worked:** the deploy-time naming gate (caught two typed names); safe-merge's row gate on the merged index.
**What failed:** in-repo tests and S3 byte verification both passed on a library that could not import on the flat runner.
**Gap found:** no instrument proved a runner-deployed import before a real run; CTO DECISION 103371 now makes it a criterion.

## Blockers

None held by this seat. Waiting (cited): 1.0.0_SA_CTO's half on BD_THREAD_R3 (not yet asked, packet @2744a9fc57);
3.0.0_SA_CVO's compile of round 6. Andrew's open call (from /next-calls, 18:3xZ): may a per-firm value FILL an absent
instrument_kind on an existing row (CTO 103218 routed it to him).

## Current State

- **MDPF_SECCLASS:** round 6 TERMINAL and drained; packet `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/2.0.0_SA_COO~M/DRAIN_END_R6_20260930.md`
  @2744a9fc57 (not yet sent to the CVO). Live table `etf-classifications`: 2,309 ticker rows + 348 `CUSIP:` rows; VNQI
  corrected. Halves: BD_THREAD_R3 COO-signed (CTO owed); MODEL_ROWS unsigned (census found 4 non-tolerating readers,
  rows W12-S1/S2 for round 7). Parked: TO-SC-e12 on 0.7.0_AE_CloudOps.
- **BD thread:** code objects on `s3://opal-data-bd/code/{gold,silver}/` are the pre-window versions (restored 18:16Z); the
  23:00Z nightly gold run started 23:00:30Z on that code (result not yet read). The fix-forward is on CLOUD but NOT
  deployed; its window is after the gold run completes and before the 04:00Z gold fire, upload first then the SSM document.
- **E_18:** deployed with the `parents[4]` hop; it is not in `gold_dispatch.sh` at all (row W10-S2), so it has no
  scheduled trigger; ledger `secclass-e18-iam-and-deploy-m-20260930` HELD.
- **IRPT_BCKEND ~M:** narrowed Holdings release H1-H4 done; H5 is the 2026-10-01 14:15Z `irpt-holdings-snapshot` fire, read
  on the Investor Reporting Holdings page (PHYS commodities/Metals). One-window ledger HELD for the BD legs.
- **Push state:** origin/CLOUD 85a765dbcd (ls-remote 23:32Z); it contains this seat's commits through @044157b073 at least;
  @2744a9fc57 is LOCAL. Local CLOUD is ahead of the stale tracking ref.
- **Loops:** `/canonical-drive` cron 9fbec7fb (10m); inbox watcher armed.

## Next Steps

1. Send the round-6 packet @2744a9fc57 to [3.0.0_SA_CVO]; ask [1.0.0_SA_CTO] for the BD_THREAD_R3 CTO half.
2. Read the 23:00Z BD gold run's result (the rollback's proof), then, with both halves, run the BD_THREAD_R3 window before
   04:00Z and read the 04:00Z fire and the FWD-1 page for z08327149.
3. 2026-10-01 14:15Z: H5, the PHYS read on the Holdings page; close the IRPT legs.
4. Round 7 (after the CTO's round-6 analysis): W12-S1 and W12-S2 fixes, a fresh census before MODEL_ROWS, E_18's trigger
   (W10-S2), the exact contract pin.
5. [Andrew] the instrument_kind fill call.
