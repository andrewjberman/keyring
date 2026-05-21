---
name: verify-channel
description: Independent data-pipeline verification. Confirms a pipeline / gold-script / S3 artifact / repair actually DELIVERS fresh, usable data by reading actual S3/DynamoDB/artifact state — never the producer's self-report, the cron/SSM config, a "rc=0" log, or a task marked complete. Enforces the 4-check method (EXISTS/FRESH/SCALED/NOT-FROZEN), verifier != fixer, sharpest-test-binds, and a final decision-useful meta-gate. Trigger: any audit -> repair -> re-verify cycle, a proactive sweep of "done"/GREEN items, or a RAVC4 / project close-out adequacy check. Adapted for ajb_workspace from corporeal's verify-channel skill. Core bar: "the pipeline pulls data AND the data is fresh and usable — not merely that crons/chains fire."
---

# /verify-channel

Independently verifies that a data pipeline (a gold/silver/bronze script, a Lambda, a portal/platinum artifact, a DynamoDB-backed surface) — or a repair to one — **delivers fresh, usable data**, by inspecting the actual artifact, not any claim about it. This is the codification of the independent-verification layer behind RAVC4 acceptance and `comp-validate`.

## When to invoke

- **Re-verify a repair**: an agent RAVC2'd a fix; confirm it holds before it counts toward close-out.
- **Field-audit a pipeline**: confirm a "fixed"/passing surface is genuinely delivering.
- **Proactive sweep of the done set**: adversarially re-check items marked complete — a completed TO is a claim, not evidence (Step 0).
- **Close-out adequacy input**: feeding a project-closure verdict — each surface enters as UNVERIFIED until this skill confirms it.

## Core principle

The bar is **"the pipeline pulls data AND the data is fresh and usable — not merely that the cron / SSM chain / Lambda fired."** The recurring failure mode this skill exists to catch is **config-OK != delivering**: a cron ENABLED, an SSM chain `exit=0`, a partition existing, a `status: ok` log, a TO marked `complete` — none of them prove fresh, usable data landed. (Anchors in ajb doctrine: `[[feedback-ship-attestation-vs-deploy-attestation-distinct]]` — a commit/RAVC-request is not proof the runtime changed; `[[feedback-s3-pull-dispatcher-no-auto-propagate]]` — a push to CLOUD does not mean the runner runs that code; the 2026-05-20 INFGRO rebuild — a "verbatim trigger" that fired `exit=0` but ran append-only and re-materialized nothing.)

Four non-negotiable rules:

1. **Verifier != fixer.** The agent who made (or will make) the repair never verifies it. If asked to verify your own work, refuse and route to a third agent.
2. **Read the artifact, never the self-report.** Inspect actual S3 / parquet / DynamoDB / platinum-JSON state with your own read. A producer's "ran fine, N rows" is not evidence.
3. **Sharpest-test-binds.** When a coarse check PASSes and a sharp check CONCERNs, the CONCERN binds. A coarse-PASS that misses a sharp defect launders a bad repair into a clean verdict.
4. **Decision-useful != mechanically-delivered.** Fresh + scaled + non-frozen + structurally-non-degenerate is necessary, NOT sufficient. The final and highest gate (Step 3.5) is whether the output is actually *decision-useful and meaningful for its consumer*. Verification never concludes on a mechanical/structural pass alone.

## Step 0 — "Complete" / GREEN is a claim, not evidence

A TO marked `complete` is NOT proof. A completed fix can break a *different* artifact two ways — (a) regress it, or (b) be entirely CORRECT yet amplify a pre-existing latent defect to critical scale. A scale-jump on a completed fix is itself a trigger to re-check cardinality even when the fix is right. Every completed/GREEN surface enters verification as UNVERIFIED. The proactive adversarial sweep of the done set is loop-essential, not optional. See `[[feedback-identity1-masks-absolute-value-class]]` — a gate can PASS to-the-cent while the per-component values are wrong.

## Step 1 — Identify the pipeline's actual delivery contract

For the target surface, establish from code/config (not assumption):
- The S3 key / DynamoDB table / platinum-JSON path the **consumer** reads (often the `latest/` promoted path, not the dated partition the producer writes — verify the one consumers actually resolve). `comp-platinum reverse <key>` and `comp-pipescript consumers <script>` resolve this.
- The cadence + expected landing time, in **UTC** (crons + SSM are UTC).
- The expected scale (rows / bytes) from recent good runs.
- For a repair re-verify: the commit, what it claims to change, and whether its output was actually **run to the consumer path**. A committed fix not executed to S3 is NOT deployed; a script pushed to CLOUD but not `aws s3 cp`'d to the runner's code path is NOT what runs (`[[feedback-s3-pull-dispatcher-no-auto-propagate]]`). `comp-pipescript deployed <script>` gives MATCH/STALE/MISSING.

## Step 2 — The 4-check method (run all four; existence alone is never sufficient)

| Check | Question | Method | Failure |
|---|---|---|---|
| **EXISTS** | Is the latest expected partition/object present at the consumer path? | `aws s3api head-object` (UTC LastModified) / DynamoDB query | absent |
| **FRESH** | Is its write recent on cadence, AND does any freshness stamp reflect real data recency (not write-time, not an unconditional `CURRENT_DATE`)? | head-object UTC + inspect the freshness column vs the underlying data vintage | stale / dishonest stamp |
| **SCALED** | Is row/byte count in-family with recent runs (max-of-N prior; reject < ~50%)? | independent `COUNT(*)` / ContentLength vs baseline | partial run |
| **NOT-FROZEN** | Is content genuinely different from the prior partition? | **ETag / content-hash**, NOT size (byte-identical size with a distinct ETag = real new content; size-only false-positives) | stale-duplicate |

For overwrite-in-place single artifacts (no dated history): SCALED's "max-of-N prior runs" is N/A — use PARITY vs the grain it should match instead. Don't manufacture a check that doesn't apply; say so. ajb note: `comp-validate <script> --artifact <file>` runs a config-driven battery of these for gold scripts — use it where a validate config exists; it does not replace your own artifact read.

## Step 2.5 — The sharp structural test (mandatory for join / aggregate / cohort data)

Coarse guards (existence, headline counts, cross-group spread) are necessary but NOT sufficient. Ask: **"what is the strongest degeneracy this data could still have that my coarse test would NOT catch?"** and test THAT.

- **Aggregate-identity masking**: an `aggregate == sum(parts)` reconciliation can PASS to-the-cent while per-component values are wrong — a residual component silently absorbs whatever leaks from the others. PASS = "internally consistent," NOT "values correct." Detect via a per-component series-walk + day-over-day plausibility, not the identity gate. (`[[feedback-identity1-masks-absolute-value-class]]`.)
- **Join degeneracy**: a join can return exact headline counts while being a near-cartesian — test the within-group completeness ratio, not just the total.
- **Freshness-stamp honesty**: for every row stamped "fresh today", is its payload provably NOT byte-identical to the last frozen snapshot? Zero today-but-frozen rows is the bar; "the distribution looks mixed" is not.
- **Dead-column class**: when a column is reported uniform-constant / all-0 / all-NULL while its rows EXIST and are fresh, do NOT scope the check to the reported column — scope it to the CLASS via the structural boundary that separates dead from live (usually a semantic subfamily — e.g. current-window metrics dead while cumulative metrics on the same rows are live, the signature of a point-in-time join landing on an empty period). Enumerate every column on the dead side across all artifacts sharing the lineage; per-column assert distinct >> 1. A representative-column check FALSELY PASSES the class.
  - **Broken-compute vs absent-data discriminator**: before concluding "data is missing", check whether a SIBLING family on the SAME rows is richly populated. If the sibling is rich, the data is present — the defect is a broken computation, not absent input.
  - **Cascade**: a dead base metric propagates into everything derived from it (percentiles, scores, rollups) — they go uniform-constant even though their own producer "ran fine". Add every derived artifact in the lineage to the checklist; for derived scores, "non-degenerate" means *genuinely discriminating*, not merely distinct > 1.

## Step 3 — Timing & timezone discipline

Two false-positive classes:
- `aws s3 ls` renders LastModified in **host-LOCAL** tz; crons are UTC. Use `aws s3api head-object` (UTC ISO8601) or normalize.
- Checking **before** the expected landing time is a true-but-transient absence = a false RED. Sample only **after** expected_landing + a cadence-variance margin. "Absent now" is a stall only if `now > expected_landing + margin`.

## Step 3.5 — Meta-analysis: decision-useful & meaningful (the FINAL gate — runs last, binds the verdict)

Everything above confirms the pipeline **mechanically delivers** fresh, scaled, non-frozen, structurally-non-degenerate data. That is necessary and NOT sufficient. The final question — implied by none of the above — is: **is the output actually decision-useful and meaningful for the thing that consumes it (the portal surface, the leaderboard, the partner-facing report), or is it mechanically churning?** Run this LAST, every verify; it binds the verdict.

Three sub-checks, in order:
1. **Gate-coverage honesty.** Does the structural gate (Step 2.5) even *structurally cover this artifact's class*? Score-/model-/embedding-derived and continuous-weight classes are routinely outside exact-match / cardinality-ratio gates by construction. If so, a clean Step-2.5 PASS is **zero evidence** of meaningfulness — state that scope-honestly.
2. **Quality-erosion under completion-pressure.** Did a multi-iteration "make it pass / faster / fit the window" arc quietly slash quality knobs (a lookback window, a sample size, a K, a tolerance band) "for speed"? Completion-pressure trades meaning for throughput while every status stays GREEN. If yes, the completion bar itself may be the defect.
3. **Consumed-output meaning probe.** (i) Run-to-run stability of the *consumed* output (the decision artifact's set/assignment stability — top-K membership, cohort labels, the rendered number's day-over-day plausibility — NOT raw scores that are scale non-identifiable). (ii) Structural sanity vs a baseline — does the output discriminate, or is it ~constant noise on a meaningful-sounding name?

Discipline for this step:
- **Honest-limit.** A structural assessment is not an empirical measurement. Assert only what is rigorously assertable; name the empirical probe as the next step — do not claim you ran it. If a probe has a real obstacle (overwrite-in-place precludes run-to-run comparison; a 2nd run would make you the producer-not-verifier), surface it as an honest-limit DEFERRED — never fake it, never silently drop it.
- **Verifier != fixer (still binds).** This step validates meaning; it never restores eroded quality params. Probe-FAIL => STOP + surface.

## Step 4 — Verdict + routing (STOP, do not repair)

A verifier never fixes — finding the defect IS the deliverable; route it.

- **PASS** — all 4 checks + the sharp structural test clean AND Step 3.5 cleared (meaning probe passed OR the meaning axis explicitly scoped-out with a stated honest-limit + routed as a distinct open axis). State the checks + actual numbers, not "looks fine." A mechanical PASS with an unaddressed Step-3.5 gap is NOT a PASS — it is PASS-mechanical + CONCERN-meaning, two axes, never collapsed.
- **CONCERN** — any check fails, OR the fix is committed-but-not-deployed, OR the artifact is confounded by degraded upstream, OR Step 3.5 surfaces a meaning gap. Do NOT pass. Specify exactly what, with the sharp evidence; tag the axis (mechanical/structural vs meaning).
- **CONDITIONAL** — the repair cannot be verified until a prerequisite lands. State the explicit sequence: prerequisite -> deploy-to-S3 -> re-verify.

Routing: PASS/CONCERN/CONDITIONAL -> the requesting exec (COO for TO-scope / close-out; CTO for an architectural call). If still-broken, STOP — do NOT fix it (that is the owner's lane, and verifier != fixer); RAVC2 the specific finding and let the exec route the repair. When two independent verifies disagree, the sharper-test verdict binds — never average, never treat a coarse PASS as exoneration.

## Step 5 — Feed the close-out

For a project-closure / RAVC4 adequacy verdict: each surface carries **two axes** — `mechanically-delivers {VERIFIED-fresh-and-usable | CONCERN | CONDITIONAL}` AND `decision-useful {VERIFIED-meaningful | CONCERN-meaning | UNTESTED-meaning(honest-limit, routed)}`. A surface is not closeable on the mechanical axis alone. Reopen/annotate any completed TO a sweep regresses; the item stays OPEN until independently re-confirmed on **both** axes. A close-out that rests on the completed-TO list, or on the mechanical axis while the meaning axis is silently assumed, is invalid.

## Relationship to ajb compiler tools

`comp-validate` (gold-script artifact battery), `comp-pipescript deployed` (runner-has-your-code MATCH/STALE), `comp-pipescript postdeps` (required post-steps), `comp-platinum reverse` (artifact -> portal consumer) are ajb's native pipeline-verification tooling — use them as inputs. They are necessary, not sufficient: they check config + structure; verify-channel adds the independent artifact read, the sharp structural test, and the decision-useful meta-gate that no tool implies.

## Configuration

No state file — verify-channel is event-driven (invoked per audit/repair/sweep/close-out item), not interval-triggered. Verifier assignment is the requesting exec's call, constrained by rule 1 (verifier != fixer).
