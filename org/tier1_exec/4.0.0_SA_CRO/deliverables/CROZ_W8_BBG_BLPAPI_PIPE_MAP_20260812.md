# W8 — BBG blpapi pipe map: what is served where, and how

**Author:** `4.0.0_SA_CRO~Z` · **Started:** 2026-08-12 ~1710Z · site Z (the Terminal box)
**Authorization:** Andrew-direct ~1702Z @`f09cbd13ef`, relayed `0.0.0_AB_MSTR~Z` 170523Z.
**Egress scope:** TRAVERSE + READ ONLY. Downloads expressly forbidden. Verification pulls are a
separate, sized ask.

> **METHOD DECLARATION — READ THIS BEFORE ANY NUMBER BELOW.**
> Every increment states its own DENOMINATOR: how many of how many, **by what instrument**, and
> what that instrument is blind to. A map that resumes cleanly but cannot say what fraction of the
> surface it covers reads complete and is not — and its author is the one person who cannot tell.
> **Nothing in this file was produced by a data pull.** Sources are: on-disk source read, `comp-find`,
> and prior committed measurement (cited with its vintage). Where a fact is inherited rather than
> re-measured, it is marked `INHERITED` with its date — an inherited measurement is a claim about
> the past, not the present.

---

## 0. STATUS / RESUME POINTER

| Increment | Covers | State |
|---|---|---|
| 1 | Ingress: services, request types, session-openers, transport | **LANDED** (this file) |
| 2 | Served axis: BBG data -> artifact -> S3 -> pipeline -> portal surface | NOT STARTED |
| 3 | Consumer/entitlement reconciliation + the sized-pull proposal (if any) | NOT STARTED |

**If this session died, resume at increment 2.** Nothing below needs re-deriving.

---

## 1. THE PHYSICAL PIPE — there is exactly one, and it is loopback

```
   Bloomberg  ──────>  bbcomm.exe  ──────>  127.0.0.1:8194   (DAPI, loopback ONLY)
                       (service)             │
                                             │  every consumer below crosses THIS ONE socket
                     ┌───────────────────────┴────────────────────────┐
                     │                                                │
              blp_client.py                                   cma env  (tia / blpapi)
           (.tools/bloomberg-mcp)                        Yang's notebooks + repo forks
                     │                                                │
              server.py (FastMCP "bloomberg")                   run_daily_pull.py
                     │                                                │
        stdio ───────┴─────── streamable-http 127.0.0.1:8790     data/model PKL
     (local Claude Code)        (SSM port-forward; NOT built)          │
                                                                (increment 2)
```

**The load-bearing property: DAPI binds `127.0.0.1`, never `0.0.0.0`** (`INHERITED`, measured
2026-07-30, NFRA_BBGMCP_PRD §1). No VPN, peering, or security-group change reaches it — **something
running ON this box must make the blpapi call.** Every remote-access design that forgets this fails
at the same place. This is why the tunnel terminates locally rather than exposing a port.

---

## 2. SERVICE AXIS — denominator 6, and we open 1

`INHERITED` — all six measured by live `openService()` on this seat, 2026-07-30
(NFRA_BBGMCP_PRD §4.2). **I did not re-probe; re-probing is a live call and the map does not need
it.** Vintage caveat: 13 days old, and §1 of that PRD explicitly warns a seat's entitlements can
change with nothing reporting it.

| Service | Open on this seat | Opened by our code | Note |
|---|---|---|---|
| `//blp/refdata` | True | **YES — the only one** | BDP / BDH / BDS / IntradayBar / IntradayTick / BEQS / Portfolio |
| `//blp/apiflds` | True | no | field discovery; PRD calls it highest-value unbuilt |
| `//blp/instruments` | True | no | security resolution |
| `//blp/tasvc` | True | no | technical studies; no demand |
| `//blp/mktdata` | True | no | streaming; **excluded BY DESIGN**, not overlooked (push-shaped vs request/response MCP) |
| `//blp/emsx` | **False** | never | order/trade. **Not reachable from this seat at all.** |

> **THE READ-ONLY PROPERTY IS AN ENTITLEMENT FACT, NOT ONLY A CODE CONVENTION.** `//blp/emsx` is
> structurally absent, so the blast radius of a client bug is bounded by Bloomberg and not merely by
> our restraint. **This must not be used to weaken the code convention** — entitlements can change
> silently — but it is the strongest single safety fact on this box.

**Blind spot of this axis:** `openService` answers *reachable*, never *entitled for a given
security*. Those are different questions and the second has already burned this estate (see §5).

---

## 3. REQUEST-TYPE AXIS — denominator 7 named on refdata, 3 implemented

Source-confirmed by direct read of `.tools/bloomberg-mcp/blp_client.py` @`f09cbd13ef` (this box, today).

| Request type | Implemented | Where | Pull class under W8 |
|---|---|---|---|
| `ReferenceDataRequest` (BDP) | YES | `blp_client.py:153` | traversal-permitted **BY CALL SHAPE, not by name** — see below |
| `ReferenceDataRequest` w/ bulk fields (BDS) | YES (same call) | `_el_to_py` array branch `:105` | same |
| `HistoricalDataRequest` (BDH) | YES | `blp_client.py:211` | **PULL — sized ask required** |
| `IntradayBarRequest` | YES | `blp_client.py:265` | **PULL — sized ask required** |
| `IntradayTickRequest` | NO | — | docstring once claimed it; never existed |
| `BeqsRequest` (screens) | NO | — | proposed |
| `PortfolioDataRequest` (PORT) | NO | — | proposed |

> ### ⚠ THE EGRESS LINE SITS ON THE CALL SHAPE, NOT THE TOOL NAME.
> The constraint as issued draws the boundary at the tool name: historical/intraday are pulls,
> health/reference are not. **That line is not sufficient, and I am recording why before making a
> single call.** `reference_data` sits on the permitted side and can still harvest content if asked
> enough times with a wide enough field list — N securities x M fields, iterated, is a data
> acquisition conducted entirely through "allowed" calls, and a tool-name rule **reads GREEN on it.**
> **OPERATIVE RULE FOR THIS SEAT:** `reference_data` is used for SCHEMA/METADATA resolution only
> (does this identifier resolve, what is this field's shape). The moment a call's purpose is to
> obtain the values themselves, it is a pull — it stops and gets sized.
> *(Elevated by `0.0.0_AB_MSTR~Z` 170828Z as an amendment to CTO~Z's constraint 3, credited here.)*

**Session model:** every public function opens a session, runs ONE request, and stops
(`blp_client.py:150,208,262`). Correct for today; the PRD flags it as the first bottleneck under
concurrent gateway callers.

---

## 4. SESSION-OPENER AXIS — who can actually touch the socket

**Denominator by instrument:** `comp-find "blpapi"` -> **53 hits across 25,663 files scanned, 1
UNREADABLE and not searched**; bands DEF=6, SURFACED=21, DOC=26. `comp-find "//blp/"` -> 35 hits,
bands HEAD=3, SURFACED=6, DOC=26.
**What this instrument is blind to:** it counts LINES in the tracked repo. It cannot see Yang's
live OneDrive notebooks (out of repo, and they are the production source), and per CLAUDE.md Rule 21
a comp-find count is never an AST-node denominator.

| # | Session opener | Env | Path | Role |
|---|---|---|---|---|
| 1 | `blp_client.py` | MCP server env | `.tools/bloomberg-mcp/` | the agent-facing surface (4 MCP tools) |
| 2 | `bloomberg_entitlement_probe.py` | `cma` | `org/tier0_utility/0.0.3_BG_BBGTerminal/deliverables/` | the 3-layer entitlement discriminator |
| 3 | Yang notebooks via `tia` | `cma` | `workflows/bloomberg/{tplus1,tzero}/src/` | the production daily pull (repo forks) |
| 4 | Yang notebooks via `tia` | `cma` | OneDrive `202511 Model Portfolio Exposure/src/` | **the live production source — OUT OF REPO** |

**TWO INTERPRETERS, DELIBERATELY** (`scheduled_daily_pull.cmd:77`): the pull needs `cma`
(`C:\Anaconda\envs\cma\python.exe`, has tia/blpapi); the publisher needs boto3, which `cma` does not
have, so it runs under Python311. **A green `bloomberg_health` from the MCP server therefore does
NOT prove a runnable pull** — different interpreter, different process, different session. This is a
live instance of "the instrument's domain is not the question asked."

---

## 5. WHAT NO INSTRUMENT ON THIS BOX CAN TELL YOU — the entitlement blind spot

This is the single most important thing in increment 1, and it is a NEGATIVE result.

`INHERITED`, measured, from `BLOOMBERG_TERMINAL_SIGNIN_RECOVERY.md` (P0 block, 2026-08-12):

| Date | `bbcomm` | `wintrv` | `bloomberg_health` | Entitlement | Lesson |
|---|---|---|---|---|---|
| 2026-08-11 | up | dead | `ok:false` | **DEAD** 12.5h | a running `bbcomm` is **not sufficient** |
| 2026-08-12 | up | **absent** | `ok:true` | **LIVE** | a running `wintrv` is **not necessary** |

**`bloomberg_health` read cleanly through both states, so it cannot discriminate either.** It is an
instrument that could not have said otherwise. Neither the process list nor the health check answers
*"is the entitlement live."*

> ### ⛔ THE ONLY DISCRIMINATING TEST IS ITSELF A PULL — AND SO I DID NOT RUN IT.
> The runbook's sole proven discriminator is resolving the `.ST` custom index: a
> **HistoricalDataRequest** expecting ~683 rows from inception `2023-12-29` @ `100.0000`.
> **Under W8's constraint that is a DATA PULL requiring a sized ask.** So the map records the
> honest state: **the entitlement is UNVERIFIED BY THIS SEAT, and verifying it is out of scope
> without a separate authorization.**
> I did **not** substitute `bloomberg_health` for it — a clean `ok:true` is exactly the
> could-not-have-said-otherwise reading that produced the 12.5h outage's false comfort.
> **And I did not attempt a Terminal sign-in:** `wintrv` is absent today, the P0 gate states plainly
> that absence is NOT evidence a sign-in is needed, a failed login is not free, and Bloomberg locks
> the account on repeats. Acting on the natural inference here converts a non-problem into a lockout.

**Standing gap, quoted from the runbook and NOT to be closed with a monitor:** *"Nothing detects a
dead Terminal."* The 07:00 ET scheduled pull has no DAPI-liveness precondition. Per the standing
alarm moratorium this is a **route/schedule design question**, and an alarm is the wrong deliverable.
Already routed to MSTR~Z for CTO/Andrew disposition — I am not re-opening it, only recording that
the pipe map's health axis terminates here.

---

## 6. INCREMENT 1 COVERAGE STATEMENT (the denominator of the map itself)

| Axis | Enumerated | Of | By instrument | Confidence |
|---|---|---|---|---|
| blpapi services | 6 | 6 | live `openService` probe, `INHERITED` 2026-07-30 | high, **13d stale** |
| refdata request types | 7 named / 3 built | 7 | source read @`f09cbd13ef`, today | high |
| in-repo session openers | 3 | 3 | `comp-find`, 53 hits / 25,663 files | high |
| out-of-repo session openers | 1 known | **UNKNOWN** | none — structurally invisible to repo tooling | **LOW — see below** |
| transport paths | 3 (stdio, http:8790, SSM) | 3 | source read + PRD gates | high; 2 of 3 NOT BUILT |
| served surfaces | **0** | unknown | not started | increment 2 |

> **THE HONEST HOLE:** the *live production* notebooks are on OneDrive, outside the repo, and no
> repo instrument can enumerate them. The repo forks are documented as differing from production in
> exactly two ways — but that is a claim in a README, not a measurement I have made. **Any statement
> of the form "the estate's BBG surface is fully enumerated" would be false at this line.**

---

## 7. TRANSPORT / REACHABILITY STATE (not built — stated so it is not assumed)

| Gate | State | Owner |
|---|---|---|
| AWS creds on this device | **SATISFIED** (`INHERITED` 2026-07-30) | — |
| IAM role + `aws_ssm_activation` | open — **must precede the MSI** | CloudOps |
| SSM Agent MSI (one-time admin) | **NOT INSTALLED** | Andrew |
| `server.py` streamable-http on :8790 as a service | **NOT LISTENING** | CloudOps |
| Bloomberg registered as a gateway backend | open, follows the rename | CloudOps |

**Consequence for W8:** the only live path to these pipes today is **local, on this box**. There is
no remote consumer of the Bloomberg MCP surface right now, which materially bounds what "served
where" can mean in increment 2.

---

*Increment 1 ends here. Nothing in it required a Bloomberg call.*
