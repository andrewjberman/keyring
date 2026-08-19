# DESIGN NOTE -- s3(c) `check_system_definitions` + T12 `comp-adversary`: the arch frame
**1.0.0_SA_CTO, 2026-08-19 ~20:5xZ. Pulled forward from the post-flip window on Andrew's pick
("love option 1, start there and then proceed through the rest").**

**Authority chain:** s3(c) = Andrew's never-again ask (@df64992815 tranche routing: *"so that we
never have this drift class issue again"* -- the OS move: a registry `resolves_via` field per
coverage-universe term + a run-mode that EXECUTES the rules and compares derived-vs-declared).
T12 = the comp-adversary composer, name RATIFIED by Andrew @7241d0dfd7. Bilateral pins (CTO x CRO,
declared both directions): THIS NOTE is the arch frame; CRO's prototype spec @5ecb069af3 + design
@50ea774684 are worked seeds UNDER it, migrating at no compatibility cost (annex fields are
additive, no consumer contract yet -- CRO's own seam protection, 203815Z). Governing law: v3.3/v3.4
ontology-as-RUNTIME (derivable values compile-or-cite, never hand-copy; drift gates non-monotone;
documents are recompilable views). Placement: LOCAL as a class per Andrew's standing criterion (b).

---

## 1. THE ONE SHARED-SHAPE DECISION (ruled here, once, before either builds)

**Both outputs ARE siblings of the L0a `boundary_report` -- one declaration-type family.**

| Artifact | Family member name | What it declares | Conformance verdict over |
|---|---|---|---|
| L0a boundary_report (exists) | the PARENT shape | a boundary claim | declared-vs-observed boundary |
| s3(c) checker output | `definitions_conformance_report` | per-term derived value | derived-vs-DECLARED definition |
| T12 delta-declaration | `validation_context_declaration` | what the validator was and was not shown | packet-vs-author-context complement |

**The family contract (what "sibling" means, exactly):** each is (i) a DECLARATION (typed claims,
one grain per artifact), (ii) a CONFORMANCE VERDICT per claim from a closed enum, (iii) EVIDENCE
PINS per claim (source pointer + vintage), (iv) DENOMINATORS in the artifact itself (the
three-number frame: attempted / writable-or-applicable / comparable -- adopted from CRO's
pre-registration, generalized). **Why one family:** the lock-down's exit bar, future gates, and
any downstream consumer then parse ONE grammar; a second declaration grammar would be the
two-vocabularies defect at the meta layer. (CRO named this as the decide-once question; L0a is
the natural parent because it already carries declaration+conformance+pins and survived its own
conformance suite.)

## 2. s3(c) -- `check_system_definitions` (the instrument that DEFINES "locked down")

### 2.1 The `resolves_via` field (registry annex, evidence layer)
One field per coverage-universe term on its REGISTRY row. Additive annex; SERVE-BY-DEFAULT (the
@7241d0dfd7 engine fix already serves annex fields -- endorsed, no flag). Carries:
- `rule`: the EXECUTABLE derivation -- what to read and how to reduce it to the term's value
  (count / enum-set / name-list / presence). Deterministic; no model call.
- `source`: **BLOCK-ADDRESSED, never file-grain** -- `path#block-anchor`. THIS IS LOAD-BEARING,
  from CRO's measured fact (a): the canonical yaml carries the segment roster in TWO BLOCKS THAT
  DISAGREE on a member name (c4_segments: `estate-infrastructure` vs segment_definitions:
  `andrew-infrastructure`) -- an intra-file two-homes at BLOCK grain, so a file-grain pointer is
  UNDERSPECIFIED BY CONSTRUCTION. Every resolves_via names its block; a term whose truth spans
  blocks names each with its role.
- `vintage`: the commit-ish the rule was last verified against.
- `last_result`: pointer to the results row of the last checker run (CRO's prototype JSONL is
  this layer's seed; migrates to the run-mode's own results home).

### 2.2 The run-mode
`check_system_definitions` (homed with the ontology tooling; comp-lane registered): for every
term carrying `resolves_via`, EXECUTE the rule at HEAD, compare derived vs declared, emit ONE
`definitions_conformance_report` (family shape, sec 1). Per-term verdict enum, closed:
- `AGREE` -- derived == declared.
- `DISAGREE` -- differs; carries both values + the block pins. **Non-monotone per v3.3: a NEW
  DISAGREE blocks the edit; a KNOWN one carries its ruling pointer and does not re-block.**
- `UNRESOLVABLE` -- the rule failed to execute (source moved, block anchor gone). LOUD -- an
  unresolvable rule is itself drift (the T13 class: a definition anchored to something gone).
- `NO-RULE` -- term has no resolves_via yet. Printed in the denominator, never silently skipped
  (coverage is a number in the report, not an assumption).
Report denominators: `attempted / writable / comparable / agreeing` (CRO's three-number frame
plus the verdict split). **"LOCKED DOWN," measurably: every coverage-universe term is AGREE or
carries a DECLARED exception with its ruling pointer -- that line in the report is what the
tranche exit and Andrew's estate-backlog release READ.**

### 2.3 Reader + moment (the convention applied to itself)
Two moments, both already existing: **(i) the ontology commit-gate moment** -- scoped to
`infra/system/ontology/**` + the registry homes; Andrew-asked (the never-again set is his
explicit ask, so this gate is legal), non-monotone as above; **(ii) on-demand** -- the tranche
exit bar, and any seat verifying a definitions claim. The report is a per-run artifact; its
summary line (counts) prints in the gate's output, so the recurring reader is the committing
agent at the existing moment. No cron, no monitor, no alarm.

### 2.4 First fixtures (real, already measured -- the mutant set starts true)
1. The block-grain two-homes (fact (a) above) -- the checker's first DISAGREE must be THIS live
   instance, not a planted one.
2. The `describes` optional-list delta (fact (b): bank's contract_record carries it, registry's
   declared list omits it) -- member-grain fixture.
3. One PLANTED drift (edit a declared count) -- the cannot-fail control: the checker must fire
   on it, and the acceptance records the firing.

## 3. T12 -- `comp-adversary` (the validator-context composer)

### 3.1 The frame (thin composer; stages fixed, internals CRO-seeded)
`profile -> neighborhood -> complement -> packet -> declaration`:
1. **PROFILE**: parse the author's evidence context from rectangle citations (what the author
   read/measured).
2. **NEIGHBORHOOD**: expand via existing tools only -- comp-blast / comp-trace / comp-similar /
   comp-estate / depth. No new traversal engine (build ladder rung 2).
3. **COMPLEMENT**: what the author did NOT examine -- toolgraph SHARES_SUBSTRATE independence
   (the independence oracle), comp-axes unexamined-axes (**consumed via SNAPSHOT ROWS, never
   live-render -- the measured 71.5s freshness leg**), comp-pulse warnings, comp-state drift,
   git/ice-drill vintages, comp-cochange FILE-MODE as the history-diversity check.
4. **PACKET**: comp-read digests of the complement set, sized for a validator context.
5. **DECLARATION**: the `validation_context_declaration` (family shape, sec 1) -- what was
   included, what was deliberately excluded and why, with pins. **The declaration is the
   product**: a validator who knows what they were not shown can refuse to conclude.
`--open` mode is FIRST-CLASS (Andrew's own instinct): a model-prior validator packet with NO
estate context -- the declaration then states that emptiness explicitly.

### 3.2 Interfaces (named, not blocked)
- **T11 admissibility method** (CRO steward, drafting off the live CRO x CVO exchange): plugs
  into stage 3/5 as the contested-cell input contract WHEN ratified -- a named slot; T12 v1
  ships without it.
- The `definitions_conformance_report` (sec 2) joins the complement sources the day it exists --
  loose coupling; neither build waits on the other's runtime.

## 4. BUILD ROUTING + ACCEPTANCE (COO cuts post-flip; 0.8.0-class; LOCAL per criterion (b))

| Build | Order | Acceptance that can fail |
|---|---|---|
| check_system_definitions v1 | FIRST (it defines the tranche exit) | fixtures 1+2 fire as DISAGREE with block pins; the planted mutant fires; a clean run prints the four-number frame; the gate blocks a NEW DISAGREE and passes a KNOWN one |
| comp-adversary v1 | SECOND | a packet built for one REAL validator run (a CVO-class review), its declaration conformance-checked against the family shape; --open mode produces the empty-context declaration; comp-axes consumed from snapshot rows (verified no live render in the run) |

**Closure discipline:** CLAIM-SETS not file-sets (the census F1 rule) -- each tranche row closes
per-claim; the prototype's annex fields migrate to sec-2.1's shape by field-rename only (CRO's
no-obligation guarantee). CRO validates the frame's landing per the pin; CVO's L0a ownership is
notified for the family-parent claim (sec 1) -- if L0a's shape cannot parent these two members,
that objection reshapes sec 1, not the builds.
