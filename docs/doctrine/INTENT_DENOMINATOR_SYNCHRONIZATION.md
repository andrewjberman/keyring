# Intent–Denominator Synchronization — the generalized schema behind every coverage failure

**Status:** foundational doctrine (binds future behaviour, and is the design spine of NFRA_ONTOLOGY2
+ NFRA_ARCHTOOL). **Authored:** 2026-07-23, `1.0.0_SA_CTO~Z`, on Andrew's directive to generalize
the process. **Earned by:** five instances of one class caught in a single day (recorded in §6).

---

## §0 The directive, VERBATIM (Andrew, 2026-07-23)

> "the biggest error we uncovered from the analysis of the tool use was the coverage issue, which is
> emblematic of the denominator issue. I think the schema here is being able to concretely generalize
> the 'C(N)' layers, node edge motif system, and how information and activity flows up and down them,
> how change happens, the divergence between intent and configuration, and a foundational element of
> this is being able to synchronize intent with denominator. Our task here is to identify how this
> process can be generalized."

## §1 The two quantities, defined once

Every assertion the estate makes — a tool answer, a gate verdict, a freshness check, a completeness
claim, a review sign-off — operates over a set. Two versions of that set exist, and the entire
failure class is the gap between them:

- **INTENT** — the set the assertion is SUPPOSED to cover. What *should* be there. It is an
  OBLIGATION, and it is sourced from **above**: a governing level, a registry, a law, a contract.
- **DENOMINATOR** — the set the assertion ACTUALLY covers. What the instrument could see this run. It
  is a POPULATION, and it is enumerated from **below**: the concrete instances that exist.

An assertion is **SOUND** iff `DENOMINATOR ⊇ INTENT`. The **COVERAGE GAP** is `INTENT \ DENOMINATOR`
— what was owed but not seen. **A coverage failure is not a wrong answer; it is a correct answer over
an unstated denominator that is smaller than the intent.** That is why it reads green: the arithmetic
is right, the scope is silently wrong (MSBEFF Verification Law 6).

## §2 The defect, generalized: a denominator that is its own configuration

The pathological case — the one caught five times today — is when **INTENT and DENOMINATOR are drawn
from the SAME artifact.** The instrument checks a thing against a set the thing itself defines. Then
`INTENT ≡ DENOMINATOR` by construction, the gap is structurally 0, and the instrument **cannot fail
even when it is wrong**. CTO's mid-arc doctrine line names it exactly: *a completeness signal whose
denominator is its own configuration.*

- `comp-freshness` names one firm in its config and checks that firm → Cottonwood is never evaluated
  (RF-2). The config is both the intent and the denominator.
- `PUBLISH_MAP` reports `9/9 all_present` → 9 is the denominator AND the intent (RF-1).
- The telemetry appender's frozen `VERDICT_EXIT_TOOLS` → the list is both what it checks and what it
  checks against (M3).
- My M2 read the compiler-log projection as if it were the population (wrong artifact).
- The R1R3 TO named `comp-tools.yaml` — a curated subset — as the registry to derive the true set from.

**The fix is always the same shape: SEVER intent from denominator. Source intent from a governance
level ABOVE the artifact being checked; enumerate the denominator from the layer BELOW at run time;
and DECLARE the residual gap.** This is one principle, and it is what R1 (coverage-declaration),
PSTMRT (the completeness gate), and the registration invariant all instantiate. They are not three
fixes — they are one law applied at three sites.

## §3 The C(N) ladder as the two-directional flow this law rides on

The ratified ladder (`NFRA_ONTOLOGY_RULE_BANK.yaml`) is exactly the structure intent and denominator
flow along. Naming the two directions is the generalization:

```
            INTENT flows DOWN                         DENOMINATOR flows UP
        (obligation / what should be)             (population / what is)
   C3  SYSTEM      ──contract obligates──▶     ◀──union-find composes── C3
    │                                                                    ▲
   C2  MOTIF       ──shape obligates────▶      ◀──recurrence composes──  C2
    │                                                                    ▲
   C1  INTERACTION ──edge obligates─────▶      ◀──edges compose────────  C1
    │                                                                    ▲
   C0  FACT        ──type obligates─────▶      ◀──nodes are the atoms──  C0
```

- **UPWARD (`binds_up`, already in the rule bank) = COMPOSITION = where the DENOMINATOR comes from.**
  You enumerate what actually exists bottom-up: nodes → interactions → motifs → systems. The
  denominator of any assertion at layer N is *populated* from the real instances at N-1 and below.
- **DOWNWARD = OBLIGATION = where INTENT comes from.** A C3 system's contract obligates the C2 motifs
  it is composed of; a motif's shape obligates its C1 edges; a type obligates its C0 facts. The intent
  of any assertion at layer N is *sourced* from the governing declaration at N+1 and above.

**An assertion at layer N is sound iff the population reaching it from below covers the obligation
reaching it from above.** The coverage gap is the vertical distance between the two flows at that
layer. This is the whole schema, and it is recursive: every layer has the same soundness condition,
so the same instrument (declare intent-source, enumerate denominator, print the gap) applies
unchanged at C0, C1, C2, C3 — and at the D1/D2/D3 dynamic rails between them.

## §4 The dynamic rails are where intent and denominator get their GRAIN

The static ladder says intent and denominator are *sets* — but of WHAT? A freshness assertion's
intent is "every partition that should exist by the cadence contract"; its denominator is "every
partition that does exist." That question is unanswerable without a **grain** (partition, not
artifact) and a **path** (which upstream vintages feed it) and a **contract** (the cadence). Those are
exactly ONTOLOGY2's D1 (grain), D2 (flow/path), D3 (contract):

- **D3 (contract) SUPPLIES THE INTENT** — the cadence/completeness/canonical-source obligation *is*
  the "what should be there" for a dynamic assertion.
- **D2 (path) + D1 (grain) ENUMERATE THE DENOMINATOR** — walking the flow at the right grain *is* the
  "what is actually there."
- **Freshness, provenance, staleness-vs-frozen are the coverage gaps** between a D3 obligation and a
  D1/D2 population. Andrew's "freshness is downstream of flow" is exactly this: freshness is the
  intent–denominator gap on the flow rail.

So ONTOLOGY2 is not a separate idea from this doctrine — it is **the vocabulary that lets intent and
denominator be stated at the right grain for dynamic questions**, the same way the C(N) ladder states
them for structural ones.

## §5 How CHANGE happens under this schema

A change enters the estate at exactly one layer/rail (a new firm at the registry; a new field at C0; a
new consumer edge at C1; a cadence change at D3). **The failure mode is a change that propagates in
only ONE of the two directions:**

- Change propagates UP but not DOWN → the population grew but no obligation was updated → the new
  instance is unchecked (silent extra; the "unregistered firm" half).
- Change propagates DOWN but not UP → the obligation grew but the population wasn't re-enumerated →
  the new requirement is unmet and invisible (silent gap; the "onboarding firm #4" half, the entire
  MDPF class).

**Therefore the change-propagation law: any change re-synchronizes BOTH directions or it is drift.**
This is what the PSTMRT commit-time completeness gate enforces (a change touching a firm-keyed
structure must re-assert cardinality against the registry) and what R4's closeout/deploy triggers
enforce (a change to state must re-fire the drift/deploy check). Generalized: **a change is complete
only when its layer's denominator and its layer's intent have both been re-derived from it.**

## §6 Intent-vs-CONFIGURATION divergence is the special case, not a separate axis

DESIRED-vs-APPLIED (comp-iam parses TF = intent-as-config; the live plane = actual population) is
**one instance of intent–denominator divergence where the intent happens to be a local
configuration** rather than a governed obligation. It is more dangerous precisely because a config is
BOTH a declaration of intent AND, if you let it, a definition of the denominator — which collapses
them into the §2 tautology. The generalization subsumes it: **a configuration is a legitimate INTENT
source only when it is governed from above; the moment it also supplies the denominator, it is the
denominator-is-its-own-configuration defect wearing a config's clothes.** DESIRED-vs-APPLIED,
completeness, freshness, and coverage are therefore not four problems — they are one axis (intent vs
population) measured at four sites.

## §6b COROLLARY — YOUR PROBE IS AN INSTRUMENT TOO (~D + CVO~Z + ~A, 2026-07-23/24; probe SCOPE, probe SHAPE, and the firing CONDITION)

> **"A sample that misses a type reads EXACTLY like an absence of the property."**

The most common way a denominator under-reaches its intent in practice is a **broad scan that returns
nothing** — because a true absence and a sample that simply missed the relevant subset produce
**byte-identical silence**. The scan feels like evidence; it is only a denominator.

Observed twice in one day by the same agent, and **both times the corrected finding was NARROWER than
what was almost filed**:
- A 400-node property sample returned `file_path`-like = 0 → one step from filing *"kuzu carries no
  file paths at all."* The targeted per-type probe falsified it: `path` present **60/60** on
  Module/ReactComponent/Component, absent only on the pipeline types. The real finding — *partial*
  coverage — is far narrower and is the one that actually blocks.
- A mechanical scan for `graph.json` readers counted a **lint-rule message string** as a data source →
  flagged `comp-manifest-check`, *the linter that enforces the rule*, as a violator. (Sibling defect:
  text-matching prose cannot distinguish a rule from a breach of the rule — the same reason
  TRIGGER_LAYER clause 2 forbids prose lints.)

**The discipline:** a broad scan's silence licenses a QUESTION, never a CONCLUSION. Before recording
an absence, run the **targeted probe that would find the thing if it were there** — the positive
control, pointed at the specific subset the claim covers. An absence recorded from an untargeted scan
is a classification asserted at a coverage the evidence never reached, which is §2 in its most
ordinary clothing.

### The same cell, second face: a MALFORMED probe (CVO~Z, 2026-07-23, twice; 0.8.0 seconded)

Where the above is the probe's **scope**, this is the probe's **shape** — and it fails the same way:

> **A malformed probe does not fail loudly. It returns a clean, plausible number — a 0, an empty set,
> a byte-identical diff — that reads as a FINDING against a working tool.**

- A probe used `.md` fixtures against a script that globs `*.json` → returned *"0 open (0 PAST)"* on a
  **populated** directory. One step from filing *"the counter does not discriminate."* The instrument
  was fine; the probe was wrong. Caught by reading the target's **contract** first; the corrected
  probe then discriminated 2/2.
- A parity probe reported *"regen owed"* off a read that had **raced** an in-flight commit — the regen
  was already folded in. Retracted. Same shape one layer out: the CAUSE was grounded, the
  RESOLUTION-STATE was not.

**Why this direction is the expensive one:** a false finding against a *working* instrument spends the
author's time and the tool's credibility, and **a retraction never fully catches its own claim** —
asymmetric with a missed defect, which stays cheap until it bites.

**THE ANCHOR THAT MAKES THIS ENFORCEABLE, not exhortation** (and why it is a corollary rather than a
new prose cell): the estate already has the mechanism — **Rule 22a's positive control, run as a
SEPARATE invocation.** A positive control *is* probe-verification: **if your probe cannot find a
known-present instance, your probe is broken, not the target.** So the rule is not "be careful with
probes"; it is *run the control on your probe before you report on the instrument* — the existing law,
pointed one step back at the apparatus doing the pointing.

### The firing condition — WHEN to run the control, since you cannot run it on every row (~A, 2026-07-24, comp-routes MACHINEFLAG sweep)

The anchor above says *run the positive control on your probe*. The unstated problem: **a control on
every row is not affordable** — a sweep over 64 flag-sites cannot positive-control all 64, so "always
control your probe" collapses into "control the probe sometimes," and *sometimes* is where the misses
live. ~A's incident supplies the cheap, always-available trigger.

> **WHEN YOUR INSTRUMENT REPORTS A DEFECT IN SOMETHING YOU HAVE INDEPENDENT GROUND TRUTH ON, CHECK THE
> INSTRUMENT FIRST.**

The MACHINEFLAG sweep's exerciser shelled out via `subprocess.run(['bash', launcher, ...])`, which on
this host Windows-resolves `bash` to the **System32 WSL stub** (the CLAUDE.md-named class — *"a
python-spawned bash … REPORTED SUCCESS EVERY TIME"*). Every one of the 10 tools it "ran" emitted a
UTF-16 *"no installed distributions"* error, and the classifier read that error text as PROSE. Result:
**10 PROSE_FALLBACK findings against 10 tools — several of them peers' work — every one false, and each
carrying a source-derived denominator (64 sites / 49 files) that would have made the ten accusations
look rigorous.** The instrument built to find "confident output from a broken retrieval" *was* one, and
it was aimed OUTWARD.

It was caught because **one of the ten rows was `comp-routes trace --json`, which the author had built
that session and verified at HEAD an hour earlier.** A finding that contradicts ground truth you already
hold is either a discovery that overturns what you know — rare — or a broken instrument — common. Treat
it as the second until proven the first: it is the one row you cannot be fooled on, so it is the cheap
control you already possess. The held-truth contradiction **costs nothing** (you are not manufacturing a
positive control; you already hold the answer), and it fired here on row 1 of 10, before a single false
finding shipped.

**The operational rule this yields:** you need not control every row, but a finding that contradicts
*any* fact you independently hold **halts the whole census until the instrument is cleared** — because a
runner that lied about the row you know cold lied about the rows you don't. One trusted row disciplines
the entire denominator. *(The mechanical residue — a lint for bare `bash`/`/bin/bash` / `subprocess.*bash`
in Python that does not route through the canonical `git_bash()` resolver — is a gate candidate: the
CLAUDE.md NEVER already exists in prose and was violated anyway by a careful agent under load, which is
the standing argument for a gate over a rule.)*

## §7 The generalized PROCESS (Andrew's ask, answered)

**To synchronize intent with denominator — at any layer, for any assertion:**

1. **NAME THE LAYER/RAIL** the assertion lives on (C0–C3 for structure; D1–D3 for dynamics). An
   assertion that cannot name its layer is answering an unknown question.
2. **SOURCE INTENT FROM ABOVE** — a governed obligation one level up (registry, contract, law), never
   from the artifact being checked.
3. **ENUMERATE DENOMINATOR FROM BELOW, AT RUN TIME** — the real instances, never a frozen or curated
   list, never the same artifact that supplied the intent.
4. **DECLARE THE GAP** — `INTENT \ DENOMINATOR`, printed, every run. A zero gap is a claim that must
   be shown, never assumed. An instrument that cannot compute the gap renders UNKNOWN, loudly.
5. **ON CHANGE, RE-DERIVE BOTH** — a change re-populates the denominator AND re-checks the intent, or
   it is drift.

**This process is layer-agnostic by construction** — which is the generalization. The same five steps
define a coverage declaration (R1), a completeness gate (PSTMRT), a freshness check (ONTOLOGY2 P3), a
registration invariant, a review sign-off, and a synthesized tool's self-test (ARCHTOOL P4). NFRA_ARCHTOOL's stability grader is this process pointed at itself: a pattern is stable enough to
build a tool from **only when its intent source is governed (law, not habit) and its denominator is
enumerable (bounded, not open)** — the §7 preconditions, graded.

## §8 The instances that earned this (all 2026-07-23, all caught by controls, not care)

*(This heading read **"The five instances"** while the list held six, and then seven. A hand-maintained
count beside a growing enumeration is the frozen-denominator defect **committed by the file that
defines it** — the numbered list is the denominator; a prose digit beside it is a second, unsynchronized
copy. It is deleted rather than corrected: **the fix for a frozen count is never a fresher count.**)*

1. **M2** — measured the compiler-log projection, not the source jsonl. Denominator was the wrong
   artifact. Caught by: Andrew asking "is this the wrong place?"
2. **CVO~Z tick-29** — census knew 2 of 3 rule-bank mapping surfaces; reported completeness over its
   own coverage. Caught by: the tick-25 methodological note it had itself banked.
3. **The telemetry appender** — frozen `VERDICT_EXIT_TOOLS`; intent ≡ denominator. Caught by: the M3
   audit measuring against the live contract surface.
4. **The R1R3 TO** — named a curated subset (`comp-tools.yaml`) as the registry, inside the TO whose
   subject is that defect, ratified by three cataloguers. Caught by: the TO's own if_mismatch mandate.
5. **CVO~Z tick-30** — first predicate flagged 5 axis-bound edges as "missing"; they carried `axis:`
   on a surface the one-read predicate didn't know. Caught by: reading the block header.
6. **comp-iam rc3 laundering (SOURCE-CONFIRMED, the live instance the schema PREDICTED)** — the retired
   frozen `VERDICT_EXIT_TOOLS` blanket-classified comp-iam as a verdict tool, so `rc3` — documented in
   `iam_cli.py:858/:900` as *"a COVERAGE refusal: nothing was compared, so nothing is concluded"* —
   rendered as findings. The M3 derivation reclassified `rc3 → REFUSE`; **CVO~Z confirmed at source on
   the committed vintage @`926487fe6` (read the code, not the report).** This is the defect of §2 in its
   purest observed form — a classifier whose denominator (what counts as a finding) was its own frozen
   configuration, laundering "I could not evaluate" into "here is a finding" — and it was caught by the
   fix for §8.3, on the day the doctrine was written, *inside the instrument that had been committing the
   class.* The count LIMB (how many historical rows) is separately gated on a re-baseline enumeration
   run off the plane that carries a real exit code (`comp-tool-runs.jsonl`, not the rc-less md log — the
   §8.1 wrong-artifact lesson applied to the re-baseline itself).

7. **The subcommand backfill — DECLARED ≠ REACHABLE (SOURCE-CONFIRMED, and the sharpest instance yet,
   because it occurred *inside this program's own remediation pass*)** — the targeted backfill closed
   the router's law-mandated coverage gap by writing `comp-iam simulate` / `comp-iam reconcile` /
   `comp-pipescript postdeps` into `tools_index`. **`comp-which` never reads `tools_index`.**
   `.tools/comp-which:1006-1010 @e6115fa66` scores over `entries[].{use_case,id,tool}` and displays
   `entries[].canonical_call`; `tools_index` has **no consumer on the routing path.** So the three
   CLAUDE.md-mandated calls were declared and **unroutable** — and the Rule 22a query ("can this role
   write to a brand-new bucket") kept routing to `comp-iam service`, *the DESIRED-only tool that same
   rule calls **necessary but not sufficient** for a new ARN.*
   **CORRECTION, +5h, AND IT IS THE SAME CLASS COMMITTED BY THIS ENTRY'S OWN AUTHOR — the mechanism
   above is a PARTIAL READ.** `entries[]` is only the **fuzzy backstop**; it can influence a fallback
   but **never creates a routing candidate.** `comp-which` *ranks* off a **curated vocabulary table**
   inside `.tools/comp-which`, and the ranked pool is **68 (tools), not 105 (entries).** So **BOTH**
   declaration surfaces are unroutable, and the prescribed remedy that followed from the partial read
   — *"give the three calls `entries[]` rows"* — **was built, behavior-tested, and surfaced nothing.**
   The author had **already read the docstring naming two layers** (*"1. CURATED high-confidence
   rules … 2. MANIFEST-FUZZY backstop"*), grounded **one**, and then wrote and reasoned about *"the
   router."* **A mechanism confirmed on one of two layers is not a confirmed mechanism — it is a
   denominator that happens to contain a true sentence.** Rule 22's `file:line @ commit-ish` was
   satisfied *exactly*, and the citation was still not the whole mechanism: **a correct citation
   bounds what you verified, never what is there.** Caught only because the acceptance had been
   written as BEHAVIOR — the lane re-ran the four queries, got nothing, and refused to report done.
   *The instruction caught its own author's error, which is the only kind of control worth having.*
   The INTENT was "an agent following
   CLAUDE.md can REACH the mandated call"; the DENOMINATOR enumerated was "declarations present in
   `tools_index`." **Two different populations, and the gap between them was the entire finding.**
   Caught by: the acceptance criterion being set to **router-reachability, not registry-presence**, and
   the gate-holder running the four behavioral queries rather than reading a registry diff. The lane
   reported honestly — *"Declaration: closed. Ranking: unverified"* — which is why this is a finding
   about the work and not about the agent: **the criterion caught it because the criterion was written
   at the right grain, and the lane declined to claim the half it had not measured.**
   **AND THE ESTATE HAD ALREADY LEARNED THIS ONE GRAIN UP.** `comp-which:708-711` (2026-07-14): *"these
   sat on disk for weeks while agents logged 'no comp-tool answers this' — registration without
   vocabulary is registration in name only."* Same class, at **tool** grain, already fixed, already
   gated (`.tools/comp-which-routing-test.py`, live in `commit_gate_runner.py`). Then the declaration
   surface grew a **finer grain** — subcommands — **and the invariant did not follow it down.**
   >> **A GUARD'S COVERAGE GOES STALE THE MOMENT THE THING IT GUARDS GETS MORE GRANULAR.** The guard
   kept passing, correctly, over a population that had quietly stopped being the whole population. This
   is the §5 change-law failure in its most deniable form: nobody edited the guard, nobody edited the
   law, and the gap opened anyway — **because a new grain is a change to the DENOMINATOR that no diff
   shows.** A registration invariant must be re-derived against the *current* grain of the surface, not
   the grain it was written for. <<

8. **CVO~Z's truncated probe — the firing condition validated AT THE VERIFIER'S OWN APPARATUS, same
   session it was written** — verifying the MACHINEFLAG census (whose central claim is *"instruments
   misread valid JSON as prose"*), CVO~Z's verification probe did exactly that: `head -c 300 |
   json.loads` truncated valid JSON mid-object, so the parser reported *"NOT JSON"* on output that
   visibly began `{"artifact":…}`. Caught by: **the §6b firing condition banked hours earlier** — *it
   looks like JSON, the parser says no → check the probe first* — fired at the verifier's own tool, on
   the exact class under verification, pre-report. The coincidence is the lesson CVO~Z named: *the
   probe-is-an-instrument doctrine is not about other people's tools.* A doctrine cell catching its own
   author's verification apparatus, the same day, is the strongest form the thesis takes.

**Every one was caught by a control, none by the author being careful — including the ones authored by
the agents who had, that same day, written the doctrine against them.** That is not a coincidence to
apologize for; it is the proof the schema must be structural. Care does not scale down the recurrence
rate of a class its own cataloguers keep committing. A synchronized intent–denominator, declared and
gap-printed at every layer, does.

**Related:** `CONTROLS_OVER_CARE.md` · `TRIGGER_LAYER.md` (a finding lands as a gate; this says what
the gate must check) · `NFRA_ONTOLOGY2_PRD.md` (the rails that grain intent+denominator for dynamics)
· `NFRA_ARCHTOOL_PRD.md` (the process, generalized into tool synthesis) · `NFRA_PSTMRT_PRD.md` (the
first site the law was enforced) · `docs/references/MDPF_POSTMORTEM_20260722.md` (the incident that
started it).
