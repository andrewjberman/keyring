# CTO ADJUDICATION -- NFRA_OUTSET round 3, S26: the seam roster is a declared domain, and its fix is placed at L10, not cut mid-round

**Seat:** `1.0.0_SA_CTO` · **Stamp:** 2026-09-09 ~16:4xZ · **On:** `2.0.0_SA_COO` 94576 (drive tick 13.5), row `NFRA_OUTSET-S26`
@`31363a4fdd` (`0.7.0_AE_CloudOps~W`, OBSERVATION, ARMED for the NEXT producer) · **Prior:** W2-S21 (round 1: the consumer's extractor
dropped 35,752 nested rows through a hand-enumerated key roster), S24/OS-s-23 @`5f39f3a512` (the publisher carries the row-count control),
S25 @`054353ac5e` (a version per call is the wrong cadence).

---

```
+-- CALL 1 of 1 -- S26 --------------------------------------------------+
  **outset_seam.run_and_build finds a producer's rows by a hand-enumerated
  top-level key list (paths | rows | uncommitted). comp-fedobs nests its
  payload at signals.coevolution.rows (38,872 rows); a naive build would have
  published rows: [] with answer_state OK and a real-looking denominator.
  ~W did not use it (seam_groupb_publish.py lifts the nested rows and refuses
  unless its count equals the producer's declared row_count, 38,872 == 38,872).
  The module is lane NFRA_HEATMAP; no CloudOps member can touch it. Where
  does the fix go?**
  --------------------------------------------------------------------
  **REC --** carry S26 to round 3's L10 as a PLACED CELL for lane
  NFRA_HEATMAP, not a mid-round cut: the spec is frozen, no order is blocked
  (OS-s-23 carries the control), the honest interim stands. Content: (c) the
  FLOOR -- cross-check any declared row_count / n against len(rows), refuse on
  disagreement; (a) the FIX -- an explicit rows selector from the caller,
  refuse when none is given and no rostered key hits. Negative arm:
  comp-fedobs's real JSON through the unpatched roster must REFUSE, not
  return an empty list.
  --------------------------------------------------------------------
  **RULING -- ADOPTED as stated: placed at round 3's L10, lane NFRA_HEATMAP,
  (c) as the floor and (a) as the fix, with one sharpening on what the fix
  must NOT be.**
+---------------------------------------------------------------------+
```

## WHY L10 AND NOT NOW

The S24 precedent (a mid-round addendum) was for a surface whose absence changed what tomorrow's served report says; this one changes
nothing served today: the only producer that hit the defect routed around it with a control that can fail, and the next producer
does not exist yet. The spec and decomposition stay frozen; a row already records the hazard; the placement is the L10's. A version
per call is the wrong cadence (S25), and this is the case that shows why.

## THE SHARPENING -- the roster is a DECLARED DOMAIN, and the fix must not be a longer roster

`paths | rows | uncommitted` is a pattern list, and a pattern list is a declared domain whose uncovered member must be hunted, not
appended to (Rule 22; Rule 24 postulate i). Adding `signals.coevolution.rows` as a fourth entry would fix comp-fedobs and re-arm the
row for the fifth producer. So the cell's accept reads: **(a) the selector is the CALLER's -- the producer's own contract names where
its rows live, and `run_and_build` REFUSES when no selector is given and no rostered key hits; (c) any scalar the producer declares
as its row count is cross-checked against `len(rows)` and disagreement REFUSES; the roster itself is not extended.** Two negative arms:
comp-fedobs's real JSON through the unpatched module must refuse (never `[]`), and a payload whose declared count disagrees with its
rows by one must refuse. OUT-OF-CORPUS stays printed for a genuinely empty population; a zero over an absent population is never OK.

## WHERE IT LANDS

Round 3's L10 addendum (this seat's): one row, lane `NFRA_HEATMAP` (`org/modules/heatmap/outset_seam.py`), verb fix, depends_on
OS-s-23 (the publisher whose control it generalises), with the accept above. The L6 cut seats a member of that lane; if the registry
names none, that is the cut's finding and the row travels with it. S26 stays ARMED on the record until the cell's negative arm is
exercised; `seam_groupb_publish.py`'s explicit lift and count check are the interim and are not weakened.

## WHAT THIS RULING DOES NOT DO

Bump the PRD now · cut a cell · touch OS-s-23's publisher or its control · widen any grant · reach the consumer's extractor (W2-S21's
fix in the runner stands as landed).

## Push state
LOCAL on commit; origin/CLOUD @`58adeff90c` by this seat's ls-remote at 16:36Z; the push window is MSTR's on Andrew's 16:2xZ word.
