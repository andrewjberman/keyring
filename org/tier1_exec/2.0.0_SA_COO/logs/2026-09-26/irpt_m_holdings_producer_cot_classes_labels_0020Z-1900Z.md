# 2.0.0_SA_COO~M -- IRPT_BCKEND~M session log, 2026-09-25 00:20Z to 2026-09-26 ~19:00Z

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DEPLOY, VALIDATE, COORDINATE

Seat 2.0.0_SA_COO~M, lane IRPT_BCKEND~M (the Holdings backend: snapshot producer, classification, COT gold mix).
Covers the window since `irpt_m_blast_mode_holdings_directory_classification_1745-0020Z.md` (1998cd5810): 129 commits
by `2.0.0_SA_COO~M`. Loops: /canonical-drive hourly (cron 25fee401) until the self-drive arm (CTO msg 101099,
@ce6aa15a17); then /closer-drive every 30 minutes (cron ae118e19, paused 15:27Z-16:03Z on Andrew's word via CTO
101278/101295, re-armed as 75ed13d3).

## Summary

- **The scheduled Holdings producer (CTO R4) is built and applied, DISABLED.** Standalone per-firm packages (40
  members, manifest-stamped), a stateless SSM dispatch function, one principal per firm with measured grants, and the
  schedule retargeted and kept DISABLED. The first apply half-landed (IAM MalformedPolicyDocument on an empty
  dynamodb_scan) and was finished in-session. What is left for Monday is the exercised negative arm (N1), one QA fire
  and the enable half.
- **COT gold admits `other` (act 1) and `cash`, each deployed as its own act.** Ledgers cot-other-admission-m-20260925
  and cot-cash-admission-m-20260925 hold R1 for Monday's first COT run.
- **Classification:** batch A written (204 keys). The loader defect was closed with no change (ticker is the HASH
  key). COT B_01b now reads `gold/canonical/holdings/`. Andrew's ONE COT OpenAI run: 1,012 of 1,012 answered.
  Andrew ruled that established equities stay and `other` is personal assets only. Batch B was re-cut into Part 1 (941
  keys, WRITTEN) and Part 2 (26 `other` keys, signed, waiting on Monday). Six name duplicates were aligned (served
  DELTA=0).
- **A code-only grant did not survive an integrator push (S141).** MSTR's CLOUD push auto-deployed the fixed B_01b; it
  was disarmed in 5 minutes by restoring the prior S3 version, with no upload in the window. The skip-list B_01b is now
  built but held OFF CLOUD so its deploy stays its own act.
- **S145 closed as a true zero (S146).** The 49F client's three accounts are $0.00 in every Schwab dim_balance field.
- **ACCOUNT own-mask labels (CTO 101302):** code on CLOUD 5d5678d6c1; both halves signed. The served-as_of rebuild
  was a STOP at all three firms, so the labels ride the first scheduled publication.
- **R4 enable diff, first read:** with the served source partitions pinned, 0 amount, node-set or clock changes at any
  firm. The one uncovered class is INF's 30,881 name facts, admitted by the CTO after a census found 0 personal data.

## Work done (by thread)

### CTO R4 -- the scheduled daily Holdings producer (~M's; enable goes to the CTO as a never-widen half)
- Row 3: opt-in `"stamp": "manifest"` bundles in safe_deploy_core (7d3e4255a8, test fix cc4eeb51d2), and
  STANDALONE_BUNDLES that are never commit-routed (ec48c5d144). Packages irpt_holdings_{49f,inf,cot} minted from
  CLOUD; ledger irpt-holdings-packages-m-20260925 CLOSED (c1c6fa7477).
- Row 4a: the publication writes through a firm-scoped publish principal (3e1ca981ab).
- Row 2: `refresh_dispatch.py`, one SSM command per firm, SHA256SUMS verified, stateless (0154b4f03a; own source dir
  4a49b03031). Artifact uploaded; ledger irpt-holdings-refresh-artifact-m-20260925 CLOSED (a045790a3b).
- Row 4b: one principal per firm; grants measured from every botocore call of each firm's build
  (HOLDINGS_FIRM_PRINCIPAL_GRANTS_20260925.json, 4e995812bb); the host script runs the whole build as the firm's
  principal (61b497f14f).
- Terraform (holdings_refresh.tf + schedule slot) under CTO exact-file grants. Both halves signed (COO @885ae2f3d6,
  CTO @6c5c27a666). APPLIED under ledger irpt-holdings-principals-dispatch-m-20260925; P1, AP1 and V1 closed
  (@253d92d48b). The half-landed first apply was fixed by 674a9c02f6. S135 (a CLOUD apply would have reverted ~P's
  09:30 schedule) was DISARMED (S136).
- Monday pre-staged: r4_monday_negative_arm.py (01c9e248ad). The exclusive trust is shown: user AssumeRole on the 3
  firm roles gives AccessDenied, 3 of 3.

### COT gold -- `other` (R5 batch B act 1) and `cash` (S138)
- Consumer census (c2aa94d8c8). C_06 admits `other`; D_03/D_04 name an unknown security `unclassified`
  (7889280827). Both halves signed. DEPLOYED (ba28316655); ledger cot-other-admission-m-20260925 D1 closed, R1 held.
- S138 measured (S139, 5cc4fc3367): $19.23M of cash across 178 clients dropped from the mix. Cash was signed as its OWN
  deploy after the AI Cottonwood views rendered cash and other on PROD (portal-v2.1.188, 36a37afc, checked in
  layout.ts:125-128). Re-applied (7fd8149448), merged (75cc52a285), DEPLOYED (ab15cb5eb4); rollback is the prior S3
  version HJa2V4VY...; R1 held.

### Classification (R5)
- 49F no-ticker rows named from the Schwab master (cb8cd03113). INF rows named by Orion's own `name` (e0f680f0df).
- Andrew's first ONE OpenAI run: 285 of 285 (9c769fba15). Batch A written, 204 of 204 (ledger CLOSED @f99c664dd0).
- R5 decision 3: the loader-skip defect is CLOSED with no change; COT B_01b reads `gold/canonical/holdings/`
  (8f67065e50, CLOUD e20b0990d5).
- CALL 2 (Andrew ~02:1xZ, @37025a10e9): the ONE COT run over 1,012 keys, 1,012 answered, file only (c3dde578b9).
- Andrew-direct ~02:3xZ, recorded verbatim @c3dde578b9: "If we have established securities are equities we should
  keep them as such"; "the only context for "other" is personal assets, like somebodys house, their credit card line,
  and similar held away".
- Write set 967 keys (R1 7, R2b 35, R3 10 excluded). Deltas read from C_06's rule: COT 09-22 and BD 09-23. The CTO
  signed @ab4a2e41bb with an a07 precondition. a07 measured: 49F 10 keys $56,952, INF 8, COT 122; 0 changes outside
  the written keys. **Part 1 WRITTEN** (aaef2843a8): 941 of 941, 0 refused, read back 941. Six NAME:: duplicates
  aligned to fixed_income on REC (served DELTA=0 over 128,359 rows; ledger CLOSED, 1d2b27a1c2).
- **S141:** MSTR's push (079fbf7d8e) auto-deployed the code-only B_01b. DISARMED 02:44:33Z by restoring version
  jRtJ.LnIa... as nSr3.NM7H...; the watermark read 404 shows no upload ran; opal-cot-gold-run never names B_01b
  (268f1a453f).
- Skip-list B_01b (Andrew's pick of option 4): 52 ruled-out + 26 Part-2 keys, and the rule-2 prompt. The dry run finds
  0 new securities. It is on branch `irpt-m-b01b-skip` @c993550, NOT merged (2365a5fda8).

### Holdings display and served checks
- S145: a true zero, dispositioned DISMISSED_WITH_REASON (S146, 5bee820159).
- Own masks: `account_mask` equals directory_runner's rule (pinned by test); each builder masks from the columns the
  directory masks from (5159863fdb, CLOUD 5d5678d6c1). Both halves signed (CTO @45bafa24a1, CRO @c412578ede). The
  served-as_of rebuild was a STOP at all three firms (@4fd998322e).
- R4 enable diff, first read (707490f568): the unpinned 158k/17k/62k were the rebuild's 09-22 partitions against the
  served 09-23 ones. PinnedListing reproduces the served inputs. INF name census (6be843ee44): 0 email-like; 8
  six-plus-digit texts, all security identifiers; SAFE.

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| comp-pipescript io (C_06 cot, B_01b) | PASS | named C_06's `gold/canonical/holdings/` source; B_01b's empty prefix |
| .tools/commit-gate.sh (every .py) | PASS | ruff F401 caught twice, fixed before commit |
| .tools/surprise-row-gate.py | PARTIAL | S146 first refused for a missing `dismissal_reason`; added, then PASS |
| .tools/safe-deploy.sh (C_06, D_03, D_04, cash) | PASS | comp-pipescript VERIFY OK on each |
| deploy_ledger.py | PASS | a sentinel staged then removed on close needed `git restore --staged` before commit |
| comp-tool rail (Bash) | WARN | a recursive grep and a .tf grep were refused; moved to Grep and targeted reads |

What worked: reading each value from the producer's own rule (C_06 `classify_holding`, a07 `classify`) instead of
predicting it; pinning the served source partitions; version-restore disarms.
What failed: an unpinned rebuild presented source-partition drift as code change; a code-only grant was blind to the
push-time deploy gate.
Gap found: the push deploy gate has no notion of grant scope (S141). A grant marked "code and dry run only" deploys on
the next CLOUD push.

## Deployment Sequence + Verification

| Act | Ledger | Verification (actual) |
|---|---|---|
| R4 principals, dispatch, schedule (DISABLED) | irpt-holdings-principals-dispatch-m-20260925 | re-plan "No changes"; CodeSha256 = artifact; 4 of 4 policies = planned JSON; N1 HELD for Monday |
| COT C_06/D_03/D_04 act 1 | cot-other-admission-m-20260925 | safe-deploy VERIFY OK x3; R1 held |
| COT C_06 cash | cot-cash-admission-m-20260925 | S3 read-back line 173 carries cash, version LmvfjXlB...; R1 held |
| bd-securities batch A | bd-securities-batch-a-m-20260925 CLOSED | 204 put, 204 read back, loader 204 |
| bd-securities Part 1 | bd-securities-cot-new-p1-m-20260926 | 941 put, 941 read back, loader 935 (+6 aligned); R1 held |
| Align six | bd-securities-cot-new-align6-m-20260926 CLOSED | DELTA=0 before; 6 of 6 read back; fresh loader 6 of 6 |
| B_01b disarm (S141) | cot-b01b-disarm-m-20260926 CLOSED | latest nSr3.NM7H... ETag eedfd1d1 = prior; HOLDINGS_LOTS_PREFIX read back |

## Blockers

- **EVENT-GATED (Mon 2026-09-28):**
  - The daily-runner host is stopped until about 12:52Z. N1, the QA fire and the enable half wait on it (ledger
    irpt-holdings-principals-dispatch-m-20260925, gate external).
  - The first scheduled COT gold run gives R1 for three ledgers, then Part 2.
- **NEEDS 2.0.0_SA_COO~D:** the firm-tab HAR from the agent walk (Andrew-direct ~02:1xZ, "have an agent do those
  walks and record HAR") for goal criterion (1).

## Current State

- Push state: `origin/CLOUD` ac15460755 (ls-remote read at this log); 707490f568 is on origin (fetch +
  is-ancestor). Commits after it are LOCAL until 0.0.0_AB_MSTR's next push. Branch `irpt-m-b01b-skip` (c993550) is
  local and deliberately unmerged.
- STATUS: `org/missions/D9/IRPT/IRPT_BCKEND/STATUS~M.md` (2365a5fda8).
- Served Holdings: 09-22 revisions COT fc199c8e, INF ba9001d5, 49F 9ab377ce (unchanged this window).
- Open ledgers (held for Monday): irpt-holdings-principals-dispatch-m-20260925 (N1), cot-other-admission-m-20260925
  (R1), cot-cash-admission-m-20260925 (R1), bd-securities-cot-new-p1-m-20260926 (R1).
- S3: COT B_01b serves the empty-prefix no-op (S141). COT C_06 carries `other` and `cash`.
- Tools for Monday, in `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/`: r4_monday_negative_arm.py,
  account_mask_publication_diff.py (--pin-served), holdings_publication_diff_classes.py,
  bd_securities_write_cot_new.py (census/write --part 2), R4_ENABLE_DIFF_20260926/.
- The retained captures, landed: INF eclipse membership date=2026-09-24; 49F taxsma projection date=2026-09-23.

## Next Steps

1. [2.0.0_SA_COO~M] Mon ~12:52Z: `r4_monday_negative_arm.py --send`, then `--read`, closing leg N1. Then one --qa
   fire of irpt-holdings-refresh-lambda. Then re-run the pinned diff and the INF name census at the fire's as_of.
   Then send the R4 ENABLE half to [1.0.0_SA_CTO] (who signs on arrival) and [4.0.0_SA_CRO].
2. [2.0.0_SA_COO~M] Mon first COT run: read back R1 on the three COT ledgers. On pass, run
   `bd_securities_write_cot_new.py census --part 2` then `write --part 2` under a new ledger, and tell
   [2.0.0_SA_COO~D] to grade z09305589 at $19,653,063.27.
3. [2.0.0_SA_COO~D] Firm-tab HAR from the agent walk, then ~M runs /verify on the goal.
4. [2.0.0_SA_COO~M] B_01b: merge irpt-m-b01b-skip and safe-deploy as ONE act under a ledger, only when COT's chain
   adds B_01b.
