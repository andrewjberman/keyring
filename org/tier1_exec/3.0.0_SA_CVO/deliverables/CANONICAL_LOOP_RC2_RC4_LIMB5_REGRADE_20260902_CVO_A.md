# Canonical loop RC2 / RC4 / step-6 limb-5 re-grade -- CVO~A

**Date:** 2026-09-02  
**Order:** CTO message 92686  
**Implementation pinned:** `689960ce164df69cdb60adc9bab633a2e5fd5c99`  
**Rail record pinned:** `4132a396a8449854255bd6f4f0ea334bb5b2f6bf`  
**Parent re-grade:** `CANONICAL_LOOP_RC1_RC3_REGRADE_20260902_CVO_A.md` @ `7f5bc19`  
**Verdict:** **RC2 GREEN; RC4 GREEN; step-6 limb 5 PARTIAL / RED; `PRD_HEADER.status` Rule-24 proposal NOT ADOPTED.** The overall canonical-loop and ETFS hold remains.

The implementation files were byte-identical between the pinned commit and the
live vintage exercised for this review; none carried a worktree divergence.

## RC2 -- GREEN

The watcher now captures `_index_now`'s status before CR stripping, treats an
empty successful response as failure, and returns before the index replacement
on every producer failure. The prior index therefore survives rather than being
overwritten with an empty result.

Independent execution of the real Bash integration path:

```text
bash org/surprise_channel/surprise-watch.sh 3.0.0_SA_CVO~A_RC2_REVIEW_92686 selftest
tool MISSING                         OK
tool exits 1                         OK
tool empty output                    OK
CRLF output, same rows               OK
stored index LF-clean                OK
same-count MUTATION                  OK
same-count DELETE+ADD                OK
selftest: 7/7 PASS, rc=0
```

The standing index independently emitted 192 `path<TAB>id<TAB>hash` tuples,
with zero CR-bearing lines. The inherited full row-gate harness also passed all
34 controls, including mutation, deletion, duplicate identity, HEAD read error,
raw JSON parsing, and the 192-row index. Markdown and raw JSON now share the
same document enumerator for both `sweep()` and `index()`.

Release condition 2 is satisfied.

## RC4 -- GREEN

The live standing pass reports:

```text
documents=19 rows=192 malformed_blocks=0 failures=4
baseline=4 known=4 new=0 resolved=0
```

Five isolated temporary-corpus controls passed:

1. a present empty baseline with a valid Markdown row passes;
2. a fenced scalar is counted malformed and refuses;
3. a non-object raw-JSON item is counted malformed and refuses;
4. a valid raw-JSON object contributes one swept row and one index tuple; and
5. an absent baseline refuses even when the corpus has zero failures.

Three independent integration controls exercised the row gate's standing limb:
a green corpus permits, a red corpus refuses, and a corpus module that cannot
load refuses. This confirms the pass is inside the existing row gate and is
fail-closed rather than merely printed.

Release condition 4 is satisfied.

## Step-6 limb 5 -- PARTIAL / RED

The useful core is real. The committed nine-case harness passes; the live
ETFS_GUARDRAIL PRD validates; header project/directive/fabric mismatches refuse;
schema-invalid `step=5` refuses; omitted/phantom endpoint definitions refuse;
and an independent correctly shaped TO path reaches the wrapper and reports one
graded staged PRD. The FWD definition regex independently discriminates a
line-start definition from prose and possessive mentions.

Two end-to-end seams remain.

### Falsifier A -- a heading is accepted as a manifest

`MANIFEST_HEADING_RE` searches the entire PRD and `_prd_conformance()` tests
only whether it matched. It does not establish a real, non-empty Markdown
section. Independent controls produced zero complaints for both:

```text
## SURFACE MANIFEST
<end of file>
```

and a PRD whose only matching heading was inside a code fence. Step 5 still has
no address rows in either case, yet the conformance limb passes. Parse an actual
top-level section outside fences and require non-empty manifest content. Do not
silently widen this repair into enforcement of the contract's full row schema;
that would be a separate refusal condition.

The committed possessive-mention control also no longer injects its advertised
specimen: it replaces the old backticked ENDPOINT heading after the PRD was
changed to the exact unbackticked heading. The core regex passed a separate
direct discrimination control, but the harness case must target the live text.

### Falsifier B -- register identity is read from the worktree

The wrapper reads PRD and header schema from the staged index, but opens
`org/projects/<project>.json` from the worktree. In an isolated Git repository:

```text
staged register directive = D9
worktree register directive = D8
PRD_HEADER.directive       = D8
violations                 = 0
```

The gate therefore passed a commit whose staged register and staged PRD header
disagreed. Load the register row from the staged index and fail closed on an
unreadable staged blob, exactly as this limb already does for the PRD and schema.

### Carrier gap -- not a new gate

COO message 92699 is confirmed: `docs/architecture/_PRD_TEMPLATE.md` has 140
lines and zero matches for `SURFACE MANIFEST`, `outcome_ref`, `depends_on`, or
`claim`. The adopted contract is instantiated in ETFS_GUARDRAIL but is not in
the authoring template. That does not excuse either falsifier and does not block
COO's active NFRA_CLDGRPH decomposition; it is a producer-carrier repair for the
CTO-owned template so future PRDs arrive conformant by construction.

## `PRD_HEADER.status` Rule-24 proposal -- NOT ADOPTED

The schema is valid Draft-07, but the proposed record does not close the four
postulates:

- **MECE fails.** A PRD withdrawn or rejected without a successor is real and
  cannot truthfully be `SUPERSEDED`. The proposal simultaneously says
  `SUPERSEDED` must follow a cited successor and maps no-successor withdrawal to
  `SUPERSEDED` with successor `none`.
- **Same grain passes.** Every value speaks about one PRD document/version.
- **Intent coherence is unresolved.** The declared intent is the binary question
  "may step 5 decompose now?", but `DRAFT` and `SUPERSEDED` are two different
  non-decomposable history states. Declare the axis as document lifecycle, or
  use a genuinely binary readiness field; do not claim both.
- **State coherence fails with the same uncovered state.** The legal transition
  account is coherent only when a successor exists. Withdrawal/rejection with
  no successor has no truthful terminal transition.

The broad token census does not cure the semantic hole. Its first two file
denominators are approximate (`145,0xx`), and token uses across deploy ledgers
and unrelated documents are not the population of `PRD_HEADER.status`. The
current live PRD-header population is one observed header, `RATIFIED`, so the
other lifecycle states remain unexercised at this grain.

Smallest correction: declare lifecycle as the axis and add a truthful terminal
state such as `WITHDRAWN`, with its no-successor meaning and legal transitions,
or replace `SUPERSEDED` with a broader terminal whose optional-successor
semantics are explicit. Re-run an exact census over parsed PRD_HEADER blocks.
Any semantic gate that refuses a TO based on `status` remains separately
unauthorized unless Andrew asks for that refusal.

## Release state

- RC1, RC2, RC3, RC4, and RC6: GREEN.
- RC5: PARTIAL / HOLD under the superseding record at `9d9035eeee`.
- RC7: open.
- Step-6 limb 5: PARTIAL / RED on the two falsifiers above.
- Codex rail: structural state (c), unchanged; no PreToolUse bridge exists in
  this runtime, so the Claude timeout repair does not reach it.

**Overall verdict: RED / HOLD.**

-- 3.0.0_SA_CVO~A
