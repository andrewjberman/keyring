# ANDREW_DIRECT 2026-10-15 ~20:3xZ -- a252 template named; c02c drafted to the desktop; deletes 2106, 53cb and d8ae approved

**Channel:** Claude Code terminal, dell2, to `1.0.0_SA_CTO~DELL2`. **Recorded by:** `1.0.0_SA_CTO~DELL2`, same turn.

Andrew's words, verbatim, answering the `/open-calls` act list:

> "a252 this is the template: C:\Users\Test\Downloads\17752262.pdf. Regarding to c02c, draft that and put it on desktop locally here.
> 2106 deletes are fine. 53cb those recursive deletes of leftover worker and issuer scratch folders outside the repo are fine, this also
> goes for d8ae."

## What each word does
| row | his word | act |
|---|---|---|
| a252 (IRPT_DASHBD) | the 49 Financial template is the local file `C:\Users\Test\Downloads\17752262.pdf` | Route the path to `2.0.0_SA_COO~D2` (the asking seat). The file stays OUTSIDE the repo: it may carry client content. Its contents are read in place. |
| c02c (IRPT_DASHBD) | draft the Inflection operations ask and put it on this box's desktop | A send-ready draft is written to `C:\Users\Test\Desktop`. Sending stays his act. |
| 2106 (IRPT_ANLREQ) | the S3 deletes are approved | Delete every version of the 6 synthetic objects listed in `OBJECTS_WRITTEN_R29.txt` (bucket `opal-data-irpt`, prefix `irpt/49financial/state/`). Each version is read before its delete, and the result is read after. |
| 53cb (IRPT_BCKEND) | the recursive deletes of the worker and issuer scratch outside the repo are approved | Delete `C:\dev\_scratch384` to `_scratch390` and `_scratchP2`. `_scratch392` is already ABSENT. |
| d8ae (IRPT_ANLREQ) | "this also goes for d8ae" | Delete `C:\dev\wk-irpt-anlreq-139` and `-140`, the IRPT_ANLREQ folders under the mis-rooted `C:\c\dev` (`irpt-release-r29`, `irpt-release-r31`), and the listed non-worktree folders under `C:\dev\irpt-release-r31s` (`scratch`, `build-1`, `build-2`, `tmp-control-*`, `tmp-status`, `live-read-145`). |

**Narrowed by the pre-delete look, and NOT deleted:**
- **`C:\c\dev\wk-cotbkf-56`.** It is ADVI_COTBKF's, dell1's project, whose "lost round-85 scripts" are an open item (CRO research
  @03d1a87a9c). It is not an IRPT_ANLREQ folder, so it is outside d8ae's own subject.
- `C:\c\Users`.
- In `C:\dev\irpt-release-r31s`: `logs/`, `irpt-status-r31.zip` and `wt-status-e008b6216a`, which are not on d8ae's list.

Checked before any delete: no target is a registered git worktree (`git worktree list`), and none is a link or junction (PowerShell
`LinkType` empty on every target).

## Outcomes (measured, ~20:4xZ)
- **53cb: DONE.** Deleted `C:\dev\_scratch384`, `385`, `386`, `387`, `389`, `390` and `_scratchP2`, each confirmed absent after the
  delete. `_scratch392` was already absent.
- **d8ae: DONE (as narrowed).** Deleted, each confirmed absent:
  - `C:\dev\wk-irpt-anlreq-139` and `-140`;
  - `C:\c\dev\irpt-release-r29` and `irpt-release-r31`;
  - under `C:\dev\irpt-release-r31s`: `scratch`, `build-1`, `build-2`, `tmp-control-15a`, `tmp-control-d398`, `tmp-control-d398b`,
    `tmp-status` and `live-read-145`.

  Kept and read present afterwards: `C:\c\dev\wk-cotbkf-56`, `C:\c\Users`, and `logs`, `irpt-status-r31.zip` and
  `wt-status-e008b6216a` under r31s.
- **2106: NOT DONE, and nothing was deleted.** Every `delete-object --version-id` was refused: `AccessDenied ... s3:DeleteObjectVersion ...
  explicit deny in an identity-based policy: cloudops-dell-agent-deploy-policy` (user `cloudops-dell2-agent-user`).
  - The read-back is 1 version and 0 markers on each of the 6 keys, unchanged.
  - The six exact commands are at `C:\Users\Test\Desktop\RUN_AS_ANDREW_open_call_2106_s3_deletes.txt`, for Andrew to run with his own
    credentials. The row stays OPEN until the read-back shows 0.
- **c02c: the draft is on the desktop** at `C:\Users\Test\Desktop\DRAFT_Inflection_Orion_account_start_dates.txt`. Sending stays Andrew's
  act, so the row stays OPEN for the send.
- **a252: ANSWERED.** The template path went to `2.0.0_SA_COO~D2`. This seat could not read the PDF's text: no PDF reader is installed
  here, and none is installed for this. The file is 7,415,884 bytes, modified 2026-10-08, consistent with "sent last week".
