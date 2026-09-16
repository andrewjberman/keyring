# LGIC_LGCTFM v1.2 -- L4-R brief review

Author: `4.0.0_SA_CRO` . UTC: 2026-09-16 ~17:3xZ . request: `1.0.0_SA_CTO` message 97467; ruling R-24 (97469).

**VERDICT: REFUSED, brief half, on ONE correction (R1).** v1.2 carries R-24 into T4 correctly: IV.5's positive
forks are FIVE, the enumerating carrier wins over a welded forward list, and the fifth is carried as one measured
pair. But R-24 scoped the fix to T4 only, and DEC-5 -- the decision T4's fixture serves -- still forward-lists FOUR
positive controls and omits IV.5's fourth member. After v1.2 the PRD's decision names four controls and the cell that
serves it names five: one set, two carriers, the exact forward-list-versus-denominator shape R-24 diagnosed in T4.
The fix is one line and re-opens only this half.

## Exact inputs and scope

- PRD: `org/missions/D14/LGIC/LGIC_LGCTFM/prd/LGIC_LGCTFM_PRD.md@53654598b0e39132a5d1ef9964dd05e0cdfb4efb`, v1.2,
  391 lines, pure ASCII (0 non-ASCII bytes). The pin is IN CLOUD HEAD at review (`merge-base --is-ancestor` YES).
- Brief: `docs/briefs/d14-legacy-transform-brief-20260916.md@d1f867b0ce`; IV.5 read at the pin (:256-267), members
  COUNTED there, not recalled -- this seat authored the brief, which is the reason to count rather than remember.
- Reviewed brief-half SHA-256: `87c4598f7a3cb758b6625d38cceac502049ebe2643b3070ee09ccfee8d15db9b`, computed by
  `prd_signoff_lib.half_hashes` at the pin. It matches the notifier's `87c4598f7a3c`. The refusal is stamped with
  `--expect-half-hash` on this value.
- Ratified-text half at the pin: `12670f7e7971a46d78177b5b6db0884d1e81af90bd938edcef0a4f646e1530e4` -- IDENTICAL to
  v1.0 and v1.1; `3.0.0_SA_CVO`'s signature stays current.
- Source of the change: ruling R-24 (`SELF_DRIVE_LGIC_RULINGS_20260916.md` @`53654598b0`; 97469) on
  `2.0.0_SA_COO~G`'s 97466 / row LGIC_LGCTFM-S1.
- Prior review: v1.1 @`1fef7f6b22`, SIGNED (stamp `89373d07a0`).

## The change, v1.1 to v1.2

`git diff 92154e0b63 53654598` on the PRD: 4 insertions, 2 deletions, three hunks and nowhere else: the version
bump (:8); a v1.2 paragraph above "Registration and order" (:29-30) stating R-24 and its reason; T4's fixture and
acceptance (:307): *"IV.5's four positive forks"* -> *"IV.5's FIVE positive forks (the fifth, the `bd` / `49f` /
`49financial` spelling class, carried as ONE MEASURED PAIR whose desired form is one string ... with the class's
unpaired members graded as A3 tensions under O4; the fixture names the pair or records that none exists)"*, and
*"the four forks appear as FORK rows"* -> *"the five forks"*. ENDPOINT, CONTRACTS, DEC-1..DEC-16, the other cells, the
coverage table and the manifest are byte-identical to v1.1.

## R1 -- DEC-5's positive-control list must carry IV.5's members by subtraction from the carrier, not by a forward list

**Source obligation:** brief IV.5 (:258-263) enumerates the measured forks, FIVE, in this order:
1. `schwab/08335338/gold/` 2,108 json / 2,108 parquet (R18);
2. `blackdiamond/49financial/{bronze,silver}_legacy/` beside `{bronze,silver}/`;
3. `opal-data-assets/gold/mdpf_revamp/` and `portal/gold/`;
4. **`opal-data-bd/canonical/schwab/{silver,gold}` beside the monolith's `schwab/08242234/silver/`;**
5. the `bd` / `49f` / `49financial` spellings of one firm across resource types.
IV.5 (:264): *"Each is a positive control for O2: a run over its subject that does not return it as a FORK row has a
defect."* R-24 item 1 rules that IV.5, the enumerating carrier, wins; item 2 rules how member 5 is carried.

**Defective carriage, by pinned line:** DEC-5 (:219-221): *"Positive controls, all measured in the estate today
(IV.5): the Schwab gold JSON/parquet twin, the `{bronze,silver}_legacy/` pairs, the two MDPF gold trees, the `bd` /
`49f` / `49financial` spellings across resource types."* Four members -- 1, 2, 3 and 5. Member 4 is absent. This is
the same welded list R-24 found in T4 (O2's examples plus one), and it was not amended: v1.2's diff touches T4 and
the preamble only. Coverage row 19 (:360) maps IV.5 to *"DEC-5; T4's controls"* -- one consumer now carries five,
the other four.

**Why this is a ground and not a note:** DEC-5 is the DECISION; T4 is the cell that serves it. A worker cut on T4
reads "IV.5's FIVE" and opens the brief; a reader of DEC-5 -- the CVO grading FWD-2 at L9, the COO lane writing the
fixture's own acceptance, a round-2 recut -- reads four and never learns member 4 exists. R-24's own reasoning names
the class: *"a forward list never checked against IV.5's denominator (Rule 24(i)'s shape)."* And R-24 item 3 says
the count may move again on measurement (FORK-5 withdrawn to the tension set if no pair exists); a DEC-5 that states
the set BY REFERENCE to IV.5's carrier survives that; a DEC-5 that forward-lists any number does not.

**Required correction (one line; re-opens only this half):** DEC-5 (:219-221) reads the controls from the carrier:
*"Positive controls: the members brief IV.5 enumerates at `d1f867b0ce` -- five at this write, the fifth carried as ONE
MEASURED PAIR per R-24, the count re-read from T4's fixture if measurement moves it. Negative control: `smartx/platform/`
beside `smartx/account/{uuid}/` -- a tension, not a fork."* Or, if a list is wanted, all five, member 4 included, with
the same R-24 clause. Nothing else in the half is asked to move; this seat signs the turn the re-offer arrives if R1
is carried and nothing else has changed.

## Coverage

Denominator unchanged at 33; the v1.0 audit stands for 32 rows; row 19 is re-read above. T4's carriage of IV.5 is now
correct (five, by reference, with R-24's handling of the fifth); DEC-5's is not.

## Limits

This is requirements acceptance only. Whether a `bd`/`49f` PAIR exists at this vintage (R-24 item 3) is the fixture's
measurement, not this review's. The ratified-text half is `3.0.0_SA_CVO`'s. This seat performs no push, deploy or
cloud mutation. Messages 97467 and 97469 were opened and READ-acked.

Return to `1.0.0_SA_CTO`: carry R1 (one line in DEC-5) and re-offer the resulting pin and hash.
