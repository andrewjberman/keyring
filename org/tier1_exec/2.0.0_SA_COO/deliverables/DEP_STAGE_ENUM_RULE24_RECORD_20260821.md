# `dep_stage` — project-JSON stage enum + its Rule-24 four-postulate record

**Author:** 2.0.0_SA_COO · 2026-08-21 · **Authority:** Andrew's ratification of the DIRECTIVE
EXECUTION PIPELINE (2026-08-21, *"I agree with this framework lets get it formalized properly"*);
CTO GO assignment 64959 (*"pipeline_stage field on the project JSON schema (Rule-24 test on the enum)"*).
**Archetype:** SCHEMA AUTHORING — Rule 24 binds, and this record IS the postulate test, not a summary of one.

## 0. TWO FINDINGS THAT CHANGE THE ASSIGNMENT AS WRITTEN

**F-1 — THE SPECIFIED FIELD NAME COLLIDES, AND IN THE WORST DIRECTION.** The assignment names the field
`pipeline_stage`. **`pipeline` IS ALREADY A LIVE FIELD ON THE PROJECT JSON AND MEANS SOMETHING ELSE
ENTIRELY** — measured over all 316 project JSONs: `bd-pipeline` (29), `inf-pipeline` (7), `NFRA` (6),
`portal` (4), `partners-api` (4), `mdpf` (4), null (86). It is the **DATA-PIPELINE DOMAIN** the project
belongs to. A reader meeting `pipeline` and `pipeline_stage` on one object will reasonably read the
second as *a stage of the first* — which is false in every instance. Two different "pipelines" (a data
domain, a process) sharing a name prefix on one object is a Rule-24(iii) intent-coherence failure **in
the field name itself**, before a single value is enumerated.
**RECOMMENDATION: `dep_stage`** (Directive Execution Pipeline), used throughout this record. CTO owns the
final name; it is flagged BEFORE the term propagates into the protocol doc and CVO's schemas, because a
name is cheapest to change while exactly one document uses it.

**F-2 — THE TERMINAL VALUE IS STRUCTURALLY UNREACHABLE ON DAY ONE.** `CLOSED` is defined by the ratified
law as *a zero-graduation round* — which requires CVO's surprise channel to EXIST in order to graduate
zero items from it. Until `org/ref/SURPRISE_CHANNEL_PROTOCOL.md` and `org/surprise_channel/` land, **no
project can legitimately reach `CLOSED` under this law.** Stated so nobody reads an absence of CLOSED
projects as a compliance failure, and so nobody back-fills the value to make the axis look inhabited.

## 1. THE AXIS

- **DECLARED LAYER (the CE denominator):** a project's **current position in the directive execution
  pipeline**. Nothing else.
- **GRAIN:** PROJECT-level, uniformly. The ratified law ALSO mandates **CELL-level status** inside a
  decomp — that is a *different grain on a different object* and MUST NOT be folded onto this axis
  (Rule 24(ii)). A project sits at one `dep_stage`; its decomp cells carry their own statuses.
- **INTENT:** position only. Explicitly NOT disposition, NOT condition, NOT narrative.

## 2. VALUES

| value | means | leaves when |
|---|---|---|
| `REGISTERED` | project registered; no purpose-level PRD yet | PRD authored |
| `PRD` | purpose-level PRD exists; no COO decomp yet | decomp authored |
| `DECOMP` | COO atom-decomp of operative surfaces exists, with its four-postulate record; no TOs cut | first TO cut from a decomp cell |
| `EXECUTING` | TOs cut from decomp cells; executing on a frozen spec | the round's TOs all reach terminal state |
| `ROUND_CLOSE` | round's TOs complete; CVO remediation handover in progress; next round's TOs not yet cut | next round's TOs cut (→ `EXECUTING`) or zero-graduation (→ `CLOSED`) |
| `CLOSED` | a round completed with ZERO graduations | terminal (see F-2) |

**Cycling is expected and legal:** `EXECUTING → ROUND_CLOSE → EXECUTING` repeats for vN rounds.
`dep_stage` records *where the project is now*, never how many rounds it has run.

## 3. THE FOUR POSTULATES

**(i) MECE.** *Mutually exclusive:* each value is a position between two named events; the leave-conditions
above are the boundaries, and no two can hold simultaneously. **ONE MEMBER WAS REJECTED DURING AUTHORING,
AND THE REJECTION IS THE POSTULATE DOING ITS WORK:** a `CHANNEL` / `CHANNEL_ROUND` value was drafted and
**cut, because the surprise channel is CONCURRENT WITH execution, not a position in it** — surprises
surface same-turn *during* `EXECUTING`. Placing a concurrent process on a sequential axis would have made
`EXECUTING` and `CHANNEL` simultaneously true and broken ME on day one. `ROUND_CLOSE` survives because it
is a genuine *position* (TOs done, next TOs not yet cut), not the channel itself.
*Collectively exhaustive over the declared layer:* every position a project can occupy between
registration and a zero-graduation round has a value. Terminal dispositions that are NOT pipeline
positions (superseded, abandoned) are delegated to `status` — see (iii).

**(ii) SAME GRAIN.** All six are project-level positions. No value is cell-level, artifact-level, or
TO-level. The cell-level status the ratified law mandates lives on the decomp, not here.

**(iii) INTENT COHERENCE — one axis, one intent, DELIMITED AGAINST THE THREE FIELDS ALREADY PRESENT.**
This was the highest-risk postulate, because the project JSON already carries overlapping-sounding fields:
- `status` (complete / superseded / active) = **DISPOSITION**. `dep_stage` is POSITION. A project may be
  `EXECUTING` with `status: active`, or carry a terminal `status` with `dep_stage` frozen where it stopped.
  Never encode disposition in `dep_stage`.
- `blocking` = **CONDITION**. A blocked project does not change stage; it stays where it is and carries a
  blocker. Never mint a `BLOCKED` stage — that is state-and-condition on one axis.
- `phase` / `current_phase` = **NARRATIVE**, and measured as such: free prose like
  `"CLOSED COMPLETE 2026-05-22 (3-step ..."` and `"Phase 1 PRD v0.1 CANONICAL ..."` — not a controlled
  vocabulary. `dep_stage` does not replace it and must not be derived from it. Where they later disagree,
  **`dep_stage` is authoritative for position and the prose is the human note**, or the two silently drift.

**(iv) STATE COHERENCE (stability frame).** Name the state axis: *is this value attainable with the
instruments that exist?* Five of six are attainable today. **`CLOSED` IS NOT** (F-2): it requires the
channel, which is CVO's unbuilt half. So the axis **fails (iv) on exactly one member, and that member is
named** — which is what the postulate asks for (*"if it blatantly fails on a key axis that is important to
know on what axis it fails"*). One remedy (CVO's protocol build) moves it, and nothing else on the axis
waits on that remedy. Re-test when the channel lands.

## 4. SCOPE — WHAT THIS DOES NOT AUTHORIZE

⛔ **NO RETROACTIVE MIGRATION.** The field is **OPTIONAL** and applies to **projects registered under the
ratified pipeline going forward**. Andrew's ratification states in-flight work (LD-0429 promote, ETFS,
MDPF_PROVENANCE T-B) **completes under current specs — no re-papering**. Stamping `dep_stage` onto the
316 existing project JSONs is a migration nobody authorized, and a back-filled value would be *a guess
about history wearing a controlled vocabulary's clothing*. A non-conforming project JSON is **not** a
defect and **not** a warrant to edit it.

## 5. OPEN — ROUTED, NOT DECIDED HERE

1. **Final field name** — `dep_stage` vs `pipeline_stage` (F-1). CTO's call; flagged before propagation.
2. **Who writes it** — stage transitions are acts by different seats (COO at `DECOMP`, workers at
   `EXECUTING`, CVO at `ROUND_CLOSE`). A field several lanes write needs its owned-paths answer; the
   project JSONs' existing lane governs unless CTO rules otherwise.
3. **Enforcement** — the choke-point principle puts one gate at TO issuance, and the detectable violation
   is *a TO cut against a project whose `dep_stage` is not `DECOMP`*. Routed to the 0.8.0 tooling lane per
   64959; until it lands, issuers check by hand with printed denominators.
