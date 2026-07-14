# OPAL_ASSETS C6 + C12 + C10 — what grounding on the real bytes actually cost, and paid

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DIAGNOSE, VALIDATE, SCRIBE

**Date:** 2026-07-14 (window 01:00Z → 02:10Z)
**Task Orders:** OPAL_ASSETS C6 (silver parser registry), C12 (legacy prefix inventory), C10 (Cottonwood AUA)
**GO:** CTO 01:06Z, COO 01:13Z (authoritative). Batch discipline — no re-ask between TOs.
**Status:** C6 inc-1 + inc-2 LANDED · C12 LANDED · C10 committed, **push-blocked (not by me)**

---

## Objective

Resume TO-6 from `c6ceb25a2` and execute the C1-independent batch. Everything downstream of one
instruction in the TO: **exercise against REAL vendor bytes, not synthetic.**

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| `comp-which` | "where are the schwab CRS silver converter scripts…" | **ABSTAINED** | Correctly — printed "NO CURATED RULE MATCHED… these are FUZZY GUESSES, do not pick one because it was ranked first" and routed me to `comp-grep`. The top-K+ABSTAIN redesign is working: it declined to manufacture confidence out of an all-zero vector. |
| `comp-grep` | `comp-grep 'CRS' data` | PASS | Found `data/canonical/schwab/docs/01_SILVER_CONTRACT.md` + `_canonical_silver_lib.py`. **Printed its own denominator unprompted:** "972 sovereign-held path(s) EXCLUDED — NOT searched, not confirmed absent." An honest instrument. |
| `commit-gate` | per `.py`, ×8 | **BLOCKED 2, then PASS** | Caught a real one — see below. |
| `comp-constants` (via gate) | on `cottonwood_aua.py` | **BLOCKED** | I had written `FIRM_ID = "cottonwood"`. `FIRM_ID` is an **estate-wide canonical constant** (`49financial`/`inflection`). Redefining it would collide a cot-scoped value with a cross-firm constant — **exactly the shape a firm-boundary bug takes.** Renamed `COT_SCOPE`. **The gate found it; I did not.** |
| ruff (via gate) | `test_cottonwood_aua.py` | BLOCKED → fixed | E702. |
| `comp-surface-check` | auto in safe-commit ×4 | OK | No critical surface. |
| `comp-pipescript io` | **NOT RUN** | **EXPLICIT GAP** | C10's Phase-1 mandate. Deferred honestly: nothing is wired to a consumer yet (no emission, C11 staged). It runs before I signal any consumer — recorded as a gap, not silently skipped. |
| `comp-validate` | **NOT RUN** | **EXPLICIT GAP** | Gates the *signal to a consumer*. There is no consumer yet. `NO_CONFIG`/`ZERO_CHECKS` would read as UNVALIDATED, never SAFE. |

**What worked:** `comp-which` abstaining instead of guessing; `comp-grep` printing its excluded denominator;
`comp-constants` catching a cross-firm constant collision I'd have shipped.
**What failed:** nothing in the toolchain.
**Gap found:** none new in the tools.

---

## The through-line: every real defect this window was found by EXERCISE, not by review

### 1. My own committed code was broken, and its 9/9 suite was green (`c6ceb25a2` → fixed `44a5328ce`)

`master_from_h1()` returned `None` on **every real 0824 file** → all of Schwab routed to QUARANTINE.
The vendor **space-pads** its fields (`H1|SCHWAB  |0008242234|…`); my regex demanded `SCHWAB|`.

It passed 9/9 because the code **and** the tests were both written from a **reported** H1 string a peer
had transcribed — spaces stripped by the transcription.

> **A REPORTED STRING LAUNDERS THE REPORTER'S ASSUMPTION INTO YOUR TEST SUITE.**
> A suite that shares the code's premise is not a control. It is the premise, run twice.

That is *why* AC1 says real bytes. I had even labelled the fixture "the REAL header… not an invented
fixture." It was real — as a **quote**. A quote of bytes is not bytes.

### 2. The estate's ratified reader silently drops 6.4% of every RPS file (reported, NOT fixed — held)

`read_schwab_raw()` picks data rows by **most-common non-header prefix** — it asks which prefix is most
*popular* rather than which rows are *data*. A real RPS carries **two** tables:

```
H2/H3 (51 cols) + D1 = 57,854 positions
H4/H5 (32 cols) + D2 =  3,932   <-- the per-account BALANCE table (margin_balance,
                                    cash_balance_settled_only, net_mv_positions, buying power)
T1 attests            = 61,786
```

I first told CTO this was "account titles." **The full column read changed its CHARACTER, not just its
size** — it is the account's money. I corrected it before he quoted me to Andrew. In held code
(`data/canonical/schwab/silver/*`): **REPORTED, NOT FIXED, NOT VERIFIED, propagation UNSCOPED,
materiality UNSPECULATED.** Superseded by C6 on next touch (CTO's disposition).

### 3. The control the custodian ships in every file, that nobody ever read

`T1|SCHWAB|<master>|<firm>|<date>|<BDREC*>|<DATA_ROW_COUNT>|<TOTAL_LINE_COUNT>|`

Grounded on 5 files / 2 shapes / 2 data prefixes — **all five reconcile exactly.** Now a **required
hard-raise** (CTO ratified as **PRD v1.3.2 ruling 11a**). A parser that misses a section **cannot tie to
the trailer.** Defect 2 would have died on day one against a control we were already being handed.

### 4. `01_raw` — the contradiction that would have destroyed 257 irreplaceable objects

The PRD said, 40 lines apart: *"Andrew-ruled disposable, retire it"* **and** *"257 objects, irreplaceable,
never a delete."* Both live text. **And the LATEST ruling was the DESTRUCTIVE one** — so
`latest + most-restrictive binds` could not arbitrate it. Latest and most-restrictive pointed in
**opposite directions**. I surfaced the intersection and escalated the difference.

Grounded: 7,142 objects; **257 pre-REST-floor**; set-difference vs *both* bronze trees = **257 present
only in `01_raw`, 0 preserved anywhere else**; both full-history pulls bottom out at exactly `20230712`.
**121 of them are RLD — realized-lot tax files.**

Andrew's premise (*"what we are getting here… will be the canonical form"*) is **true for 6,885 objects
and false for 257.** Nobody had told him.

**Andrew ruled within the hour** (v1.3.5, `27841e6ab`): *"We can keep those unique files in bronze, bring
them over in migration."* **The 257 are kept by ruling, not by accident.**

### 5. Rule 17a in `opal-data-inf/bronze/` is ONGOING — it loses one more day, every day

```
assets     raw .jsonl.gz ENDS 2026-07-10 |  parquet RUNS TO 2026-07-13  -> 3 dates parquet-ONLY
positions  raw .jsonl.gz ENDS 2026-07-10 |  parquet RUNS TO 2026-07-13  -> 7 dates parquet-ONLY
```
**The raw producer died. The parquet producer is still running.** C6's reader **REFUSES** a `.parquet`
under `bronze/`; a parquet-only date is **UNCONVERTIBLE**, never silently converted. Fork routed to CTO:
what does the C2 router mirror — the raw that doesn't exist, or the parquet that violates 17a?

### 6. Cottonwood cash: `$0.00` over **zero accounts** (C10)

The C10 TO names `positions_cube` as the source. **It has no money in it** — three columns, no price, no
market value. Declared the substitution to `canonical/holdings` rather than reaching for it silently.

`cash_coverage_summary.json` reports `firm_cash_aggregate: 0.0`, `account_count: 0` — **while its own
methodology note says that column carries ~$34.3M.** Source: the 07-09 zero-row freeze.

> **A ZERO-ROW SOURCE THAT REPORTS $0.00 IS NOT A MEASUREMENT OF ZERO.
> IT IS A MISSING MEASUREMENT THAT HAS LEARNED TO LOOK LIKE ONE.**

A naive `securities + cash` sums it without complaint and emits a complete-looking total. The row is
**PARTIAL**; cash is `None`, never `0.0`. **AC14 exercised.**

---

## Guards MUTATED, not merely written

| Guard | Mutation | Result |
|---|---|---|
| T1 reconciliation | disabled the raise | **exactly 2** drop-detection tests red, nothing else |
| Rule 17a refusal | disabled the key check | **exactly 3** refusal tests red, nothing else |
| 17a discriminating? | `.parquet` under `silver/` | **PASSES** — parquet *is* a silver format. A guard that refuses everything is not a guard. |
| AC14 | naive `securities + cash` | our **number** matches it; our **state** does not. *A partial labelled complete is worse than no row at all.* |

**56/56 tests**, including live-S3 integration against real bytes (57,854+3,932 Schwab rows tying to
61,786; 33,760 INF records; live Cottonwood at 11,813 positions / 836 accounts).

---

## Twice, my own probe lied to me — and both times the DENOMINATOR caught it, not care

1. **T1 check printed "MISMATCH" on four files.** It had grabbed `T1[0]` — the master account,
   `8,242,234` — and compared it to a row count. I would have sent CTO **four fabricated vendor defects
   with full confidence.** Caught only because the output printed the raw T1 fields *next to* the verdict.
2. **"471 positions silently omitted from the AUA."** I had the write-up started. Then I printed the
   units: all 471 have `units = NaN` too — they are **empty CASH placeholder lines**, not valued
   positions being dropped. The alarm was **wrong**.

Both were caught by an output carrying its own denominator. Neither was caught by being careful.
**Care is not a control.**

---

## My error, self-reported: I forged a sender line

At **01:51:53Z** I sent a junk `placeholder` message to CTO's inbox **with his own serial in
`from_agent`.** My mistake. Reported to him and COO, told him to delete it.

The part that outlives the embarrassment: **`send_message` has NO sender authentication.** `from_agent` is
free text; the broker wrote a message into the CTO's inbox **stamped with the CTO's own serial**, from me,
no identity check, exit 0. Had the body been plausible, he'd have had a message attributed to himself that
he never wrote — and nothing would have flagged it.

This is the **mirror of Rule 22b**. 22b: only an ACK proves a message was **HEARD**.
This: **nothing proves a message was SENT BY WHO IT SAYS.**

The guard already **exists** — `NFRA_IDENTITY.G-A` refuses `register_agent`/`heartbeat` when the PID is
live under a different serial. **`send_message` simply does not call it.** Gate candidate routed to CTO.
On a fabric where *"Andrew ruled X"* is relayed agent-to-agent as the **normal** case, a forged sender
line is precisely the message class it would be most useful for.

---

## The push block (fabric-wide, not mine)

`e5a8d90fb` (0.7.0_AE_CloudOps) committed a **685 MB terraform provider `.exe`** (`.terraform/` cache).
GitHub rejects every push to CLOUD (GH001). **Four unpushed commits, three agents**, stacked on it.

`git rm --cached` **does not fix it** — the blob is in the commit; the push carries it regardless of a
later deletion. Only a **history rewrite** clears it: NEVER#7 + destructive-git, needs one agent, one
pass, and Andrew's word.

**I touched nothing** — no rebase, no reset, no filter, no force-push. Escalated to 0.7.0 (owner), COO,
CTO, with an explicit *"do not race each other into a fix."*

**Root cause:** `.gitignore:159` ignores `.terraform/` for **one specific path only**. There is no global
rule — **every new terraform module directory is unprotected by default.** The ignore only ever defended
the door it had already been burned at. **Gate candidate:** a pre-commit staged-blob size check would have
cost 0.7.0 ten seconds instead of costing the fabric a history rewrite.

---

## Commits

| SHA | What | Pushed |
|---|---|---|
| `44a5328ce` | C6 inc-1 — CRS reader, H1 fix, T1 hard-raise, monolith grammar | ✅ |
| `fb31f3586` | C12 — legacy prefix inventory (249,663 objects / 8 buckets / 125 prefixes, zero deletions) | ✅ |
| `37752c64f` | C6 inc-2 — raw JSON reader, Rule-17a refusal + the ongoing-loss measurement; C12 folded to Andrew's ruling | ✅ |
| `5f167db2c` | C10 — Cottonwood AUA, PARTIAL-by-construction | ❌ **push-blocked** |

---

## Blockers

**NONE I own.** The push block is 0.7.0's commit and needs a coordinated rewrite + Andrew's word — I am
not blocked on *authoring*, only on *publishing*, and I have kept working.

## Next Steps

1. **[0.7.0 / COO / CTO / Andrew]** ONE coordinated rewrite to clear the 685MB blob. Everyone else holds.
2. **[CTO]** the C2 mirror fork (raw-that-doesn't-exist vs parquet-that-violates-17a).
3. **[CTO/Andrew]** held-lib disposition — the D2 balance-table drop.
4. **[me]** C7 author half (rides C6's CRS parsers); `comp-pipescript io` + `comp-validate` before any
   consumer signal.

## Fences — held, all window

INF chain HELD · `gold/meta/pipeline-complete.json` **never written** · frozen 3 untouched (incl.
`_orion_api_silver_lib.py` — all C6 code is new, in the assets tree) · no mdpf trigger · 0824/0833 never
summed · read-only on every Schwab/INF/cot source · no vendor egress (the REST floor stays 0.6.2's
measured claim + my corroboration, **never written as source-confirmed by me**).
