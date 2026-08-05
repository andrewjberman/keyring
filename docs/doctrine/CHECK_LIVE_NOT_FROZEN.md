# CHECK LIVE, NOT FROZEN

**Ratified:** LD-0314. Member of the verification-doctrine family alongside
[`CONTROLS_OVER_CARE.md`](CONTROLS_OVER_CARE.md); the general form of Verification Laws #7
(*well-grounded ≠ freshly grounded*) and #8 (*a stale record says something false with authority*).
**Instances:** [`docs/references/CHECK_LIVE_NOT_FROZEN_INSTANCES_20260718.md`](../references/CHECK_LIVE_NOT_FROZEN_INSTANCES_20260718.md)
(`F-1`…`F-8`). Split 2026-08-05 on Andrew-direct.

---

> # A thing defined against a FROZEN reference drifts silently. The fix is to track LIVE state on a cadence.

> # CARDINAL RULE (Andrew-direct, 2026-07-30, VERBATIM): **"we can never ever have dependencies on frozen maps."**

**The cardinal rule is stronger than the doctrine above, and the escalation is the point.** The
doctrine says a frozen reference *drifts*. The cardinal rule says a frozen artifact **may not be a
DEPENDENCY**. Drift is tolerable in a document nobody computes from; it is not tolerable under a tool
that answers questions. **It converts "re-check your references" into "do not build a read path onto
something that cannot refresh."**

## The mechanism

Whenever an artifact is DEFINED-AGAINST a reference that can change — a snapshot, a schema, a coverage
set, a count, an abstraction of a live system — **it does not announce when reality moves past it.** It
keeps reporting the frozen answer with full authority while the truth diverges. **The failure is silent
by construction: nothing errors, the number just stops being true.**

**THE FAILURE SIGNATURE — a live half joined to a frozen half:**

> ### CURRENT VOCABULARY OVER STALE FACTS.
> A newly-added term renders as `UNASSIGNED` rather than as an error — so **the decay is silent AND it
> grows in proportion to how well the living half is maintained.** Every legitimate edit widens the gap.

*(`F-7`: a served artifact narrated as "LIVE fresh 2026-06-15" whose live truth was 45 days later.)*

## Scope — read this before applying it; it is narrower than it sounds

***Dependence* is the operative verb.** The rule forbids a frozen artifact being **depended on** —
computed from, resolved through, served out of. It does **NOT** forbid frozen artifacts existing, nor
copies, nor archives, nor evidence snapshots; pre-delete archives and session decks are frozen **BY
DESIGN** and correctly so.

> ### The discriminating question is never *"is it frozen?"* but ***"does anything DERIVE STATE from it?"***

A mirror that declares its vintage and is only READ is legal. **The same mirror becomes illegal the
moment a tool resolves through it.** *(`F-8` — without this refinement the rule collapses into "never
write anything down.")*

## The remedy is not a fresher snapshot

**Delete the snapshot for everything derivable and compile it at run time**, leaving only what
genuinely requires human judgment — which is then small enough to date, review and keep honest.

## How it binds

- **Ground APPLIED, never DESIRED**, for any *"did it land / is it true now"* claim.
- **Print the denominator** of every scan you reason from.
- **An abstraction of a live system needs a live-cadence back to its source**, or it silently ossifies.
- **A frozen reference is not a control** — the live-cadence check against it is.
- **A CONTROL'S OWN DENOMINATOR IS LIVE STATE TOO.** The allowlist / surface-map / threshold-set /
  coverage-list a control reads FROM needs the same live cadence, or **the control silently narrows
  what it can see and reads that narrowing as coverage.** Classify-all-and-print-exclusions, never a
  silent allowlist; prefer a live-derived denominator. *(`F-6`: the frozen-drift gate was itself
  frozen-drifted, mapping 1 of ~35 live files in its own hand-picked surface map.)*

## The sibling boundary — do not over-apply

**This is NOT licence to call every unmoving number a defect.** The inverse is equally binding: a
correctly-frozen value (Friday's T-1 AUM read on a Monday) is **HEALTHY**, and treating its age as a
staleness finding is the false-alarm CLAUDE.md NEVER#1 exists to prevent.

> **Do not reason from a frozen artifact's age in EITHER direction — ground the live state and count in
> the right frame.** Frozen-reference-drift (check live) and frozen-but-correct (don't false-alarm) are
> two faces of one discipline: **the answer is always to GROUND, never to infer from staleness.**

## Gate candidate — NAMED, NOT BUILT; do not read this as enforced

A commit/registration-time lint denying any comp-tool read path whose source resolves a **date-pinned
literal directory** (`logs/YYYY-MM-DD/`, `*-20YYMMDD/`) or any artifact on the declared frozen list
(`estate-coverage-resolver.json`, `stitch_graph.json`, `graph_contracts`). **Until it exists this is
prose, and prose taxes every session — so it is a build item, not a decoration.**

---

**Related:** [`CONTROLS_OVER_CARE.md`](CONTROLS_OVER_CARE.md) ·
[`INTENT_DENOMINATOR_SYNCHRONIZATION.md`](INTENT_DENOMINATOR_SYNCHRONIZATION.md) (a frozen denominator
is the §3 defect; SEMANTIC REDIRECT is its meaning-side twin) · CLAUDE.md NEVER#1 (the trading-calendar
default, the inverse error).

*Split 2026-08-05 by `4.0.0_SA_CRO` (120 → this + `F-1`…`F-8`). **Nothing cut — the evidence moved.***


---

## Grounded evidence in agent memory

> Citations of the form `memory/<slug>` root at the **agent memory DIRECTORY**
> (`~/.claude/projects/C--Users-AndrewBerman-Desktop-ajb-workspace/memory/`), **now under version
> control** (genesis `6843c2f`, 2026-08-05). Those records are the *grounded incidents* — typically
> 40–60 lines each with measured numbers; the law here is their compression. **Doctrine holds the
> law; memory holds the evidence.** Wired 2026-08-05 on Andrew-direct; the two corpora had **zero**
> links between them before that.

- `memory/feedback_a_stale_arm_does_not_go_quiet_it_goes_confident` — the failure signature, in one line.
- `memory/feedback_mtime_fresh_content_stale_trap_verify_data_as_of` — a fresh mtime over stale content.
- `memory/feedback_f6_vintage_anchor_s3_not_local_ls` — a local `ls` that can only ever report absent.
- `memory/feedback_ground_producer_live_state_for_deploy_strand_diagnosis` — ground APPLIED, not DESIRED.
- `memory/feedback_cdn_cache_staleness_masquerades_as_fe_bug` — staleness wearing another defect's costume.
- `memory/comptool_gap_comp_iam_reconcile_census_stale_06_03` — a control reading from a frozen census.
