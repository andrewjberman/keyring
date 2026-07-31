# 0.8.0_AE_CloudComp~C -- NFRA_VELOCITY WS-C1: the D3 lifecycle axis, built + enforced

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE
**Window:** 2026-07-31 ~0245Z -> ~0450Z (site Z). Lane `~C` (no `~C` agent folder exists; logged to
the base folder per the /log convention, lane named here).
**TO:** NFRA_VELOCITY_CORE.WS-C1.lifecycle-axis-build (@5da07cf62, amended @d79957d22)
**Spec:** WS-C1_LIFECYCLE_DESIGN_SPEC.md -- consumed at REV 1 @bab75bba5, REV 3 @691860493, REV 4 @50643084b
**Gate:** 1.0.0_SA_CTO~Z (items 1-17) -> 3.0.0_SA_CVO~Z verify. **Status: WS-C1 CLOSED, nothing owed.**

## Summary

Built the D3 lifecycle/supersession vocabulary into the rule bank and then ENFORCED it on the
kill-list path. The spec moved through four revisions while I built; I built the section three
times and threw away the first two rather than patch a stale artifact forward.

Two of my inputs changed the spec: `KEEP_DORMANT` (admitted as `DORMANT`, the 8th->7th value) and
the halt that converted step 2 from a gate into a precondition.

## Deliverables landed

| commit | author | what |
|---|---|---|
| `880f527cc` | CTO~Z (I built) | rule bank v1.7 -> v1.8, the lifecycle axis. Gate 19/19, ratified drift NONE |
| `b5854411b` | me | **item 10** -- the gate ACTUALLY ENFORCED on comp-legacywriter's kill-list path |
| `e05afbdc6` | me | TO status staged -> pending |
| `895c3b94a` | CTO~Z (my measurement) | affected_population MEASURED: at most 3 of 7 |
| `17b24fad2` | CTO~Z (my finding) | corrects the false `variance.Orphan` liveness claim |
| `fffba74c2` | CTO~Z (my (b) result) | precondition gains a 2nd requirement + a named casualty |

**Land path:** `org/modules/graph/` is exec-locked (`ANY_EXEC`); my serial is NOT permitted, so the
rule bank was BUILD (me) -> HAND OFF -> GATE + LAND (CTO~Z). `comp_legacywriter.py` is
`ANY_EXEC_OR_AE` and I landed it myself. Both verified with `check_agent` + a positive control.

## What the axis does (one paragraph, for a zero-context reader)

`lifecycle_class` is a 7-value enum (PERMANENT / TRANSIENT / EVENT_CREATED / DORMANT / LEGACY /
RETIRED / UNDECLARED) declared per contracted resource, producer-asserted and never inferred. Each
value states BOTH polarities -- what ABSENCE means and what PRESENCE means -- because absence is
HEALTHY on 2 of 7 rows and presence is a FINDING on 2 of 7, so a single-polarity existence detector
is wrong on 4 of 7, in the direction that proposes deleting live infrastructure. Every value carries
required falsifier fields, `revalidate_by` decay, and an explicit `scope`.

## Item 10 -- the enforcement half (`b5854411b`)

Added `resolve_lifecycle()` + `load_lifecycle_contracts()` to `comp_legacywriter.py` and gated the
scorer in `dossier()`. Behaviour on the REAL census path, exit 0:

```
contracts: registry ABSENT -- 0 declarations, every resource UNDECLARED
0 of 439 scored surface(s) carry a declaration; 439 UNDECLARED
0 GATED; 0 kill-list-eligible      (4846 files scanned, 439 surfaces still scored + printed)
```

The tool now CHECKS everything and can CLAIM nothing -- the claim-vs-check bound as behaviour, not
prose. 7 new C9 controls (17/17 total), each asserting behaviour, plus 3 mutants run: empty
`GATED_CLASSES`, bypassed required-field check, and a name-inferring resolver. All three kill their
controls. CTO~Z ran an INDEPENDENT mutant (GATED_CLASSES = all seven) and got `[FAIL] C9b, 16/17`.

## Findings issued

1. **`KEEP_DORMANT` was missing from the spec.** Disclosed a divergent draft unprompted before
   landing, listing five divergences against my own interest. CTO~Z read `keep-dormant.yaml` at
   source and amended: rev 1 would have proposed deleting the registry's deliberate belts.
2. **`variance.Orphan` HAS NO EMITTER.** Source-confirmed `summary_corpus.py:582`
   (`singleton -> return None  # Orphan/Superseded deferred v1`); only 4 verdict sites
   (Fork-Shadow x2 / Canonical / Twin); zero repo-wide emitters; no dynamic `kind`. It is DECLARED
   at labels + catalog + polarity + phrasing and IMPLEMENTED at none. **HALTED step 2 rather than
   write a guard on absent code** -- an unfalsifiable, unmutatable control. F-2's structural insight
   stands; only its liveness premise was false, and I had propagated that false claim into the rule
   bank myself.
3. **The assumed population of 7 collapsed a conjunction.** `variance.Orphan` is
   singleton AND no-sibling AND no-consumer; `keep-dormant` establishes only the third. Measured via
   the GOVERNED `_position_key` (not hand-simulated): **4 of 7 positively excluded** -- 3 carry no
   firm-dimension token (`mdpf`/`imo` are not in `[bd, cot, inf]`, so position_key is unchanged ->
   no verdict) and `bd-gold-qa-runner` HAS A LIVE SIBLING (`inf-gold-qa-runner`).
4. **(b): the named casualty.** `inf-gold-incremental-daily` (registry entry 1, Tier A) clears BOTH
   structural conjuncts -- 4 incident edges, ZERO consumes-class against a denominator of 7. But
   "no consumer" has NO implemented definition, so I reported BOTH readings and refused to pick;
   the divergence (reading A flags a live belt, reading B does not) is the finding.
5. **`SILENT-RESIDENT` and `variance.Orphan` diverge on a real resource** -- that node IS contained
   by `AEventMotif`, so an enumerator traverses it. The renames separated two genuinely different
   predicates, not merely two colliding tokens.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-ontolint` | bare, x3 | PASS | Relation-vs-Role invariant held across every rule-bank revision |
| `comp-manifest-check` | `completeness`, x3 | PASS | incl. stage-2 vocab invariant (23 tools, all rail/grain/plane/scope in canon enums) -- the path my change had to not break |
| `comp_output_contract.py` | direct, x3 | rc=0 | registration invariant unaffected |
| `comp-system` | bare, x3 | rc=0 | regenerated `06_current_state` + 7 sibling spans; hit the documented uncommitted-source deadlock |
| `comp-kuzu` | 5 queries | PARTIAL | sibling probe + edge-type resolution. **First run exceeded the 120s foreground timeout -- see Gap** |
| `comp-legacywriter` | `--self-test`, `--census` | PASS | 17/17 controls; census exercised the new gate end to end |
| `commit-gate.sh` | per .py edit | **CAUGHT A REAL BUG** | undefined `contracts` -- would have been a runtime NameError on every census |
| `safe-commit.sh` | x3 | PASS | surface-check OK, risk-reflex clean/read |
| `owned-paths-validate` | `check_agent` x9 | PASS | lane determination, with positive controls |

**What worked:** the commit gate caught a total-failure defect I was entitled to dismiss as
paperwork. Positive controls caught an undiscriminating instrument. Mutants proved the new controls
can redden.

**What failed (mine, 4):** (1) an owned-paths harness that returned False for EVERYONE including
the control -- I passed the wrong config node; (2) a verifier that printed `*** RATIFIED DRIFT ***`
because I reused a cumulative flag for a specific verdict; (3) a comp-kuzu timeout recorded as
"returned nothing" when it had been BACKGROUNDED and COMPLETED with results -- I never read the
output file; (4) the gate wired into the wrong function. **None was caught by care.**

**Gap found:** `comp-kuzu` routinely exceeds a 120s foreground timeout on this box and gets
backgrounded. The failure mode is that a backgrounded completion reads as a null result unless the
agent goes back for the output file. This is a genuine instrument-honesty hazard, not just latency:
**a tool's non-return is a MISSING OBSERVATION, never a measurement.** No tool change proposed.

## Blockers

None outstanding. Two were hit and cleared: the exec-lock on `org/modules/graph` (routed, not
overridden -- `.owned-paths.yaml` documents this class recurring three times, remedy is always a
lane-add BY A GRANTOR, never the grantee) and the `comp-system` uncommitted-source deadlock
(documented path, cleared by regenerating).

## Incident touched (not mine)

A rev-1 build of mine was lost uncommitted from the shared working tree -- MSTR~Z's 0312Z
backtick/command-substitution incident (CLAUDE.md F-010). **I reported the loss WITHOUT naming a
mechanism** (my leading suspect, `comp-system`, would have been a false accusation) and confirmed
fidelity of the recovered patch `5cf6bf72e` as author, including chasing two apparent gaps that
turned out to be my own deliberate removals. Root cause: three seats share one checkout.

## Current State

- Rule bank at HEAD: **v1.8**, lifecycle axis live, all my findings folded. Verified at HEAD, not
  from self-report.
- `comp_legacywriter.py` at HEAD carries `resolve_lifecycle` + 7 C9 controls; gate live but
  **INERT in the gating direction** (0 declarations exist until ESTATE WS-E1 lands contracts) --
  its present effect is entirely claim-suppression. Stated in-file, not implied.
- `variance.Orphan` remains UNIMPLEMENTED and UNGATED by design; the rule bank now carries a
  PRECONDITION -- implementing it requires the lifecycle exclusion in the same change, and must
  state which no-consumer reading it uses.
- Repo 0/0 with origin. 06 current.
- Untouched by standing hold: rule bank (exec-locked), `summary_corpus.py`, audit-archive, stash.

## Next Steps

- **[1.0.0_SA_CTO~Z]** owns WS-C2. Nothing in CORE starts without their word.
- **[0.8.0_AE_CloudComp~C]** IDLE-BUT-WARM. Probes (a) and (b) STOOD DOWN -- do not restart.
  CVO~Z formally withdrew the item-17 prerequisite; no measurement obligation remains.
- **[ESTATE / WS-E1]** unblocked by the vocabulary; the gate becomes load-bearing when contracts land.
- Untracked infra/system regeneration (pre-existing tool-count drift 91->90 / 70->69) is sitting in
  the shared tree, NOT mine, left for its owner.
