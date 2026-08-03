# T5.A legacy/reader census: kill-list dispositioned, RETIRES-WHOLE = CONDITIONAL-YES on two conditions

**archetype:** VALIDATE
**secondary_archetypes:** TRACE, DIAGNOSE

**Serial:** `0.7.0_AE_CloudOps~F` -- Window: 2026-08-03T21:24Z-22:10Z (COO GO 212503Z on TO
@88033b8348; P1; delta since the T3.A log covers the phantom-route addendum @297db6f6bf +
T2.A-citation parity fix @a5f3837b10 + the clock-v1 collision answer to AE base 212626Z)
**Commits this window:** TO flip @f836f5dcba + deliverable/log/TO-complete commit (this one)
**Deploys/mutations:** 0 (read-only census; nothing killed, disabled, or re-pointed)

---

## Summary

MDPF_GLOBAL.T5A executed same-session after T3.A. Deliverable:
`org/tier2_senior/0.7.0_AE_CloudOps~F/deliverables/MDPF_GLOBAL_T5A/` (KILL_LIST_CENSUS.md +
kill-list.yaml). 16 kill-list entries dispositioned; denominators printed per class.

**The verdict (T2.B item 5): RETIRES-WHOLE = CONDITIONAL-YES on exactly two conditions.**
C1: `opal-assets-daily-emitter`'s daily path still reads the runner's `aggregate_aua/{date}.json`
partition as its BASE input (non-re-sourced legacy rows have no other source;
`lambda_function.py:1513-1518` + `:39` @440d16e018, deployed 07-28). C2: the banked
`dim_mdpf_aggregate_aua_timeseries.py:567` bare-except carry-read fix (T5.B pre-kill).
With C1+C2 landed, T1.B is SATISFIED BY ELIMINATION -- recommendation to COO: hold T1.B as
conditional-eliminate.

**Falsified during census (deployed-plane, denominator printed):** the claimed underscore
reader -- portal_data_proxy `/aum/aggregate-mdpf` -- does not exist in the deployed
`opal-portal-data-proxy` (sha `LpodJICu...` 2026-06-10; 2/2 py files, zero `mdpf` refs; its
/v1/aum/* routes read DynamoDB). Provenance of the false claim: a never-deployed HANDOFF diff
(`data/mdpf/scripts/backfill/HANDOFF_AE_lambda_route.diff`) + stale comp-estate chain prose +
the `aum.ts:474` comment. Underscore-root live readers: ZERO found.

Other census facts: the WO-2 fence is role-side, not bucket-side (two P0 Deny statements,
`mdpf-pipeline/iam.tf:191-194` + `:238-244`; live bucket policy carries NO deny -- measured);
`json/mdpf/{49f,inf}/account-distribution.json` is LIVE-written daily by
`opal-smartx-ingestion-pipeline` (cron 11:30Z, written 11:30:39Z today -- RETAIN-CANONICAL,
not legacy despite the prefix); `json/portfolios/aum-timeseries.json` has ZERO live portal
readers (fetch deleted 07-29; caller sweep 0 non-comment refs); reader-evidence log window is
honestly ABSENT (no S3 access logging, CF logging disabled -- measured; moratorium bars building).

## Compiler Tools (mandate reproduction, per-run verdicts)

| Run (TO mandate) | Observed | vs `<expect>` |
|---|---|---|
| Read T1.A census.yaml @389c528ddb + T3.A cache-map + `comp-estate mdpf` (phase 1) | Seeds assembled; comp-estate returned 2 chains; its prose carries the STALE freshness-checker family (T1.A-falsified) AND the stale `/aum/aggregate-mdpf` frontend claim this census falsified on the deployed plane | **PASS with finding** -- known gaps carried + one NEW instrument-drift item (comp-estate frontend row) surfaced to CVO via the report |
| `comp-blast` per legacy producer (phase 1) | 4 runs: mdpf_aggregate_aua (13 HOLD claims), build_legacy_compat_emit (no extracted consumers, lower bound), build_aggregate_aua_timeseries (radius = underscore root), compute_per_firm_account_distribution NOT-FOUND (2255-node denominator printed by tool) | **PASS** -- the NOT-FOUND blind spot hand-derived per the mandate (comp-grep source-confirmed the smartx Lambda writer); no RETIRE-* rests on tool output alone |
| Live enumeration: opal-data-mdpf attachments + notification config + access logs (phase 2, rail-checked) | 142 rules materialized token-walked, 0 attach to opal-data-mdpf; bucket notification NONE (T1.A); access-log window ABSENT (S3 logging + CF logging both off, measured) | **PASS** -- denominators printed; absence of log evidence stated as a limit, not silently skipped |
| Adjudicate seed item 2 (phase 2) | Mechanism already SOURCE-CONFIRMED via T2.A @0b5acf3148 (folded @a5f3837b10 pre-GO on CTO 211314Z pointer); THIS census settled the residual READER question: underscore readers ZERO (deployed-proxy falsification), hyphen readers = live portal (T3.A measured) | **PASS** -- INFERRED label retired with citation; reader half closed with deployed-plane evidence |
| Report to COO + CTO with verdict + T1.B implication (phase 3) | Sent this window with kill-list path + commit + denominators + CONDITIONAL-YES verdict | **PASS** |

Additional: comp-grep x8 (json/mdpf writers, json/portfolios writers, underscore refs, OWNTS
readers, caller sweeps -- all on-rails, logged); aws primitives under rail-checked markers
(get-bucket-policy, get-function x2, get-function-configuration, s3 listings, secretsmanager
for the T3.A-supplement QA token -- key material deleted in-session).

## MCP traffic

Inbound acted on: COO T3.A supplement 210339Z (deep capture filed @297db6f6bf), CTO RAVC-4
ACCEPT 210534Z, COO VALIDATED 210601Z, CTO T2.A pointer 211314Z (parity fix @a5f3837b10),
AE base clock v1 212449Z (collision answer returned 212626Z: CLEAN with 25-min TTL margin),
COO T5.A GO + live seed 212503Z (ACK 212712Z), COO clock-v2-pending FYI 214101Z, AE base
clock v2 214643Z (vintage stamp updated to reference both declarations). Outbound: 6 messages
(2 ACKs, 2 completion reports, collision answer, T5.A report).

## Blockers

None. T5.A complete pending CTO validation. T3.B staged: bound now ET-anchored 12:15-12:45 ET
per clock v2 @5a20433a5c; activates when the v2 T2.C apply lands.

## Current State (zero-context handoff)

- **T3.A COMPLETE + CTO/COO validated** (@0f71d7d2f9, addendum @297db6f6bf, parity @a5f3837b10).
- **T5.A COMPLETE at this seat** (@this commit): 16-entry kill-list, verdict CONDITIONAL-YES
  {C1 emitter base-read re-source, C2 :567 fix}, T1.B-elimination recommendation with COO.
- **T3.B staged** on the T2.C v2 apply; design inputs = T3.A F1-F4 + CTO's explicit-policy
  reframe + the day-1-new-scope error-caching nuance (carried into v2 s.3 leg-6 per AE base).
- Instrument drift for CVO's register: comp-estate mdpf chain prose asserts a portal_data_proxy
  /aum/aggregate-mdpf frontend route that does not exist on the deployed plane (same stale-prose
  family as its freshness-checker rows).

## Next Steps

1. **[1.0.0_SA_CTO]** T5.A acceptance + the RETIRES-WHOLE ruling call (C1/C2 owners + T1.B
   conditional-eliminate).
2. **[2.0.0_SA_COO]** T1.B hold decision on the verdict; route C1 (AE base + DS) and row-8
   DS-confirm.
3. **[0.7.0_AE_CloudOps~F]** T3.B on the v2 apply; event-driven standby.
