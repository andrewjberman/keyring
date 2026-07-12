# The Front-Pass Rule Set -- Canonical Numbering (FP-R0 .. FP-R4)

**Owner:** 3.0.0_SA_CVO (verification artifact; the rail set the front pass grades against -- NFRA_TOOLPASS sec.5a
gives it to CVO). **Ratified against the committed repo, not messages.** Vintage: 2026-07-12.
**Cite as `FP-R{n}@FRONTPASS_RULES_canonical_20260712`.** A rule asserted only in a message or session log is NOT
ratified.

> **STATUS: this is the CVO-owned canonical FRONT-PASS rule set** -- the version-pinned home of NFRA_TOOLPASS sec.1
> "THE FOUR RULES", now FIVE with **FP-R0** minted upstream (CTO arch-gate-ratified 20260712T134429Z; routing
> corrected 20260712T135144Z). NFRA_TOOLPASS sec.1 amends to cite THIS set (the CVO-publishes-canonical /
> doc-amends-to-match pattern, same as RAIL_SET_canonical is the AC-0 of NFRA_COMPASSURANCE). New front-pass rules
> are minted HERE first, with an exercised incident, then flow into NFRA_TOOLPASS -- never authored in a message and
> back-filled.

## The two rail-sets are DISTINCT -- disclosed to kill the two-names-per-number hazard (the collision CVO~A caught in the R0 routing, CTO 135144Z)

There are TWO CVO-owned, separately-versioned R-numbered rail sets. A bare `R{n}` is AMBIGUOUS across them; every
citation MUST carry its set's `@`-vintage:

| Set | Purpose | Rules | Cite |
|---|---|---|---|
| **FRONT-PASS rules (THIS set)** | bind the front pass -- how to make a SOUND finding | FP-R0 QUESTION-CLASS / FP-R1 CLASS / FP-R2 FALSIFIER / FP-R3 BRANCH-FROM-TARGET / FP-R4 CONSUMER-CENSUS | `FP-R{n}@FRONTPASS_RULES_canonical_20260712` |
| **Verification negative-controls** | "how could this instrument read GREEN while wrong?" | R1 NEGATIVE / R2 VARIANCE / R3 NULL / R4 INVOCATION / R5 DISCLOSURE / R6 IDENTIFIABILITY / R7 DISC-OF-OBSERVATION (+ R2-per-limb) | `R{n}@RAIL_SET_canonical_20260710` |

They serve different instruments and MUST NOT be conflated. CTO's own R0 ruling initially conflated them (authorized
minting into RAIL_SET_canonical while the reasoning cited the front-pass R1-CLASS/R3-BRANCH); corrected here. The
`FP-` prefix is the durable fix so no future citation reads a front-pass rule against a negative-control number.

## The rules

| # | Name | The rule it binds | Committed definition | Discovered by (incident) |
|---|---|---|---|---|
| **FP-R0** | **QUESTION-CLASS** (the class ceiling) | Classify the QUESTION before the CLAIM. A DYNAMIC question answered from SOURCE is auto-`INFERRED`, regardless of reading-confidence. FP-R0 sets the class CEILING (dynamic-from-source can NEVER be `OBSERVED`); FP-R1 applies WITHIN it. | NFRA_PASSCRAFT_PRD sec.3c @362272cce + this ruling (NFRA_PASSCRAFT.TO-R0) | CTO founding pass on comp-adapter-audit (tool-1, 4/10 wrong, all this class); CVO~A all-63 sweep; CTO's own comp-transform false-UNUSED fix -- THREE design-independent corroborations |
| **FP-R1** | **CLASS EVERY CLAIM** | Every line carries exactly one of `OBSERVED`/`INFERRED`/`NOT-CHECKED`. Only `OBSERVED` may be reported as a DEFECT; `INFERRED`/`NOT-CHECKED` travel as LEADS. An `OBSERVED` claim cites the exact command + the exact output line. | NFRA_TOOLPASS sec.1:45-47 @11af75d95 | CTO founding front pass |
| **FP-R2** | **FALSIFIER-RUN** | Every finding carries its falsifier ("this is false if X"), and the falsifier is RUN. A falsifier you cannot afford to run is a finding you cannot afford to make. | NFRA_TOOLPASS sec.1:49-51 @11af75d95 | CTO founding front pass |
| **FP-R3** | **BRANCH-FROM-TARGET** | Branch membership comes from the TARGET, never from the tool's report about the target (the tool is the defendant). Establish which branch a target enters by inspecting the target / an observation the tool does not produce. | NFRA_TOOLPASS sec.1:53-55 @11af75d95 | CTO founding front pass (the by-name branch-coverage targets) |
| **FP-R4** | **CONSUMER-CENSUS** | A removal/gate/make-optional requires a consumer census with the DENOMINATOR printed ("0 consumers found by <predicate>", never "no consumers"); an addition requires a control. | NFRA_TOOLPASS sec.1:57-59 @11af75d95 | CTO founding front pass (the D9 gate-disabling opt-in write) |

## FP-R0 -- the full specification (the new rule; FP-R1..R4 are carried verbatim from NFRA_TOOLPASS sec.1)

**THE MECHANICAL TEST -- the 5 DYNAMIC-question types** (each answerable ONLY by EXECUTION / STATE / ESTATE
observation, never by reading the code that could produce it -- NFRA_TOOLPASS:86-87 @11af75d95):
1. **which-branch-ran** (control flow) -- reading `if C: A else: B` does not establish which ran.
2. **what-value-flowed** (data) -- reading the assignment does not establish the runtime value.
3. **did-a-side-effect-happen** (mutation / write) -- reading the write does not establish it fired.
4. **who-reads-X-at-runtime** (estate / access) -- reading the code does not establish who called it.
5. **what-the-served-artifact-contains** (served state) -- reading the producer does not establish the served bytes.

A claim answering any of these FROM SOURCE is `INFERRED` (a lead), never `OBSERVED` (a defect), however confident the
reading felt. FP-R0 removes reading-confidence from the classification -- the exact vector that failed on tool-1.

**WHY FP-R0 IS A RULE, not a re-label of FP-R1:** FP-R1 ("class every claim") leaves the OBSERVED/INFERRED boundary
to author judgment -- and a SOURCE read IS "a command (`cat`) + an output line", so a dynamic-question-from-source
passes FP-R1's LETTER while being INFERRED in truth. FP-R0 classifies the QUESTION's dynamism FIRST and caps the
class mechanically. It GENERALIZES FP-R3 (which covers only which-branch, and only from the tool's own report) to
all 5 dynamic types from ANY source. Composes with both; duplicates neither.

**EXERCISED (the minting bar -- a new rule is minted with an exercised incident):**
- **Founding-4 (CTO, comp-adapter-audit / tool-1):** 4 of 10 findings wrong, ALL this class -- D9 (did-a-side-effect:
  the manifest write's load-bearing consumers), the by-name branch-coverage targets (which-branch), D7
  (what-value-flowed: `return stub` vs the served `split:true`), D3. (NFRA_TOOLPASS:94-99 @11af75d95.)
- **All-63 (CVO~A):** comp-transform "is `views` rendered?" (what-value-flowed) read "unused" from source; EXERCISE
  (running chains/schema-check) proved it rendered -> OBSERVED required execution. comp-whoread "who DID read the
  bucket?" (who-reads-at-runtime) proven by bounded Athena EXERCISE, never a config read.
- **CTO's own comp-transform false-UNUSED fix (this session, design-independent):** a "is views rendered?"
  value-flow caught ONLY by exercise.

**TIE TO CLAUDE.md Rule 22 (cited so they never drift):** FP-R0 is the FRONT-PASS RULE-FORM of Rule 22's state-side
principle -- "Ground against served, NEVER source" for STATE claims. FP-R0 does NOT contradict Rule 22; it makes
Rule-22's state-side MECHANICAL for the front pass. The founding authors violated the principle DESPITE Rule 22
existing precisely because it was doctrine, not a mechanical rule -- FP-R0 lands it as the rule (NFRA_TOOLPASS:84,
89-90 @11af75d95: "the mirror Rule-22 never wrote down"; the candidate amendment "routed to CVO, NOT self-landed" --
FP-R0 IS that landing).

## Downstream

- **NFRA_PASSCRAFT.TO-R0 ruling = R0 IN, recorded here** (this artifact IS the TO-R0 deliverable + the RAIL_SET
  reference the front pass grades against). Hands to PASSCRAFT.TO-2's emitter fold: the emit checklist classifies
  question-type; a dynamic-from-source verdict emits `INFERRED`, never `OBSERVED`.
- **The exercised-reach corollary (shared with CVO base's effective-axis, 135301Z):** any `effective=yes` /
  reach-claim must cite an EXERCISED oracle_run, never a bare source `file:line` -- FP-R0 at the reach layer. It
  binds both the CVO~B exercised probe and any hand-authored ToolAudit `effective` (the latter is INFERRED and
  therefore an assurance-plane annotation, never the wire's effective source -- FP-R0 is exactly why CTO decoupled
  them, 134939Z).
- **Governance:** the two-set `FP-` prefix distinction above is the durable fix for the cross-set R-number
  collision. If a deeper formalization is wanted (renaming the negative-control set's citations too), that is a
  separate governance proposal.
