# MDPF EXECUTION PLAN — CVO `/verify` of Section D

**Reviewer:** `3.0.0_SA_CVO` · **Requested by:** `1.0.0_SA_CTO` @155326Z, Andrew-direct ~1552Z
**Plan under review:** `org/critical_paths/MDPF_EXECUTION_PLAN_20260722.md` **@d1454d183** (175 lines, 12
assumptions). Re-based from `@52e20e140` on CTO's 155735Z supersession notice; local file verified
byte-identical to `d1454d183`. **All citations below are at vintage `@d1454d183`.**
**archetype:** VALIDATE

---

## 0. COVERAGE FRACTION OF THIS REVIEW *(R10 applied to my own work)*

**THIS IS A PARTIAL VERDICT. 4 of 12 assumptions are discharged.**

| | |
|---|---|
| **Discharged** | **A2** (exercised) · **A3** (exercised) · **A11** (source-grounded) · **A12** (deferred *by construction*) |
| **NOT YET EXAMINED** | **A1, A4, A5, A6, A7, A8, A9, A10** — 8 of 12 |
| **Also not yet done** | D1–D4 ruling review · D-vs-R1–R12 consistency · ordering-law inversion check |

I took the three CTO prioritised (the two exercise-not-read, plus A11 first) and am reporting before
the remainder because **A11 gates S1 and S1 gates all build.** A verdict that arrives complete but late
is worth less than the load-bearing half arriving now. **Do not read this as a plan-wide clearance.**

---

## 1. A2 — count-source-audit tripwire — **CONFIRMED (exercised)**

**Claim:** the tripwire returns `rc=1` on an unaudited prefix **before** the `--firm` branches.

**Method.** Stubbed the S3 *listing* only; real `main()`, real `unaudited_firms()`
(`data/mdpf/scripts/gold/mdpf_revamp_count_source_audit.py:102-109`, called at `:234`, branches at
`:249`). **Nothing was written to `gold/mdpf_revamp/`** — that prefix holds the staged set under
co-sign consideration, and injecting a fake firm into it to test a tripwire would spend the hold's
credibility to buy evidence.

| Case | rc | What it establishes |
|---|---|---|
| `cottonwood` present, `--firm all` | **1** | fires |
| **clean set, `--firm all`** | **0** | **not stuck-on** — without this the other two rows mean nothing |
| `cottonwood` present, **`--firm inflection`** | **1** | **fires even when `--firm` excludes the new firm** |

Ordering observed directly: `LIST gold/mdpf_revamp/` precedes both `LEG` calls in all three cases.

> **VERDICT: A2 holds. The S3 forced ordering stands — you cannot stage first and audit later.**
> The third row is the one worth keeping: a firm-scoped nightly still trips, so the forced ordering
> does **not** depend on anyone remembering to pass `--firm all`.

### 1a. SIDE FINDING (exercised) — **an EMPTY artifact reads as CLEAN**
Real `audit_inflection()` against `dates: []` → **`rc=0`**, verdict *"no disagreement on the audited
dates"*. It also prints `UNAUDITABLE: -1 date(s)` and claims `FRONTIER EXCLUDED (1 date)` on an
artifact with zero dates. The module docstring promises **`2` on an instrument problem**; observed
**`0`**.
**Bears on S3/1e**, which folds *"verdict + coverage into `cycle_complete`"*. The human-readable
output is honest — it prints `0 date(s) audited` and `0 of 0`. **An `rc`-only consumer is blind to
exactly that.** If the fold gates on `rc`, a cycle that produced nothing is indistinguishable from a
cycle that produced something clean. The fix belongs *in* the fold, not after it.

---

## 2. A3 — three-firm sibling tuples — **CONFIRMED (deployed AND exercised)**

**Claim:** the tuples are **live and exercised**, not declared-and-unapplied.

### 2a. DEPLOYED — downloaded the running artifacts, did not read the repo
| Function | CodeSha256 | LastModified | Tuple in **deployed** artifact |
|---|---|---|---|
| `etfs-canon-fanin` | `90JBXG1I7ZEE…` | 2026-06-25T21:37:31Z | `CANONICAL_PARTNERS = ("49financial", "inflection", "cottonwood")` |
| `opal-assets-daily-emitter` | `6TMWk6omkcuG…` | 2026-07-13T14:27:57Z | `FOLD_PARTNERS = ("49financial", "inflection", "cottonwood")` |

Negative control `ZZZnotafirm` = 0 occurrences in both, so the search discriminates.

### 2b. EXERCISED — output-side evidence, with controls
**`etfs-canon-fanin` → DynamoDB `opal-etfs-ownership-daily`** (scan denominator **508**):
`partner=cottonwood` **104** · `partner=inflection` **252** (positive control) · `ZZZnotafirm` **0**
(negative control).

**`opal-assets-daily-emitter` → DynamoDB `opal-assets-daily-aua`**: 252 `etf_ownership_held` rows
(control `model_value` = 147, so the filter discriminates), forming a symmetric **4 ETFs × 3 firms ×
21 dates** grid — `etf_{divz,idvz,pfde,pfoe}__held_cottonwood`, **21 rows each = 84 cottonwood rows.**
Table current through `run_date` 2026-07-18.

> **VERDICT: A3 holds on both limbs. Cottonwood is not merely enumerated in these siblings — its rows
> are physically in both output tables.** The premise that *MDPF is the laggard, not the frontier* is
> supported by exercised evidence, not by a repo grep.

### 2c. TWO NOTES THAT DO NOT CHANGE THE VERDICT
1. **Deployed `opal-assets-daily-emitter` is HEAD-minus-80-lines** — 80 additions in repo, **zero
   removals**, tuple byte-identical. Not divergence; the repo is simply ahead.
2. **The plan's citation `opal-assets-daily-emitter:696` is a REPO line. The deployed artifact carries
   it at `:620`.** Substance unaffected, but per CLAUDE.md *a line citation without a vintage is not a
   citation* — anyone re-verifying against the deployed artifact by line number lands 76 lines off.

---

## 3. A11 — **FAILS AS STATED. The sequence changes.**

**A11:** *axis C is closable by set-difference, AND the estate's list-of-enumerated-subject-lists is
itself bounded.*

### 3a. The set-difference is not computable over the very list that motivated axis C
`infra/aws/terraform/mdpf-pipeline/iam.tf:246-252`, `AssetsRevampSilverRead`, five ARNs:

| ARN | names a… |
|---|---|
| `eclipse/inflection/silver/*` | **FIRM** |
| `orion/inflection/silver/*` | **FIRM** |
| `smartx/platform/silver/*` | **PLATFORM** — no firm token |
| `schwab/08242234/silver/*` | **CUSTODIAL ACCOUNT NUMBER** — no firm token |
| `gold/mdpf_revamp/*` | firm-agnostic staging root |

**Two of five name no firm.** They cannot be differenced against `{49financial, inflection,
cottonwood}` by name-matching, because they are not in that namespace.

### 3b. Not an accident of one list — it is the declared grammar
`infra/aws/terraform/opal-assets/monolith.tf:22-32` — `{source}/{scope}/{layer}/…` — and **`scope` is
heterogeneous BY DESIGN**, six kinds in one block: account numbers (`schwab/08242234`,
`schwab/08335338`) · platform (`smartx/{model|platform}`) · firms (`orion|eclipse/inflection`,
`blackdiamond/cottonwood`) · tickers (`trueshares/{DIVZ,IDVZ}`, `pathfinder/{PFOE,PFDE}`).
**Segment 2 is SCOPE, and firm is only sometimes the scope.**

### 3c. >> THE FAILURE MODE IS WORSE THAN BLINDNESS — IT RETURNS A CONFIDENT WRONG ANSWER <<
Run the specified set-difference naively on those five ARNs and it reports
**`inflection` PRESENT · `49financial` ABSENT · `cottonwood` ABSENT.**
**`49financial` is present TWICE** — `smartx/platform` is its model source, `schwab/08242234` its
custodial master. **One true positive and one false positive, indistinguishable in the output.**
Axes A and B fail *silent*; **axis C's instrument as specified fails LOUD AND WRONG** — and a census
that flags a firm which is in fact wired is one somebody "fixes" by adding a grant that already exists.

### 3d. The resolver it needs does not exist, and two mappings are NOT FUNCTIONS
- **`blackdiamond` → firm is ONE-TO-MANY**: serves 49financial (`bd` tree) *and* cottonwood
  (`blackdiamond/cottonwood/**`, D5). Vendor alone cannot resolve a firm.
- **`schwab/{account}` → firm is MANY-TO-ONE, and collapsing it destroys a control deliberately
  built.** `router_iam.tf:173-177`: the two masters are enumerated individually *"so no single identity
  can write both trees and 'do not commingle 0824 and 0833' becomes a property of the ROLE rather than
  a rule someone has to remember."* A resolver mapping both to `49financial` erases exactly that
  distinction — and standing record carries Andrew's two separate prohibitions (never SUM, never
  SUBSTITUTE). **The alias resolution axis C needs is in tension with a live firm-separation control.**

### 3e. **AXIS D — ENCODING BY ALIAS** *(fourth axis, or a fatal under-specification of the third)*
> *A firm that IS enumerated, under a token from a different namespace.*
> Axis A cannot see it (no firm token). Axis B cannot see it (no arity signal).
> **Axis C MIS-READS it — the one axis that does not merely miss, it misreports.**

C and D have **different cures**: C's is *add the missing entry*; D's is *build the resolver*. The
label is CTO's call; the consequence is identical either way — **the axis-C fraction as written cannot
be computed today.**

**INDEPENDENT LIVE CORROBORATION, found while verifying A3 rather than A11:** my DynamoDB query
`partner = :p` returned **0 for cottonwood, inflection AND 49financial** on `opal-assets-daily-aua`.
Not an absence — the firm is encoded as a **suffix inside a composite `cohort_id`**
(`etf_divz__held_cottonwood`), with no `partner` attribute at all. **I hit axis D live, in a different
system, while checking a different assumption, and my instrument reported a clean zero.**

### 3f. A11's second limb is the wrong question — the constructive part
*"Is the list-of-lists bounded?"* is answerable and probably **yes**. **It is not what closure depends
on.** Closure depends on:
> **(i) are the NAMESPACES through which the estate can name a firm bounded and enumerated, and
> (ii) is each namespace→firm resolver TOTAL and LAW-PRESERVING?**

Namespaces already grounded: **firm-id** · **short-code** (`bd`/`inf`/`cot`, CLAUDE.md's own
firm-separation rule) · **scope** (heterogeneous, `monolith.tf:22`) · **vendor/source** ·
**custodian+account** (`router_iam.tf`) · **bucket name** (`main.tf:56-61` — `bd_bucket`, `inf_bucket`,
**no `cot_bucket`**, a genuine axis-C instance) · **portal `firmId`** · **composite cohort key**
(`etf_divz__held_{firm}`, found above). **Eight, from four files, without looking hard.** I have NOT
established that eight is all of them — **and that is the open question S1's exit now rests on.**

**PROPOSED REPLACEMENT EXIT CRITERION for axis C** *(CTO's to accept or reject)*:
> C is closed when **(1)** the firm-naming namespaces are enumerated with a stated method, **(2)** each
> list is resolved into a common namespace before differencing, and **(3)** every entry that cannot be
> resolved is reported **UNRESOLVED** — never silently dropped, never assumed firm-agnostic.

**(3) is the load bearer.** An unresolvable entry silently dropped is precisely how `smartx/platform`
becomes "not a firm list" and the census returns clean.

---

## 4. A12 — **NOT VERIFIABLE YET, BY CONSTRUCTION**

CTO specified *exercise after apply; do not infer*. The apply is held. **I will not substitute a config
read for an exercise** — that is the DESIRED-only applied-claim Rule 22a names. A12 stays open and
should be discharged by AE post-apply with a `simulate-principal-policy` carrying **ONE**
`--resource-arns` and a **separately invoked** positive control.

---

## 5. METHODOLOGICAL FINDING — **FOUR INSTRUMENT ARTIFACTS ON ONE ASSUMPTION, ALL POINTING THE SAME WAY**

Verifying A3 produced **four** false signals, **every one of which pointed toward "A3 FAILS," and every
one caught only by a control:**

| # | The false signal | What it would have supported | Caught by |
|---|---|---|---|
| 1 | `--delimiter` + `CommonPrefixes` query returned `None` | "no partner dirs exist → tuple is inert" | listing actual keys: **139 keys, cottonwood 26** |
| 2 | Deployed docstring: *"SKELETON — NOT DEPLOYED"* | "the artifact isn't really live" | **104 cottonwood rows** in the output table |
| 3 | `partner = :p` → 0 for **all three** firms | "cottonwood absent from the emitter output" | **positive controls also returned 0** → filter invalid |
| 4 | naive diff: **2444 changed lines** | "deployed has drifted massively from HEAD" | CRLF normalisation → **80 lines, additions only** |

**Artifact 4 was MY OWN**: I wrote the deployed copy with CRLF, then measured drift against it.

> **THE PATTERN THAT MATTERS: I WAS PRIMED TO EXPECT A3 TO FAIL.** CTO's brief — correctly and
> reasonably — warned *"a repo tuple is not a running tuple"* and cited an unapplied IAM grant found
> that same day. **I then accepted four pieces of weak negative evidence in a row without a control,
> and each one confirmed the expectation I had been handed.** A3 is TRUE. **Every single artifact
> pointed at FALSE.**
> **Expectation-shaped evidence is not a reasoning error you can spot from inside the reasoning** —
> each of those four looked like a finding, not like an artifact. **The only thing that separated them
> was running a control I had no positive reason to run.** This is the third distinct instance today of
> *care is not a control*, and it is the strongest, because the prime came from a correct warning.

**Corollary for the census work:** artifact 3 is *also* an axis-D instance. **An instrument aimed at
the wrong namespace returns a clean zero, not an error.** That is exactly what axis C will do at scale
if the resolver requirement is not made explicit.

---

## 6. WHAT I HAVE NOT DONE — stated, not implied

**A1, A4, A5, A6, A7, A8, A9, A10** not examined. **D1–D4 not reviewed as rulings.** **D-vs-R1–R12
consistency and the ordering-law inversion check not performed.** A5 in particular — the one CTO most
wants turned into a gate — is **untouched**, and if the cottonwood-absent build cannot be produced
read-only I will report it as STILL-AN-ARGUMENT rather than dress a reasoning pass as a control.

**On S1b: not re-verified, per CTO's instruction.** The three limbs are stated to the standard I would
have asked for, and `desired == applied` is what makes *"never built"* the right reading rather than
drift.

**Everything in §3 is SOURCE-GROUNDED, NOT EXERCISED.** I read TF and a grammar comment; I did not run
a set-difference instrument and watch it emit the false positive, **because no such instrument exists
yet to run.** §3c is a **DERIVED PREDICTION** about what the specified instrument would do — falsifiable
the moment DE builds it. If his implementation already carries a resolver, my prediction is wrong and
A11 survives in a narrower form.

-- `3.0.0_SA_CVO`, 2026-07-22
