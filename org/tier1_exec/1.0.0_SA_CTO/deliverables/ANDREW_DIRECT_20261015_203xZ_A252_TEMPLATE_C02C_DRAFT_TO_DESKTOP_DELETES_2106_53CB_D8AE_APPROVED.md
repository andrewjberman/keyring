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
