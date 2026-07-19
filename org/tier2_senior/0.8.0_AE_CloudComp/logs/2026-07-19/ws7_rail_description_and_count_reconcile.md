# NFRA_SYSPARITY.WS-7 -- rail description + count reconcile

**archetype:** MIXED (SCRIBE doc-parity + a scoped IMPLEMENT: the front-end docstring fix)

**Session:** `0.8.0_AE_CloudComp~Z` | **Date:** 2026-07-19 | **TO:** NFRA_SYSPARITY.WS-7 @ac96b0803
(COO context-reallocation of the ~Z comp-which/COMPRAIL/count-reconcile thread, Andrew-direct idle-
reallocation-by-context). Ground-truth spec: `docs/briefs/NFRA_SYSPARITY_BRIEF_20260719.md` §3 comp-tools.

## What WS-7 asked + what landed

| Part | Ask | Done |
|---|---|---|
| (a) | `03_comp_tools.md` names the rail but not its ENFORCEMENT | Added `## Rail enforcement (COMPRAIL -- Rule 21)`, grounded on `.tools/hooks/comp-tool-hud.sh`: LIVE marker-escapable hard-DENY on **graph-backed classes ONLY** (raw-aws-inspection + `infra/.tf`-grep); broad repo-`grep`/`find`/`rg` + native `Grep`/`Glob` = STAGED-AS-NUDGE (advisory); Read/operational-aws/pipe-greps = free; audit log + `/freeform`. **Self-corrected post-accept @<fix> -- v1 (@2f5018048) OVERSTATED the broad-grep tier as a live deny (see Self-correction below).** |
| (b) | "tenant-neutral comp-tools" over-reach | Corrected `README.md` Generalization: the MECHANISM (C0-C3/graph/FEDOBS/loop) is tenant-neutral; the comp-tool CLIs are NOT -- only comp-genesis + comp-which parameterize. **Tightened per CVO VL#10:** the ~61 CLIs are Opal-BOUND (not tenant-parameterized); ~12 carry EXPLICIT `opal-*` literals (grounded: 11 comp-* source files at HEAD), the rest bound by graph/estate assumption -- survives a literal-count rebuttal. Porting UNBUILT (P6). (`:39` "comp-genesis registered tenant-neutral" is TRUE -- left.) |
| (c) | SDK front-end docstring 3->4 | `frontends/__init__.py` enumerated 3 and OMITTED `python_resolved` (the REAL whole-project RESOLVED_SEMANTIC tier, landed 2026-07-18) while mislabeling `tree_sitter_stub` as THE resolved tier. Corrected to FOUR front-ends across three tiers; tree_sitter_stub reframed as the TS/JS-only remaining gap. commit-gate PASS. |
| (d) | Reconcile remaining docs/memory count copies to the live gate | Live gate authority (comp-manifest-check) = **79 exec / 61 routable / 66 entries-tools / 82 coverage-map** at run time. The one present-tense stale copy -- `NFRA_SYSTEM_PRD.md:9`+`:28` "~30 tools" -- is an **ANY_CTO-lane architecture doc**: the owned-paths gate correctly BLOCKED my edit, so it is **ROUTED TO CTO** (recommend "~60 tools; gate-maintained -- see comp-manifest-check"), not self-applied. No in-my-lane count edit remained -- (d) is entirely identify + route + confirm-gate-managed. |

## The count-reconcile was minimal BY DESIGN -- and here is exactly what I did NOT touch, and why

The sweep across docs/ + memory/ + infra/system/ found the stale-count surface is already mostly gate-managed
or historical. I reconciled ONE copy and deliberately left the rest:
- **`03_comp_tools.md` counts (61/82)** -- inside `<!--cs:-->` `comp-system`-managed regions, ALREADY LIVE.
  The doc itself says "do not hand-edit the numbers between the cs: markers." Left untouched (refresh = WS-2).
- **CLAUDE.md count line** -- CTO already refreshed 62/49 -> 78/60 (@49dad1c83). NOT re-touched (CTO owns the law).
- **memory/** -- ZERO stale tool-count copies (the one "0 of 63 store files" hit is a store-vocabulary count, not a tool count).
- **Historical records LEFT AS-IS (rewriting them would falsify the record):** the NFRA_COMPCLOSE / COMPASSURANCE
  PRD descriptions of the PAST four-disagreeing-counts defect ("of 63" / "66 entries / 38 tools"); the
  `comp-tool-universe.md` / LD-0271 DOCTRINE lines ("ship no N of 63"); date-anchored snapshots; approximate
  coverage metrics (NFRA_LIVELEARN "4/~63") and the already-correct "~60 tools" in NFRA_COMPASSURANCE.md.

- **`NFRA_SYSTEM_PRD.md` "~30 tools" (lines 9 + 28)** -- the ONE genuine present-tense stale copy. But it is an
  **ANY_CTO-lane architecture doc**: the owned-paths gate blocked my commit (correct -- architecture PRDs are
  CTO-owned, like CLAUDE.md's count line). Reverted my edit; ROUTED the "~30 -> ~60 gate-cited" fix to CTO.

**A doc that RECORDS a past finding is not a stale live-claim; editing it corrupts the finding. Only the
present-tense "we have ~30 tools" claim misleads a reader about current reality -- and that copy is CTO-lane,
so it is routed, not self-applied. The owned-paths gate enforced that boundary; I did not have to remember it.**

## The live number moved DURING the session -- which is the whole point of "cite the gate, don't hand-count"

comp-manifest-check read **78/60** during my TO-4 reconcile earlier this session and **79/61** during WS-7
(the registration flow added a tool between them). I therefore wrote "gate-maintained -- see comp-manifest-check"
rather than freezing a digit. A hand-counted number is stale the moment the next tool registers; the gate is not.

## Compiler Tools (AC5 -- every mandate <run> reproduced, observed vs <expect>)

| Phase | run | observed | vs expect |
|---|---|---|---|
| 1 before-write | `comp-manifest-check completeness` (registration-invariant) | 79 tracked / tools_index 61 / excluded 15 / entries-tools 66 / coverage-map 82; PASS | The LIVE gate number (authority). Differs from the TO's 78/60 -> used the live invariant per if_mismatch + noted the +1 delta. |
| 1 before-write | stale-count sweep `docs/` + `memory/` + `infra/system/` | only NFRA_SYSTEM_PRD:9 "(~30 tools)" is a present-tense live-claim; rest = historical/doctrine/auto-managed | Confirmed the reconcile surface; classified each hit (record vs live-claim). |
| 3 after-commit | grep 03 for enforcement terms | 5 hits (rule 21 / rail-checked / DENY / freeform / HUD / rail.log / STAGED-UNARMED) + `## Rail enforcement` header | PASS -- 03 now describes the gate. |
| 3 after-commit | re-grep stale counts (present-tense) | only `NFRA_SYSTEM_PRD` "~30 tools" remains (CTO-lane, routed) | The IN-LANE surface is clean; the sole present-tense live-claim is a CTO-owned architecture doc -> routed, not self-edited. |
| owned-paths | `safe-commit` owned-paths gate | BLOCKED `NFRA_SYSTEM_PRD.md` (lane=ANY_CTO, agent not permitted) | WORKED AS DESIGNED -- reverted the edit, routed to CTO. Same class as the CLAUDE.md-is-law boundary. |
| after-write | `commit-gate.sh __init__.py` | All checks passed (py_compile + ds-precommit + ruff) | PASS. |

comp-which not run live (a live probe pollutes the rail log it feeds; the enforcement I documented is
source-grounded on CLAUDE.md Rule 21 + the gate this session already exercised). `org/compiler-tools-log.md`
row appended same commit.

## Self-correction (post-accept) -- I OVERSTATED my own (a), and caught it by EXERCISING the gate

v1 (@2f5018048, the version COO accepted) said the (a) enforcement subsection was: "Bash raw repo-grep/find/rg
+ a raw aws INSPECTION ... DENY unless the call carries a `# rail-checked` marker." **That overstates.** Grounding
against the LIVE gate (`.tools/hooks/comp-tool-hud.sh:184-198`): HARD-DENY fires ONLY on the graph-backed classes
-- raw-aws-INSPECTION (tier 1) + `infra/*.tf` grep (tier 2a). The **broad repo-grep/find/rg tier is STAGED-AS-NUDGE**
(hook:193-194: "STAGED as nudge ... today it routes to the comp-which advisory nudge, NOT a deny"); native
`Grep`/`Glob` NEVER deny (hook:189). My first bullet even CONTRADICTED my own last bullet (which correctly called
the broad-grep hard-DENY STAGED-UNARMED). Corrected 03 to the live tiers + flagged that CLAUDE.md Rule 21's prose
is itself the announce-phase TARGET, not the live state.

**Why this is the finding, not just a fix:** WS-7 (a) exists BECAUSE "03 names the rail without its enforcement."
I then described the enforcement OVERSTATED -- representation-over-reality, in the fix FOR a representation gap,
which is the exact class NFRA_SYSPARITY is about. Root cause: I followed Rule 21's PROSE instead of exercising the
hook. It was caught by running the control (reading the actual gate before recording the PASS), not by care --
"CARE IS NOT A CONTROL." Self-flagged to CVO before its verdict.

## LD-0318 CVO gate

Per PRD S7 + LD-0318, WS-7's rail-description accuracy + the count reconcile are CVO-verified. Pinging CVO on land.

## Outcome

WS-7 COMPLETE: parts (a)(b)(c) landed + verified; (d) count-reconcile scoped honestly -- the one present-tense
live-claim (NFRA_SYSTEM_PRD "~30 tools") is an ANY_CTO-lane architecture doc, ROUTED to CTO (owned-paths gate
enforced the boundary); 03 counts auto-managed + current, memory clean, historical records + CLAUDE.md-law
left untouched. No CLAUDE.md self-edit, no architecture-PRD self-edit, no historical record rewritten.
