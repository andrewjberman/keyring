# LGIC_LGCTFM v1.0 -- L4-R brief review

Author: `4.0.0_SA_CRO` . UTC: 2026-09-16 ~14:2xZ . request: `1.0.0_SA_CTO` message 97416.

**VERDICT: REFUSED, brief half, on ONE correction (R1).** The coverage denominator is exact (33 of 33), every entry has
a disposition, the ENDPOINT block is byte-identical to the block Andrew confirmed, and thirty-two entries carry their
content. One entry carries a contradiction the PRD created between its own decisions: DEC-1 makes the absorbed Rule 24
record the authority for every schema enum, and DEC-6 and DEC-4 then use enum tokens that record's census explicitly
did NOT mint. A worker reading DEC-1 and a worker reading DEC-6 would author two different enums for one field -- the
two-carrier defect this project exists to remove, inside its own PRD. The fix is word-level and re-opens only this half.

## Exact inputs and scope

- PRD: `org/missions/D14/LGIC/LGIC_LGCTFM/prd/LGIC_LGCTFM_PRD.md@e996f463bbbe636316f915b29115fdc0934b8b4f`, v1.0,
  385 lines, 43,073 bytes, pure ASCII (0 non-ASCII bytes). The pin is IN CLOUD HEAD at review (`merge-base
  --is-ancestor` YES; HEAD `2ceee2821f`). Read whole with `git show` at the pin; positive control: a wrong path at the
  same pin printed `fatal: path ... does not exist`.
- Brief: `docs/briefs/d14-legacy-transform-brief-20260916.md@d1f867b0ce`, 522 lines, this seat's own. Heading
  denominator MEASURED at the pin: 33 = 8 top-level (title + Parts I-VII) + O1-O9 + IV.1-IV.15 + `## REFS TO CARRY`. (A
  raw `#`-prefix count prints 34 because brief :395 is a prose line beginning `#1a`; it is not a heading.)
- Reviewed brief-half SHA-256: `04b3c4c1821017ca937cb19ad7db671cdcd84a53106825f99ef8b03a0a2a120a`, computed by
  `prd_signoff_lib.half_hashes` at the pin. It matches the notifier's `04b3c4c18210`. The refusal is stamped with
  `--expect-half-hash` on this value.
- Ratified-text half, identified and not graded here: `12670f7e7971a46d78177b5b6db0884d1e81af90bd938edcef0a4f646e1530e4`
  (`3.0.0_SA_CVO`'s). ONE FACT about it stated because it is measurable and not a judgment: the ENDPOINT section's fenced
  block (87 lines) is BYTE-IDENTICAL to the block in `LGIC_LGCTFM_ENDPOINT_FORWARD_20260916.md` that Andrew confirmed
  as cut at ~13:5xZ (`difflib.unified_diff`, 0 lines). The CVO grades that half; this line only says the paste is exact.
- The absorbed prior art: `infra/logic/11_LGCTFM_CONTRACT_SCHEMA_RECORD.md@a71a2406be` (this seat's, OPTION 1),
  which DEC-1 names as the enum authority. Its section 4 fixes the tension `kind` enum and defines FORK as a ROW kind;
  its section 6 is the token census.
- Consumed for the audit: `org/standards/NAMING_SCHEMA.json` v1.10 (the 33-type partition), the endpoint document,
  `SELF_DRIVE_LGIC_RULINGS_20260916.md` R-16/R-17 as the PRD cites them.
- Prior review: none (v1.0).

## R1 -- Align DEC-6's tension-kind enum and DEC-4's RAISE vocabulary to the record DEC-1 absorbs

**Source obligation:** brief Part V.1 (:403-407): *"The contract schema arrives with its Rule 24 record ... and the
word-boundary token census of its enum values."* The record landed at `a71a2406be`; its census (section 6) decided,
per token: `fork` MINTED as a ROW kind (`RESOURCE | PLANE | FORK`, section 1.2), disambiguated from ISCK's lineage
fork; `orphan` NOT MINTED (it is ISCK's link-missing state and `/canonical-flow`'s ORPHAN-WORKTREE; an undeclared
resource is comp-find's `LIVE-no-DECLARED`); `unresolved` NOT MINTED (ISCK's no-trusted-root state; a missing registry
row is the schema's own `RAISE`). Its section 4 fixes the tension `kind` enum: `HOME | FORMAT | GRAMMAR | COMPUTE |
DECLARATION | PROCESS | IDENTITY` -- what MOVES to close the tension -- with axis and deciding rules as the other two
intents.

**The PRD adopts that authority, correctly:** DEC-1 (:182-193) -- *"T1 authors the JSON schema FROM it and cites it,
and a schema enum the record does not name is a Rule 24 act of its own, not a T1 liberty."*

**Defective carriage, by pinned line:**
- DEC-6 (:219-221): *"Type = (axis A1-A5 plus process and identity) x (the R-ids ...) x (kind: departure / fork /
  orphan / undeclared)."* Three of the four tokens are not the record's: `orphan` was rejected by the census; `fork` is
  a ROW kind (DEC-5 already treats a FORK as its own row), so naming it a TENSION kind mixes two grains the record's
  postulate (ii) separates; `departure` and `undeclared` name no value the record carries (an undeclared resource is
  `current.drift_class = LIVE-no-DECLARED`, a measured cell, not a tension kind).
- DEC-4 (:210): *"it is UNRESOLVED, never graded OUT-OF-PATTERN on a placeholder."* The record's `desired.verdict` set
  is the schema's own `CONFORMANT | ALIAS | OUT-OF-PATTERN | RAISE | NOT_GRADED | NOT_COVERED`; a missing registry row is
  a `RAISE` row with `missing_registry_row` populated. `UNRESOLVED` is not in the set and the census rejected it.
- Coverage row 26 (:361) cites *"DEC-6 (the closed type set)"* and row 27 (:362) cites *"DEC-4 (UNRESOLVED, never
  guessed)"* -- so the table carries both tokens forward as if they were the closed set.

**Why this is a brief-half defect and not a style note:** T1 (the schema, from DEC-1) and T5 (tensions, from DEC-6)
are separate cells in the same round. Cut as written, T1 mints seven kinds and no `orphan`; T5's worker face reads
four kinds including `orphan`. That is one field with two carriers -- the defect class Andrew named LGIC to end
(*"one structure ... so that every resource in a forked path has the same structure"*), and CLAUDE.md Rule 24 forbids
an enum without a census. The brief's own IV.12 (:354-365) is where the stale wording came from (*"a closed set over
(axis x rule x fork/orphan/undeclared)"*); Part V.1 made the record the place that sentence was to be settled, and it
was. The PRD should carry the settled form, not the pre-census draft.

**Required correction (word-level; re-opens only this half):**
1. DEC-6: replace the parenthetical kind list with the record's: *kind (what moves to close it): HOME | FORMAT |
   GRAMMAR | COMPUTE | DECLARATION | PROCESS | IDENTITY -- `11_LGCTFM_CONTRACT_SCHEMA_RECORD.md` section 4.* Keep the
   axis, the deciding-rules citation rule and the four measured factors exactly as written. State in one clause that a
   FORK is a ROW (DEC-5), never a tension kind, and that an undeclared resource is `current.drift_class =
   LIVE-no-DECLARED` on its row.
2. DEC-4: replace *"it is UNRESOLVED"* with *"it is a RAISE row (`desired.verdict = RAISE`, `missing_registry_row`
   populated)"*; the rest of the sentence stands.
3. Coverage rows 26 and 27: update the two cited phrases to match.
4. Optional, for the record's sake: coverage row 26 may cite the record's section 4 beside DEC-6, since that is where
   the closed set now lives.

Nothing else in the half is asked to move. Re-offer the resulting pin and hash; this seat signs the turn it arrives if
R1 is carried and nothing else has changed.

## Coverage audit -- 33 entries, content inspected

| # | entry | content checked in the consuming cells | result |
|---|---|---|---|
| 1 | title / preamble | both commission messages verbatim (:41-46); the boxed "moves nothing" line as DEC-13; Rule 30 as DEC-4; the ~13:5xZ word verbatim with this seat's narrow read adopted (:21-27) | Carried |
| 2 | PART I heading | structural | Structural |
| 3 | O1 | DEC-1 (UNMEASURED never missing), DEC-3 (the walk order, both APIs, instrument + denominator per step), DEC-14 (blind spot on every row) | Carried |
| 4 | O2 | DEC-5: fork from the desired twin never name patterns; canonical member rule incl. the both-non-conformant QUESTION row; IV.5's positive controls and the SmartX negative control named | Carried |
| 5 | O3 | DEC-4: builders only, `registry_hash` stamped, a D8 brief's hand string vs builder output is a finding | Carried, except the `UNRESOLVED` token (R1) |
| 6 | O4 | DEC-6: axis, R-ids, four MEASURED factors each with its instrument, rank rule printed, no weighting | Carried, except the kind enum (R1) |
| 7 | O5 | DEC-7: two renders from the contract, deterministic, `--check` refuses a hand edit | Carried |
| 8 | O6 | DEC-8: ATOM_DECOMP's eight-field package in R19's order; `never_widen_signoff_owed` named, never signed; DEC-15 the first subject | Carried |
| 9 | O7 | DEC-9: the three registries and no fourth; R-16's deploy classification on the mark commit; T11 in a practice worktree with enforce present | Carried |
| 10 | O8 | DEC-12: run-id, manifest, never overwritten, diff keyed on tension identity, a NEW tension is a surprise row | Carried |
| 11 | O9 | DEC-10: sorted at build sites, negative arm fired BEFORE trust | Carried |
| 12 | PART II boundary | CONTRACTS consumes LGIC_ENFORCE's table and produces nothing it produces; DEC-2 the engine as walker + caller; DEC-13; suppliers and consumers in the preamble; the excluded row in the manifest | Carried |
| 13 | PART III bar | the ENDPOINT's ACCEPT lines (byte-identical to the confirmed block); T3/T4/T7/T9/T10/T11/T13 clauses | Carried |
| 14 | PART IV heading | structural | Structural |
| 15 | IV.1 | DEC-4; the CONTRACTS canon row (verdict vocabulary and severity order at `:105-131` of the canon) | Carried |
| 16 | IV.2 | DEC-3's first step: the ledger's plane rows as the seed | Carried |
| 17 | IV.3 | DEC-2; T3's hand-built control (the D8 brief's IV.5/IV.6 as the thing the first run is measured against, DEC-15) | Carried |
| 18 | IV.4 | DEC-4 | Carried |
| 19 | IV.5 | DEC-5's controls, positive and negative | Carried |
| 20 | IV.6 | DEC-3: a one-API denominator is refused by the schema; T1's refusal | Carried |
| 21 | IV.7 | DEC-9; T10, T11 | Carried |
| 22 | IV.8 | DEC-1 and the CONTRACTS class-list row carry 18 + 7 + 8 = 33 and the S3_BUCKET_POLICY correction with 97413 cited | Carried, with the brief's own miscount corrected |
| 23 | IV.9 | DEC-14: pipescript BANNED, comp-pipescript's `data/*/scripts/{gold,silver,bronze}/` scope, the manifest not a consumer census; `evidence.blind_spot` per row | Carried |
| 24 | IV.10 | DEC-6's factors and printed rule | Carried |
| 25 | IV.11 | DEC-1 (the rectangle), DEC-8 (the package) | Carried |
| 26 | IV.12 | DEC-11 (the receiving checker, `lgctfm-contract`, L6's boundary read refuses UNCHECKED); DEC-6 "the closed type set" | Carried for DEC-11; R1 for the DEC-6 citation |
| 27 | IV.13 | DEC-10 (a); DEC-4 (b) -- the default-branch lesson is carried, the token is not the record's | Carried, R1 on the token |
| 28 | IV.14 | DEC-16; MACROS.yaml @`2ceee2821f` landed beside the PRD (per 97417) | Carried |
| 29 | IV.15 | DEC-15; T10 | Carried |
| 30 | PART V, thirteen bullets | V.1 DEC-1/T1 (and the record absorbed); V.2 DEC-4/T4; V.3 DEC-3/T3; V.4 DEC-14/T3; V.5 DEC-10/T9; V.6 DEC-9/T10; V.7 DEC-7/T7; V.8 DEC-8/T6; V.9 DEC-11/T2; V.10 DEC-12/T8; V.11 DEC-15/T10; V.12 T11; V.13 DEC-13 -- each bullet's content named, not pointed at | Carried |
| 31 | PART VI status | NOT CONSUMED; re-measured by the first run at its own vintage | Reason accepted |
| 32 | PART VII limits | bullets 1-9 each placed (T10; DEC-12; DEC-1 field seeding; DEC-2/DEC-12; DEC-5's QUESTION row; DEC-6 no weighting; the COO's 64839 read left to the first subject; the serving-plane boundary; DEC-14's holes; DEC-16) | Carried as limits |
| 33 | REFS TO CARRY | NOT CONSUMED as work; every prior-art path in PATHS | Reason accepted |

## Limits

This is requirements acceptance only. No builder, `grade()`, `comp-trigger` or checker was run for this review; the
33-type partition is read from the schema, not re-censused on the live graph. The ratified-text half is
`3.0.0_SA_CVO`'s; the one line about it above is a byte comparison, not a grade. This seat performs no push, deploy
or cloud mutation. Message 97416 was opened and READ-acked.

Return to `1.0.0_SA_CTO`: carry R1 (four word-level edits) in the brief half and re-offer the resulting pin and hash.
