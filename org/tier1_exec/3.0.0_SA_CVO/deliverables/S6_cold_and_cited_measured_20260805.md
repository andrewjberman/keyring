# S6 — COLD *AND* CITED is computable, and the 08-04 reversal was not a near-miss. It was 84%.

**Seat:** `3.0.0_SA_CVO`, SIGNAL half of the comp-tool split @7a3e7117d. **S6 scope:** verify the
cold-AND-cited cell is computable — the cell that reversed the dated-briefs archive on 2026-08-04.
**Verdict: COMPUTABLE. Measured below.**

## The two halves, and both exist today

| half | tool | emits |
|---|---|---|
| **COLD** | `comp-heat freshness --json` | 23,039 files scanned · hot 1,352 / warm 4,931 / **cold 16,757** · 1,125 cold subtrees, each with `n`, `n_cold`, `cold_frac` |
| **CITED** | git-tracked corpus scan | 22,240 files read of 22,382 outside the subtree (142 skipped >400KB) |

`comp-heat` ranks `docs/briefs` as its **#2 cold subtree** — 490 files, 427 cold, 87% cold. On
coldness alone it is one of the most archivable directories in the estate.

## The measurement — and it inverts the archivability verdict

```
COLD files under docs/briefs .............. 403
  >> COLD *AND* CITED .................... 338   (84%)   DANGEROUS TO ARCHIVE
  >> COLD AND UNCITED ..................... 65   (16%)   safe-archive queue
  of the cited, referenced from PRODUCTION LAMBDA SOURCE ... 14
```

Named production citations (basename appearing inside a live Lambda source file):

| brief | cited from |
|---|---|
| `bd-49f-interim-cookie-solution-rest-api-20260625.md` | `infra/aws/lambda/bd-pipeline/bd-49f-keepalive/lambda_function…` |
| `cot-har-auth-api-first-analysis-20260608.md` | `infra/aws/lambda/cot-pipeline/cot-bd-session-trigger/lambda_…` |
| `aws-cost-audit-deepverify-20260605.md` | `infra/aws/lambda/ec2-auto-shutdown-enforcer/main.tf` |
| `macro-may-blank-june-filled-rootcause-20260601.md` | `…/yang_pipeline/macroeconomics/yang…` |
| `bmkaud-ws3-methodology-walkthrough-20260601.md` | `…/yang_pipeline/portfolios/yang-model-portfolio-benchmarks…` |

**The last two are the briefs the 08-04 reversal named by hand.** They are not exceptional — they are
2 of 338.

## Why this matters more than the incident did

On 2026-08-04 an archive of the dated briefs was ratified, then reversed mid-flight when someone
measured citation-liveness and found several cited from production Lambda source. That read as a
**close call caught by diligence.**

**It was not close. 84% of that cold subtree is cited.** Archiving on coldness alone would have
broken 338 citations, 14 of them from code that runs in production. The reversal was not a lucky
catch on a handful of files; the archive premise was wrong about five-sixths of its own target.

**And the mechanism generalises past this directory:** *coldness measures WRITE recency; archivability
requires READ liveness.* They are different axes, and `comp-heat` measures only the first — correctly,
and it says so (`ADVISORY-ONLY`). The defect is not in the tool. **It is in treating a cold-subtree
list as an archive queue**, which is exactly what a "cold subtrees (archive candidates)" label invites.
*Name-pattern is not a deadness predicate; neither is write-age.*

## Honest limits of this measurement

- **Basename substring matching is CRUDE.** It can false-positive on a coincidental occurrence, so
  **338 is an UPPER bound on citation** — and symmetrically **65 is an upper bound on safe-archive**,
  since a reference in a path form my matcher missed would move a file the other way. Neither number
  is exact; the *direction* is not in doubt at 84%.
- **The 14 production-Lambda hits are the high-confidence subset** — a dated brief's basename
  appearing inside Lambda source is very unlikely to be coincidence.
- **Denominators stated:** 16,757 cold of 23,039 scanned; 22,240 of 22,382 corpus files read.

## Recommendations

- **R-S6-1 (P1):** the cell should be a **standing capability, not my ad-hoc script**. Whichever tool
  owns it, the output must carry both counts and the production-citation subset — a cold list without
  its cited-fraction is an archive queue with the safety interlock removed.
- **R-S6-2 (P2):** `comp-heat`'s `cold_subtrees` label reads as "archive candidates." Recommend the
  emission itself state that coldness is WRITE-recency and says nothing about READ-liveness. The tool
  is honest at the tool level; the field name is what misleads at the consumer level.
- **R-S6-3 (P2), found in passing:** `cold_subtrees` is contaminated by vendored dependency trees
  (`…/pyiceberg-nessie-deps/python/pygments/lexers`, `…/openai/types/responses`, plus `__pycache__`
  dirs). Same denominator-contaminant class as the co-movement bookkeeping I excluded in S3
  @d7d3b6fab, and the same remedy shape: a **declared** exclusion list, reported.

**S6 CLOSED as scoped** — the cell is computable, and the measurement is decision-useful today.

-- 3.0.0_SA_CVO
