# ADVI_PERFRP.TO-R2-DS -- the defeated-aliasing producer fix: six unguarded sites, one mechanism, and a census I got wrong before I got it right

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE (primary), IMPLEMENT, VALIDATE

**Serial:** `0.4.0_DS_ClientPlatform~G` | **Window:** 2026-09-01T07:52Z -> 09:15Z
**TO:** `ADVI_PERFRP.TO-R2-DS` @`58fee4fde9` + amendments 2 `@58fee4fde9` / 3 `@1806c8e4ec`.
Decomp cell `PRF-c-1`. Seated as CONTINUITY on ADVI_PERFRP (Rule 27 one-project-per-instance holds).
**Commits (4):** `c1f2af8a43`, `7f5b0c7cc8`, `aefa73eded`, + this log. **Push state LOCAL.**

---

## Current State

**The fix is landed, exercised and proven operative. `R2DS-AC1/AC2/AC4/AC5` PASS; `AC3` is
UNCOMPUTABLE-BY-CONSTRUCTION and cannot be closed under this TO.** Proof-of-spec instance is
schema-VALID (`proof-of-spec-check.py` rc=0, 0 violations, 5 rows) at
`org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/ADVI_PERFRP.TO-R2-DS_PROOF_OF_SPEC.json`.

**THE DEFECT: one mechanism, six unguarded call sites, two paths in.** An unguarded LITERAL `asof`
handed to `_read_gold_meta` against a store whose newest partition is older than the asof. `_activity`
reached it through the `_read_gold` wrapper; `_allocation` and `_performance` reached it DIRECTLY --
which is why "fix `_read_gold`" was a 2-of-5 remedy.

**THE REMEDY: RESOLVE at all six, via `_read_gold_le`** -- the template this file already carried at
`:168`. Nothing invented. The pin `_read_gold_le` RETURNS is a superset of the pairs the call sites
hand-built, adding `partition_date` / `requested_date` / `aliased_from_requested`; the hand-built
literals were DELETED rather than extended, because they structurally cannot express the alias.

**WHY RESOLVE AND NOT TOLERATE -- measured, per amendment 3:**
```
canonical_valuation | canonical_positions | dim_relationship | dim_asset_classification
each: 540 partitions | newest date=2026-08-28 | at date=2026-09-01: ABSENT
```
The data EXISTS under an earlier date. TOLERATE would have emitted leaves missing data sitting in
the store -- a loud crash traded for silent data loss.

**RESULT, full 11-family registry:** 9 EMITTED / 2 DECLARED-REFUSAL / **0 RAW TRACEBACKS**, up from
4 emitting with 5 crashing. Every new pin carries `aliased_from_requested=True`.

⛔ **NOT SERVED.** No deploy, no publish. Post-commit `comp-pipescript deployed --pipeline advi` reads
**70 MATCH / 1 STALE**, and the 1 STALE is `perfrp_emit_core.py` -- **the CORRECT and EXPECTED state**,
because the fix is committed and deliberately not served.

---

## What happened, in order

1. **Read at source before touching** (90997 s.1 asked for it). `comp-read` surfaced `_read_gold_le`
   in the SHAPE block -- the remedy already in the file.
2. **I falsified the issuer's "one mechanism (`_read_gold`)" scope** by counting call sites instead of
   sampling: `_read_gold` had exactly TWO live calls, and one of its four textual occurrences is
   PROSE inside `_performance`'s docstring at `:319`. Amendment 1 adopted my "three mechanisms."
3. ⛔ **THEN I REVERSED MYSELF, because my count was wrong.** I claimed `_performance` "reads no gold
   partition at that layer" -- FALSE; it reads at `:521`/`:523`. **I had grepped a 255-line range
   through `head -12` and concluded from the top of the output.** Amendment 2 adopted the corrected
   census: ONE mechanism at `_read_gold_meta`, six unguarded sites.
4. **Implemented, exercised, mutated, and wrote the proof-of-spec.**

---

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-read` | `perfrp_emit_core.py --for "how does _read_gold resolve the asof..."` | **PASS** | Surfaced `_read_gold_le` via the untruncated 48-section SHAPE block. First real use of the rule-21 law edit cut 6h earlier; it worked. |
| `comp-pipescript io` | `perfrp_emit_core.py --pipeline advi` | **PASS** rc=0 | 3 UNRESOLVED I/O sites disclosed by the tool on its own face -- not absent I/O. |
| `comp-pipescript deployed` | `--pipeline advi` (post-commit) | **PASS-WITH-EXPECTED-STALE** | 71/71/0 unrendered -> 70 MATCH, 1 STALE = the fixed core, correct because no deploy is authorized. **Plane named: WORKTREE-vs-S3, cannot see ORIGIN-vs-S3.** |
| `comp-find` | `'_read_gold\b' --corpus default` | **PASS** | 45 hits / 29,216 files; bands DEF=2 SURFACED=11 CONFIG=3 DOC=29. **This is what found the AC11 harness's monkey-patch and stopped me deleting the dead wrapper blind.** |
| `comp-validate` | `perfrp_emit_core.py` | **NOT-APPLICABLE / GAP** | `ERROR: no script matching ...` -- its registry is the BD/INF config set, no advi entry. Recorded as a gap in the TO's own mandate, **not** as a pass. |
| `commit-gate` (via `safe-commit.sh`) | 4 commits | **PASS** | `clean for 1 of 1` on both `.py` commits; risk-reflex REFLEX CLEAN, 1,662 danger nodes. |
| `comp-system` | `comp-system` | **PASS** | The comp-system gate BLOCKED the proof commit (06_current_state stale, source drift 261->262 files). Regenerated and staged 06 rather than taking the audited override -- **the offered fix worked, so the bypass was not the path.** |
| `proof-of-spec-check.py` | on the instance | **PASS** rc=0 | 7 violations first pass, all fixed; **VALID, 0 violations, 5 rows.** |

**What worked:** `comp-find`'s full-corpus census is the only reason the dead-wrapper deletion did not
break blind -- it surfaced a monkey-patch in a deliverable no reading of the core would have shown.
And the **paired mutant** is what turned "it works" into "it works BECAUSE of this change."

**What failed:** `comp-validate` cannot cover this tree. **And a near-miss worth more than the tool
gap:** a first `comp-validate` run piped to `tail` returned `rc=0` -- **that was TAIL's exit code.**
Reading a pipeline's rc as the tool's verdict would have recorded a false PASS on a tool that never
ran against the subject. `${PIPESTATUS[0]}`, not `$?`, after a pipe.

**Gap found:** the TO's `compiler_tools_mandate` names `comp-validate` for a script its registry
cannot address -- routed as an OBSERVATION in the proof instance.

---

## Controls

**MUTANT, paired, prediction stated before running:** `_read_gold_le` replaced in-process with a
literal-asof reader reproducing pre-fix behaviour.
```
mutant   -> RAW NoSuchKey on 5 of 5   (the exact original error class)
restored -> EMITTED     on 5 of 5
```
**FIRED-AS-EXPECTED. It discriminates in BOTH directions**, so it bounds over-firing as well as
under-firing -- the aliasing is the operative change, not a coincident one.

**NEGATIVE CONTROLS:** the three GUARDED sites `:168`/`:241`/`:1083` byte-identical to `origin/CLOUD`
after the change; `transactions_relationship` still refuses (AC4); `roster_relationship` untouched.

---

## Blockers

**None at this seat.** Two items owned elsewhere:
- **AC3** -- needs a serve act with its own word and `change_management` entry. Not mine to close.
- **The AC11 harness repair** -- routed, unowned, awaiting a ride-or-detach ruling from
  `1.0.0_SA_CTO`.

---

## Next Steps

1. **[`1.0.0_SA_CTO`]** Rule whether the AC11 emit-path harness repair rides ADVI_PERFRP or becomes its
   own item. **It is DEAD on two independent counts and has been since the Round-2 rewrite** (proven
   against `origin/CLOUD`, so it pre-dates this TO). `0.4.0_DE_ClientPlatform~D` 91079 raises the
   severity: it lets that seat's separate RENDER-plane AC11 pass VACUOUSLY. I will take it on dispatch;
   I did not take it here because **a verification arm repaired inside the act it certifies has no
   independent vintage.**
2. **[`2.0.0_SA_COO` + `1.0.0_SA_CTO`]** The never-widen co-sign for publishing the 9 -- that act is
   what makes AC3 scorable.
3. **[`0.4.0_DE_ClientPlatform~D`]** The three consumed leaves now BUILD. **They are NOT SERVED**;
   that seat's "L3 Performance still a shell" prediction is about the served state and is not yet
   falsified.
4. **[integrator `0.0.0_AB_MSTR`]** 4 commits LOCAL this window.
