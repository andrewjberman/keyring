# 0.0.3_BG_BBGTerminal — F8 relaunch, an Andrew-facing message-loss defect, and the OPAL_ANALYST speed addendum — 2026-08-20 1600–1840Z
**archetype:** SERVE + VALIDATE

---

## >> SUCCESSOR: TWO DUTIES ARE WAITING ON YOU. READ THIS BLOCK FIRST. <<

### DUTY 1 — S2 ACCEPTANCE (one-time, fires on YOUR launch, not mine)

`ENABLE_TOOL_SEARCH auto:25` was applied to this seat's launcher block **@e23b879dad**
(MSTR~Z, 2026-08-20 ~1838Z). **The env reads AT LAUNCH**, so my session never saw it —
**you are the first session that will.**

**What to report:** did you reach your **first Teams ACK with ZERO `ToolSearch` calls?**
Report to MSTR~Z + CTO~Z. If any of the six hot gateway tools still defers at `auto:25`,
**say so** — the config line then drops to `"false"`.

The six: `send_chat_message`, `read_chat_messages`, `poll_addressed_teams_messages`,
`whoami`, `ack_messages`, `opal_data_refresh_upload`.

⚠ **THE BASELINE, because "zero" is only checkable against a known prior and you have no
memory of mine:** this session made **FIVE** `ToolSearch` schema loads before its first
outbound act — `send_chat_message`, `whoami`, `read_chat_messages`,
`poll_addressed_teams_messages`, `ack_messages`. Five is the number S2 is trying to make
zero. **Without this line you cannot tell a pass from an ordinary morning** — you would
launch, notice nothing unusual, and the acceptance would silently never happen.

### DUTY 2 — S1 LIVE POSITIVE (A5), if it has not already occurred

The teams-watch message-grain fix (**@7e138ad6ef**) is LIVE. **A5 = the first REAL
multi-message exchange from Andrew delivered complete** — both messages, in order, carrying
the `(1 of 2)` / `(2 of 2)` frame.

**DO NOT MANUFACTURE IT.** Do not seed his chat to close the item; a control you generate
is one that could not have failed. It closes on his natural traffic or not at all.

When it happens: **confirm IN-THREAD to Andrew and retire the interim re-send rule in the
same message** (the rule he is currently operating under: *"if I ever answer only your most
recent message, assume I never saw the earlier ones and re-send"*). Then report to CTO~Z +
AE~Z. S1 sits `ACCEPTED-PENDING-LIVE-POSITIVE` until you do.

---

## VERDICT: seat relaunched and serving; W6-T1 closed; a live Andrew-facing defect found, fixed, and re-armed inside one hour.

| Leg | State | Evidence |
|---|---|---|
| F8 identity binding | **CLOSED** | W6-T1 accepted @8460648ef9 — three legs each with a control |
| Startup | ALL GREEN | both Monitors, whoami PASS, DAPI + `cma` exercised, 0 crons |
| Teams message loss | **FIXED + LIVE** | S1 @7e138ad6ef, 23/23, re-armed task `bbk8u5v67` |
| Speed addendum | **RATIFIED** | OPAL_ANALYST_PRD §11 @208a4f3b57, my budget = scope law |
| A5 live positive | **PENDING ANDREW** | see Duty 2 |

## 1. F8 live positive (W6-T1)

Launched via `ajb` 16:00:03Z, session `00a52644`. `.launch-path` (`bg-concierge …
launcher=ajb.ps1 host=OPAL_BLOOMBERG`) + `.serial` both present, both written by the
launcher — G1 forbids this seat `org/mcp/**`. **Negative control was not hand-chosen:** my
own reaped prior session `245e7a44` has NEITHER file. Estate denominator: `*.launch-path`
= 1, `*.serial` = 69. Fence resolved **ACTIVE-ENFORCE**. Classed call `Write ->
docs/.f8-probe-DELETE-ME.md` **DENIED**, and the **effect verified** by the file's absence
afterward; the same `Write` tool through the same live hook PASSED to an allowlisted path
in the same minute. Accepted @8460648ef9.

## 2. The defect — teams-watch dropped an Andrew message

Andrew ran an unannounced responsiveness test. He sent **two** messages; **I received only
the second.**

```
18:00:12.095Z  Andrew  "What is year to date performance on the ST model"   NEVER DELIVERED
18:01:07.797Z  Andrew  "What is the interval on your polling..."            delivered
18:01:58.9Z    teams-watch emits ONE [TEAMS] line (the second message only)
```

Two layers. **(1) Latency, 51.1s** — expired pinned token, TO6 quiet-retry backoff widening
the poll 15s -> 90s. Correct behaviour; not the fault. **(2) The defect** —
`poll_addressed_teams_messages` returns **one entry per CHAT carrying the LATEST message**.
A chat-grain instrument read as a message-grain one. Two messages in one window => the
earlier is **dropped, not queued**, and the cursor advances past it. Layer 1 made it land
today; **the loss is available at any interval.**

**Why it evaded my own checks:** I ran that exact poll at startup, got `count 0`, and
recorded "Teams backlog 0". That was **true about chats and warranted nothing about
messages** — `count: 0` never says "0 of what". The designed half of the denominator class:
no way of *calling* it differently fixes it, only corroborating **outside** it does, which
is what `read_chat_messages` did.

**Historical incidence: UNKNOWABLE, and I quoted no count.** A dropped message leaves no
trace anywhere this seat can read. Confirmed lost = 1, a floor. **Andrew DECLINED the
backfill sweep** (*"no this is not necessary no one uses you but me"*) — question CLOSED,
recorded in §11; nobody re-raises it.

## 3. Served

**ST (Short Term) YTD +2.33%**, `data_as_of` 2026-08-19 (T-1 by design = current). Index
bm +2.21% (+0.12), ETF bm +2.31% (+0.02); vol 3.2 vs 4.4 / 5.01. Model-DESIGN caveat
delivered with the number. Denominator printed: 5 models (UST/ST/INT/LT/ULT); confirmed I
read **ST**, not the adjacent **UST** at +1.91%.

## 4. The measured latency budget (now §11's scope law)

Question -> answer = **5m45s**. Retrieval inside it = **0.92s = 0.3% of elapsed.**

| stage | measured | class |
|---|---|---|
| detection | 51.1s | architectural (polling) |
| wake hop | **UNMEASURED** | **refused to rank it** |
| turn overhead | ~55s | 5 deferred-schema round trips -> **S2** |
| research | ~8 serial calls | partly collapsible -> S5 |
| retrieval | 0.92s | **NOT the bottleneck** |

**The data layer is not the bottleneck and no pipeline work on it will help.** That
sentence became the addendum's scoping law. Program: S1 message-grain fix (done) · S2
resident schemas (applied, awaiting your acceptance) · S3 wake hop by hand · S4 routing
call (gated, Andrew widening) · S5 one-call retrieval · S6 push-not-poll (gated, design
first). Target **~60s** pre-S6.

## 5. One correction I sent upward

CTO~Z's re-arm instruction asserted *"TaskStop does NOT reap the child."* **This instance
it did** — I ran the kill step and found nothing to kill (wrapper 1398721 + python 1399107
both gone). Accepted at the gate; the durable form is **verify the census by pid, kill only
what survives.** Assuming in *either* direction is the error: assume-survives and you kill
a process you do not own; assume-reaped and you arm a second poller onto one cursor file —
**re-manufacturing this very defect through its own repair.**

## Compiler Tools

| Tool | Result |
|---|---|
| `comp-which` availability (A.3) | OK — resolves at `~/bin/comp-which` |
| comprail Gate-1 | **FIRED** on my `infra/*.tf`-path grep of DATA_CATALOG.yaml; re-run with an audited `# rail-checked:` marker naming why no comp-tool models a seat-local request-routing table. Correct behaviour; logged as a round-trip cost in the latency budget. |
| `portal_lookup.py get/channels` | the sanctioned portal path — timed 3x (0.922/0.876/0.950s) as budget evidence |
| Not run | `comp-estate` / `comp-iam` / `comp-kuzu` — no estate-topology, IAM or cross-layer graph question arose; this seat reads served artifacts and Teams, and the one search that touched an infra path was rail-checked rather than routed. |
