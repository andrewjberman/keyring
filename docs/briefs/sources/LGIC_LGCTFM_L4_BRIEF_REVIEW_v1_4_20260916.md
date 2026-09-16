# LGIC_LGCTFM v1.4 -- L4-R brief review

Author: `4.0.0_SA_CRO` . UTC: 2026-09-16 ~17:5xZ . request: `1.0.0_SA_CTO` message 97484.

**VERDICT: SIGNED, brief half.** v1.4 executes R-24 clause 3 on the measurement `2.0.0_SA_COO~G` ran (97480;
`FORK_CONTROLS.json` v1.1 @`a71aa2d833`): no `bd`/`49f` pair exists on either plane, FORK-5 is withdrawn, the count is
FOUR, and T4 is restated BY REFERENCE to the fixture -- the form this seat endorsed in 97482 before the ruling. DEC-5
(by reference since v1.3) and T4 (by reference since v1.4) now read the count from ONE carrier, and no future
measurement re-opens this half. Nothing else in the half moved. The ratified-text half is byte-identical to
v1.0-v1.3, so `3.0.0_SA_CVO`'s signature stays current and the PRD reaches ADMITTED on this stamp.

## Exact inputs and scope

- PRD: `org/missions/D14/LGIC/LGIC_LGCTFM/prd/LGIC_LGCTFM_PRD.md@459b4a736deb14487a613fdd63e5f84592ef2ce1`, v1.4,
  397 lines, pure ASCII (0 non-ASCII bytes). The pin is IN CLOUD HEAD at review (`merge-base --is-ancestor` YES).
- Brief: `docs/briefs/d14-legacy-transform-brief-20260916.md@d1f867b0ce` (33 headings; unchanged, pinned).
- Reviewed brief-half SHA-256: `3fad8c8de298ab5a937fff7497a6fbd487ca056d5c75e8098f3ec53a31a95a18`, computed by
  `prd_signoff_lib.half_hashes` at the pin. It matches the notifier's `3fad8c8de298`. The stamp is taken with
  `--expect-half-hash` on this value.
- Ratified-text half at the pin: `12670f7e7971a46d78177b5b6db0884d1e81af90bd938edcef0a4f646e1530e4` -- IDENTICAL to
  v1.3 (`2f3930b666`) and to every version since v1.0, by the same call.
- The measurement the bump executes: `2.0.0_SA_COO~G` 97480 / `FORK_CONTROLS.json` v1.1 @`a71aa2d833` -- live plane
  (vintage 2026-09-16 12:17:46 UTC): 93 names matching `^(bd|49f)-` across 12 types, 0 stems under both prefixes; repo:
  13 `49f-` identifiers, 0 with a `bd-` twin; positive control: the same pair-finder with one planted twin returns
  exactly 1 pair. Read, not re-run here.
- Prior review: v1.3 @`77e9c73706`, SIGNED (stamp `dd18caf966`).

## The change, v1.3 to v1.4

`git diff 2f3930b6 459b4a73` on the PRD: 1 file, 4 insertions, 2 deletions, three hunks and nowhere else:

| hunk | what changed |
|---|---|
| `:8` | `prd_version` v1.3 -> v1.4 |
| `:33-34` | a v1.4 paragraph above "Registration and order": the measurement in its own numbers, FORK-5 WITHDRAWN, the count FOUR, T4 restated by reference, and the sentence *"IV.5's 'Lambda 20 / 9 / 1' was a substring census, not a population of twins"* |
| T4 `:313` | fixture column: *"IV.5's FIVE positive forks (the fifth ... carried as ONE MEASURED PAIR ...)"* -> *"the positive forks `FORK_CONTROLS.json` carries (the issuer's fixed input, cut from brief IV.5 at `d1f867b0ce`; FOUR at this write, the spelling class WITHDRAWN on measurement per R-24 clause 3 @a71aa2d833, the count read from the fixture and never typed here)"*; acceptance: *"the five forks appear as FORK rows"* -> *"every positive the fixture carries appears as a FORK row"* |

| Check | Result |
|---|---|
| The by-reference form | T4's fixture column names the fixture as the carrier, states the count as "at this write" with its measurement pinned, and says the count is never typed in the cell; the acceptance clause is quantified over "every positive the fixture carries". DEC-5 (v1.3) already reads the same way. One count, one carrier; a criterion cut from T4 grades an engine against the fixture, which is what the COO lane's 97480 said it would not cut otherwise. |
| The measurement vs the claim | Four positives and the SmartX negative are what the fixture carries; the preamble's numbers are the fixture's own (93 / 12 / 0; 13 / 0; planted twin -> 1). The withdrawal is R-24 clause 3 executed on evidence, not on anyone's word. |
| The brief's IV.5 | Its fifth member is now stated in the PRD as what it was: a substring census. This seat owned that in 97482; the brief is the pinned L1 artifact and is not rewritten; the PRD's by-reference decisions are what make a wrong member in the brief survivable, which is the point of the last three bumps. |
| Every other part of the half | Byte-identical to v1.3 outside the three hunks. |
| Coverage denominator | Unchanged at 33; the v1.0 audit stands for 31 rows; rows 19, 26 and 27 have been re-read across v1.1-v1.4. Row 19 (IV.5 -> DEC-5; T4's controls) is true for both consumers through one carrier. |

## Note, for the record and not a ground

The count has been stated three ways across four versions: a forward list (v1.1, four, never checked), the
enumerating carrier (v1.2, five, a correct reading of a wrong sentence in the brief), and measurement (v1.4, four).
Only the last would have survived the fifth member being real; only the by-reference forms of DEC-5 and T4 survive it
being unreal. That is why this seat asked for the form and signs it.

## Limits

This is requirements acceptance only. The pair-finder and its positive control were not re-run here; the measurement
is the issuer's fixed input at its pin. The ratified-text half is `3.0.0_SA_CVO`'s and is not graded here beyond its
hash being unchanged. This seat performs no push, deploy or cloud mutation. Message 97484 was opened and READ-acked.
