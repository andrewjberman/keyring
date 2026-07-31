# ~B lane: the capture-writer LEAK, 213 forged quotes, and the C3 labeling layer -- 1300-2115Z

**archetype:** MIXED (IMPLEMENT + DIAGNOSE)
**secondary_archetypes:** VALIDATE, DEPLOY, SCRIBE, COORDINATE
**Serial:** `0.7.0_AE_CloudOps~B` (PID 23960, Monitor `bwbej7fil`)
**Prior log:** `2026-07-31/lane_B_corpus_corrections_v3_v4_capture_2340-0215Z.md` (predecessor session)
**Window:** 12 commits, `3b9e54730a` -> `fb96b284a2`

---

## Arc

Started at a hard park. Andrew carved the project back in mid-turn, and the day split in two:
**an IAM boundary that had to be built and then caught leaking**, and **a governance spec that took
four reviews and got corrected three times by its own reviewers.**

1. **Startup + carve-out.** Registered, armed, read two messages parking the v4 build. Andrew then
   authorized it directly (3 verbatims, recorded `@3b9e54730a`, broadcast same turn) and **reframed
   it**: the pipeline is not adjacent to NFRA_VELOCITY, it is **upstream** of the ESTATE half.
2. **213 FORGED QUOTES.** Corpus-scale measurement of the capture store found harness text filed as
   Andrew's words. Fixed `@1c3a75bfff` with a 5-prediction control.
3. **estate-capture-writer built** -- because the device wrote as an ADMINISTRATOR.
4. **THE LEAK.** The ruled `*/text-input/*` shape let the producer write INSIDE `signed-review/`.
   Caught on the draft, before apply.
5. **The C3 labeling-layer spec** (Andrew-direct), 4 revisions, 3 CVO reviews + CTO arch-gate.
6. **C3L.3 steps 1-2 built** on Andrew's explicit authorization -- and the tool's own negative
   control fired on its first run.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| commit-gate | x4 (`.py` touches) | PASS 3 / **BLOCKED 1** | the BLOCK was real: dead code after a `return` left `INTENT_SOURCE_REJECTED` unreachable -- the spec's own canonical case, silently not firing |
| terraform validate | x3 | PASS | |
| terraform plan / safe-apply | x4 plan, x2 apply | PASS (+1 **REFUSED**) | the refusal was correct -- see Deployment Sequence |
| `simulate-custom-policy` | 20+ invocations | PASS | draft batteries; ONE `--resource-arns` each |
| `simulate-principal-policy` | 13 invocations | PASS | applied batteries, both principals, separate positive controls |
| `accessanalyzer` | not needed | SKIPPED | no action-name validity question arose |
| comp-iam gaps | x1 (after `iam.tf`) | PASS | no new gap; 17 pre-existing in other pipelines. Tool printed its own caveat: action-only, no resource comparison |
| comp-grep / comp-glob | x6 | PASS | found the registry, the C3 taxonomy, the `C3L.` absence (2 files, neither a TO) |
| comp-surface-check | auto in safe-commit x12 | PASS | no critical surface |
| comp-pulse risk-reflex | auto x12 | PASS + **1 HOLD** | the HOLD sent me to CLAUDE.md:81 -> ran `comp-iam` |
| `get-bucket-lifecycle-configuration` | x4 | PASS | **discriminating** positive control -- see below |

**What worked:** the **discriminating positive control** on the lifecycle check. Rather than
controlling against call-shape errors, I controlled against buckets carrying the exact hazard
(`opal-data-bd` has `expire-noncurrent-versions-90d`). So the clean read on `opal-estate-report` is a
**controlled** negative, not a silent one.

**What failed:** `simulate-custom-policy` via `file://` returned `InvalidInput` on all five cases.
Isolated it (inline minimal policy -> `allowed`; identical policy via `file://` -> `InvalidInput`) --
MSYS path handling, failing loud. **The dangerous half: a careless read of "not `allowed`" as
"denied" would have scored FOUR PASSES on a call that never evaluated anything.**

**Gap found:** `comp-iam gaps` cannot see the estate-capture-writer boundary at all -- it models
`(action)`, never `(action, resource)`, and this whole role is a resource-shape constraint. Not a new
gap, but a first-hand instance of the known one.

---

## Deployment Sequence + Verification (AE)

**Ledger:** `org/critical_paths/change_management/20260731T1440Z_estate-capture-writer-role_deploy_completion.md`
-- OPENED at apply-start, **CLOSED in-session**, both legs.

| Leg | Result |
|---|---|
| v0.2.0 | `2 added, 0 changed, 0 destroyed` -- tagauthz PASSED, tombstone CLEAN, 0-diff verified |
| v0.2.1 | `1 added, 0 changed, 1 destroyed` (policy replaced, role untouched), 0-diff verified |

**A GATE REFUSED THE FIRST APPLY AND IT WAS RIGHT:**
```
safe-apply: ERROR -- could not produce a plan JSON to run the tag-authz gate
safe-apply: a gate that cannot evaluate must not pass. Refusing to apply. (Fail closed.)
```
Cause was mine: I shipped `capture_day` REQUIRED with no default, and `safe-apply.sh:161` runs its
OWN var-less internal plan to feed comp-tagauthz. **A REQUIRED NO-DEFAULT VARIABLE MAKES A MODULE
UN-GATEABLE BY ANY WRAPPER THAT PLANS IT VAR-LESS.** The gate offered `TAGAUTHZ_OVERRIDE` -- taking it
would have been **bypassing a live gate because my own change broke its ability to evaluate.** Fixed
the module (`@4222b84da2`); CVO's later ruling removed the variable entirely.

**APPLIED TRUTH (live primitives, not the TF view):**
```
policy Resource : arn:aws:s3:::opal-estate-report/????-??-??/text-input/*
policy Action   : s3:PutObject ONLY
trust Principal : {"AWS":"arn:aws:iam::313476888478:user/Andrew_Berman"}  -- exactly one
```

**APPLIED BATTERY, both principals, each with its OWN separately-invoked positive control:**
```
capture-writer  ALLOW today/text-input          allowed
                DENY  past/text-input           (v0.2.1: allowed, DELIBERATE -- see below)
                DENY  today/signed-review       implicitDeny
                DENY  past+today manifest.json  implicitDeny
                DENY  DeleteObject / DeleteObjectVersion  implicitDeny
                DENY  today/kimi-report         implicitDeny
runner          DENY  today/text-input          implicitDeny   (provenance cross-deny)
                DENY  today/signed-review       implicitDeny
                CTRL  daily/  SEPARATE CALL     allowed        (proves it discriminates)
```

---

## Work Completed

| Commit | What |
|---|---|
| `3b9e54730a` | Andrew-direct record: pipeline UNPARKED + reframed as a Lifecycle Values DEPENDENCY |
| `1c3a75bfff` | **213 forged quotes removed** from the capture classifier |
| `888c2fd4e5` | **estate-capture-writer role** (Andrew-direct "yes on estate capture writer") |
| `4222b84da2` | sentinel default -- the un-gateable-module fix |
| `b04b62e67a` / `9cc9de137e` | deploy ledger closed; `pipeline_inventory.xml` v0.2.0 |
| `f3fa7601de` | **the leak fix** -- day segment pinned to `????-??-??` |
| `382e9971ab` / `9f7d04df07` / `1f32bb995d` | C3 spec v0.2 / v0.3 / v0.4 |
| `606a950334` | C3L.3 TO drafted (staged, dispatch HELD) |
| `fb96b284a2` | **C3L.3 steps 1-2: the walk agenda builder** + spec count correction |

### THE LEAK -- caught on the draft, before apply

CVO ruled the date-literal superseded by `*/text-input/*` (the literal carried a **daily apply
forever** -- a capture path whose grant renews only if a human remembers). Re-authoring to it:
```
PutObject  {day}/signed-review/text-input/evil.md   ->  ALLOWED
```
**IAM's `*` MATCHES `/`.** So `*/text-input/*` means *any key containing `/text-input/` at any depth*
-- the producer could write inside the reviewer surface by nesting a segment. **A producer that can
write the review surface can SIGN ITS OWN CAPTURE.**

>> **IT WOULD HAVE SHIPPED GREEN. The specified adjacent-subfolder DENY passes over it:**
>> `{day}/signed-review/x.md` is correctly DENIED while `{day}/signed-review/text-input/x.md` is
>> ALLOWED. **The battery reports a clean boundary over an open one, with every verdict in it
>> honest.** Both CVO's floor and ~A's rewritten battery would have returned a clean pass. <<

Fixed with `????-??-??` (pins the day to ten date-shaped chars). `~A` reproduced the leak
independently on a policy they authored. **CVO then probed MY fix** and named its residual (`?` also
matches `/`; every real subfolder is excluded by the shape of its own name -- **measured luck, not
design; a SIXTH subfolder must be re-probed**).

### 213 FORGED QUOTES

297 sessions / 197,757 rows / 3,628 stored. **The single most-repeated "utterance" in the store was
harness boilerplate** -- 130 `<local-command-caveat>` blocks filed as Andrew's words, plus 83
compaction preambles and 2 skill bodies (one 155,719 chars). **5.9% of the corpus was forged.**

Structural cause: **UNCLASSIFIED fired ZERO times across 197,757 rows.** A three-way fail-closed
classifier running as a BINARY one -- **no channel for "I don't know," so not-knowing rendered as
confidence, in the forging direction.** A bucket that never fires is not conservative; it is absent.

Control (5 predictions stated BEFORE running): caveats 0, compaction 0, UNCLASSIFIED reachable,
total 3415, **fixture-1 all 10 dedup_keys byte-identical** -- 213 forgeries removed, zero genuine
utterances moved.

---

## Decisions Made

1. **Stopped before authoring the IAM policy to check what principal the device actually uses.** It
   was `user/Andrew_Berman`, in `AdministratorAccessOpalCapital`, already ALLOWED on the capture key.
   Had I not checked, the battery would have run against the RUNNER role and returned **four
   methodologically immaculate greens on a role that does not do the writing.**
2. **Refused `TAGAUTHZ_OVERRIDE`** and fixed the module instead.
3. **Refused to self-authorize a principal adjacent to Andrew's identity** -- routed to CTO
   arch-gate; the answer came back in under an hour.
4. **Refused to propose a C7 bridge.** CTO ruled it restraint, not abdication: *abdication leaves the
   reader unable to act; restraint leaves them able to act AND NAMES WHO ACTS.*
5. **Did NOT push** when LD-0368 fired -- surfaced the audited override to Andrew as his call.
6. **Left the 29-vs-43 denominator parameterised** -- a spec pre-committing a scope Andrew is
   mid-deciding would have to be re-opened by his ruling instead of absorbing it.

---

## Findings issued / corrections taken

- **Against myself, x4:** "zero false positives" was true of 14 records and FALSE of the corpus ·
  "all four covered audit logs" when MANIFEST holds 13 (9 CRLF) · **a phantom cross-fabric blocker I
  inherited from a review answer and PROMOTED without testing** (CTO ran the lint: it passes) · the
  `REJECTED_NO_GOVERNANCE_ABOVE` class is **10, not 3** (tranche 2 added 7; nobody re-counted).
- **Taken from reviewers:** CVO narrowed my property-1 claim (refuted by its own case's resolution --
  the intent WAS data) and re-pointed property 3 at SOURCE-FIRST; COO corrected my
  fourth-consumer framing to *enhancement, not dependency*.
- **Issued:** the CRLF mechanism (source-confirmed, `core.autocrlf=true`, 9 of 13) · `/cloud-ops`
  instructing the BANNED watcher relaunch (CTO fixed + swept `@b6208f506a`) · **`~A`'s gate closed on
  a false negative** (they read the runner role, not the capture-writer).
- **CTO's gap, found by testing my phantom:** the rule bank's `intent_source` rejection is **PROSE**
  -- self-naming PASSES, garbage PASSES. Recorded at spec s.4.1 so the spec does not lean on a gate
  that is not there.

>> **THE SHARED SHAPE OF THE DAY: three times an instrument was correct, correctly read, and pointed
>> ONE OBJECT OFF.** CVO's hold would have re-proved the wrong object; my battery nearly ran against
>> the runner; ~A's gate read the runner. **The failure is never the measurement -- it is the NOUN.** <<

---

## Blockers

**None of mine, and the git blocker is CLEARED** (COO measured it; I confirmed the fix LANDED rather
than reverted -- 3 layers + positive control + live policy).

1. **[3.0.0_SA_CVO -- hold (a) v3, WHOLE]** Not lifted, and I did NOT ask for a partial lift.
   **BOUNDARY PROVEN / PATH UNPROVEN** -- the fallback mutant needs the capture write path, which does
   not exist. Until it runs, **a silent boto3 fallback to ambient admin is indistinguishable from the
   role working.** The role is not trusted for anything.
2. **[1.0.0_SA_CTO]** C3L.1 unissued -- gates C3L.3 steps 3-5. **Authorization cannot make a schema
   exist.**
3. **[Andrew]** retention ruling (`opal-estate-report`) · site-Z capture path · the 29-vs-43 walk
   denominator · whether to take the audited push override.

---

## Current State

**LIVE:** `arn:aws:iam::313476888478:role/estate-capture-writer`, created 14:51:57Z. Sole grant
`s3:PutObject` on `arn:aws:s3:::opal-estate-report/????-??-??/text-input/*`; trust names exactly
`user/Andrew_Berman`. Tags `estate-report-v0.2.0` / `v0.2.1`. Schedule `estate-report-0900et` DISABLED.
Bucket versioning Enabled, lifecycle = `abort-incomplete-mpu` only (no noncurrent expiry).
**Zero objects exist under any `{day}/text-input/`.**

**The runner role is DELIBERATELY unchanged** (`daily/*`, `manifest/*`, `logs/*`) -- the deployed
runner code still writes that layout, so flipping its grants alone would strand it. Recorded in
`iam.tf`'s header. *(~A still read it as un-applied -- the note is in the wrong place to be found
from outside; my defect, not theirs.)*

**BUILT:** `.tools/estate-capture.py` (classifier fixed) · `.tools/estate-capture-fixture1.py` (~A's
detector, my 10 keys, PASS at my post-fix HEAD) · **`.tools/c3-walk-agenda.py`** (C3L.3 steps 1-2;
12 of 14 surface, 2 quiet; AC2 payload scan = 0; fail-loud on an unreachable rule bank).

**SPEC:** `org/tier2_senior/0.7.0_AE_CloudOps~B/C3_LABELING_LAYER_SPEC_20260731.md` v0.5 -- 3 CVO
reviews + CTO arch-gate, all folded. **TO:** `C3L.3.kimi-loop-integration.md`, staged.

**POSTURE: idle at gate** under Andrew's hard pause, except where he authorized C3L.3 directly.
All work committed; 12 commits; nothing blocking the integrator.

---

## Next Steps

1. **[1.0.0_SA_CTO]** Issue C3L.1 -- it is now the critical path for the whole layer.
2. **[0.7.0_AE_CloudOps~B]** C3L.3 steps 3-5 on C3L.1's landing. **Do NOT build the return half
   against an invented schema.**
3. **[0.7.0_AE_CloudOps~A]** The applied battery + both mutants. **If the fallback mutant is not
   RUNNABLE (no write path), report NOT-RUNNABLE -- do not substitute a proxy.**
4. **[3.0.0_SA_CVO]** Hold (a) v3 lifts on their read of the mutants, not before.
5. **[Andrew]** the four open calls above.
6. **[1.0.0_SA_CTO]** the `.gitattributes` fix (lane-blocked from me; exact stanza delivered) and
   their own prose-gate `intent_source` gap.

---

## The thing worth carrying

**A CONTROL THAT PASSES ON EVERYTHING IS NOT A CONTROL, AND IT LOOKS EXACTLY LIKE ONE THAT WORKS.**

Three times today, in three different layers: the adjacent-subfolder DENY that passed over a nested
leak with every verdict honest; the classifier whose UNCLASSIFIED bucket never fired in 197,757 rows;
and my own agenda builder surfacing 14 of 14 on its first run. **In each case every individual
reading was TRUE.** The negative control is the only thing that separates them -- and in the third
case it was a criterion I had written into my own TO an hour earlier, which then fired on me.

The corollary I did worse at: **promoting an untested claim to a more load-bearing position makes it
look more verified while adding zero evidence.** I moved a phantom blocker from a footnote into a TO
table and described the move as rigour.
