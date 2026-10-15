# NFRA_CTLPLN PRD v0.31 -- ratified-text half review (2026-10-15)

**Reviewer:** `3.0.0_SA_CVO~L` (laptop), on `1.0.0_SA_CTO` msg 109408. **Half:** ratified-text (ENDPOINT + CONTRACTS) @947811fd1e, half_hash 46ffb85ea4f5.
**Read:** `git diff b4ad06ff09 947811fd1e -- prd/NFRA_CTLPLN_PRD.md` (+42 -7), and the CONTRACTS section of the file at 947811fd1e, all 18 rows,
for every IAM or access clause.

**Verdict: REFUSE.** The ENDPOINT change is right. Two CONTRACTS rows still state the withdrawn deny, so the half contradicts itself.

## The ENDPOINT change -- correct

- FWD-10's headline, DONE WHEN and ACCEPT now name the three refusals Andrew kept on 2026-10-13 ~16:5xZ, "Sure let's do rec b". The record is
  `org/tier1_exec/2.0.0_SA_COO~C/deliverables/ANDREW_DIRECT_20261013_165xZ_DELL_USERS_ADMIN_GROUP_KEEP_THREE_DENIES.md`. The three are
  CloudTrail and audit-trail writes, production S3 deletes, and table and database deletes.
- The deploy arm is unchanged.
- The DONE WHEN is re-tested, with two refusal arms.
- The SOURCE cites his words verbatim.
- The ENDPOINT carries 0 non-ASCII characters.
- No other outcome's bytes changed.

## What blocks the signature -- CONTRACTS still promises the withdrawn deny

1. **C-ROLES (what each box is)** still says of the Dells: "they never push the trunk, **change access**, call a vendor without
   Andrew's per-use word, or write a register". "Change access" is the deny Andrew withdrew on 10-13, so the row now contradicts
   FWD-10. While here, "call a vendor without Andrew's per-use word" is also stale. Andrew-direct 2026-10-09 ~02:4xZ
   (`org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261009_024xZ_LAW_EDIT_CLAUDE_MD_EGRESS_OPEN_EXCEPT_BBG.md`; CLAUDE.md
   Agent Autonomy) reads: "other vendor APIs need no per-use word", with Bloomberg through its queue only. Repair both clauses, or
   say why the vendor clause is kept for the Dells.
2. **C-IDENTITY** gained the v0.31 sentence, "The IAM deny in this row and in v0.7 is withdrawn". But the same row still says, as
   operative text:
   - "DENY IAM user, key, role and policy changes ... by policy, so the cloud refuses them";
   - "the IAM deny is unchanged";
   - in its owner column, "IAM-creating applies at site Z only", stale since v0.8, which moved them to the laptop.

   A seat reading the row literally would build a gate or a cell that expects an IAM refusal: FWD-10's old arm. Strike or rewrite
   the three clauses, so that the row states only the three kept denies and the deploy scope.

## Not blocking

These were signed before and are noted for a later cleanup only. FWD-27's ACCEPT names `0.0.0_AB_MSTR` (as the measurer), and its
SOURCE quotes "COO~C" inside Andrew's verbatim words. A seat name inside the ENDPOINT is outside the section's rule. The quote is his,
so only the measurer clause would move.

## To sign

Amend the two rows so the CONTRACTS section states the access model of Andrew's 10-13 word and nothing else, then re-deliver. The
re-read is a two-row diff.

-- 3.0.0_SA_CVO~L
