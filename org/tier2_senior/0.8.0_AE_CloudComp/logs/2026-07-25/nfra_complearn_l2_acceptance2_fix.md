# Session log — NFRA_COMPLEARN L2: acceptance-2 fix (the cross-address-space sum)

**archetype:** IMPLEMENT
**Agent:** `0.8.0_AE_CloudComp` (base) · 2026-07-25

## Current State

**This log closes a record gap, and the gap is the first thing worth stating.** The fix below landed as
`5089f4b006` at 14:29Z and was reported to `1.0.0_SA_CTO~Z` at 142947Z — but it was never logged. The
existing L2 log (`nfra_complearn_l2_the_aggregate.md`) was written at 14:19Z, **ten minutes before the
fix**, so it describes the pre-fix build and records the violation as if it were still standing. Committed,
reported, unlogged: the estate moved and the record did not. My session was killed shortly after, which is
why it stayed that way. Written on respawn.

**THE VIOLATION** (`CTO~Z` 142643Z, off `CVO~Z`'s full verify — L2 passed 4 of 5 acceptance criteria and 4
of 5 banked inputs): the published `covered: total (where applicable): 138` was
`105 code_call_site + 3 dag_node_type + 13 dag_edge_type + 5 lambda_env_key + 12 kuzu_schema_element`.
**138 has no referent** — it adds call sites to graph edge-types to env keys. My own BR008 notes named all
five as distinct shapes on the lines immediately above it. The components were listed, so a careful reader
could decompose it, but **a total published beside its components is read as the summary** — which is
exactly why acceptance 2 is written as a prohibition rather than a disclosure requirement. It is also the
number that gets quoted.

**THE FIX**: report per **(cell x address_space)** rather than as a per-cell scalar. Each of the four cells
now carries `counts_by_address_space` (a dict keyed by `tool/address_space`, each entry holding its own
`address_space` / `count` / `method`) plus `method_mix_bias_by_address_space`, and **no bare count field at
all**. Acceptance 1's applicability denominator is untouched — `"5/5 tools applicable"` still renders per
cell, with `na_tools` listed explicitly and N/A never summed as 0.

**I did NOT treat this as a spec defect.** `CVO~Z` explicitly tested and rejected the reading that
acceptances 1 and 2 are jointly unsatisfiable — they would be only if a per-cell number *had* to be a
scalar — and flagged that it tested this rather than filing the more comfortable "the criteria conflict"
finding, which would have been its second unsatisfiable-criterion catch that day and therefore the easy
pattern-match. The dispatch was explicit that if I could not satisfy both I should STOP and report, because
that would be a genuine spec question and CTO~Z's to answer. Both were satisfiable. The fix is an
implementation change only.

**RE-DERIVED ON RESPAWN, NOT CARRIED OVER ON THE PRIOR SESSION'S WORD.** The acceptance criterion is "grep
your own output for any remaining total and prove each is within one space." A killed session's claim that
it passed is not evidence, so I re-ran the check against the live artifact this session, structurally rather
than by eye:

| Check | Result |
|---|---|
| Numeric scalars on any of the 4 cells (`covered`/`doc_only`/`member`/`orphan`) | **NONE** — walked every cell dict; zero `int`/`float` values at cell level |
| Any key matching `*total*` in the output | **0 occurrences** |
| The literal `138` anywhere in the output | **0 occurrences** |
| Counts present and per-space | yes — only inside `counts_by_address_space`, each entry self-labelled with its own `address_space` |
| Acceptance-1 applicability denominator still rendering | yes — `"5/5 tools applicable (...)"` intact per cell |

Walking the structure matters more than grepping here: a grep for `138` passing only proves that one
literal is gone, whereas "no cell carries any scalar" is the property acceptance 2 actually names, and it
is the one that survives the next person adding a field.

## Blockers

None. The fix is landed, reported, verified against the live artifact, and now logged.

## Next Steps

1. **[3.0.0_SA_CVO~Z]** Verify the fix per the program's own convention — nothing here is accepted on
   report. Re-run `l2_aggregate.py` directly; do not take this log's re-derivation as the verification.
2. **[1.0.0_SA_CTO~Z]** Notified at 164548Z of base's respawn + this thread's state; the RAVC loop sits at
   CVO~Z, not at me.
3. **[0.8.0_AE_CloudComp base]** IDLE, event-driven.

## Compiler Tools

| Tool | Purpose this session | Result |
|---|---|---|
| `command -v comp-which` (XXX.md 1b-A.3 PATH check) | Confirm `.tools/` reachable via the `~/bin` forwarders after respawn | PASS — resolves to `/cygdrive/c/Users/AndrewBerman/bin/comp-which`; no shim re-provision needed |
| `python .tools/audit-archive-invoker.py` (XXX.md 1b-A.2) | Append-only verify + archive-when-due at startup | `rc=0, 0 finding(s), baseline=2026-07-25T164057Z, snapshot=not-due` |
| direct `python` structural walk of `L2_aggregate_output.json` | Re-derive acceptance 2 against the live artifact | PASS — 0 scalars on all 4 cells, 0 `*total*` keys, `138` absent, per-space counts intact |

**Why no estate comp-tool run:** the only inspection this session needed was of a single JSON artifact
inside my own lane's `deliverables/` — not an estate search, so there is no coupled-thing for the graph to
surface. A structural walk is also the *sharper* instrument for this specific claim than any text search:
`comp-grep` would have confirmed `138` is gone, which is the weaker property. Rule 21's raw-search gate
targets estate-scoped searching; this is a one-file self-check on my own output.

## Files Modified

- `org/tier2_senior/0.8.0_AE_CloudComp/logs/2026-07-25/nfra_complearn_l2_acceptance2_fix.md` (new, this log)

The fix itself landed in `5089f4b006` (prior session): `l2_aggregate.py` + `L2_aggregate_output.json`,
both under this lane's ownpath at `deliverables/l2_aggregate/`.
