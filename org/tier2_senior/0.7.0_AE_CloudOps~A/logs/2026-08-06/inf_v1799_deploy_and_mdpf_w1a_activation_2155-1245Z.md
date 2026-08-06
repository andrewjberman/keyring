# 0.7.0_AE_CloudOps~A — INF v1.7.99 deploy + MDPF_CANRTE W-1a activation legs (2155Z 08-05 -> 1245Z 08-06)

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, COORDINATE

## Summary

Two deploys landed and verified in this window. Neither has passed ACCEPTANCE — both acceptance
runs fire within the hour of this log, and both are consumer-side.

1. **`inf-pipeline-v1.7.99`** — rep 10 (Noel Soderblom) into the Inflection scope allowlist across
   5 Lambdas. Closes the AE half of the 5-day INF gold outage.
2. **MDPF_CANRTE W-1a legs L5+L6** — `aggregate_aua` consumer re-point from served platinum to the
   gold spine. Applied inside a live multi-seat window with `0.4.0_DS_ClientPlatform`.

Prior log: `ba7cfa20b` (2155Z 08-05), which closed with the outage BLOCKED on a serve-hold. That
hold was released by CTO/COO at ~2200-2245Z and everything below follows from it.

## Window

2155Z 2026-08-05 -> 1245Z 2026-08-06. 4 commits, ~20 MCP messages, 2 deploys, 1 tag,
2 deploy-completion ledgers, 1 Andrew-direct ruling relayed into execution.

## Commits

| Hash | What |
|---|---|
| `60cfec425` | artifact rebuild + source map sha256 for the 5 rep-10 Lambdas |
| `79e9a43c9` | INF deploy-completion ledger, CLOSED with a declared deviation |
| `28f7fdd3d` | MDPF W-1a L5+L6 staged (TF edited, plan-verified, NOT applied at commit time) |

Ledger leg closures (via `deploy_ledger.py close-leg`, tool-written not hand-edited): W-1a L5, L6.

## Deployment Sequence + Verification

### Deploy 1 — `inf-pipeline-v1.7.99` (5 Lambdas)

Sequence: code `@2c0808790` -> per-function `build-and-upload.sh` (5x, each write-VERIFIED on
size + sha256 metadata) -> source map commit `@60cfec425` -> `terraform plan` -> **targeted**
`safe-apply.sh` -> 0-diff re-plan -> live hash verify -> tag -> ledger.

```
Apply complete! Resources: 0 added, 5 changed, 0 destroyed          @ 23:17:33Z
targeted plan -> "No changes. Your infrastructure matches the configuration."

LIVE CodeSha256 vs uploaded artifact sha256:
  MATCH  inf-accounts-v2-daily   (2026-08-05T23:17:33.000+0000)
  MATCH  inf-api-positions       (2026-08-05T23:17:33.000+0000)
  MATCH  inf-api-reps            (2026-08-05T23:17:33.000+0000)
  MATCH  inf-silver-chain        (2026-08-05T23:17:33.000+0000)
  MATCH  inf-portal-publisher    (2026-08-05T23:17:33.000+0000)
```

Tag `inf-pipeline-v1.7.99` (annotated, NOT pushed — standing regime is LANES COMMIT, INTEGRATORS
PUSH). Ledger `@79e9a43c9`.

**TARGETED, and the reason is a finding:** the full-tree plan carried **7** changes, 5 mine and 2
foreign — `module.inf_etf_ownership_daily.aws_lambda_function.this` plus
`aws_iam_role_policy.inf_etf_ownership_daily_s3`, the latter an **IAM grant EXPANSION** adding
`s3:GetObject` on `opal-data-assets/orion/inflection/silver/fact_positions/*` and a conditioned
`s3:ListBucket`. Excluded deliberately. **Consequence stated, not buried: the FULL-TREE
inf-pipeline plan is NOT 0-diff and must not be read as one.** Routed to COO (ownership) + CTO
(IAM/arch), split to avoid double-reporting.

### Deploy 2 — MDPF_CANRTE W-1a, legs L5 + L6

Window `mdpf-canrte-w1a-aggregate-aua-repoint`, opened by DS at 0009Z, 4h, 9 legs, single rollback
point. My legs are the two Lambda-env (Terraform) activations. Path COO-ruled 0001Z:
base `gold/mdpf_revamp/_aggregate_aua` on `opal-data-assets` (underscore deliberate — internal,
not served-lineage).

```
L5 opal-assets   -target=module.emitter              0 added / 1 changed / 0 destroyed; re-plan "No changes"
   LIVE: AGGREGATE_PREFIX="gold/mdpf_revamp/_aggregate_aua/"  (WITH slash)
         PLATINUM_BUCKET="opal-data-assets"
L6 mdpf-pipeline -target=module.mdpf_daily_trigger   0 added / 1 changed / 0 destroyed; re-plan "No changes"
   LIVE: PLATINUM_AGG_PREFIX="gold/mdpf_revamp/_aggregate_aua"  (NO slash)
         PLATINUM_BUCKET="opal-data-assets"
```

Key-construction tie-out **EXERCISED, not asserted** — computed with the live literals:

```
emitter :1513 bare concat -> gold/mdpf_revamp/_aggregate_aua/2026-08-05.json
trigger :413  f-string    -> gold/mdpf_revamp/_aggregate_aua/2026-08-05.json
IDENTICAL: True
target key EXISTS 10,100 B   (byte-size-identical to DS's L1 copy control)
NEGATIVE CONTROL: gold/mdpf_revamp/_aggregate_aua2026-08-05.json -> 404 (instrument discriminates)
```

Second tree, same foreign-drift shape: opal-assets plan showed 2 changes, mine plus an undeployed
`aws_iam_role_policy.bd49f_reporting_io`. `-target` excluded. mdpf-pipeline plan was clean (1).

## Findings I authored this window

**Three defects in the W-1a leg spec, all silent in production, all source-confirmed BEFORE staging:**

1. **L6 needed `PLATINUM_BUCKET` too** — spec listed only the prefix. Live env carried NEITHER
   (full denominator: 9 vars); both ran on code defaults `:148-149`. Prefix-only leaves the bucket
   defaulting to `opal-data-portal-v2`, so `:413` head_objects a 404 -> `ROLL_SOURCE_ABSENT` ->
   the per-partner gate DEFERS PERMANENTLY. **A DEFER reads as patience, not as failure.**
2. **The consumers need OPPOSITE trailing-slash conventions.** Emitter `:1513` bare-concats (needs
   `/`); trigger `:413` f-strings (must not have one). DS then widened it: **one WITH, three
   WITHOUT** across four consumers — and the odd one out is the only one whose failure mode is a
   SUCCESSFUL WRITE to a garbage key.
3. **The obvious edit was a trap.** Re-pointing via `local.platinum_bucket` would have looked clean
   and moved served surfaces — that local has **17 references** incl. `mdpf_egress_publisher.tf`
   and `mdpf_portal_publisher.tf` `SERVE_BUCKET`. Used `local.gold_bucket` / `local.gold_mdpf_prefix`.

**Ordering call (DS deferred it to me): L4 before L5/L6.** Riskiest leg first (their deploy path
had already false-PASSed once that night), producer-before-consumer, 12h runway. DS confirmed it
caught a real bug in their protocol — their step 3/4 said "both staged, then fire", and **staged is
not deployed**. Firing on staged would have re-pointed the emitter onto the 439 partitions DS had
just COPIED, which would have read GREEN off stale data. DS's own words: the history copy, which
was necessary and which they argued for, is exactly what would have made that failure silent.

**Acceptance sharpening (carried by DS into L7/L8/L9):** exact-key compare rather than
"a partition exists"; gate PASSES rather than does-not-error; and mine — **the compare must be
against the run_date AFTER the producer next writes**, because `2026-08-05` exists in gold via the
L1 copy regardless of whether the re-point works at all.

## Compiler Tools

| Tool | Target | Result | Note |
|---|---|---|---|
| `comp-trigger` | `inf-gold`, `inf-accounts-v2` | PASS | printed denominator (142 rules + 14 schedules); revealed the accounts-v2 13:22Z cron that set my deploy deadline |
| `commit-gate.sh` | 10 .py | PASS after exclusion | BLOCKED on pre-existing Guard B drift in `inf-api-txn` — the gate working |
| `comp-constants check` | estate | PASS | surfaced remaining `manual_api` drift + the 3 constant aliases |
| `build-and-upload.sh` | 5 functions | PASS | per-function targeting kept blast radius to the fix; each upload write-verified |
| `safe-apply.sh` | 3 applies | PASS | HALTGT checkpoint passed each time |
| `terraform validate` | 2 trees | PASS | caught nothing, ran before both plans |
| `deploy_ledger.py` | 2 ledgers, 2 leg closes | PASS | the tool-written path is what made my L6 correction durable |
| `record-terraform-deploy.sh` | inf-pipeline | **FAIL** | created no tag, appended nothing to CHANGELOG.json |

**What worked:** `comp-trigger`'s live-API framing (DISABLED is a fact, not a verdict) stopped me
concluding the INF chain had no trigger — the real path is a direct lambda invoke from the silver
aggregator, invisible to `list-rules-by-target`. `deploy_ledger.py close-leg` is the reason my L6
spec correction survived when DS's hand-edit of the same record did not.

**What failed:** `record-terraform-deploy.sh` silently did neither of its two jobs (tag created by
hand; `CHANGELOG.json` last entry is still `v1.7.48` from 2026-05-11 — stale since May,
pre-existing). Known-flaky per the cloud-ops skill.

**Gap found:** `deploy_ledger.py` has `open / close-leg / close / hold / check / list` and **no
verb that can amend a leg SPEC or append a log note.** A manifest authored with a defect cannot be
corrected through the sanctioned path — the only writable field on a closed leg is its proof, which
is the wrong field for a spec error. Compounding it, the committed `change_management/*.md` is a
RENDERING of the sentinel: any tool write silently discards hand edits, with no warning at edit or
commit time. DS lost an amendment to exactly this. Routed via DS to COO.

## Blockers

**None on me.** Both deploys are landed and verified on the applied layer.

**Pending verification, correctly not closed:**
- W-1a entry HELD-SOVEREIGN-GATED on the ~13:00Z chain, `open-verify=['L7','L8','L9']`.
- INF acceptance is the 13:47Z scheduled run.

**FINDING routed, not blocking me:** `inf-api-txn/_orion_api_silver_lib.py` still carries
`{3,6,11,12}` and `GUARD_B_AUA` bounds of `50_000_000`/`400_000_000` vs canonical
`150_000_000`/`300_000_000` — a 3x-wider safety bound in a forked copy. Excluded from my commit
rather than silently absorbed; tightening a live guard is a separate decision from adding a rep.

## Current State

- INF: rep 10 live in BOTH trees — DS's scripts on the runner (`code/silver/...` `:630`, deployed
  22:48:54Z) and my 5 Lambdas (`v1.7.99`, 23:17:33Z). `inf-accounts-v2-daily` fires **13:22Z** and
  is the first real exercise of the Lambda half; the INF gold chain fires **~13:47Z** via the
  silver aggregator's direct lambda invoke (all three EventBridge rules read DISABLED — the
  aggregator is the live path).
- MDPF W-1a: L1-L6 CLOSED with proof. Producer writes gold (`code/scripts/gold/mdpf_aggregate_aua.py`
  `:79-80`, deployed 00:29:44Z); both my consumers read gold. Chain fires **~13:00Z**.
- Ledger `.md` L6 SPEC column still reads the defective instruction ("PLATINUM_AGG_PREFIX -> gold");
  the correction lives only in the PROOF column. Re-execution risk reduced, NOT closed — a
  re-executor reads the spec, not an 837-char proof blob.
- Branch ahead of `origin/CLOUD`, UNPUSHED. Tag `inf-pipeline-v1.7.99` local only.

## Next Steps

1. **[0.7.0_AE_CloudOps~A]** Take the acceptance reads as the runs land: `inf-accounts-v2-daily`
   13:22Z, MDPF ~13:00Z, INF chain ~13:47Z. INF bar: chain-COMPLETE **AND** the five `'unknown'`
   rows GONE from `gold/views/account_team.parquet` **AND** no excusal entry. NOT chain-green.
2. **[0.7.0_AE_CloudOps~A + 0.4.0_DS_ClientPlatform]** W-1a L7/L8/L9 consumer-side, compared
   against the run_date AFTER the producer next writes — not against `2026-08-05`.
3. **[1.0.0_SA_CTO]** `inf-api-txn` weakened Guard B; the duplicated-constant lint (accepted).
4. **[2.0.0_SA_COO]** Owner-routing for the two foreign undeployed IAM changes
   (`inf_etf_ownership_daily`, `bd49f_reporting_io`) across two TF roots.
5. **[OPEN, unowned]** The 08-01 NNA AT-RISK register listed 17 accounts and named none of the five
   already filtered out that morning. It is the early-warning surface for that exact class and it
   was silent on the live instance. **It does not close when the chain goes green.**

## Note for whoever reads this next

Four instruments this window reported green over an incomplete action: `safe-deploy` ("all files
deployed and verified", exit 0, over a 2-of-11 skip), `comp-constants index` (its own sanctioned
command deletes its documentation header), the full-tree Terraform plan (clean only if you do not
ask WHOSE changes are in it), and the deploy-ledger `.md` (committed, diffable, cited as the
record, and a rendering). None is a bug in the ordinary sense. All four are the shape that started
this whole thread: a system internally consistent with something that has moved.
