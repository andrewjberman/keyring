# ROUND 1 ANALYSIS -- NFRA_OUTSET

**Seat:** `1.0.0_SA_CTO` (L10, the CTO's one send) · **Stamp:** 2026-09-05 ~20:1xZ
**On the slug:** `surprise-channel/remediations/REMEDIATION_v1.md` + `adjudications/ADJUDICATION_v1.md`
@`4fa04aaf4c` (`3.0.0_SA_CVO`, msg 94392) · **Completion report:** `2.0.0_SA_COO` @`a483609584`

---

## 1. The coverage read -- and it does NOT come out clean

Every endpoint outcome is served by a cell, and every cell that was cut passed its bar. **The round is not
short a cell. It is short a SURFACE**, and the surface is one this PRD's own §3 named and then failed to
place.

`3.0.0_SA_CVO` measured it: the SERVED estate-report runner (125,857 B, dated **2026-08-25**) carries **0** of
`_outset_read` / `OUTSET_ANSWER_STATE_TO_STATUS` / `tool_row_cited`, against **4 / 3 / 7** at HEAD. One hop
further in, nothing publishes to the consumption seam and the runner's role holds no grant on any seam prefix.

So **FWD-2, FWD-3, FWD-4 and FWD-7 cannot grade REALIZED on a served day**, whatever their cells passed. That
is the ETFS_GUARDRAIL correction arriving on a second project within a day, and the CVO applied it here from
its first grade rather than waiting for this analysis to impose it.

## 2. THE DEFECT IS IN THIS PRD, AND IT IS THIS SEAT'S

§3 of this PRD chose the artifact-shape consumption seam and stated its cost in these words:

> **The cost, stated:** a publishing step and a freshness question per artifact — an artifact that fails to
> publish must read as FAILED in the report rather than as an absent section, **which is exactly what FWD-5's
> acceptance already demands, so the cost lands on a limb the PRD already carries.**

**That sentence is the defect.** The cost was correctly IDENTIFIED and then assigned to an ACCEPTANCE LIMB
instead of to a MANIFEST ROW. A cost on an acceptance limb is a claim about how something will be GRADED. A
cost on a manifest row is WORK SOMEBODY DOES. §7's own header calls the manifest "the handoff, not an
appendix" — and the publishing step never entered it. Neither did the S3 upload that deploys the runner:
`S14`, `W1-S25`, `W1-S26` say that upload **belongs to no cell**.

⛔ **THE GENERAL FORM, which is what the next PRD needs and what this round earned:** a PRD that COSTS a step
and does not PLACE it lets a project pass every criterion it was cut for **while the thing the estate actually
reads is unchanged.** Naming a cost is not assigning it. The test is mechanical and belongs at L4: *for every
step this PRD's architecture section costs, which manifest row owns it?* — and a step whose answer is "an
acceptance limb" has no owner.

This is not the issuer's defect and not the workers'. The cut was clean against the manifest it was given, the
workers passed their bars honestly, and eight of thirteen wrote the limit of their own claim beside the pass.
**The manifest was wrong before any of them saw it.**

## 3. The answer: a PRD ADDENDUM, not merely this analysis

Under the spine, L10 answers with an addendum when an outcome no cell served is found. The variant here is
narrower and worse: outcomes ARE served, and the SURFACES that carry them to a served day are not. The
addendum lands as `prd_version` v0.2 → **v0.3** with two rows added to §7:

| id | outcome_ref | surface | claim | lane | verb | accept |
|---|---|---|---|---|---|---|
| `OS-s-18` | FWD-3 | the PUBLISH: an outset tool's artifact reaching the consumption seam, and the runner's role granted to read it | **absent** — nothing publishes; the role holds no grant on any seam prefix (W1-S19, W1-S20, W2-S15) | CloudOps | build | one artifact per outset tool is readable at the seam by the runner's own role, and a failed publish reads FAILED |
| `OS-s-19` | FWD-2, FWD-4, FWD-7 | the DEPLOY: the single S3 upload that puts the runner the estate reads at HEAD's version | **absent** — the served runner is dated 2026-08-25 and the upload belongs to no cell (S14, W1-S25, W1-S26) | CloudOps | deploy | the served runner's bytes match the graded commit's, read by head-object and a content diff, with a NEVER-2 ledger entry |

Both are `CloudOps` lane and neither is a worker's: an S3 deploy and an IAM grant are cloud acts, which is the
same boundary that sent `OS-s-6` and `OS-s-7` to that lane at the original cut.

## 4. Grades

`dep_stage` **EXECUTING → ROUND_CLOSE**. Not CLOSED: FWD-2, FWD-3, FWD-4 and FWD-7 grade **NOT_EVALUATED** on
the served plane, and they become gradable only when `OS-s-18` and `OS-s-19` land. R6 refuses CLOSED until
every grade is REALIZED, and it is right to here — **the estate reads a runner from eleven days before this
project started.**

## 5. What the round is worth recording for

- **COMMITTED IS NOT SERVED**, and it is now the second project in one day where cell PASS and outcome
  REALIZED came apart. On ETFS_GUARDRAIL it was a promise awaiting a real event; here it is code that exists
  and is not running. **Both are the same axis of Rule 22 and neither was visible from the cell's own bar.**
- **The workers wrote the limit of their claim beside the pass on eight of thirteen graded criteria**, and the
  CVO made the limit part of the grade. That is the habit that let this finding surface at L9 rather than at a
  user's first confused morning.
- **`S3` and `S14` are this seat's**, along with nine other routed items; they are carried into this seat's
  queue rather than left in the row.
- Two corrections the CVO volunteered about a commit message it could not amend are noted and believed: the
  document text is right, the message's rider and push state are stale, and a three-file commit that timed out
  at 5 minutes is why. **A commit message is not amendable and a document is — say which one is wrong.**

## 6. Next

`2.0.0_SA_COO` recuts from this analysis: two rows, both CloudOps, no worker fan-out. Nothing here returns to
Andrew.
