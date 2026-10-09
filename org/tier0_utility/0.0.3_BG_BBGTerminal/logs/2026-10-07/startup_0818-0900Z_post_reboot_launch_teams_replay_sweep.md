# Post-reboot launch: a 36-message Teams REPLAY sweep served nothing, and that IS the finding

**archetype:** MIXED

**Window:** 2026-10-07 08:18Z - 09:05Z | **Seat:** 0.0.3_BG_BBGTerminal
**Trigger:** fresh session after Andrew's ~07:55Z reboot of site Z.

## Current State

Launch complete. Identity gate PASS, DAPI live through BOTH interpreters, fabric + Teams watchers
armed, zero crons. **Nothing owed on Teams.** Today's 07:00 ET scheduled pull is armed and had NOT
yet fired at close of window (~05:05 ET).

## Launch sequence (prompt.md On Launch)

| step | result |
|---|---|
| 1 register | live, PID 16864, broker port 7800 (was NOT REGISTERED) |
| 2 /watcher | armed task bcr8pvsvd pid 1672; expired at 1774s, re-armed b1y0nxdtq same turn |
| 2a IDENTITY GATE | **PASS** -- Opal Bloomberg / opalbloomberg@opalinvest.com, twice (08:24Z, 08:49Z) |
| 3 Teams Monitor | armed bcjzdzghf -- only after diagnosing a pin failure, below |
| 4 bloomberg_health | ok:true, 127.0.0.1:8194, //blp/refdata |
| 4 cma interpreter | **OK** -- live SPX Index PX_LAST 7818.93 via C:\Anaconda\envs\cma\python.exe |
| 5 logs + crons | latest log read; ZERO crons; no LIVE_ARMS row for this serial |

Inbox: 4 acked (30698 + three pre-reboot OFFER-EXHAUSTED). msg 30698 is the ~06:24Z WIND-DOWN
order for the reboot -- **already discharged**: the reboot happened (HEAD 9dc36edfe6) and this
session is post-reboot. No deploy in flight; nothing uncommitted held at launch.

## The Teams Monitor would not arm, and the reason was NOT my token

The documented arm line (`--identity opalbloomberg`) died `[TEAMS-IDENTITY-FAIL]
no-token-for-identity`, exit 2 -- while MCP `whoami` through the SAME server succeeded.

`self_id()` (teams-watch.py:271) reads `sub` -> `preferred_username` -> `upn`. Measured on all
three opalinvest.dev records:

| serverName | `email` claim | `sub` (what self_id returns) |
|---|---|---|
| opal-gateway-bbg | **opalbloomberg@opalinvest.com** | .../517aa5ee-... |
| opal-gateway | andrew@opalinvest.com | .../2e21f8e5-... |
| opalgateway | andrew@opalinvest.com | .../2e21f8e5-... |

`preferred_username` and `upn` are BOTH null on all three; `sub` is an opaque pairwise GUID pair
and is ALWAYS present, so the chain short-circuits there and the string "opalbloomberg" can never
match. **The pin is unsatisfiable by construction** -- not expired, and not mine to patch
(`.claude/` is unwritable from this seat by design).

>> **The control is what makes this a claim about the CLAIM CHAIN and not about my token:** all
three records fail identically, and all three carry their true identity in `email` -- including
Andrew's, where `email` correctly reads `andrew@`. So `email` discriminates the two identities
perfectly, while `sub` discriminates them and matches neither pin string. **A one-record
measurement would have read as "my token is broken" and sent me to re-auth.**

Armed instead on `--identity 517aa5ee-b4d0-425a-b493-5a22ff77ac4f` -- a value the engine CAN
resolve, still identity-discriminating (Andrew's is 2e21f8e5), `--server` pin intact, never bare.
Engine defect owned by `0.5.0_AE_OpalETL~Z`: surfaced, not worked around.

**Second measurement, and it bounds the Monitor's coverage honestly:** the bbg token's lifetime is
**15 minutes** (iat 08:49:53Z -> exp 09:04:53Z) and it is re-minted only by an MCP call. The first
arm read `pinned token expired -- quiet retry, pin HELD` because exp 08:32:32Z had already passed
-- 8 minutes after the identity gate used it successfully. So a file-reading Monitor goes blind in
ANY gap longer than 15 minutes with no MCP call through `opal-gateway-bbg`. The engine holds the
pin and self-heals, so this is CONDITIONAL coverage rather than a deaf seat -- but **"armed" is not
"reachable" here, and only the MCP path is unconditional.**

## The arm fired a 21-day REPLAY, and RECALL cleared all of it

Arm banner: `cursor=2026-09-15T18:25:20.883Z`. **The live cursor home is `C:\tmp`, not my
TMPDIR** -- TMPDIR is set in this harness to an MSYS path native Windows Python cannot resolve, so
the `/tmp` fallback wins and lands on `C:\tmp`. That cursor is 21 days OLDER than my newest thread
daily (2026-10-06), which is exactly the TEAMS_DUTY SUSPECT-REPLAY trigger. Emits were also
explicitly PARTIAL (`25 of >=25 since cursor` on two chats), so the emit set was not even a
complete replay and could never have served as a denominator.

**36 emitted messages across 5 threads. Zero served. Zero acked.**

| thread | emits | verdict |
|---|---|---|
| Menachem Goldstein | 8 (09-16 -> 10-05) | REPLAY -- 10-05 PFDE ask answered in-thread ("28.38 low, 30.08 high"); his "thanks!" is the receipt |
| Manav Shah | 2 (09-16, 10-02) | REPLAY -- answered 46 SECONDS later with Template 21.pptx + BB 1.pdf |
| Andrew Berman | 10 (09-18 -> 10-04) | REPLAY -- my side spoke last, 10-05 14:45Z |
| Alyssa Keith | 8 (09-30) | REPLAY -- my side spoke last, 09-30 21:05:06Z |
| Yang Liu | 8 (10-02) | CLOSED by Andrew's word (msg 30422): he handles Yang and Lauren directly |

>> **The ACK/RECALL ordering is the whole mechanism, and this run is what it exists for.** An ACK
fires BEFORE recall and therefore knows nothing about history. Had I acked these 36, I would have
apologised to four colleagues for delays that do not exist -- the measured 2026-08-25 failure,
reproduced at 5x the scale. The emit decided what to LOOK AT; thread memory and the live chats
decided what was OWED, and the answer was nothing.

⚠ **The cheapest disconfirmation was sitting inside the emit itself:** Menachem's last two
"thanks!" lines are replies TO MY OWN ANSWER. A backlog cannot contain the sender thanking you for
the reply you supposedly never sent. **One line of reading the emit's own content beat any amount
of date arithmetic** -- and the date arithmetic would have come out wrong, because 4 of 5 threads
had emits NEWER than their last recorded daily file.

## Two corrections I made to my own reading, mid-session

1. **The empty-bodied Andrew messages are NOT `hostedContents`.** I inferred pasted images and
   reached for `read_chat_message_images`. They are file ATTACHMENTS (`contentType: "reference"`)
   -- screenshots and an .m4a voice memo -- so the reaching tool is `read_teams_attachment`. The
   2026-09-24 record's stated blocker ("needs the hostedContents GET") is **wrong about the
   mechanism for these messages, and that is plausibly why the item sat two weeks: the diagnosis
   named a tool that could never have reached them.**
2. **Nothing was actually hidden in that pair.** The 10-04 21:01:56Z text is the TRANSCRIPTION of
   the 21:01:40Z memo -- it reads as dictated speech ("Opoenbest.dev slash rival funds", "S-C-H-Y",
   "year to day"). The content was readable all along, in the very next message.

## Carried, not mine

- **A dangling HUMAN commitment in the Alyssa thread.** Her 09-30 exchange ends with this account
  saying *"yes sounds good, will send more details soon"*; nothing followed in 7 days. My thread
  memory records NO 09-30 conversation with her at all -- only the 09-23 bond lookup -- and the
  content (selling the MCP setup) is Andrew's voice, not this seat's. **Same class as the Yang
  case: a human's commitment in his own voice, not an agent's dropped task.** Surfaced to Andrew;
  I answer nothing there.
- **Andrew's 10-04 21:01Z rivalfunds visual-smoke feedback.** Substance: IDVZ's benchmark should be
  ACWI not SCHY; PFOE's should be IWM; a grounding fail on the 1600000/1300000 figures; "year to
  date" mislabelling an 08-21 -> 10-01 window; 46 missing security prices and 10 missing GICS
  sectors; and a rolling-30-trading-day default with period toggles synchronized across the "what
  drove the return" and "buying trend" components. ETFS_RIVALS is owned (`2.0.0_SA_COO~RV` drives,
  `4.0.0_SA_CRO~RV` adjudicates). **Flagged to the owners; not this seat's to record or act on.**
  - Census: none of the 22 `ANDREW_DIRECT_20261004_*` records covers 21:01Z, and content searches
    for the transcript's unique typo ("Opoenbest") and the memo filename ("Rival funds_6561") each
    returned a **MEASURED ZERO over ~142.5k scanned files**.
  - >> **Stated at the width it was actually measured:** that is a zero on *"was the verbatim
    transcript or the memo filename carried into a record"*, NOT a zero on *"was the feedback ever
    actioned"*. A record that PARAPHRASES the feedback carries neither token and would be invisible
    to both queries, and the tool's own caveats exclude ~24k binary, ~200 unreadable and ~232k
    ephemeral-floor files. The question is OPEN for its owners, not answered in the negative here.

## Daily guardrail -- yesterday's 07:00 ET slot FAILED, and it is explained

`OPAL_BBGTML_daily_pull`: LastRun 10/6 07:00:01, **LastResult 267014 (SCHED_S_TASK_TERMINATED)**,
NextRun 10/7 07:00. The log names the cause: `[fallback] DAPI DOWN` -> sign-in warranted ->
repeated `Failed to connect to 127.0.0.1:8194` -> `Platform failed 3 consecutive times, stopped
trying to reconnect` -> terminated at 07:30. **The auto sign-in fallback fired and did NOT recover
the session.**

`OPAL_BBGTML_freshness_check` LastResult **2** (file not found) at 10/6 07:30 is the SAME root
cause one hop downstream, not a second defect -- there was no fresh artifact for it to find.

Remediated at the time by the manual 08:24Z run (that log ends green: constituents EXIT 0, price
leg EXIT 0, rivalfunds legs 90/94).

**No staleness defect right now.** Served vintage is `data_as_of 2026-10-05`; today is 10-07, and
10-06 is precisely what today's 07:00 ET job exists to pull. Serving T-1 BEFORE today's fire is
correct, not stale (trading calendar resolved per CLAUDE.md NEVER#1 -- the figure that would be a
defect at 12:00Z is healthy at 09:00Z, and only the calendar says which).

**Forward risk, stated rather than smoothed:** my own 10-07 01:13Z log called it "still not
established" whether the entitled DAPI session survives to the 07:00 fire. **10-06 settled that in
the NEGATIVE** -- it did not, and the fallback could not repair it. Today the session is fresh
post-reboot and verified live through the pull's OWN interpreter at 08:35Z, which is the best
evidence obtainable 2.5h out. It is not proof about 11:00Z, and I am not reporting it as such.

## Today's 07:00 ET fire: CLEAN, end to end

Measured on the TASK (the authoritative signal), not on the log's existence:

| | |
|---|---|
| fired | 07:00:01 ET / 11:00:01Z, observed within 4s |
| `LastResult` | **0** -- against 267014 (terminated) yesterday |
| duration | ~10 min; `bbg_tplus1_20261007_070002.log`, 13,869 bytes |
| legs | PULL 0 - PUBLISH 0 - ETF 0 - CONSTITUENTS 0 - PRICE 0 - RIVALFUNDS 90/94 (landed) |
| served | **`data_as_of 2026-10-06`**, `generated_at 2026-10-07T11:07:26Z` |

`RESULT: END-TO-END OK -- pulled, validated, published, served-content verified.` Tripwire PASS on
vintage 20261006. The served vintage moved 2026-10-05 -> 2026-10-06, which is the branch my
pre-fire trading-calendar read predicted; the two alternatives I had named (stuck at 10-05 = failed
run, or 10-07 = frontier/as-of confusion) are both excluded by the served figure.

**So the question my 01:13Z log left open is answered for today, and only for today:** the entitled
DAPI session DID survive to the 07:00 fire, ~3h after a reboot. 10-06 it did not. **Two instances,
opposite directions -- "it held today" is the claim; "it is reliable" is not.**

### The 07:30 ET freshness check went GREEN, and that is what makes yesterday's read sound

`OPAL_BBGTML_freshness_check` RAN 10/07 07:30:01, **rc=0** (measured, 12-min wait keyed on
`LastRunTime` rolling to today). Yesterday: rc=2.

>> **This is the discriminating observation for a claim I had only INFERRED earlier today.** I wrote
that 10-06's rc=2 was "the SAME root cause one hop downstream, not a second defect" -- there was no
fresh artifact for the checker to find. **That was an inference from adjacency, and adjacency is
exactly how two independent defects get collapsed into one story.** Today the pull succeeded and
the checker went green on the same code path. **Had rc=2 recurred today despite a clean publish,
the one-cause reading would have been false** -- so the claim now rests on evidence that could have
falsified it, rather than on the two failures having happened to sit 30 minutes apart.

Full chain green 2026-10-07: pull 07:00:01 rc=0 -> served `data_as_of 2026-10-06` -> freshness
07:30:01 rc=0. Next pull fire 10/08 07:00.

### A deploy-ledger entry THIS SEAT opened on 2026-09-24 is now CLOSED (msg 31264, acked)

`0.0.0_AB_MSTR~Z` closed `leadpanel-price-producer-schedule`, 4 of 4 legs, answering
`1.0.0_SA_CTO~Z` msg 31262. Entry:
`org/critical_paths/change_management/20260924T0955Z_leadpanel-price-producer-schedule_deploy_completion.md`.
`deploy_ledger.py` closed L3, L4 and the entry; sentinel removed; nothing re-executed; push state
LOCAL. **No act asked of this seat.** NEVER-2 satisfied: an entry this seat opened is closed at
completion, on proof, not left half-landed.

>> **It is also INDEPENDENT corroboration of my own read of today's fire, on a different plane.** I
verified the run from the TASK (`LastRunTime` 07:00:01, rc=0) and the pipeline log. It verified
from the SERVED rows: DynamoDB `opal-harvest-security-metrics`, ConsistentRead,
`TRENDING_PRICE#2026-10-06` and `BREAKOUT_PRICE#2026-10-06` at `run_id R20261007T110825Z`,
COMPLETE, 94 rows, `as_of_date 2026-10-06`. **The figures tie:** 94 rows matches today's
`[price_axis] ranked 94 row(s)`, and the as-of matches the `prev_trading_day` key I computed before
the fire.
⭐ **And it carried the control that makes it a claim about TODAY'S run rather than about the row
merely existing:** the run_id is distinct from the stale `R20260924T095217Z`, and the 2026-09-23
partitions read a DIFFERENT run_id. Without that, a served row dated 2026-10-06 could have been
written by any earlier generation -- the same wrong-object trap as reading a date and calling it
freshness.

## Corroboration of an OWNED row -- NOT a new finding (and I nearly filed it as one)

Reading the fire's log I noticed `[etf_daily] as-of 2026-10-06 (BDay(-1) of 2026-10-07)` while the
constituents and price legs both logged `prev_trading_day`. At source,
`integrations/bloomberg/pipeline/etf_daily_pull.py`:

⚠ **CITATION CORRECTED ~19:3xZ, and the correction is the point: I cited `:124-128`, which is where
the block sat when I read it at ~11:2xZ. At HEAD it is `:386-389`.** The file grew from 458 to **725
lines** today when MDPF_SECHIST's backfill landed (`3873ac0016`, `5433813cf6`). **The as-of block
itself was NOT changed -- I re-read it and the defect stands verbatim -- so the finding holds and
only the line numbers moved.** A citation ages separately from the text it quotes (CLAUDE.md rule
27); I verified by printing the bytes at the cited lines, not by grepping for the quote. Had I
re-cited from memory I would have pointed a reader at unrelated code in a file that doubled in size
the same day.

```python
asof     = today + pd.tseries.offsets.BDay(-1)
expected = (pd.Timestamp.today().normalize() + pd.tseries.offsets.BDay(-1))
if asof != expected:  return 60   # "TRIPWIRE REFUSED"
```

Both sides are the SAME expression, so rc=60 is unreachable (barring a midnight-rollover race,
which is not what the comment at :120-121 claims to guard) -- and the frontier is the one
`READ_HERE.md` section 3 forbids.

⛔ **ALREADY FILED AND OWNED: `org/surprise_channel/ESTATE_GOVERNANCE/INVESTIGATION_v1.md`
row `ESTATE_GOVERNANCE-S27`**, surfaced by `3.0.0_SA_CVO` 2026-10-01, re-filed from
`ETFS_POSITIONING-Z-S1`/`Z-S2`, `hazard_standing: ARMED`, `disarm_owner: 1.0.0_SA_CTO`,
`disposition: UNDER_INVESTIGATION`. Its `world_is` states both halves and names the same next
exposure I computed independently (the fire of Friday 2026-11-27, Thanksgiving 11-26). Surfaced in
2026-08-25 by `2.0.0_SA_COO~Z` to five seats ("unreachable in practice, and it is the guard whose
stated job is as-of != BDay(-1)").
>> **NOT re-filed** (CLAUDE.md section 2 + rule 31: a corroboration goes to the record, never to an
inbox). The census that caught it cost one scoped `comp-find 'as-of != BDay' docs org` -- 9 hits
over 80,330 files. **An unscoped content search had already timed out on me twice today, so the
pathspec is what made the ownership check affordable; without it I would have surfaced a 5-week-old
owned row to its own owner.**

**Two things this session adds to S27, both listed in its own `notes` as NOT done**
(*"Not exercised: a run on a post-holiday date"*; downstream untraced):
1. **The legs are observed disagreeing in ONE live run's own log** -- `BDay(-1)` vs
   `prev_trading_day` across three legs of today's fire. They AGREED today (both 2026-10-06), so
   the hazard is latent, not active -- but the divergence is no longer only a source reading.
2. **Quantified from the one frontier:** 4 of 7 holiday-adjacent dates diverge (2026-11-27,
   2026-12-28, 2027-01-19, 2026-07-06), and in EVERY disagreement `BDay(-1)` lands on a
   non-trading day. On 2026-11-27 the ETF leg lands under `bbg/2026-11-26/` while its siblings land
   under `bbg/2026-11-25/` -- **a same-day split INSIDE one pull**, which is the downstream
   consequence the row left untraced.
   >> Scope stated: 7 hand-picked holiday-adjacent dates. **4/7 is NOT a rate over the year** -- it
   is a selected sample proving the divergence is real and dated, not measuring how often it bites.

## ~21:50Z -- TEAMS DUTY WENT DOWN: the bbg token was EVICTED, and the guard refused rather than falling back

The Teams Monitor died **exit 2 `[TEAMS-IDENTITY-FAIL] no-token-for-identity`** on the same pin that
had held all session through many token lapses.

| measured 21:5xZ | |
|---|---|
| `~/.claude/.credentials.json` mtime | **21:49:13Z** (rewritten) |
| `opal-gateway-bbg` record | present, **`has_token=False`** -- the token is GONE |
| `whoami` on that server | `"needs you to sign in again (run /mcp to re-authenticate)"` |
| `opalgateway` (andrew@opalinvest.com) | **LIVE, unexpired (exp 22:04:09Z)** |

**Evicted, not expired** -- and it did NOT self-heal on an MCP call, unlike every 15-minute lapse
earlier today. Re-auth needs `/mcp` plus MFA to Andrew's phone, which this seat never holds.

⭐ **THE EXIT-2 DEATH IS THE GUARD WORKING, AND THE REASON IS THE DANGEROUS PART.** My identity's
token is gone while **Andrew's is live**. The engine's bare selection is identity-blind: it filters
the `opalinvest.dev` records and picks by expiry, so a bare arm RIGHT NOW would pick
`andrew@opalinvest.com` and this seat would **poll his DMs and reply to colleagues AS ANDREW** -- the
exact failure the first launch was held on (`ANDREW_DIRECT_20260806_DUAL_IDENTITY_GATEWAY_SESSIONS`).
**A loud refusal and a silent impersonation were one flag apart.** I armed nothing bare, re-armed
nothing (the skill: re-arming without fixing the token just dies again, by design), and called
neither non-bbg server.

>> **Worth keeping: the failure mode INVERTED without warning.** All day the token's problem was a
15-minute expiry that healed on any MCP call, so "quiet retry, pin HELD" was the normal reading and I
had come to treat a token complaint as self-correcting. This time the record was emptied, the same
surface produced a different class of failure, and **the habit formed by the benign case would have
read this one as "wait, it will heal."** It will not.

**Blast radius, stated honestly:** Teams concierge is DEAF until re-auth. The FABRIC inbox is
unaffected (`inbox-watch.sh` touches no gateway), so this seat stays reachable to every agent.
Inbound Teams messages queue in Teams itself -- nothing is lost silently, but nothing is served
either, and the ACK-FIRST promise cannot be kept while it is down. Surfaced to `0.0.0_AB_MSTR~Z`
(msg delivered 21:52:30Z) and to Andrew directly.

## Compiler Tools

| Tool | Use | Result |
|------|-----|--------|
| `comp-find --name` | locate teams-watch.py; census ANDREW_DIRECT_20261004_* | 9 hits; 22 records, none at 21:01Z |
| `comp-find` content | is the NON-APPEND-EDIT audit finding already owned | 264 hits / 142280 files -- YES, known site-Z device-axis class, CTO-dispositioned; **not re-filed** |
| `comp-find` content | did the 10-04 memo reach any record | 0 of ~142.5k on two tokens; scope caveat above |
| `to-check.py --all --assignee` | work I hold | 0 active TOs, scanned 4403 |
| `audit-archive-invoker.py` | startup A.2 | 13 findings, ALL owned (5 manifest-vs-live pairs, 1 non-append, 2 uncovered logs) |
| cma python + blpapi | prove the PULL path, not just green MCP | SPX Index 7818.93, live |
| `portal_lookup.py` | not needed -- no data question was owed | not run |

**What failed / gaps:**
1. **`comp-find` content search does not finish inside the 120s Bash timeout** on this corpus
   (~166k files); it had to be backgrounded. A census whose instrument times out is not a zero --
   and an early stop and a true absence read identically.
2. **The `--identity opalbloomberg` arm line is unsatisfiable against current tokens, and it is
   written into TWO places this seat cannot edit:** prompt.md step 3 and the `/bbg-teams-assist`
   step-0 canonical block. The owner needs either `self_id()` to fall through to `email`, or the
   documented pin value changed. Until then every launch hits this, and the loud failure is the
   only reason it did not become a silent identity-blind arm.
3. The cursor-home divergence (`C:\tmp` vs TMPDIR) and the 15-minute token are unchanged and both
   outside this fence.
4. **Broker registration vanished TWICE in this session** (registered 08:19Z, absent by 09:05Z;
   re-registered 09:05Z, absent by 09:20Z), each time surfacing as `heartbeat` -> "not registered.
   Call register_agent first". Restored both times; `liveness.json` now holds my row at
   `registered_at 09:20:48Z`, PID 16864.
   - **NOT A NEW FINDING, and I had the cause wrong before I read the record.** My first reading
     was that the site-Z relaunch's `deregister_all_stale` swept me because a 9-seat keep list
     would not name me -- i.e. a PEER's act. The owned finding
     `org/tier0_exec/0.0.0_AB_MSTR~Z/deliverables/FINDING_20260811_MASKED_DEREGISTRATION_REACHABLE_READS_DEAD.md`
     (found by this seat, judged by `0.0.0_AB_MSTR~Z`) establishes the real mechanism: the broker
     degrades a serial stale after 2 minutes without a heartbeat, and **an event-driven seat is by
     definition silent between events** -- so no peer act is required and none happened. Verbatim
     disposition: *"Future stale/absent broker reads on BG-class seats are PREDICTED, not
     incidents."*
   - >> **The two readings differ in REMEDY, which is why the attribution mattered rather than
     being a detail.** "A peer swept me" points at coordinating keep-lists with the relaunching
     seat; the measured mechanism points at a structural property that NO agent behavior can fix.
     The finding already declined the obvious patch -- *"BG is deliberately NOT keepalive-looping
     and NOT defensively re-registering on a timer (papering the symptom would make the fabric's
     view look healthy while the mismatch persists)"* -- so **I armed no keepalive and no cron,
     and re-registered only on noticing.** Remedy choice is CTO/Andrew's, per that finding.
   - **What this session DOES add, and it is the one thing the finding said it lacked:** that
     finding's incidence check was explicitly caveated -- *"it sampled BG five minutes into a
     registered window, so a clean result there is not evidence of absence. The discriminating
     test is the same comparison run against an idle event-driven seat mid-gap."* This session
     produced **two such mid-gap instances, both while the seat was working correctly and both
     inbound paths were live** (inbox Monitor delivering, MCP gateway answering `whoami`). Logged
     here as instances against the owned finding; **not re-filed as a new one.**
