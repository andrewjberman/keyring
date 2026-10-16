# NFRA_TRNSPT PRD ADDENDUM 3 -- ratified-text half review (FWD-8 ACCEPT): SIGNED

**Seat:** `3.0.0_SA_CVO~DELL2`, 2026-10-16 ~14:0xZ. **PRD:** `org/missions/D9/NFRA/NFRA_TRNSPT/prd/NFRA_TRNSPT_PRD.md` @881f9a12c2
(ADDENDUM 3 @b95bb36126 plus the PARKED line @881f9a12c2). Asked by `1.0.0_SA_CTO~DELL2` msgs 9404 and 9414.
**Half reviewed:** ratified-text, half_hash `2dd636bd711c598539ec4434ea22cc3ac0c9439a1aa040e8601fcf5f99b1f407` (was `43de98f5f810...`,
signed v0.2 @3aef5982b9). endpoint_hash `cb3a4539ad5a...` is unmoved: the change sits in the addendum, not in the ENDPOINT block.

## What I read

1. **The change against the in-place FWD-8 (line 64).** The new ACCEPT is the old one with "the terminal seat's account" struck and
   "(his word, 2026-10-07)" dropped. Nothing else differs: the refusal of everyone else, "shown, not asserted", the narrower reader on the
   wiped copy, and the no-content-copy rule are all kept word for word. DONE WHEN is unchanged.
2. **The ground.** The Andrew-direct record
   `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_134xZ_SYNTHETIC_TEST_DELETES_NEED_NO_CALL_OPAL_TERMINAL_GONE_DELL2.md`
   quotes him: "opal terminal key and account are already deleted from IAM". I measured it live at ~14:0xZ:
   `iam get-user --user-name Opal_Terminal` returns NoSuchEntity. Positive control: `sts get-caller-identity` returns
   `user/cloudops-dell2-agent-user`, so the call path works.
3. **What it does NOT do.** No reader is named in the terminal account's place. That is correct, because FWD-8 says only Andrew names
   readers, and naming one here would be this seat or the CTO widening his list. The second-reader role is left as it is. A trust
   statement on a deleted user is bound to that user's unique id, so a re-created `Opal_Terminal` would not match and the role grants
   nothing. Its removal is a separate IAM pair.
4. **The state.** @881f9a12c2 records that FWD-8 stays PARKED under ADDENDUM 2: the addendum issues nothing and lifts no hold.
   That matches msg 9414 and withdraws msg 9403's "the HOLD lifts".

## Verdict

**SIGNED.** The ACCEPT narrows only by a reader Andrew himself removed. Every other clause holds, and FWD-8 can still be realised
as written once it is un-parked.

**Note for the un-park, not a condition:** the narrower reader (the wiped copy) has no principal until Andrew names one. When FWD-8 is
cut, that half of the ACCEPT is graded NOT-REALIZABLE-YET rather than passed by absence.

-- `3.0.0_SA_CVO~DELL2`
