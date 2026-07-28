# OPAL ARCHETYPES — the RUNTIME-PROVENANCE axis: establishing patterns (1A) and migrating pattern breaks (1B)

    author:      3.0.0_SA_CVO
    status:      ASSESSMENT + GUIDING DOCUMENT. **Not a standard.** Feeds OPAL_STNDRD / OPAL_TAXONOMY
                 (CTO + 0.7.0_AE_CloudOps~Z) and NFRA_TOOLARCH (~Z group + 0.8.0_AE).
    authority:   Andrew-direct 2026-07-28 ~1508Z, CVO terminal. Verbatim in §0.
    extends:     `docs/architecture/NFRA_TOOLARCH_PRD.md` (chartered Andrew-direct 2026-07-23).
                 **This brief does NOT re-derive TOOLARCH's archetype census. It adds an axis that
                 census does not carry** — established by measurement in §1, not by assertion.
    measured:    2026-07-28T151x-152xZ, live AWS us-east-1 acct 313476888478. Denominators printed.

---

## §0 Charter — Andrew-direct, VERBATIM (CVO terminal, 2026-07-28 ~1508Z)

> *"THis is the real task I need you on. It is something that I had tasked the ~Z group and 0.8.0_AE
> agents with over the last few days but I don't think we got to this specific topic. It is
> understanding the domain for the various comp-tools, establishing where they are blind. We wanted to
> figure out how to dynamically set up oracles, but to your point in this particular example, the
> oracle was not aware of an s3 code producer. Accordingly I want your task this session to take on two
> parts. 1.) I need you to continue to hammer down our archetypal patterns. We've been doing this for
> lambdas, EC2, buckets, and more as a function of OPAL_STNDRD and OPAL_TAXONOMY, but clearly there are
> more dynamics we need to bring under that umbrella like runtime code injections as a function of
> source (the S3 code import scenario). I want you to assess the status of our universe and daily ops
> by using the Trino Heat Analytics, Nessie/Iceberg, git commits and co-changes, and more to get an
> understanding of the day to day operations of our system and try to gauge what patterns we have and
> where there are pattern breaks in those vectors. That means you need to be assessing 'how do we set
> up EC2s? Where do those EC2s get their code? how do we set up lambdas? how do those lambdas get their
> code? how do we set up bucket and bucket structure? What do we use for triggers (eventbridge rules vs
> schedule, should use one or the other)?' etc etc etc etc there are many items and we need to
> understand them concretely so we can start to A.) Establish our patterns system-wide and B.) Clean
> up/migrate the pattern breaks. I need you to write a brief on 1A.) and 1B.) so that what I'm
> describing here is persisted and serves to be your guiding document on this subject. Please address
> that first and then we will address 2.) in more detail, which is essentially establishing the
> denominator/coverage of the scanners and how those are generalized and validated across tool
> library."*

**Part 2 (scanner denominator/coverage + generalisation across the tool library) is HELD by his own
sequencing until this lands. It is already scoped as `NFRA_TOOLSEM`.**

---

## §1 What already exists, and the measured gap this brief fills

**Andrew's premise — that `~Z`/`0.8.0_AE` "did not get to this specific topic" — is HALF right, and the
half that is wrong would have cost this session.** The archetype program exists and is substantial:

| existing work | what it covers |
|---|---|
| `NFRA_TOOLARCH_PRD.md` §2 | Q1 archetype census (C0-C3 ladder), Q2 pattern inventory, Q3 generalisation |
| `NFRA_TOOLARCH_PRD.md` §3 | the **stability grader** — GOVERNANCE / CHURN / POPULATION / VIOLATION / BLAST |
| `NFRA_MSBEFF` | the empirical corpus: 21,775 log rows, 718 findings, 187 override intents |
| `NFRA_SYSPARITY` + `infra/system/` | modelled-vs-live parity register (closed 22/22 CLEAN) |
| `OPAL_STNDRD` | one-capacity-one-service; `trigger-map.json` census (07-18) |

**THE GAP, MEASURED NOT ASSERTED.** `NFRA_TOOLARCH_PRD.md` is 116 lines. Token census over it:

    "provenance"       0        "artifact store"   0        "Rule 12"      0
    "pulls"            0        "runtime.*code"    0        "code.*bucket" 0
    POSITIVE CONTROL — "archetype"  12

**Zero coverage of the runtime-provenance axis, against a positive control proving the retrieval
works.** The reason is structural, not an oversight: TOOLARCH classifies via the **C0–C3 ontology
ladder** — C0 typed nodes, C1 relations, C2 motifs, C3 systems. That ladder models **what a thing IS
and how it RELATES**. It has no cell for **how a thing COMES TO BE what it is at run time.**

> **A Lambda and an EC2 runner can be identical as typed nodes with identical relations, and be
> entirely different objects operationally — because one carries its code and the other fetches it.**

---

## §2 The new axis — RUNTIME PROVENANCE

**Definition.** For every executing capacity, the answer to: *at the moment it runs, where did the code
it executes come from, and what governs the path between the authored artifact and that location?*

**Provenance classes observed in this estate:**

| class | mechanism | drift detectable by a repo scan? |
|---|---|---|
| **P1 REPO-RESIDENT** | code in the repo, deployed as a Lambda zip via Terraform | **YES** — repo is the source of truth |
| **P2 S3-RESIDENT** | code authored locally → pushed to S3 → **pulled by the compute at run time** | **NO** — the executing artifact is not in the repo |
| **P3 IMAGE-RESIDENT** | container image (3 Lambdas) | NO — image digest, not repo state |
| **P4 LAYER-RESIDENT** | dependencies in Lambda Layers, versioned separately | PARTIAL — layer ARN pins a version |

**P2 IS NOT A DEVIATION. IT IS THE LAW.** CLAUDE.md Deployment Rule 12:
> *"S3 is the artifact store for ALL EC2 code — never write code on a VM, never inline Python in SSM.
> Local → S3 → EC2 pulls → execute, even for ad-hoc diagnostics."*

>> **THE CENTRAL FINDING OF THIS BRIEF: our scanners model an estate in which code lives in the
>> repository, while our own law requires that EC2 code does not. The tooling contradicts the standard
>> it exists to enforce.** <<

That is why `comp-clobber` — in **both** of its modes — reported a clean bill of health on a served key
that had been clobbered on 07-25, 07-26 and 07-27 (`cc025f038`). It is not a tool bug. **Every
repo-scanning instrument in the suite inherits this blind spot, and the blindness is exactly
co-extensive with the set of things Rule 12 governs.**

**Why this generalises beyond code:** the same question — *"what is the provenance of the thing that
actually ran/served, and is the authored version even in a place we scan?"* — is the same shape as
DEPLOYED-vs-REPO drift, as DESIRED-vs-APPLIED IAM (Rule 22a), and as the served-artifact-vs-gold
lineage. **Provenance is a missing DIMENSION of the ontology, not a missing tool.**

---

## §3 (1A) THE PATTERNS TO ESTABLISH — dimensions, measured state, and the governing law

For each dimension: **what the law says**, **what the estate measurably does**, and **whether the shape
is STABLE-BY-LAW** in TOOLARCH §3's sense (governed + low churn + bounded population + zero live
violations) — because that grade decides whether a pattern extractor may be regex or must be structural.

### D1 — COMPUTE CAPACITY: how we set up Lambdas
**Measured:** 191 functions. `PackageType` Zip **188** / Image **3**. Layers: **118 carry ZERO layers**,
65 carry 1, 8 carry 2. CodeSize min **0**, p50 6,358, max **58,785,015**. Name prefixes: `opal` 50,
`yang` 28, `inf` 23, `bd` 18, `trade` 7, `seeking` 7, `smartx` 5, then a long tail.
**Law:** Rule 1 (Terraform is the only deploy mechanism), Rule 3 (dependencies go in Layers), Rule 4
(source-map entry per Lambda), Rule 5 (size deliberately; never leave `yang-lambda` 256MB/30s defaults).
**Grade: NOT stable-by-law.** Population bounded and enumerable, but **VIOLATION is non-zero on its
face** (see 1B-2, 1B-3) and the naming shape is convention, not law.

### D2 — RUNTIME PROVENANCE: how Lambdas and EC2s get their code ← **THE NEW AXIS**
**Measured:** Lambda = P1/P3/P4 (zip via TF, 3 images, 73 with layers). EC2 = **P2 universally**, per
Rule 12. **38 Lambdas are <2KB** — candidate stubs/runtime-fetchers that would be P2-like on the Lambda
plane, which nothing currently classifies.
**Law:** Rule 12 (EC2 → S3 → pull), Rules 1/3 (Lambda → TF/Layers), Rule 10 (never push code into EC2
images).
**Grade: GOVERNED BUT UNMODELLED.** The law is clear and the population enumerable; **no tool models
the axis at all**, so VIOLATION is currently unmeasurable — which is itself the finding.

### D3 — CODE LOCATION: which bucket holds runtime code
**Measured — and this is the sharpest result in the brief:**

    ARTIFACT buckets            opal-runner-shared              code/  PRESENT
                                opal-313476888478-lambda-artifacts     -- EMPTY --
                                opal-313476888478-lambda-layers        -- EMPTY --
                                opal-ci-staging                        -- EMPTY --
    DATA buckets                opal-data-mdpf                  code/  PRESENT
                                opal-data-inf                   code/  PRESENT
                                opal-data-bd                    code/ + scripts/  PRESENT
                                opal-data-cot                   code/  PRESENT
                                opal-data-assets                code/  PRESENT

**5 of 5 data buckets carry runtime code. The three dedicated artifact buckets are empty of it.**
**Law: NONE.** Rule 12 says code lives in S3; **it does not say WHICH bucket**, and the estate has
answered "the data bucket" 5 times out of 5 while purpose-built artifact buckets sit unused.
**Consequence, not aesthetics:** code and data then share one bucket policy, one versioning/lifecycle
regime, one IAM blast radius, and one `.parquet`-deny-style guard surface. It also means a
firm-separation IAM boundary drawn around a data bucket silently encloses executable code.
*(Observed in passing at `s3://opal-data-mdpf/code/scripts/backfill/.crosswalk_cache.pkl`, 185,393 B —
a pickle cache under a `code/` prefix. A `.pkl` is a code-execution surface on load. Noted, not
diagnosed.)*

### D4 — TRIGGERS: EventBridge Rules vs Scheduler
**Measured:** 141 Rules on the default bus (**121 scheduled + 20 event-pattern**; 123 ENABLED, **18
DISABLED**) + **10 Scheduler schedules** (9 ENABLED, 1 DISABLED).
**⇒ 131 time-triggers split across two services.**
**Law:** OPAL_STNDRD one-capacity-one-service (event → Rule, time → Scheduler) + **NEVER#4: a
production pipeline MUST have a schedule; a pipeline whose only trigger is another pipeline's success
has no schedule and is a defect.**
**Grade: GOVERNED, HIGH VIOLATION.** The standard exists and the estate is 121/131 on the wrong side of
it. This axis is the most migration-ready of all of them.

### D5 — EC2 FLEET SHAPE
**Measured:** 34 non-terminated — **30 stopped / 4 running**; 10 distinct instance types; **33 of 34
carry an IAM instance profile** (the exception is `i-06376c11d8b3c3443`, `seeking-alpha-scraper` —
independently surfaced by `comp-kuzu run_validation` Q2 on 07-25, so this is a second sighting, not a
new claim). Ephemeral-runner shape dominates: gold-layer runners, QA runners, exporters, scrapers.
**Law:** Rules 7/8/9/11/12 — `safe-ec2-deploy.sh`, `EC2_MANIFEST.json` as source of truth, TF manages
infra-not-code, parity check before EC2 work.
**Grade: MOSTLY GOVERNED**, population bounded; the stopped-majority is by design (ephemeral runners),
**not** evidence of debt — do not read "30 stopped" as an outage.

### D6 — BUCKET GRAMMAR
**Measured:** 39 buckets. Families: `opal-data-*` (15), `opal-313476888478-*` (4, account-scoped),
logs/audit (5), product/app (the rest).
**Law:** `{source}/{scope}/{layer}/{type|feed}/{date}` key grammar on `opal-data-assets`; naming law
silver `fact_*` / gold `dim_*`; Rule 17a bronze-is-raw with a LIVE `.parquet`-under-`bronze/` bucket
policy deny — **on ONE bucket only** (07-16), with other trees' `bronze/` still open.
**Grade: STABLE-BY-LAW on `opal-data-assets`** (declared grammar + a live gate) — this is the one
dimension where TOOLARCH §3 would license a regex extractor, provided it cites the grammar.
**Not** stable across the other 38.

### D7 — DEPLOY PATH INTEGRITY (the axis that made D2 bite)
**Measured, from the MDPF incident:** `mdpf` is absent from `safe_deploy_core.py`'s `PIPELINE_MAP`, so
a push **cannot deploy that tree at all**; the runner executed 07-21 code for 7 days (deployed 51,999 B
vs repo HEAD 124,241 B).
**Grade: THE CLASS IS OPEN.** Any Rule-12-conformant tree not registered in `PIPELINE_MAP` is
simultaneously (a) undeployable by the normal path and (b) invisible to deployed-vs-repo drift
detection. **`mdpf` is the instance that bit us; the class is unenumerated.**

---

## §4 (1B) PATTERN BREAKS — measured, ranked by silent-failure risk

**Ranked by "how long could this be wrong before anyone noticed," not by count.**

**B1 — RULE-12 TREES ARE INVISIBLE TO DRIFT DETECTION (class-level, highest).** Every repo-scanning
tool is blind to P2 code. Measured consequence: 7 days of stale execution, and a two-producer clobber
that both comp-clobber modes reported clean. **Migration is not "add `mdpf` to `PIPELINE_MAP`"** — that
closes one instance and leaves the class open, and the next Rule-12 tree rots identically and silently.
**The fix is a provenance-aware oracle** (see §5).

**B2 — 118 of 191 LAMBDAS CARRY ZERO LAYERS** against Rule 3 ("dependencies go in Lambda Layers"). Not
all are violations — a dependency-free function legitimately needs none — **so this is a CANDIDATE SET,
not a finding, and I am not reporting it as one.** The discriminator is whether the function has
non-stdlib imports; that is a per-function structural test nobody has run. **Denominator stated so the
next agent knows the size of the question: 118.**

**B3 — RUNTIME FRAGMENTATION: 6 runtimes live** — python3.11 (107), python3.12 (69), **python3.9 (3)**,
nodejs20.x (6), nodejs22.x (2), **nodejs18.x (1)**. Three Node majors and a py3.9 tail. Rule 15 requires
`from __future__ import annotations` precisely because of py3.9 runners — **the 3 py3.9 functions are
the population that rule exists for**, and nodejs18.x is past AWS's maintained window.

**B4 — 121 SCHEDULED RULES vs 10 SCHEDULER** — one capacity, two services, 92% on the non-standard
side. Highest-volume, lowest-risk migration; entirely mechanical.

**B5 — 18 DISABLED EventBridge RULES** carried on the default bus. A disabled rule is either dead
config or a suppressed control; **both are debt and they are indistinguishable from outside.**

**B6 — RUNTIME CODE IN DATA BUCKETS, 5 of 5.** No law violated (Rule 12 is silent on which bucket);
**a standard is owed rather than a migration.** Until it exists, code inherits data's lifecycle, IAM
and guard surface by default.

**B7 — 1 of 34 EC2 WITHOUT AN IAM INSTANCE PROFILE** (`i-06376c11d8b3c3443`). Second independent
sighting; already routed by CVO~Z on 07-25. Recorded here for the axis, not re-opened.

---

## §5 How this feeds the existing machinery — the deliverable shape

**This brief's output is an AXIS, and the axis must land in three places or it will not survive:**

1. **TOOLARCH's archetype census (Q1)** gains **PROVENANCE as a classification dimension** alongside
   environment/layer/tenant/plane/cadence — so every capacity is typed `P1|P2|P3|P4`.
2. **TOOLARCH's pattern inventory (Q2)** gains the pattern *"the executing artifact is not the authored
   artifact, and the authored one may not be in a scanned location"* — with its tool column currently
   **EMPTY**. Per §2 of that PRD, an empty tool column IS the gap statement.
3. **TOOLARCH's stability grader (§3)** is the right gate for the fix. Provenance grades
   **GOVERNED (Rule 12) / LOW CHURN / BOUNDED POPULATION / VIOLATION-UNMEASURABLE** — and by that PRD's
   own ruling, *"a pattern extractor whose governing law is not cited is unregistrable."* **A
   provenance oracle must cite Rule 12**, so that if Rule 12 changes the oracle fails loudly.

**The oracle Andrew asked about ("how to dynamically set up oracles") has a concrete first instance
here:** for any capacity, resolve its provenance class, then choose the comparison basis accordingly —
P1 compares repo↔deployed; **P2 must compare S3-artifact↔deployed↔repo, a THREE-way comparison no
current tool performs**; P3 compares image digests. **An oracle that assumes P1 on a P2 capacity does
not error — it returns clean.** That is the property that makes this class dangerous rather than merely
incomplete.

---

## §6 Scope, ownership, and what this brief deliberately does NOT do

- **This is an assessment, not a standard.** Per my prompt §8 I qualify and recommend; ratification
  routes to **CTO + `0.7.0_AE_CloudOps~Z`** (OPAL_STNDRD/OPAL_TAXONOMY) and the `~Z` standards lane.
- **It does not re-derive TOOLARCH's census** — §1 measures the specific absence it fills.
- **Trino Heat Analytics / Nessie-Iceberg / git co-change analysis are NOT yet incorporated.** Andrew
  named them as instruments for this assessment and **I have not run them.** The §3/§4 findings stand
  on live-AWS + source measurement alone. **Stated as a coverage limit, not left implicit** — the
  co-change axis in particular is the one that would show *which files move together*, i.e. the
  empirical shape of a pattern, and its absence means every "pattern" here is argued from population
  and law rather than from observed co-evolution. **That is the first extension.**
- **B2's 118 is a candidate set, not a violation count.** Reported with its denominator precisely so it
  cannot harden into "118 violations."

## §7 Next

1. Run the **co-change / Trino-heat** pass to ground patterns empirically rather than by law+population.
2. Enumerate the **P2 population** — every Rule-12 tree and whether it is in `PIPELINE_MAP` (B1's class).
3. Discriminate **B2's 118** by structural import analysis.
4. **Part 2** — scanner denominator/coverage across the tool library (`NFRA_TOOLSEM`), held by Andrew's
   own sequencing until this brief lands.

— 3.0.0_SA_CVO
