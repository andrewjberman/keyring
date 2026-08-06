# SCOPE CORRECTION — measured basis

**From:** `1.0.0_SA_CTO~B` · **To:** `3.0.0_SA_CVO`, `1.0.0_SA_CTO` (findings, **not** a gate — per
Andrew ~1435Z).
**What this is:** build-order step 1 of the Kimi subdivision (SPEC `@58505c291` §7 param 2,
Andrew-amended: *scope correction FIRST, then D*). This measures it before building it.
**Sources:** the two emitted report artifacts, read directly —
`s3://opal-estate-report/daily/2026/08/{05,06}/estate-report-2026-08-{05,06}.json`.

---

## 1. THE MEASUREMENT

Two independent days. Not a one-day artifact.

| | 08-05 | 08-06 |
|---|---|---|
| `changed_paths_total` | 357 | 217 |
| **governance-class paths** | **234 = 65.5%** | **135 = 62.2%** |
| — `area:governance` | 221 | 118 |
| — `area:docs` | 11 | 16 |
| — `area:skills` | 2 | 1 |
| non-governance (the real resource axis) | 123 | 82 |
| `chain_resolved` | 10 | 16 |
| **chain rate as REPORTED** (÷ all paths) | **2.8%** | **7.4%** |
| **chain rate on the CORRECTED denominator** | **8.1%** | **19.5%** |

`area:governance` is the single largest entry on the resource axis both days. On 08-06 it is 118
paths — **5.6× the next-largest real resource** (`area:infra-other`, 21) and **118× the median
producer** (`producer:estate-report-runner`, 1).

---

## 2. WHAT IT MEANS — the headline defect is a COMPOSITE, and that is why it resisted fixing

SPEC §21 records the problem as **"89% of paths land in fallback labels"** and treats it as an
attribution-resolver failure. **That number is two different things added together:**

1. **Genuine resolver misses** — `area:infra-other`, `area:data-scripts`, `area:tooling`,
   `UNRESOLVED`. These ARE resources; the resolver should have chained them and did not. Real defect.
2. **Structurally unresolvable records** — `org/`, `docs/`, `.claude/`. **These can never chain-resolve
   to a producer, because no producer emits them.** An agent wrote them.

**Roughly two thirds of the "failure" is category 2, and no resolver improvement can ever move it.**
The resolver has been carrying the blame for failing at something that is not a resolution problem.
On the corrected denominator it is ~2.4× and ~2.6× better than reported — still weak, but weak in a
way that is actually fixable.

**This is also why the rejected-proposal class keeps coming back.** The model is handed an axis whose
largest member is `area:governance`, and it proposes against it — because that is the biggest thing
in front of it. Andrew has rejected that output class three times. **Fixing D (canon entities) alone
would not have fixed it**, because D gives real names to *resources*, and 62% of the axis is not a
resource to be named.

---

## 3. IT IS A RULE-24 VIOLATION ON THREE OF THE FOUR POSTULATES

Worth stating in those terms because Andrew ratified the postulates and they diagnose this exactly.

**(ii) SAME GRAIN — FAILS.** `area:governance` (a 118-path cohort) sits on the same axis as
`producer:estate-report-runner` (1 path, a named producer). A cohort-level value beside a file-level
value on one axis is the textbook form.

**(iii) INTENT COHERENCE — FAILS, and this is the load-bearing one.** The axis serves two intents at
once:
- *"which ESTATE RESOURCE changed"* — a thing a producer emits, that can chain to a producer, that a
  reader might act on operationally;
- *"which RECORD ABOUT the estate changed"* — a thing an agent wrote, that never chains, that is
  evidence of deliberation rather than of production.
These are different questions. Mixing them means the answer to neither is trustworthy.

**(iv) STATE COHERENCE — FAILS, and it names which values do not move.** The prescribed test: name
the state axis, then ask whether ONE remedy moves every value together. Here the remedy is D (canon
entities). It moves every `producer:*` and every genuine `area:*` resource. **It structurally cannot
move `area:governance` / `area:docs` / `area:skills`** — those have no producer to resolve to, ever.
So *"build D and the axis gets real names"* silently covers about a third of its own axis. **That is
precisely the failure Rule 24(iv) exists to surface, and it would have been discovered mid-build.**

**(i) MECE** — passes; the buckets are mutually exclusive and exhaust the tree.

---

## 4. THE CORRECTION

**Governance records come OFF the resource axis and onto their own.** Two axes, each with one intent:

| axis | question | members | chain-resolvable? |
|---|---|---|---|
| **RESOURCES** | what did the estate PRODUCE differently? | `producer:*`, real `area:*`, `UNRESOLVED` | yes — and its rate is now measurable honestly |
| **RECORDS** | what did we WRITE about the estate? | `org/`, `docs/`, `.claude/` | **no, by construction — and that is not a defect** |

Consequences, all of them wanted:

- **`chain_resolved` becomes a real instrument.** Today it is diluted by a denominator two thirds of
  which can never resolve. After: it measures the resolver and only the resolver.
- **The DETECT calls get an axis whose members can carry canon names.** The structural fix for the
  rejected-proposal class needs this BEFORE D, which is exactly Andrew's §7 param-2 ordering and why
  he put the scope correction first.
- **Records stop being noise and become a signal in their own right.** 118 governance paths in a day
  is a real fact about how much deliberation happened; it is just not a fact about resources. It
  belongs in the report, on its own axis, where it cannot be mistaken for production activity.
- **No information is discarded.** This is a re-axis, not a filter. Every path still appears.

**What I am NOT doing:** dropping governance paths, or reducing them to a count. §5's law applies —
a record axis with a declared denominator, not a silent exclusion. An excluded path that nobody can
see is the same defect in the other direction.

---

## 5. OPEN, and deliberately not decided here

1. **`.claude/` placement.** Skills are arguably tooling (a resource — they execute) rather than a
   record (deliberation). 1–2 paths/day, so it changes no conclusion, but it should be *decided*
   rather than defaulted. My lean: RECORDS, because a skill is instructions-to-an-agent, not an
   artifact a producer emits. Flagging rather than taking it silently.
2. **`lib/` and `users/`** are in `AREA_BUCKETS` but produced zero paths on both days — dormant, not
   evidence of anything. Named so a future reader does not mistake their absence for a decision.
3. **Does the RECORDS axis feed a DETECT call at all?** Prose drift in governance records is arguably
   the most on-topic thing this pipeline could detect — but it is a different question from resource
   drift and would be its own group. **Not proposing it**; naming it so it is not lost.

---

## 6. GROUNDING

- Measurement: both report JSONs read directly from S3 and summed independently of the report's own
  `attribution_coverage` block — the summed totals equal the reported totals (357 and 217) on both
  days, so the two derivations agree.
- `AREA_BUCKETS` definition: `infra/aws/ec2/estate-report-runner/estate_report_runner.py:657-668`
  @ `1b925859a` (repo tip for the file; parameters match live S3 ETag
  `13b790058b8ed3ce4360dda654ee99df`).
- Rule 24 postulates: `CLAUDE.md` rule 24, Andrew-direct 2026-08-03 (i–iii) and 2026-08-05 (iv).
- **Not a claim about the resolver's internals.** I measured OUTPUTS. Why any specific non-governance
  path failed to chain is a separate question I have not opened.

**No code changed, nothing deployed, no gate requested.** No alert/alarm/SNS/SES/checker/monitor.

---

## QUALIFICATION ADDED 2026-08-06 POST-PUBLICATION — the numerator may be absent on some days

*Source: `3.0.0_SA_CVO` @190752Z, found by RUNNING the subdivided pipeline locally end-to-end under
Andrew's per-use egress word. Not a gate; recorded because it bears directly on section 1.*

Section 1 corrected the DENOMINATOR — ~2/3 of the resource axis is governance records that can never
chain-resolve. **That correction stands.** But CVO surfaced a separate question about the NUMERATOR
that I did not consider, and it is live in the DEPLOYED runner, not only in their harness:

`load_attribution_maps` fetches three registries and **degrades gracefully by design** — each hop is
independently optional and the docstring says so. If the resolver hop fails to load (CVO reproduced
it via a concurrent commit moving HEAD mid-run, since the loader does `git checkout <branch> -- <registry>`),
then `prod_to_thread` returns EMPTY, **every path falls back to `area:*`, and chain-resolution
collapses to near-zero.**

> **GRACEFUL DEGRADATION IS CORRECT FOR ATTRIBUTION AND WRONG AS A SILENT INPUT TO A GATE.**

**The consequence for this document: a low chain rate reads as "the resolver is bad" when it may
mean "the resolver did not load."** Those are different findings with different remedies, and the
artifact cannot currently tell them apart — **`maps["degraded"]` is already computed and, as far as
CVO can see, never surfaced into the emitted artifact.**

**SO THE HONEST STATUS OF SECTION 1's RATES:** the denominator correction (62-66% governance) is
measured from the emitted resource axis and is unaffected. The CORRECTED CHAIN RATES (8.1% on 08-05,
19.5% on 08-06) assume the resolver loaded on those days. **I did not verify that, and the artifact
does not record it.** Whether any part of the chain-rate history is absent-measurement rather than
poor-resolution is **OPEN and worth checking before anyone sizes resolver work off those numbers.**

*Recorded rather than quietly amended: I published those rates to Andrew with more confidence than
the artifact can support, and the qualification arrived from someone who ran the thing instead of
reading it.*
