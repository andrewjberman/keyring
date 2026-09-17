# L4-R REVIEW -- NFRA_SPMOVE PRD v0.2, BRIEF half -- REFUSE, three additive corrections

**Reviewer:** `2.0.0_SA_COO~B`, in `4.0.0_SA_CRO`'s stead (no live CRO session; this lane does not hold NFRA_SPMOVE's round).
**Delivered as:** msg 97670 from `1.0.0_SA_CTO`, 2026-09-17T21:48Z.
**Reviewed object:** `org/missions/D9/NFRA/NFRA_SPMOVE/prd/NFRA_SPMOVE_PRD.md` @`46dce14101`, read by `git show` at that pin
(275 lines), never from the working tree. `half_hash` as delivered and as `prd-signoff.py status` printed: `83d29f363092`.
**Against:** `docs/briefs/schwab-trn-sharepoint-export-brief-20260916.md` @`d5e870fed2`, read by `git show` at that pin (231 lines).
**Instrument:** both files read in full by this seat; then a fixed-string census of 23 brief facts over the PRD text, run on
the two extracted files. This is a different instrument from `2.0.0_SA_COO~G`'s and `2.0.0_SA_COO~O`'s v0.1 reviews, which
censused the PRD for the coverage section's existence.

## Verdict

**REFUSE -- additive, brief-half-only.** v0.2 answers all four items the two v0.1 refusals named, and answers them well: the
coverage table exists over the right total, PART V is mapped 10 of 10 with a holder on every row, PART VII is carried 7 of 7
as open items, and s.4.5's bytes reach C4 labelled MEASURED or INFERRED with the design value each one decides. The refusal
is on CONTENT CARRIAGE inside three rows the table marks CARRIED: the row points at a contract, and the fact a consuming
cell needs is not in that contract or anywhere else in the PRD. Each correction below can land in the brief half alone
(BRIEF COVERAGE, Scope, SURFACE MANIFEST, Acceptance matrix), so the ratified-text half need not re-open.

## The denominator

The total matches: **22 of 22** lines matching `^#` in the brief at the pin. **The split printed at PRD `:184` does not.**
The PRD says "1 H1 + 15 H2 + 6 H3". Measured at `d5e870fed2`: **1 H1 + 10 H2 + 11 H3** (H3 = the six outcomes O1-O6 at
brief `:44-64` plus the five substrate subsections 4.1-4.5 at `:104-153`). A total that is right over a decomposition that
is wrong still certifies the sweep; it is listed because the next reader will re-use the split. Correction 0, one line.

## The three corrections (each: brief line -> PRD row that claims it -> what is missing -> what it decides)

**1. No row identity, and exact duplicates in the source -- 0 hits in the PRD.**
Brief `:114-115`: "No unique row id exists; 97 exact same-day duplicate rows per master in August are in the source."
PRD row 13 (`:203`) marks 4.1 CARRIED to C1. Census over the PRD: `unique` 0 hits, `97 ` 0 hits; `duplicate` 1 hit, printed:
`:134` "Masters are never merged and nothing is de-duplicated." -- a sentence whose subject is the masters.
What it decides: acceptance **A1** (`:259`) compares "one row ... field-for-field with its source row", and PART III's bar
is that the row count Andrew reads matches the count the run printed. With no row id, "its source row" has no key; with
exact duplicates in the source, a cell that keys on full-row equality or that drops exact duplicates as a hygiene step
breaks the count while passing a field comparison. C1's "nothing is de-duplicated" reads, in context, as the across-masters
rule. A1 needs to say how a row is located (position within the day partition, or a full-row multiset comparison for one
day) and the coverage row needs the 97 carried as an expected-not-a-defect, the same treatment the 99.98% overlap already gets.

**2. The source and marker ADDRESSES are not in the PRD -- 0 hits for the bucket.**
Brief `:105` gives the source as `s3://opal-data-assets/schwab/{08242234|08335338}/silver/fact_trn/date=YYYY-MM-DD/data.parquet`;
`:121` gives the marker under the same bucket; PART V.6 (`:174`) gives the read scope as exactly
`schwab/{08242234,08335338}/silver/fact_trn/`. Census: `opal-data-assets` 0 hits in the PRD. **S7** (`:253`) says "scoped to
exactly the two masters' `fact_trn`" and C2 gives the marker key without its bucket.
What it decides: S7 IS a path. A read role "scoped to exactly" something the PRD never addresses will be scoped by whoever
cuts the cell, from memory or from the brief, and the PRD's "never a widening" bar cannot be graded against a scope it does
not state. These are EXISTING addresses the project reads, so stating them is carriage, not a Rule 30 hand-typed new name.

**3. The exercised builder output, and the tenancy it revealed, are not in the PRD -- 0 hits.**
Brief `:129-135`: `address("schwab","08242234","platinum","trn-export","month=2026-09")` returns
`s3://opal-data-49financial/schwab/08242234/platinum/trn-export/month=2026-09`, "the registry places both masters in the 49
Financial tenancy"; `name(...)` returns `schwab-trn-export-lambda` / `-daily` / `-role`; `table` and `trn-export` are
placeholders the builder accepted. PRD row 15 (`:205`) marks 4.3 CARRIED to C3; A3; S3. Census: `49financial` 0,
`49 Financial` 0, `trn-export` 0.
What it decides: (a) S1's write home and S7's "output prefix" are in a FIRM bucket while the source is in the shared assets
bucket and the destination is the main Opal SharePoint -- an L5 decomposer reading this PRD alone cannot see that the
project crosses that boundary; (b) CLAUDE.md Rule 30's own mechanism is that the L4 PRD CITES builder output for every new
address and name. C3 says the address "is builder output" and cites none. Carrying the brief's exercised calls verbatim,
labelled PLACEHOLDER WORDS / TIER OPEN AT L5, satisfies both without deciding the tier.
A measured note for whoever cuts S7, offered and not a refusal reason: `opal-data-49financial` carries a bucket-policy
statement `DenyForeignFirmPrincipals` that denies `s3:*` to principals matching `role/cot-*`, `role/inf-*`, `role/mdpf-*`
and `role/opal-assets-mdpf-*` (`infra/aws/terraform/mdpf-pipeline/iam.tf:598-603` @`46dce14101`, which records it measured
from a host). The builder's `schwab-trn-export-role` matches none of the four, so the name the builder gives is also the
name that works; a hand-chosen name under one of those prefixes would apply cleanly and grant nothing. This seat met that
wall on IRPT_BCKEND (rows W2-S49, S53).

## Carried adequately, checked and NOT refused on

- Rows 2-12, 14, 16-22 and both maps: read against their brief sections; the content is present where the row says.
- V.4 "RULED: rebuild" by the CTO: the brief `:170-171` expressly leaves that ruling to "the COO or CTO".
- 4.2's fire times (09:45/21:45 and 10:15/22:15 UTC) are absent from the PRD (0 hits). Not refused on: C2 makes the marker
  the trigger, so no clock value is load-bearing, and "second fire" carries the one fact the design tolerates.

## Two smaller items, fold into the same bump or not at the author's judgment

- 4.1's daily magnitudes are absent (`1,900` 0 hits, `25,000` 0 hits; brief `:111`). They bear on C5/A4: a normal day is
  ~1,900 rows and a rebalance day ~25,000, a thirteen-fold swing that is NORMAL, so a row-count threshold cannot be what
  tells a short day from a quiet one. One sentence on row 13 or in A4.
- V.1 (`:219`) names the holder as "LGIC_NAMING (`2.0.0_SA_COO~G`)" and C3 says "ratified through LGIC_NAMING's schema
  bump". `sequence-check` read LGIC_NAMING `dep_stage=CLOSED status=complete` on 2026-09-17. The schema file still has an
  owning lane; naming that lane, rather than a closed project, keeps V.1 actionable. The brief's "Explicitly out" also
  lists "recipients other than Menachem" (`:86`), which Scope does not repeat.

## Push state

Stated in the commit report that carries this file, as a measured value.
