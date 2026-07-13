# INF phantom advisor -> ROOT CAUSE -> the TIME-LOCK (Andrew-ruled)

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, VALIDATE

**Agent:** 0.4.0_DS_ClientPlatform
**Window:** 2026-07-13 10:34Z -> 15:03Z (`2ffb0bdb2` .. `53098d018`, 18 commits)
**Prior log:** `aor_forkB_round8_ssot_ledger_gates.md` (`dcf362496`). The round-8.2 series
(`558f54bc8`..`dbab19e4c`, 02:01-03:57 local) PREDATES this window and is covered by CVO~B's
gate-2 (`60529951f`) -- it is not re-reported here.
**Dispatch:** COO URGENT, question-first: *"WHY is rep_id NULL in silver for accounts 560/703/1225?
Read the silver converter. Do NOT build. Do NOT run a gold rebuild."*

---

## Summary

Answered the question, and the answer inverted three standing rulings. `rep_id` is **not a
transaction field** -- it is a LEFT JOIN from the CURRENT `accounts_v2` dimension onto a
FULL-HISTORY transaction spine (`convert_transactions_to_silver.py:519`), and **Orion's
`/Portfolio/Accounts/NewPortfolio` stopped returning 3 accounts on 2026-07-09**. That produced a
PHANTOM ADVISOR on the served client-facing spine holding **$52,604.80 of Patrick Scanlan's money**
for five days.

The same line is a second, larger defect: the nightly re-derived SIX YEARS of attribution from
today's roster on every pass, so ONE book transfer on 2026-07-08 handed Joe Brandenburg
**$2,106,047.92** of other advisors' history. Andrew ruled: *"history stays with whoever held it at
the time"* + *"the NNA is the HOUSE ACCOUNT for the period it is in the house account -- that is the
rawest approach rather than attempting to normalize."* Built the TIME-LOCK to implement it.

**Nothing served. Nothing wired. Chain held throughout.**

---

## Work Completed

### 1. ROOT CAUSE (`2ffb0bdb2`) -- the question, answered
- `rep_id` is MANUFACTURED by a LEFT JOIN from `accounts_v2` (`:519`); the script's own docstring
  says so at `:61`. `accounts_v2` has ONE source: `GET /Portfolio/Accounts/NewPortfolio`.
- Bronze diff: **2026-07-08 = 2,968 rows (all 3 present, `Fidelity_Inflection`, `clientId=227`,
  `isActive=True`, `representativeName='Patrick Scanlan'`); 2026-07-09 = 2,965 rows, ALL 3 ABSENT.**
- **Replayed BOTH pipeline gates against the 07-08 bronze row-by-row: KEPT/KEPT/KEPT.** We did not
  drop them; the vendor did.
- Four independent oracles (household_rep_mapping -- present in ALL 70 partitions; the firm roster;
  Custom Report 28198's `repName` ON the txn rows; the live REST spine) all say Patrick.
- **CORRECTED THE RULEBOOK:** CTO's `ef923bf10` amendment said *"roster presence plays no part in
  this derivation AT ALL"* -- true of `INF_C_01` in isolation, FALSE of the system. CTO amended
  CLAUDE.md against himself (`af3287053`).

### 2. COVERAGE + RESIDUAL GUARDS (`d52ab4cbe`, `883d66112`, `a233b84f5`)
- Two DISJOINT classes (measured, zero overlap): CATCHALL (3 accts -> phantom) and AT-RISK (14
  accts / $439,326.22 absent from the feed). **Neither guard catches the other's class.**
- **RETRACTED MY OWN PROVEN-RED** (`883d66112`): my live control was RIGGED -- I fed the guard a
  basis its own caller can never construct, watched it go RED, and called it a positive control.
  Rebuilt on the sound unit: the **(PARTITION, ACCOUNT)** pair.
- **FALSIFIED the $439K deletion premise** the whole fabric was acting on: the full re-derive
  ALREADY RAN on 07-10 (1,389 of 1,410 partitions) and all 20 rows SURVIVED. CTO~B then correctly
  sharpened it -- they are not SAFE, they are UNSTRUCK (survival depends on the DATA's shape).
- Guard **WATCHED RED on the real defect case** (real partition `canonical_nna_2026-01-15`, real
  account 47, 31 real co-tenants). All 7 of CTO~B's spec conditions met.

### 3. POST-DEPLOY IMPORT LINT (`a2af41a11`) -- CTO-ruled a gate
- **The guard I deployed at 07:22Z COULD NOT IMPORT.** head-object, `s3 ls`, hash match, the deploy
  log, `comp-pipescript deployed` and 28/28 unit tests ALL said GREEN. The actual import: ImportError.
- `.tools/deploy-import-lint.py`: downloads from the BUCKET, imports in a FRESH interpreter with an
  isolated `sys.path`. Goes RED on a broken bucket, PASSES on a good one, **ERRORS (never passes) on
  an empty prefix**. Self-test arm (`--expect-fail`).
- **A PRESENT FILE IS NOT A LOADABLE ONE, AND A GREEN SUITE IS NEITHER.**

### 4. ATOMIC DEPLOY + ARM (`c67c4fd6d`, `de041f640`)
- Refused CTO~B's first GO: it named 2 files, but `INF_C_01` imports `aor_resolution` (NOT DEPLOYED)
  and the guard imports `KNOWN_ADVISOR_KEYS` from a STALE 359-line `inflection_rep_scope`. Deploying
  as ordered would have replaced a WORKING script with one that ImportErrors. GO retracted, re-scoped.
- Shipped all 4 atomically. **VERIFIED BY IMPORT FROM THE BUCKET: 16/16 modules load; deployed
  guard-call count 0 -> 3; `AOR_FOLD_ACTIVE` OFF.**

### 5. PATRICK'S RESTORE (`10273505d`, `fa0e596f5`) -- co-signed, SERVE-HELD
- `rep_id` rescued from `household_rep_mapping` via `householdId` -- **the SAME canonical map
  `accounts_v2` itself reads.** READING, not inferring.
- Exercised through the REAL `build_silver`: 3,283 rows rescued; **DELTA-0 across 1,394,630 rows**
  (mutant-validated control); firm total conserved.

### 6. GATE-1 A + B (`59d70b95e`) -- CLEARED by CTO~B
- **A:** the floor closed the NULL and not the LOSS (floored `advisor_key`, left `rep_bucket` `<NA>`,
  which SILENTLY drops the row at `INF_09:193`). Floor BOTH atomically + ALARM + RAISE on incoherence.
- **B:** `.dropna()` converted a ROW claim into a COLUMN claim. Row-level assertion, FIRST.
- CTO~B's own falsifier arm A turned out to ASSERT THE DEFECT; he struck it.

### 7. THE TIME-LOCK (`18840dd26`, `877cdfc82`, `fd7764ce3`, `4a4c787cf`, `3b61cecb0`, `48904598a`)
- `lib/advisor_timelock.py` + `timelock_preview.py`. **The LOCK is the fix; the backfill is cleanup.**
- **The lock keys on a STAMP, not on existence** -- so a legacy row is not locked, gets derived
  correctly ONCE, and is stamped. **The backfill falls out of the lock's own rule. No mode, no env
  var, NO BYPASS** (structural test asserts the lib contains no `os.environ` at all).
- Poison assert: 2026-04-28 (96.2% catchall) + 2026-05-08 (0 rows) rejected BY PROPERTY. The ruling
  taken literally is a PERMANENT NIGHTLY OUTAGE -> three outcomes (usable / ACKNOWLEDGED-and-excluded
  by a reviewed decision / unacknowledged-and-RAISES).
- **MISSED A PRE-REGISTERED NUMBER TWICE AND MOVED NEITHER.** Both times the number was right and my
  story was wrong. ($705,895.51 -> Andrew overruled CTO; $3,512.28 -> the registration was incomplete.)
- **REFUSED to cast a silent policy vote** (`48904598a`): the time-lock and the AoR fold are OPPOSITE
  policies and the wiring order would have frozen the winner FOREVER. `assert_attribution_policy_settled`
  RAISES rather than choosing.

### 8. P1/P2/P3 (`53098d018` + the P3 measurement)
- **P1:** gold suite GREEN 184/184. **I had committed a RED suite** -- read the commit-gate line and
  not the test line. Census exception is EXPLICIT + REASONED + names its own death condition.
- **P2:** my preview was a FALSE ORACLE (derivation lived in TWO places). Now ONE shared function
  called by the preview AND the producer; structural test fails the build on a second caller.
- **P3: NOT BUILDABLE.** `advisor_of_record_raw` appears in **0 of 70** `accounts_v2` snapshots; the
  AoR field exists in EXACTLY ONE artifact estate-wide (`20260710_accounts_roster.json`).
  **YOU CANNOT DERIVE AN EFFECTIVE-FROM FROM A SINGLE OBSERVATION.** Routed as a RULING, not a build.

---

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-which "which script converts bronze transactions to silver..."` | PARTIAL | routed to `comp-dispatch`; did not fit. Fell through to `comp-glob`/`comp-grep` as designed (no dead-end). |
| `comp-glob "data/inf/scripts/silver/*.py"` | PASS | 18 silver scripts -- located the converter set. |
| `comp-grep "rep_id" data/inf/scripts/silver` | PASS | per-file DENOMINATOR (17 hits in `convert_transactions_to_silver.py`) -> identified the writer. |
| `comp-grep "rep_id_is_historical" .` | PASS | the census-by-FUNCTION that proved ZERO functional consumers (only a docstring + a comment). |
| `comp-pipescript io INF_C_01` | **FAIL** | reported **"WRITES: (none detected)"** for the script that writes the SERVED per-advisor NNA spine (`GOLD_NNA_PREFIX` at `:99`, `put_object` at `:217`). |
| `.tools/deploy-import-lint.py` (NEW, mine) | PASS | 16/16 deployed modules import; went RED on the broken bucket first, which is why its green means anything. |

**What worked:** `comp-grep`'s per-file counts gave me the write-site denominator immediately, and
the census-by-function on `rep_id_is_historical` is what proved the column is a comment with a dtype.

**What failed:** `comp-pipescript io INF_C_01` -> **"WRITES: (none detected)"**. It reports ONE read
and ZERO writes for a script that writes `gold/canonical/` and feeds the served advisor spine. An
agent trusting it would conclude `INF_C_01` has no downstream at all.

**Gap found:** (1) the `comp-pipescript io` I/O manifest is blind to `INF_C_01`'s writes (above) --
worth a maintainer look, since `comp-blast`/`comp-pipescript` reachability inherits from it.
(2) `comp-which` does not route a "which script WRITES silver X" question to a producer lookup;
`pipescript --resource` would have. Worth a routing entry.
(3) **`comp-pipescript deployed` answers "is the object there and does its hash match?" and CANNOT
answer "would this import?"** -- and we have been reading the first as if it were the second. That is
the `deploy-import-lint` gap and CTO has ruled it a gate.

---

## Briefs Written

| Brief | Path | Status |
|---|---|---|
| INF phantom advisor -- ROOT CAUSE | `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/INF_PHANTOM_ADVISOR_ROOT_CAUSE_20260713.md` | committed `2ffb0bdb2` |

---

## Files Modified

See commit messages: `2ffb0bdb2`, `d52ab4cbe`, `883d66112`, `a233b84f5`, `10273505d`, `59d70b95e`,
`a2af41a11`, `c67c4fd6d`, `de041f640`, `18840dd26`, `877cdfc82`, `fd7764ce3`, `4a4c787cf`,
`3b61cecb0`, `48904598a`, `53098d018`.

New files worth naming for a zero-context reader:
- `data/inf/scripts/gold/lib/nna_coverage_guard.py` -- coverage + residual guards (LIVE on the runner)
- `data/inf/scripts/gold/lib/advisor_timelock.py` -- the time-lock (NOT wired)
- `data/inf/scripts/gold/timelock_preview.py` -- read-only preview of the irreversible write
- `.tools/deploy-import-lint.py` -- the post-deploy import gate (CTO-ruled)

---

## MCP Traffic

~40 messages. Significant: COO's URGENT root-cause dispatch (opened); CTO `af3287053` (amended
CLAUDE.md against his own ruling on my evidence); my `[STOP]` on the bronze-pull repair (carried the
MECHANISM, not the verdict); CTO~B's GO -> my REFUSAL (import-closure contradiction) -> his
RETRACTION -> re-scoped GO; NEVER#2 co-sign (CTO + COO); Andrew's two rulings (HONOUR-CATCHALL;
"history stays with whoever held it at the time"); CVO~B's `[STOP]` on wiring (policy contradiction)
+ her pre-registered bar; my bar-finding to CVO~B (T1 blind spot) -- CONFIRMED and amended by her;
`~A` coordination on P3 (I kept it, he took INF_B_00).

---

## Blockers

**NONE that I own.** All waits are evidence-cited external gates:

1. **[RULING -- Andrew/CTO~B] P3, the date-aware fold.** BLOCKED ON DATA THAT DOES NOT EXIST, not on
   effort. `advisor_of_record_raw` is in **0 of 70** `accounts_v2` snapshots; the AoR field has ONE
   observation estate-wide. Cannot derive an effective-from from a single point. Proposed ruling:
   the fold applies FORWARD ONLY from first AoR observation; history uses the servicing timeline
   (70 snapshots, validated). **Fails closed today anyway** (column absent -> RAISES under switch-ON).
2. **[CVO~B] The first re-derive is an IRREVERSIBLE WRITE** and must be verified BEFORE it stamps.
   Her account-grain bar v2 is running; my `timelock_preview.py` is the artifact it consumes.
3. **[CTO~B / 0.7.0_AE_CloudOps] Chain release.** Held at the gold-dispatch chokepoint AND by the
   `build_assets_dim.py` basename collision. **I have not touched the collision by any verb.**

---

## Current State (zero-context handoff)

**LIVE ON THE RUNNER:** `lib/nna_coverage_guard.py` (coverage + residual guards) + `INF_C_01` +
`aor_resolution` + `inflection_rep_scope`, deployed atomically at `de041f640` and **verified BY
IMPORT from the bucket** (16/16 load; guard-call count 3). `AOR_FOLD_ACTIVE=0`.

**COMMITTED, NOT DEPLOYED / NOT WIRED:**
- `data/inf/scripts/silver/convert_transactions_to_silver.py` -- Patrick's $52,604.80 restore.
  CTO+COO co-signed (NEVER#2 satisfied). **DEPLOY-SERVE-HELD.** Ships when the chain is released.
- `data/inf/scripts/gold/lib/advisor_timelock.py` -- the time-lock. `apply_time_lock` is called
  **ZERO times**, and that is the CORRECT state, not a coast: the wiring order is an irreversible
  policy vote that only Andrew can cast, and `assert_attribution_policy_settled()` RAISES rather
  than casting it silently.

**THE NUMBERS (pre-registered, then reproduced -- do not adjust these; amend the bar instead):**
```
peter_lee                     104,647,053.28 -> 105,228,347.70
patrick_scanlan                14,036,951.32 ->  14,904,901.83   (incl. the phantom's 52,604.80)
joe_brandenburg                12,564,418.50 ->  10,458,370.58   (gives back 2,106,047.92)
inflection_wealth_management    1,806,639.74 ->   2,516,047.53   (ANDREW-RULED house periods)
inflection_unmapped_rep            52,604.80 ->           0.00   GONE
FIRM MAX nna                  133,107,667.64 == 133,107,667.64   *** UNCHANGED. IF IT MOVES, STOP ***
283 rows change. Reconciles TO THE CENT with CVO~B's independent roster-derived figures.
```

**SERVED TODAY (still wrong):** `platinum/firm/advisor_nna_canonical.json`, `data_as_of 2026-07-09`,
still carries `inflection_unmapped_rep` as an advisor. Day five.

**THE ONE-SHOT RISK, stated because it governs everything downstream:** the time-lock STAMPS
(`attribution_model`), and a stamped row is FROZEN. **The first re-derive is not a run; it is an
irreversible write.** If its derivation is wrong it is wrong permanently, escapable only by restoring
8,805 gold objects from backup. It does not serve until CVO~B's bar passes. I do not self-certify.

---

## Next Steps

1. **[1.0.0_SA_CTO~B / Andrew]** RULE P3: the fold is forward-only from first AoR observation (the
   date-aware mechanism has no input -- 0 of 70 snapshots carry the field). Blocking the wiring.
2. **[3.0.0_SA_CVO~B]** account-grain bar v2 vs `timelock_preview.py` output. Her bar gates; my
   output does not.
3. **[0.4.0_DS_ClientPlatform]** on the ruling: wire the time-lock, deploy ATOMICALLY with the libs,
   verify BY IMPORT from the bucket, then the one-shot -- verified BEFORE it stamps.
4. **[1.0.0_SA_CTO~B / 0.7.0_AE_CloudOps]** chain release + the `build_assets_dim.py` collision, as
   a gated act. Patrick's restore ships on that run.
5. **[CTO/CTO~B]** wire `.tools/deploy-import-lint.py` into `safe-deploy` as a post-deploy step --
   CTO ruled it a gate; it must land before the chain re-arms, because an unloadable lib is a dead
   nightly.

---

## Self-Reported Instrument Failures (7, all caught by controls, none by care)

1. A dtype `.isin()` returned all-False against a string column -- nearly sold me a whole wrong
   mechanism (a rep-10/Noel allowlist gap). The partition walk killed it.
2. My "proven-RED" coverage guard was RIGGED by my own harness. Retracted before the co-sign.
3. A DELTA control printed "0 rows changed" while reporting 3,283 rescued -- `pd.NA` in a boolean
   mask is dropped as False, so it discarded the rows it was measuring.
4. `"Ran 0 tests"` read as green -- pytest-style functions under `unittest`. Real denominator: 141.
5. An AST symbol-diff blind to `ast.AnnAssign` -- a LOST annotated symbol would have been invisible
   to my own regression check.
6. An exit code swallowed by a pipe (`| tail`) -- printed EXIT 0 on a run that correctly FAILED.
7. **I committed a RED test suite** -- read the commit-gate line, not the test line. In the tool
   whose entire job is to make an irreversible write safe.

*Knowing a failure mode by name does not immunize you against writing it. Controls over care.*
