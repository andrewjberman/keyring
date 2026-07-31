# 3.0.0_SA_CVO~Z -- WS-C1 VERIFY VERDICT (0402-0412Z)

**archetype:** VALIDATE

Addendum to `velocity_core_ws-c1_design_attack_and_fence_ruling_0248-0330Z.md`. Gate signal received
from `1.0.0_SA_CTO~Z` 040236Z; build-verify released.

---

## VERDICT: WS-C1 PASSES

**Subject:** rule bank v1.7 -> v1.8 `@880f527cc` (+234/-1); 06 recompiled `@e22f38c41` as_of 880f527cc.
Both pushed, repo 0/0. Verified against the **COMMIT**, not the disk (tree clean for the rule bank).

**Method: RE-DERIVED, not confirmed.** I did not read CTO~Z's stated 19/19 into my probes. Independent
comparator, controls first, comparison to their result only afterward. We agree.

## Item 13 -- ADDITIVITY, against oracle `8f8a63200`

Controls before the check, because a comparator that cannot fail is not a control:

| control | result |
|---|---|
| PC1 oracle identity | PASS -- md5 `37e16648dc965424b75c14677927a636` == pinned at 0255Z |
| PC2 extraction denominator | 19 top-level sections oracle / 19 landed (a number, not a boolean) |
| NC mutant test | PASS -- 1-byte flip inside `variance` -> DETECTED |

Result: **CHANGED = exactly `{dynamic_rails, meta}` · ADDED 0 · REMOVED 0.**
**12 of 12 present ratified sections BYTE-IDENTICAL** (variance, completeness, type_tuple, roles,
relations, role_priority, relation_composites, non_relation_edges, lineage, scope_outs, node_bindings,
contextual_types). `type_tuple` UNAMENDED. 48217B/425L -> 85160B/658L.

## Content -- 15/15, after correcting TWO FALSE FAILS IN MY OWN PROBE

Both were my instrument, not the build. Recorded because four seats shipped a lying instrument tonight
and the pattern is the finding, not the instances.

1. **F-1 token check -- FALSE FAIL.** I tested "SUPERSEDED/ORPHAN absent as a STRING anywhere in the
   lifecycle+typed_violations subtree." The requirement is absent **AS TOKENS**. Every hit was prose
   *stating the prohibition* (`lifecycle.token_hygiene`, `SILENT_RESIDENT`'s "never ZOMBIE/ORPHAN",
   and `typed_violations.gate.two_variance_orphan` -- the gate I asked for). **My check would have
   forbidden the rule bank from documenting its own rule.** Corrected to enum members + violation keys,
   with live-search controls (LEGACY + SILENT_RESIDENT present; Superseded/Orphan still found in
   `variance.labels`, proving the search was not dead). **F-1 SATISFIED.**
2. **UNDECLARED -- FALSE FAIL.** I asserted every enum value must carry `requires`. UNDECLARED carries
   `requires: []` plus `falsifiable_by: "n/a -- UNDECLARED is the honest absence of a claim, never a
   claim itself."` **Correct, and my check was incoherent** -- S.3 binds values that FLIP a detector's
   polarity; demanding a falsifier for a non-assertion is demanding evidence for the absence of a claim.

## My findings verified IN THE ARTIFACT (not merely in the spec)

`lifecycle.token_hygiene` (F-1) · `typed_violations.gate.two_variance_orphan` (F-2, variance.Orphan
NAMED as a gated consumer) · `lifecycle.max_dwell_binding` (F-3) · `lifecycle.exercised_not_resolved`
(F-4) · `scope` in `contract_record.required` (F-6) · `lifecycle.decay.stale_semantics` (R-1) ·
`lifecycle.decay.revalidation_predicate` (R-2) · `rolling_is_a_derivation` (F-8, citing the PRD's own
derivation law).

PRD WS-C1 tuple satisfied **including optionality**: required = [intent_source, obligation,
lifecycle_class, revalidate_by, scope]; optional = [successor, expiry_condition, cadence,
vintage_probe] -- the PRD's `successor?` / `expiry_condition?` honoured as literal optionality, with
`debt` consuming expiry_condition as a derivation. 6 derivations, none a primitive. TRANSIENT and
DORMANT explicit. YAML parses; non-ASCII 0 of 658 lines.

## V-1 -- NEW FINDING (my surface, routed to CTO~Z, NOT a rev-4 reopen)

**The committed parity artifacts are STALE while the disk is CORRECT, and `comp-system --check` reads
the disk -- so it reports SYSTEM CURRENT over a repo that still carries the drift.**

| file | COMMITTED | DISK |
|---|---|---|
| `infra/system/00_synthesis.md` | ledger_union 91 | 90 |
| `infra/system/03_comp_tools.md` | 91 / tools_index 70 | 90 / 69 |
| `infra/system/README.md` | 91 / 70 | 90 / 69 |

**A device pulling CLOUD right now gets 91/70.** This is the DESIRED-vs-APPLIED inversion pointed at
the parity surface itself, and it is the LD-0319 responsibility.

**Not committed, deliberately, with the measurement rather than a hedge:** substantive delta is
**10 lines** (all `cs:` spans), but `git diff --stat` shows **160/160** because `core.autocrlf=false`
+ **`core.eol=lf`** + CRLF-stored blobs + no `.gitattributes` -> *"CRLF will be replaced by LF the next
time Git touches it."* **12 tracked files are in that state and 11 of them are the news_scanner files
sitting in `stash@{0}`.** Flipping stored line endings on shared tracked files mid-incident, burying a
10-line correctness fix in ~160 lines of churn, is not a call I take on my own authority. Proposed:
land the 10 lines with EOL preserved and verified byte-wise, and route the 12-file EOL condition
separately. Nothing downstream consumes a wrong number today -- the disk is correct.

## Verifier ruling -- item 17

**Measured before the SILENT-RESIDENT gate is WRITTEN; not before this vocabulary lands.** Holding a
verified, additive artifact for a number that constrains a *different* artifact would be the wrong
trade. But the gate is the thing that can propose deleting live infrastructure, and authoring it
against an assumed 7 is precisely the defect item 17 exists for. `~C` takes it as a budgeted task.

## Protocol 1

LANDED + CTO~Z-GATED + CVO~Z-VERIFIED -- all three satisfied. **ESTATE WS-E1 edge 2 CLEARS**; relayed
to `0.0.0_AB_MSTR~Z` at 041117Z for carriage to base MSTR.

**HELD-OUT FENCE: HOLDS.** The landed artifact contains no ADVI_PERFORMANCE or MDPF_GLOBAL surface and
nothing in it was authored to make a rail look expressive.

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-system --check` | SYSTEM CURRENT (26 regions, 0 drifted) | reads the DISK -- see V-1; the CURRENT verdict is true of the tree and false of the commit |
| `comp-surface-check` / `comp-pulse diff` | clean, denominator printed | via safe-commit on both commits |

Bespoke verify probes (`verify_additivity.py`, `verify_content.py`) were written for this pass rather
than routed to a comp-tool: no comp-tool answers "is section X byte-identical between two refs", and
the whole point of item 13 was byte-identity at a pinned vintage. Both probes were control-tested
before their verdicts were read.

---

# INCREMENT 2 VERIFY (item 10) -- PASS. WS-C1 CLOSED, BOTH INCREMENTS.

**Subject:** `comp_legacywriter.py` @`b5854411b` -- the D3 lifecycle gate on the kill-list path.
CTO~Z gated 17/17 (with their own mutant on C9b). **Verified by EXERCISE, not config read** (Rule 22a:
a behaviour claim needs the test that fails if the claim is false).

Temp contract registry built; `resolve_lifecycle` RUN on every branch. Denominator: 6 declarations
loaded, **7 cases exercised, 7 PASS**.

| case | gated | kill_eligible | verdict |
|---|---|---|---|
| TRANSIENT fully declared | True | False | NOT-ASSERTED (declared healthy state) |
| DORMANT fully declared | True | False | NOT-ASSERTED -- *the 7 belts rev-1 would have deleted* |
| EVENT_CREATED fully declared | True | False | NOT-ASSERTED |
| **PERMANENT (NEG CONTROL)** | **False** | **True** | eligible -- correctly NOT protected |
| **LEGACY (NEG CONTROL)** | **False** | **True** | eligible -- debt, not a protected class |
| TRANSIENT HALF-DECLARED | False | False | UNKNOWN, LOUD (missing revalidate_by, scope) |
| UNDECLARED (no record) | False | False | OBSERVED (lifecycle UNDECLARED) -- never DEAD |

**The negative controls are the load-bearing rows: a gate that protects everything is not a gate.**
PERMANENT and LEGACY come back kill-ELIGIBLE, so it discriminates. The half-declared row is F-3/S.3
working as specified -- no fallback to the declared value, no fallback to PERMANENT.

**MUTANT ON MY OWN SUITE:** forced `GATED_CLASSES` to the full enum so PERMANENT became wrongly gated
-- **my suite CAUGHT it.** The control can fail, so its pass is evidence.

**CTO~Z's "inert" claim independently CONFIRMED:** live registry ABSENT, **0 declarations, gating path
fires on 0 real resources today.** Present effect is entirely CLAIM-SUPPRESSION (the S.4 bound in code
rather than prose), which is real; the *gating* direction is unexercised in production by construction.
The code is honest about it -- an absent registry returns *"0 declarations, every resource UNDECLARED"*
rather than an empty success, which is the difference between zero coverage and no problem.

## V-2 -- observation on the gate's OUTPUT SHAPE (not a blocker)

`kill_list_eligible=False` is reached by **three structurally different routes**: (1) GATED -- a
POSITIVE CLAIM OF HEALTH; (2) HALF-DECLARED -- a declaration we cannot trust; (3) UNDECLARED -- no
claim at all. A consumer branching on the **boolean alone** collapses all three.

The information IS present (`declared`, `lifecycle_class`, `verdict` separate them cleanly), so this is
not an implementation defect. The hazard is that `kill_list_eligible` is the field a downstream
consumer reaches for, and it is a 3-to-1 collapse of **exactly the distinction the axis exists to
preserve** -- *absence is a SET of states and an existence check cannot partition it*, S.1's own law
reappearing one layer up, in the gate's own return shape. Recommended: the consumer contract states
that `kill_list_eligible` must not be branched on alone.

## Still open after WS-C1 closes

`variance.Orphan` ungated (CTO~Z holding the gate's authoring on ~C's population measurement --
endorsed) · item 17 population UNKNOWN, bounded above by 7 · **the first REAL declaration is worth an
end-to-end verify** -- it will be the first execution of the gating path on a live resource, and my
exercise used a synthetic registry.

## Blockers / Next

None at me. **WS-C1 CLOSED, both increments, verified.** V-1 closed @41256c702. Fence Amendment 1
landed @4b94ad6f3 (M9 capture unblocked; Control 2 declared to `0.7.0_AE_CloudOps~Z` by CTO~Z).
SDK v1.2 hardcode disposed as MINE, queued, DERIVE-NOT-BUMP affirmed with a corrected denominator
(8 occurrences / 7 files -- base CTO's list missed `tenants/demo/company.yaml`) plus a second
defect (marker ABSENCE in the four required files) attached. Zero crons armed. Open call at Andrew on
the SYSPARITY cron conflict stands (see the 0248-0330Z log). WS-C2 next.

---

# CORRECTION 1 -- F-2's LIVENESS PREMISE WAS FALSE (2026-07-31 ~0440Z)

**Correcting BOTH this record and `..._design_attack_and_fence_ruling_0248-0330Z.md`, which describe
`variance.Orphan` as "a SEPARATE, already-LIVE detector."** That is FALSE. Raised by
`0.8.0_AE_CloudComp~C` (who halted rather than gate absent code), landed by CTO~Z @`17b24fad2`,
**independently re-derived by me before acceptance** -- a refutation taken on trust is the same error
as a claim taken on trust.

```
summary_corpus.py::_variance_verdict :581-582
    if len(present) < 2:
        return None   # singleton -> no firm-sibling; Orphan/Superseded deferred v1
emission sites -> kind = Fork-Shadow x2 / Canonical / Twin.   NO Orphan.
'Orphan' as a quoted VALUE in repo python: 0
MY POSITIVE CONTROL: Fork-Shadow 9, Canonical 9, Twin 7  -> the search is alive
```

**`variance.Orphan` is DECLARED at four layers and IMPLEMENTED at none.**

## What survives / what falls

- **SURVIVES:** F-2's structural insight -- a token occupied on a ratified axis makes a reader believe
  both are gated when only one is. True whether or not the colliding detector is built. The
  `LEGACY` / `SILENT-RESIDENT` renames stand on their own merits. **F-1 is untouched** -- it was always
  a declaration-level fact about `variance.labels`, not a liveness claim.
- **FALLS:** the liveness limb, and with it F-2's **BLOCKING severity**. I wrote that the kill-list
  danger "remains reachable through a path your gate does not name." **There was no path.** A blocking
  finding on an unreachable bypass spends a gate's credibility on nothing -- the false-alarm face of
  the same coin as a missed finding, and severity is not a rounding error.

## The error, named precisely

**The falsifying evidence was a CODE COMMENT on the returning line of the emitter.** I never opened
`_variance_verdict`. I reasoned from `variance.polarity` and from the rule bank's own `# WIRED+LANDED`
header carrying contract and wire commit hashes -- **treating a header comment asserting wiredness as
evidence of wiredness.** Two named failures at once, both of which I invoked at other seats this same
session:

1. **DESIRED-read-as-APPLIED** -- my own F-7 charge against CTO~Z's S.4, filed and then committed by
   me, in a finding I escalated to BLOCKING.
2. **CHECK THE MARKER, NOT THE COMMENT** -- CLAUDE.md Rule 21 carries that scar with base-CVO's name
   on it. **This seat is the one that rule was written about, and it repeated the class.**

*Knowing a failure mode by name does not immunise you against writing it.* Third time tonight that
sentence has been the finding, and this instance is mine.

## Consequence I unmade

I ruled item 17 *"measured before the gate is WRITTEN"* and CTO~Z made it a hard prerequisite on my
disposition. **That prerequisite rested entirely on the false premise, so I WITHDREW it** -- holding
`~C` to a budgeted `position_key` derivation would have spent real work sizing a guard for a detector
that does not exist, on my error. CTO~Z's reclassification is adopted and is better than what I asked
for: **the exclusion becomes a PRECONDITION on implementation** -- `Orphan` may not be implemented
without the lifecycle exclusion landing in the same change. Gating a non-existent emitter yields a
control that can never fire and can never be shown to fire: unfalsifiable, unmutatable, **not a
control** -- my own standard, correctly turned on my own finding by the build lane.

**Increment-2 verify UNAFFECTED:** `SILENT-RESIDENT` gates a real emitter, exercised 7/7 with negative
controls and a mutant. That PASS rests on its own evidence.

## The law this earns (routing to MSTR~Z with CTO~Z co-signing, as ONE proposal)

> **A CHECK THAT CANNOT DISTINGUISH A THING FROM A STATEMENT ABOUT THE THING WILL FORBID THE RECORD
> FROM DOCUMENTING ITSELF** -- and its sibling, **`git show` renders (smudge filter applied),
> `git cat-file` reports (raw bytes).** One confuses a mention with the fact; the other confuses a
> rendering with the bytes. Same law at two altitudes; splitting them loses the generality.

*(Note for any re-verify: the false sentence is preserved as quoted provenance in
`two_variance_orphan_correction`. Check it FIELD-BY-FIELD, never on the blob -- a blob search flags
the correction itself. That is the token-USED vs token-NAMED trap for the third time tonight.)*
