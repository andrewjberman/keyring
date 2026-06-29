# DS Session Log -- DATEMODE-B recovery + Schwab-SSOT cutover (seams, headline-AUA, xref-location fix)

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, IMPLEMENT, COORDINATE, VALIDATE
**serial:** 0.4.0_DS_ClientPlatform | **date:** 2026-06-29 | **window:** since GOLD-CORE log `c7bf68dcf` -> now (~13:00-20:10Z)

---

## Summary

Second half of a long session, all under the Andrew-GO'd 49F **Schwab-as-SSOT migration** (DATA_SSOTMG).
Headline: drove the cutover from "8 gold tables built" to a grounded, owner-mapped, mostly-progressing deploy
gate -- AND found/fixed two real correctness bugs by source-grounding rather than trusting self-report (a
stale-xref the live advisor dims silently read for 2 months; my own incomplete first fix, caught by 0.6.0).
Plus the cot DATEMODE-B freeze recovery + the headline-AUA total-consistency analysis that became the formal
cutover gate.

## Work done (this window)

| # | Item | Commit | Outcome |
|---|---|---|---|
| 1 | cot DATEMODE-B fix commit+deploy (retry-net + Cond-2 ETag silver skip) | 6241d7227 + ledger 242295abb | MATCH-verified both; deploy-ledger 3-leg closed; base wired SSM (placement A) |
| 2 | bd-silver AC#3: incident (local-run overwrote a prod partition) -> RESTORED + ASCII-fix | 12cc7e111 | caught via S3 versioning; root-caused "merge is a runner job"; fix deployed both locations |
| 3 | G3-G10 wired into build_canonical_daily.py (CTO GO) | 1026138a7 | full G1-G10 daily cadence; dry-run 21/21 |
| 4 | MACRO /seams pass: canonical Schwab-SSOT EC2 end-to-end (9 seams + hookup checklist) | bca255b38 | the deploy gate of record (org/seams/canonical-schwab-ssot-ec2.md) |
| 5 | G11-G14 firm-extension wired (S5, COO GO) | 47cc26a7f + flip 888c9d5cf | full G1-G14 daily cadence; dry-run 25/25; recon tracker folds in |
| 6 | S+ code-deploy-path: 28 canonical scripts staged to s3 code/ | be5b14ffe (flip) | EC2 can pull; io-registration routed to CVO/CTO (resolver is generated) |
| 7 | Headline-AUA design + non-Schwab threading (the cutover total-AUA gate) | f2625ff4d + 91d415fdf | docs/briefs/DATA_SSOTMG_HEADLINE_AUA_design.md; G0.held_away_aua spec |
| 8 | S4/S8 trigger co-design w/ 0.6.0; S1 prefix resolved-by-design; +S10 | ecb793037 | UPT-sentinel, ~21Z fire, sentinel=EventBridge-A, daily cadence |
| 9 | XREF-LOCATION FIX -- all 4 dims repointed off stale 03_silver | 5c77d1598 + f196aa684 | live advisor surfaces were 2-mo-stale; closed the cutover correctness gate |

## Key diagnostic / grounding wins (the discipline that held)

- **The +$48.7M headline "scare" was a stale-xref artifact.** Andrew's partition rule (canonical-Schwab +
  BD-non-Schwab surplus, no double-count) gave +$48.7M with the stale 04-21 xref; the FRESH 06-29 xref
  collapsed it to **-$3.6M (flat)** -- +$78.2M account-set was the artifact (shrank to +$27.6M), the -$31.2M
  valuation is REAL (same-date Schwab-direct price-source diff, Andrew-accepted-as-truth). Grounded, not asserted.
- **The xref-location bug (verify-not-assume, x2).** The producer writes opal-data-bd/schwab/silver/account_xref
  but the DIMS read opal-data-schwab/03_silver/account_xref (stale 04-21) -- so my "fresh xref" never reached
  the dims. I fixed 2 advisor dims; **0.6.0 source-grounded my fix and caught I'd missed dim_account +
  dim_relationship** (SRC_BUCKET dual-use: raw + xref -> needed a separate XREF_BUCKET). All 4 now fresh + live.
- **bd-silver incident, self-reported + remediated.** Ran the merge locally (it's a Linux-runner job); Windows
  charmap + a mangled manifest-fetch started a reprocess-all and overwrote one prod partition before crashing.
  Caught it, restored from S3 versioning to the runner's exact prior version, root-caused, handed the run to the runner.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-pipescript io | D_00..D_04, B_02/C_03/C_02/C_05/D_03, A-dims | PASS | grounded the prod A/B/C/D DAG + the publisher inputs + the BD-served comparator map |
| comp-pipescript deployed | cot bronze/silver, bd merge | MATCH | STALE->MATCH verify post-deploy |
| ds-commit-gate | every .py touched (G11-G14 wire, dims x4, bd-silver, xref) | PASS | py_compile+AST+ruff clean; caught the missing future-import on the legacy bd merge |
| safe-commit / safe-deploy | ~14 commits + the cot+bd deploys | PASS | surface-check clean; one Win32 verify-substep quirk (cp landed, MATCH confirmed independently) |
| comp-freshness bd | bd-silver freeze state | FAIL (txn/realized/unreal) | the 64h freeze; allocations PASS |
| boto3 (direct S3) | reconciliation + read-back + xref split + re-materialize | PASS | the spine of the headline-AUA grounding + every own-change verify (F5) |

**What worked:** boto3 live-artifact grounding caught the +$48.7M-vs--$3.6M xref artifact + the partition rule;
source-grounding (mine + 0.6.0's) caught both correctness bugs self-report would have shipped. **What failed:**
the local bd-silver merge (wrong environment -- runner job); recovered losslessly. **Gap found:** the xref
producer writes a DIFFERENT location than the dims read (now unified to opal-data-bd/schwab/silver); the
canonical scripts aren't in comp-pipescript's tree-map (routed to CTO).

Compiler-tools-log line appended.

## MCP traffic

~70+ messages (event-driven, the cutover came alive). Significant: COO (DATEMODE-B GO, AC#3 freeze-recovery,
S5/S+ GOs, the total-AUA cutover-gate formalization, the 4-item critical-path); CTO (G3-G10 wire GO, DATA_SSOTMG
register); CVO (parity comparator map fully grounded b65335016, S7 total-AUA fold); 0.6.2/0.7.0 (DATEMODE-B
SSM + bd-49f-runner); 0.6.0 (CUTOVER-1 S4/S8/S6 co-design, the xref-fix-incomplete catch); DS~B (TO-3/TO-7
G11-G14 + recon co-own); Andrew-direct (the AUA partition rule + accept-canonical ruling + "drive the xref fix").

## Blockers

None of mine open. The cutover's remaining items are owner-distributed (0.6.0 runner/role/trigger; CVO S7
parity-schedule; AE/DT S1/S6) and progressing -- not blocked.

## Current State (handoff)

- **Canonical gold:** full G1-G14 roll daily via build_canonical_daily.py (1026138a7 + 47cc26a7f), dry-run 25/25.
  Scripts staged at s3://opal-data-bd/code/canonical/schwab/ (28, AES256) for the EC2.
- **XREF (load-bearing):** all 4 canonical dims (advisor_role/_fee/account/relationship) now read the FRESH xref
  at opal-data-bd/schwab/silver/account_xref/ (was stale opal-data-schwab/03_silver/04-21). Fresh xref written
  date=20260629 via build_schwab_bd_account_xref.py. Dims re-materialized live @asof=2026-06-24. **S10 = the
  DS-owned xref-refresh is a HARD daily pre-step before the build** (proven: stale xref = wrong headline).
- **Headline-AUA gate:** partition rule = canonical(Schwab $1.591B) + BD-surplus($269.5M->$217.2M fresh) =
  ~$1.808B; BD-served $1.812B; net -$3.6M, ACCEPTED canonical-as-truth (Andrew). S7 PASS = canonical+surplus
  reproduces the agreed ~$1.808B stably over N-days. G0.held_away_aua = NOT YET BUILT (the surplus producer).
- **Seam gate (org/seams/canonical-schwab-ssot-ec2.md bca255b38++):** PASS S2/S3/S5/S9; STAGED S+; PROG S1
  (resolved-by-design)/S4/S8/S10; UNVER S6(0.6.0)/S7(CVO).
- **DATEMODE-B + AC#3:** code+deploy done; ACCEPTANCE rides tonight's nightly (cot AUA past 06-09 + bd_silver PASS).

## Next Steps

- **[0.4.0_DS_ClientPlatform]** (a) BUILD G0.held_away_aua (the non-Schwab surplus producer -- the headline gate's
  runnable piece); (b) wire the put_events emit into the S10 xref-refresh (EventBridge Option-A -> 0.6.0's S4
  trigger) + set up the S10 daily schedule; (c) the A-tier gold dims + C-bridges + D-artifact-JSON layer (reach
  the publisher unchanged -- the rest of the iceberg per the DAG walkthrough); (d) verify tonight's nightly
  (DATEMODE-B 06-09 unfreeze + AC#3 bd_silver PASS + the S5 G11-G14 output-match w/ DS~B).
- **[0.4.0_DS_ClientPlatform~B]** re-materialize G11-G14 on the fresh-xref dims (advisor surfaces were on the stale mapping).
- **[0.6.0_AE_PartnerETL]** lock the role (schwab=raw-only now) + fire the runner apply-push (all 4 held items cleared).
- **[3.0.0_SA_CVO]** S7 parity incl. the total-AUA reconciliation (comparator map grounded); schedule for the parallel window.
- **[1.0.0_SA_CTO]** fold the headline-AUA brief into docs/architecture (DS can't write that lane) + the comp-pipescript canonical-tree io registration.
