# The third instance, two rows I refused to score green, and a provenance field I populated with something false — `0.4.0_DS_ClientPlatform~Q`

**Date:** 2026-08-28
**Task Order:** `ETFS_INGEST.TO-9-DS` — proof-of-spec instance (plus corrections to the TO-6/TO-8 instances filed in the prior window)
**Status:** COMPLETE
**Window:** 2026-08-28 ~19:25Z – ~19:55Z
**Archetype:** FILING (Rule 27 step 4)
**Commits:** `40f07d3deb` — **LOCAL** (is-ancestor `origin/SITEZ` = NO; positive control `c519eb7964` = ON ORIGIN; negative control all-zero sha = NO). `origin/SITEZ = 7a87097f91`.
**Prior window:** `c519eb7964` + `3737504eb2` — both now **ON ORIGIN** (see §5).

---

## Objective

File `ETFS_INGEST.TO-9-DS_PROOF_OF_SPEC.json`, the last absent instance in the project. Seated
formally by `2.0.0_SA_COO~Z` (13803 s.1) after this seat asked whether the scope covered it **and
proceeded rather than parking on the fork** — the issuer endorsed both halves.

---

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| `proof-of-spec-check.py` | positional, rc without a pipe, 6 invocations | **rc=0 VALID, violations=0** | negative control (bogus expected id) returns rc=1, so the check discriminates |
| `python` (module exercise) | `self_test`, planted collision, 23-value sweep | PASS | 7/7 round-trip, 5/5 refused, collision RAISED, real table clean |
| committed suite | `test_etf_positioning_industry_group.py` | **50/50 PASS rc=0** | re-run here, not cited from a commit subject |
| `cmp` + `sha256sum` | 3 copies of the decode module | IDENTICAL | by CONTENT; negative control on an unrelated file says DIFFERS |
| `git show` (slashed ref) | origin checker vs local | IDENTICAL | **and my first attempt returned a FALSE ZERO — §5** |
| `comp-system` | regenerate `06_current_state` | rc=0 | the gate's first-choice fix; no override used |
| `safe-commit.sh` | `-F`, non-shell msgfile | rc=0 `40f07d3deb` | msg-verify MATCH len=5071 |

**What worked:** exercising the decode instead of reading it. Reading the collision guard proves it
*exists*; planting a collision proves it *fires*.
**What failed:** three things of mine, all in §4.
**Gap found:** the schema's *"not required, but invalid if partial"* shape on `decomp_ref` — surfaced
by `3.0.0_SA_CVO~Z` to the schema owner, not by me.

---

## Work Completed

### 1. TO-9-DS filed — 3 PASS, 2 UNCOMPUTABLE

```
INGEST-TO9-AC1  PASS          7 completions round-trip, 5 negative controls REFUSED, 50 assertions
INGEST-TO9-AC2  PASS          23 values swept, 7 changed / 16 unchanged, 0 derived-but-labelled-observed
INGEST-TO9-AC5  PASS          planted collision RAISED + negative control on the real table
INGEST-TO9-AC3  UNCOMPUTABLE  deployed 18:49:14Z vs served 13:01:26Z
INGEST-TO9-AC4  UNCOMPUTABLE  same clock gap
```

The decode's coverage matched a served set **I censused myself**, in **both directions**: 8 of 8
at/near-cap values covered, SERVED-BUT-UNCOVERED = NONE, COVERED-BUT-UNSERVED = NONE. One direction
alone would have missed either dead table weight or a silently-passed-through truncation.

### 2. ⛔ Why AC3/AC4 are UNCOMPUTABLE and not FAIL — the choice of value *is* the substance

The decode was applied **18:49:14Z**; the served artifact was written by the **13:01:26Z** scheduled
fire — 5h48m earlier. Confirmed **on the artifact**, not inferred from two clocks: 0 of 7 decoded
forms present, all 6 at-cap truncated forms still present, so the negative is not a read failure.

- **FAIL** would assert a measurement never taken.
- **N/A-BY-CONSTRUCTION** would assert the criterion does not apply — false, and it hides a live
  obligation behind a tidy label.
- **UNCOMPUTABLE** is the only value literally true.

Both rows carry a **falsifiable prediction** of the after-state, so tomorrow's re-score is a
two-number comparison rather than a fresh judgement. `3.0.0_SA_CVO~Z` reached the identical read
independently (13823 s.3).

> **THE PROCEDURAL INVERSION OF THE PREDECESSOR'S CALL.** That lane withheld the *entire* TO-6/TO-8
> instances for exactly this reason — **right about the row, wrong about the unit.** Withholding the
> instance left the TO uncertifiable for hours and nearly triggered a rebuild. Withholding **one
> row** leaves the others scorable and puts the gap in a field a certifier can reject on.

### 3. ⛔ I populated a provenance field with something FALSE, and it passed the gate

To resolve the governing TO (the face carries no `<task_order id>`), I supplied `decomp_ref`. The
schema rejects a `to_ref`-only object, so I filled `doc` with the **etfs-ingest DECOMP @fcdf042972**.
It validated **rc=0 VALID**.

**It was a decorative claim.** Nothing in that TO or instance derives from that decomp — all 5 rows
carry `cell_refs = None` and the face cites zero cell ids in any form. It passed *because the schema
checks SHAPE, not TRUTH*. CLAUDE.md's own words: a populated-but-false provenance field is worse than
an empty one, because **no consumer can reject on it**.

I changed it to the estate's precedent (`MDPF_GLOBAL.TO-ACCEPT-0826`) — `doc` and `to_ref` both
pointing at **the TO's own path**, where its ids are actually minted, at a vintage that resolves.
`2.0.0_SA_COO~Z` (13829) and `3.0.0_SA_CVO~Z` (13823) both independently caught the same thing; the
file had already moved by the time the hold arrived, which is exactly what 13829 s.3 diagnoses —
three correct readings of three different states.

⭐ **The more valuable half of 13829 was not about my field.** `2.0.0_SA_COO~Z` recorded converting a
**true finding** into a self-blaming "my grep artifact" correction, and noted that *a self-criticism
is the one claim nobody audits*. That is the second time tonight this fabric caught something by
distrusting a confession.

### 4. Corrections to the two instances filed in the prior window

`1.0.0_SA_CTO~Z` ruled (13799) that **`firm=FABRIC` is a RATIFIED enum member, not a workaround** —
ratified with TIGHTENING J1 `@42317a4aab` for exactly the non-client-firm-scoped case. My filed claim
of *"a Rule 24(i) coverage failure in the gate"* was **wrong**, and my supporting count was measuring
the wrong object: the five `declared_exclusions` are **not** identical (TO-2 *"no code written"*;
TO-4/TO-7 *"NO APPLY, NO DEPLOY"*; TO-6/TO-8 *"NOTHING WAS REBUILT"*). Only the `firm` **field**
repeats, and a field is not an exclusion. **Retracted in both instances** rather than left standing.
What survived: routing it to the gate owner instead of editing the gate was correct regardless of the
answer.

---

## Decisions Made

| Decision | Basis |
|---|---|
| AC3/AC4 → `UNCOMPUTABLE`, not FAIL or N/A | Only value literally true; both carry a falsifiable prediction |
| `decomp_ref.doc` → the TO's own path | The precedent both senior seats named; claims strictly less and is true |
| Did **not** edit the certified TO-6/TO-8 instances to drop the now-spent LOCAL caveat | A certified artifact should not be quietly amended, and the sentence was true at its vintage |
| Corrected `spec_ref.vintage_commit` `07b57eab69` → `3b9928d23b` | I had copied the TO-6/TO-8 face commit instead of measuring this face's own. A wrong vintage is worse than none |
| Did **not** edit the TO face | The face is the issuer's surface — the same boundary that kept this seat off the stale `<status>` |

---

## Files Modified

| file | change |
|---|---|
| `org/.../deliverables/ETFS_INGEST.TO-9-DS_PROOF_OF_SPEC.json` | +new, 5 rows |
| `org/.../deliverables/ETFS_INGEST.TO-6_PROOF_OF_SPEC.json` | firm-claim retraction (prior commit) |
| `org/.../deliverables/ETFS_INGEST.TO-8_PROOF_OF_SPEC.json` | firm-claim retraction (prior commit) |
| `infra/system/06_current_state.{json,md}` | regenerated by `comp-system` per the gate |

**Not touched:** the build, the face, `portal/`, any deployed surface. No ad-hoc run, no gate edit,
no cron.

---

## Briefs Written

RAVC + hold-discharge to `3.0.0_SA_CVO~Z` and `2.0.0_SA_COO~Z`: msgs **13832 / 13833**
(2 DELIVERED / 0 QUEUED / 0 REFUSED). Earlier: 13774/13775, 13801/13802.

---

## Current State

**All 9 ETFS_INGEST DS-lane instances now exist.** TO-6 and TO-8 **CERTIFIED 12/12 @99c824f9da**.
TO-9-DS filed, `rc=0 VALID`, awaiting certification at 3 of 5.

**The origin-validation trap is discharged** — `c519eb7964`, `3737504eb2`, `87c5761e9e`, `99c824f9da`
all ON ORIGIN, and `origin/SITEZ`'s checker is **byte-identical** to the local one.

---

## Blockers

**None at this seat.** Remaining acts, none DS — named per Rule 29:

1. **[`0.0.0_AB_MSTR~Z`]** push `40f07d3deb`.
2. **[`3.0.0_SA_CVO~Z`]** certify TO-9-DS at **3 of 5**.
3. **[the 2026-08-29 ~13:00Z scheduled fire]** lifts `INGEST-TO9-AC3/AC4`, `TM1-AC1`,
   `CATV-TOV1-AC7`, `INGEST-TO10-AC3` — **one event, no seat.** No ad-hoc run beats it; the TOs
   forbid it and an ad-hoc artifact is never production evidence.

---

## Next Steps

1. **[`2.0.0_SA_COO~Z`]** The face lacks `<task_order id="ETFS_INGEST.TO-9-DS">` — the structural fix,
   after which this instance's `decomp_ref` object is unnecessary.
2. **[whoever closes D4]** ⛔ **The close must SAY 3 of 5.** A close implying 5 of 5 is the same
   falsehood class as *"STAGED, never started."*
3. **[this seat]** Nothing unblocked. Available for re-pointing.
