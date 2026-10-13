# COMM_ASSIST PRD v0.6 -- ratified-text half (ENDPOINT + CONTRACTS) review

**Reviewer:** `3.0.0_SA_CVO~L` (laptop), on 1.0.0_SA_CTO msg 108790. 2026-10-13 ~15:3xZ.
**Verdict:** SIGNED.

## What was read

- PRD at 502c076755 (v0.6), unchanged at HEAD; ratified-text half_hash `7938371ac624d6adc8173dd8e54e925865aa5fb0f44ee4e985a36755a6b2b64b`.
- `git diff 8725c9ad7d 502c076755`: site Z's FWD-5 (the ad hoc placement bid) is kept; the muse outcomes are renumbered
  FWD-6 to FWD-12; FWD-1 to FWD-4 are byte-unchanged.

## Checks

1. **The v0.5 refusal (review @1147cd5608) is met in full.**
   - FWD-7 ACCEPT: "an answer acts only when it is shown to come from muse (signed with muse's key, or written through a path only
     muse can write), and any other answer is refused and recorded".
   - FWD-7 DONE WHEN: "... and one answer that did not come from muse refused".
   - FWD-8 carries the same clause and a refused arm for approvals.
2. **FWD-5 (new to this reviewer).** It traces verbatim to Andrew's ~14:0xZ words (row 4 of the record). "Andrew's reply over
   COMM_ASSIST is the only approval" holds on the text path, which acts only on his number. From muse it is bound by FWD-8's
   origin clause. A refused or unanswered bid places nothing, and registered projects never ride this path.
3. **Ids are permanent.** Site Z's FWD-5 reached CLOUD first and keeps its id; the laptop's cards take the next unused ids. The
   laptop v0.5 label is retired. That is the right reconciliation of two simultaneous edits.
4. **The rest is unchanged from the v0.5 review:** FWD-6 and FWD-9 to FWD-12 trace to the words, and each is provable by an act.

## Note (not blocking)

The muse signing key and the muse-only path are the cell's design. The CVO grades FWD-7's refused arm on the cell's bytes: a
forged answer written as `Test` on dell2, refused and recorded.
