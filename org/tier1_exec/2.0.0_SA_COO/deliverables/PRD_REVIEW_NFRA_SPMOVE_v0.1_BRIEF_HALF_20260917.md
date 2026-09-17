# L4-R REVIEW -- NFRA_SPMOVE PRD v0.1, the BRIEF HALF

**Reviewer:** `2.0.0_SA_COO~G`, in the stead of `4.0.0_SA_CRO` (no live CRO session), per Andrew 2026-09-11 ~05:3xZ.
**Subject:** `org/missions/D9/NFRA/NFRA_SPMOVE/prd/NFRA_SPMOVE_PRD.md` v0.1 @aad379d84b, half_hash `f1d2f2d92157`, requested by
`1.0.0_SA_CTO` msg 97662.
**Half reviewed:** BRIEF -- Authority and project arc, Scope and evidence boundary, SURFACE MANIFEST, Acceptance matrix,
Canonical handoff. ENDPOINT and CONTRACTS are `3.0.0_SA_CVO`'s half and I take no position on them.
**Brief:** `docs/briefs/schwab-trn-sharepoint-export-brief-20260916.md` @d5e870fed2 (commit resolves; 231 lines, 22 headings).

**VERDICT: REFUSED.** One structural defect, and it is the first thing the review request itself asks for. The rest of the half
holds and the correction is additive -- no re-write.

---

## THE DEFECT -- there is no BRIEF COVERAGE section, so the brief's content is neither carried nor counted

The review request states the bar: *"every BRIEF COVERAGE entry carries its section's CONTENT into the consuming cell (fields,
units, paths, guards, proof gaps), not a pointer; the heading denominator matches the brief at the named pin."*

Measured: the PRD has seven `##` sections -- Authority and project arc, Scope and evidence boundary, ENDPOINT, CONTRACTS,
SURFACE MANIFEST, Acceptance matrix, Canonical handoff. **There is no BRIEF COVERAGE section at all**, and a case-insensitive
read of the whole PRD for `brief coverage|does not claim|non-claim|Part V|Part VII` returns **0 hits across 128 lines**. So:

- **No heading denominator exists to compare.** The brief carries 22 headings at @d5e870fed2 (7 Parts, five 4.x substrate
  subsections, six O-outcomes, the verbatim-words section, s.8 and REFS). Nothing in the PRD states that count or maps against
  it, so a section the brief carries and the PRD drops cannot be detected by reading the PRD.
- **PART V (what must be true, without scoping it now) is carried nowhere by name.** Its preconditions are the brief's own
  statement of what the project must establish; the sibling PRD reviewed an hour earlier (NFRA_MCPINDEX v0.1) does exactly
  this -- "its nine preconditions (Part V) land as: C1 ..., S8 ..." -- which is the form this half is missing.
- **PART VII (what this brief does not claim) is carried nowhere.** The Evidence boundary section carries two real
  qualifications (the SharePoint site choice is this seat's reading, confirmed at L5 not assumed; completion markers exist only
  from 2026-08-31, so marker behaviour before that date is UNMEASURED) -- good, but partial, and not the brief's non-claims.
  A non-claim that is silently dropped reads later as a claim nobody made.
- **The measured substrate (brief 4.1-4.5: the data, the trigger, the address, the destination and write path, the measured
  file size) is not inventoried in this half.** In fairness, CONTRACTS -- the OTHER half -- does carry much of that content
  well, including the 140 source columns, the marker path, and BOTH measured marker irregularities with their dates
  (2026-09-11's second fire, 2026-09-15's rewritten zero-table marker). My point is narrow and structural: the brief half is
  where the coverage claim and its denominator live, and neither exists, so nothing shows that the carry is COMPLETE.

**THE CORRECTION I ASK FOR:** add a BRIEF COVERAGE section that (a) states the brief's heading denominator at @d5e870fed2, (b)
maps each Part V precondition to the contract, surface or cell that lands it, and (c) carries Part VII's non-claims into the
evidence boundary rather than dropping them. Content, not pointers, per the request. Corrections by pinned line, as asked.

## WHAT I MEASURED AND FOUND SOUND

- **The brief pin resolves** (`git cat-file -t d5e870fed2` -> commit) and the brief is present at it.
- **Andrew's words are carried verbatim and attributed** in Authority and project arc: the five inputs (an AWS folder on the
  main Opal SharePoint whose paths follow the AWS path structure; masters 08242234 and 08335338 only; monthly workbooks,
  separate per master, all 140 columns; standing and daily about fifteen minutes after the Schwab pull; Menachem as recipient
  only after several clean days on his word), the commissioning words ("a small project") and the confirmation ("3 approved",
  record @57a15b2bbe).
- **Outcome coverage closes in both directions.** Every FWD-1..FWD-6 is claimed by at least one surface (FWD-1 S1+S2, FWD-2 S1,
  FWD-3 S2+S3, FWD-4 S4, FWD-5 S5, FWD-6 S6, with S7 the read role serving all), and no surface is outcome-less. A1..A6 map
  one-to-one onto FWD-1..FWD-6; A7 and A8 cover contracts C2 and C4.
- **The acceptance bars are exercises, not reviews**, and several are genuinely discriminating: A2 requires a morning whose
  pull completed on its SECOND fire; A4 requires a quiet day and a failed/short day to be distinguishable from the run record
  ALONE, without opening the workbook; A5 requires a refusal BEFORE the word and a delivery after it; A6 requires the diff to
  show no new build. A7's bar -- never a half-written workbook -- is the right shape for the marker irregularity the brief
  measured.
- **The scope boundary is honest about what it will not do**: no cross-master de-duplication (Andrew chose separate files, so
  the ~99.98% overlap is expected and named as expected), no change to `dim_transaction`, no general-purpose SharePoint write
  tool, no vendor egress, and NFRA_OPLGTW's reader roles "never widened for this".
- **The handoff states its own place in the queue correctly**: NOT in Andrew's 2026-09-17 seat order (IRPT_BCKEND,
  NFRA_MCPINDEX, MDPF_TAXSMA), so it takes a lane only when he places it or one frees past those three; and the first cells are
  ordered for a reason that is stated (confirm site and tier, then the producer, because the delivery capability is only worth
  building once the object exists).

## WHAT I DID NOT MEASURE

- No AWS, S3, SharePoint or Gateway state; no run of any producer; no read of `fact_trn` or of a completion marker. The brief's
  substrate figures (row counts, the 140 columns, file sizes, the two marker irregularities) stand as the brief's measurement
  at 2026-09-16, not as mine.
- The tier question (platinum vs gold) is explicitly deferred to L5 against the canon; I did not pre-empt it.
- ENDPOINT and CONTRACTS bytes, which are the other half's.

## NON-APPLICATION

This refusal binds the brief half's bytes at `f1d2f2d92157` only. It is additive: nothing already written needs removing, and
the six outcomes, seven surfaces and eight acceptance rows are not in dispute.
