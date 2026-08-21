# Deploy-completion ledger — gateway server rename `m365-gateway` -> `opal-gateway`

**Status:** CLOSED 2026-07-31 (in-session; behaviourally verified; SUPERSEDED by the 08-15 opal-gateway cutover, LD-0414/0415)
<!-- scanner-alignment line added 2026-08-18 by 0.0.0_AB_MSTR (RED-disposition act, org/tier0_exec/0.0.0_AB_MSTR/deliverables/DEPLOY_LEDGER_RED_DISPOSITIONS_20260818.md): mirrors this file's own close declaration below; deploy_ledger.py's unindexed scanner could not read the original form (defects A/B/shape-C, see the disposition doc). Not a new closure. -->

**Opened:** 2026-07-31 ~01:45Z (at deploy-start, per CLAUDE.md NEVER#6)
**Owner:** `0.7.0_AE_CloudOps~Z` (site Z) · **Service:** `m365-mcp-gateway`, instance `i-07dccb1615503ac99`
**Code commit:** `042f96d44` (committed + pushed BEFORE deploy, Deployment Rule 2)
**Deploy path:** `infra/aws/ec2/safe-ec2-deploy.sh m365-mcp-gateway infra/aws/ec2/m365-mcp-gateway/deploy-to-ec2.sh` (Rule 7 — never the service script directly)

**Authorization:** Andrew-direct, relayed by `0.0.0_AB_MSTR~Z` `20260731T014056Z`, VERBATIM:
> *"just sort out the gateway split, i dont care i can reinstall it on alyssas computer or give her
> instruction to reauthenticate or whatever"*

Discharges the hold I placed at `20260730T223838Z`. The hold was correct and is retired by the
sovereign, not by peer override.

## What this deploy DOES and DOES NOT do — stated because the premise moved twice

- **DOES:** change `serverInfo.name` in the MCP handshake from `m365-gateway` to `opal-gateway`,
  and ship an 18-line comment at `tools.py:37` recording the measured key-vs-name fact.
- **DOES NOT:** change any client-visible tool name. **The `mcp__<prefix>__` segment comes from the
  client's REGISTRATION KEY, not this string** — measured 3/3 (`m365`→`mcp__m365__`,
  `opal-agent-comms`→`mcp__opal-agent-comms__*` with hyphens intact, `playwright`→`mcp__playwright__*`).
  Bloomberg would still land as `mcp__m365__*` after this ships.
- **The comment is the durable half.** The misleading string is what produced the wrong section-3
  premise; deleting it silently would leave the trap for the next reader.

## Pre-deploy checks (measured, not assumed)

| Check | Result |
|---|---|
| Drift between `deployed_commit` `c390d1c6a` (2026-07-15) and HEAD, scoped to the gateway tree | **Exactly ONE commit: `042f96d44`, 1 file, +18/-1.** No hitchhiking changes — the deploy ships only the intended change |
| `commit-gate.sh` on `tools.py` | PASS |
| Live traffic on this endpoint | **Real and current** — 55,878 audit records; andrew 54,976 (through today), alyssa 895 (through today). Deploying a live OAuth endpoint, not an idle one |
| Deploy window | ~01:45Z, lowest-traffic window of the day |

## Legs

| # | Leg | Status |
|---|---|---|
| 1 | ledger opened at deploy-start | **DONE** |
| 2 | code committed + pushed before deploy (`042f96d44`) | **DONE** |
| 3 | drift check — only the intended commit in range | **DONE** |
| 4 | deploy via `safe-ec2-deploy.sh` (Rule 7) — **code leg landed, wrapper then died; see 4a** | **DONE** |
| 4a | **HALF-LANDED, repaired in-session** — manifest leg stranded by a charmap crash | **DONE** |
| 5 | **LIVE-PLANE verify** — on-box file, service state, and BEHAVIOURAL response | **DONE** |
| 6 | ledger CLOSED in-session | **DONE** |

## Leg 4a — the deploy half-landed, and the failure was cosmetic-looking but not cosmetic

`safe-ec2-deploy.sh` returned **rc=1** after the SSM step had already reported
`OK: deploy Success (ssm:84d7f05d-cb2d-4551-9d59-72040c6c08f9)`. The wrapper then died on:

```
aws: [ERROR]: 'charmap' codec can't encode characters in position 434-473
ERROR: Deployment script failed. Manifest not updated.
```

**So the CODE deployed and the MANIFEST did not** — precisely the half-landed state NEVER#6 exists
for. Rule 8 makes `EC2_MANIFEST.json` the source of truth, so a stranded manifest leg leaves the
estate's own record asserting `c390d1c6a` / `0.2.0_DT_PortfolioAnalytics` / `2026-07-15` while a
different commit runs on the box — **an instrument that reads confidently and is wrong.**

Repaired in-session with the wrapper's own jq semantics (`safe-ec2-deploy.sh:184-186`), same four
fields. **`deployed_commit` records `48e1fceaf` — the commit actually packaged — NOT HEAD.** HEAD had
moved to `78872c30c` (CVO's overnight work merging in) between deploy and repair; recording HEAD
would have claimed a deploy that never happened. The gateway tree is byte-identical across that
range (empty diff), so the code is current either way — but the field means *what was deployed*.

**Root cause is the estate's own non-ASCII rule biting the deploy path on Windows:** the wrapper
emits box-drawing/check glyphs and the CLI's cp1252 stdout cannot encode them. CLAUDE.md § Code
Quality already forbids non-ASCII "in production code, logs, or anything that runs on AWS" — this is
that rule's violation *inside the deploy tooling itself*, and its cost is a silently stranded leg
after a SUCCESSFUL deploy. **Any EC2 deploy run from site Z will strand its manifest leg the same
way.** Routed, not fixed here (deploy-wrapper ownership sits outside this lane).

## LIVE-PLANE verification (leg 5) — three layers, config through behaviour

| Layer | Check | Result |
|---|---|---|
| Artifact | on-box `/opt/m365-mcp-gateway/app/tools.py` | `:54` `FastMCP("opal-gateway", ...)` — new name present (line moved 37→54 by the 18-line comment, itself confirming the comment shipped) |
| Process | `systemctl is-active` + `ActiveEnterTimestamp` | `active`, entered `2026-07-31 01:46:21 UTC` — restarted at deploy, not a stale process |
| Socket | `ss -lntp` | uvicorn pid 1449219 listening `0.0.0.0:8080` |
| **Behaviour** | `GET https://mcp.opalinvest.dev/mcp/` | **HTTP 401 in 0.87s** — app UP and enforcing auth. A dead app returns 502/503, so this discriminates |
| **Closed loop** | that probe in the server's own journal | `01:49:58 ... "GET /mcp/ HTTP/1.1" 401 Unauthorized` — **my request appears in this instance's log**, proving the probe reached THIS box and not an edge cache |
| Health | ALB checks since restart | `GET /health 200 OK` every 15s from both nodes, zero errors |

## CLOSED — outcome

**Rename deployed, behaviourally verified, manifest repaired, nothing stranded.** The gateway now
self-identifies as `opal-gateway` in the MCP handshake.

**And it changed nothing client-visible, exactly as predicted** — tool prefixes still read
`mcp__m365__*` because those come from the registration key. That is not a defect in this deploy;
it is the finding this deploy was re-scoped around, and the `tools.py:54` comment is what carries it
forward.

**Remaining, not mine:** client key `m365`→`opal` (MSTR, this device) · `teams-assist` literals →
bare names (MSTR) · Alyssa's machine (Andrew, by his own word).

## Rollback

Redeploy the parent commit (`042f96d44^`) via the same wrapper. The change is a single string plus
comments — no schema, no state, no data migration. Nothing to unwind beyond the redeploy.

## NOT in this deploy (split, per MSTR `20260731T014056Z`)

- **Client registration key `m365` -> `opal`** — MSTR owns this device's `~/.claude.json`; Andrew
  owns Alyssa's machine by his own word. Per-device config, not a deploy.
- **`teams-assist/SKILL.md` literals** — MSTR, converting to BARE tool names rather than
  re-hardcoding `mcp__opal__`. Verified support: **zero** permission-allowlist entries encode the
  prefix (`.claude/settings.json`, `settings.local.json`, `~/.claude/settings.json` all 0), so bare
  names carry no hidden dependency. Bare names are also correct in BOTH key states simultaneously,
  which removes the transition ordering constraint rather than managing it.

---

## ON-BOX RESOLUTION OF THE CONTESTED DEPLOY DIRECTORY — 2026-08-21T02:2xZ (`0.7.0_AE_CloudOps`, LD-0428)

**Why this section exists.** The `D7_TICKETING.GW-APPLY` TO recorded this record and the
`20260815T0230Z_opal-gwrename-s3-cutover` record as a **CONTESTED PAIR** on the gateway's deploy
directory: this record's leg-5 artifact row verifies `/opt/m365-mcp-gateway/app/tools.py` serving,
while the 08-15 record says S4-14 deployed to `/opt/opal-gateway` and S6-15 REMOVED
`/opt/m365-mcp-gateway`. Site Z marked it CONTESTED rather than flipping it record-vs-record, and
the TO's ruling was **only the box settles it** — `safe-ec2-deploy` needs the right destination.

**⛔ THE SUPERSEDED MARKER ON LINE 3 WAS ALREADY CORRECT, AND IT WAS NOT YET EVIDENCE.** It landed
2026-08-18 @b9df62247f as part of MSTR's RED-disposition sweep — a **record-derived inference** from
the 08-15 record, i.e. exactly the record-vs-record act the TO declined to rely on. This section does
not change its verdict; it **grounds** it. A correct conclusion reached from the wrong plane is still
the wrong plane, and the next reader needs to know which one they are holding.

**Method — APPLIED/EXECUTING truth, not a staged read (CLAUDE.md Rule 22a).** Two read-only
`AWS-RunShellScript` SSM invocations against `i-07dccb1615503ac99`
(`ad2fc9fd-80d8-457d-a826-d3b2694fb318`, `0aa6ca13-1045-458b-aa85-6cd3816dd65c`, both `Success`,
empty stderr). Rule 22a's EC2 clause binds: an S3-staged object may be inert, so the oracle is the
**running process**, read through `/proc`.

| Layer | Measurement | Result |
|---|---|---|
| Unit files present | `ls /etc/systemd/system/ \| grep -iE 'gateway\|m365'` | **`opal-gateway.service` ONLY** (950 B, Aug 20 16:19) |
| Unit state, both names explicitly | `systemctl show -p LoadState/ActiveState` | `opal-gateway.service` **loaded/active/running/enabled**; `m365-mcp-gateway.service` **`load=not-found`** — the unit does not exist, it is not merely stopped |
| ExecStart | `systemctl show -p ExecStart` | `/opt/opal-gateway/.venv/bin/uvicorn app.server:app --host 0.0.0.0 --port 8080` |
| WorkingDirectory | `systemctl show -p WorkingDirectory` | `/opt/opal-gateway` |
| **EXECUTING TRUTH** | `readlink -f /proc/2249865/cwd` | **`/opt/opal-gateway`** (MainPID 2249865, cmdline `/opt/opal-gateway/.venv/bin/python3.11 .../uvicorn app.server:app`) |
| Contested path A | `[ -e /opt/m365-mcp-gateway ]` | **ABSENT** |
| Contested path B | `[ -e /opt/opal-gateway ]` | **EXISTS**, 126M, mtime 2026-08-20 16:19:20 UTC |
| `/opt` full inventory | `ls -la /opt` | exactly two entries: `aws`, `opal-gateway` — the ABSENT verdict has its denominator |
| **NEGATIVE CONTROL** | `[ -e /opt/zzz-no-such-gateway-9999 ]` | **ABSENT** — the instrument discriminates; the ABSENT verdict above is not an undiscriminating "no" |

**VERDICT: record (B) — `20260815T0230Z_opal-gwrename-s3-cutover` — is CORRECT ON THE BOX. This
record's leg-5 artifact row (`/opt/m365-mcp-gateway/app/tools.py`) was TRUE WHEN WRITTEN on
2026-07-31 and is SUPERSEDED IN FACT: that tree no longer exists, and its systemd unit is
`not-found`.** The canonical deploy destination for `safe-ec2-deploy` is **`/opt/opal-gateway`**,
which also matches `EC2_MANIFEST.json`'s `remote_path` (a third record, now grounded rather than
merely concurring). **The historical rows above are NOT edited** — they are a closed ledger's record
of what was true at its own vintage; this section is the annotation, per the TO's "annotate, never
flip record-vs-record."

**RESIDUAL, SURFACED NOT CHASED (routed to COO, no action taken here):**
`infra/aws/terraform/opal-gateway/main.tf:191` user-data still runs
`install -d -o ec2-user -g ec2-user /opt/m365-mcp-gateway` — so **an instance REPLACEMENT would
re-create the old path** and the box would diverge from this resolution on first boot. Not touched:
a TF change is an apply act, and no GO covers it.

Read by `0.7.0_AE_CloudOps` under the LD-0428 item; discharges the `D7_TICKETING.GW-APPLY`
prerequisite only — **it opens no apply and closes no G-criterion of that TO.**
