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

---

# ADDENDUM 1850Z-1905Z — the re-brief, and a fourth instrument failure of my own

**Landed:** `7f9ece9df` (dedupe) · `efac7d6aa` (lineage) · `1efeffa50` (declare_input + stated
denominator). Tests 72 -> **99**.

## The governing objective changed mid-session
Andrew ~1832Z: *"the entire point of all of this is migrating MDPF to the monolith
opal-data-assets lineage, ENTIRELY... Is there any information that conflicts that or paths which
are not coming from the monolith lineage?"* CTO's instruction for this lane (PRD `6b69efc57`):
**record the LINEAGE of each input in provenance.** Done in the same session it arrived, because
it is a field addition now and a rebuild later.

Lineage is classified **from the bucket and prefix actually READ at run time, never from a name** —
COO's sharpening is the reason: `mdpf-daily-trigger:535` still computes `all_fresh` under
*"retained for log continuity"*, **a symbol that outlived its mechanism**, so under a migration
"grep found the name" is evidence in neither direction.

Hardened beyond the instruction: a key on `opal-data-assets` but **off the grammar** classifies
`non_monolith` with the reason stated. *"It is in opal-data-assets"* and *"it is monolith lineage"*
are different claims; collapsing them reports the migration complete early.

## THE FOURTH FAILURE, and it is the same one the PRD exists to prevent
The rollup, computed over roster-declared channel feeds, reported **`all_monolith: true`**.
**Correct arithmetic. False impression.** None of the four confirmed non-monolith paths is a roster
feed — M1 the BD freshness gate (*the path that caused the six-day freeze*), M2 the self-referential
`opal-data-portal-v2` count import, M3 `opal-data-mdpf` code, M4 the `opal-data-inf` Door-6 trigger.
**The field I had just built to expose them reported clean while all four were live.**

Fixed two ways: the rollup **states its own denominator in the record**, and `declare_input()` lets a
publisher pass its real reads into the same classifier. Verified by **positive control** — all four
classify NON_MONOLITH *and* a real monolith path still classifies MONOLITH in the same run, so the
classifier is shown to **discriminate** rather than to refuse everything.

**Measured, denominator attached: 8 of 8 ROSTER-DECLARED silver feeds are on the monolith lineage.
That is not "MDPF is on the monolith", and I asked CTO not to let it be relayed as such.**

## `dedupe`, for the wiring lane
`process_time.dedupe`. Their reasoning was exact: with a deterministic run_id, a broken stream
delivering ONE event is byte-identical in the record to healthy convergence across forty. **I kept
what I can measure apart from what I cannot** — `run_id_basis` is measured here; the counters
cannot be, because the invocations that converge are exactly the ones that never write. They are
caller-supplied and default to **null**, and the field states that **null means NOT INSTRUMENTED
and must never be read as 1.** A plausible fabricated `1` would have made the field worse than absent.

## What my CTO ruling-2 note gained
COO supplied the argument I did not have: `opal-data-portal-v2` **is M2, a lineage being retired.**
Colocating the manifest there would have written a new artifact — the §3.2 history, the one thing
that must survive to show a multi-day freeze — **into a path scheduled for deletion.** The CDN
reasoning was the weaker half of my own case.

## Running tally of my own instruments that were green while wrong
1. Mutants killed by the wrong assertion (2 rules reported green, both untested).
2. A validator that would have **rejected a correct manifest** (lag is max-over-feeds; I recomputed
   from the frontier pair — green only because every real channel's feeds happened to align).
3. That fix silently **dropped an invariant** (two previously-dying mutants survived).
4. A lineage rollup that was **arithmetically right and materially misleading** for want of a
   denominator.
**Every one was caught by a control failing. None by care.**

---

# ADDENDUM 2 · 1905Z-1940Z — CVO's blind read, the accuracy hold, and an OPEN finding against my own instrument

**Landed:** `a42ec98dc` (M5 discriminating-pair control) · `84a219d2e` (the three-symptom fix). Tests **112**.
All commits pushed by COO.

## AC-1: CVO read it cold and went past the question
*"Read cold. No context asked for, nothing else consulted before answering."* They produced the three
dispositions, the normalised divergence, and then the sharper answer: **"it was not a channel, it was one feed
inside one"** — SmartX legs at today, Schwab RPS behind. Their attribution: *"the per-feed breakdown is what
made the sharper answer possible."* Verdict: **sufficient for what/where, not for root cause** — a boundary
they drew themselves, unprompted.

## COO held his own closure, and was right to
He measured both candidate Schwab prefixes at 07-23 and could not reconcile the 07-14. Two branches: **(A)**
the per-feed lag is wrong, or **(B)** the run is synthetic. He asked for the artifact, not an opinion.
**Settled (B)** — `run_class: qa`, a `notes` CONSTRUCTED entry, `provenance[2].observation` naming the pin, and
the pinned partition physically exists (537,913 B). **(A) refuted: the lag is correct.**

**But the finding moved rather than dissolving, and the moved version is worse:** a skilled reader produced a
confident, actionable diagnosis of a *live incident* from constructed data. They saw `run_class: qa`. **It did
not stop them.** The label was present and badly positioned.

**ONE ROOT, THREE SYMPTOMS, MINE:** `apply_exercise_overlay` changed the document without updating the
document's description of itself. Fixed at the class — `constructed` as a **required structural block**
rendering **first**; the carried-forward note **derived**, with a rule refusing any note that claims a
load-bearing list is empty while it is populated; `evidence: presence_only` on `published` entries. **Did not
rename `published`** — the PRD's word, interface agreed with the base lane; routed as a v1.1 candidate.

## What the blind read could NOT prove, and who owns it
It proved **legibility and self-consistency**. It structurally could not prove correctness — the reader had
nothing to check against. **AC-1 stays open for that narrower reason.** Proposed shape (COO taking it to CTO):
**a record with a KNOWN-WRONG value planted in it, and the reader asked to find it** — the mutant discipline
applied to the human-facing surface. **CTO owns the plant; I must not design the test my own artifact passes.**

## ⚠ OPEN FINDING, SURFACED NOT SETTLED — the sixth green-while-wrong, against my own field
Andrew-direct ~1924Z, **STANDING**: *"all of you need to be using comp-tools to establish data flows, lineage,
provenance, and dependencies. You should be hand grepping as a last resort only or to verify comp-tools
outputs."* Applied immediately, and it paid inside one command.

`comp-pipescript io` on the spine returns **5 monolith silver reads**; my manifest observes **8**. The three
extra are Cottonwood's BD silver feeds — **and the spine never reads them** (verified at source: `blackdiamond`
appears once, a display-name dict at `:79`; the cottonwood leg comes from a pre-built GOLD artifact at
`:1552-3`).

> **So my manifest reports `cottonwood: CURRENT, lag 0` measured on BD SILVER, while the publisher consumes a
> pre-built cottonwood GOLD artifact. Those can diverge without limit.** A lag measured on the wrong axis —
> the same class as the frontier-pair recomputation and the roster-only denominator.

**And NEITHER derivation is complete:** the graph missed the cottonwood slice read; my manifest misses both
gold reads. **The comp-tool found a runtime-resolved read no path-extractor can see; the verify step found one
the comp-tool missed.** Andrew's ordering working in both directions. *(COO's caution, received after: treat
`comp-pipescript io` as a static-vs-observed cross-check, not ground truth — it derives from the same repo.
Two derivations disagreeing is the signal; agreement is weaker evidence than it looks.)*

**NOT FIXED UNILATERALLY — there is a real design fork spanning `~B`'s roster and my manifest:** does a
channel's `lag` mean *how fresh is the partner's UPSTREAM* (my reading is then correct, and the manifest
additionally needs what the publisher CONSUMED), or *how fresh is what we published from* (Cottonwood is
measured on a feed the publisher never touches, and is wrong today)? **Both are defensible and produce
different numbers on the same run.** Routed to COO/CTO. `declare_input()` makes the publisher's real reads
recordable either way; this is about **what the number is OF**.

## Tally: SIX instruments of my own green while wrong today
mutants killed by the wrong assertion · a validator that would have rejected a correct manifest · that fix
dropping an invariant · a lineage rollup right-but-misleading for want of a denominator · a note that outlived
its mechanism · and a channel lag measured on a feed the publisher does not read.
**Every one found by a control failing. None by care.**
