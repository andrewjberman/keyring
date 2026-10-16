# L4-R review -- SOC2_MSLOGS PRD v0.1 @bedd22acc3, ratified-text half

**archetype:** VALIDATE
**Reviewer:** 3.0.0_SA_CVO (dell1), 2026-10-16 ~16:4xZ. Delivered by 1.0.0_SA_CTO~DELL1 msgs 6867 and 6868 (both acked). Half hash
`21a6f3391809`.
**Read:** the ENDPOINT section against `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_SOC2_MSLOGS_20261016.md` @b8c7dd61e8;
every CONTRACTS row; the counterpart TCKT_MTADTA PRD v0.5 @aca2d95d6f (C-ACCESS); Andrew's records of ~16:12Z and ~16:2xZ.

## Verdict: REFUSE (one ground, a one-row fix)

## ENDPOINT -- passes

All nine FWD blocks (title, DONE WHEN, ACCEPT, SOURCE) are byte-identical to the confirmed source, checked block by block as a substring of
the file at @b8c7dd61e8. The scope cap and the responder definition are in the source too. Andrew's "all recs approved" (~16:2xZ) names
that file's nine DONE WHEN lines as confirmed. The raw, every-account and no-content choices stand on his own words ("get the raw audit pull,
dont redact it unnecessarily"; "we dont need to see the body of an email"), and C-POPULATION, C-RAW and C-CONTENT carry them faithfully.

## The ground -- a member's write is no longer constrained, and that contradicts C-RAW and FWD-8

- **C-RAW:** "Bronze is the audit records exactly as Microsoft ships them, byte for byte". Its proof is "a stored record compared byte for
  byte against the blob the API served for it".
- **C-ACCESS** is "inherited, as amended by TCKT_MTADTA v0.5", and "the members' alias serves the reads of C-READS, a write and the
  maintenance ops".
- **What v0.5 actually inherited:** the write that v0.5 gave members "runs the same C-POPULATION drop and C-FIELDS levers as the
  collector's put before any byte is stored". This PRD retires that filter. So the inherited constraint points at nothing, and as written a
  member's `put` stores whatever bytes the member sends.
- **What follows:** one stolen group login can forge or (if `put` may overwrite a key) replace audit records in bronze. That breaks:
  - C-RAW's byte-for-byte property;
  - FWD-1's "nothing in it was prepared by hand";
  - FWD-8's "the record survives an attacker", which is the project's stated purpose with FWD-9.
- **C-RESIDUAL (4)** says a member can "write through the door", but not whether that write can add or alter stored records. So the
  statement Andrew holds is incomplete on the one point that decides whether the record can be trusted.

**The fix (the CTO's choice of form):** C-ACCESS states what a member's write may store. The two clean forms:

- (a) The members' write is the re-collect op only. The door itself fetches a content blob from the Management API inside the 7 days,
  and refuses a caller-supplied payload.
- (b) The members' write is dropped.

Either way:
- A bronze key is write-once, so no op overwrites a stored record. Name the mechanism, for example the door refusing an existing key, or
  S3 Object Lock.
- C-RESIDUAL (4) says plainly what a stolen member login can and cannot write.

Andrew's 15:3xZ word ("read/write/do ops in there") is honoured by either form. What it did not decide is that a write may bypass "as
Microsoft ships them". He decided that at 16:12Z.

## Nits (fix in the same pass; not grounds)

1. **The reads FWD-5 and FWD-6 have no named op.** C-ACCESS admits "the reads of C-READS", and C-READS lists `timeline`, `exposure`,
   `session_span` and `persistence`. Two reads are left out:
   - the per-account baseline read (FWD-5);
   - `outside_baseline` (FWD-6, named in C-BASELINE).

   Add both to C-READS, or have C-ACCESS name C-BASELINE's reads.
2. **"Raw objects" versus "raw records".** C-READS returns "query results, never raw objects". C-RESIDUAL (4) says a member "can read every
   Opal account's raw records". Both can be true (full field values, one account and window per call), but say it once in the same words.
3. **The frozen table.** C-SWITCH freezes `audit_events` ("never written again"). C-ACCESS's members' write and maintenance ops should
   name `audit_records` as their only bronze target, so the freeze is a rule the door enforces and not a convention.

## Not this half's to grade

- Employee notice and policy (OPEN AT ANDREW) is correctly placed with Andrew and counsel, as a fact and not a gate.
- C-HOMES builder output is graded at the cut, not here.

-- 3.0.0_SA_CVO
