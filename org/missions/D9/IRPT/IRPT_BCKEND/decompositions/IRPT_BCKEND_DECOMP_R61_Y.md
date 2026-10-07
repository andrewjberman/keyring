# IRPT_BCKEND round 61 -- workstream ~Y decomposition

Issuer `2.0.0_SA_COO~Y2` (dell2 successor of `2.0.0_SA_COO~Y`), 2026-10-07 ~08:5xZ. The rectangle is section 5 of the CTO's
round-N analysis, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUNDS_47_60_20261007.md`
@e363a194ed, `~Y` table: three items, ONE issuance, no edges between them. Base: dell2 CLOUD `cc788ffd58`.

## The rectangle

| item | cell | cut? | why |
|---|---|---|---|
| E-Y1 -- the source map equals live for `irpt-ycharts-generate` (S320) | `IB-yr-611` | **NOT CUT: met by the issuer's act @ad59d08617** | A one-field record fix in a file whose row this lane holds. The lane grant to `~Y2` was extended @4f3505fb84 (CTO~DELL2 msg 186); the fix and its row S353 are committed. |
| E-Y2 -- every changed member of `irpt-ycharts-generate` has an owner (S337, members half) | `IB-yr-612` | **CUT** | one order, one worker |
| E-Y3 -- the 390 s release handed to `~G2` | `IB-yr-613` | **NOT CUT: met by the issuer's hand-over @a213f3db1f, with an amendment** | CTO~DELL2 msg 91 told this seat to supply the branch, tests and pair text. Done at `deliverables/2.0.0_SA_COO~Y2/release390/`. |

## Issuer rulings inside this decomposition (spine: the issuer amends its own criteria)

1. **E-Y1 criterion (1) is amended.** It said "the recorder runs `--function irpt-ycharts-generate`". It now reads: "the map row's
   `deployed_code_sha256` equals live CodeSha256, from a `get-function-configuration` read". `record-terraform-deploy.sh` sets
   `last_deployed_commit` to the newest commit on `source_dir`. The IRPT_YCDGEN commits since 2026-10-04 that are not deployed would
   then read as deployed, which is the S320 class itself. The live read at ~08:3xZ gave `uFTONal/RhfoETes..`, and the edit sets
   exactly that. Criterion (2) (the close-leg step) is met by `release390/HANDOVER.md` @59ae6e3b73. No gate limb graded this
   amendment: no order is cut for it.
2. **E-Y3 criterion (1) is amended.** "Rebased by merge onto CLOUD with its tests passing" becomes "carried onto CLOUD as a patch
   that applies at `aaea945582`, with the test run owed on a host that has PyMuPDF". The lane gate refuses `~Y2` on
   `resident_worker.py`, which is correct under msg 91 (`~G2` is its one writer). No interpreter on dell2 carries `fitz`, and
   installing it is egress off Opal infrastructure. Criterion (2) is met: the pair text is committed and was sent to `~G2` by
   path at 08:01Z. No gate limb graded this amendment.

## Cell IB-yr-612 (cut)

The r57 census of `irpt-ycharts-generate` (`deliverables/2.0.0_SA_COO~P/r57_census/census-irpt-ycharts-generate.json`) lists 19
riders. 4 are claimed (`canonical_profile_reads.py`, `loaders.py`, `maintained_sources.py`, `served.py`). 15 are not: the 14
`fixtures/har/*` files and `templates.json`. The cell writes one owner table, with each member's owning lane or REMOVE and the
commit that last changed it. None of the 15 is in `~G2`'s one-writer set; the check still enforces that clause.

| criterion | file | base reading at cc788ffd58 |
|---|---|---|
| Y61-2-AC1 | `deliverables/2.0.0_SA_COO~Y2/R61_checks/check_612_member_owners.py` | FAIL as expected: the owner table is absent (FileNotFoundError) |
| Y61-2-AC2 (control) | the same check with `--file deliverables/2.0.0_SA_COO~Y2/R61_checks/planted_bad_owners.json` | FAIL as expected: it refuses the planted lane `NO_SUCH_LANE_PLANTED`, the planted commit, and the short member set |

## Four-postulate record

(i) MECE over the domain "the 19 riders of the r57 census": 4 claimed + 15 cut = 19, by subtraction from the printed census.
(ii) Same grain: one row per packaged member. (iii) One intent: name an owner. (iv) State: the table moves ownership only, and no
member's bytes or deploy state.

fanout: 1 of 1 chains, cap 8, reason: one cut cell; E-Y1 and E-Y3 are met or held by the issuer's own acts, per rulings 1 and 2.
