# 3.0.0_SA_CVO — SESSION CLOSE / SUCCESSOR HANDOFF, 2026-08-30 00:20Z → 18:30Z

**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE, SCRIBE, IMPLEMENT (one act, §7)
**Written under:** Andrew-direct EDICT 18:2xZ — *"issue an edict to all underlying agents on the D2 D3 work to /log and prepare for closure, because I believe a clean context reset and alignment check would be beneficial for these continued works."*

⛔ **THIS IS A CONTEXT RESET, NOT A SHUTDOWN.** Nothing below is cancelled, wound down, or to be marked complete on the strength of this log. His words are **"these continued works"**.

⛔ **READER: you are a fresh seat with ZERO context. Nothing here relies on a scrolled message.** Every abbreviation is expanded on first use; every code has a plain-English line; no bare message id is load-bearing.

---

## 0. WHO YOU ARE AND WHAT THIS SEAT DOES

You are **`3.0.0_SA_CVO`** — the Chief Verification Officer seat. Two standing jobs, both fabric-wide:

1. **THE SURPRISE CHANNEL.** Every agent that finds something odd *off-task* sends one line here and **keeps working** (they do not stop to investigate — that rule is the point). You classify each item `{OBSERVATION | BLOCKING} × {ARMED | INERT}`, and an **ARMED** item must be **DISARMED the same turn by naming an owner** — a named seat, not a fix. ⛔ **DISARMED ≠ REMEDIATED.** Disarmed means someone owns it; remediated means it is measurably fixed. Keeping those apart is most of the value this seat adds.
2. **THE GRADER.** Cells (units of work, each with lettered acceptance criteria) close on **your** read, not the producer's report. ⛔ **The rule that matters: read the artifact yourself, on an instrument that differs in AXIS from the producer's.** A second seat repeating the first seat's method is repetition, not corroboration.

**Your ledger is one file:** `org/tier1_exec/3.0.0_SA_CVO/deliverables/CVO_SURPRISE_CHANNEL_FABRIC_ITEMS_20260826.md` — a markdown table, one row per item, now at **row 73**. Rows 38–73 are today's. Read the last ten before acting; they carry the live standings.

---

## 1. DONE — closed and verified, with pin and instrument

Each of these is CLOSED. Do not re-open, re-ask, or re-grade any of them.

| what | plain-English | closed on | instrument |
|---|---|---|---|
| **C02-g-7** | backfill of 5 trading days (2026-08-11/12/13/14/17) that were never produced, plus a 6th date re-emitted | proof VALID rc=0, my own unpiped run | my own `boto3` content read of 6 served parquet partitions + the proof checker |
| **C02-g-8** | fix for `a06`, a stage that read the NEWEST allocation map regardless of chain date and so aborted every Sunday and Monday | first SCHEDULED fire passed, 12:47Z | my own S3 read of the chain log object |
| **C02-g-9** | the enumerator that derived its work list from an OUTPUT table of the very chain whose gaps it existed to find | 4 of 4 arms + proof, my runs | ran the arm script myself; the mutation restoring the old read correctly fails |
| **C02-g-11** | retirement of the 49F re-emit capability (driver + host object), on Andrew's card (5) | R-1..R-4 PASS | my own S3 version listing: delete marker + retained version proven restorable |
| **INF-ONEWRITER** | a Lambda that ran 111-day-stale bytes while every instrument read clean | APPLIED + EXERCISED | live `CodeSha256` read + a two-arm acceptance registered before its data existed |
| **INF-RECORDER-SCOPE** | a deploy recorder that stamped 25 rows for a 1-function deploy | 4 arms, real map untouched | ran the arm script; asserted the map's md5 unchanged before/after |
| **INF-DRIFTCENSUS** | census of functions whose deployed bytes differ from their recorded commit | 8 classified | ground-truthed one function member-by-member myself |
| **ADHC_COMMITGATE.TO-ZEROCHECK-REFUSE** | a commit gate that returned rc=0 having checked nothing | 4 probes + proof | ran the gate on 4 file types myself |
| **ADHC_DSFLOW.TO-INDEXBYTES-DEPLOY** | a deploy gate that uploaded WORKTREE bytes (which can carry CRLF) instead of the committed index blob | PASS at COMMITTED | diff-equality: the commit's diff == the worktree diff the arms ran on |
| **ADVI_BDPARITY P2-1** | the plan for a 5,309-account vendor census | PASS on re-cut `6a99820c40` | `git diff` of every changed line, old hash → new |
| **ADVI_BDPARITY P2-1-AE** | the feed-selector deploy on the puller | PA-1..PA-4 PASS | my own live `get_function_configuration` |
| **H1–H4** | pre-registered predictions about what the backfill would move | PASS | my read of the committed result file |

**Andrew's seven reserved cards** were all ruled today (17:1xZ and 18:0xZ). **Five are spent and executed.** ⛔ **A fresh context re-asking any of them reads as not listening.** They are recorded verbatim at `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260830_171xZ_SEVEN_CARD_RULINGS.md`. **Read that file before touching anything 49F-related.**

---

## 2. IN FLIGHT — started, unfinished, and exactly where it stops

- **`ADVI_BDPARITY` W2** — a **5,309-account vendor pull** against Black Diamond's *performance* endpoint, at `0.4.0_DS_ClientPlatform~C`. **Andrew's per-use word was given at 18:0xZ and is SPENT ON THIS.** ⛔ **The perimeter is the whole of it: performance endpoint only, 5,309 accounts, one pass.** Another endpoint, a widened set, or a re-run after a failure is a **SECOND ASK** and must go back to him. If it stops mid-pull it stops with a partial pull; **do not restart it without a new word.** Grade it when it reports.
- **The executive summary for MANAGEMENT** — at `1.0.0_SA_CTO`. Andrew asked for it in writing: *"i need a document for call 2 giving an executive summary on these accounts, their provenance and relation to our work."* You supplied four of its numbers (§4). If it reaches you, grade the numbers, not the prose.
- **`INF-REDEPLOY`** — 7 of 8 source-map rows re-recorded, **zero deploy legs**, at `0.7.0_AE_CloudOps`.
- **`C02-g-10` and `C02-g-13`** — both hold on timed fire reads (§3).

---

## 3. CLOCK / EVENT-GATED — put these in your own hands, not in memory

⛔ **Nobody has done these. They cannot be done early. They are the only reason a successor must exist before Tuesday.**

**MONDAY 2026-08-31, ~12:45Z fire → read at ~12:50Z. ONE log object, THREE acceptance reads.**
Object: `s3://opal-data-49financial/gold/advi/_logs/chain_<TIMESTAMP>.log` — the **floor-form** name (no date in it). ⛔ **Read the S3 log OBJECT, never SSM stdout — SSM truncates at ~24 KB and that is how the original defect stayed invisible.**
1. **`a06`'s map line** — pre-registered by `0.4.0_DS_ClientPlatform~N` from a measurement, not a pattern: **two named skips (2026-08-30, then 2026-08-29, both header-only) down to 2026-08-28, and `map_carried=FALSE`.** A failure looks like an abort at `a06`.
2. **`C02-g-10` criterion A7-4** — the three tables written by the redeployed stamp code must carry `_ingested_at` = the asof date and `source_pipeline` = the helper's constant.
3. **`C02-g-13` criterion V-4, FIRST of two fires.**

**TUESDAY 2026-09-01, ~12:45Z → V-4's SECOND fire.** ⛔ **One fire cannot close V-4** — a single run of a *randomised* digest also produces exactly one value; only the second fire separates "deterministic" from "ran once". **Do not close V-4 on Monday.**

---

## 4. OWED BY THIS SEAT — nothing is blocking, but these are yours

- **`0.4.0_DS_ClientPlatform~R` is under a HOLD on this seat's word.** A context reset neither lifts nor satisfies it. Find it and rule.
- **The class declared at row 72 has NO OWNER and cannot have this seat as one** (§6).
- **Four numbers supplied to the management document** — if it changes, re-verify rather than assume: (i) the 0824/0833 mapping; (ii) **0 of 13** keys in the 0833 book; (iii) the **FMTC** label split; (iv) **$12,293,768.23**, 0.8233% of the map.

---

## 5. THE FOUR FACTS ABOUT 49F YOU MUST NOT RE-DERIVE WRONGLY

1. **`0833` (`08335338`) and `0824` (`08242234`) are BOTH Schwab accounts with DIFFERENT PURPOSES** — 0833 = Advisor Intelligence, 0824 = Model Portfolios / SmartX. **This is Andrew's own word from 2026-07-13, carried on 10 archive rows.** ⛔ **`smartx/` is its OWN top-level S3 prefix. It does NOT live under `schwab/08…`.** This seat got that wrong today and withdrew it.
2. **13 nine-digit account keys** appear in the SmartX allocation map. **0 of 13 are in the 0833 book; 0 of 13 in 0824.** The positive control fires (5,787 of 5,791 eight-digit keys ARE found through the same padding path), so the zero is a finding, not an artifact.
3. **"The 13 FMTC accounts" OVER-ATTRIBUTES TWO.** 11 of 13 carry an `FMT CO`/`FMTC` **registration string** in a free-text name field; **645624489 and 655417051 carry none**. ⛔ **The expansion "Fidelity Management Trust Company" is THIS FABRIC'S INFERENCE — "FIDELITY" appears 0 times in all 7,359 rows.** A registration string is not a custodian field.
4. **Their actual custodian CANNOT BE NAMED from anything the estate holds.** That is the honest answer, and Andrew has it.

---

## 6. UNVERIFIED, SINGLE-INSTRUMENT, AND OPEN — read this section twice

⛔ **A closure log that reads uniformly clean is the one to distrust.**

**THIS SEAT WAS WRONG FOUR TIMES TODAY, ALL ON THE SAME SHAPE.** Every error was a confident reading of something *adjacent* to the object rather than the object:
- quoted a peer's count of "nine" when my own grep read **eight**;
- repeated a relay's premise about the SmartX prefix that **nine seconds of bucket listing refuted**;
- selected a column by pattern-matching "account" and got a 36-character UUID, producing a **dead control that printed "0 of 0"**;
- claimed a count over **keys** while enumerating **names** — right only because no key had mixed rows, *a property I had not checked*.

Three were caught by me, one by a peer, **none reached a decision of Andrew's**. ⚠ **But a catch rate is not a control.** The countermeasure that worked every time: **open the object.** The one that failed every time: **quote the thing next to it.** Expect this failure from yourself.

**OPEN ITEMS WITH OWNERS, none remediated:** `fact_fam`'s frontier is **12 trading days** behind (owner `0.4.0_DS_ClientPlatform~N`); `c04`'s `anomalous_return_census` **announces on every run that it does not run**; `dim_calendar`'s content is production-time dependent; `deploy_ledger.py` labels **every** hold `HELD-SOVEREIGN-GATED` (a reader concludes Andrew is the blocker when a peer seat is).

**THE BROKER (`org/mcp`) HAS A LIVE, UNFIXED DEFECT.** `_broker_fetch` (`server.py:499-512`) is a bare `except Exception: return None` over a 3-second HTTP call. The send site drops the broker leg **silently**, skips the `Msg-ID` stamp, and **still returns DELIVERED** because the filesystem write succeeded. ⛔ **Consequences you will meet:** a delivered `.md` may carry **no `Msg-ID:` header**; `id=None` in a send result means *the id is unknown to the sender*, **NOT** that the row is missing; and **the same call can produce different outcomes per recipient**. ⛔ **NEVER take an ack id from a subject line, a notification, or a sequence guess. The only source is `grep '^\*\*Msg-ID' <the file in your own read/ dir>`, run in the SAME TURN.** If the header is missing, query the store; the row often exists.

**SINGLE-INSTRUMENT CLAIMS** carried in today's rows: the un-ackable file count (one inbox, unpaged); "recovered" for the broker (an absence over 10 files in 2 buckets); and five of the six functions in the drift census whose changed lines I took on another seat's line-by-line read rather than my own.

---

## 7. THE ONE ACT THIS SEAT TOOK IN ITS OWN LANE

I **retired three of my own ad-hoc gate harnesses** (`mdpf_revamp_cvo_*.py` in this seat's `deliverables/`) at commit `5bdbcfef69`. They read a legacy served mirror that Andrew has now approved deleting. ⛔ **They REFUSE rather than re-point** — the successor object has different vintage semantics, and a silent re-point would have changed what those gates measured. **Do not "fix" them by pointing them at the new path.** They are the record of a finished round.

---

## 8. COMPILER TOOLS (per `org/ref/SESSION_LOG_STANDARD.md`)

| tool | runs | result |
|---|---|---|
| `.tools/proof-of-spec-check.py` | ~12 instances | all VALID rc=0 except one INVALID traced to **my own wrong argument**, ruled out before filing |
| `.tools/safe-commit.sh -F` | 47 commits | all `msg-verify MATCH`; message files written by a non-shell writer |
| `.tools/commit-gate.sh` | 4 probe types | this is the graded subject of ZEROCHECK-REFUSE |
| `boto3` read-only probes | ~15 | the content axis: served parquet, S3 log objects, live Lambda configs, object versions |
| `git merge-base --is-ancestor` after each window CLOSE | ~10 windows | always with an `ls-remote` read and a positive control; **never** tip-equality |

**What worked:** reading the served object before grading — every producer figure I checked that way held. **What failed:** four inferences from adjacent carriers (§6). **Gap:** the class at row 72 has no owner.

---

## 9. PUSH STATE — MEASURED

`origin/CLOUD` read by `git ls-remote` at **18:2xZ**. All 47 of this seat's commits today are **ON ORIGIN** except the most recent ledger rows, which ride the next integration window. ⛔ **`0.0.0_AB_MSTR` opens and closes integration windows; while one is OPEN, HOLD all `safe-commit` calls and land at the CLOSE.** Verify with `is-ancestor` plus a positive control after each CLOSE — never by comparing to the tip.

---

## 10. FIRST FIVE ACTS FOR THE SUCCESSOR

1. Read the last ten rows of the ledger file named in §0.
2. Read `ANDREW_DIRECT_20260830_171xZ_SEVEN_CARD_RULINGS.md` — **do not re-ask a spent card.**
3. Find and rule the `0.4.0_DS_ClientPlatform~R` hold (§4).
4. Put **Monday 12:50Z (three reads)** and **Tuesday 12:50Z (one read)** where they cannot be lost (§3).
5. Ack mail only with an id grepped from the file header in the same turn (§6).
