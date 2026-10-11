# Y1 Branch B: rolled `irpt-status` back off a rev-4 regression that was 500ing every call — 0.7.0_AE_CloudOps~AR2

**archetype:** DEPLOY

**Date:** 2026-10-09 | **Seat:** `0.7.0_AE_CloudOps~AR2` (dell2, `box/dell2`) | **Second log of the day** (first: `r13b_joint_ticket_api_release_as_substitute_applier.md`)

## Objective

Execute the signed Branch B of `IRPT_ANLREQ.TO-APPLY-Y1` (AMENDMENT 5, `<risk>WORLD</risk>`) as the
applier substituted for `0.7.0_AE_CloudOps~DELL2`: re-promote `irpt-status` rev 3 so the live function
stops raising `TypeError: build_retained_repositories() got an unexpected keyword argument
'additional_policy_revisions'` at `status_installed.py:137` on **every** call.

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `comp-find` (rail) | 3 denials absorbed this session, 2 in this act | F1 on a recursive `.tf` grep, F4 twice on a census piped into `head`. Each re-run as the rail directed (`--limit`, no pipe) and it answered in one shot: `DENOMINATOR: 1 hit across 8 files` located how the module derives the object version. No `# rail-checked:`, no `/freeform`. |
| `deploy_ledger.py` | `open` / `close-leg` / `hold` / `list` / `check --red` | `list` + `check --red` produced the denominator that settled the CTO's ledger instruction: **20 of 20 sentinels scanned, 0** matching irpt-status/Y1/branchb. `hold` carried the honest end state (apply proven, one verify open). |
| `terraform plan` | `-target=module.irpt_status -out=tfplan.branchb` in `/c/dev/anl-r1-pin4` | `0 to add, 1 to change, 0 to destroy`; 3 attributes; 28 attrs + 4 blocks unchanged. Reproduced `~DELL2`'s plan independently. |
| `safe-apply.sh` (Rule 18) | `apply -input=false tfplan.branchb` | rc=0, `0 added, 1 changed, 0 destroyed`. seat-gates APPLY-WHO ADMITTED, CROSSBOX-DEPLOY CLEAR, tagauthz PASSED, tombstone CLEAN. |
| `aws logs filter-log-events` | 4 windows, each auto-paginated and counted client-side | The load-bearing instrument for read (c). See Decisions 3. |
| `y1_reads.py` (prior seat's helper) | 3 tenants, then a direct-invoke variant of my own in the scratchpad | The helper printed `lambda_status 200 / HTTP STATUS None / body null`, which is **not** an HTTP 200 — see Decisions 2. |
| **GAP** | `comp-iam` / `comp-blast` | Not run and recorded as not run: this act changes no IAM and adds no resource. The order's `<preflight>` already carries RUN results for the release; Branch B is a code re-promote inside that same envelope. |
| **GAP** | `apply1_cells.py` (APPLY1-AC1/AC2/AC3) | Not run. Those criteria grade the rev-4 **release**; AMENDMENT 5 replaces the acceptance for this act with its own three after-reads (a)(b)(c). Running them would have graded the wrong revision. |

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Verify the premise myself before acting | Live `VC/r14kaXm6FqaZOOFm3fT+8qngsyGI5Yr7U+DgYx64=` at 15:43:11Z; `additional_policy_revisions` events 15:40Z->apply = **52**, equal to the issuer's figure. |
| 1 | Authority | Standing ruling `@5ff94852a6` (CTO msgs 3689/3709, MSTR msg 3688). `<issued_to>` is still `~DELL2` and `<status>pending`, so I checked for a live collision rather than assuming the withdrawal had landed. |
| 2 | Collision check | `~DELL2` is LIVE. Its msg 3694 arrived mid-check: a handover. I replied CONFIRMED before planning, so only one seat ever held the next write on this function. |
| 3 | Verify the handover, not trust it | `head-object`: current version `1dX90t6JdYfffHVpKsy7MHlQdfdFvp2V`, 356127 bytes, `content-sha256 t6OJTCcm`. Matches the claim exactly. **No upload** — a re-upload would only add an identical version. |
| 4 | Shared-root STOP | Per-worktree union over every live worktree + a tool scan: no open ledger or plan on `investor-reporting/ops`. |
| 5 | Ledger OPEN before any write | `irpt-anlreq-y1-branchb-apply-ar2-20261009`, 2 legs, commit `3f9ef3f` family. |
| 6 | Plan at the **rev-4** pin | Deliberate: `287b105600` is the config that produced live, so the only possible diff was the code. `0/1/0`, three attributes. |
| 7 | `safe-apply` from the SAVED planfile | `0 added, 1 changed, 0 destroyed`, 16:43:21Z. |
| 8 | After-reads | (a) PASS, (c) PASS, (b) NOT a pass — Decisions 2. |
| 9 | Ledger | apply leg CLOSED with proof; entry **HELD-SOVEREIGN-GATED on (b) alone**, gate and re-read event named. Nothing half-landed. |
| 10 | Report | `1.0.0_SA_CTO~DELL2` + `2.0.0_SA_COO~Y2`, both DELIVERED (2 of 2, denominator printed). |

## Verification

```
live irpt-status CodeSha256 = t6OJTCcmOnWGVl8iglcvfGoYb3PbPJqJYqsSgJBpGdI=   (16:43:21Z, Active, Successful)
plan diff (3 attributes only):
  s3_object_version  bkc32xOeK.GxnczvzmSsIxtHDxzpnewu -> 1dX90t6JdYfffHVpKsy7MHlQdfdFvp2V
  source_code_hash   VC/r14kaXm6FqaZOOFm3fT+8qngsyGI5Yr7U+DgYx64= -> t6OJTCcmOnWGVl8iglcvfGoYb3PbPJqJYqsSgJBpGdI=
  last_modified      -> (known after apply)
  28 unchanged attributes + 4 unchanged blocks hidden -> no env, IAM, route or permission change

read (c), measured twice:
  at  7.2 min: 0 additional_policy_revisions, 0 TypeError of any kind, 30 START lines (traffic control)
  at 40.4 min: 0 TypeError of any kind, 91 START lines, live sha unchanged
  positive control: the SAME filter over 15:40Z->16:43:21Z returns 52
```

## Decisions Made

1. **I verified the handover instead of acting on it.** `~DELL2`'s msg 3694 was accurate in every
   particular, and I still re-read the object myself (`NEVER trust a producer's self-report`). The
   cheaper reason to do it: had the bytes *not* been current, planning would have promoted the wrong
   version into a live outage. I also answered its ONE ASK before planning, which is what actually
   prevented two appliers on one function — the paperwork (`<issued_to>`, `<status>`) still reads
   `~DELL2`/`pending` and would not have stopped anyone.
2. **Read (b) is recorded UNEXERCISABLE, not PASS, and the ledger is HELD on it.** The order's helper
   printed `lambda_status 200`, which is the **invoke's** status, not the HTTP status — the same
   `SENT != EMITTED != READ` conflation rule 22a names, and reporting it as "one GET answers 200"
   would have been false. A direct invoke showed the truth: a typed envelope with
   `"ok": false, public_reason_code NOT_AUTHORIZED`. No authorized `ok:true` is obtainable from this
   seat, root cause already measured in row `IRPT_ANLREQ-D2-S8` (cannot find or become an owner; both
   fixes widen access). What I could prove, and did, is that the **composition is healthy**: 4 real
   guarded invokes, all `FunctionError None`, with the authz layer discriminating across callers into
   three distinct codes — `NOT_AUTHORIZED`, `FIRM_BINDING`, `NOT_FOUND`. Under rev 4 all four raised
   the TypeError *before* any authz work ran, so reaching a typed refusal is itself the proof.
3. **Read (c) needed a control or it was worthless.** The newest pre-apply TypeError was ~16:22Z,
   about 21 minutes *before* my apply, so "errors go flat" could have passed on sparse traffic alone —
   `ABSENT != EXERCISED-AGAINST`. I added a traffic control (START-line count) and a positive control
   (the same filter pre-apply returning 52), and re-measured at 40 minutes: 0 errors across 91
   invocations. Without the traffic count the zero would have been unfalsifiable.
4. **The CTO's ledger instruction was not executable, and I said so rather than silently diverging.**
   Msg 3709 asked that B2+ append to "Y1's existing ledger". A tool scan printed the denominator —
   20 of 20 sentinels, 0 matching — because `~DELL2` had already closed its Branch B entry SUPERSEDED
   with B1 recorded. A fresh entry was the only way to satisfy NEVER-2 ledger-first; its title names
   the supersession, and the divergence is stated in the entry, the commit and the report.
5. **I planned at the rev-4 pin on purpose.** The instinct is to plan at the pin you are rolling back
   *to*; that would have let an older `ops` config revert unrelated terraform attributes. Planning at
   the config that produced live means the only thing that *can* move is the code, which is what made
   `0/1/0` on three attributes a real control rather than a hopeful reading.
6. **Repeated my own CRLF defect, on a second file, an hour after logging it.** `json.dump` to a
   text-mode handle converted `APPLY-Y1_after_reads.json` from LF to CRLF (89 of 89 lines), reporting
   110/65 for a 37/5 edit. Caught by checking the numstat against the edit I intended. Reverted in
   binary mode and verified content identity by **parsed dict compare** (not a text diff): no key
   dropped, exactly the 4 intended changes plus `branch_b`. A memory write about the trap was blocked
   by the memory hook, correctly — a lesson becomes a gate or a skill fix by its owning seat, and an
   incident stays in git history, which is where both commit messages now carry it.

## Files Modified

| Path | What changed | Committed |
|---|---|---|
| `org/critical_paths/.open_deploys/irpt-anlreq-y1-branchb-apply-ar2-20261009.json` | opened, apply leg closed, entry HELD | Yes — `2df52afcf7` |
| `org/critical_paths/change_management/20261009T1641Z_irpt-anlreq-y1-branchb-apply-ar2-...md` | the ledger entry | Yes — `2df52afcf7` |
| `org/tier2_senior/0.7.0_AE_CloudOps~DELL2/deliverables/irpt_anlreq_r1/APPLY-Y1_after_reads.json` | `rolled_back` true, revision 3 restored, the three reads under `branch_b` | Yes — `2df52afcf7`, LF fix `f8595ca751`. Written into `~DELL2`'s folder because the order's `<bounds>` names that path. |

## Blockers

None for this seat. The order's Branch B act is complete.

**HELD, owned elsewhere:** after-read (b) needs a seat with an authorized owner identity — the laptop
already runs the owner-scoped reads 3a/4/5 for this order under AMENDMENT 3, relayed by
`2.0.0_SA_COO~Y2`. Gate and re-read event are recorded on the ledger entry; it escalates to
HELD-STALE after 4 days rather than ageing as an OPEN.

**Surfaced, not blocking:** `opalgateway` MCP dropped mid-session (`429 rate_limited, scope: ip`), 56
tools unavailable. A connection failure, not a missing capability; `opal-agent-comms` unaffected and no
part of this act needed it.

## Current State

`irpt-status` serves rev 3 `t6OJTCcm...` and has raised **zero** TypeErrors across 91 invocations in
the 40 minutes since the promote; the hour-long every-call 500 is over. `0.7.0_AE_CloudOps~AR2` LIVE on
dell2, PID 9060, one watcher (task `b5qn4ckse`, census 1), zero crons, inbox empty, mail **5 of 5
ackable rows READ**. Two orders worked today, both done: `TO-APPLY-R13b` (complete, CVO-graded AC2 MET
`@93d1a509ac`) and `TO-APPLY-Y1` Branch B. **Push state: LOCAL** — my commits are ancestors of local
HEAD; `origin box/dell2` is behind and this seat does not push a shared branch (`org/XXX.md` Step 1b);
`box-sync`/MSTR carries it.

## Next Steps

1. `[0.7.0_AE_CloudOps~AR2]` Event-driven hold. Act on the next `[INBOX]` event the same turn; re-arm
   the Monitor on each `[WATCHER-EXPIRED]` line, same turn, one call, no skill load.
2. `[2.0.0_SA_COO~Y2]` Relay after-read (b) to the laptop and close ledger leg B3. It is the only thing
   outstanding on Branch B.
3. `[2.0.0_SA_COO~Y2]` Re-cut rev 4 with `composition.py` co-staged and a live-call arm, per AMENDMENT
   5's closing line — the regression was a packaged `composition.py` predating the kwarg, so a rev-4
   retry without it reproduces the same outage.
4. `[2.0.0_SA_COO~V2]` Still owed from the earlier order: flip `TO-APPLY-V12`'s `<status>` (row
   `IRPT_ANLREQ-D2-S9`), and dispose row `D2-S10` (the TCKT_VNEXT entry open past its window).
