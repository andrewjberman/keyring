# Drive log -- 2.0.0_SA_COO~O, NFRA_OPLGTW round 38 (EXECUTING), 2026-10-16 14:30Z to 15:25Z (site Z)

Continues `drive_log_20261016T14Z_opal_bloomberg.md`. Finish-by Fri 2026-10-16 ~22:00Z. Push state: on origin @78cc59051e (ls-remote read 15:20Z).

## Done this stretch

| act | result |
|---|---|
| `OG-ap-29` closed | `0.7.0_AE_CloudOps~ZS` applied the dedicated 49F live read role (ledger `nfra-oplgtw-grants-ap29` CLOSED); I ran `ap29.AC2.sh` myself: simulate GetObject and ListBucket allowed 4 of 4, negative controls 4 of 4, trust only the instance role; proof VALID at `e497bc910d`, status complete |
| `OG-ap-28` cut | the ONE batched gateway release (E4, E5, E6, E8, E9, E10, `OG-en-12`, `OG-ts-1`, MX-c-26's catalog edit, the seventh reader key, `mcportal_commit` `59e802a`), staged, `40c539b06d`, addendum R3-T.97; the gate admitted it (WORLD, placeholders NONE) |
| `ap28.AC1` / `ap28.AC2` dry-run | base FAIL; AC1 PASS arm on a git-plumbing release commit (18 files); controls fail for the right reason (misaligned env slot, no env key, `tools.py` touched); AC2 served-record arm OK / NO / NO; the order's literal `<expect>` regexes match the PASS text and not the FAIL text |
| `Z-S294` dispositioned | `Z-S296` dismisses it (my `ap29.AC1` check defect, fixed, grant applied and proven), `78cc59051e` |
| mcportal pin | MP's ask (msg 35075, CTO msg 35074): `59e802a` replaces `c66ca82952`; origin DEV holds it and it descends from the live pin; MP told |

## Rulings and notes

- The live ref's `deploy-to-ec2.sh` carries `OG-ap-23`'s staging and six-key hunk; trunk's copy does not (the release branch was never merged back). The seventh-key hunk is applied on the LIVE script, never taken from trunk.
- A check that edits one long `printf` line needs a positional-slot grader, not a line-count one: `_dsh_check.py` removes the new slot from both the format and the argument lists and requires the base's lists back.

## Open

MI's final catalog (msg 35086: four rows on trunk, `98ce7eb4e7` and `a608e7bc84`; the emit is refused until amendment A4 `86f4e326a5` fixes eight registry rows, worker `~49`); then the Phase A GO for `OG-ap-28` to `0.7.0_AE_CloudOps~Z`; the `OG-en-11` re-run (closes Z-S292, Z-S293); E3 (blocked by the gateway MCP's 429, Z-S177); the L10 slug (draft `cbc4a9476f`); `OG-ng-3` and `OG-en-4` clerical flips; ten CVO-graduated armed rows awaiting DISARM.

## Traps met

- A heredoc through the harness eats backslashes: write scripts with the Write tool.
- Run a check from the repo root: its helper paths resolve after `_root.sh` changes directory.

## Compiler Tools

`git ls-remote`, `git cat-file -e`, `drive-mode.py read`. Gap: no tool grades a one-line-many-slots edit positionally.
