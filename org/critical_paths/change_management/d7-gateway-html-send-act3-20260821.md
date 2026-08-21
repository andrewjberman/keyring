# DEPLOY LEDGER — opal-gateway: D-HTML Teams send + the queue (ACT 3 of 4)

**Opened:** 2026-08-21T14:30:46Z by `0.5.0_AE_OpalETL~Z` (deploy-start; NEVER#6)
**Status:** **CLOSED 2026-08-21T14:40:02Z** -- deployed, restarted, and VERIFIED ON THE BOX (not from the deploy's
own rc). All 6 legs closed; nothing stranded.
**GO:** Andrew-direct ~1346Z, VERBATIM: *"approved on all three, proceed"* — relayed `1.0.0_SA_CTO~Z`
msg 4344 @`8a99d851f2`, **as AMENDED by msg 4350** (ACT 3 inherits GW-APPLY's G1–G6; G1's discharge
was stale).
**Applying seat / device:** `0.5.0_AE_OpalETL~Z` on **site Z**, Rule 26. Both GW-APPLY build commits
(`2b7258f31c`, `90d526c199`) are this seat's and ancestors of HEAD here.
**Target:** `i-07dccb1615503ac99` · **`main.tf` :191/:193 NOT TOUCHED** (user_data is instance
replacement — excluded in terms by GW-APPLY, and exercising it is the disaster the criterion exists
to prevent).

## G1 — RE-RUN, AND IT FALSIFIED MY OWN PRIOR RECORD

The 0240Z discharge described an instance that **no longer exists** (LaunchTime 2026-08-21T07:58:44Z).
Re-read on the box that exists now, **read-only over SSM**:

```
uptime -s                       2026-08-21 07:58:49          <- this IS the replaced box
opal-gateway.service            active
m365-mcp-gateway.service        inactive
ACTIVE unit ExecStart           /opt/opal-gateway/.venv/bin/uvicorn app.server:app --workers 1
ACTIVE unit WorkingDirectory    /opt/opal-gateway
FragmentPath                    /etc/systemd/system/opal-gateway.service
/opt/m365-mcp-gateway           DOES NOT EXIST  (ls: cannot access)
/opt/opal-gateway/app/tools.py  38,604 B  md5 06e1fd0a11029c74e7cd24294eafc78a
localhost:8080/health           200
```

**AN `ls` WOULD HAVE BEEN THE WRONG ORACLE** — a directory existing proves nothing about what
executes, and the OPAL_GWRENAME cutover deliberately left the old unit stopped-and-disabled rather
than removed. **The decisive read is the ACTIVE unit's own `ExecStart`/`WorkingDirectory`.**

⛔ **THE DESTINATION IS `/opt/opal-gateway`, AND MY OWN 15h-OLD MESSAGE SAYING
`/opt/m365-mcp-gateway` IS WRONG FOR THIS BOX.** That message halt-gated my own ACT-1 apply twice
today and was cited in the amendment. **The record is annotated, not flipped:** it was written
2026-08-20 ~23:0xZ and was *already* wrong then — **I had corrected the identical claim in my own
commit `bbb6f2529d` at 18:56:04, 3.5 minutes after making it in `f3c1ccbe20`.**
>> **THE CORRECTION LIVED IN A COMMIT MESSAGE AND THE ERROR TRAVELLED IN A MESSAGE TO SOMEONE WHO
WOULD ACT ON IT.** A correction carries the text, not a citation. The wrong claim then caused a
*correct* action (re-running G1) for a partly wrong reason — the instance replacement was the real
justification.

**CORROBORATION:** the on-box `app/tools.py` md5 `06e1fd0a…` **matches `EC2_MANIFEST.file_checksums`
exactly**, so the manifest's `deployed_commit 5a1cc39e8e` self-report is confirmed on the CODE layer
by an on-box read rather than trusted.

## Rule 11 parity, BEFORE work

`verify-ec2.sh` rc=1 estate-wide (27 checked / 2 clean / 7 drift / 18 skipped). **The gateway's own
row: 8 undeployed commits to the service dir** — expected, and it is what this deploy lands.

## What actually ships (the tarball carries `app deploy requirements.txt identity_tool_allowlist.txt`, NOT README)

**4 commits / 3 files** in the shipped set, re-measured at deploy time rather than recalled *(my
earlier "3 commits / 3 files" was correct before my own D-HTML commit landed this session)*:

| commit | ships |
|---|---|
| `90d526c199` | `tools.py` — `lastModifiedDateTime` on the two message readers |
| `2b7258f31c` | `tools.py` + `integrations/opal_portal/integration.py` — the `alwaysLoad` marks |
| `cdedf37b8f` | `teams_format.py` (NEW on the box) + `tools.py` — D-PROSE at the send path |
| `7b7b0004a9` + this act | `teams_format.py` html renderer + the 4-line wiring |

⛔ **THIS IS NOT "A FORMATTING CHANGE". It carries THREE fabric-wide behaviour changes:**
1. **Teams message formatting** for every seat's every send (D-PROSE + now HTML).
2. **`alwaysLoad` marks 0 -> 5** — measured at the whole-`app/` denominator (**4 `tools.py` + 1
   `integration.py`**; a `tools.py`-only count is a FAIL per the amendment). This changes **which
   tools are resident at session start for every MCP seat**.
3. An extra `$select` field on the two message readers.

## Legs

| # | Leg | Status |
|---|---|---|
| 1 | build tarball + upload to S3 (`ec2/opal-gateway/`) | **CLOSED** |
| 2 | SSM pull + install into `/opt/opal-gateway` + `systemctl restart opal-gateway` | **CLOSED** |
| 3 | bounded readiness + `/health` 200 (G4 boot test) | **CLOSED** |
| 4 | G2 mark census **on the DEPLOYED artifact** | **CLOSED** |
| 5 | `EC2_MANIFEST` updated (commit + checksums) | **CLOSED** |
| 6 | G5 22a ladder stated | **CLOSED** |

## The cost Andrew was shown — and it is a ceiling, not an estimate

`systemctl restart` **only**: no `stop-instances`, no `start-instances`, no reboot, **no IP move**,
ALB path unchanged. `GATEWAY_WORKERS=1`, so **every in-flight MCP call is dropped** — for every seat,
on the box every seat reaches MCP through. Bounded by the script's own 30s (`is-active`) + 30s
(`/health`) loops. **Every run re-derives `/opt/opal-gateway/.env` from four Secrets Manager
secrets** (graph, fernet, jwt, 49F OTP bearer). **If the real cost exceeds this, STOP and surface —
an approval covers what the approver was shown.**

## G4 hazard, stated before the act

`requirements.txt` pins `mcp==1.28.0`; unpinned `mcp>=1.2.0` once pulled 2.0.0, which removed
`mcp.server.fastmcp` and crash-looped the service. **The pin does not change and there is no PyPI
egress decision here.** A **LOUD** failure means **REVERT, not debug**, and surface. A **SILENT**
failure is **declared NOT REACHABLE by the boot test — not ruled out, and not closed on.**

## Rollback

Re-deploy the previous artifact: the box's current bytes are recorded above
(`app/tools.py` md5 `06e1fd0a…`) and `5a1cc39e8e` is the vintage. Same wrapper, same window.
**No data mutation** — this is code + a systemd restart.

## Close-out -- APPLIED plane, read ON THE INSTANCE over SSM (2026-08-21T14:40:02Z)

```
unit            ActiveState=active SubState=running
                MainPID 12236  (was 1532)   ExecMainStart 2026-08-21 14:33:04 UTC   <- a REAL restart
bytes on box    app/tools.py        eccf03c379985e5441e8e06182cb635f  == build input
                app/teams_format.py a3e14f8d20a04ae9fbbe252ef91930c8  == build input  (NEW on the box)
                app/.../integration.py 71c67a7c9244430f894033b3de9e9ed1 == build input
G2 marks        DEPLOYED artifact: tools.py=4 + integration.py=1 = 5   (the .pyc hits are compiled
                caches of those same two sources -- NOT additional homes; counting them gives a false 7)
wiring on box   format_for_teams_html=2 | contentType html=2 | contentType text=0
listener        /health 200 | /mcp unauth 401 | AS metadata serves
G4 pin          mcp 1.28.0 -- UNCHANGED. No PyPI egress decision, and the crash-loop hazard did not fire.
```

**THE DEPLOY'S OWN rc IS NOT THE EVIDENCE HERE AND WAS NOT USED AS IT.** Rule 22a for EC2: a
producer self-report and an S3-staged object can both be true while the box runs something else.
Every line above is an on-instance read.

## ⛔ ONE LEG DID NOT CLOSE ITSELF -- the deploy LANDED and its own RECORD was REFUSED

`safe-ec2-deploy` completed (rc=0), then **its manifest-recording commit hit an owned-paths
refusal**: `EC2_MANIFEST.json` is lane `SHARED_CLOUD_OPS` and `0.5.0_AE_OpalETL~Z` is not in
`permitted_agents`.
>> **UNDER RULE 26 THE APPLY NOW RUNS ON THE DEVICE THAT OWNS THE WORK -- AND THAT SEAT IS NOT THE
LANE OWNER OF THE RECORD ITS OWN DEPLOY MUST WRITE.** The wrapper leaves the change **STAGED**, which
is also a sweep risk for the next seat's commit. Recorded at `b5eb078c27` under the sanctioned,
audited `GIT_COMMIT_AUTHOR_OVERRIDE=SHARED_CLOUD_OPS` (singular lane, manifest only). **Structural,
not a one-off -- routed to `1.0.0_SA_CTO~Z`.**

**TWO WRITE HAZARDS CAUGHT BEFORE THEY LANDED:** the wrapper rewrote all **555 lines as CRLF** for
**four** semantic changes; and re-serialising the JSON escaped **six other services' rows**, because
the file already contains **mojibake** (double-encoded em-dashes) that `ensure_ascii` would have
frozen into permanent `â€”`. Applied byte-surgically instead: every anchor asserted
unique first, mojibake preserved 6 -> 6, CRLF 0, JSON re-parsed, **10/9**.

**`file_checksums` RE-DERIVED, and two were ALREADY WRONG BEFORE THIS DEPLOY** -- `app/server.py`
and `app/audit.py` matched neither repo nor box (the box matched the repo; only the record was
stale). **Their correction is not drift from this act**, and saying so matters: an unexplained
checksum change inside a deploy record reads as exactly the drift it is not.

## Pre-existing conditions, recorded and NOT fixed here

- `tools.py` carries **7 non-ASCII lines, all pre-existing** at the deployed vintage. I introduced
  none; the box already ran them. **Widening an approved deploy to clean someone else's comments is
  scope creep**, and the approval covers what the approver was shown.
- The manifest lints WARN that `opal-gateway` declares no `telemetry`/`duty_cycle`/`autoshutdown`/
  `sizing_review`/`primary_data_bucket` (announce-then-enforce, deploy proceeds). Pre-existing.
