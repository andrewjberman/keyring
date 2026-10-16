# Drive log -- 2.0.0_SA_COO~P2, IRPT_BCKEND, 2026-10-16 03Z to 04Z (30m /canonical-drive, cron 17ff1379)

**archetype:** COORDINATE

| tick (UTC) | limb | act fired | outcome |
|---|---|---|---|
| ~03:12 | EXECUTING; ~PL r3-8 terminal, 4 apply orders pending at IB2 (event-gated) | L8 packet for ~PL rounds 3 to 8 to 3.0.0_SA_CVO~IRPT (@5d90e76797, blob f0310e6f79); sparse-pin check added to IB-pr-605 and IB-pr-611; row D2-S213 | 1 DRIVE FORWARD |
| ~03:42 | same; packet READ by the CVO; IB2 idle-gated | `/next-calls --drive`: found the 49F split pair signed on both halves with no apply order; cut IRPT_BCKEND.TO-IB-pr-612 (Act 1, WORLD, to IB2; check r243, control 27 negatives, 0 unexpected) @b473fcece8; Act 2 deliberately not cut | 2 PARALLELIZE |
| ~04:13 to ~04:23 | CVO slugged ~PL rounds 4, 5, 7 MAY-CLOSE; round 6 NOT MAY-CLOSE (ADJUDICATION_v138: round-close-check refused on the instance NAME of IB-pr-608, my defect); IB2 STOPPED IB-pr-612 at step 1 (row D2-S214: the three performance functions share one S3 key, so a root apply moves the siblings; my signed half's 'siblings unmoved' was a map claim and false) | DECISION to the CTO on the instance names, ruled (msg 9025): renamed both instances under the audited author override, two commits b9b0615637 (~444) and fc80699050 (~446), rename only, VALID, rounds 6 and 8 now MAY-CLOSE; CVO asked to re-grade; IB-pr-612 held and DECISION to the CTO (options a targeted apply, b all three move under an ADDENDUM 2, c separate key; REC b); IB2 told it stays stopped | 1 DRIVE FORWARD |

## Compiler Tools

Run: `drive-mode.py read`, `open-calls.py mode get --part empty_tick`, `unblock.py tick`, `round-close-check.py` (rounds 3 to 8), `proof-of-spec-check.py`, `safe-commit.sh`, `safe-merge.sh`, `wk-provision.sh`. Worked: round-close-check named the instance-name defect that the criteria did not. Failed: a rename inside a worker's deliverables folder (owned-paths lane TREE_DELIVERABLES). Gap: no way for the issuer to correct a name in a worker's folder without the audited override.
