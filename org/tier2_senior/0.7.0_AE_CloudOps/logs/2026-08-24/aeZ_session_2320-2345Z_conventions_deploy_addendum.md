# 0.7.0_AE_CloudOps~Z -- ADDENDUM: the conventions deploy, and a sha my own earlier log now names wrongly

**archetype:** DEPLOY

**Window:** 2026-08-24T23:20Z -> 23:45Z. **This entry exists mainly to correct two of my own logs.**

---

## ⛔ READ THIS BEFORE CITING EITHER EARLIER LOG TONIGHT

`aeZ_session_2006-2240Z_...` records `etfs-netassets-daily` live at
`CodeSha256 BEITykjhmRlEvcM8p9cBUFmKX7doqEP+jHGRPhOprxo=`. **That is now SUPERSEDED.**
A third deploy landed at 23:24:00Z:

```
  etfs-netassets-daily   BEITykjh...OprxoU=  ->  xosks8suawJqxyE0DW2yIHzso5tPPTwnQSa7h8Ua4OU=
                         1,126 lines         ->  1,335 lines
  last_deployed_commit   4e5800fde0          ->  d7aa525fa9  (the TO-4 conventions commit)
```
**A closed record is a snapshot, not an oracle** -- my own banked lesson, and the more precisely
someone cites those two logs the more confidently they can now be wrong. Both remain accurate AS OF
their windows; neither carries a forward reference to this one, which is exactly why this entry
leads with the correction rather than burying it.

## What happened

`0.4.0_DS_ClientPlatform~Z` STOPPED before writing the Z-S16 as-of fix, having measured that the
fields it would point at do not exist in the deployed bytes. `1.0.0_SA_CTO~Z` upheld the stop and
classified the 209-line gap: **PENDING DEPLOY, not drift** -- conventions commit `d7aa525fa9` at
22:26:48Z is **two hours AFTER** the 20:31:09Z deploy. Ruling 5732: deploy the conventions layer,
THEN the as-of fix, both before 13:00Z. **Step (1) was mine.**

>> **THE CLASSIFICATION IS THE WHOLE LESSON: "209 lines behind its tree" invites INVESTIGATE and the
>> correct reflex was DEPLOY.** The two are indistinguishable from the line count alone; only the
>> timestamps separate them. A drift finding and a pending-deploy finding look identical and take
>> opposite actions.

## Acceptance -- CTO~Z's check, run on the DEPLOYED BYTES

```
                                     BEFORE      NOW
  vendor_trueshares_Date                0          2
  as_of_basis                           0          5
  POSITIVE CONTROL fetch_trueshares_holdings       3    <- the census discriminates
  NEGATIVE CONTROL zzz_no_such_token_9999          0
  package sha == live CodeSha256                 YES
  member RAW-matches its HEAD blob               YES
  0-diff re-plan                                 rc=0 (no pipe)
```
**DS~Z's fix now has its input.** Against the prior bytes it would have been authored against the
tree, passed commit-gate, cited Andrew's ruling correctly, and changed nothing -- which is the most
dangerous shape available, and their stop is what caught it.

I re-derived the pending-deploy classification before acting, and applied my own 21:45Z constraint to
myself: verified the packaged file was COMMITTED and tree==HEAD before building, rather than trusting
that I would remember the rule I had written for someone else.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `deploy_ledger.py` | `open` (5 legs) / `close-leg` x5 / `close` | PASS | Third ledger of the session; opened at deploy-START, closed in-session. |
| live AWS primitives | `get-function-configuration`, `get-function` -> Code.Location download | PASS | The acceptance check is a CODE-layer read of the running package, not a tree read -- which is the entire point of the ruling. |
| `terraform` (via `safe-apply`) | plan / apply / `-detailed-exitcode` | PASS | 0 add / 1 change / 0 destroy; rc=0 re-plan. |
| `git log` / `git show` | timestamp + blob comparison | PASS | The timestamps are what classified pending-deploy vs drift; the blob compare is what proved the package matches HEAD. |

**Gap found (SECOND TIME TONIGHT, same tool).** `record-terraform-deploy.sh` routed around again --
measured CRLF-rewrite defect on this box. Set the three fields by hand with a script that PROVES the
JSON round-trip lossless on the UNMODIFIED file before writing. **Twice in one session is no longer
an incident, it is a cost the estate is paying per deploy**, and it is the tooling lane's to fix.

## Blockers

**None.** Three deploys tonight, three ledgers, all closed in-session, none stranded.

## Current State (supersedes the corresponding lines in both earlier logs)

- **`etfs-netassets-daily`**: `CodeSha256 xosks8suawJqxyE0DW2yIHzso5tPPTwnQSa7h8Ua4OU=`,
  1,335-line member, `last_deployed_commit d7aa525fa9`, `last_deployed_at 2026-08-24T23:24:00Z`.
  Carries the TO-4 conventions layer. Trigger `cron(0 22 * * ? *)` unchanged.
- **`etf-positioning-producer`**: `CodeSha256 sR9QvfiS82IyXzRC4JUECpn1yFxLKfSehqT32nteems=`
  (marshal fix), 512 MB / 120 s, `cron(0 13 * * ? *)` ENABLED. Env: `ETFS_BUCKET` +
  `OPAL_ETFS_PUBLISH_GRANT` only.
- **Source map** 201 functions; both ETF rows current on all three Rule-4 fields.

## ⛔ APPENDED 23:52Z -- A CORRECTION TO MY OWN EARLIER LOGS, AND A SECOND OBLIGATION

⛔ **RE-CORRECTED 23:46Z -- READ THIS BEFORE THE PARAGRAPH BELOW IT.** `1.0.0_SA_CTO~Z` (5893)
withdrew their own "second cause" framing after opening the file gold ACTUALLY CONSUMED:
```
  silver/holdings/2026-08-21.parquet   <- named by gold's own manifest as its input
     114 rows · PFDE filepoint 90 · PFOE filepoint 24 · TrueShares rows: ZERO
```
**That partition was written FRIDAY -- before the TrueShares capture ever worked.** My F2 remediation
went live 20:31:09Z tonight; the first partition that has ever contained DIVZ/IDVZ holdings is
`2026-08-24`. **So TODAY's cause is SINGULAR: gold reads T-1 = Friday, and Friday's file predates the
fix.** It is NOT a join failure and NOT a characteristics gap.
>> **THE CHARACTERISTICS COVERAGE ISSUE IS REAL AND IT IS A FUTURE RISK, NOT A PRESENT CAUSE.** It
>> becomes operative at TOMORROW's 13:00Z fire, when gold reads T-1 = Monday 08-24 -- the first file
>> with 73 TrueShares rows in it -- and the join actually has something to miss on. **My 11:00Z read
>> obligation therefore STANDS UNCHANGED**; only the reason it exists is re-dated. The paragraph
>> below is preserved as written because its conditional ("if the characteristics leg misses,
>> tomorrow...") was always about TOMORROW and remains correct; what was wrong is calling it a cause
>> of TODAY's shells, which is CTO~Z's framing that I adopted and repeated.
*Three seats reasoned about the chain; the answer came from opening the file. That is the fourth time
tonight the resolution was to drop a layer rather than arbitrate between two readings.*

---

`1.0.0_SA_CTO~Z` (5806) found what was then called a **SECOND cause** for the DIVZ/IDVZ shells, and it
makes a line in my two earlier logs incomplete in its implication.

**What I wrote:** *"tonight's rows reach gold at TOMORROW's fire, by design."* **Literally true and
it stays true** -- the rows do reach gold tomorrow. **But the natural reading is "so the shells
resolve tomorrow," and that is NOT established.** Measured by CTO~Z:
```
  bbg/2026-08-21/characteristics.parquet   109 rows
  AAPL present · NVDA present     BBSEY ABSENT · AMX ABSENT · CPA ABSENT · BNPQY ABSENT
  109 == the PRE-A5 universe count. The DIVZ/IDVZ constituents are not in the attribute file at all.
```
>> **HOLDINGS ARRIVING IS NECESSARY AND NOT SUFFICIENT.** The gold producer JOINS holdings to the
>> Bloomberg per-security characteristics; if those do not cover the securities, the rows arrive with
>> a NAME AND NOTHING ELSE -- *not a filled book, an empty one with more rows*.
**TPG is today's one-row live specimen**: `2602335D` (a Bloomberg internal id where a ticker belongs)
is ABSENT from characteristics, so it serves as `Equity / null / weight 0 / all-null returns` and
renders "Other". **That is what all 73 TrueShares rows do if the join misses.**
**I am recording this against my own log rather than leaving it to be discovered**, because a
successor reading "by design" would reasonably infer the books fill and would be wrong for a reason
my sentence does not contain. *An accurate statement with an unstated precondition is the shape this
session kept catching; this one is mine.*

## Next Steps

- [`0.4.0_DS_ClientPlatform~Z`] TO-7 step (2): the as-of VALUE fix at `:526`. **Input is now live.**
- [`0.7.0_AE_CloudOps~Z`] ⏰ **NEW, and it comes FIRST: READ THE 07:00 ET LEG BEFORE 13:00Z**
  (CTO~Z 5806, jointly with `0.0.0_AB_MSTR~Z`). **A READ, not an assumption:** the emitted
  constituent count, and a spot-check that **BBSEY and AMX are present in the emitted
  characteristics**. The 07:00 local fire is **11:00Z**; the producer fires **13:00Z**; **that ~2h
  window is the only place this is cheap.**
  ⛔ **THE RISK IS NAMED: A5 HAS NEVER BEEN EXERCISED END TO END.** MSTR~Z deployed it and correctly
  declined a full-script run to avoid muddying which run tomorrow's evidence belongs to -- so
  **tomorrow's 07:00 fire is A5's first real run, and the whole DIVZ/IDVZ fill sits behind it.** If
  that leg fails, 13:00Z produces books with names and nulls.
  ⭐ **APPENDED 23:57Z -- WHAT THIS READ IS ACTUALLY FOR, and it is not what I first wrote.**
  `0.4.0_DS_ClientPlatform~Z`'s reframe, adopted by CTO~Z (5846): if the characteristics leg misses,
  **tomorrow the books flip from HONEST SHELLS to FULL-LOOKING BOOKS WITH REAL WEIGHTS AND BLANK
  ANALYTICS.** A `book_only` shell reads as *"not there yet."* A 44-row book with real weights, real
  prices and blank yield/beta/sector reads as **a partially broken product.**
  >> **SO THIS READ IS NOT "de-risk the fill." IT IS "find out BEFORE 13:00Z whether tomorrow looks
  >> WORSE than tonight."** That is a different question with a different urgency, and the ~2h window
  >> is the only place it can be answered while it is still cheap -- after 13:00Z the books LOOK full,
  >> and a looks-full-but-empty artifact is exactly the class that stops people asking.
- [`0.7.0_AE_CloudOps~Z`] **AC7, ~13:00Z 2026-08-25** -- the first SCHEDULED fire of
  `etf-positioning-producer`, observed at its own invocation record, `run_class: "scheduled"`.
  **Expect ONE invocation and ONE manifest. If three appear, the marshal fix did not take -- report
  that, do not reconcile it.**
  ⚠ **AC7 AND THE FILL ARE DIFFERENT QUESTIONS AND MUST NOT BE FUSED.** AC7 asks whether the
  SCHEDULE fired correctly. Whether the books FILL is a different question AC7 does not measure.
  **A green AC7 on empty books is a possible and correct outcome**, and reporting it as a pass on the
  product would be the instrument-lies shape this project exists over.
  ⛔ **APPENDED 23:53Z -- THERE ARE NOW THREE INDEPENDENT REASONS THE BOOKS COULD STILL BE EMPTY
  TOMORROW, AND AN OBSERVER WHO CHECKS ONLY THE FIRST TWO WILL MISATTRIBUTE THE THIRD:**
  ```
  (1) T-1 FILE PREDATED THE CAPTURE   -- today's singular cause. RESOLVES tomorrow by construction:
      gold reads T-1 = Mon 08-24, the first partition that has ever held TrueShares rows (73).
      Measured by CTO~Z: bronze trueshares holdings exists ONLY for 20260824/, and silver
      08-19..08-23 are all 114 rows / trueshares 0. There was never anything earlier to read.
  (2) CHARACTERISTICS COVERAGE        -- MY 11:00Z READ. Becomes operative tomorrow for the first
      time, because only then does the join have TrueShares rows to miss on.
  (3) ⭐ GLOBAL AS-OF -- A DESIGN DEFECT, NOT A TIMING ONE (Andrew ~23:5xZ, CTO~Z 5922).
      His word: "We should be able to display data for all 4 ETFs every day." `resolve_as_of`
      returns ONE GLOBAL as-of for all four funds, so ANY FUND WHOSE HISTORY STARTS LATER IS EMPTY
      BY CONSTRUCTION. The fix is PER-FUND AS-OF. DS~Z's lane; not mine, and NOT fixed by anything
      I deployed tonight.
  ```
  >> **SO IF TOMORROW'S BOOKS ARE STILL EMPTY, THE ANSWER IS NOT AUTOMATICALLY "THE DEPLOY FAILED"
  >> OR "THE SCHEDULE FAILED."** Check the disjunction in order and name which one, on evidence.
  >> **AND (3) IS THE ONE THAT SURVIVES A CLEAN (1) AND (2)** -- it is structural, so it will still
  >> be there on a day when the file is right and the characteristics are right.
- [`0.7.0_AE_CloudOps~Z`] **DEPLOY TO-7's as-of VALUE fix -- DEADLINE 22:00Z 2026-08-25, *NOT* 13:00Z.**
  Measured gap: `_v_ts_Date` tree 5 / deployed 2 -- it is in MY Lambda and NOT running.
  ⛔ **DO NOT INHERIT THE 13:00Z CLOCK FROM THE ITEMS NEXT TO IT.** silver 08-24 was written
  2026-08-24T22:00:17Z by the OLD code; 13:00Z gold READS that already-written partition, so a deploy
  at any hour before it changes nothing about what 13:00Z serves. **The first partition the fix can
  affect is the 08-25 silver write at 22:00Z.** Only the AC3 re-derive can change what 13:00Z serves.
  **Do not deploy while DS~Z is mid-edit** -- packaging a half-finished tree against a deadline that
  does not exist is the worst of both.
- [`0.7.0_AE_CloudOps~Z`] **DEPLOY the AC3 bronze re-derive when DS~Z lands it** (CTO~Z 5934; DS~Z
  build started, feasibility HIGH). **ACCEPTANCE IS A NETWORK ASSERTION, NOT AN INSPECTION:** it must
  read existing bronze and perform **ZERO issuer HTTP** -- *exercise it and assert zero outbound
  requests.* A grep answers PRESENCE; only the run answers BEHAVIOUR, and that gap is what this whole
  session kept finding.
  ⛔ **AND THE REQUIREMENT I AM MOST LIKELY TO SKIP: the re-derived partition must SELF-IDENTIFY.**
  A scheduled-produced partition silently overwritten by an ad-hoc act, with nothing in the object
  saying so, **is the provenance defect committed by the fix for it.** `run_class` is the precedent.
  **Do not deploy a re-derive that lacks the equivalent.**
  If it cannot be built AND verified before 13:00Z: **WITHHOLD** (CTO~Z (3)). One day of known-wrong
  provenance, recorded and surfaced, beats a partition nobody can attest to.
- ⛔ [`0.4.0_DS_ClientPlatform~Z` owns the disarm; recorded here because I deployed the bytes]
  **ARMED HAZARD, LIVE NOW ON `etfs-netassets-daily`:** `:1183`
  `run_date = event.get("run_date") or now.date().isoformat()` -- operator-supplied, with **no replay
  path behind it** (rederive/from_bronze/SKIP_FETCH/BRONZE_REPLAY all 0). An invocation that LOOKS
  like a replay -- `{"run_date":"2026-08-24"}` -- **re-fetches the CURRENT sheet and lands it under
  the OLD date**: a FABRICATED OBSERVATION, reachable by one plausible call. Found by
  `0.0.0_AB_MSTR~Z`, confirmed by me on the DEPLOYED bytes with controls.
  **NOTHING IN THE AE LANE DISARMS THIS** -- the parameter is read inside the handler; IAM cannot see
  an invocation payload. The only AE-lane control is an operational rule with no enforcement:
  ***never invoke `etfs-netassets-daily` with a `run_date`*** -- stated as a stopgap and labelled as
  one, because MSTR~Z's whole point is that a rule is not a control. **The real disarm is code, and
  the AC3 build is its natural vehicle** (make `run_date` imply bronze-replay rather than re-fetch),
  so doing AC3 properly closes this as a side effect. **It predates my deploys and survives them.**
- [tooling lane] `record-terraform-deploy.sh`: fails closed on cp1252, CRLF-rewrites under the UTF-8
  workaround. Routed around twice tonight.
