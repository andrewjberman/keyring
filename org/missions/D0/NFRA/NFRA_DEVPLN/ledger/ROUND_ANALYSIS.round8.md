# NFRA_DEVPLN -- ROUND-8 ANALYSIS (1.0.0_SA_CTO, 2026-10-14 ~13:3xZ)

**On:** the issuer's drain end `org/tier1_exec/2.0.0_SA_COO~DV/deliverables/NFRA_DEVPLN_ROUND8_DRAIN_END_20261014.md`
(2 of 2 orders, `round-close-check` MAY-CLOSE, reviewer `3.0.0_SA_CVO~L` present), and the CVO's L10 slug
`surprise-channel/adjudications/ADJUDICATION_v3.md` @4757c9c8da (rounds 3-8, 18 rows, 0 open, 0 ARMED; nothing
graduates; W1-S19 contained by the pre-push hook). **PRD:** v0.3, unchanged.
**Verdict:** every outcome grades REALIZED, so the project is **CLOSED on its outcomes**. One closing repair cell remains
(section 3).

## 1. Grades, FWD-1 to FWD-7

| FWD | grade | evidence (the act, and where it was read) |
|---|---|---|
| FWD-1 | REALIZED | dell2's features followed end to end: candidate branches, Andrew's five approvals (`by=andrew`, ~11:4xZ record), merge-forward to DEV (A14a), then a chosen-set promote (`portal-v2.1.218`, CI 38563449756, five `Approved-By: andrew @dell2-` trailers, `--check PROD` `unapproved=0`). The live bundles carry the shipped strings. |
| FWD-2 | REALIZED | Approve arm: the five dell2 rows, read back by merge-forward. Declined arm: `e89f`, refused by both scripts with DEV unchanged (round 3). Both arms ran on the open-calls list Andrew reads. |
| FWD-3 | REALIZED | A direct DEV push from a box seat was refused, both at the typed-command gate (S03, identical on four boxes, round 4) and at the git hook (payload limb on four boxes, fail-closed, round 6). The same work then landed through merge-forward (A14a). |
| FWD-4 | REALIZED (APPLIED) | Every commit landing on DEV and PROD since the settlement carries its approval trailer, and the per-commit read prints `unapproved=0` at the PROD tip. |
| FWD-5 | REALIZED | A chosen set shipped three times (rounds 2, 6 and 8). Seven unapproved dell2 DEV commits were left behind in round 6. |
| FWD-6 | REALIZED | Settled in round 1 by Andrew's act. The record is `ledger/SETTLEMENT_LIST.md`. |
| FWD-7 | REALIZED (APPLIED) | The line is in `portal/CONTRIBUTING-BOXES.md` and in CLAUDE.md's Portal rule (@fcdfc34843). The gate reads the same classes. |

**Limit on FWD-1's grade, stated, not hidden:** no signed-in client session was used, and the partner-firm route is gated
to DEV. The client hop is graded on deployed code: the served bundle, and the approval trailers on PROD. A rendered
read in a client session would be a stronger instrument. It is not a precondition of the DONE WHEN, which asks that
the feature be followed with its approval read.

## 2. Rulings

- **Whose file is `.tools/hooks/never-rules-gate.sh` (W1-S19)?** The PRD's surface S03 names its portal DEV/PROD limbs
  as one edit with one writer, `1.0.0_SA_CTO`. So this seat removed the FAST-lease and test-only carve-outs itself, under
  Andrew's answer 6 (~11:4xZ) and the CLAUDE.md Portal law. A live lease's seat pushing DEV is now DENIED, and the test
  suite's former positive is a DENY. No path grant to the issuer is needed. The commit is cited in the broadcast.
- **The `DPy1-AC1` amendment** is read and correct. A count on a trunk that other boxes also write cannot be a
  criterion; `unapproved=0` at the resolved ref is.
- **MSTR's deletes of `cand/dell2` refs** were restored at the row-bound shas. A `cand/*` ref is deleted only after its
  feature is on PROD; the issuer's report shows that order is now kept.

## 3. Closing repair (one LOCAL worker-light cell; no new outcome)

1. `.tools/dev_push_payload_gate.py`: the `walk =git(` spacing.
2. `.claude/skills/closer-drive/SKILL.md` step 5 example: `--project NFRA_DEVPLN` becomes `<CODE>`.

Both are DP-j-1's own defects. They are cut as one cell. Its drain closes the project with no further analysis unless
the cell fails.
