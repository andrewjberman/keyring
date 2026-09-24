# DEPLOY LEDGER -- `amgt-py-aws-hoist-leg-isolation`

**Opened:** 2026-09-24T14:33Z by `1.0.0_SA_CTO~Z` (site Z), BEFORE any edit, per CLAUDE.md NEVER-2.
**Status:** OPEN
**Disarms:** `AMGT_RESAPP-Z-S248` (ARMED, surfaced by `0.0.3_BG_BBGTerminal` 2026-09-24T10:10Z)
**Disarm owner named on the row:** the owner of this file's models/ETF/constituents legs -- this seat,
which authored the 2026-09-04 leg-isolation fix the defect sits inside.

## WHY THIS IS A DEPLOY AND NOT AN EDIT -- measured, not assumed

`Get-ScheduledTask` on this box returns **`OPAL_BBGTML_daily_pull`, State=Ready**, whose action is
`cmd.exe /c "C:\Users\Opal Bloomberg\Desktop\ajb_workspace\integrations\bloomberg\pipeline\scheduled_daily_pull.cmd"`
-- **the WORKING-TREE path, directly.** So the bytes in the working tree ARE what the next fire executes;
there is no build, no package and no promote between the edit and production. ⛔ **An uncommitted edit to
this file is a live deployment**, which is why this entry is opened first.

**Next fire:** `Get-ScheduledTaskInfo -> NextRunTime` = **2026-09-25 07:00:00 local (~11:00Z)**, about 20.5
hours out. **The window is not contended**, so there is no risk of the task firing mid-edit.

## THE DEFECT, CONFIRMED AT HEAD BY THIS SEAT RATHER THAN TAKEN FROM THE ROW

| line | fact |
|---|---|
| `:145` | `if "%DAPI_OK%"=="1" goto :etf_leg` -- jumps to the label at `:228` |
| `:166` | the **ONLY** `set "PY_AWS=...python.exe"`, sitting INSIDE the SEND leg |
| `:234` | `"%PY_AWS%" -u "%ETF_PULL%"` |
| `:285` | `"%PY_AWS%" -u "%CONS_PULL%"` |
| `:323-325` | the file's own comment ALREADY documents this defect, added when the price leg was built |

`cmd` expands an unset variable to the empty string, so on the pull-failed/DAPI-up path both landing legs
invoke `"" -u <script>` and cannot land. ⚠ **That path is the 2026-09-04 leg-isolation fix's own protected
path** -- added so a models fault could not turn one leg's failure into two legs of permanent data loss --
so the defect defeats exactly the guarantee its surrounding comment makes.

## BLAST RADIUS -- what this act MAY touch, and the rollback for each

**The change is ONE LINE MOVED and is strictly one-directional.** Enumerated by path rather than asserted:

| path into `:etf_leg` | `PY_AWS` before | `PY_AWS` after | change |
|---|---|---|---|
| SEND path (`:188 goto :etf_leg`, models rc=0) | SET at `:166` before use | SET earlier | **none** |
| fall-through from `:pub_failed` (`:190` -> `:213`) | SET at `:166` (precedes `:190`) | SET earlier | **none** |
| pull-failed / DAPI-up (`:145 goto :etf_leg`) | **EMPTY** | SET | **broken -> working** |

⭐ **NO PATH GOES FROM WORKING TO DIFFERENT.** Exactly one path goes from broken to working, and the two
already-working paths are unaffected because the assignment already preceded its use on both.

**What lands as a result:** on that one path, the ETF and CONSTITUENTS legs will execute rather than
no-op. They write their own keys with their own producers -- this act adds no key, moves no key and
changes no producer's rule. **It is not a served-output MOVE**, so NEVER-1's never-widen pair is not the
instrument here; the act restores an intended write on a failure path.

**ROLLBACK:** `git revert` the single commit, or move the `set "PY_AWS=..."` line back below the
`if not "%RC%"=="0"` block. The file is the deployment, so the revert IS the rollback -- no artifact to
re-push, no task to re-point, no cache to bust.

## LEGS

| id | kind | target | proof required |
|---|---|---|---|
| L1 | git | hoist the `:166` `set "PY_AWS=..."` above the `:145` branch, in `scheduled_daily_pull.cmd` | commit hash + the three-path table re-read at the new line numbers |
| L2 | verification | exercise `cmd`'s ACTUAL expansion on the DAPI-up path, with a negative control | a temp `.cmd` reproducing the control flow: PRE-fix prints empty, POST-fix prints the interpreter |
| L3 | verification | the interpreter the hoisted line names actually exists on this box | `test -x` / version read on that path |

⚠ **L2 EXISTS BECAUSE READING `cmd` IS NOT RUNNING IT.** The whole defect is an expansion-semantics
question, and this seat's reading of `:145`/`:166`/`:234` is the same instrument that would miss a second
`set` on another path. The control has to be `cmd` itself, with a PRE arm that fails.

## STATUS LOG

- 2026-09-24T14:33Z -- OPENED before any edit. No leg executed yet.
