# Window 15 (the Analysis chain, sixth attempt, resident `lt`): READY live -- the first Analysis report

Author `2.0.0_SA_COO~Y`, 2026-09-27 ~17:4xZ. Packet on `51362fca`, both halves signed (CTO @04d670fd75, CRO @6901753e46).
Bounds: at most 2 status GETs per receive, at most 5 receives, 0 read re-captures, at most 1 saved GET; cap 18:03Z.
Word: Andrew at ~Y, "as many analysis attempts as needed" (@460e2ae8cb). Principal `irpt-uiwalk-1790524948`, created by
P at 16:03:44Z (@dc102ceda7). Log: `LIVE_CHAIN_1203_20260927_W15.json` (scrubbed; the password field reads
`<redacted>`).

## The acts

| Time | Act | Answer |
|---|---|---|
| 16:04:50Z | login | 200; "logged in" sent to P (16:05:31Z) |
| 16:06:28Z | password parameter | reads absent (P 101953: ParameterNotFound) |
| 16:06:33Z | K4 upload | 200 RESOLVING, then NORMALIZED at 16:06:36Z, input `portfolio_32fbcd0b..` |
| 16:06:40Z | K5 Overview | 200 QUEUED, `REQ-67e12718b0ba7c0c70ebb45b`; portfolio 2363831, upload record 779777 (2 rows echoed) |

## The resident journal

1. **16:06:34Z** `handled=1`: receive 1.
2. **16:07:03Z** `READ_BACK_RELEASE step=read_back status=200 portfolio_status=calculating source=status polls=2
   wall_s=16.8`, then `retained_for_retry class=ReadBackPending code=READ_BACK_PENDING:CALCULATING`.
   - **Release-and-resume works live** (CTO 101917 (b)): 2 status GETs, both 200 and calculating, with no WAF
     challenge, no re-capture and no ATTENTION.
   - The job row stays SUBMITTING, with its upload and portfolio checkpoints kept.
3. **16:22:09Z** (the redelivery) `READ_BACK_DONE step=read_back status=200 portfolio_status=available
   source=saved_portfolio polls=1 wall_s=3.6 drifted=- absent=- tolerated=level_as_of_type=custom_date`.
4. **16:23:00Z** `handled=1`. The job row went SUBMITTING, then CERTIFYING (16:22:36Z), then **READY** (read at 16:23:23Z).
   The report is `RPT-5288c06d6c9799f5251f3a27632ffc1b` (ANALYSIS), with 7 of 7 settings matched or tolerated.

Bounds, all within the signed packet:
- 2 receives (at most 5);
- 3 status GETs (2, then 1; at most 2 per receive);
- 1 saved GET (at most 1);
- 0 re-captures.

Retained:
- the vendor PDF `ART-ac668d3b..`, sha256 `6e753361..`, 582,765 bytes, 23 pages;
- the extraction evidence `ART-714ae6fa..`;
- `effective_inputs.settings.level_as_of_type = custom_date`.

At READY, D was sent the request for K10 (16:24:24Z) and P was told to delete the principal after that walk (16:24:33Z).

## The level basis (CTO condition 2 fired; CRO's line): `IRPT_BCKEND-S159` (P) and `-S160` (Y, @1a5e710dbd)

- **Stored:** `custom_date`. **Sent:** `prior_close`.
- **The certified PDF's basis:** p.14 "Performance Calculation Settings" reads Static, Quarterly, Earliest, **As Of: Custom**.
- The same page's methodology text says the As Of setting "determines which allocation snapshot is applied throughout the
  historical performance calculation". So ~Y 101938's display-only reason is false; the CTO withdrew it (101971).
- **Control:** the research-era certified PDFs (Sep. 11, a Friday; `opal-data-ycharts research/20260911`, overview
  `abab2ffe..`) also read **As Of: Custom**. Each has 10 "Data as of" lines dated its generation day.
  - Window 15's PDF has 23 as-of lines: Sep. 27 (Sunday, its generation day) x10, June 30 x5, Sep. 25 x4, Aug. 31 x4.
  - That S159's 5 sections would read 09-25 under prior_close is unmeasured: no PDF with another As Of is on record.

## RULED (CTO 101971) and built: the tolerance is narrowed to Static

- Y branch `36837771d6`; `P_STATIC_TOLERANCE_20260927.patch` (sha256 `737aea0b..`).
- The patch is cut against P's `f92445392d` and applies cleanly (apply-check rc=0).
- Its runtime files are content-identical to the proved overlay: extract `719369d5`, resident_worker `9b2dbd18`,
  recipe `982d8171` (a comment-only change on the served file).
- When a read-back row is tolerated, the resident reads the Type the PDF prints in **the portfolio's own row** (selected
  by name) and refuses `TOLERANCE_REQUIRES_STATIC` unless it is Static.
  - It checks this **before the PDF is retained**, so a redelivery has nothing to publish from.
  - The journal line is `IRPT_RESIDENT_TOLERANCE_TYPE type= as_of=`, closed tokens only.

Real PDFs: `calculation_settings` answers as follows.

| PDF | Row asked for | Answer |
|---|---|---|
| window 15, overview, comparison, multicomp | the job's own portfolio | Static / Custom |
| comparison, multicomp | the Opal model rows | Dynamic / Initial |
| any | a wrong or truncated name | None |

Real entry point (`resident_job_preflight.py`):
- the served `lt` tar `ae854f00..` (S3 version `xOjZ..`);
- phase 1 re-run on the served generate zip `G/TqLPdL..` with window 15's input;
- the production census `44853788..`;
- window 15's shape: 2 calculating reads, then release, over 3 deliveries.

| Arm | PDF | Stored | Result |
|---|---|---|---|
| A: `lt` as served | window 15's | custom_date | tolerated, **READY**, 1 REPORT# (reproduces live) |
| B: overlay | window 15's, unchanged (the row names another portfolio) | custom_date | `type=- as_of=-`, **ATTENTION** TOLERANCE_REQUIRES_STATIC; 0 S3 puts, no checkpoint_pdf |
| C: overlay | window 15's, with p.14's 2 name strings rewritten to this job's name | custom_date | `type=Static as_of=Custom`, **READY**, 1 REPORT# |
| D: overlay | C, with p.14's 1 "Static" rewritten to "Dynamic" | custom_date | `type=Dynamic`, **ATTENTION**; 0 S3 puts |
| E: overlay | window 15's | prior_close | no TOLERANCE line, **READY** |

Tests:
- test_calculation_settings 5/5; test_resident_worker, 4 new tests;
- resident suites 55 passed, 8 skipped; test_host_capture 10/10; ruff clean.
- extract/test_publication's 3 committed-variant tests fail on the Y worktree whatever the change, because a docs census
  file is absent there.

**Open:** the saved-GET discriminator the CTO approved (one read-only GET of an advisor-created prior_close portfolio,
in its own packet and halves) has not been run.
