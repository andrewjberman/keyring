# Closed an acceptance leg, ruled a NEVER#3, and got corrected on a claim I made confidently — 2.0.0_SA_COO

**archetype:** MIXED
**secondary_archetypes:** VALIDATE, DIAGNOSE, COORDINATE

Window 2026-07-29T16:31Z -> 17:09Z (since `c8df0865dd`). **ZERO commits** — this window was rulings,
verifications and corrections, all MCP-routed. Nothing deployed, nothing applied, freeze intact.
17:15Z emitter had NOT fired at window close.

## Objective

Hold for the fires with the baseline re-take queued. Four items arrived; three were mine to decide
and one was a correction to me.

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| `comp-grep` | `portal/gold/mdpf` over `data/` + `infra/` | PASS — load-bearing | Denominator printed: **8,213 of 9,814 files scanned**. Every hit a READER; no writer. Fed directly into the NEVER#3 ruling, stated there as a repo-plane null and NOT as proof of absence. |

One comp-tool run this window; the rest was operational `aws s3api` (list-object-versions,
head-object, `s3 cp`) on served/origin artifacts plus targeted file reads — none of which the rail
nudges, and none of which a comp-tool answers better. **`comp-dataflow origin` produced the biggest
finding of the window but CVO ran it, not me** — my part was the two-step verification of it.

**What worked:** printing the denominator on the `comp-grep` null. It let me report "no writer found"
as a *bounded* claim rather than an absence, which is the distinction I had just gotten wrong
elsewhere in the same window.

**Gap:** none new. The `comp-pipescript` rc defect from the prior window is with CTO/AE.

## Work Completed

### 1. D2's 16:15Z publisher leg — CLOSED on my own criterion
DT reported the served output byte-identical with `_provenance.written_at` still `00:35:21Z` and
correctly refused to call it, routing it to me as the criterion owner. Measured at ORIGIN:
```
platinum/mdpf/{global,cottonwood}/aggregate-aua-timeseries.json
  new versions @ 2026-07-29T16:15:32Z ; _provenance.written_at = 2026-07-29T16:15:31Z
  written_by = opal-assets-mdpf-portal-publisher
  source_vintages = {"...": "2026-07-27"}  source_keys = .../2026-07-27.json
```
**The publisher fired unattended on `cron(15 16)`. Leg CLOSED.** DT had read a CDN-cached copy six
minutes after origin moved. **The byte-identical output is EXPLAINED, not excused:** the publisher
faithfully copied gold dated 07-27 — same source, same bytes. Corroborates CTO's cottonwood
refutation and the producer finding independently.

**Made NO staleness call on the 07-27 gold vintage** — trading-calendar question, gold owner's, and a
wall-clock age is not a finding.

### 2. The discriminator DT thought did not exist
DT: *"a run producing byte-identical output is indistinguishable from no run at this layer — only
AE's PIN-4 invocation record discriminates."* True at their layer. **`_provenance.written_at` at
ORIGIN is a second, independent discriminator needing nobody else.** Banked as: *when content cannot
discriminate a re-run, the artifact's own self-stamp usually can — read it at ORIGIN, never through
the CDN.* **It is the inverse of the rule we apply everywhere else:** the SERVED plane answers "is
the serve correct"; the ORIGIN plane answers "did the producer run." Same object, opposite correct
answers by question.

### 3. DT's oracle — their catch, bigger than my correction
The correction exposed that DT's whole-object md5 acceptance leg, load-bearing on all four promotes,
**would have failed spuriously on the next one** — the publisher legitimately re-stamps `written_at`
every run. Their diagnosis: the oracle asserted *"has not been REPUBLISHED"* while claiming *"is
unmoved"*, accidentally equivalent only until the publisher fired. Re-specified and committed
(`3e945f1cc4`), with my asymmetry as a call-out: **the new spec cannot detect a DEAD publisher, by
design.** I validated the evidence at the ref (73 lines, call-out present at line 44,
positive-controlled) and caught that the cited hash `e86ea2819d` was Andrew's MERGE, not DT's
authoring commit — the CLAUDE.md provenance-note class. DT found the general instrument:
`git log --diff-filter=A -1 -- <path>`.

### 4. *** MY OWN ERROR: a portal-scoped null reported as general ***
CVO ran `comp-dataflow origin` and flagged `dim_mdpf_aggregate_aua_timeseries.py:567` reading
`json/mdpf/{firm}/aggregate-aua-timeseries.json`. I verified both their steps:
- **VALUE SOURCE, not a fallback** — docstring: *"a real daily-snapshot NOT recomputable from
  opened_ts alone, so it is IMPORTED to tie served EXACTLY at COMMON dates."* `SERVED_BUCKET =
  "opal-data-portal-v2"` (`:67`).
- **Their in-flight caveat does NOT apply** — `git status data/mdpf/scripts/gold/` empty; last commit
  `0d653d4aa3` (DS, 00:58Z). Committed code, so their own "maybe the edit IS the re-point"
  alternative is ruled out.
- **Removal fails SILENT:** `except Exception -> WARN -> return {}` — no crash, every `account_count`
  goes None on a client-facing series.

**I had told AE~A and CTO that `json/mdpf` had NO live consumer and the Deny was a clean fence. I
enumerated PORTAL COMPONENTS and reported the null as CONSUMERS.** Producer-side readers were
structurally invisible to my method, and I never stated the population. Corrected to CTO and to
AE~A, whose fence verdict rested on my answer.

### 5. NEVER#3 co-sign — CONCURRED it is a serve-widen, CO-SIGN HELD with three conditions
CTO requested co-sign on granting `mdpf-daily-runner-ec2-role` Put+GetObject on
`opal-data-assets/portal/gold/mdpf/*`, having reversed his own prior, and asked me to rule on merits.

**Found it IS a serve-widen.** Decisive limb: the `iam.tf:410-412` text is TREE-scoped categorical
language (*"NO portal/* write is granted here... 'publish HELD' enforced in IAM"*), not
component-scoped — and reading narrower intent into categorical prohibition text is the CLAUDE.md §23
failure that cost four agents. Sharpened his proves-too-much point: if "the route is already live"
exempted a grant, **NEVER#3 would not be narrowed, it would be deleted.**

**Evidence I added, which made his outstanding precondition HARDER:**
```
portal/gold/mdpf/* newest 8 objects: ALL @ 2026-07-29T00:35:16-17Z
  -> NOT rewritten at 16:15Z; the publisher only READ it. The 00:35Z writer is a separate
     component that has not run since.
comp-grep over data/ + infra/ : every hit a READER (publisher lambda :7, its TF :5,
  egress read-prefix :72, aum_metrics comments). NO WRITER FOUND.
  DENOMINATOR: 8,213 of 9,814 scanned -- a repo-plane null, NOT proof of absence.
```
So the grant would add a **known** principal beside an **unidentified** one on a serving-adjacent
tree. CTO said UNDETERMINABLE keeps the hold; the evidence sits closer to undeterminable.

### 6. Pre-registered acceptance for `comp-legacywriter` (Andrew-direct handoff to me)
Andrew-direct via CVO: when CTO~B's build passes CVO's battery it hands to me for first production
exercise across cottonwood / 49financial / global / inflection. **Sent my test criteria NOW, while it
is still being built** — five failure modes, every one MEASURED today with a live fixture: read-vs-write
confusion, bucket-vs-key-path, unnamed population, no-coverage-renders-clean + rc-not-output, and the
one specific to a retirement tool — **"is it read?" is the wrong question; "what happens when it is
gone?" is the right one.** A reader inside a bare `except` returning an empty default is MORE
dangerous to retire than one that hard-fails.

## Decisions Made

| Decision | Rationale |
|---|---|
| Closed D2's 16:15Z leg on origin-plane evidence | My criterion; DT correctly refused to close or dismiss it. |
| Held the NEVER#3 co-sign rather than granting or refusing | Need is real; precondition unmet and my evidence weakened it further. CTO asked not to be rubber-stamped. |
| Get+Put together or neither, as a condition | The bare-`except` disarm makes a PutObject-only compromise strictly worse than refusing. |
| Corrected my own json/mdpf verdict to three agents unprompted | AE~A had acted on it; a wrong "no consumer" would have licensed a retirement. |
| Pre-registered comp-legacywriter criteria before the build lands | Cheapest moment to influence a tool I will have to sign the output of. |
| Did NOT re-verify CVO's finding from scratch, only their two named steps | They stated the verify; duplicating it wastes the division of labour. |

## Files Modified

None. Zero commits this window — rulings and verifications only.

## Blockers

None held by me. NEVER#3 co-sign is HELD (conditions stated, actionable); `json/mdpf` teardown is
BLOCKED behind a re-point of the `:567` reader — evidence-cited, not assumption-blocked.

## Current State

- Watcher live, Monitor `bek0zd4f3`. PID 28928. Zero crons. `/drive` OFF.
- **D2 16:15Z leg CLOSED.** 17:15Z emitter NOT yet fired at window close.
- **NEVER#3 held** on: (C1) 00:35:16Z writer identified + a coordination story if it is live;
  (C2) Get+Put together or neither; (C3) R5 anti-clobber EXERCISED post-apply, not config-read,
  with `simulate-principal-policy` one `--resource-arns` per call and the positive control separate.
- **Teardown wave (mine, post-fires)** now carries, in order: 3 live legacy-plane clobbers; schwab
  v1/v2/v3 (only CONFIRMED repo multi-writer); `BD_S3_BUCKET` name collision; price-update
  script-vs-Lambda; CTO's permanent-red LEGACY-EMIT. **`json/mdpf/*` sits BEHIND the `:567` re-point.**
- **Queued at me:** baseline re-take (DS~A run + artifact hash; discriminating values in
  `startup_verification_wave_1455-1555Z.md` @`8c55c2635d`); `comp-legacywriter` first exercise on
  CVO's build+verify report.
- OPEN, deliberately not guessed: whether the `account_count` trailing-None run (407/450 non-null,
  tail None) is GROWING from the 07-28 Deny or is the designed pre-cutover boundary. Identical in
  the artifact; needs the None date range against the Deny install date. DS/AE lane.

## Next Steps

- **[2.0.0_SA_COO]** 17:15Z emitter observation; baseline re-take when DS~A's run lands, plane- and
  artifact-labelled; teardown wave post-fires.
- **[1.0.0_SA_CTO]** NEVER#3 disposition on my three conditions; cottonwood basis rule; the
  wrong-label class as doctrine (raised, unruled).
- **[0.7.0_AE_CloudOps~A]** CloudTrail identification of the 00:35:16-17Z writer — the gating item
  for the NEVER#3.
- **[0.4.0_DS_ClientPlatform~A]** Ad-hoc cottonwood run; deployed-vs-repo on the distribution producer.
- **[3.0.0_SA_CVO]** `comp-legacywriter` battery; my pre-registered criteria sent 165733Z.
