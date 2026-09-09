# CTO ADJUDICATION -- NFRA_OUTSET round 3, S23: drift is a property of a DEVICE, and a scheduled clean host cannot report it

**Seat:** `1.0.0_SA_CTO` · **Stamp:** 2026-09-09 ~15:2xZ · **On:** `2.0.0_SA_COO` 94512 (drive tick 10.5), substrate
`0.7.0_AE_CloudOps~W`'s BLOCKING row S23 @`76131249a0` and the issuer's interim L6 amendment @`c82df8ce20` · **Prior in this chain:**
@`e18317d0e0` (S16/S17 placed), @`d6fd9eca07` (round-2 L10: *a seam is two ends and a clock*), Andrew's GO @`e1b44ba4cc`.
**Timing:** mid-round the PRD is FROZEN; this ruling states the PROPERTY, the issuer re-cuts the face under the standing test
(@`9f4a57262f` + @`1ced87e810`), and the PRD row is corrected at round 3's L10 with one new row placed here -- the S16/S17 shape.

---

```
+-- CALL 1 of 1 -- S23 --------------------------------------------------+
  **`comp-heat drift`'s only measurement is the producing machine's dirty
  working tree (`git status --porcelain`, cmd_drift :502-578,
  object_freshness.py:259-268). A freshly cloned automated host is EMPTY BY
  CONSTRUCTION, so an off-host schedule publishes n=0 every day with
  answer_state OK, a correct denominator and a vintage minutes old -- and
  OS-s-21's accept as the PRD writes it ("vintage precedes the run; FRESH
  with age < 26 h") PASSES on that zero. (a) device-side drift with the
  artifact carrying its device, the PRD stating the non-application of an
  off-host schedule for drift; (b) change which producer feeds group A;
  (c) accept the scheduled n=0 and say so?**
  --------------------------------------------------------------------
  **REC --** (a), with two sharpenings: the artifact carries its producing
  device and its tree's own denominators (n, n_modified, n_untracked, the
  tracked-file count as the positive control); the publish runs on the
  DEVICE'S own timer and the PRD row states the non-application of an
  off-host schedule for drift. (b) re-opens what group A means, above the
  round. (c) refused: it writes the confident zero into the spec.
  --------------------------------------------------------------------
  **RULING -- (a) ADOPTED, both sharpenings adopted, and two more.**
+---------------------------------------------------------------------+
```

## WHY (a), on the architecture and not on convenience

Group A is the PROPAGATION stratum: what has moved from a working tree to git to the served plane. Its first hop -- the dirty
tree -- exists only on a machine where people work, so drift is a property of a DEVICE, not of the estate. An automated host
asking "what is uncommitted here?" is asking a machine that has nothing to be uncommitted, and its true answer is n=0 with a
tracked-file count of zero-work: OUT-OF-CORPUS, not absence (CLAUDE.md Rule 21's own line). The assignee measured the contrast
that decides it: this device's hand publish carried n=154 (6 modified, 148 untracked); a clean clone yields 0. **The producer's
question survives a clone only for `freshness` (git commit timestamps are identical on every clone; the mtime reads cover
untracked files only) -- so freshness is schedulable off-host and drift is device-bound.** That asymmetry is the ruling's
whole substance, and it is the fourth confident-zero instance on this project (W2-S21, S14, S21, S23): a detector that cannot
return non-zero on the positive case is a constant wearing a measurement's clothes.

(b) would change the QUESTION group A answers; that is a PRD s.3 decision on the seam's meaning, above this round, and nothing
measured says the question is wrong -- only that one producer was asked it from the wrong machine. (c) would put the
structural zero into the spec as the intended meaning, which is the exact defect Rule 22's DISCRIMINATION axis exists to
refuse: an accept the false case satisfies.

## THE FOUR SHARPENINGS

1. **The artifact carries its device and its denominators** (the issuer's first): `device` (the fabric key, `laptop` | `site-z`,
   never a hostname invented per run), `tree_root`, `git_head` (the tree's HEAD at the read), `n`, `n_modified`, `n_untracked`,
   `tracked_total` as the positive control, and its vintage. A consumer can then tell *"device X reported a clean tree at T"* from
   *"no device has reported in 26 h"*; without the device field the ceiling conflates a quiet estate with a dead publisher.
2. **The device's OWN timer, and the PRD row's stated non-application** (the issuer's second): the publish is a scheduled task ON
   the device (the producer's own trigger, so the schedule rule stands), and OS-s-21's row states plainly that an off-host
   schedule does not apply to drift -- *four rows or a stated non-application each*, applied to the clock.
3. **ONE KEY PER DEVICE, and a consumer that composes them -- placed as a new row.** Today `estate_report_runner.py:1844` reads
   ONE key, `outset/comp_heat_drift.json`. Two devices writing one key is last-writer-wins: a confident partial. So the drift
   artifact is keyed `outset/<device>/comp_heat_drift.json`, and the CONSUMER's per-device composition is its own surface:
   **OS-s-22 (placed here for round 3's L10 addendum v0.5; lane CloudOps by the runner's deploy, code in
   `estate_report_runner.py`): group A renders each device's drift with that device's vintage and its own 26 h ceiling, reads QUIET
   (a device reported a clean tree, n=0 with tracked_total > 0) and SILENT (no report inside the ceiling -> INSTRUMENT_FAILED for
   that device) as DIFFERENT states, and never sums devices into one n.** Until OS-s-22 lands, the single key carries ONE device's
   artifact with its device field -- honest for the one device doing this project's work today, and the consumer reads it as
   that device's, not the estate's. The seam key roster (OS-s-13's composition contract) admits the device segment; the R2 probe
   key and the freshness key are untouched.
4. **The accept for the drift half reads EXERCISED on a served day with a control that can fail:** the served group A names the
   device and an n that equals that device's `git status --porcelain` row count at the artifact's `git_head` (the control, read
   at the CVO from the device, not from the artifact); the negative arms stand as the issuer's interim amendment wrote them -- a
   clean-clone artifact is INADMISSIBLE whatever its vintage, and a device that did not publish inside its ceiling reads
   INSTRUMENT_FAILED, never FRESH. **A raised ceiling or a hand publish cannot buy the green.**

## WHERE IT LANDS, AND WHEN

- **Now, the issuer's, under the standing test:** OS-s-21's face is re-cut so its DRIFT half reads the property above (device-side,
  the device's own timer, the artifact's device field and denominators, one key per device) and its FRESHNESS half proceeds
  off-host as already building; the re-cut is judged on EFFECT and told to the CVO, not asked. The face's bound keeps the R2
  probe untouched and the freshness key unchanged.
- **At round 3's L10 (this seat's), PRD v0.5:** OS-s-21's row re-worded to the property with the stated non-application, and
  **OS-s-22** added as above. `endpoint_outcomes` unchanged; FWD-3 is what both serve.
- **Bound on every row of this seam, stated once:** a producer that answers "how much of X" prints the POPULATION it could see
  beside its count and a positive control; a zero over an empty population is OUT-OF-CORPUS and the consumer renders it so.

## WHAT THIS RULING DOES NOT DO

Change group A's question (b) · admit a scheduled clean-clone zero (c) · touch OS-s-20 (landed under Andrew's GO; its accept
pending the 2026-09-10 served day against the pinned baseline) · build a device timer, a key layout or a consumer change now
(Andrew's "no new work until the transcript" holds; the rows are PLACED and the loop cuts them) · grade O21-AC2 (the CVO's at L9).

## Push state
LOCAL on commit; origin/CLOUD @`58adeff90c` by this seat's ls-remote at 15:18Z; LD-0522 hold standing.
