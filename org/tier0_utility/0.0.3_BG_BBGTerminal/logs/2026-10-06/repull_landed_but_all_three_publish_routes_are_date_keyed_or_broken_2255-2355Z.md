# The re-pull landed fresh data, and all THREE routes to the portal are date-keyed or broken

**archetype:** MIXED

**Window:** 2026-10-06 22:55Z - 23:55Z | **Seat:** 0.0.3_BG_BBGTerminal | **Trigger:** Andrew's
GO on the PKL rename (msg 30404), then his publish-leg order (30412), both under the fabric HOLD
with my re-pull as the named carve-out (30394).

## Current State

**The fresh 2026-10-05 PKLs exist and are correct. NOTHING I CAN DO PUBLISHES THEM.** The served
benchmark artifact is still the pre-fix one. One act remains and it is not mine to trigger: the
gateway send once hotfix OG-rl-10 is live (2.0.0_SA_COO~O owns the release).

## What landed

**Rename** (Andrew verbatim, 30404: *"sure just overwrite them"*; MSTR's reading -- rename to
"v1 bkp", keep a copy, delete nothing, only those two files):

| | before | after |
|---|---|---|
| `data 20261005 v1.pkl` | 8,710,610 B @ 08:27:16 | -> `v1 bkp.pkl`, byte-identical |
| `model 20261005 v1.pkl` | 17,919,590 B @ 08:29:04 | -> `v1 bkp.pkl`, byte-identical |
| unsuffixed `v1.pkl` remaining | 2 | **0** (so the reuse branch CANNOT fire) |

Pre-checked for collision first: 0 existing `*20261005*bkp*`, and the `*20261005*` denominator was
**2**, so the rename provably touched those two objects and no third.

**Re-pull** (tplus1, target 20261005): exit 0, `RESULT: PASS`. **Fresh pull PROVEN, not assumed --
0 `Loading existing data` lines and 0 `FAIL:`.** Both halves differ from their backups by SHA256.

> **The model PKL's byte count is IDENTICAL to its backup (17,919,590 both).** Only the hash
> separated them. Had I reported on size I would have called the model half unchanged. **A byte
> count is not a content check, and here the coincidence was exact.**

## The CIX fix is PARTIAL -- 4 of 13, measured with a control

| series | OLD | NEW | rows | |
|---|---|---|---|---|
| `.INT_BMK` `.LT_BMK` `.ST_BMK` `.UST_BMK` | 2026-09-29 | **2026-10-05** | 718->722 | ADVANCED |
| `.LT_ETF` `.ST_ETF` `.UST_ETF` | 2026-09-29 | 2026-09-29 | 718->718 | **STILL STALE** |
| the other 6 | 2026-10-05 | 2026-10-05 | 722 | same |

POSITIVE CONTROL `SPX Index` held at 2026-10-05 / 1446 rows, so the comparison discriminates.
Null count 0 before and 0 after -- no regression. Yang fixed the `_BMK` definitions, not the
three `_ETF` ones. Routed to Andrew, who is messaging Yang himself (30422).

> **My first benchmark check returned "0 of 0 custom CIX columns" -- a WRONG-OBJECT ZERO.** I
> assumed `return_daily` was wide-by-ticker; it is 115,139 rows of LONG format with a `bbg_ticker`
> column. Reported as-is, that tidy zero reads as "no benchmarks present". The denominator line
> (6 columns against 115k rows) is what exposed it. **A zero from the wrong shape is
> indistinguishable from absence, and it arrives looking complete.**

## THREE ROUTES, ALL CLOSED -- and the first two fail for the SAME reason

1. **Gateway `/data-refresh`:** `{"error":"portal login 403","integration":"opal_portal"}`, twice.
   Not transient. **MSTR~Z reproduced it byte-identically from its OWN gateway identity** -- two
   distinct identities failing the same way localises the fault to the gateway's service login,
   away from my credentials. Hotfix OG-rl-10 pending.
2. **Publish leg** (`publish_to_portal.py`, Andrew's order 30412): rc=0, every tripwire check
   PASS, then `SKIP: portal already serves data_as_of 2026-10-05 ... NOT re-firing the pipeline.`
   **GATE 3 is `if live == iso: SKIP` -- pure date equality**, and the script has no force
   argument and is under Andrew's no-modify order.
3. **The notebook** (yesterday's finding): `if os.path.exists(pkl_data): pickle.load(f)`.

>> **1 and 3 are the same defect at two layers: both assume a DATE identifies its CONTENT.** This
>> operation is "same date, corrected content", which is the one case neither can express. The
>> rename defeated layer 3; nothing in my reach defeats layer 2. Reported and STOPPED on Andrew's
>> own instruction ("If it refuses, send its reason and stop") -- I did not route around a gate
>> whose comment says it exists so a retry cannot re-fire live data.

## Null census on the artifact that actually feeds the view

`json/benchmarks/model_portfolio_benchmarks.json`, `data_as_of 2026-10-05`,
`generated_at 2026-10-06T16:16:50Z`, 19,610 B. 5 models x 10 periods = 50 cells per field.

| field | cells | null | |
|---|---|---|---|
| `index_benchmark` | 50 | **50** | ALL NULL |
| `index_benchmark_volatility` | 50 | **50** | ALL NULL |
| `index_spread` | 50 | **50** | ALL NULL |
| `etf_benchmark` / `etf_spread` | 50 | 40 | partial |
| `etf_benchmark_volatility` | 50 | 43 | partial |
| `model` / `model_source` | 50 | **0** | populated |
| `model_volatility` | 50 | 15 | partial |

**288 of 450 return cells null.** The models are healthy; only the benchmark columns are empty --
exactly the "Index view not displaying properly" Andrew described.

> **CORRECTION TO MY OWN EARLIER REPORTING, and it ran for hours.** I had been quoting
> `json/latest/manifest.json` (`generated_at 12:32:48.874590Z`) as "the served state" at 18:12Z,
> 18:42Z, 19:0xZ and 23:0xZ. The benchmark question is served from a DIFFERENT object,
> `json/benchmarks/model_portfolio_benchmarks.json` (`16:16:50Z`) -- which is also the publisher's
> own `SERVED_KEY`. When the publisher cited a timestamp I had never seen, **the discrepancy was
> mine.** Two served artifacts, one question, and I had picked the wrong one and re-read it four
> times without ever testing that it was the right object. Re-reading the same wrong source is not
> corroboration.

## Teams back online -- and a near-miss in the other direction

Andrew restored the OAuth; **step-2a gate PASSED** (`whoami` -> "Opal Bloomberg", not Andrew).
Census: 7 of 7 chats (`@odata.count` 7, a full census not a page).

Found on the Yang Liu thread -- **which was absent from `threads/INDEX.md` entirely despite traffic
back to 2026-07-13**: Yang 2026-10-02 *"plz let Lauren know that the screener data is updated"*,
answered *"will do thanks!"*. Surfaced as UNVERIFIABLE, not as a failure: no Lauren chat on this
account, and `search_email` is scope-denied to my identity (`identity_scope_denied`, OPAL_ANALYST
PRD 4.3 -- the fence working; I did not route around it). **Andrew closed it himself** (30422,
*"all recs approved i will handle messages directly"*); I post to neither party. Dir + INDEX row
created at RELEASE; see `threads/2026-10-06-yang-liu/`.

> **Both halves of that read were traps.** The chat list looked CLEAN because every thread's last
> message was a "thanks!" or came from this account -- but a thread ending in my own ACK is the
> exact shape of an ask never answered. And I nearly filed it as MY dropped task when the gateway
> was unauthenticated at that timestamp, so this seat could not have sent it. **Checking whether
> the credential was live at the message's time is what separated an agent's lapse from a human's
> commitment.**

## HOLD compliance and RELEASE

Held from 22:08Z: no writes, drains, deploys or pushes; reads and watcher re-arms only. The
re-pull and its send were the named carve-out (30394), grounded in Andrew's own ordering rather
than MSTR's reading. I declined to write even a session log during the freeze.

**RELEASE verified independently:** HEAD and `git ls-remote origin CLOUD` both read
`b60156b7bd82d84de5245f42cd5f5a3f9f25deec`, matching MSTR's claim -- so this morning's logs,
reported LOCAL earlier, are now on origin.

## bbcomm, 7 samples: stable, still no Terminal UI

15:21Z -> 21:40Z, same pid 14404 throughout, 8194 listener always 1, `wintrv` ABSENT at every
sample, `.ST_BMK` resolving at 115.9929824176067 at the last. **Still NOT established** that it
survives to the 07:00 fire; 6h19m of evidence is not 14 hours, and R1 is still unfixed beneath it.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| `comp-read publish_to_portal.py --for` | why it skipped | found GATE 3 at :161-168 and `SERVED_KEY` -- this is what identified the date-equality defect AND my wrong-artifact error |
| `comp-read run_daily_pull.py --for` | the reuse branch | found cell 16's `os.path.exists` |
| `.tools/aws s3api get-object` | read the served benchmarks artifact | 19,610 B; **rc=0 wrote NOTHING on a `/tmp/` path first** (MSYS rewrote it) -- re-ran via PowerShell with a native path |
| `portal_lookup.py get benchmarks ...` | the right served object | `data_as_of 2026-10-05`, vintage quoted |
| `list_chats` / `read_chat_messages` | Teams census | 7 of 7 chats; the message read was a PAGE (`@odata.nextLink` present) and is labelled so |

**What failed / gaps:**
1. **The `/terminal-upload` skill's variant path is stale** (`workflows/bloomberg/<variant>/`; real
   home `integrations/bloomberg/pipeline/<variant>/`). Second log in a row carrying this; I can
   write neither copy of the skill.
2. `comp-find 'run_daily_pull' --files` exceeded 120 s and was backgrounded; `Glob` answered in
   under a second.
3. A send was **REFUSED by the broker at 153 words** against Rule 31's 150-word cap. Cut to ~138
   rather than reach for `send_override` -- that escape needs a human operator's request.
4. `search_email` scope-denied to this identity -- recorded as a real capability boundary, not a
   bug, and the reason the Lauren question stayed unverifiable rather than becoming a claim.
