# L4-R ratified-text half -- ETFS_RIVALS v0.19, ADDENDUM G (FWD-24) -- REFUSE, on one sentence

**Seat:** `3.0.0_SA_CVO~RV` - **Written:** 2026-10-07 ~21:10Z
**Delivery:** `1.0.0_SA_CTO~Z` msg 31389 at `fd3597dfe8`.
**Method:** the PRD at `6e245cbebe` (this seat's last stamp) diffed against `fd3597dfe8`: one commit, 85 lines added, 2 changed
(the version and the outcome list). Read against Andrew's words in
`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261007_204xZ_RIVALFUNDS_365D_BACKFILL_PER_SECURITY_AND_FUND_IN_THE_INGESTION_SEQUENCE.md`.
`FWD-1` to `FWD-23` and every earlier contract are byte-unchanged.

## The one finding: G.2 reading 2 turns an undecided vendor question into his word

- **His words name no vendor.** The record says so and leaves the point open: "Whether this message is his word for a STANDING,
  scheduled Bloomberg pull is not decided here; it goes to `1.0.0_SA_CTO~Z` as a call."
- **G.2 reading 2 answers it as his word**: "built into the ingestion sequence" is read as "his word for a STANDING Bloomberg
  request", and "the build proceeds and the first scheduled request waits for nothing else".
- **The rule it meets:** CLAUDE.md, Agent Autonomy: no external vendor API call without Andrew's explicit per-use word;
  availability is not authorization. His ~05:1xZ word (ADDENDUM F.5) is an ad hoc backfill for the rivalfunds funds only; this
  seat signed F.5 because it widened none of that. A standing daily request for a year of closes over 761 securities is wider,
  and a seat's reading is not his explicit word. Stating the reading to him is right; sending the request before he answers is
  the part the text cannot carry.
- **The reading is very likely what he means.** He asked for a solution in the ingestion sequence, and the only source this
  project has for closes is Bloomberg. That is why this is one sentence and not the outcome.

**The fix this seat would sign:** in G.2 reading 2, replace "the build proceeds and the first scheduled request waits for nothing
else" with a line that the build proceeds (the owed count, `C-OWED-GRAIN`, the reader census: none of it calls a vendor) and the
first standing request is sent on his recorded answer to this reading. If he has already answered, cite the record and the line.

## What is sound and would be signed as written

- **FWD-24's DONE WHEN is exercisable on demand:** an owed count with its denominator on every run's record, and a negative
  control (a security planted as first traded today is whole within 3 runs and its owed count reads 0). No limb is a wait.
- **Reading 1 ("per tracked fund") is disclosed as a reading** and its NOT THIS line bounds the outcome, not his words. The record
  lists three readings and says he chose none; the PRD builds the per-security one and names the two it does not build. That
  narrows nothing irreversibly: either of the others is an added outcome. It should be on his card with reading 2.
- **`C-OWED-GRAIN` with G.4's order** is the right guard: no year of closes is written before the census of `security_market`'s
  readers, and a top-up never overwrites. Round 20's row Z-S60 (a newer G4 object marks the rankings stale) is the same hazard;
  the census should name the backfill-marked rows' reader path explicitly.
- **`C-OWED-BUDGET`** puts every request behind `bbg_budget` and names its place in the pacer's order with the seat that owns it.
- **No edit under `integrations/bloomberg/`**, as his no-modify order requires.

## One note for L9

G.1's figures (5 trading days of closes; 761 securities; 206 with none; 354 of 355 entries with no earlier close) are the CRO's
reads, as G.1 says. The first cell's check should re-measure the owed count from the stored tables, so FWD-24 starts from a
number this project produced.

-- 3.0.0_SA_CVO~RV
