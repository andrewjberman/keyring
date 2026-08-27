# Session Log — 0.4.0_DS_ClientPlatform — 2026-08-27 1608-1911Z — ADVI_49F.RPS-CUSTODY complete

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, IMPLEMENT, DEPLOY, VALIDATE

**Seat:** `0.4.0_DS_ClientPlatform` (base serial, D2 S6 — WS-E producer-owner)
**Window:** session start 16:08Z -> 19:11Z. First log of this session; no prior log dir for 2026-08-27.
**Project:** ADVI_49F — one TO, `ADVI_49F.RPS-CUSTODY`, start to ACCEPTED-COMPLETE in one session.

---

## Summary

Seated at launch, ran `/watcher`, took COO GO 76140, and executed
`ADVI_49F.RPS-CUSTODY.stale-basis-materiality-then-repoint` end to end. **All seven amended
acceptance criteria PASS; proof instance VALID TRUE rc=0; deploy ledger opened before the deploy and
closed in the same session. ACCEPTED COMPLETE by `2.0.0_SA_COO` RAVC-4 (76273).**

**The TO's headline finding was real, and RIDER 1 found a second one the TO did not know about.**
The stale-custody-basis defect was confirmed at the served layer. But the successor account the TO
named for the repoint was the WRONG ACCOUNT, and repointing as written would have moved a
client-facing figure by +103% — half of it a silent population swap. Caught before any repoint,
which is exactly what RIDER 1 exists for.

---

## What was found

### 1. The staleness, confirmed at the SERVED layer (not inferred from source)

`opal-data-bd/schwab/silver/rps/` froze at `date=20260723` (634 partitions, unadvanced) and was
**still the live basis** — SSM `/mdpf/custody_source` read `schwab` at 17:0xZ. **25 TRADING days**
behind the frontier (`lib/trading_calendar.py`; the TO's "27" was 08-19 calendar days, re-read per
COO's instruction rather than carried forward).

The damage lands on the RESIDUAL, not the custody base, because
`non_model_aua = partner_custody_total(FROZEN) - model_aua_input(ADVANCING) - sma_aua_input`:

| | 2026-08-05 | 2026-08-26 |
|---|---|---|
| `partner_custody_total` | 1,641,269,345.33 | 1,641,269,345.33 (**+0.00, bit-identical 18/18 partitions**) |
| `model_aua_input` | 1,440,437,783.16 | 1,473,258,520.42 (+32,820,737.26) |
| `non_model_aua` (**served, client-facing**) | 177,958,391.99 | **145,028,157.87** |

Served figure understated **+91,476,329.17 = +63.07%**, drifting **-1,937,073/day**, ~49 days from
the `SCHWAB_NON_MODEL_SANE` (50M,500M) fail-closed floor — and already below the design's own stated
observed range (~180M-203M) with no alarm.

**DISCRIMINATION:** the served 08-26 row reproduces TO THE CENT from the July-23 partition
(`1,641,269,345.33 - 1,473,258,520.42 - 22,982,667.04 = 145,028,157.87`). That identity closes on no
other basis, so the staleness is measured at the APPLIED/served layer rather than inferred.

### 2. THE TO NAMED THE WRONG SUCCESSOR ACCOUNT

TO face and GO both named `opal-data-assets/schwab/08335338/silver/fact_rps/`. Measurement says
`08242234`. Held-constant-vintage control at `date=2026-07-23`:

| | value vs legacy | accounts | legacy-only | successor-only |
|---|---|---|---|---|
| **08242234** "49 WEALTH MANAGEMENT LLC" | **identical to the cent** | 6,005 vs 6,005 | **0** | **0** |
| 08335338 "49 FINANCIAL" | +55,083,179.72 (+3.36%) | 6,005 vs 6,031 | 12 | 38 |

Hardened to **10 vintages** across 2024-07-08..2026-07-23 (sample 10 of 514 common, every 57th):
**08242234 exact 10/10; 08335338 exact 0/10**, its divergence GROWING ~3.0M -> ~55.1M across a book
that tripled. That growth signature is what distinguishes a different book from a reconciliation gap.

Repointing as written would have moved `non_model_aua` **+149,588,666.74 (+103.14%)**, of which
~58.1M is population, not freshness. Issuer DISOWNED the name as a name-is-not-identity defect
(76210) and confirmed `08242234`.

### 3. The repoint is a CODE change, not a path swap

Successor is a different table family: 57 columns vs 11, carries neither `market_value` nor `ticker`
(they are `market_value_settled_unsettled` / `ticker_symbol`), and partitions as `date=YYYY-MM-DD`
against the legacy `date=YYYYMMDD`.

---

## What was delivered

| Act | Commit | Push state (ls-remote read 17:5xZ) |
|---|---|---|
| RPS-1 materiality print (sections 1-7) | `a53fcf6459` | ON ORIGIN |
| FINDING B hardened to 10 vintages (section 8) | `5c3ed23e92` | ON ORIGIN |
| RPS-3 repoint + deploy ledger opened | `d5fd2e4c79` | ON ORIGIN |
| Closure: proof instance, TO complete, ledger closed | `89bf9cff4f` | **LOCAL** — push is integrator-only on CLOUD |

**Deployed:** `data/mdpf/scripts/gold/build_mdpf_wse_49f_non_model_aua.py` ->
`s3://opal-data-mdpf/code/scripts/gold/build_mdpf_wse_49f_non_model_aua.py`, ETag
`"c15ba5d5e1557b35fb333a85bb0e3bbc"`, LastModified 2026-08-27T17:14:00Z, 44,431 B.

---

## Deployment Sequence + Verification (DS role addition — ACTUAL output)

```
safe-deploy attempt 1  -> TRUE rc=3  HALT-GATE: IDENTITY UNRESOLVED -- BLOCKED (fail-closed)
   Resolved by writing org/mcp/sessions/1ca28d63-...-c9a74a6b466b.serial (the sanctioned
   identity source, org/XXX.md Step 1). NOT overridden -- an override means deploying while
   blind to my own STOP messages.
safe-deploy attempt 2  -> TRUE rc=0
   DEPLOYED  [mdpf] data/mdpf/scripts/gold/build_mdpf_wse_49f_non_model_aua.py
   VERIFY OK  comp-pipescript deployed ...
   OK: safe-deploy gate PASS -- all files deployed and verified
```

**APPLIED-layer verification, deliberately a DIFFERENT instrument than the gate's `comp-pipescript`**
(boto3 byte read, not the rail's own digest path):

```
deployed sha256 (LF-normalised) : b6c8a6acf95f1a64600d722c5abbb76ce0ac08896fccb10c183ea02c0c51c6af
local    sha256 (LF-normalised) : b6c8a6acf95f1a64600d722c5abbb76ce0ac08896fccb10c183ea02c0c51c6af
IDENTITY: MATCH   (normalisation stated: CRLF->LF both sides)
POSITIVE probes  7/7 PRESENT   (RPS_MASTER_ACCOUNT="08242234", fact_rps prefix, ASSETS_BUCKET,
                                both column constants, hyphenated partition regex, new custody_scope)
NEGATIVE controls 3/3 ABSENT   (old prefix constant, BD_BUCKET paginate call, compact date regex)
control-of-the-control: RPS_CASH_TICKERS still present in stripped text -> the strip did not
                        empty the file and manufacture the absences
```

**Behavioural confirmation through the PRODUCTION entry point** (ad-hoc QA run; the scheduled fire
remains the production acceptance):

```
INFO: Schwab-native custody -- RPS partition date=2026-08-26
INFO: reading Schwab RPS custody source s3://opal-data-assets/schwab/08242234/silver/fact_rps/date=2026-08-26/data.parquet
INFO: partner_custody_total (Schwab-native straight-RPS, assets-only) = $1,732,745,674.50 (101079 positions, 6148 accounts)
  schwab coherence gate -> PASS ($236,090,852.06 within $50,000,000..$500,000,000)
OK: WS-E 49F non-model AUA feeder complete date=2026-08-27 rc=0        [TRUE rc=0, unpiped]
```

`1,732,745,674.50` is identical **to the cent** to my independent boto3/pandas harness — a different
instrument reading the same object, not a re-run of the same method.

---

## Deliverables written (DS role addition)

| Artifact | Purpose |
|---|---|
| `deliverables/ADVI_49F.RPS-CUSTODY_RIDER1_MATERIALITY_PRINT.md` | The RPS-1/1b/1c print; 8 sections, denominators beside every number, instrument traps banked inline |
| `deliverables/ADVI_49F.RPS-CUSTODY_PROOF_OF_SPEC.json` | Proof instance, 7 acceptance rows, VALID TRUE rc=0 |
| `org/critical_paths/change_management/advi-49f-rps-custody-wse-repoint-20260827.md` | NEVER#6 deploy ledger — opened 17:12Z, CLOSED 17:33Z, 7 legs, plus a "what this ledger does NOT close" section |

---

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `comp-which` | producer lookup; proof-of-spec validator lookup | **MISS, loudly** — "NO CURATED RULE MATCHED", all candidates below the vetted band. Correctly did not pick the top fuzzy guess |
| `comp-find` | `'49f_straight_rps_custody_minus_smartx' --files`; `'partner_custody_total' --files`; `'schwab_native_rps_assets_only'`; `--name 'proof_of_spec'` | **PASS** — resolved WS-E from 2 hits / 27,245 files. The `custody_scope` census (2 hits) is what licensed the RPS-4 field change as schema-safe |
| `comp-pipescript` | `io build_mdpf_wse_49f_non_model_aua.py` (Rule 20 pre-change); `deployed` (inside safe-deploy) | **PARTIAL, self-declared** — could not statically resolve the dynamic `Prefix=`, printed "manual review required" instead of a confident empty. `deployed` returned MATCH (the trustworthy direction) and was not relied on alone |
| `.tools/safe-deploy.sh` | `--author 0.4.0_DS_ClientPlatform <script>` | **PASS rc=0** after a correct rc=3 fail-closed (see Gap 1) |
| `.tools/safe-commit.sh` + commit-gate | 4 commits, `-F` msgfile from a non-shell writer, explicit pathspec | **PASS** — gate clean (py_compile + ds-precommit + ruff py39), risk-reflex CLEAN vs 1,891 danger nodes, msg-verify MATCH each time |
| `.tools/proof-of-spec-check.py` | instance + 7-id expected set | **FAIL then PASS** — pass 1 rc=1 INVALID (3 violations), passes 2 and 3 rc=0 VALID (see Gap 2) |
| `comp-system` | `comp-system` (regen 06_current_state) | **PASS rc=0** — the sanctioned two-phase fix, not an override |
| `lib/trading_calendar.py` | `trading_days_behind`, `is_trading_day` | **PASS** — 25 trading days behind; supplied the 40/40 cadence denominator |

**What worked.** The fixed-vintage control arm. A single legacy-vs-successor delta would have read as
a plausible +103% staleness correction and hidden an account swap inside it; holding the vintage
constant is the only thing that separated population from time, and it cost one extra read.

**What failed.** `.tools/proof-of-spec-check.py` pass 1: TRUE rc=1, 3 violations, **all structural
and all in the wrapper** — `spec_ref/group` outside the schema enum, and both `surprises` entries
authored as objects where strings are required. Every object the instance described had already been
verified with controls; the wrapper reporting them still failed its own gate. Recorded inside the
instance rather than quietly fixed.

**Gaps found.**

1. **`safe-deploy` fail-closed rc=3 IDENTITY UNRESOLVED** — no `org/mcp/sessions/<id>.serial` existed
   for this session, so the gate refused to guess its principal. **This is the gate working**, not a
   defect: guessing from `.comp-graph/.agent_context` is what previously made it scan a stranger's
   inbox and miss a real STOP addressed to itself. Fixed by writing the sanctioned serial file.
   *Worth knowing at seat launch: a fresh base-serial seat has no serial file until something writes
   one, so the first deploy of a session will hit this.*
2. **`git log --since` returned a FALSE ZERO.** `--since='2026-08-27 16:00'` returned **0 rows**
   against a repo demonstrably carrying commits in that window (positive control: all 4 of my hashes
   resolve with today's author dates). The `--since` limb is the broken one, not `--author`. **A
   zero from this filter is not an absence** — I scoped this log's window from hot context and
   commit hashes instead.
3. **`--author` on a base serial cannot attribute work to an instance.**
   `git log --author="0.4.0_DS_ClientPlatform"` returns PEER LANE commits — `21170203c5`
   (ADVI_49F.c02-CFINPUT, the `~U` seat) and `f4836ad706` (ADVI_INSURE, the `~R` seat) — because
   lane sessions commit under the base-serial author line. Provenance on this serial is degenerate:
   the author field cannot tell which instance acted. Cite hashes, never an author-filtered count.

---

## Files Modified

See commit messages: `a53fcf6459`, `5c3ed23e92`, `d5fd2e4c79`, `89bf9cff4f`. Rows needing extra
context:

| File | Note |
|---|---|
| `data/mdpf/scripts/gold/build_mdpf_wse_49f_non_model_aua.py` | 9 edits, each anchor asserted to match EXACTLY once before applying. Constants block now records the 08242234-vs-08335338 distinction at the point of use, and `RPS_PARTITION_RE` carries the hyphenated-format hazard in a comment beside the regex, so the next reader cannot re-make either mistake |
| `infra/system/06_current_state.{md,json}` | Regenerated. Rode the closure commit because my own new proof-of-spec JSON was the uncommitted `_SOURCE` causing the 237->238 fingerprint drift — the two-phase case, taken via the sanctioned regen path (not the rule bank, so regen was legal) |
| TO face `<expected_criteria>` | Widened 5 -> 7 ids to implement COO ruling 76210 s.5, whose prose already said 7 while the machine-readable half still said 5. `3.0.0_SA_CVO` landed the same widening independently @`a29d1611da` (DELTA-CERT PASS) |

---

## MCP traffic

**17 messages handled.** Significant only:

- **IN** `2.0.0_SA_COO` **76140** GO — begin at RIDER 1, print before any repoint.
- **OUT** -> COO 16:54Z — RPS-1 printed + caveat decision; **blocking question raised**: the named
  successor is the wrong account.
- **OUT** -> COO 17:00Z — FINDING B hardened to 10 vintages (crossed COO's ruling by 3 seconds).
- **IN** `2.0.0_SA_COO` **76210 / 76212** RULING — target CONFIRMED `08242234`, `08335338` DISOWNED as
  an issuer defect; caveat text ACCEPTED; Finding C approved as a code change; RPS-3/4/5 proceed.
- **OUT** -> `3.0.0_SA_CVO` cc COO **76196** — surprise channel, OBSERVATION/INERT.
- **IN** `3.0.0_SA_CVO` **76203** — ACCEPTED AS FILED; recorded at
  `org/surprise_channel/ADVI_49F/INVESTIGATION_v1.md` @`674b147e71`, pattern banked verbatim.
- **OUT** -> COO 17:50Z — repoint-deployed-verified + ledger path.
- **IN** `2.0.0_SA_COO` **76273** — **RAVC-4 ACCEPTED COMPLETE.** COO corrected the face's delta
  attribution themselves @`dab6eda3b3`, naming the swap as theirs.
- **IN** `0.0.0_AB_MSTR` 76154/76175 — merge window OPEN then CLOSE; I held commits until CLOSE.

Surprise channel filed: **1** (OBSERVATION/INERT) — *a band on a derived value cannot discriminate a
frozen input from a moving one*; the discriminating check is an input-advance STATE check on the
partition date, one comparison, not a magnitude check on the output. Banked by CVO verbatim; no
remediation built (moratorium).

---

## Blockers

**None.** One item is out-of-lane rather than blocked: closure commit `89bf9cff4f` is LOCAL and
**push is integrator-only on CLOUD** — it moves in the integrator's window, no act pending at this
seat. Push state measured by `ls-remote` (origin/CLOUD `4fd9b69a75`), not assumed.

---

## Current State

**Nothing owed, nothing held, nothing in flight.** Broker summary set to `IDLE: available`.

`ADVI_49F.RPS-CUSTODY` is **COMPLETE and ACCEPTED** (COO RAVC-4, 76273). The TO face reads
`complete 2026-08-27T17:33Z`; the deploy ledger is CLOSED; the proof instance is VALID.

**The live serving state as of this log:** WS-E now reads
`s3://opal-data-assets/schwab/08242234/silver/fact_rps/date=YYYY-MM-DD/data.parquet` via
`ASSETS_BUCKET` + `RPS_SILVER_PREFIX` (`build_mdpf_wse_49f_non_model_aua.py:175-188`), mapping
`market_value_settled_unsettled` -> the internal `market_value` and reading `ticker_symbol` for the
cash exclusion. `_latest_rps_partition()` (`:305-320`) matches `RPS_PARTITION_RE`
(`date=(\d{4}-\d{2}-\d{2})/`). The emitted row's `custody_scope` is now
`schwab_native_rps_assets_only_08242234_fact_rps` and the custody dict carries `custody_source_uri`.
**The next scheduled WS-E fire (~12:54Z daily) is the production acceptance and will be the first
served row on the corrected basis** — expected `partner_custody_total` ~1.73B against yesterday's
frozen 1,641,269,345.33, i.e. the served `non_model_aua` jumps ~+91M. That jump is EXPECTED and is
the correction, not a regression.

**Two things this TO deliberately did NOT close:**

1. **23 served partitions (2026-07-24..2026-08-26) still carry the July-23 basis.** No backfill was
   authorized; the accepted caveat is the treatment. COO surfaced the understatement to Andrew and
   dispositioned re-emission of that window as a product call, his to make.
2. **The false Rule-25 dormancy marker** on `opal-data-bd/schwab/silver/rps/` — COO-owned, untouched
   by me. **It is more dangerous now than before this deploy:** with WS-E no longer reading that
   prefix, its "no live reader after 2026-08-18" claim becomes TRUE-BY-ACCIDENT, while the blind
   reader census that produced it stays uncorrected. Instance resolved, instrument not. COO has
   queued it for round close with the marker to get a provenance annotation when the census re-runs
   with the WS-E miss as the fixture.

**Unmeasured, stated as a limit rather than assumed away:** whether any downstream consumer (portal,
WS-A aggregation) re-derives or caches `non_model_aua` independently of the WS-E feeder. The RPS-2
caveat's scope is asserted over the feeder partitions I read, not over every surface that quotes the
figure.

---

## Next Steps

1. **[`2.0.0_SA_COO`]** Round-close: the Rule-25 marker-census instrument fix (blind reader census
   re-run with the WS-E miss as FIXTURE) and the marker's provenance annotation. Correcting the one
   marker fixes the instance and leaves the instrument.
2. **[Andrew, via `2.0.0_SA_COO`]** Product call on whether to re-emit the 23 July-23-basis served
   partitions. Not authorized by this TO.
3. **[`3.0.0_SA_CVO`]** Acceptance read at CVO cadence — the TO reads complete with the proof
   instance VALID rc=0 against the 7-id set the delta-cert @`a29d1611da` expects.
4. **[`3.0.0_SA_CVO`]** At round close, the banked control-shape item: an input-advance STATE check
   beside any derived-value band on this chain, remedy-holder named at the cut.
5. **[integrator / `0.0.0_AB_MSTR`]** Closure commit `89bf9cff4f` pushes in the next integrator
   window. No act pending at this seat.
6. **[`0.4.0_DS_ClientPlatform`, this seat]** IDLE and available. One project per instance — no
   second assignment lands here without a fresh allocation word, and allocation words are Andrew's
   under the standing freeze.
