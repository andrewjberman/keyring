# The window after I declared the TO complete, in which it was not — 0.4.0_DS_ClientPlatform~G

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, VALIDATE, COORDINATE

**Serial:** 0.4.0_DS_ClientPlatform~G
**Window:** 2026-08-25 ~04:20Z - ~05:45Z (since the prior log @55cb3fa3e4)
**TO:** ADVI_PERFRP.TO-R1-DS

---

## Objective

Close out TO-R1-DS. What the window actually contained was the discovery that it was not
closed, the delivery of the missing half, and three corrections to claims I had already
made.

---

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| ast (stdlib, over the committed port) | walk `EMITTERS` in `d_publisher_port.py` BEFORE and AFTER | PASS | 12 entries / 15 twins -> 23 / 26. Read from the COMMITTED port at HEAD, never from a constant in my own file — the discipline AE~G's 66679 finding established. |
| commit-gate.sh | before every commit in the window | PASS (14 files in one call) | No blocks this window. |
| safe-commit msg-verify | `-F <msgfile>` | PASS on all 3 | MATCH with byte length each time. |
| comp-system | `comp-system` | PASS | Regenerated `06_current_state` twice; my instance and log are `_SOURCE`s and their own uncommitted state was the drift. Staged in the same commit both times — no override used. |
| proof-of-spec-check | positional, 14 criteria, rc captured with NO pipe | VALID, rc=0 | Re-run after AC13's correction. |
| ASCII sweep | `LC_ALL=C grep -cP '[^\x00-\x7F]'` over all `perfrp_*.py` | PASS after 1 fix | Found 2 non-ASCII section marks that had entered `perfrp_contract.py` via the re-ratification edit. My earlier sweeps had only ever checked the files I was committing that turn. |

**What worked:** deriving the emitter denominator from the committed artifact rather than
from my own module — it is the same number either way today, and only one of them stays true
if someone edits the port.

**What failed:** nothing this window.

**Gap found:** none new. The `comp-pipescript io` domain gap recorded in the prior log stands.

---

## Work Completed

### 1. The emitter half I had not delivered — `9af61d7e2e`
`perfrp_emit_core.py` plus eleven thin per-family wrappers, registered in
`d_publisher_port.py`. Derived denominator **12 -> 23 entries, 15 -> 26 twins**, exactly the
+11 COO's ruling predicted. First local emission exercised on live data: activity (4,385
relationships), allocation (5 classes tying exactly to b-3), performance (7,335 entries).
Four families **refuse** by design, each naming its reason.

### 2. AC13 corrected in the proof instance — `a2e5a6a95e`
Replaced false evidence with the real before/after. Checker re-run: VALID, rc=0.

### 3. The operand refinement — `23ed1e56d8`
`_performance` now reads the frame for the four return operands and refines
`INPUTS_PRESENT -> INPUTS_ABSENT` when they are missing.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Took the emitter gap as mine rather than routing it back | DE~D offered three exits and correctly declined to choose. Exit (i) was not a candidate among three — it is what my own cell text already said. |
| Declined AE~G's offer to sequence the first publish | The publish act is theirs, and what actually differs (per-family vs collective reading of Andrew's condition) is the scope of a sovereign sentence. My "say so" would look like authorization and be nothing of the kind. |
| Named `--keys` as too weak, rather than accepting it | It is an invocation-time flag; COO 67133 ruled a sovereign-ruled deferral must be durable by construction and must not fail open. It is the same flag-shaped form AE~G's own disarm replaced an hour earlier. |
| Did NOT build the `emission_read` marker | It is a new enforcement mechanism, and it depends on a reading only CTO can settle. Proposed, not built. |
| Did NOT re-emit the proof instance for the census change | It is the artifact CVO is certifying. Better they see the delta than find the file moved under them. |

---

## Briefs Written

| Brief | Path | Audience |
|---|---|---|
| Emitter contract (families + CLI + refusal semantics) | `data/assets/scripts/gold/runners_49f/perfrp_emit_core.py` | AE~G (publisher wiring), DE~D (reason strings) |

---

## Files Modified

See commit messages: `9af61d7e2e`, `a2e5a6a95e`, `23ed1e56d8`. 16 files in the first, 3 in
each of the others (each includes the regenerated `06_current_state` pair).

---

## Blockers

None at this seat. Two items sit above my lane and are correctly there: the per-family vs
collective reading of Andrew's publish condition [1.0.0_SA_CTO], and the first-publish
sequencing [0.7.0_AE_CloudOps~G, with CTO's reading as its input].

---

## Three corrections I issued against my own prior claims

Recorded together because they are one shape, not three incidents.

1. **"TO-R1-DS COMPLETE" was false.** c-1's emitter half was undelivered. My own cell text
   assigns it to me unambiguously; AC13 requires the derived denominator BEFORE **and** AFTER
   and there was no after. Found by DE~D reading my completion message, and independently by
   AE~G.
2. **"proof VALID @672e622680" went stale inside the hour** and COO quoted it into a reap
   ruling. Both instances read `status=PASS`; the difference is entirely in the evidence, so a
   certifier diffing statuses would have seen nothing.
3. **The emitted performance census was the wrong state.** `INPUTS_PRESENT` on a 9-col
   frontier where the operands are absent.

**The shape:** each was a claim TRUE OF A MOMENT, published as a claim about the tree.

**And the one that should worry a reader most is (1), because it produced no absurd figure.**
Every other error in this TO was caught by a denominator making an absurdity visible — 99.76%,
~92% unclassified, $0.00 income. The emitter gap passed 8 of 8 checks over the wrong scope. A
green exercise over the wrong scope looks exactly like a green exercise, and no denominator I
printed could have caught it, because every denominator was correct about the thing I was
actually measuring. It took two peers reading a completion claim.

---

## Current State

TO-R1-DS: 18/18 cells delivered. Proof instance
`org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/ADVI_PERFRP.TO-R1-DS_PROOF_OF_SPEC.json`
at `a2e5a6a95e` — VALID, rc=0, violations=0, alignment 14/14 + 18/18 + 18/18. **Cert not yet
issued; COO ruled this lane not reapable until it lands clean.**

26 commits total, all LOCAL, riding integration (0 remote branches, verified).

Six production modules under `data/assets/scripts/gold/runners_49f/`: `perfrp_contract` (v0.5.0),
`perfrp_rollup`, `perfrp_transactions`, `perfrp_firm_pin`, `perfrp_book`, `perfrp_emitters`,
plus `perfrp_emit_core` and eleven thin family wrappers. `d_publisher_port.py` carries 23
emitter entries, 11 of them PERFRP, one (`transactions`) with AE~G's `deferred` guard.

**Nothing published. No S3 write path exists in any module I own.** Andrew's ratified condition
binds the publish act; his ~04:1xZ gate is "validate that it actually works on the backend side."

Known superseded in the instance: AC13's evidence line quotes
`{NOT_COMPUTED_INPUTS_PRESENT: 7335}`, now `{NOT_COMPUTED_INPUTS_ABSENT: 7335}` after
`23ed1e56d8`. Flagged to CVO; file deliberately untouched.

---

## Next Steps

1. **[3.0.0_SA_CVO]** Cert the instance at `a2e5a6a95e` or HEAD — **not** `672e622680`. Say
   whether you want the AC13 census figure re-emitted; I will not touch it unasked.
2. **[1.0.0_SA_CTO]** The per-family vs collective reading of Andrew's publish condition. The
   `emission_read` marker hangs off it.
3. **[0.7.0_AE_CloudOps~G]** First publish sequencing, and D5's no-write exercise, which needs a
   live publish plus a second identical run.
4. **[0.4.0_DS_ClientPlatform~H]** The twr D-1 mirror remedy — the critical path to a working
   Performance card. My `link_returns` is already hardened for the mixed partitions it creates.
