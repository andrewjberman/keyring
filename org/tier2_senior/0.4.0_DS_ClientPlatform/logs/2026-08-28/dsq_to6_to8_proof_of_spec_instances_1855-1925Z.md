# Filing two instances over evidence I did not produce -- and the defect I was briefed to expect had been fixed eight minutes before I measured it -- `0.4.0_DS_ClientPlatform~Q`

**Date:** 2026-08-28
**Task Order:** `ETFS_INGEST.TO-6` and `ETFS_INGEST.TO-8` -- proof-of-spec instances
**Status:** COMPLETE
**Window:** 2026-08-28 ~18:55Z - ~19:25Z
**Archetype:** FILING (Rule 27 step 4 -- execute ON SPEC; a records act, not a build)
**Commits:** `c519eb7964` -- **LOCAL** (is-ancestor of `origin/SITEZ` says NO; positive control `a951b1bd21` says YES; negative control all-zero sha says NO). `origin/SITEZ = a951b1bd21`.
**Predecessor:** this lane's prior session died with the build done and the instances unfiled. Re-seated 18:55:34Z by `2.0.0_SA_COO~Z` (msg 13720).

---

## Objective

File `ETFS_INGEST.TO-6_PROOF_OF_SPEC.json` and `ETFS_INGEST.TO-8_PROOF_OF_SPEC.json` from SERVED
evidence. ⛔ **Explicitly NOT a build.** The brief is unambiguous: the build is on origin, deployed
02:26:49Z, exercised by the 13:01:26Z scheduled fire, and *"a re-execute of accepted work is a
REWIND"* (CLAUDE.md NEVER-2). The predecessor withheld both instances DELIBERATELY and correctly --
`TO-6 AC3` and `TO-8 AC2/AC5` were gated on a scheduled fire that had not yet happened, and filing
`FAIL` for a gated criterion writes a false failure into a record already holding 18 such rows.
**That gate is now discharged. The withholding was right then; filing is right now.**

---

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| `proof-of-spec-check.py` | positional, rc without a pipe, 4 invocations | **PASS rc=0 VALID both, violations=0** | **and the first two invocations were MY error -- see section 4** |
| `aws s3api` (via `.tools/aws`) | head/get/list-objects-v2/list-object-versions | PASS | `s3api` not `s3 ls`: UTC vs LOCAL, and every timestamp here is scored against a cron boundary |
| `git merge-base --is-ancestor` | 7 push-state reads | PASS | positive control (pushed sibling) + negative control (all-zero sha) on every read |
| `comp-system` | regenerate `06_current_state` | PASS rc=0 | the gate's FIRST-CHOICE fix; **no override was needed and none was used** |
| `safe-commit.sh` | `-F` msgfile written by the Write tool | PASS rc=0 `c519eb7964` | msg-verify MATCH len=6599; risk-reflex CLEAN over 4 files vs 1,417 danger nodes |
| `python` + pandas/pyarrow | censuses over 5 artifacts | PASS | every count printed beside its denominator; a negative control in each census |

**What worked:** **S3 object versioning.** It turned `TO8-AC4` from a recollection into a diff without
needing anyone's local pre-fire capture -- and it is the reason I could state, honestly, what my
instrument does *not* buy.
**What failed:** two of my own invocations (section 4). Both failed LOUDLY.
**Gap found:** none new. `firm` has no `ETFS` value for the fifth instance running.

---

## Work Completed

### 1. Startup, and one thing the doctrine got right

`/watcher`: no `inbox-watch.sh` process existed for this serial, registration read OFFLINE at PID
29740 against my own PID -- so the discriminator that matters (*whose* PID, not "is anything live")
said **genuine predecessor death**, not a live peer and not a context-clear. Armed cleanly,
`parent-tied: pid 491116` (protected, not orphan-capable). The Monitor then delivered the two
messages I had already read -- **a consumer-side confirmation, which is the only sound delivery
oracle**; I did not infer reachability from `ps` or from a drained inbox.

`org/XXX.md`: Step 1b-F row 613, `Tier-2/3 workers (+ ~lanes)` -- `/watcher` once, **zero crons**.
Nothing armed.

### 2. The three rungs, re-derived rather than relayed

`TO8-AC2` says the denominator *"must be re-derived, not copied"*, and CLAUDE.md says a second seat
confirming via the FIRST seat's method is **repetition, not corroboration**. So I measured all three
rungs at this seat rather than citing `2.0.0_SA_COO~Z`'s figures:

```
RUNG 1  bbg/2026-08-27/characteristics.csv   172 x 14, field present, 165 non-null, neg control absent
RUNG 2  gold/holding/date=2026-08-27         189 x 31, industry_group + basis present, neg control absent
RUNG 3  platinum/etfs/positioning_data.json  KEY PRESENT 189/189, non-null 180, null 9
```

The **189 / 4 portfolios** was re-derived by walking the document (DIVZ 30 + IDVZ 45 + PFDE 90 +
PFOE 24), not assumed from the TO. Gold and served carry **identical** basis distributions
(observed 180 / not-applicable-non-equity 8 / absent-from-source 1), so the publisher passes the
field through rather than re-deriving it -- two expressions that could drift are in fact one.
Scored as **KEY PRESENCE**, never `.get()`: the two are indistinguishable on a null value, and the
difference between an absent key and a null value is this TO's entire subject.

`TO8-AC4` against the **S3 noncurrent version** (`WeQkbjug...`, 128122 B, 08-27T13:01:25Z):
189/189 `sub_asset_class` identical, 0 added, 0 dropped, all 12 values matching count-for-count,
served row key set **13 -> 15** adding exactly the two intended keys and removing none.

> ⚠ **WHAT THAT INSTRUMENT DOES AND DOES NOT BUY, STATED IN THE INSTANCE RATHER THAN CLAIMED AS
> TRIANGULATION.** It is a **different retrieval path over the SAME OBJECT** `2.0.0_SA_COO~Z`
> captured locally. It corroborates the **capture**; it does **not** corroborate the **choice of
> baseline**. One rung measured twice is not two rungs, and writing it up as independent
> confirmation would have been the exact error this estate has banked.

### 3. ⛔ THE BRIEFED DEFECT WAS ALREADY FIXED, AND THE RECORD I FILED SAYS SO

`2.0.0_SA_COO~Z` msg 13731 (19:08:54Z) told me every `ETFS_INGEST` instance would read **INVALID**
on alignment, instructed executors to file anyway and state it as the known upstream cause, and
routed a **rename-29-cells vs widen-the-regex** adjudication to `1.0.0_SA_CTO~Z` as a D4 close-out
blocker. I filed anyway, as instructed. **Then the instrument disagreed:** both instances read
`rc=0 VALID`, violations=0, alignment fully closed (forward-1 6/6, forward-2 2/2, backward 2/2,
40-id decomp space).

**CAUSE:** `1.0.0_SA_CTO~Z` landed `87c5761e9e` at **19:16:16Z -- eight minutes after the brief was
written, while I was measuring.** It takes the widen option NARROWLY (prefix-anchored, etfs-ingest
TIER form) and records the shape-general alternative as *built and rejected by its own control*:
572 NEW-ONLY tokens vs 36, the 36 all real INGEST ids.

⛔ **I HAD ALREADY WRITTEN THE FALSE VERSION INTO BOTH INSTANCES** -- a `surprises[0]` asserting they
would read INVALID, drafted from the brief before I ran the checker. **Corrected in both before
commit.** Committing the briefed expectation as if it were a measurement would have put a falsehood
into the durable record and, worse, would have looked perfectly well-sourced.

> **VINTAGE QUALIFIER, AND IT IS LOAD-BEARING:** `87c5761e9e` is **LOCAL, not on origin**. So VALID
> is true at local HEAD and **will not reproduce** against `origin/SITEZ` or on the other fabric
> until the integrator pushes. A seat that re-runs this and gets INVALID has found an unpushed
> checker, not a bad instance. Both instances carry that sentence.

Reaching VALID cost no compliance theatre: **no cell renamed, no `cell_ref` retrofitted** -- the
alignment fields are byte-identical to what I would have filed expecting INVALID.

### 4. Two instrument errors of mine, both of which failed safe

- **I passed the TO FACE as `argv[2]`.** `coverage_check():149-151` reads `argv[2]` as a criterion-id
  **LIST** (one per line, or comma-separated). Handing it the markdown made all **479 lines**
  "expected criteria" -> 486 violations **my own call manufactured**. The correct argument is the
  face's `<expected_criteria>`.
  ⛔ **AND THE ALIGNMENT FIGURES WERE IDENTICAL ACROSS BOTH RUNS** -- that layer resolves the
  governing TO from `decomp_ref.to_ref` *inside the instance*, not from argv. **A wrong `argv[2]`
  leaves exactly the numbers a reader is most tempted to quote looking perfect.**
- **An unbraced `$n_PROOF_OF_SPEC`** resolved as one undefined variable; `rc=2 READ-ERROR`. It failed
  loudly rather than validating the wrong file, which is the only reason it cost seconds.

### 5. A hypothesis of mine, raised and killed by measurement rather than filed

`HOLDING_KEYS` reads **14 members without `industry_group_basis`** at `@39495cf260`, which looked
exactly like `TO8-AC6`'s provenance field being served but **uncovered** by the publisher's
completeness assertion -- the very hazard AC6 quotes from CLAUDE.md. **FALSE.** `f0e2a05889` already
carries the 15-member list and **precedes the 02:26:49Z apply by 12 minutes**, so the 14-member
state lived 39 minutes in the tree and **never shipped**. Recorded in the instances as a retired
hypothesis, not filed as a finding.

---

## Decisions Made

| Decision | Basis |
|---|---|
| File both instances with **all 12 rows PASS** | Every criterion measured on a landed artifact or committed bytes; nothing scored on a producer self-report |
| Use TO-8's **bare `TO8-ACn`** ids, not firm-tokened | Matches `<expected_criteria>` verbatim. The id defect is recorded ON THE FACE as deliberately deferred pending a citation census; "correcting" it inside my own instance would break the comparison AND create the two-carrier divergence the deferral exists to avoid |
| Score `TO8-AC4` **PASS** despite its premise naming 2 non-equity values when 1 exists | The values that exist are all identical pre/post-fire. Failing on a premise mismatch would blame the build for a face defect; smoothing it over would hide it. Scored PASS **and** surfaced |
| **No override** on the comp-system gate | Its first-choice fix (`comp-system` regen) worked, rc=0. The `STRUCTURAL-TWOPHASE` prefix is reserved for the rule-bank population and using it here would corrupt the instrument that tells the two populations apart |
| Did **not** push | Integration window: push is the integrator's (`0.0.0_AB_MSTR~Z`) |

---

## Files Modified

| file | change |
|---|---|
| `org/.../deliverables/ETFS_INGEST.TO-6_PROOF_OF_SPEC.json` | +240 new -- 6 rows, all PASS |
| `org/.../deliverables/ETFS_INGEST.TO-8_PROOF_OF_SPEC.json` | +215 new -- 6 rows, all PASS |
| `infra/system/06_current_state.{json,md}` | regenerated by `comp-system` as the gate's prescribed fix |

**Not touched:** every production file (this was a filing act) - `portal/` - `TO-9-DS` (Andrew
stopped the traffic 18:24Z) - `TO-10-AE` (`0.7.0_AE_CloudOps~I`'s, live) - the decomp, its cell
ids, and its certificate. **No rebuild, no ad-hoc gold run, no deploy, no gate edit, no cron.**

---

## Briefs Written

None. The RAVC close is msg 13774 / 13775 (`2.0.0_SA_COO~Z` + `1.0.0_SA_CTO~Z`,
**2 DELIVERED / 0 QUEUED / 0 REFUSED**, denominator 2).

---

## Current State

```
TO-6   AC1 PASS   AC2 PASS   AC3 PASS   AC4 PASS   AC5 PASS   AC6 PASS     rc=0 VALID
TO-8   AC1 PASS   AC2 PASS   AC3 PASS   AC4 PASS   AC5 PASS   AC6 PASS     rc=0 VALID
```

Both at their declared `instance_path`. Committed `c519eb7964`, **LOCAL** (measured, controlled).
The 7-sibling absence that re-seated this lane is closed: **9 of 9 ETFS_INGEST instances now exist.**

**Four items surfaced to `2.0.0_SA_COO~Z` as issuer, none chased:** (a) `TO8-AC4`'s "2 non-equity
values" vs the served 1; (b) the synthesized residual is not separately identifiable on the served
plane; (c) TO-6's A5 premise oracle still returns a clean zero in the direction that stops work;
(d) `firm=FABRIC` declared for the fifth instance running -- a workaround repeated five times is
evidence the gate should move.

---

## Blockers

**None at this seat.** Two acts remain and neither is DS -- named per Rule 29, which permits ending
on a report only when the next act is out-of-lane:

1. **[`0.0.0_AB_MSTR~Z`]** the push. `c519eb7964` and `87c5761e9e` are both LOCAL, and the second is
   what makes the first validate -- **a seat validating against `origin/SITEZ` today still gets
   INVALID.** The two travel together.
2. **[`3.0.0_SA_CVO~Z`]** certification, now that instances exist to validate. Its prior cert was
   PARTIAL (3 certified, 9 NOTHING-FILED) precisely because these two were absent.

---

## Next Steps

1. **[`2.0.0_SA_COO~Z`]** Read msg 13774 s.2 before acting on 13731 -- the adjudication it routed is
   **already discharged** and the 29-cell rename is not needed.
2. **[`1.0.0_SA_CTO~Z`]** The `firm` enum has no `ETFS` value, five instances deep.
3. **[this seat]** Available for re-pointing. No unblocked `ETFS_INGEST` act remains.
