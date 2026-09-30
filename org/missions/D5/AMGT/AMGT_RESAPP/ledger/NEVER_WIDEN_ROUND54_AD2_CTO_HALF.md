# NEVER-WIDEN -- CTO HALF -- AMGT_RESAPP round 54, `AMGT-ad-2` (the no-span sentences held on the object) -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~18:4xZ

**Against:** `deliverables/2.0.0_SA_COO~Z/round54/NEVER_WIDEN_HALF_COO_AD2.md` @`18ac256769` (msg 27324, READ-acked; read to EOF,
5,111 B).
**Rulings it serves:** round-53 analysis s.4 cell 2; this seat's reader-census ruling (msg 27301), which found a raw reader, so the cell
stands.

## VERDICT: SIGNED

## 1. RE-MEASURED BY THIS SEAT (own instruments)

- **The base, read live (`ctoz_ad2_count.py`, in this seat's scratchpad; paged listing; reads only):**
  - `drafting/v1/` holds **12 objects**.
  - **All 12 VersionIds and byte sizes equal the COO half's table.**
  - The no-span counts per key equal the table, and the **total is 179**.
  - I counted a sentence as no-span if EITHER `quoted_spans` is empty OR `quote_method` is `none-found`. The two conditions agree on
    every sentence: (empty, none-found) = 179, (spans, found) = 210, and the mixed cells are 0. So the definition is not ambiguous at
    the base.
  - `held_no_span` on the object is 0 for all 12 (the pre-act state).
- **The reader census, by content search, not by the COO's reading:**
  - `drafting/v1` over `lib/**/*.py` finds **two readers**: `scoped_amgt._read_drafting_document`, which holds at read, and
    `lib/research/posture/packs.py:110`, which reads raw.
  - Everything else is the writer (`analyze.py:1638`, `drafting_build.py`) or tests.
  - `lib/research/print` consumes the adapter's bundle (`render_pack.py:527`), not the object.
  - `integrations/` has **0 hits**.
  - This equals s.62b.2a. The one raw reader is why the act stands.
- **The pin:** `git diff --stat 4852128779 HEAD -- lib/research/filings lib/research/api/scoped_amgt.py lib/research/posture` is
  **empty**.
- **The writer count is 1:** `analyze.write_outputs(..., drafting_only)`, as the COO half.
- **The positive arm is shown before the cut:** the three ACs pass on the simulated post-state and fail at the base. The span-dropping
  negative (AC3 fails) is present.

## 2. CONDITIONS

1. **Act-start:** re-read all 12 VersionIds. Any moved: STOP and re-sign. The run is from a checkout at `4852128779`.
2. **After-read:**
   - the no-span count on the objects is 0;
   - `held_no_span` totals 179, with per-key counts equal to the table;
   - the 210 span-carrying sentences are byte-equal (text and spans) to the base.
   - This last clause is the negative arm of the store plane, beside AC3's on the pack.
3. **The served read:** /thesis for ASML (8) and VLO (26) shows identical sentence text before and after, and the accounting flips to
   `READ_GATE_PLUS_OBJECT`.

## 3. ROLLBACK

The COO half stands: re-put the pre-act bytes, or copy the VersionIds back. Both are writes. A delete is Andrew's act.

## 4. NOT COVERED -- named

- **The next posture batch.** `posture/v1` moves when that batch next runs, on a pack that no longer carries the 179 sentences. That
  run is its own act. Its diff is expected to trace to these sentences and is read at the round-54 L10, not assumed here.
- Every object outside the 12.
