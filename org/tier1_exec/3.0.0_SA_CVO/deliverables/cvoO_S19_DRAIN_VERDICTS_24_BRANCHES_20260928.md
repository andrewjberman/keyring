# S19 post-purge drain: a verdict per branch for the 24 (section 6 of the MSTR~Z state doc)

Adjudicator: `3.0.0_SA_CVO~O`, on `0.0.0_AB_MSTR~Z`'s ask (file 20260928T172853Z) under Andrew's hold. Recorded
2026-09-28 ~17:5xZ. State doc: `org/tier0_exec/0.0.0_AB_MSTR/deliverables/mstrZ_S19_POSTPURGE_DRAIN_STATE_AND_PROPOSAL_20260928.md`
@f10abae456.

**Totals: SUPERSEDE 17, LAND 3 (one of them records only), HOLD 4.** None is to be `git merge`d; each LAND is by
cherry-pick (state doc section 3).

## Method (read-only; it ran against local `CLOUD` @f2a7ff8252, the pre-rewrite trunk)

- **Per branch:** the files that `CLOUD..<branch>` touched, and whether the tip's blob equals CLOUD's.
- **Per commit:**
  - Does CLOUD carry a commit with the same subject since 2026-09-10?
  - What share of the commit's added lines (non-blank, over 3 characters) appear verbatim in CLOUD's current file?
- **For the high-presence family:** every residual line was listed by file and checked against the trunk.
- **Order state:** each order read from its first line-anchored `<status>` at CLOUD.
- **Scripts** (session scratchpad): drain_scan.py, drain_scan2.py, drain_resid.py.
- **Limit:** verbatim line presence is a heuristic. A line the trunk re-indented or rephrased reads as absent, so
  "present %" is a floor.

## SUPERSEDE (17): the content is on the trunk, or the order it served completed another way

| branch | evidence |
|---|---|
| `rel-nfra-oplgtw-sprint-owner` | 99.0% of 4,200 added lines on trunk; 5 of 13 subjects verbatim on trunk |
| `rel-nfra-oplgtw-email-deny` | 99.0% of 4,198; 5 of 12 subjects |
| `rel-nfra-mcpindex-r2-gateway` | 98.8% of 3,719; 5 of 11 |
| `rel-nfra-opalai-portal-grant-gateway` | 97.8% of 1,943; 5 of 10 |
| `rb-nfra-mcpindex-r2-base` | 97.8% of 1,943; 5 of 10 |
| `rel-nfra-opalai-zs18-gateway` | 97.6% of 1,595; 5 of 9 |
| `rb-nfra-opalai-portal-grant-base` | 97.6% of 1,595; 5 of 9 |
| `rb-nfra-opalai-zs18-base` | 97.3% of 1,419; 5 of 8 |
| `rel-nfra-mcportal-r2-gateway-2` | 98.3% of 1,265 |
| `rel-nfra-mcportal-r2-gateway` | 98.3% of 1,258 |
| `rel-nfra-opalai-r1-gateway` | 99.4% of 338 (one release-cut commit f1f0fc6780) |

**The gateway/base residual, examined.** The same 2 to 43 lines recur across all 11 branches, because they are one
stacked series. They sit in:
- `opal-gateway/app/owner_gate.py`, `tools.py` and `tests/test_admin_round2.py`;
- `EC2_MANIFEST.json` timestamps;
- one line each in `admin_grants.py`, `deploy-to-ec2.sh`, `asker_scope.py` and `data_entitlement.py`.

The trunk rewrote those spots later:
- `owner_gate.py` was last changed on the trunk by b2fb5c6adb.
- `read_chat_message_images`, `planted_name` and the `OA-t-5` entries all exist at CLOUD in their later form.

Nothing unique to these branches is left.

| branch | evidence |
|---|---|
| `wk-amgt-13-26` | rk-19 producer half. TO-AMGT-rk-19 (both files) is complete on the trunk (7aef98df54, cc1433fa8a) |
| `wk-amgt-13-27` | rk-19 adapter half, `wip`. Same completed orders |
| `wk-amgt-13-28` | rk-21. TO-AMGT-rk-21 is complete on the trunk (1b18a89f03). This branch's build is 1.2% present: the trunk carries a DIFFERENT implementation, and this is the losing variant |
| `wk-amgt-13-29` | rk-30 producer half. rk-30 is complete on the trunk (5b767811e7, 98672e1c57) |
| `wk-amgt-13-29-sp` | the same rk-30 producer half, a split-off; the same completed orders |
| `wk-amgt-13-30` | `criteria_quality_checker` shape6. It landed on the trunk as c9816ba669 (the same worker, rk-28) |

## LAND (3): by cherry-pick; content absent from the trunk and worth keeping

| branch | what lands | note |
|---|---|---|
| `cvo-z-harvst-l4r` | 3 commits: `3.0.0_SA_CVO~Z`'s L4-R REFUSAL of AMGT_HARVST v0.2 @c19ef6cd and its HOLD-cutover review. 0% on trunk; records only | Records of a signing seat's refusal are part of the sign-off history. No conflict risk |
| `closer/amgt-r-20260923` | 12 commits, `4.0.0_SA_CRO~Z`: `deliverables/AMGT_COO_SPLIT_PROPOSAL_20260923/` and `AMGT_R_CLOSER_20260923/` (reviews, measurements, their scripts). 0% on trunk | 20 of 21 files are absent on the trunk and 1 differs; resolve that one at the pick |
| `wk-amgt-14-50` | **RECORDS ONLY:** `change_management/20260919T1433Z_amgt-rk49-lusha-enrich_deploy_completion.md`, the worker's proof/session-log deliverables and its surprise row | The CODE (`lib/research/management/*`) is SUPERSEDED: TO-AMGT-rk-49 is WITHDRAWN (@85a05bd6ab). **Do not land `.open_deploys/amgt-rk49-lusha-enrich.json` in an OPEN state:** read the tip's ledger first (an AC3 live write was attempted, and the ledger records it). Re-append the surprise row instead of picking the shared channel file |

## HOLD (4)

| branch | why, and who releases it |
|---|---|
| `closer/amgt-experience-z-20260923` | Pre-marked. Its standing instruction is: do not merge the tip without explicit word. **Andrew** |
| `closer/amgt-h-y-20260923` | 23 commits of CODE and docs (Price caller migration, daily-score retention), 13% on trunk, including a merge from the retired SITEZ trunk. Whether later AMGT work superseded it is a code judgement, not a verifier's. **Its owner `2.0.0_SA_COO~Y`**, or Andrew if that seat stays down |
| `wk-NFRA_OPALAI-1` | OA-t-1 (product files moved into opal_ai; gitlink advance). The order was superseded today (@4ce47993e4) pending **Andrew's G-ACCT / G-AUTH / G-PUSH**. Its content must not land before that cutover; the round-2 re-cut starts from it |
| `wk-NFRA_OPALAI-3` | OA-t-3 (runtime setup; hook removal). Same gates, same reason |

## Not covered here

- The 52 worktrees' 121 uncommitted files. They are not branch content, and their owners' `reset --mixed` keeps them
  (state doc section 5).
- Any branch outside the 24.

-- 3.0.0_SA_CVO~O
