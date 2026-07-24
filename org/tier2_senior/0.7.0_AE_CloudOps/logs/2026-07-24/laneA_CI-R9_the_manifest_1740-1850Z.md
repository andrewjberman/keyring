# 0.7.0_AE_CloudOps~A — CI-R9 row 9: THE MANIFEST, the only failure surface

**archetype:** IMPLEMENT

**Session:** 2026-07-24 17:23Z–18:50Z · lane `~A` (fresh) · TO `MDPF_CHANNEL_INDEPENDENCE.CI-R9`
**Authorization:** Andrew-direct ~1720Z *"Go now, this is P0."* via COO GO @174040Z.
**Landed:** `f030ac80d` (build) + `b57ca6fcb` (convergence + validator fix) — **committed, NOT pushed**
(Tier-1 push only, Andrew ~1600Z; COO is push operator).

---

## What was delivered

| Artifact | Purpose |
|---|---|
| `infra/aws/lambda/mdpf-manifest/mdpf_manifest.py` | build + validate + immutably write. stdlib + boto3, no pandas, so the EC2 gold-runner and the future C3 Lambda import the same code |
| `infra/aws/lambda/mdpf-manifest/emit_manifest.py` | observes live channel state; CLI **and** `lambda_handler` |
| `infra/aws/lambda/mdpf-manifest/tests/test_mdpf_manifest.py` | **72 checks, 20 mutants + 6 constructor refusals**, no AWS |
| `infra/aws/lambda/mdpf-manifest/README.md` | schema + the AC-5 interface contract with the base lane |

**Row 9 mechanisms, each with a mutant proving it fires** — §3.1 r1 (`data_as_of` from the data:
`derive_data_as_of()` is the only constructor and accepts no bare date and no process time),
§3.1 r2 (two independent detectors — by NAME for a date-only `generated_at`, by VALUE for an
innocently-named key holding a clock; either alone is evadable), §3.1 r3 (UNKNOWN excluded from the
spread **and forcing signal**), §3.2 (`If-None-Match: *`, so a re-used `run_id` is refused **by S3
with a 412**, not by our politeness), the **third state** (`published | skipped | carried_forward`,
where the label cannot be claimed without its evidence), and `run_class` production|qa enforced
twice — validated field **and** a writer that refuses a QA record into the production prefix.

**Exercised live, not config-read:** healthy **0/0/0 no signal** on real frontiers (49F 07-23 /
INF 07-23 / COT 07-22 — a raw metric reads 0/1/2 here and fires on a healthy estate); the AC-2
constructed run with `skipped=1 carried_forward=1` built from a **real** older partition; the
immutability refusal with its positive control run as a **separate** invocation; and the QA→production
prefix refusal. All writes went to `gold/mdpf/_manifests_qa/`.

---

## The three things I would want a successor to read

**1. My own suite reported 57/57 while two of its rules were untested.**
Two mutants were killed by the **divergence recomputation** rather than by the disposition rule and
the skipped-entry rule they were written to test. Both rules were reported green and were in fact
unexercised. I fixed it structurally rather than by hand: `mutate()` now requires the intended
violation string to appear, so **a mutant killed by an unrelated assertion FAILS**. *A suite that
cannot tell which assertion fired is measuring its own optimism.*

**2. My validator would have REJECTED A CORRECT MANIFEST, and only a constructed case found it.**
A channel's lag is the **MAX over its feeds** (the worst feed); its `actual_frontier` is the **MIN**
over their as-ofs (the stalest). I recomputed the channel lag from the frontier **pair**, which is a
different quantity. Measured: cottonwood with its same-day roster feed 3 trading days stale beside
two D+2 feeds exactly at their own frontier → max-over-feeds **3**, frontier-pair **1**. It read
green all session **only because every real channel's feeds happened to be aligned that day.**
*A rigorous instrument on the wrong axis survives review.* And the fix then **silently dropped an
invariant** — two mutants that had been dying immediately survived, because the lag check no longer
reached `actual_frontier`. Added explicitly: `actual_frontier`/`data_as_of` must equal the min over
measurable feeds. **A recomputation that no longer reaches the underlying evidence is not a
recomputation.**

**3. I shipped a roster I should not have owned, and the reason it had to go is not "theirs landed
first."** I built a roster seed so the manifest could emit before row 7 existed. `~B` landed the real
one (`fd6e92faa`) — and **my seed carried `inflection value_effective_from: "existing"`**, the exact
PRD §2.6 value CTO had already amended to 2026-05-15 (`f642948889`). **My seed was the stale
definition, and an effective date is silent when wrong — no failing test, the alarm simply never
fires.** Deleted; `load_roster()` now reads `data/mdpf/config/partner_roster.json` through
`mdpf_roster`, and lag/divergence come from that module rather than a second implementation.

---

## A finding I reported rather than worked around

`mdpf_roster.divergence()` @`fd6e92faa` left **`signal: False` for a channel whose every feed was
unmeasurable** — lag `None`, excluded from the spread, nothing folding it back in. **A dark channel
read as a healthy estate**, on the only failure surface the estate has (no SES, no alarms). Its own
`channel_lags` docstring stated the principle correctly (*"an unknown rendered as 0 is the shape that
lets a frozen channel read healthy"*); the roll-up one layer up did not honour it.

Reproduced before reporting (20260724T182648Z). `~B` reproduced, found it **worse** than I measured
(all three channels dark also read `False`), and **fixed it upstream @`9f0214122`** with an
`unmeasured-channel` limb + `signal_reasons`. My interim overlay — labelled on the face of the record
and explicitly disposable — was **deleted the same session**. The limb belongs in the roster module.

The cross-check stays: `_cross_check_divergence()` **raises** if the two implementations disagree on
arithmetic. *Two independently written implementations agreeing is a real check; one agreeing with
itself is not.*

---

## Measured en route, surfaced not adjudicated

`blackdiamond/cottonwood/silver/fact_allocations_s2` and `fact_unrealized_s2` each have **ten
partitions (07-13..07-22) written within ONE MINUTE on 07-23** — a backfill. Content `_source_as_of`
agrees with the partition date, so it reconciles the "cot allocations frozen since 07-17" record
rather than contradicting it. **Invisible to any freshness check reading only the newest partition
date; visible in `write_lag_trading_days`.** `~B` is adding a per-feed backfill discriminator to the
roster; I keep emitting the raw measurement as provenance. One measures, one interprets — no
duplication.

Also noted, not fixed (not my lane): `portal-auth/cloudfront-distribution.tf` says "9 FE-read paths"
three times in comments while `mdpf_assets_behavior_paths` enumerates **11**.

---

## Two items surfaced to CTO's gate, neither blocking

1. **§3 vs §3.1 contradict.** §3 sketches a top-level `run_at`; §3.1 r2 binds *"no bare timestamp
   fields anywhere."* Latest-and-most-restrictive binds → `run_at` under `process_time`, zero bare
   timestamps at any level. Reverses on a ruling.
2. **I deviated from "colocated".** Manifests default to `gold/mdpf/_manifests/`, not the served
   prefix. Grounded: `opal-data-assets` is CDN-reachable only via exact-path behaviors + an exact-key
   bucket policy (`AllowMdpfPortalCloudFrontOACRead`), whereas `opal-data-portal-v2` carries a
   catch-all `/*`. A manifest names buckets, keys, ETags and per-firm lags. **Bucket and prefix are
   configuration**, so either ruling is an env change, not a rewrite.

---

## Not claimed

- **AC-1 is NOT met.** The bar is a named reader who has not traced S3 explaining the state from the
  manifest alone. **My own assessment does not count, and briefing the reader first would measure the
  briefing.** COO is routing one. To help without contaminating the test, the manifest opens with a
  **derived** plain-English `headline` that the validator recomputes — a hand-written summary would be
  a second source of truth.
- **No IAM verified.** No Lambda role exists yet; the wiring lane owns it. I did not run `comp-iam`
  and report a GREEN in its place — it models `(action)`, never `(action, resource)`, and would report
  GRANTED for a bucket the role cannot touch.
- **Nothing deployed, nothing pushed.**

---

## Compiler Tools

| Tool | Command | Result | Value |
|---|---|---|---|
| `comp-which` | `comp-which "where does the MDPF platinum publisher lambda write its served artifacts and what triggers it"` | routed to `comp-trigger` / `comp-routes` / `comp-platinum` | PASS — routed, though the answer came from `pipescript` |
| `pipescript` | `pipescript mdpf` | 2 threads, producers + served keys + frontend | **PASS, and its own VINTAGE WARNING earned itself** — the snapshot is 39d old and flagged the mdpf platinum key as changed 07-23; I grounded every load-bearing key on live S3 rather than the snapshot |
| `comp-routes` | `comp-routes trace platinum/mdpf` | `No match` + full COVERAGE/BLIND disclosure | PASS — the honest miss sent me to the Terraform, which is where the exact-path behavior list and the OAC bucket-policy scoping actually live |
| `comp-grep` | roster/manifest pre-existence sweep | 0 matches in 3162 files scanned | PASS — and it **warned me my `\|` alternation was literal**, which would have made a 0 an artifact of my regex rather than a real absence |
| `comp-surface-check` | auto in `safe-commit` ×2 | OK, no critical surface | PASS |
| `comp-pulse` | auto in `safe-commit` ×2 | REFLEX CLEAN, denominator 6/5 files vs 1511 danger nodes | PASS — denominator printed |
| `commit-gate.sh` | 3 `.py` files ×2 | all checks passed | PASS |
| `comp-to` | `comp-to MDPF_CHANNEL_INDEPENDENCE.CI-R9` | session TO_ID set race-free | PASS |
| `comp-iam` | **NOT RUN, deliberately** | — | There is no Lambda and no role yet — the wiring lane owns both. Running it would have produced a GREEN about a role that does not exist, and `comp-iam` models `(action)` not `(action, resource)` so it fails GREEN on exactly this shape. Recorded as NOT-RUN rather than reported as a pass. |

**Gap for CTO:** no comp tool answers *"which S3 prefixes of this bucket are reachable through
CloudFront, and under what policy?"* — the question that decided where manifests are written. I
answered it by reading `cloudfront-distribution.tf` plus the bucket-policy statement name by hand.
`comp-routes trace` correctly declared itself blind here rather than guessing, which is the right
behaviour, but the coverage gap is real and it is a security-adjacent question.
