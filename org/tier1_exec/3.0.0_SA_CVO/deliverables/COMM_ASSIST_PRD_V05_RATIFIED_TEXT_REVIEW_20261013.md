# COMM_ASSIST PRD v0.5 -- ratified-text half (ENDPOINT + CONTRACTS) review

**Reviewer:** `3.0.0_SA_CVO~L` (laptop), on 1.0.0_SA_CTO msg 108782. 2026-10-13 ~15:2xZ.
**Verdict:** REFUSED. FWD-6 lets a file in a shared folder send mail in Andrew's name, and nothing requires that file to be his.

## What was read

- PRD at 8725c9ad7d (v0.5); ratified-text half_hash `aef22ab1ae47e01cb9dfb88dbb5d3ec94e548a11d62b856171bc1834ae23cb14`.
- `git diff 2b0847d728 8725c9ad7d`: FWD-5 to FWD-11 are appended; FWD-1 to FWD-4 are byte-unchanged; CONTRACTS are unchanged.
- Andrew's words: `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261013_143xZ_DEVPLN_RECS_APPROVED_AND_COMM_ASSIST_THROUGH_MUSE.md`
  (lines 5-11) and `ANDREW_DIRECT_20261013_144xZ_MUSE_DECISIONS_AND_COMM_ASSIST_TO_LAPTOP.md` (lines 5-8).

## What holds

- **FWD-5 to FWD-11 trace to his words.** The dell2-hosted folder read over SSH comes from "hosted on DELL2 ... for muse to
  access through SSH". The fallback kept on an efficacy read comes from decision 1. FWD-7's ad hoc bid comes from his FWD-13
  clarification.
- **Each is provable by an act.** FWD-9's deliberate failed refresh and FWD-10's refused off-tailnet attempt are good negative
  arms.
- **FWD-1 to FWD-4 and the contracts are untouched.**

## Why refused (FWD-6)

1. **The answer path carries no identity.** FWD-6's ACCEPT: "his answer is a file muse writes into the dell2 folder, which a dell2
   job hands to the assistant; the assistant then posts, drops or redrafts exactly as it does on a text". Muse reaches dell2 by
   SSH key as the dell2 account `Test` (this seat's own logins, 2026-10-12/13). dell2's agents run as that same account
   (LD-0644: dell2's login is `Test`). So a file in the folder written by muse and one written by any dell2 agent, script or
   other key holder are the same to the forwarder.
2. **The text path is authenticated; this one is not.** The text path acts only on Andrew's own number. FWD-6 promises "the same
   effect as answering by text" and "nothing goes out in his name without his answer, from either place". Those two sentences
   cannot both hold while the folder accepts an answer from any writer. The send is mail in Andrew's name, outward and not
   reversible once sent.
3. **The DONE WHEN has no negative arm.** It reads only the happy path ("one draft sent and one dropped from muse"). Nothing
   exercises a forged answer.

## What would be signed

FWD-6 gains one ACCEPT clause and one DONE WHEN arm, in Andrew's terms:
- **ACCEPT:** "an answer is acted on only when it is shown to come from muse (for example signed with muse's own key, or written
  through a path only muse can write); an answer from anywhere else is refused and recorded."
- **DONE WHEN:** "... and one answer written into the folder by something other than muse, refused."

The mechanism (a signature check, a muse-only account or path) is the cell's, not the card's. The same clause applies to
FWD-7's approvals, which also act on Andrew's word.

## Notes (not blocking)

- The prd-signoff tool names `3.0.0_SA_CVO~Z` as the owed signer, since it signed last. A `~L` stamp evaluates as the CVO's
  (`prd_signoff_lib.py:53` strips the lane). This refusal is stamped as `3.0.0_SA_CVO~L` on the CTO's placement ruling
  (@b4ad06ff09).
