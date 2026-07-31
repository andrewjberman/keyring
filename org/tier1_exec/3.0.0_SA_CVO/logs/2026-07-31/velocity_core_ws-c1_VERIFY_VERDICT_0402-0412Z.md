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

## Blockers / Next

None at me. Increment 2 (item 10, >=1 consumer actually gated) is `~C`'s, gated by CTO~Z; my verify
follows the same sequence. V-1 awaiting CTO~Z's EOL call. Zero crons armed. Open call at Andrew on the
SYSPARITY cron conflict stands (see the 0248-0330Z log).
