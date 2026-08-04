# RCG MIGRATE / layer-refactor spec -- cohort-structured, repaired-ledger population

**Author:** 4.0.0_SA_CRO. **Reviewer:** 1.0.0_SA_CTO~B (cycle-3 protocol). **Ratifier:** Andrew.
**Population basis:** LABELS.jsonl last-row-wins @32d835195 (post label-constant repair):
**MIGRATE = 1,614** (denominator printed at derive; matches the R-0020 recorded ~1,600 + tail).
Binds under the Cycle-4 Execution Policy addendum (same date): knowledge_space only,
ratify-before-execute, cap-100 single-cohort batches, label-vs-warrant validated.

## Cohort A -- vendored-dependency trees inside Lambda source dirs (1,482 files)

| Cohort | Files | Composition |
|---|---|---|
| infra/aws/lambda/infrastructure_monitor | 1,368 | vendored pip site-packages inline: openai 980, pydantic 107, anyio 43, tqdm 34, httpcore 32, httpx 24, remainder misc dist-info |
| infra/aws/lambda/daily_agenda_generator | 114 | `package/` vendored build dir, same class |

**Diagnosis:** Deployment Rule 3 violation class ("dependencies go in Lambda Layers; no
`pip install -t .` into source dirs") committed as tracked source.
**Deploy-coupling (the reason this is NOT a cycle-4 git execution):** the repo tree is the deploy
source for these bundles -- `git rm` of the vendored trees without a layer in place breaks the next
Terraform deploy. Under the policy's execution-plane routing rule, cohort A is **PREPARED HANDOFF,
not RCG execution**:
1. RCG (knowledge-plane, this cycle): derive per-function `requirements.txt` from the vendored
   dist-info METADATA (exact pinned versions, verifiable), inventory the trees, stage the file
   lists + sha256 manifests. No repo mutation.
2. AE lane (0.7.0_AE_CloudOps, normal Terraform cycle, OUTSIDE RCG): build the layer(s) per Rule 3,
   deploy, verify 0-diff, THEN the `git rm` of the vendored trees rides that same change as an
   ordinary lane commit -- at which point the repo move is deploy-verified by construction.
3. RCG closes the labels on the lane commit landing (label close row cites the lane commit).

**Note for the sitting:** infrastructure_monitor is already 0.7.0_AE_CloudOps-owned (2026-07-07
migration record) -- the handoff lands at its existing owner.

## Cohort B -- EC2-side scraper residue (51 files)

infra/aws/ec2/seeking_alpha_scraper: `cookie-env/` (venv artifact, 15) + one-off run/forensic docs
(COOKIE_CAPTURE_GUIDE, DEEP_DIVE_RESULTS, FORENSIC_ANALYSIS, ...). Same routing logic as cohort A
where EC2 pull-paths reference the tree (EC2 code deploys from S3, so coupling is likely absent --
verify per file at derive); the venv artifact is archive-shaped once decoupling is confirmed --
flagged for one cohort verdict at the sitting rather than per-file adjudication.

## Cohort C -- pure knowledge-plane relocations (~81 files) -- CYCLE-4 EXECUTES THESE

docs/architecture 23, org/ref 10, data/analysis 8, docs/briefs 8, data/schwab 6, infra/prompts 4,
lambda strays (portal 4, test_seeking_alpha_unauth 5, market_query 3, news_scanner 3),
org/tier0 2, tools/seeking-alpha-ui 2, data/seeking-alpha 1, docs/reference 1,
infra/aws/secrets/README.md 1.
**Remedy:** `git mv` to the canonical home + citation repair, atomic per-unit commits (move +
repaired citations in one commit), `git show` positive control per moved file, revert = one unit.
Target homes derived per file at batch cut; each batch ratified under the policy before execution.

## Sequencing

1. Cohort C first -- pure git, exercises the cycle-4 mechanics at lowest risk (cap-100 batches).
2. Cohort A prep artifacts (requirements derivation + manifests) in parallel -- no repo mutation.
3. Cohort A/B handoffs dispatch on Andrew's ratification of this spec; label closes follow the
   lane commits.

## What this spec does NOT do

No layer builds, no deploys, no AWS mutations, no `git rm` of anything deploy-coupled -- those are
lane work under lane law, outside RCG, per the scope lock. RCG's deliverable is the labeled truth,
the prepared handoff, and the pure-git relocations.
