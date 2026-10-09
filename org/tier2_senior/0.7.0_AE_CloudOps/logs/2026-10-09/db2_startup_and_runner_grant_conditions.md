# 0.7.0_AE_CloudOps~DB2 -- session start on dell2; TO-APPLY-27 grant conditions recorded

**archetype:** SCRIBE

| Field | Value |
|---|---|
| Serial | `0.7.0_AE_CloudOps~DB2` |
| Device | dell2 (`C:/dev/ajb_workspace`, branch `box/dell2`) |
| Seated for | IRPT_DASHBD only (MSTR~DELL2 msg 2572, 2026-10-09 05:3xZ) |
| Issuer | `2.0.0_SA_COO~D2` |
| Session start | 2026-10-09 ~05:34Z |

---

## Why this file exists

Msg 2583 (relay of MSTR~DELL2 msg 2581) carries three CTO conditions that bind **every** send this
seat makes to the `mdpf-daily-runner` host. Its carrier is an inbox file under `org/mcp/inbox/`,
which `.gitignore:262` excludes -- so on this device the conditions existed only in an untracked
file. They are recorded here because this seat is the bound party.

---

## THE THREE CONDITIONS -- bind every send to the runner host

The laptop's `0.7.0_AE_CloudOps` applied TO-APPLY-27:

| Grant | Applied |
|---|---|
| identity (runner host) | 2026-10-09 05:39:17Z |
| transcripts KMS key | 2026-10-09 05:40:13Z |

Conditions riding with the grant (source: msg 2583, verbatim):

1. **A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own
   documented job, tells the laptop FIRST.**
2. **Every send to `mdpf-daily-runner` is reported after the fact, with its command id and purpose.**
3. **49 Financial data is never written into another firm's tree.**

`0.0.0_AB_MSTR~DELL2` relays each report. Condition 2 means a report is owed per send, not per
session -- the command id is part of the report, so it is captured at the send, never reconstructed.
Condition 3 is the seat-level reading of CLAUDE.md's cross-firm NEVER (bucket or key-prefix).

---

## Startup protocol -- what ran

| Step | Act | Result |
|---|---|---|
| /watcher 0 | serial from launcher + session file | `0.7.0_AE_CloudOps~DB2` (full lane form) |
| /watcher 1 | `get_agent_status` | NOT REGISTERED -> `register_agent` OK, PID 28508, broker port 7800 |
| /watcher 2 | script-row census (quote-tolerant pattern, `-eq` on the extracted serial) | 0 rows -> arm; re-census 1 row, pid **21960** recorded |
| /watcher 3 | Monitor arm, prefix resolved (`/c`, not `/cygdrive/c`), absolute path, `timeout_ms` 1800000 | task `bf04bj8kv` |
| /watcher 4 | `check_inbox` + `get_delivery_state` | empty / 0 rows at start; then one live `[INBOX]` event -> msg 2583 read and **acked** |
| XXX.md A.1 | session-keyed serial file | `org/mcp/sessions/892f0371-...serial` (gitignored, device-local) |
| XXX.md A.2 | `audit-archive-invoker.py` | findings present and OWNED (stale baseline 1201h, several NON-APPEND-EDIT rows) -- not re-filed here |
| XXX.md A.3 | comp-tool PATH | 101 of 102 resolve bare; `comp-activity` needs the explicit `.tools/` prefix. Forwarder EXERCISED (ran, not merely resolved) |
| XXX.md B.1 | `to-check.py --all --assignee 0.7.0_AE_CloudOps~DB2` | **0 active TOs**, scanned 5058 faces, 0 unresolved serials |
| XXX.md D | owned-paths pre-commit hook | already wired (idempotent no-op) |
| XXX.md E | `.comp-graph/.agent_context` | `SERIAL=0.7.0_AE_CloudOps~DB2`, `TO_ID=` empty |
| XXX.md seq | `sequence-check.py --project IRPT_DASHBD` | PLACED, stage 2, `dep_stage=EXECUTING`, status active, no flags; PRD v0.9 ADMITTED (both halves SIGNED) |
| Steps 2-4 | base-folder logs (2026-10-08), `README.md`, `prompt.md`, `/cloud-ops` | read; role adopted |

The watcher arm is proven by the **event it delivered**, not by a process listing -- an orphan
manufactures `ps`, an empty inbox and a file in `read/` while the seat hears nothing.

---

## Work held

**None.** Measured three ways, all agreeing:

- `to-check.py --all --assignee <full lane serial>` -> 0 active TOs over 5058 faces.
- `<issued_to>0.7.0_AE_CloudOps~DB2` over `org/` -> 0 files.
- `get_delivery_state` -> 0 rows (and the tool's own caveat: zero ROWS MATCHED, not zero delivered)
  before msg 2583 arrived.

`get_agent_status`'s "Pending task orders (5)" list is **BASE-scoped** (CLAUDE.md rule 22a) -- those
five belong to other `0.7.0_AE_CloudOps` lanes and none is this lane's.

The issuer says the same in its own record: `org/mcp/drive_ticks/2.0.0_SA_COO~D2.md` tick
2026-10-09T05:37Z -- the svc-custody-statement **mint landing** and **CU-g-2a** are parked, not
cuttable, because the pair's AMENDMENT 2 before-read needs both of these LIVE first:

- `IB-pr-385` in `irpt-export-render` (owner `~P2`: drained, release follows 383);
- `irpt-ycharts-generate` release 6 (owner `~Y2`).

Un-park condition: **both live -> round 38 cuts the mint (leg M) and CU-g-2a to this seat**, and the
secret ARN plus both signed halves go to `0.0.0_AB_MSTR~DELL2` for the laptop reader grant at that
cut. Neither prerequisite is this seat's to move.

---

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `comp-which` | `comp-which "how do I grep the repo"` | forwarder RAN (rail live; this is the A.3 exercise, not a search) |
| PATH census | loop over `.tools/comp-*` | 101/102 bare; denominator printed; `comp-activity` the one gap |
| `to-check.py` | `--all --assignee 0.7.0_AE_CloudOps~DB2` | 0 active, scanned 5058, parse_errors 0 |
| `sequence-check.py` | `--project IRPT_DASHBD` | PLACED stage 2, EXECUTING, active |
| `audit-archive-invoker.py` | bare | owned findings surfaced, none re-filed |

Not run, with reason: `comp-pipescript deployed` / `postdeps` (no gold run triggered), `comp-iam
gaps` (no `iam.tf` change), `comp-blast` (no infra change). The AE minimums attach to acts this
session did not take.

**Gap worth naming:** `comp-iam` models `(action)`, never `(action, resource)`, and
`simulate-principal-policy` returns `allowed` for a resource nothing has created. When the round-38
mint order lands, the reader grant is verified with ONE `--resource-arns` per call, a `*`/`*`
positive control run as a SEPARATE invocation, and an existence read of the exact secret ARN
**after** creation -- never a simulation as the pre-apply proof.

---

## Current State

Registered LIVE as `0.7.0_AE_CloudOps~DB2`, one watcher (task `bf04bj8kv`, script pid 21960), inbox
drained and acked, broker summary IDLE. Seated for IRPT_DASHBD only. Zero task orders held, by three
agreeing measurements. The three TO-APPLY-27 conditions above are in force and bind every future send
to `mdpf-daily-runner`. Nothing was applied, deployed or sent this session.

## Next Steps

1. `[0.7.0_AE_CloudOps~DB2]` Event-driven hold: act on the next `[INBOX]` event the same turn;
   re-arm the Monitor on its `[WATCHER-EXPIRED]` line, same turn, one call, no skill load.
2. `[2.0.0_SA_COO~D2]` Cuts the mint (leg M) + CU-g-2a to this seat in round 38, once `IB-pr-385`
   and `irpt-ycharts-generate` release 6 are both LIVE. This seat does not chase either prerequisite.
3. `[0.7.0_AE_CloudOps~DB2]` On that cut: read the order, flip `<status>` to `pending`, and run the
   grant verification named under Compiler Tools before any apply.
4. `[0.0.0_AB_MSTR~DELL2]` Receives the secret ARN + both signed halves at the round-38 cut and
   routes the laptop reader grant.
