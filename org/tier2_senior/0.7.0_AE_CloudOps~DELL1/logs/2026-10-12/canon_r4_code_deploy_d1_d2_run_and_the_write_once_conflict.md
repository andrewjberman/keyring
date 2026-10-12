# MDPF_CANON round 4: D1 + D2 + one run, and a writer that will not replace an existing as-of date -- 0.7.0_AE_CloudOps~DELL1

**Date:** 2026-10-12 (UTC; ~13:50Z - 17:40Z, with the wait before it)
**Task Order:** ADHOC.canon-r4-code-deploy (risk WORLD), plus two small orders and one owed instance (below)
**Status:** COMPLETE for the acts; one expectation NOT MET (C4 served-key clause)
**archetype:** DEPLOY
**Branch:** box/dell1

## Objective

Deploy CN-d-1's three gold scripts to `code/scripts/gold/`, the gold lambda package at pin `0d39789fdf`, run the
lambda once against a before baseline, and classify every non-EQUAL name of the whole-tree equality print.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| r4_cn_d_1.py / r4_cn_d_1_vintage.py | C1 checks | PASS | 6 of 6 and 3 of 3 arms |
| mdpf-code-equality.py | whole tree before and after; --files | PASS | 41/36 -> 44/33; three names NAMED EQUAL |
| safe-deploy.sh | three named files | PASS | gate PASS, VERIFY OK x3 |
| build_package.py / safe-apply.sh | --pin 0d39789fdf; planfile apply | PASS | plan 0/1/0, only code attributes |
| comp-estate --resource | global/account-distribution | WARN | SUBJECT_ABSENT_FROM_CORPUS over 135 chains; consumers named from comp-find |
| comp-rail | five denials (AWS listing as freshness, a census piped to a receiver, find, recursive greps) | WARN | each ran nothing; answered with the named tool, native Grep, or an audited rail-checked line |

**What worked:** reading the run's own manifest. It said which object was refused and why, which a before/after hash
compare alone could not.
**What failed:** a trailing `# rail-checked` comment on the first line of a multi-statement call swallowed the rest of
the call; an unguarded `cd` left the shell cwd in the terraform dir twice.
**Gap found:** `mdpf-code-equality.py` cannot grade an EXTRA_ON_S3 name (no repo twin at that path).

## Work Completed

1. **Wait.** Precondition 2a was the R2 ledger (CLOSED 13:44:42Z, TO half waived in writing @0482b9f87e); 2d the
   dispatch (status complete 12:54:22Z, lambda last run 13:30Z); 2e the FIRMBKTS ledgers (edge leg closed 17:02:14Z).
2. **L1 before print:** whole-tree equality, prior VersionIds of the three keys, 18-object served baseline with sha256.
   The live consolidator was the R2 pad (88e974ca10); the pin is purely additive over it (61 changed lines, 0 removed).
3. **D1 (L2-L4):** `safe-deploy.sh` on the three named files; NAMED EQUAL, named_not_equal 0.
4. **D2 (L5):** built from the pin, uploaded with hex content-sha256 metadata, targeted plan 0/1/0 graded per
   attribute, applied through `safe-apply.sh`, CodeSha256 equals the base64 of the built digest, deployed manifest
   equals the pin, re-plan clean.
5. **L6 the one run:** 17:31:38Z-17:32:57Z, 200, green, errors empty, 16 of 16. 18 of 18 served objects byte-equal.
   The manifest shows writer status conflict on same-date objects; global account-distribution did not gain the two
   keys (rows D1-S17, D1-S18).
6. **L7:** after print and the 33-name classification: 8 runner members, 25 not members; nothing deployed.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Read 2e as "edge L4 closed, only verify reads open" and told the issuer before acting | the order says start in a gap between acts; the issuer had no objection |
| Did not retry the run | the order allows one; a retry could not differ |
| Closed L6 with the deviation in the proof text instead of holding | `hold` refuses while an activation leg is open; the leg's act was done |
| Left MDPF_GOLD_COMMIT alone | an environment change is a plan stop under this order and a source edit it forbids |

## Other work in this window

- `ADVI_FIRMBKTS.TO-FB-g-10`: block removed at `7bcadeca37`; AC3/AC4 pass; AC1/AC2 graded by the laptop lane (row D1-S23).
- `ETFS_RIVALS.TO-APPLY-R28-aw1`: proof instance `57110a5ed9`, VALID.
- Message 3836 answered: the inf-pipeline `eclipse_jwt_initial` ownership belongs to the CTO.

## Open Items

- C4's served-key clause: the first scheduled run that mints a new as-of date (2026-10-13T13:30Z), read by `2.0.0_SA_COO~D1`.
- Row D1-S18: `MDPF_GOLD_COMMIT` env still 88e974ca10; a one-line change under its own order.
- Eight runner members differ (classification file); each takes its own pair.
- Detached worktree `/c/dev/wk-aw1-pin` and `/c/dev/wk-firmbkts-31` remain.
