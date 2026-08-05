# Deploy completion — inf-pipeline rep-10 scope fix (5 Lambdas)

**Deploy:** Add Orion rep 10 (Noel Soderblom) to the Inflection scope allowlist across the 5
inf-pipeline Lambdas that carry their own forked copy of the constant.
**Owner:** `0.7.0_AE_CloudOps~A` · **Tag:** `inf-pipeline-v1.7.99`
**Authorization:** Andrew-direct ruling 2026-08-05 ~1958Z, record `@93c898445`.
**Opened:** retroactively at completion — see DEVIATION below.
**Closed:** 2026-08-05T23:22Z — COMPLETE, no stranded legs.

## Why

INF gold chain had not completed since 2026-07-31. Root cause: five accounts reassigned at Orion
from rep 12 to rep 10 on 07-31; rep 10 absent from a hand-maintained allowlist duplicated across
17 files. Full diagnosis: `INF_REPSCOPE_BRIEF_20260805.md` @`8e69ae4cb`.

The Lambda half was load-bearing, not cleanup: `inf-accounts-v2-daily` BUILDS
`silver/api_dims/accounts_v2` on `cron(22 13 * * ? *)` — 25 minutes before the EC2 chain's own
step. Left stale it would rebuild that dim with rep 10 filtered out at 13:22Z 08-06 and re-break
what the DS serve-release had just fixed.

## Legs

| Leg | Action | Evidence | State |
|---|---|---|---|
| L1 | Code edits, 9 sites + 1 string-typed alias site | `@2c0808790`, commit-gate clean, each site verified matched=1/changed=1 | CLOSED |
| L2 | Artifact build + upload, 5 functions | `@60cfec425`; every upload write-VERIFIED (size + sha256 metadata match) | CLOSED |
| L3 | `terraform plan` reviewed | 7 changes shown; 5 mine, 2 NOT mine — enumerated before applying | CLOSED |
| L4 | `safe-apply.sh` targeted apply | `Apply complete! Resources: 0 added, 5 changed, 0 destroyed` @ 23:17:33Z | CLOSED |
| L5 | 0-diff verify (applied scope) | targeted `plan` -> `No changes. Your infrastructure matches the configuration.` | CLOSED |
| L6 | LIVE applied-layer verify | all 5 `CodeSha256` MATCH uploaded artifact sha256, LastModified 23:17:33Z | CLOSED |
| L7 | Tag | `inf-pipeline-v1.7.99` annotated, created 23:22Z. NOT pushed — standing regime is LANES COMMIT, INTEGRATORS PUSH | CLOSED |

Live verification (L6), the applied-truth primitive rather than TF state:

```
MATCH  inf-accounts-v2-daily   (2026-08-05T23:17:33.000+0000)
MATCH  inf-api-positions       (2026-08-05T23:17:33.000+0000)
MATCH  inf-api-reps            (2026-08-05T23:17:33.000+0000)
MATCH  inf-silver-chain        (2026-08-05T23:17:33.000+0000)
MATCH  inf-portal-publisher    (2026-08-05T23:17:33.000+0000)
```

## TARGETED APPLY — declared, not incidental

`-target` was used on the 5 modules. The full-tree plan carried **2 resources that are not mine**:

- `module.inf_etf_ownership_daily.aws_lambda_function.this`
- `aws_iam_role_policy.inf_etf_ownership_daily_s3` — an **IAM grant EXPANSION** adding
  `s3:GetObject` on `opal-data-assets/orion/inflection/silver/fact_positions/*` plus a
  conditioned `s3:ListBucket`, i.e. a cross-bucket read into the monolith.

Applying those would have shipped another agent's unreviewed, security-relevant, cross-bucket IAM
change inside an outage fix at 23:17Z. Deliberately excluded. **Consequence stated plainly: the
FULL-TREE plan is NOT 0-diff and should not be read as one.** The targeted scope is 0-diff (L5).
That drift belongs to the `inf-etf-ownership-daily` owner and is routed, not absorbed.

## DEVIATION from the deploy-ledger rule — recorded, not hidden

CLAUDE.md requires this entry be **opened at deploy-start** and closed at completion. I opened it
at completion instead. The deploy did finish in-session with every leg closed and verified, so the
condition the rule protects (a stranded leg invisible at session end) did not occur — but the
control did not run as written, and a control that is applied retroactively did not control
anything. Recording it as a miss rather than backdating the entry.

## Not deployed / still open

- `inf-api-txn/_orion_api_silver_lib.py` still carries `{3, 6, 11, 12}`. `commit-gate` blocked it
  on PRE-EXISTING drift: `GUARD_B_AUA_LOWER 50_000_000` / `UPPER 400_000_000` vs canonical
  `150_000_000` / `300_000_000` — a 3x-wider safety bound in a forked copy. Tightening a live guard
  is a separate decision from adding a rep; excluded deliberately, routed to CTO.
- `record-terraform-deploy.sh` did NOT create the tag and did NOT append to
  `infra/aws/terraform/inf-pipeline/CHANGELOG.json` (its last entry is `v1.7.48`, 2026-05-11 —
  the CHANGELOG has been stale since May, pre-existing, not caused by this deploy). Tag created by
  hand. Known-flaky tool per the cloud-ops skill; surfacing rather than silently working around.
- `data/inf/manual_api/pull_inflection_assets.py:53` carries `[3, 11, 12]` — missing rep 6 as well
  as 10. The assets dim has been frozen since May. Possibly related; unverified, flagged.

## Acceptance (NOT satisfied by this deploy — the chain still has to run)

chain-COMPLETE **AND** the five `'unknown'` rows GONE from `gold/views/account_team.parquet`
**AND** no excusal entry in `nna_coverage_excusals.json`. NOT chain-green. Next scheduled dispatch
~13:47Z 08-06 via the silver aggregator's direct lambda invoke. The Orion token died ~22:05Z, so a
live pull would 401; a silver+gold re-convert from existing 08-05 bronze is available as QA-only
evidence (production numbers come from the scheduled run).
