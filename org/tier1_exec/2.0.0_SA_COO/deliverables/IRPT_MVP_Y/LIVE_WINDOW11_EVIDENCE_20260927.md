# Window 11 (the Analysis chain, fourth attempt, resident `wf`): two defects named by the journal, both fixed and proved offline

Author `2.0.0_SA_COO~Y`, 2026-09-27 ~13:4xZ.

Packet: blob `9ee0c7c5` (CTO @1e5b0a08af, CRO @8253c62327). Word: Andrew at ~Y, "yes you can run as many analysis
attempts as needed" (@460e2ae8cb). The principal was `irpt-uiwalk-1790513738`.

## The acts: one login, then K4 and K5 (`live_chain.py`; log `LIVE_CHAIN_1203_20260927_W11.json`, scrubbed)

| Time | Act | Answer |
|---|---|---|
| 12:58:40Z | login | 200 |
| 13:00:09Z | the password read absent | K4 released |
| 13:00:14Z | K4 upload | NORMALIZED at 13:00:16Z, input `portfolio_f1bff850..` |
| 13:00:20Z | K5 Overview | 200 QUEUED, `REQ-717c91a59228070704e81cba` |

## The resident (the journal's closed-token lines, from the patches shipped today)

- The upload and portfolio create succeeded (`model_portfolio_id` 2363812).
- 13:01:00Z `STEP_WAF_REFRESH step=read_back status=202 portfolio_status=- polls=3 wall_s=32.1`: the WAF challenged the
  3rd status poll, even at 15 s spacing.
- 13:01:02Z `retained_for_retry class=OperationRefused code=CAPTURE_FAILED:LEASE_NOT_HELD`: **defect 1**.
- 13:16:04Z, on redelivery: `STEP_REFUSED step=read_back status=200 portfolio_status=available polls=1 drifted=<all 7>`
  and the job went ATTENTION: **defect 2**.

## Defect 1: the host capture inherits the resident's Python path

- The resident unit sets `PYTHONPATH=/opt/irpt-resident/fe64236bbb-wf`, which vendors a urllib3 that needs
  Python 3.10+.
- The capture wrapper inherited it, so the Node runner's `aws` CLI (`/usr/bin/python3`, 3.9) crashed.
- The runner's lease port reports any failed `aws` call as "held by another runner", hence `LEASE_NOT_HELD`.
- Its lease row stayed at fence 13: the conditional update never ran.
- Measured on the host, read-only (`sts get-caller-identity` only):

| Context | Result |
|---|---|
| systemd-run as ec2-user, no PYTHONPATH | rc 0, `irpt-ycharts-runner-role` |
| the same, with the resident unit's PYTHONPATH | `TypeError: unsupported operand type(s) for \|` in `/opt/irpt-resident/fe64236bbb-wf/urllib3/_base_connection.py` |
| the patched `host_capture.py` (sha256 `2905c73b`) under the resident PYTHONPATH: inherited env | rc 1, the TypeError |
| the same file, through `capture_env()` | **rc 0**, `irpt-ycharts-runner-role` |

This is very likely also the unrecorded cause of window 6's receive-1 failure (S151): the same resident-launched
wrapper failed within 2 s, while the manual wrapper run, which had no PYTHONPATH, succeeded.

**Fix:** `host_capture.capture_env` runs the wrapper with the resident's environment minus every `PYTHON*` variable.

## Defect 2: the read-back compared the status body, which carries no settings

- An `available` portfolio's `/model_portfolios/{id}/status` answer held none of the 7 fields.
- `status_ok.json`'s settings were derived, never measured: the HAR evidence has no `/status` response.
- The only live-proven settings read is the research worker's `GET /model_portfolios/fixed/{id}` -> `portfolio[field]`
  (`variant_worker.verify_owned_snapshot`).

**Fix:** `recipe.step_read_back` polls the status only until `available`, then reads the SAVED portfolio once and
compares. A field the vendor omits is named in `absent`, apart from `drifted`. The journal line adds `source=` and
`absent=`.

## Proof

Fix: Y branch `ff1f95a701`, `P_W11_CAPTURE_ENV_SAVED_READ_BACK_20260927.patch`. The patch is cut against P's
`3aa870163d` and applies cleanly (apply-check rc=0). Its runtime files are content-identical to the proved overlay.

Real entry point (`resident_job_preflight.py`: served `wf` content, the real Overview PDF, the production census):

| Run | Result |
|---|---|
| (A) window 11's bare `available`, deployed `wf` | ATTENTION; journal `status=200 portfolio_status=available polls=1 drifted=<7>`, **identical to the live 13:16 line** |
| (B) the same, with the fix | `READ_BACK_DONE source=saved_portfolio drifted=- absent=-`, **READY**, 1 REPORT# |
| (C) the full window 11 sequence (2 calculating, a WAF challenge, a stubbed re-capture, bare available), with the fix | `STEP_WAF_REFRESH`, 1 capture, `READ_BACK_DONE source=saved_portfolio`, **READY** |

Tests:
- `test_read_back_poll.py` 8/8; `test_host_capture.py` 9/9.
- Resident suites 48 passed, 8 skipped; the session suite has 97 passed, and its 2 failures are the parked
  FirmDestinationPolicy absence.

Limit: the saved-portfolio answer in B and C is the recipe's own values in the research worker's shape. The live
shape is proved by the next attempt, and `absent` names any field it lacks.

## For the next packet

K5's read-back becomes:
- up to 6 status GETs 15 s apart;
- then **ONE `GET /model_portfolios/fixed/{id}`**;
- plus ONE re-capture on a read WAF challenge, which now runs outside the resident's PYTHONPATH.

The upload `779765`-class object and portfolio 2363812 are kept.
