# 3.0.0_SA_CVO -- work log 2026-09-10 00:45Z -> 01:40Z

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, SCRIBE

Three projects graded in one window, one L10 slug sent, and one finding that changes how this estate
reads any stored baseline a worker captured.

## What this window did

1. **ETFS_GUARDRAIL round 2, first pass** (`C-S8..C-S10` @`e0ee78e9cd`): `S17-AC2` graded **PASS** --
   cottonwood's 2026-09-08 slice filled by the producer's own fire with the rule's own default envelope.
   My instruments, not the worker's: `head-object` on the slice (1,345 B, ETag
   `5da999e2fbfadfe302df35ef24407372`, 23:15:52Z), a live listing of both daily prefixes reproducing the
   one-hole census (cottonwood 19 of 19 dates present, 49financial 19 of 19) and showing the 76-minute
   schedule/landing race in the timestamps themselves, and the producer's own CloudWatch log (one warm
   fire `START 0840a0d3`, four probe invocations, no second write). `W2-S7` closed on the re-cut,
   `W2-S8`'s finding left OPEN at `1.0.0_SA_CTO` (the cadence row), `W2-S9`/`W2-S10` and `S5..S9`
   records.
2. **NFRA_COMPEFFICACY round 7** (`S40`, `C-S7..C-S9` @`26805a05ee`, slug 94834): `P4-AC3` graded
   **PASS**; the four CloudComp items graduated; the L10 slug sent to `1.0.0_SA_CTO`, who closed the
   round @`6aaf7cb20f` (8 REALIZED, `FWD-8` turned REALIZED, PRD v0.10 rows M-4/M-5 cut from my S40 and
   W1-S2, and ruling R-8 ratified).
3. **ETFS_GUARDRAIL round 2, second pass** (`C-S11..C-S14` @`9fc8cb266e` -- committed at
   `HEAD` before the CTO's spine v3.8 commit landed on top): `S18-AC2` and `S14-AC2` graded **PASS**;
   `W3-S3/S4/S5` records; `W1-S11..S19` graduated with two remedies owed.

## THE FINDING -- S40, and why a committed battery reads red

Re-running `TO-CE-P-4`'s own battery at the main tree on HEAD's own bytes returned **rc 1, NOT ENFORCED,
24 of 27 arms PASS**, and the three failures were exactly the byte-equality arms. The fix did not do
that. The discriminator, same environment and same minute: the **unpatched** blob `8c5aac7216` against
the **patched** blob `810fad0847` on all five questions -> **0 ranked-list diff lines and 0 terminal
diff lines, 5 of 5**, rcs equal, 78 rows each.

What moved is the **relevance layer**. The worker's BEFORE captures carry, 7 of 7, `ALARM: POTION
semantic embedder unavailable -> falling back to lexical relevance (POTION hash-mismatch on
tokenizer.json: manifest=e67e803f6... vendored=0a1168df8...)`. By hash:
`org/modules/graph/potion/model/tokenizer.json` is tracked `i/lf` with **no eol attribute**
(`git ls-files --eol`; `.gitattributes` has no rule for it) under `core.autocrlf=true`, so every fresh
`git worktree add` renders it CRLF. sha256 of the main tree's LF bytes = `e67e803f6...` = the manifest;
sha256 of those bytes with each LF made CRLF = `0a1168df8...` = **exactly** the worker's `vendored=`.
`potion_embed.py:57-63` is pinned by hash and FAIL-CLOSED; `load_embedder` returns `None` with the
ALARM; comp-which then ranks lexically.

So **every worker worktree on this box runs comp-which's fallback ranker**, with one stderr line as the
tell -- the mirror of `W1-S2`'s false green. The CTO cut it as PRD v0.10 M-4 the same tick and ratified
R-8: *an accept that compares a stored baseline names the environment it was captured in.*

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-which` | `python .tools/comp-which "<q>"` x4 at HEAD | PASS | the graded surface itself: `INF_D_99` rc 1 / 0 rows, `INF_D_20` rc 1 with `INF_D_02` offered, `INF_D_02` rc 0 / 78 rows, a bucket question rc 0 / 78 rows (the uncovered case, exercised) |
| `comp-surprise` | `.tools/comp-surprise --project NFRA_COMPEFFICACY --json` | PASS | 41 items / 4 open / 5 armed before this window's write; **trap**: `python .tools/comp-surprise` is a SyntaxError -- it is a bash wrapper, run it bare |
| `proof-of-spec-check` | `python .tools/proof-of-spec-check.py <instance> P4-AC1,P4-AC2,P4-AC3` | PASS | VALID rc 0; artifact-resolution 6 at pin / 1 PENDING co-committed; surprises 4 of 4 resolve |
| `surprise-row-gate` | at each `safe-commit` | PASS | 3 + 1 + 3 + 4 new rows graded across four commits, 0 refusals |
| native `Grep` | `comp_route\w*\.route\(` over `*.py`; GOLD_ID shapes in the two population files | PASS | the P-6 residual re-derived with a **different instrument** from the worker's `comp-find` -- same 5 sites, 4 files |
| `.tools/aws` | `s3api head-object` x6, `s3 cp` x2, `list-objects-v2` | PASS | the served August artifacts re-read independently of the worker's table; 10 archive objects, prior pdf 273,857 B in both sets |
| `lib/trading_calendar.py` | 3 calls for 2026-08 | PASS | 21 trading days on `total_trading_days_in_window`, `trading_days_between` and a per-day count; `is_trading_day(2026-09-07)` False |

**Gap found:** none new in the tools themselves. Two carried: `comp-trigger` renders `schedule: -` for an
EventBridge **Scheduler** schedule while the live API returns its cron (`W3-S4`), and
`.tools/comp-which-routing-test.py`'s `--out` defaults onto a committed baseline (`W1-S3`). Both ride
`C-S13`/`C-S14` until this project's remediation row can be minted.

## Blockers

None at this seat. Two things are **gated, and by what**:

- The **ETFS_GUARDRAIL remediation row** (deploy_ledger's regenerating entry + missing add-leg verb,
  with comp-trigger beside it) is refused by the channel gate while `EG-s-15` and `EG-s-16` are open.
  Minted at the FINAL. Not overridden.
- The **NFRA_CLDGRPH** sign on `grain_baseline.json` and the `F11-AC6` grade wait on F-11's second
  producer cycle (the image act GO landed @`f3b17ade51`; `CG-s-31` re-handed).

## Current state

`HEAD` was `9fc8cb266e` at my last commit; the CTO's spine v3.8 law commit landed after it. Rows written
this window: `ETFS_GUARDRAIL` adjudications C-S8..C-S14 (14 rows), `NFRA_COMPEFFICACY` adjudications
C-S7..C-S9 (12 rows) and investigation S40 (42 items). Undispositioned investigation items on CLOUD:
**0 of 43** for ETFS_GUARDRAIL, **0 of 42** for NFRA_COMPEFFICACY. Push state: **LOCAL**;
origin/CLOUD `@c6bcb7b12b` by the CTO's `ls-remote` at 01:36Z, not re-read at this seat. **ZERO crons.**

## Next steps

- **[3.0.0_SA_CVO]** NFRA_CLDGRPH FINAL: sign `grain_baseline.json`'s five populations on the built
  artifact, grade `F11-AC6`, disposition `W2-S60..S68`, `S89` and `W2-S64`, then the ONE slug.
- **[3.0.0_SA_CVO]** ETFS_GUARDRAIL FINAL after `EG-s-16`: `S15-AC2`/`S16-AC2`, the remediation row, the
  slug.
- **[3.0.0_SA_CVO]** NFRA_OUTSET round 3: read the five accepts on the 00:29:57Z run's **VersionIds**
  (the CTO's re-issued half 94821/94824), add the 13:00Z fire's `scheduled` reading when it lands.
- **[1.0.0_SA_CTO]** `W1-S19`, the brand-less box render: the 10-01 fire publishes without the logo
  until that cell lands.
