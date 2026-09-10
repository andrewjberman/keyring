# 0.7.0_AE_CloudOps~W -- 2026-09-10 12:20-15:00Z -- NFRA_OUTSET round 3

**archetype:** MIXED

## What this session was handed

Six pending task orders (`OS-s-20, 21, 22, 23, 24, 26`), none with a `proof_of_spec` instance, and
an instruction to **measure each artifact before re-executing anything** (NEVER-2). A seventh
(`OS-s-27`) was cut mid-session on a row this seat filed.

## Outcome

**Five orders TERMINAL, two open at exactly one arm each.**

| order | state | commit |
|---|---|---|
| `TO-OS-s-20` | TERMINAL | `789aba9d2a` |
| `TO-OS-s-21` | TERMINAL | `835f298bba` |
| `TO-OS-s-24` | TERMINAL | `c6a85cfb5a` |
| `TO-OS-s-26` | TERMINAL | `0a5b6f435e` |
| `TO-OS-s-27` | TERMINAL | `20d5c41567` |
| `TO-OS-s-22` | OPEN, 5 of 6 arms | `5c8a35aba4` |
| `TO-OS-s-23` | OPEN, 6 of 7 arms | `5c8a35aba4` |

Six batteries written, one corrected; six proof instances written and VALID; two deploys landed
under NEVER-2 entries opened before the act; seven surprise rows filed (`S38`-`S44`, minus the
CTO's `S42`).

## The two deploys

1. **The S36 disclosure arm** (`0d5c4f083f`, uploaded 12:55:13Z). Landed **five minutes before the
   13:00Z fire**, so today's scheduled run is the first served day carrying it. Ledger
   `20260910T1250Z`, four legs verified.
2. **The stratum-string serialization** (`22ca10d25e`, uploaded 14:15:40Z), `TO-OS-s-27`. Ledger
   `20260910T1412Z`, four legs verified, backfills nothing.

## What the 13:00Z run settled

Group B moved `INSTRUMENT_FAILED` -> `OK`. Because that chain advances only on `absent=True`, which
only the `FileNotFoundError` arm sets, which only a 404 reaches, **one read proved two things**: the
exact-key grant is EXERCISED (the CTO's residual, retired) and the 12:55Z runner deploy landed.

## The findings that were not about the estate

⛔ **THREE OF FOUR FAILURES IN ONE BATTERY WERE MINE.** `test_os24` read mutable keys at `latest` in
three arms. All three **passed when written** on 09-09 and became wrong on 09-10 with no line
changed -- the 12:30Z build re-published two seam keys and the 13:00Z fire replaced the token. **The
arms did not break; the world moved past them.** Row `S44`. The fix is to SELECT (the version
preceding the run start; the token whose `run_id` matches), never to pin a literal.

⛔ **A GREEN ARM WITH A FALSE SENTENCE.** `test_os23` arm (a) looked for a field the artifact does
not carry, got `None`, skipped its own comparison, and printed *"equal to the artifact's own
declared row_count"*. An absent field must never be read as agreement.

⛔ **I CORRECTED MY OWN ROW BEFORE ITS REMEDY WAS BUILT.** `S40` said both blocked clauses lived in
the stratum's denominator. `S41`: the grain tag lives on the **vintage** (`:1425`, one line below
`:1424`). A denominator-only fix would have closed one clause of two and looked complete. Both the
COO and the CTO verified all three of `S41`'s mechanical claims at source.

⛔ **A WRITE THAT SELF-REPORTED SUCCESS WHILE FAILING.** `Set-ScheduledTask -Principal` returned
*Access is denied*; the wrapper printed `SET-OK` anyway (non-terminating error). The **read-back**
caught it. The discriminating control -- a SETTINGS write on the same task in the same session
succeeding -- is what attributed the denial to the PRINCIPAL rather than the task. And that control
itself reverted two battery flags to cmdlet defaults, caught only by reading the object back. Rows
`S38`/`S39`.

⛔ **AN ID COLLISION.** I minted `S42` from a read taken minutes earlier while the CTO's own `S42`
landed at HEAD. Renumbered mine to `S43` by rewriting exactly one id inside my own block. The row
gate printed OK because it grades **STAGED** rows and neither was staged.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-find` | `--name 'NFRA_OUTSET.TO-OS-s-*.md' --all --limit 40` | 26 hits / 157,934 files. Resolved the task-order set after a `tier2_senior` glob returned zero -- that zero was OUT-OF-CORPUS for the tree layout, not absence. |
| `comp-find` | `--name 'estate_report_runner.py' --all --limit 10` | 1 hit / 157,955 files. Exactly one runner in the repo, so the BUILD INPUT for the deploy comparisons is unambiguous. |
| `comp-find` | `'stratum_status' --all --limit 30` | 135 hits / 154,114 files, banded SURFACED 44 / CONFIG 38 / TEST 17 / DOC 36. **Surfaced a SECOND producer of the group-block shape nobody had counted** (`kimi_pipeline.py:650/:681/:852`) -- row `S43`. |
| `comp-read` | runner `--enumerate 'grain=\|resource-grain\|grain_note\|GRAIN'` | 10 hits / 3,181 lines. Put `:1424` beside `:1425` and **caught the wrong mechanism in my own row `S40`** before the issuer cut a remedy from it. |
| `comp-read` | runner `--enumerate 'comp_heat_freshness_tools\|freshness'` | 17 hits, **none the key name** -- the consumer does not read that key at all, which stopped `test_os21` asserting a link the cell never built. |
| `comp-read` | runner `--enumerate 'stratum_status\|"groups"\|groups_unmeasured'` | 19 hits. Found the two assembly sites to touch AND the third at `:3084` NOT to touch, which is why the manifest side effect is disclosed rather than discovered later. |
| `comp-read` | runner `--enumerate 'NoSuchKey\|FileNotFoundError\|_outset_loader\|ClientError'` | 12 hits. Showed the loader had NO `NoSuchKey` arm -- the reading that drove the whole disclosure design. |
| `.tools/proof-of-spec-check.py` | 6 instances | All VALID rc=0. Refused three instances first on real defects: a string `decomp_ref`, `PENDING-THIS-COMMIT` on already-committed paths, and an artifact row naming a (commit, path) pair git refutes. |
| `.tools/commit-gate.sh` | every `.py` edit | Blocked 4 times on ruff (unused imports, unused variables) and once on `ds-precommit` (`undefined name 'st'`). All real. |
| `.tools/surprise-row-gate.py` | at each row commit | OK each time -- **and its OK is vacuous for an unstaged row**, which is how the `S42` collision passed it. |

**Gap found:** the surprise-row gate grades only STAGED rows, so it cannot see an id collision
between a worktree row and one that landed at HEAD. The discriminator is a HEAD-versus-worktree
count, which no gate runs.

## Blockers

**None at this seat.** Two orders wait on the 2026-09-11 13:00Z fire, and that wait is qualified:
a manual run now would rewrite today's served keys (the `S34` act), which `TO-OS-s-27`'s own bound
forbids. One item is parked with Andrew by design -- the S4U re-principal (`S39`), an elevated line
no agent session on this box can run.
