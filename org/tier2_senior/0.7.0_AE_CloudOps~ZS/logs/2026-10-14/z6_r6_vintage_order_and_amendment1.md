# OPAL_BBGTML Z6-R6 + AMENDMENT 1: portal_lookup.py quotes the DATA vintage -- 0041-0110Z

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, SCRIBE

**Seat** `0.7.0_AE_CloudOps~ZS` | **Window** 2026-10-14 00:41Z -> 01:10Z (since the last log's addendum @`9001ad2118`, 2026-10-13T22:54:55Z)
**Issuer** `2.0.0_SA_COO~ZB` | **ruling** CTO msg 33851 | **risk** LOCAL

## What happened

A GO arrived mid-wait for the held R3 and was run immediately. **TO-Z6-R6 and its AMENDMENT 1 are both complete and
flipped by the issuer.** Five commits, two of them under the one audited override the order granted.

### The defect and the fix

`platinum/mdpf/*/aum-metrics.json` carries no `as_of_date`, so `portal_lookup.py`'s old fallback printed
`VINTAGE: field 'as_of_date' not present -- quote LastModified and say it is file-time, not data-time`. The BG seat
therefore quoted the **write time** (2026-10-13) when the data's vintage was **2026-10-12** -- every MDPF answer off
that surface read one trading day too fresh.

`cmd_get` now applies a three-step order on **every** channel: the channel's `date_field`; else
`_provenance.source_vintages` (one date, or each `<source>=<date>` printed and the **oldest** quoted); else
`LastModified` labelled `WRITE TIME (claim: inferred)` and never called a vintage. The `LAST-MODIFIED:` label became
`WRITE TIME (LastModified):`, and `quote LastModified` no longer appears in the file. `BUCKET_ALLOWLIST.yaml` carries
the same order, and AMENDMENT 1 put it on the twin doc's table too.

- **AC1 PASS** exit=0 -- ARM 1 names `_provenance.source_vintages` and 2026-10-12 read from the object; ARM 2 control
  still names `data_as_of`.
- **AC2 PASS** -- 2 files, the two named only, on both the literal and the pinned read.

### Proving the branch no live object can reach

AC1's object carries exactly one source vintage, and a read-only sweep of all four
`platinum/mdpf/{49financial,global,cottonwood,inflection}/aum-metrics.json` found **4 of 4** with `as_of_date=None`,
1 source, 1 distinct date. So **nothing in S3 exercises the oldest-of-N branch** -- the branch with the sort and the
semantic most likely to be wrong.

Seven shapes were driven through the **real** `cmd_get` in the deployed file with only `fetch_object` stubbed: three
distinct dates; several sources sharing one date; nothing to go on; `date_field` winning over provenance; empty values
(no `IndexError`); `source_vintages` as a list (no crash); and the discriminating arm.

**The lesson of the session is in that last arm.** My first multi-date arm had the oldest date sitting on the
lexically-first source name, so "oldest date" and "first source" would both have printed `2026-10-09` -- a PASS that
proves less than it looks like. Arm G put the **newest** date on the lexically-first source: "first source" prints
2026-10-12, "oldest date" prints 2026-10-07. It printed **2026-10-07**. A passing arm whose two candidate explanations
agree is not evidence between them; the arm has to be built so only one can pass.

**The limit stated, not implied:** arms A-G stub the S3 boundary. They prove the shipped function's logic, not that a
publisher ever writes multi-source provenance. ABSENT is not EXERCISED-AGAINST; the first real multi-source object is
still the first live test.

### Row Z-S19, and the loop it closed

Step 3 asked whether the twin `refs/PORTAL_RETRIEVAL.md` contradicts the edit. **It does not** -- line 13 rule 2 says
to answer from the data's as-of, "never the run date", which is what R6 implements; it is simply silent on an absent
field. What was stale is line **43**, the `mdpf-platinum` table row, still naming `as_of_date` -- a field absent from
all four objects measured. Filed as **Z-S19** rather than edited, because the order capped the cell at two files and
the override grant covered those two; it was not stretched to a third.

The issuer then issued **AMENDMENT 1 on that row** and granted the commit, so the finding closed its own loop inside
30 minutes. `31566aa49d`: one table cell, now matching the allowlist and the tool.

### Two instrument notes worth carrying

1. **The override audit prints TWO `OVERRIDE` lines per act.** Both R6 commits show it -- `act=8732e547cab1` at
   00:51:02Z and 00:51:05Z, `act=2b06380c0b36` at 01:04:59Z and 01:05:03Z -- plus one `LANDED-2P` line each. Two acts,
   two grants, **four** OVERRIDE lines. An auditor counting lines over-reports 2x against a one-override grant; the
   sound denominator is distinct `act=` ids. Reported at the drain and taken to the round's drain-end record. Observed
   on two distinct acts, so systematic rather than coincidence.
2. **`--date=format:'%H:%MZ'` renders LOCAL time and appends a literal Z.** Building this log's window I read my own
   commits as 20:51-21:07**Z** when they are 00:51-01:07 UTC -- the box is UTC-4. Caught against `%cI`, which prints
   `2026-10-13T20:51:12-04:00` and cannot lie about the offset. Never type a `Z` into a date format; use `%cI`, or
   `TZ=UTC` with `format-local`.

## Current State

- **Live in the world:** `org/tier0_utility/0.0.3_BG_BBGTerminal/tools/portal_lookup.py` at
  `sha256 b7f5ab25238a781cb70ec816b892f57b3fc292969f6d7f0bc71101ac313268ec`, 405 lines, LF, 0 non-ASCII. It runs from
  the working tree whenever the BG seat answers a question, so the next answer already uses the new order.
  `refs/BUCKET_ALLOWLIST.yaml` and `refs/PORTAL_RETRIEVAL.md` (`sha256 eb559e8dca...`, 79 lines, 26 non-ASCII) carry
  the same order.
- **Rollback, per key:** `git checkout b195dc14fe~1 -- <the two files>` for the cell, and
  `git checkout 31566aa49d~1 -- org/tier0_utility/0.0.3_BG_BBGTerminal/refs/PORTAL_RETRIEVAL.md` for the amendment.
  Pre-edit bytes: `portal_lookup.py` `65c9dd2d...`, `PORTAL_RETRIEVAL.md` `06cb1ee8...`. No infra, no S3 write, no
  ledger (LOCAL risk, read-only S3 throughout).
- **Order states:** TO-Z6-R6 `complete`, drained ~01:1xZ by the issuer, covering the cell and AMENDMENT 1. TO-Z6-R2
  `complete`. **TO-Z6-R3 still `held`** @`31ac9b5255` on row Z-S17 -- untouched by R6, which says so explicitly;
  worktree `C:/tmp/zs-z6-r3` stays `git worktree lock`ed with no R3 edits.
- **Rows:** Z-S19 filed (OBSERVATION / INERT). Its remedy has landed but **its disarm is the issuer's** -- the remedy
  landing is not the disarm. Z-S15/16/17 remain the issuer's from the earlier window.
- **Push state, MEASURED** (`git ls-remote origin box/sitez` = `43bde59c58` at 01:06Z, control passing):
  `b195dc14fe`, `ce59b6de56`, `e9b1d65b70` **on origin**; `31566aa49d`, `2eb2facd20` and this log **LOCAL**, pending
  this box's scheduled `box-sync`. This seat does not push a shared branch.

## Blockers

**None on this seat.** R3 is held by its issuer with an explicit do-nothing, pending Andrew's no-modify reading carried
by `0.0.0_AB_MSTR~Z` and `1.0.0_SA_CTO~Z`. Nothing this seat can do brings it forward.

## Next Steps

1. `[2.0.0_SA_COO~ZB]` Disarm or re-class **Z-S19** now its remedy has landed, and disposition Z-S15/16/17.
2. `[2.0.0_SA_COO~ZB]` Carry both drain-end notes: the multi-date arm is stub-only, and the override audit's
   two-lines-per-act counting trap.
3. `[0.0.0_AB_MSTR~Z]` / `[1.0.0_SA_CTO~Z]` Andrew's no-modify reading -- the only thing gating R3.
4. `[0.7.0_AE_CloudOps~ZS]` On a later R3 status line naming the reading: resume at step 1 in the locked worktree with
   its AMENDMENT 1 (the `if ($absent -eq 3)` guard) folded in. The step-2 exercise additionally needs `dapi_check` to
   read DOWN; it read UP at 21:14:16Z and 21:43:37Z.
5. **Owner of `.tools/commit-gate.sh`** Three suffixes fell through unexamined this session -- `.ps1`, `.yaml`, `.md`.
   The gate says so honestly each time, which is why each was caught, but the next reader who treats the WARN as noise
   ships something unchecked. Named here, not filed as a row: it is fabric tooling outside this project's channel.

## MCP traffic

4 in this window. **Received and ACKED** msg 33859 (GO on R6) and msg 33870 (GO on AMENDMENT 1, which also drained R6
and took both notes to the drain record). **Sent** two reports to `2.0.0_SA_COO~ZB` -- the cell report and the
amendment hash. The first send was **REFUSED at 156 words** against Rule 31's 150-word cap and was trimmed rather than
forced with `send_override`; the cap is enforced at the broker, so a long body never reaches a recipient.

## Files Modified

See commit messages: `b195dc14fe`, `ce59b6de56`, `e9b1d65b70`, `31566aa49d`, `2eb2facd20`. Two rows need context:

| file | note |
|---|---|
| `.../tools/portal_lookup.py` | the behaviour change. `cmd_get` only; +16 lines net. Landed under the granted override because lane `TIER0_UTILITY` refuses this seat |
| `.../refs/PORTAL_RETRIEVAL.md` | AMENDMENT 1, ONE table cell. A mixed-encoding file: 26 non-ASCII chars before and after, edited in binary with ASCII-only text, so no reader's encoding assumption changes |

## Compiler Tools

| tool | result |
|---|---|
| `py_compile` + `ruff check --target-version py39` on `portal_lookup.py` | PASS both |
| `yaml.safe_load` + recursive walk of every `vintage_field` | PASS -- 1 of 3 values changed, the right one, against a bad-YAML control that raised `ParserError` |
| real-`cmd_get` driver, S3 boundary stubbed, arms A-G | PASS 7 of 7; **G** is the discriminating one |
| read-only S3 GET x4 + x2 inside AC1 | PASS -- 4 of 4 `as_of_date=None`, 1 distinct date each |
| `r6_vintage_check.sh` (AC1) | PASS exit=0, both arms |
| `git diff --stat` pinned + `--name-only` (AC2) | PASS -- 2 files, the two named |
| markdown structural read (pipe count vs header, line count, non-ASCII count, anchor assertion) | PASS -- the language-appropriate instrument for the `.md` the gate skipped |
| `.tools/safe-commit.sh` x5, two with `GIT_COMMIT_AUTHOR_OVERRIDE=TIER0_UTILITY` | all landed; surprise-row gate 1 new of 19; naming-gate PASS 0 graded |
| `git ls-remote` + `merge-base --is-ancestor` with controls | PASS |

**What worked.** Asserting `count == 1` on every replacement anchor before writing. It is the same guard that caught the
CRLF error on R2, and here it is what let me promise "nothing else moved" on a one-cell edit inside a table and mean it.
Stubbing only `fetch_object` exercised the shipped function against shapes S3 does not contain.

**What failed.** Two self-inflicted probe errors, both caught by a second instrument rather than by luck: a YAML check
that looked up `d['buckets']` when the top-level key is `allow`, printed `None`, and read as "the edit did not land"
(resolved by walking the whole tree); and the local-time-plus-literal-Z date format above. A `None` or a timestamp from
a hand-typed accessor is a probe failure, not a measurement.

**Gap found.** `commit-gate` graded 0 of 1 on the `.md`, 1 of 2 on the `.py`+`.yaml` commit. Three suffixes unexamined
this session. Carried to Next Steps item 5.
