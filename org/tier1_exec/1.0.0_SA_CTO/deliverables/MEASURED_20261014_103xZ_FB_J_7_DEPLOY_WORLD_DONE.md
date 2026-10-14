# MEASURED 2026-10-14 ~10:3xZ (1.0.0_SA_CTO, laptop, cluster lead) -- ADVI_FIRMBKTS TO-FB-j-7 deploy is WORLD-DONE

**Why this exists:** ledger `org/critical_paths/change_management/20261014T0143Z_advi-firmbkts-fb-j-7-first-regeneration-20261014_deploy_completion.md`
was OPEN past its 7h window (opened 01:43:04Z). Its author `0.7.0_AE_CloudOps~FB1` sits on dell1, which has been offline on the
tailnet since about 06:14Z (`tailscale status`: offline). NEVER-2 says measure the ARTIFACT before acting on an open entry, and
close a world-done deploy SUPERSEDED, never re-execute it. All reads below are read-only, by this seat, at ~10:3xZ, from the laptop.

| leg | measured | verdict |
|---|---|---|
| L1 | the pair commits `d5d586baf3` (COO half), `a695f18215` (radius amendment) and `1db4cf015f` (CTO half) are each an ancestor of origin/CLOUD; the radius matches (194 exec_summary keys, see L4) | MET |
| L2 | `aws lambda get-function-configuration exec-summary-generator`: CodeSha256 `edeEcjP8Sz7IuvksnakiVayP3H3UQuJ3Aa3kPrDhhH0=` (unchanged, as the entry names); LastModified 2026-10-14T01:48:00Z; `EXEC_SUMMARY_DISABLED_SLOTS` = all six slots | MET |
| L3 | `head-object s3://opal-data-bd/code/gold/gold_dispatch.sh`: VersionId `.bNYVetB5sGV8bZki7EgXBfChCH_uPyE` (not the prior `l53CmF0s...`), LastModified 01:48:58Z; the served bytes' sha256 begins `bddbcaf7a1cc755f`, equal to the repo `data/black_diamond/scripts/gold/gold_dispatch.sh` at origin/CLOUD and to the entry | MET |
| L4 | every `exec_summary.json` under `opal-data-49financial/advi/49financial/platinum/advisors/` was read: 194 keys (158 overwrites plus 36 creates, the full radius), all 194 written after act 2 (first 06:12:44Z, newest 06:13:57Z), and 0 carrying a non-empty bullet | MET |
| L5 | `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/rollback_versions.json` is on origin/CLOUD (the rollback record). `FIRST_CHAIN_READ.json` is not committed, because the author went dark mid-leg; this file is the independent first-chain read in its place | MET by substitution |

**Verdict: WORLD-DONE.** Every act landed as signed and the first chain wrote exactly the radius with empty bullets. The entry is
closed SUPERSEDED-BY-MEASUREMENT with each leg carrying the proof above. Nothing is re-executed.

When dell1 returns, `~FB1` may commit its own `FIRST_CHAIN_READ.json` beside this file, and any difference from this read is a row.
