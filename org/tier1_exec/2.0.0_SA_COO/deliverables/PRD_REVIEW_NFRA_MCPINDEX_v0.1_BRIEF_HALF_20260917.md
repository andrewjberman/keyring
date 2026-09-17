# L4-R REVIEW -- NFRA_MCPINDEX PRD v0.1, the BRIEF HALF

**Reviewer:** `2.0.0_SA_COO~G`, in the stead of `4.0.0_SA_CRO` (no live CRO session), per Andrew 2026-09-11 ~05:3xZ.
**Subject:** `org/missions/D9/NFRA/NFRA_MCPINDEX/prd/NFRA_MCPINDEX_PRD.md` v0.1 @033f152e5d, requested by `1.0.0_SA_CTO` msg 97654.
**Half reviewed:** BRIEF -- everything except ENDPOINT and CONTRACTS (those are `3.0.0_SA_CVO`'s half): Authority and project arc,
Scope and evidence boundary, SURFACE MANIFEST, Ground truth measured at authorship, BRIEF COVERAGE, Acceptance matrix, Canonical handoff.

**VERDICT: REFUSED.** One defect in the half, stated below with its citation. Everything else I measured holds, and the refusal is
narrow: it names a correction, not a re-write.

---

## THE DEFECT -- the named single writer denies, in its own bytes, that it writes the live catalog

The brief half's Scope section (`:51-53`) relies on "`app/refs/DATA_CATALOG.yaml` and its one writer" as an unchanged
dependency, and the PRD's product logic rests on ONE catalog with ONE writer (C1, the other half, names
`emit_catalog_v02.py` as that writer).

Measured at HEAD, on the writer's own text:

```
workflows/atom_decomposition/emit_catalog_v02.py:5   "THE LIVE refs/DATA_CATALOG.yaml IS NEVER TOUCHED BY THIS SCRIPT.
                                                      The staged file becomes ..."
workflows/atom_decomposition/emit_catalog_v02.py:3   ".../catalog_v02/DATA_CATALOG.v0.2.staged.yaml (the STAGED port artifact)"
workflows/atom_decomposition/emit_catalog_v02.py:43  OUT = os.path.join(OUT_DIR, "DATA_CATALOG.yaml")
```

So the script writes a STAGED artifact into its own output directory and disclaims the live file. The live catalog is
`infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`, `version: 0.3`, 15 channels. **Nothing in the PRD or in the writer
names what writes THAT file.** A project whose first contract is "one catalog, one writer" cannot rest on a writer that
disclaims the artifact, and the brief half inherits the error by carrying the dependency as settled.

**THE CORRECTION I ASK FOR** (either is enough, and both are cheap):
1. Name the actual writer of the live `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` at HEAD, with its path, and say
   how `emit_catalog_v02.py` relates to it (a superseded port? a staging step whose output is promoted by hand?); or
2. State that the live catalog's writer is UNKNOWN AT THIS VINTAGE and make identifying it the first act of surface S1, so the
   "one writer" contract is a thing the project ESTABLISHES rather than a thing it assumes.

Either way the Scope section's "relies on and does not change ... its one writer" needs the same qualifier, because as written
it asserts a writer relationship the estate does not evidence.

## WHAT I MEASURED AND FOUND SOUND

- **Every commit the half cites resolves** (`git cat-file -t`): `57a15b2bbe` (the Andrew-direct record), `9da61cab00` (the
  endpoint document), `826ac6925a` (the CRO brief), `033f152e5d` (this PRD).
- **The live catalog is v0.3**, as the PRD says, at the gateway path; `version: 0.3` read from the file.
- **The D6 bar the PRD leans on is real and says what the PRD says it says**: `D6_OPAL_ANALYST_GRAPHQL_PRD.md:57` -- "The
  GraphQL layer cannot precede W5 without re-minting a second catalog (build-ladder violation)."
- **Outcome coverage is complete in both directions.** The acceptance matrix's A1..A10 map one-to-one onto FWD-1..FWD-10, and
  A11/A12 cover contracts C2 and C3. Every FWD is claimed by at least one surface in the manifest (FWD-1 S1+S2, FWD-2 S3,
  FWD-3 S4+S7, FWD-4 S4+S8, FWD-5 S5+S7+S8, FWD-6 S6, FWD-7 S9, FWD-8 S10, FWD-9 S7+S11, FWD-10 S1+S8); no surface is
  outcome-less and no outcome is surface-less.
- **The acceptance bars are exercise-shaped, not review-shaped**: each names a count with its denominator, a transcript, or a
  refusal that must fire (A10's planted unclassified tool, A12's hand-typed non-conforming name). That is the shape a brief
  half should carry.
- **The evidence boundary is explicit and honest** (`:60-63`, `:149-150`): repository only; no AWS state, table sizes, object
  counts or query timings; per-property common questions not enumerated; every capacity claim DESIRED until a cell exercises
  it, with the first analysis cell of each property carrying the measurement. The brief's own six non-claims are carried here
  rather than dropped, which is what BRIEF COVERAGE asserts and what I checked it against.
- **The handoff is correctly scoped**: L5 is the COO's on a lane MSTR seats; Andrew's 2026-09-17 seat order puts this project
  second, behind IRPT_BCKEND; FWD-3's live exercise waits on NFRA_OPLGTW's own enabling act and the cells prove their own half
  meanwhile.

## WHAT I DID NOT MEASURE, so no one reads this review as wider than it is

- **The tool counts** in Ground truth ("49 tools registered, 44 enabled ... 35 Microsoft 365, 6 YCharts, 1 portal upload, 2
  estate graph") are NOT reproduced here. The internal arithmetic is consistent (35+6+1+2 = 44), and
  `infra/aws/ec2/opal-gateway/app/tools.py` carries no registration or classification structure at all (enumerated: 0 hits for
  `safety_class|classification|"enabled"` across 817 lines), so the registry those numbers come from is elsewhere and I did not
  find it within this review's cost. They stand as the author's measurement, not as mine.
- **`read_teams_attachment` as the live unclassified-tool defect**: the symbol exists in `app/tools.py`; I did not verify that
  it is enabled in deployment nor that it is denied to every tier.
- **The 36 served-data rows** figure belongs to C1, the other half, and is outside this review. I note only that the live
  catalog's shape is 15 channels, so whoever signs that half should confirm what "36 rows" counts.
- No AWS state, no deployed state, no portal parity read.

## NON-APPLICATION

This refusal is about the brief half's bytes at `033f152e5d` only. It takes no position on ENDPOINT or CONTRACTS, which are
`3.0.0_SA_CVO`'s to sign, beyond flagging the C1 writer question that the two halves share.
