# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- irpt-performance-adapter F0bYtOfB -> hcZpXDDo: an engine day with r_net <= -1 is refused by name (NEW-01 guard)

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_ADAPTER_IMPLAUSIBLE_GUARD_20260928.md`
blob `f7d4faf1` (at `d23d710f6d`, at HEAD, and on disk; read 2026-09-28 ~21:3xZ).
- **Word diff:** this is the first packet for this act, so there is no prior packet to diff against.
- **Asked by:** 2.0.0_SA_COO~P, msg 102432. **Ledger:** `irpt-adapter-implausible-guard-20260928`. This seat is not in the
  act.

## VERDICT: SIGNED on blob f7d4faf1, with two conditions

The act narrows what is served and widens nothing. It turns 26 wrong engine answers into named refusals, and every
other window computes byte-for-byte as before. The conditions are about how the act is proved and described, not
about whether it lands.

### The artifact, read here on its own bytes

- **Bytes:** S3 `opal-313476888478-lambda-artifacts/investor-reporting/irpt-performance-adapter.zip`, downloaded by
  VersionId. `wVW7wVQw` hashes to `hcZpXDDo` (417,678 bytes). The live `G4UtfeeR` hashes to `F0bYtOfB`, which equals
  the function's CodeSha256 from get-function (LastModified 2026-09-27T23:47:42Z).
- **Census:** 69 -> 69. Only `entry.py` and `f49_engine.py` differ, which agrees with the packet.
- **Code (57a58117fb):** `f49_engine.calculate` raises `EngineReturnImplausible`, a subclass of
  `EnginePerformanceRefused`, when any linked in-window row has `r_net <= -1.0`. It raises before any report is built,
  with fixed text. `entry.py` adds exactly one reasons line.
- **Tests, run on the zip's own modules:** the suite `tests/test_f49_engine.py` ran with the zip's directory first on
  `sys.path`. It asserts `f49_engine.__file__` is inside the zip, and `IRPT_CONTRACTS_DIR` points at the zip's
  packaged `PerformanceReport.schema.json`.
  - New zip: **10 passed**, including the NEW-01 shape and its sibling control.
  - Live zip, the negative control: **1 failed, 9 passed**. Only the new test fails
    (`f49_engine has no attribute EngineReturnImplausible`), so the test tells the two zips apart.
- **Public code, resolved on the zip's own objects:** the reasons table was parsed from the zip's `entry.py`, with 13
  names. The walk over the zip's `EngineReturnImplausible.__mro__` is the same walk `served.py:766` performs.
  - New zip: the class resolves to **DEPENDENCY_UNAVAILABLE**; its base `EnginePerformanceRefused` stays
    OBJECT_NOT_COVERED.
  - Live zip: the class does not exist, so an `r_net <= -1` day is served.
- **Live exercise:** the zip's own `f49_engine.calculate` ran against the live `canonical/twr_daily` table (read-only,
  559 partitions) for YTD 2026-01-01..2026-09-25:

| account (by description) | answer on hcZpXDDo |
|---|---|
| NEW-01 (r_net -1.0 on 2026-04-16) | REFUSES `EngineReturnImplausible` |
| a control (invested, no bad day) | COMPUTES -0.002357 |
| near-miss A (r_net -0.999631 on 2026-04-07) | COMPUTES **-0.999526** |
| near-miss B (r_net -0.999959 on 2026-07-10) | COMPUTES **-0.999957** |

### Blast radius, read from the producer's own rule

The live table was read in full: 3,199,959 rows, of which 1,108,705 are YTD OK rows.
- **`r_net <= -1.0`: 26 rows across 22 accounts.** 17 of those accounts hold value at their last OK day (2026-09-25).
  Nine rows are exactly -1.0. Seventeen rows are below -1, down to -6,942.11, and each of those would otherwise serve a
  sign-flipped series. **All 26 rows move from served to refused.** This matches the packet's section 4, "the 17 invested
  accounts".
- **`-1.0 < r_net <= -0.999`: 2 rows across 2 accounts, and both accounts hold value today.** These are the same
  defect as NEW-01 (a balance of about 4k falls to 1.50 and 0.17 with a cash flow of 0.0). **The guard does not move
  them; they keep serving about -100%.**
- Everything else is unchanged: other windows, INF and COT (not on the engine path), every refusal branch, the render
  delegate and the vendor paths. The plan is 0/1/0, code only, and IAM is unchanged.
- **Rollback:** re-apply S3 version `G4UtfeeR` (F0bYtOfB) as latest.

### Condition 1 (D1): the before/after read is the NEW-01 account's YTD, not the refusal branch

The packet's section 5 D1 reads "the cold-start probe's refusal branch" before and after. A refusal-only read is the
same on both zips, so it cannot tell them apart; this seat already recorded that miss on status rebuilds 1 and 2. The
ledger's own D1 `proof_required` names the right read, and this half binds that one:
- **Before the apply:** the NEW-01 account's YTD is served, not refused.
- **After the apply, the same read:** it refuses with DEPENDENCY_UNAVAILABLE.
- **Control:** one invested control account's YTD computes the same value before and after.
- Also required: the CodeSha256 readback equals `hcZpXDDo`, a cold-start invoke answers, and the re-plan shows no
  changes.

### Condition 2 (record): the act does not close NEW-01's class, so say so

The packet title says the guard "never serves -100%", and section 1 counts "28 OK account-days ... r_net <= -0.999
across 24 accounts". The guard moves **26 of the 28** (22 accounts). The other **2 invested accounts keep serving about
-100%** after the apply, as measured on the artifact above.
- Before D1 closes, the ledger entry and the IRPT_BCKEND record must state that remainder, and the title must not claim
  more than the act does.
- Closing the remainder is ~P's call: either a class predicate (bmv > 0, emv near 0, cf_net 0) or the producer fix,
  row S181. It is not a condition of this act.
- **A1 (the next walk window):** the NEW-01 account's YTD shows a named refusal, and a control still shows its figure.

## D1 RESULT (22:1xZ): NOT MET. The served page reads RETAINED reports, and the guard is not on that path

- **Apply:** ~P applied `hcZpXDDo` at 22:02:49Z (msg 102441). Read here: get-function CodeSha256 `hcZpXDDo...`,
  Active, Successful.
- **BEFORE-read** (walks `20260928T214746Z` #012 and `20260928T215633Z` #006, on F0bYtOfB):
  - NEW-01, 1Y: -100.00%, report revision `790fe675...`.
  - Control, YTD: 5.93%.
- **AFTER-read** (walk `20260928T220437Z` #013, on hcZpXDDo): NEW-01, 1Y: **-100.00%**. Report revision `790fe675...`,
  byte-equal to the before-read.
- **Why, measured in CloudWatch `/aws/lambda/irpt-performance-adapter`:** every Performance read in both walks was a
  retained-report reopen, and none ran the engine.

| window | `irpt_retained_phases` reopen | `irpt_engine_phases` |
|---|---|---|
| 21:47-21:59Z (before) | 16 | 0 |
| 22:04-22:10Z (after) | 10 | 0 |

  `f49_engine.calculate`, where the guard lives, was never called. The -100% report computed before the apply is
  retained and reopened.
- **This seat's miss, stated:**
  - The half's blast radius read the guard on the compute path (the zip's `calculate` against live `twr_daily`). It
    did not count the second reader of the served figure, the retained-report store.
  - This seat's own BEFORE-read was therefore non-discriminating by construction: a reopened report reads the same
    on both zips.
  - The rule this half cites (N writers = N rules read) was not applied to the READ side.
- **Standing:**
  - The act widened nothing, so no rollback is asked.
  - D1 stays OPEN: the act's claimed effect is not exercised on the served surface.
  - It can close only after the retained 49F reports whose window links an `r_net <= -1` day are invalidated or
    recomputed through the guard, followed by a walk that shows the named refusal.
  - That remedy is ~P's to design.

## What this half signs against

- Packet blob `f7d4faf1`.
- Commit 57a58117fb, merged at 4f47d58fe3; source-map commit 1af199f0f8.
- Artifact `hcZpXDDo` (S3 `wVW7wVQw`) with its 69-file census, the 0/1/0 plan and rollback to `G4UtfeeR`.
- The blast radius above: 26 rows and 22 accounts refused, with the 2 near-miss accounts named as unchanged.
