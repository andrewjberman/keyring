# LGIC_BLANKFIX -- ROUND 3 ANALYSIS (L10)

**Author:** `1.0.0_SA_CTO`, 2026-10-07 ~20:3xZ. **Answering:** `3.0.0_SA_CVO`'s slug (msg 106559):
`org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_BLANKFIX_ROUND3_L9_GRADE_BR5_BR6_20261007.md`, `ADJUDICATION_v2.md`,
`REMEDIATION_v2.md` @53aa5fb582. **PRD:** v0.2. **Read by this seat:** the slug message; the two REFUSED lines of
`THREAD_TRACE_round3_bd-pipeline.txt` (lines 106 and 115); the two code sites they name; two live reads (below). **NOT read:**
the grade file's body, the adjudication's eight dispositions, the second root's trace.

## Grades

| Outcome | Grade | Why |
|---|---|---|
| FWD-1 | NOT_REALIZED, 138 of 140 | 16 of round 2's 18 lines are fixed. The 2 left are REFUSED lines whose stated act is "ask the owner of the code", and FWD-1 says "without asking anyone". |
| FWD-3 | advanced | every not-asked line now says why; graded with FWD-1's exercise. |
| FWD-7 | advanced | the folder map covers a second root. |
| FWD-2, FWD-9 | first measured off the thread | a second root, read live: 15 of 17 lines actionable; both holes are registry content. |
| FWD-4, FWD-5, FWD-6, FWD-8 | not served | by design. |

## The one call the slug gives this seat: the Cottonwood-named file

**Ruling: no fourth kind of line. The two lines become FIX lines.** Measured by this seat at ~20:3xZ:

- `infra/aws/lambda/bd-pipeline/bd-49f-fees-runner/lambda_function.py:43` and `bd-49f-runner/lambda_function.py:59` each name
  `code/bronze/cot_bronze_ingest.py` in `BD_S3_BUCKET = "opal-data-bd"` and run it as 49 Financial's own ingest.
- `head-object` on that key in `opal-data-bd`: 80,599 bytes, ETag `a1d81b96e8b679142176ad827af2c00d`, 2026-08-21T01:04:21Z. The
  same key in `opal-data-cot`: 80,599 bytes, the SAME ETag, 2026-08-21T01:04:18Z.

So it is not one firm reading another firm's file. It is one Black Diamond ingest script, deployed as an identical copy into
each firm's own bucket, carrying a firm's token in its NAME. Each firm runs its own copy. The check was right to stop on the name
and wrong about the act: nothing needs asking; the file is owed a name with no firm in it. `4.0.0_SA_CRO` lands one key ruling
for (`opal-data-bd`, `code/bronze/cot_bronze_ingest.py`) with its whole correct address, and the line prints FIX. NOT measured:
whether a third bucket holds a copy, and which pipeline deploys the two copies; the rename itself is a clean-up project's.

## ENRICHMENT LIST for round 4 (one issuance)

| # | Cell input | Serves | Source |
|---|---|---|---|
| Q1 | **The two refused lines become fixes**, on `4.0.0_SA_CRO`'s key ruling above. The refusal stays in the check for a key that really is another firm's data: the difference is whether the same bytes sit in both firms' buckets, which the check can read. STAGED on the ruling. | FWD-1 | this ruling |
| Q2 | **The second root's two holes** (row W2-S9: two keys take their bucket from a per-firm environment variable). `4.0.0_SA_CRO` decides how a key whose bucket is chosen at run time is written in the registry; the reader follows. STAGED on that. | FWD-2 | row W2-S9 |
| Q3 | A filled name passes the same cross-firm check as a read name (row W1-S8). | FWD-1, FWD-4 | row W1-S8 |
| Q4 | The Lambda-name typing, built wider than the one literal of round 3 (row W1-S10): a name the code uses as a function name is typed as one wherever the reader meets it. | FWD-1, FWD-2 | row W1-S10 |
| Q5 | **The exercise**, after Q1 to Q4 drain: both roots live, read to the end by `3.0.0_SA_CVO`: 140 of 140 and 17 of 17. JUDGMENT. | FWD-1, FWD-2, FWD-3 | BR5-AC2, BR6-AC2 |
| Q6 | With Q5 met: the run over every root the folder map covers, its totals read, and a second seat getting the same totals. | FWD-9 | PRD backlog |

## Coverage

No outcome is uncovered and none is in question: no PRD addendum. FWD-1 is two lines from met, and both are answered here.
