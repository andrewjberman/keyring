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

## Addendum ~16:1xZ -- re-sign at the merged bytes (2.0.0_SA_COO~CA msg 108800)

Site Z's `1.0.0_SA_CTO~Z` re-cut FWD-5 at a2ea4d0ac1 (15:33Z), on `3.0.0_SA_CVO~Z`'s refusal @8a7a68a9cc. `3.0.0_SA_CVO~Z` signed it
(b085dc7e27), and box-sync carried both in after this seat's v0.6 stamp. `git diff 502c076755 HEAD` on the PRD is one word in FWD-5's
ACCEPT: "a registered project's work" becomes "an ACTIVE registered project's work". That restores Andrew's verbatim "not for
active registered projects" (row 4 of the 14:0xZ record). It is correct, and it changes nothing else. Re-signed at the current
bytes; ratified-text half_hash `cf94d73bb2f21ec95babf614481ac1cdc9ef325b36591713b8e88087ae608fc5`.

**Note for the CTO:** two CVO lanes signed this project's ratified half within 20 minutes (`~L` at v0.6, `~Z` at v0.5 re-cut).
Each stamp made the other read STALE and refused the L6 gate. Since the CTO placed COMM_ASSIST on the laptop (@b4ad06ff09), one
signer (`~L`) is the stable choice. The tool still routes to `~Z` as the last signer.
