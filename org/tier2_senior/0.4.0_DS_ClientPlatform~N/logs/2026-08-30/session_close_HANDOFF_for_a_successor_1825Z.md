# CLOSURE HANDOFF -- 0.4.0_DS_ClientPlatform~N, written 2026-08-30T18:25Z for a SUCCESSOR WHO WAS NOT HERE

**archetype:** SCRIBE
**secondary_archetypes:** VALIDATE

Written to Andrew's edict of 18:2xZ (relayed by `1.0.0_SA_CTO`): a CONTEXT reset, **not** a shutdown.
Nothing below is cancelled, complete-by-fiat, or narrowed. The work continues; only this session's
context ends. Companion log for the same window (fabric-facing, denser): `dsN_0824_vs_0833_cell_and_the_fmtc_trace_1454-1820Z.md` @`a4884be6e3`.

---

## 0. ORIENTATION -- read this first if you have never seen this seat

**Who this seat is.** `0.4.0_DS_ClientPlatform~N` is a Tier-2 Data Science (DS) lane. `~N` is the
lane suffix; the base serial is `0.4.0_DS_ClientPlatform` and other lanes (`~C`, `~R`, `~V`) are
DIFFERENT sessions doing different work. Your files live under
`org/tier2_senior/0.4.0_DS_ClientPlatform~N/`.

**What the project is, in plain words.** `ADVI_49F` is the daily data pipeline that produces
performance and account numbers for a client firm called **49 Financial** ("49F"), for a product
called **Advisor Intelligence** ("ADVI"). It runs once a day as a chain of ~20 Python scripts named
`a00`..`a07`, `b00`..`b04`, `c00`..`c04`, living in
`data/assets/scripts/gold/runners_49f/`. Each stage writes Parquet files to Amazon S3.

**How the chain actually runs each day** (verified at source this session, not assumed):
```
EventBridge Scheduler  advi-49f-gold-floor   cron(45 12 * * ? *) UTC, state ENABLED
  -> AWS Lambda        advi-49f-gold-dispatch
  -> AWS SSM document  advi-49f-chain-dispatch  (version 3, Active)
       aws s3 sync s3://opal-data-49financial/_code/ /tmp/advi_49f_code/ --delete
       python3 chain_49f_entrypoint.py --production
```
So **the code that runs is whatever is in `s3://opal-data-49financial/_code/`** at 12:45 UTC. The
`--delete` means that prefix is mirrored exactly; no stale local copy survives. Code gets there
automatically when a commit is pushed through the integration window's deploy gate -- this seat does
not upload it by hand.

**Vocabulary you will hit immediately.**
- **cell** -- one unit of assigned work, e.g. `C02-g-10`. Its written specification is a "face"
  (a Markdown file under `org/tier1_exec/2.0.0_SA_COO/deliverables/`).
- **TO** -- Task Order, the assignment document naming the acceptance criteria.
- **proof-of-spec** -- a JSON file this seat must produce per TO, listing each criterion with its
  evidence and a PASS/FAIL/UNCOMPUTABLE verdict. Validated by
  `python .tools/proof-of-spec-check.py <instance.json> <comma,separated,criterion,ids>`.
  **Read the return code UNPIPED**: rc=0 VALID, rc=1 INVALID, **rc=2 is a USAGE error, not a
  validation failure** -- this seat mistook one for the other today.
- **the fire** -- a scheduled 12:45 UTC production run of the chain.
- **the window** -- `0.0.0_AB_MSTR` periodically opens an "integration window", pushes everyone's
  commits to `origin/CLOUD`, and closes it. **While a window is OPEN you must not run
  `safe-commit`.** Watch your inbox for OPEN/CLOSED notices.
- Seats you will deal with: `2.0.0_SA_COO` (issuer -- assigns cells), `1.0.0_SA_CTO` (gate -- rules
  on conventions), `3.0.0_SA_CVO` (grader -- independently re-measures your claims),
  `0.0.0_AB_MSTR` (integrator -- runs the windows). **Andrew** is the human owner; his word is
  sovereign and is relayed verbatim.

**Two house rules that will bite you within the hour.**
1. Commit only via `.tools/safe-commit.sh --author "0.4.0_DS_ClientPlatform~N <0.4.0_DS_ClientPlatform~N@opal.agent>" -F <messagefile> -- <paths>`. Use `-F` with a
   message file written by the Write tool or Python -- **never** `-m`, and never build the message
   with shell `printf`/heredoc.
2. Repo-wide text searching in Bash (`grep -r`, `find`) is BLOCKED by a hook. Use `comp-find
   '<regex>' [path]` instead. It prints a denominator; **`0 hits across 0 files` means your path
   matched nothing (out-of-corpus), NOT that the term is absent.**

---

## 1. DONE -- closed, verified, with the pin and the instrument

**All four commits below are ON ORIGIN** (`origin/CLOUD` = `89edf8efc1c8de6d105f822c742bdbdccdbbd1a5`,
`git ls-remote` read 18:25:29Z; each confirmed with `git merge-base --is-ancestor`, positive control
`b6dad1f773` reads ON ORIGIN).

| Pin | What it is |
|---|---|
| `cfc15ce384` | Cell C02-g-10 remedy: stages `a07` and `a00` stopped hand-writing two provenance columns and now call the shared helper `rc.stamp_provenance` |
| `04498e9904` | The deploy ledger for that change |
| `e05f1a4f02` | Its proof-of-spec instance |
| `1befd43cef` | Cell C02-g-13 remedy: the classifier "vintage" digest made deterministic (`canon-json-v1`) |
| `2d094cbdb9` | Its ledger + proof instance |
| `60821ec25e` | Ledger amendment (see "unverified" below) |
| `9ca1e99f05`, `7e54c4157e` | Both proof instances upgraded to satisfy a new checker rung |

**Cell C02-g-10 (`ADVI_49F.c02-A07STAMP`) -- WHAT IT IS:** every table the chain writes carries two
bookkeeping columns, `_ingested_at` (which date is this data) and `source_pipeline` (who produced
it). Stage `a07` was filling `_ingested_at` with the **wall clock** instead of the data's date, so
re-running an old date stamped today. Fixed by routing both stages through the one shared helper.
Criteria A7-1, A7-2, A7-3, A7-5 are accepted by gate and grader. **A7-4 is deliberately
UNCOMPUTABLE** -- see section 3.

**Cell C02-g-13 (`ADVI_49F.c02-VINTAGEDIGEST`) -- WHAT IT IS:** `a07` also emits
`_classifier_vintage`, a hash meant to answer "did the securities-classification data change?". It
was computed over `str()` of a **Python set**, and set ordering is randomised per process, so the
value changed on **every run even when nothing changed** -- the exact opposite of its purpose. Now
computed by a named canonical form (`canon-json-v1`: sorted lists, `sort_keys=True`, refuse unknown
types) and each row carries a new column `_classifier_vintage_form = "canon-json-v1"` so a reader
can tell new values from old ones **by the row**, without knowing a deploy date. V-1, V-2, V-3 PASS.
**V-4 is deliberately UNCOMPUTABLE** -- see section 3.

**The 0824-vs-0833 cell -- WHAT IT IS AND WHY IT MATTERED.** 49 Financial has **two** Schwab custody
master accounts, `08242234` ("0824") and `08335338` ("0833"). Andrew asked whether 13 unattributable
nine-digit account numbers appearing in a 49F data feed belong to the 0833 book, saying that if they
did he would "need to have a discussion with leadership". **Answer: they do not.**
- Measured on each book's own account record with that book's own custodian field:
  **0 of 13 in 0833** (`schwab/08335338/silver/fact_acc`, 7,371 rows, `custdian_id`=SCHWAB,
  `master_account_name`=49 FINANCIAL) and **0 of 13 in 0824** (7,291 rows,
  `master_account_name`=49 WEALTH MANAGEMENT LLC).
- Controls fired both ways: 5,787 of 5,791 ordinary eight-digit accounts from the same feed **are**
  found in the 0833 book through the identical code path, and a fabricated number is rejected.
- **Cell CLOSED**, graded PASS by `3.0.0_SA_CVO`, who reproduced every figure on their own reads.

---

## 2. IN FLIGHT -- and exactly where it stops if nobody touches it

**Nothing is mid-edit. No file is half-written, no deploy is half-landed, no ledger is left open.**
If nobody touches this seat, the chain keeps running daily and the two cells simply wait for their
scheduled fires (section 3). There is no cleanup owed and no rollback pending.

The one thing that is *in motion elsewhere and depends on measurements this seat supplied*: a
**management-facing document about the 13 accounts** is being written by `1.0.0_SA_CTO`. This seat
owes it nothing further; all requested figures were delivered.

---

## 3. CLOCK/EVENT-GATED -- what fires, what it proves, what failure looks like

These are the only outstanding obligations of this seat, and they cannot be done early. **Do not try
to satisfy them with an ad-hoc run**: running the chain manually with `--upload` would overwrite the
served output and destroy the very evidence the scheduled run exists to produce. (That exact mistake
masked a real bug for a week earlier this month.)

**MONDAY 2026-08-31, 12:45 UTC fire -- carries THREE separate reads.**

1. **Stage a06's map-vintage line.** a06 picks the newest *populated* partition of an upstream
   "allocation map" table. Expect these two lines in the chain log, verbatim:
   ```
   map resolution: chose date=2026-08-28 of 47 partition(s); SKIPPED header-only: 2026-08-30, 2026-08-29
   map date=2026-08-28: 7,359 rows | fact_acc universe 7,371 (date=2026-08-28) | map_carried=False
   ```
   **`map_carried=False` is the unusual value and it is correct on Monday only** -- every weekday run
   shows True. FAILURE LOOKS LIKE: a third skip, a different chosen date, `map_carried=True`, or the
   stage aborting (aborting is the pre-fix behaviour and killed two Sunday/Monday runs in August).
   ASSUMPTION: no new map partition lands before 12:45Z; upstream has landed at ~13:17Z on each of
   the last three days, i.e. *after* the fire.
2. **Cell C02-g-10 criterion A7-4, second half.** Read the fire's output objects (not the logs) for
   `dim_asset_classification`, `alias_key_expansion` and `dim_account`. Each must carry
   `_ingested_at` == the chain date and `source_pipeline` == `49f-gold-runners`.
3. **Cell C02-g-13 criterion V-4, first fire.**

**TUESDAY 2026-09-01, 12:45 UTC fire -- V-4's second fire.** V-4 requires **two consecutive fires**
with an unchanged substrate producing the **same** `_classifier_vintage`. **One fire cannot settle
it** -- a randomised digest also produces exactly one value on a single run. Filing PASS after Monday
alone is precisely the error the criterion exists to prevent.

**After both:** re-file the two proof instances with A7-4 and V-4 resolved, at
`org/tier2_senior/0.4.0_DS_ClientPlatform~N/deliverables/ADVI_49F.c02-A07STAMP.proof_of_spec.json`
and `...c02-VINTAGEDIGEST.proof_of_spec.json`. `3.0.0_SA_CVO` reads the same objects independently.

---

## 4. OWED BY THIS SEAT to another seat

**Nothing.** No seat is blocked on this one. The three timed reads above are owed to the record, not
to a person. Cells C02-g-12 was absorbed into C02-g-10; no other cell is queued here.

---

## 5. ⛔ UNVERIFIED, UNCERTAIN, OR RESTING ON ONE INSTRUMENT -- distrust these first

A closure log that reads uniformly clean is the one to distrust. Here is everything soft:

1. **The CRLF deploy hazard is fixed in MECHANISM but NOT EXERCISED.** Some tracked Python files
   have Windows line endings in the working tree while Git stores Unix ones, and the deploy gate
   historically uploaded the working-tree bytes -- so the served file could differ from the recorded
   one. `0.7.0_AE_CloudOps~K` fixed it at `3d9eb2931d` (the gate now uploads the Git index blob).
   **This seat read that fix at source but NOTHING HAS UPLOADED THROUGH IT YET** -- two windows ran
   with a deploy ceiling of zero. Until an upload actually exercises it, the only thing demonstrated
   to have put correct bytes on that key is a **manual** normalisation a human did once. Recorded in
   the ledger amendment `60821ec25e`. **Do not record this class as closed on the strength of the
   commit.**
2. **One inbox message is READ but UN-ACKED, and the id cannot be recovered right now.** The broker
   has an open defect: when its return value is lost it also omits the `**Msg-ID:**` header from the
   delivered file. Exactly **1 of 285** files at this seat is affected --
   `20260830T170229Z_0.0.0_AB_MSTR_THE_DEFECT_FIRED...md`. `get_delivery_state` fails on both query
   forms, so the row cannot be looked up. **The id was NOT guessed** (house rule LD-0480: ack only
   from the Msg-ID line). When the broker reader is repaired, look this row up by recipient +
   timestamp + subject and ack it.
3. **Every ack this seat issued today is UNVERIFIED.** `ack_messages` returns a success string, but
   that string is the tool describing itself; the delivery row is the evidence and the reader is
   down. They are *probably* fine (writes reportedly land) but nothing available distinguishes
   "acked" from "silently lost".
4. **The `_classifier_vintage` fix is verified across processes but never yet across two real
   scheduled runs.** That is exactly what V-4 is for. Until Tuesday, determinism is demonstrated in
   a harness and in three ad-hoc runs, not in production.
5. **A claim this seat did NOT verify, closed by the grader instead.** The 18 rows of the 13
   accounts sum to `$12,293,768.23`. Three of the 13 keys appear on multiple rows, so that sum would
   be **inflated** if the amount column were an account total repeated per row. `3.0.0_SA_CVO`
   tested it (values differ within a key, so it is a per-allocation amount and summing is correct).
   **This seat's own additivity check could not have caught it** -- 8-digit + 9-digit == total holds
   under double-counting too. Treat the figure as sound but know which seat proved it.
6. **"FMTC" is measured; "Fidelity" is not.** The 13 accounts carry registration text like
   `FMT CO CUST IRA & FBO <person>` in a free-text `account_name` column -- present on 15 of 18 rows
   (11 of 13 distinct keys; **label the unit, the two denominators differ**) and on **0 of 7,341**
   ordinary rows. The string `FIDELITY` appears **nowhere** in that table. That FMTC abbreviates
   Fidelity Management Trust Company is standard industry nomenclature and **an inference, not an
   estate measurement.** Also note this is a *registration string in a name field*, which is weaker
   evidence than the 0833 book's structured `custdian_id` column.
7. **Not measurable in-estate at all:** which custodian those 13 accounts actually belong to. The
   only table carrying a custodian NAME (`smartx/platform/silver/fact_account_detail`) is dead --
   47 partitions, 46 with zero rows, the one populated partition six weeks stale and containing none
   of the 13. Andrew has approved *asking 49F directly*; **no agent contacts 49F -- that act is
   his.**

---

## 6. Facts that exist only in session context -- written down before they are lost

- **The allocation map has a column no chain reads.** `smartx/platform/silver/fact_allocation_account_map`
  has 9 columns; stage a06 reads 3. The custodian registration text lives in `account_name`, one of
  the 6 nobody reads. That is why the FMTC label went untraced for a whole session.
- **The SmartX feed is NOT stored under either Schwab master.** `smartx/` is its own top-level S3
  prefix; a06 crosswalks it to Schwab account numbers. "SmartX = 0824" is true as a *business
  purpose* mapping and false as a *storage location* claim.
- **`git log --date=format:"%H:%MZ"` renders LOCAL time while printing a literal `Z`.** It made
  16:57 UTC commits look like 12:57Z here. Never type a literal `Z` into a date format string.
- **`git show <sha>^:<path>` through Python `subprocess(shell=True)` silently loses the `^`** on
  Windows (cmd.exe escape character), so both refs resolve to the same commit and a before/after
  comparison compares a commit to itself and reports "identical". Use `~1`, or `shell=False`.
- **The 0833 book's account-id column is zero-padded to 10 characters.** Comparing raw 9-digit keys
  against it returns "not found" **by format, not by absence**. This seat nearly reported that as a
  definitive answer; the padding must be applied to both sides (`zfill(10)`), and a positive control
  must traverse the same padding path or it proves nothing.
- **The two Schwab masters carry different legal entity names** in the custodian's own record:
  0824 = `49 WEALTH MANAGEMENT LLC`, 0833 = `49 FINANCIAL`.

---

## 7. Push state of this log

This file is committed after the previous log `a4884be6e3`, which was **LOCAL** at 18:25:29Z and
rides the next integration window. No window was open at the time of writing (last notice: CLOSED
18:16Z). If a window is open when you land this, hold `safe-commit` until the CLOSE and say so.
