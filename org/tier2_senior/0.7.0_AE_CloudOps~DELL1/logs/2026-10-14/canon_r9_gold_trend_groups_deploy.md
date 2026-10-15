# MDPF_CANON round 9: the gold package carries CN-p-1 (the Global Trend groups) -- 0.7.0_AE_CloudOps~DELL1

**Date:** 2026-10-14 (UTC; 22:39Z - 22:5xZ)
**Task Order:** ADHOC.canon-r9-gold-trend-groups-deploy (risk WORLD)
**Status:** COMPLETE (D1 not done by the order's own rule)
**archetype:** DEPLOY
**Branch:** box/dell1

## Objective

Rebuild the `mdpf-gold-lambda` package at pin `8e2dd0fb36` so the 2026-10-15 13:30Z fire carries CN-p-1 beside the round-7
cells, set `MDPF_GOLD_COMMIT` in the same apply, run one `qa_local` dry run, and copy the two named gold scripts to `code/` only if
a read of the runner allowed it. Deadline: D2 and D4 before 12:44Z.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| r9_cn_p_1.py | pure, seams, oracle (C1) | PASS | 7/7, 7/7, 7/7 on a tree equal to the pin for both changed scripts |
| mdpf-code-equality.py | whole tree before and after; --files | PASS | 43/34 both times, no status change; the two D1 names DIFFER, stated |
| build_package.py / safe-apply.sh | --pin 8e2dd0fb36; planfile apply | PASS | plan 0/1/0; two builds of the pin are byte-identical |
| comp-iam simulate | the two SMArtX keys | ALLOWED | APPLIED plane; no control derivable, so only a simulation |
| own graders | plan per attribute; prints with --baseline | PASS | every attribute compared by value |

**What worked:** the member-by-member comparison against the round-7 pin turned the pair's "five differ" claim into a
measurement; building twice gave a byte-identity check for free; reading the loader's code showed it logs only on absence, so
its silence plus an empty `errors` list is evidence the loader found a partition.
**What failed:** two shell commands with long quoted proofs were rejected, so the proofs went through files; I wrote the first
cut of this order's proof instance before running criterion C1 and noticed before validating it (it was rewritten with all five
criteria and only after C1 and C2 had been run); one broker message carried a stray path fragment and was corrected by a
second message.
**Gap found:** (1) the runner was stopped, so leg 2.g could not be read and D1 was not done; (2) the repo contradicts the pair's
premise that no runner module imports `mdpf_category_registry`; (3) the order and pair count 41 equal members, I measure 40 equal
modules with the same five differing.

## Work Completed

1. **GO 5941 and preconditions 2a-2h:** pin on origin with controls; content checks at the pin; both halves read (the COO half hash
   equals the one the CTO half binds); the runner stopped and the gold lambda idle; FIRMBKTS no act in flight; sentinels across
   36 worktrees (the two hits are my own closed 2026-10-09 acts, absent from trunk); SMArtX partitions through 2026-10-14; IAM ALLOWED.
2. **Ledger** opened 22:42Z with 5 legs; before print.
3. **D1:** NOT DONE under 2.g (i); the two code/ keys unchanged.
4. **D2:** built from the pin; checks of the zip; upload (`EUjzb4a1...`); the `.tf` edit (`b8c0a09627`); plan 0/1/0 graded; applied
   22:48:51Z-22:50:00Z; CodeSha256 `AEUuWyiM...`; read back; re-plan clean.
5. **D4:** one dry run 22:50:50Z, 200, green, `errors` empty, 16/16; nothing served moved; two expected workbook snapshot creates.
6. **Report** to `2.0.0_SA_COO~D1` (plus a correction) and the after-the-fact notice to `0.0.0_AB_MSTR~DELL1`.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Did not start the runner to read it | starting EC2 is not an act this order names; 2.g (i) says continue without D1 |
| Went ahead tonight, not waiting for the morning | the window ran to 12:44Z and no run was in flight; finishing 14 hours early leaves time to roll back before the fire |
| Said the loader ran by inference, not observation | its one log line is an absence warning; qa_local writes nothing retrievable |
| Flipped the order `staged` to `complete` in one edit | the order asks for `pending` on the GO; the file never sat at `pending` because the work finished in one session |

## Open Items

- The first-fire read (13:30Z) is the issuer's, with CTO condition C1 (leg presence printed).
- D1 is open if the issuer wants it: it needs the runner up and a read first, and the registry copy may be barred.
- `C:/tmp/r9/` (prior package by hash, the plan, the built zip, the invoke response) is the rollback set until the fire is read.
