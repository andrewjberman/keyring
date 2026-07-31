# MECHANISM LAWS -- the fourteen shapes an assertion goes wrong in

**Subject: WHERE AN ASSERTION SITS.** Fourteen mechanisms, derived from the incident corpus, each
stated as a law with the question that exposes it and the gate or test that absorbs it.

**Source corpus:** `org/tier0_exec/0.0.0_AB_MSTR/deliverables/INCIDENT_TAXONOMY/` (13 files;
`00_SUMMARY.md` s.2.1 for the mechanism distribution, `AXES.md` AXIS 4 for the definitions and the
exposing questions). **Built:** 2026-07-31 by `0.8.0_AE_CloudComp~C` under NFRA_VELOCITY WS-C8
artifact 1. **Gate:** `1.0.0_SA_CTO~Z`; **verify:** `3.0.0_SA_CVO~Z`.

---

## THE BOUNDARY -- AND IT IS THREE-WAY, NOT TWO

> **THIS DOCUMENT** -- `MECHANISM_LAWS.md` -- holds **WHERE AN ASSERTION SITS**: the fourteen ways a
> claim comes to be wrong about its own subject.
>
> **`docs/doctrine/CONTROLS_OVER_CARE.md` SECTION III** holds **HOW AN INSTRUMENT LIES** -- III-a
> through III-g, instrument fallibility with measured instances. **The M-taxonomy does not type
> instrument fallibility, by construction**, so section III is not a subset of this file and this
> file is not a superset of it. Read both.
>
> **AND THERE IS A THIRD FAMILY, WHICH HAS NO HOME TODAY: HOW A RULE OR ROLE FAILS TO BE ONE.** How
> a rule is drafted (name the PROPERTY, not the EVENT), how a procedure is drafted (a step naming no
> actor is not a step), how a role is constituted (first exercised by a non-owner). **That family is
> covered by NEITHER this document NOR CONTROLS_OVER_CARE III.** It is named here as an open gap and
> deliberately not filled -- creating its home is not authorised by this artifact.

**Why the third is stated rather than quietly omitted:** a doctrine head whose first act is a
two-way boundary would assert a completeness that is false. Measured (`3.0.0_SA_CVO~Z`,
2026-07-31, against `CONTROLS_OVER_CARE.md`, 95578 B): the rule-and-role concepts return **six
zeros** -- `"names no actor"` 0, `"actorless"` 0, `"non-owner"` 0, `"role whose first"` 0,
`"property, never the event"` 0, `"pre-commitment"` 0 -- with **positive controls confirming the
scan works** (`"control"` 103, `"instrument"` 37) and the concepts absent under broader wording too
(`"actor"` 1, `"who does"` 0). The family is genuinely unhomed, not merely differently worded.

> **AND ONE OF THOSE UNHOMED LAWS IS AN INSTANCE OF ITSELF:** *a step that names no actor is not a
> step* -- and that law currently has no owner and no home. A doctrine corpus should be able to say
> that out loud, so it is said here.

---

## THE DENOMINATOR PROBLEM -- READ BEFORE QUOTING ANY NUMBER BELOW

**There is no canonical per-incident mechanism mapping, and every headline figure in circulation is
computed on an unstable base.** From the corpus's own correction (`00_SUMMARY.md`, custodian
`0.0.0_AB_MSTR`, arithmetic by `3.0.0_SA_CVO~Z`):

- The s.2.1 mechanism counts **sum to 219**, not 210.
- The share column is computed on **210**, so it **totals 104%**.
- The 219-210 = 9 gap is **NOT** multi-coding: exactly **1** multi-coded incident was measured.
- Across five parse methods the denominator is **204 / 208 / 210 / 219 / 221** -- five methods, five
  answers.
- **The "210-row instance table" is a PROPOSED move (s.5). IT DOES NOT EXIST AS AN ARTIFACT.**

> **THEREFORE: the `n` column below is a count of ASSIGNMENTS, and the assignment total is 219.**
> It is NOT a count of incidents and NOT a share of 210. **"55%" and "52.5%" are equally misquotes.**
> What is durable is the CONCENTRATION -- M6+M1+M2+M5 dominate under *every* parse method, in the
> region of **52-55%** -- and that range is the honest form. Cite the artifact and the parse, never
> a bare point figure.

**Reconciliation shown:** 42+29+22+22+19+16+14+14+11+10+7+6+5+2 = **219 assignments** across 14
mechanisms. Against a stated incident population of 210 that is a 9-assignment excess with 1
measured multi-code, leaving **8 unreconciled** -- which is the structural gap, not an arithmetic
slip, and is what WS-C8's instance table is chartered to fix.

### THE MERGE NOTE -- why merged instances do NOT change any `n`

**WS-C8 artifact 2 merged three staged laws into this file as INSTANCE ROWS, and NONE of them
increments the `n` on its host mechanism.** The `n` values count **ASSIGNMENTS FROM THE INCIDENT
TAXONOMY** -- one population, one parse, already unstable at 219-vs-210. The merged rows are
**observations from a different corpus** (`WS-C8_STAGING_LAWS_DERIVED_20260731.md` @dd5d53314),
collected by different seats under a different method.

> **ADDING THEM TO `n` WOULD BE M1 COMMITTED BY THIS DOCUMENT** -- silently pooling two populations
> under one denominator so that no reader could afterwards say which count came from where. **The
> merge is additive in CONTENT and inert in ARITHMETIC**, and it is labelled that way on every row so
> a later reader cannot mistake a merged instance for a taxonomy assignment.

**Zero instances were lost in the merge:** each staged law's substance, its exposing question and its
named counter-instrument are carried into the host mechanism's row; nothing was summarised away and
nothing was deleted from the source, which remains authoritative at its pin.

---

## THE FOURTEEN

Ordered by assignment count. **Every row's gate-or-test cell is populated**; where no gate is
possible the reason is stated rather than left blank.

### M6 -- AXIS / GRAIN MISMATCH  (n=42 assignments, the largest)
**LAW:** An instrument sampled an axis the defect does not live on. The measurement is clean and
answers a different question than the one asked.
**EXPOSING QUESTION:** *State the grain of every input and of the conclusion.*
**GATE-OR-TEST:** `type_tuple` grain/rail/scope declaration (rule bank `type_tuple`), enforced by
comp-manifest-check's stage-2 vocab invariant -- an assertion that cannot name its grain is
machine-detectable. **PARTIAL: it types TOOL declarations, not ad-hoc agent claims.**
**INSTANCES:** 42 assignments. Live 2026-07-31: a per-plane edge census reported the frontend as
cloud because node `layer` and edge `layer` disagree (WS-C3, `29b5ccacc`).

### M1 -- SHARED DENOMINATOR  (n=29)
**LAW:** The expectation was derived from the measured thing. Both sides of the comparison trace to
one authority, so the gap reads zero by construction.
**EXPOSING QUESTION:** *Where did the EXPECTED side come from, and is that the same authority that
defines the population?*
**GATE-OR-TEST:** `INTENT_DENOMINATOR_SYNCHRONIZATION` s.2 -- intent from ABOVE, denominator from
BELOW, gap printed every run; realised in the rule bank's `completeness` axis (population
read-from-file from a governed registry, never from the artifact checked).
**INSTANCES:** 29 assignments. Includes the correction above -- a distribution over *assignments*
compared to a percentage over *incidents*, with nothing reconciling the two.
**MERGED STAGED-LAW INSTANCES** (WS-C8 artifact 2; NOT added to the 29 -- see merge note):
`L-2` *"a self-chosen denominator cannot refute the instrument that chose it"*
(`WS-C8_STAGING_LAWS_DERIVED_20260731.md` @dd5d53314) -- **denominators you do not own are the only
ones that can contradict you.** Three 2026-07-31 findings were caught by no other means: a strict
parser silently dropping the 4 rows whose mechanism column is an em-dash (precisely the incidents
the taxonomy could not classify); a naive grep scoring 14 disposition rows as incidents; and the
**219**-vs-210 share column, found only by summing a table neither author maintained.
*Exposing question, carried from L-2:* **whose count would have to be wrong for mine to be right?**

### M2 -- SHAPE-MATCH, WRONG CONTENT  (n=22)
**LAW:** Retrieval broke and returned the right TYPE. An error message counted as content; an empty
result read as a true zero.
**EXPOSING QUESTION:** *Could this have returned non-zero? Run the positive control.*
**GATE-OR-TEST:** the positive control, plus CLAUDE.md's retrieval rule -- put the control on the
RETRIEVAL, not the pattern (`| wc -l`, never `grep -c`). **A named practice, not an automated gate.**
**INSTANCES:** 22 assignments. Live 2026-07-31: `git stash show -p <ref> -- <path>` returned 91
bytes of error text and every token grep then returned 0; only a structure control caught it.

### M5 -- SCALAR COLLAPSE  (n=22)
**LAW:** A count, an rc, or a boolean summarised the population away. The number survived; the
population it was computed over did not.
**EXPOSING QUESTION:** *What population did it pass OVER, and can it name what fell outside?*
**GATE-OR-TEST:** the printed-denominator convention + the boundary-report registration invariant
(comp-output-contract: address space, traversal residue, failure direction as required output).
**INSTANCES:** 22 assignments. Live 2026-07-31: a census parse using `[A-Z_]+` silently dropped
every edge type containing a digit; caught only because the total failed to reconcile against the
instrument's own count.

### M14 -- PROSE-AS-CONTROL  (n=19)
**LAW:** The finding's only carrier is text that nobody is required to read. Nothing halts on it.
**EXPOSING QUESTION:** *Can this fail? What stops on it?*
**GATE-OR-TEST:** TRIGGER_LAYER doctrine -- a finding lands as a GATE or an OWNED BLOCKING ITEM,
never a note. **NO AUTOMATED GATE POSSIBLE for the general case: detecting that a document is
un-read requires knowing who was obliged to read it, which no instrument holds.**
**INSTANCES:** 19 assignments. Live 2026-07-31: a live dispatch existing only as an untracked file
(the CORE task orders, committed for durability at `862a80438` once surfaced).
**MERGED STAGED-LAW INSTANCES** (WS-C8 artifact 2; NOT added to the 19 -- see merge note):
`L-11` *"a check that cannot block what it measures is not a gate, it is a comment"*
(`WS-C8_STAGING_LAWS_DERIVED_20260731.md` @dd5d53314) -- **if the measurement and the action share a
command block, the measurement has no path to stop the action; it will print a correct number beside
a completed mistake.** `0.7.0_AE_CloudOps~Z` ran an ASCII check on a deliverable, **the check printed
the count and the commit executed anyway**, because check and commit were one invocation. **The
instrument worked perfectly and changed nothing.** *Placement, not logic* -- the sharpest variant of
this mechanism, because unlike the other instances the control here is CORRECT and still inert.
*Exposing question, carried from L-11:* **if this check FAILED right now, would anything stop?**
*Counter-instrument:* the check runs as a **separate, blocking step** whose exit status the action
depends on (their `ab6850527` is the first commit where it did).

### M8 -- TEXT vs SEMANTICS  (n=16)
**LAW:** A mention scored as a use. The string was present; the value was never read.
**EXPOSING QUESTION:** *Does it READ the value, or merely contain the string?*
**GATE-OR-TEST:** AST-based checks over text matching (`ds-precommit-check` undefined-name scanner;
comp-iam's AST call-site tracer). **PARTIAL and known-blind: the tracer misses derived-object and
resource-style two-hop calls, so its silence is not absence.**
**INSTANCES:** 16 assignments. Live 2026-07-31: a token-presence check would have flagged a
correction that merely QUOTED the withdrawn claim -- token-USED vs token-NAMED, hit three times.

### M7 -- SELF-REPORT AS POINTER  (n=14)
**LAW:** The subject of the measurement chose its own target. The instrument measured what it was
handed.
**EXPOSING QUESTION:** *Did I establish the input from the CALLER's side?*
**GATE-OR-TEST:** CLAUDE.md NEVER-rule -- never trust a producer's self-report or rc=0; verify
against the SERVED artifact or live state. Realised as the RAVC evidence requirement (commit hash,
artifact path, tool output).
**INSTANCES:** 14 assignments. Live 2026-07-31: a gate PASS issued only after the gate owner re-ran
the producer's own control battery rather than accepting the report.

### M11 -- TAUTOLOGY  (n=14)
**LAW:** Both sides of a check are the same computation. The check cannot fail.
**EXPOSING QUESTION:** *What would have to happen for these two sides to disagree?*
**GATE-OR-TEST:** the MUTANT -- mutate the subject and require the control to redden. **A practice
with no automated enforcement; a control never mutated has never been tested.**
**INSTANCES:** 14 assignments. Live 2026-07-31: a lifecycle gate whose reading-nothing and
reading-correctly produced identical output while the registry was all-default.
**MERGED STAGED-LAW INSTANCES** (WS-C8 artifact 2; NOT added to the 14 -- see merge note):
`L-5` *"convergence is not corroboration when the converging arguments share an unmeasured premise"*
(`WS-C8_STAGING_LAWS_DERIVED_20260731.md` @dd5d53314) -- **N arguments agreeing is evidence only if
their premises are independent; six grounds resting on one unchecked fact is one ground.** Twice in
six hours: `3.0.0_SA_CVO~Z` refused six converging grounds and ruled from the ratified substrate --
**ground 1 later measured FALSE**, so a ruling on the convergence would have been void; and they
refused to let *"all 7 keep-dormant belts"* stand as corroborated by its own plausibility. Its
arithmetic twin: *"the concentration survives the re-bucket"* would have been an artifact of
non-independent axes -- **M6 and M5 both being grain mismatches is one fact stated twice, not two
facts agreeing** -- which is this mechanism reaching the taxonomy's own summary statistics.

### M9 -- DESIRED vs APPLIED  (n=11)
**LAW:** A configuration read was used for a behavioural claim. Declared and landed were treated as
the same fact.
**EXPOSING QUESTION:** *Did I exercise the path that fails if the claim is false?*
**GATE-OR-TEST:** CLAUDE.md Rule 22a -- STATE/IAM claims cite both the DESIRED view and the live
primitive; BEHAVIOUR claims EXERCISE the path. Withheld GO by the cert owner if absent.
**INSTANCES:** 11 assignments. The rule's own origin: comp-iam's DESIRED-only parse read as APPLIED.

### M3 -- PROXY FOR THE THING  (n=10)
**LAW:** A hash, key, partition or name stood in for content. The proxy moved independently of the
thing it named.
**EXPOSING QUESTION:** *What is this a function of that I have not keyed on?*
**GATE-OR-TEST:** grain declaration at the `(bucket, key)` / `(node_type, position_key)` level --
the governed grouping key, not a name prefix. **PARTIAL: enforced where a governed key exists,
absent elsewhere.**
**INSTANCES:** 10 assignments. Live 2026-07-31: two nodes sharing a name prefix are NOT siblings;
`position_key` is the governed key and a prefix match is not a substitute for it.

### M10 -- UNREACHED BRANCH  (n=7)
**LAW:** The exercise never entered the governed domain. The test passed without touching the thing
the claim is about.
**EXPOSING QUESTION:** *Did my input actually reach the branch the claim is about?*
**GATE-OR-TEST:** a fixture carrying the NON-DEFAULT value, plus a mutant proving the branch can
redden. **NO AUTOMATED GATE: coverage tooling reports line entry, not whether the input was
discriminating.**
**INSTANCES:** 7 assignments. Live 2026-07-31: a polarity check that PASSED VACUOUSLY on an empty
enum, because the field it searched had been renamed.

### M4 -- COPY DRIFT  (n=6)
**LAW:** A restated literal diverged from its source. Both copies read as authoritative.
**EXPOSING QUESTION:** *Is this a copy or a read? Enumerate the copies.*
**GATE-OR-TEST:** the MIRROR CONTROL -- a reader asserts its own field list against the schema it
depends on (`comp_legacywriter` C9l vs the rule bank's `contract_record.required`, `88bf8f7bb`).
**Covers ONE reader; there is no general copy-enumeration gate.**
**INSTANCES:** 6 assignments. Live 2026-07-31: a `scope`->`locality` rename fixed in the bank and
hit hours later from the reader side, with no instrument connecting the two.

### M12 -- BORROWED SENSITIVITY  (n=5)
**LAW:** It works only while a person keeps doing something. The control's discrimination is
supplied by a human habit, not by the mechanism.
**EXPOSING QUESTION:** *What has to keep happening, by a person, for this to keep working?*
**GATE-OR-TEST:** **NO GATE POSSIBLE -- by construction.** The dependency is on human behaviour
outside the system; an instrument cannot detect that its own sensitivity is on loan. The only
counter is the exposing question asked at design time, and the `revalidate_by` decay convention,
which forces re-confirmation on a clock rather than on memory.
**INSTANCES:** 5 assignments.

### M13 -- POLARITY / NAMING INVERSION  (n=2)
**LAW:** The label asserts the opposite of the behaviour. The name reads as safety while its
presence does harm.
**EXPOSING QUESTION:** *Does the name describe what its PRESENCE DOES?*
**GATE-OR-TEST:** token-collision refusal at ratification -- a token already occupied on another
axis may not be reused (rule bank `lifecycle.token_hygiene`; v1.6 `222b0c27c` Andrew-ratified).
**Covers ratified vocabulary only.**
**INSTANCES:** 2 assignments. Live 2026-07-31: `SUPERSEDED` and `ORPHAN` were occupied on the
ratified variance axis with different definitions, and a gate naming one concealed that the other
was ungated.

---

## SHAPING CORPUS (declared, per the held-out fence)

`org/tier0_exec/0.0.0_AB_MSTR/deliverables/INCIDENT_TAXONOMY/` (`00_SUMMARY.md` s.2.1, `AXES.md`
AXIS 4); `docs/doctrine/CONTROLS_OVER_CARE.md` (READ FOR BOUNDARY ONLY -- not collapsed into this
file, see below); CLAUDE.md Rules 22 / 22a; rule bank `NFRA_ONTOLOGY_RULE_BANK.yaml` at v1.8;
`3.0.0_SA_CVO~Z`'s six-zero measurement of the rule-and-role family; live 2026-07-31 instances from
WS-C1 / WS-C3 and their commits, cited inline.

**NOT drawn on, and not opened: `ADVI_PERFORMANCE`, `MDPF_GLOBAL`.** They are the held-out set
(rule bank `dynamic_rails.held_out_fence`); no surface of either appears here.

## WHAT THIS ARTIFACT DELIBERATELY DOES NOT DO

- **It does not collapse `CONTROLS_OVER_CARE.md` section III into the M-classes.** That direction is
  impossible: the M-taxonomy types where an assertion sits and does not type instrument fallibility,
  which is exactly what section III is. The TO's `collapse-source` reference asserting that direction
  is superseded (`1.0.0_SA_CTO~Z`, 2026-07-31 150036Z).
- **It authors NO new law.** Every mechanism here is one of the corpus's fourteen. Live 2026-07-31
  observations appear as INSTANCES under existing laws, never as new entries.
- **It merges no staged L-id.** Those are later artifacts.
- **It re-points nothing.** CLAUDE.md Rules 22/22a continue to point at `CONTROLS_OVER_CARE.md`; a
  re-point is a law surface crossing the main-CTO seam and is not done here.

## PRE-COLLAPSE BASELINE (`docs/doctrine/`, measured 2026-07-31 before this file existed)

```
   8692  A_VALUE_MUST_CARRY_ITS_CLAIM.md      95578  CONTROLS_OVER_CARE.md
   9449  CHECK_LIVE_NOT_FROZEN.md             24236  INSTRUMENTS_AND_AXES.md
  28707  INTENT_DENOMINATOR_SYNCHRONIZATION.md 1593  README.md
   4138  TRIGGER_LAYER.md
 172393  TOTAL, 7 files    (MECHANISM_LAWS.md did not exist)
```

**Consumer enumeration for `CONTROLS_OVER_CARE.md`, run before authoring: 87 consumers across
25144 tracked files** (`git grep -l`, self excluded). `comp-which` could NOT answer the consumer
question -- it returned tool candidates (comp-estate, comp-pipescript, comp-cache, top 3 of 68) --
so this was enumerated by hand with the denominator printed, as the mandate directs. **CLAUDE.md is
among the 87**, which is why this artifact re-points nothing.
