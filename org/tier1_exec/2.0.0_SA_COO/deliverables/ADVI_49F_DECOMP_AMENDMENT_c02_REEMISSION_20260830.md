# ADVI_49F — DECOMP AMENDMENT 2: the c02 gross-leg RE-EMISSION (cells `C02-g-2`, `C02-g-3`)

**Issuer:** `2.0.0_SA_COO` · **Written** 2026-08-30 ~01:3xZ · **Project** `ADVI_49F` (directive D2) · **Predecessor cell** `C02-g-1` (`ADVI_49F_DECOMP_AMENDMENT_c02_GROSSLEG_20260829.md`), whose §4 CARRIED this decision and expressly did not scope it.
**Authority:** the D2 & D3 drive-pair verdict ledger ROW 16 (`org/tier1_exec/1.0.0_SA_CTO/drive_pairs/D2-D3/VERDICTS.jsonl`, ts 2026-08-30T01:25:02Z, tick 69) — `3.0.0_SA_CVO` 84078/84079 **APPROVED** as narrowed; never-widen sign-off COMPLETE (COO 84019, CTO 84038); serve-gate limb RULED (CTO 84038); disposition (a) rollback CLOSED by Andrew's word, LD-0477 AMENDMENT 2 item 1, VERBATIM *"id rather we just keep pushing forward, i dont want to rollback anything lets just push on"* (0.0.0_AB_MSTR 84032). **This document quotes the ruling; it does not re-rule it.**

This is an **ISSUER AMENDMENT** adding **TWO** cells in dependency order. `C02-g-1` stays as determined (outcome (a) CODE WRONG, G-1..G-5 closed @`cee023004c`, fix @`946b5c5a3c` on the DEPLOYED plane at `s3://opal-data-49financial/_code/c02_twr_engine.py` ETag `2f709fc66ed6cb2e9a853704ef0e83c6`).

---

## 1. THE STATE THIS AMENDMENT EXISTS FOR

```
  DEPLOYED  c02_twr_engine.py @946b5c5a3c  -- corrected sign: r_gross - r_net == +|fee|/bmv on fee days
  STORED    twr_daily, 534 partitions      -- INVERTED sign on every fee day (DS~N G-4: 205/205 NEGATIVE
                                              across 15 partitions spanning 2024-07-08..2026-08-28)
  MARKER    none. schema_version "1.0" on both vintages; the manifest carries no gross-leg vintage.
```
The next c02 emission writes ONE corrected partition beside 534 inverted ones under one label. A consumer linking across the changeover multiplies opposite conventions. **Ruled remedy: re-emit the FULL stored range + forward under ONE convention, with a field a consumer can reject on.**

**TIME-SHAPE (measured, comp-trigger 49f, 140 rules + 18 schedules):** `bd-49f-runner-daily` cron(0 2) **DISABLED**; `bd-49f-fees-session-daily` cron(20 22 MON-FRI) ENABLED; `bd-49f-insurance-session-daily` cron(35 4 daily) ENABLED. **Which chain dispatches c02 today is UNREAD** (84019 item 2 ask to `0.4.0_DS_ClientPlatform~N` / `0.7.0_AE_CloudOps~K`); MON 08-31 22:20Z is INFERRED. Per CVO: if the re-emission cannot land before the MEASURED fire, the fallback HOLD goes on the c02 DISPATCH specifically, never on the whole fees session.

---

## 2. THE CELLS

### `C02-g-2` — THE VINTAGE FIELD: make the re-emitted column carry its claim (DS, engine)

**DECLARED DOMAIN:** what `c02_twr_engine.py` WRITES per partition and per manifest for `canonical/twr_daily` — the columns of `part` and the keys of `manifest` at the emit site (`c02_twr_engine.py:438-452` @`946b5c5a3c`; `SCHEMA_VERSION = "1.0"` at `:40`). **Outside the domain:** the return arithmetic (`:198-207`, ruled and fixed under `C02-g-1`), `cf_net`/`r_net`, row selection (`c02-CFINPUT`), every other runner, and the RE-RUN itself (`C02-g-3`).

**OWNER:** DS lane (Rule 13). Seat: `0.4.0_DS_ClientPlatform~N` — continuity on the same file, same project (Rule 27), the seat that determined and fixed `C02-g-1`.

**SEVERITY:** BUILD-ONLY. Commit is consent to the window's deploy leg (the `~C` rule: *for a deploy-gated tree with no shared home, COMMIT IS CONSENT*) — and here the deploy is WANTED: `C02-g-3` re-runs against the deployed engine. Serve stays behind arm-(a) + the CTO serve-gate limb.

**THE RULE-24 CAUTION, VERBATIM FROM CVO 84079 AND BINDING:** *"the vintage is its OWN field (e.g. gross_leg_vintage = the fix commit), and schema_version moves BESIDE it — schema_version alone was already caught spanning two column counts under one value; do not make it carry a second meaning."*

#### Acceptance criteria
- **V-1 THE FIELD — a CONVENTION vintage, not an engine-HEAD vintage (CVO grading note 84130, adopted into the cell before the build).** `twr_daily` partitions carry a new column `gross_leg_vintage` (string) whose value is the commit-ish that DEFINED the `r_gross` convention now in force — the fix commit `946b5c5a3c` today — from a declared constant in the module whose comment states the rule: **it moves ONLY when the `r_gross` convention changes (a P3-class, CTO-gated act), never on an unrelated engine commit** (Rule 24 (iii): one field, one intent — "which convention", not "which build"; an engine-HEAD semantics would make a reject-on-mismatch consumer refuse to link across boundaries where nothing about `r_gross` changed). **Never derived from `git` at runtime on the host, which has no repo.** The manifest carries the same key with the same value. Populated on EVERY row the engine emits, including `status != OK` rows (an absent vintage on a null row is a second silent convention). The V-4 arm asserts the constant RESOLVES (`git cat-file -e <value>` in the repo at test time) so a typo cannot ship as a vintage.
- **V-2 SCHEMA BESIDE IT.** `SCHEMA_VERSION` moves off `"1.0"` (to `"1.1"`) in the SAME commit, and the `POLICY_BLOCK` check at `:132` is NOT the same object and is NOT touched — the policy block's own `schema_version` "1.0" is a different schema. State that in the commit message.
- **V-3 CONSUMER CENSUS BEFORE THE BUMP.** Census every reader of `twr_daily`'s `schema_version` and of `r_gross` across `data/assets/scripts/gold/runners_49f/`, `data/assets/scripts/gold/runners_49f/tests/`, the arms tree (`org/**/arms/`), and `parity_period_returns.py` — `comp-find`, denominator printed, `-i`. **A consumer that REFUSES on `schema_version != "1.0"` moves in the same commit or the bump breaks it silently** (a value arm). A consumer that reads `r_gross` from a DOWNSTREAM table (c03 lineage, nna, PERFRP b-series leaves) is NAMED to the issuer as a follow-on re-emission candidate, **not re-emitted under this cell**.
- **V-4 EXERCISED, COMMITTED.** The engine's test module carries an arm that asserts `gross_leg_vintage` present + non-empty on every emitted row and equal to the manifest's, and that `schema_version == "1.1"` on the part and the manifest; the arm's invocation and output are in the proof-of-spec instance, **as a committed artifact** (the `~V` lesson: an ad-hoc arm that did not survive the reboot is a sentence, not evidence). One ad-hoc QA emission to `--local-out` on a real partition date shows the column; the emitted local file is the evidence, its path in the instance.
- **V-5 NOTHING ELSE MOVED.** Diff census: changed lines confined to the emit block, the constant, the test module, and any V-3 consumer moved; `:198-207` and `:286-292` UNTOUCHED, shown by the diff.

**Owed back:** one message to `2.0.0_SA_COO` + `0.7.0_AE_CloudOps~L` at commit, naming the commit-ish, the vintage value the field will carry, and the V-3 census result — **that message is `C02-g-3`'s start condition.**

### `C02-g-3` — THE RE-EMISSION: 534 partitions + forward under ONE convention (AE, campaign)

**DECLARED DOMAIN:** the stored `canonical/twr_daily` partitions in `opal-data-49financial/gold/advi/` for every date the P14-VEHICLE campaign emitted (534, ledger pin `9dd522c50d`) plus any date emitted since, re-written by the engine at the `C02-g-2` vintage. **Outside the domain:** every OTHER canonical table (`valuation`, `flow_ledger`, `nna_canonical`, `dim_*`) — **their partitions must be byte-identical before and after**; the serve/publish plane; the nightly's own emissions (which will carry the new vintage by themselves once the engine is deployed).

**OWNER:** AE lane (Rule 13: the re-run is a campaign act; DS owns the engine). Seat: `0.7.0_AE_CloudOps~L` — the seat that ran the 534-date P14-VEHICLE campaign, holds the SSM `--date` vehicle mechanics (`ADVI_49F.P14-VEHICLE` `complete`), and knows the nightly-mutex trap.

**START CONDITION:** `C02-g-2`'s commit-message from `0.4.0_DS_ClientPlatform~N` AND the engine at that vintage READ on the deployed plane (`_code/c02_twr_engine.py` ETag == local md5 at the named commit — read it, never inherit the window report). **Until both: MEASURE and PLAN only** (R-1), no emission.

**SEVERITY:** BUILD-ONLY. Serve unchanged. No re-grade of G-1..G-5; CVO grades this as a GRADED ROUND.

#### Acceptance criteria — the bar is CVO 84079's, verbatim where quoted
- **R-1 VEHICLE, MEASURED FIRST.** Read at source how a single-stage c02 re-emission runs for one historical date: the P14 finding was *"no stage-scoping"* on `chain_49f_entrypoint.py` (@`f62e93b9bb`), so the candidates are (i) a stage-scoped invocation of the entrypoint if one exists at HEAD, (ii) `c02_twr_engine.py --date D --upload` directly with `--canonical-local`/`--calendar-local` pointed at the host mirror, (iii) a full-chain `--date D --upload` — **(iii) is PROHIBITED** because it re-writes tables outside the domain. If neither (i) nor (ii) can run on the host as-is, the missing stage-scoping is a BUILD act: name it to the issuer with the minimum change; do not improvise on the host. Measure date-1 wall time; project the campaign span; state it.
- **R-2 THE NIGHTLY MUTEX + THE FIRE DISCRIMINATOR.** Before the first emission: which chain dispatches c02 and when (the 84019 item-2 read, if not already landed) — measured on the LIVE trigger plane, not the .tf. No campaign date starts inside [per-date wall time + margin] before that fire; the campaign never coexists with a production run (P14 V14-4c(d) verbatim applies). If the campaign cannot finish before the measured fire, the seat REPORTS and the issuer places the HOLD on the c02 DISPATCH (CVO's fallback) — the seat does not disable a rule itself.
- **R-3 (CVO bar a) `r_net` VALUE-IDENTICAL** to the current partitions on **534 of 534** — read old vs new per partition (versioned bucket: prior VersionId is the "before"), max |Δr_net| printed = 0.000e+00 over the matched OK account-days, denominator = partitions AND account-days.
- **R-4 (CVO bar b) `r_gross > r_net` on EVERY fee day, 534 of 534 partitions**, SIGNED gap `r_gross - r_net` published (never `abs()`), with the non-fee-day EQUALITY as the negative control, denominators printed as partitions AND account-days.
- **R-5 (CVO bar c) THE VINTAGE FIELD PRESENT on 534 of 534 partitions + each manifest**, value == the `C02-g-2` vintage; `schema_version == "1.1"` on all; **zero partitions left at "1.0"** (a partial range reproduces the mixed-vintage column).
- **R-6 OUT-OF-DOMAIN TABLES UNMOVED.** For every OTHER canonical table, the listing before vs after (key + ETag/VersionId) is identical: 0 new versions. Printed with its denominator.
- **R-7 (CVO bar d) BUILD-ONLY.** No serve, no publisher, no platinum key. Reporting cadence: date-1 measured, then per 100, then completion — completion reported from the campaign ledger, never the projection.

**Owed back:** the proof-of-spec instance + the campaign ledger to `2.0.0_SA_COO` and `3.0.0_SA_CVO` (grader). Nothing to `4.0.0_SA_CRO`.

### `C02-g-4` — THE HOLD: silence the c02 dispatcher until the column carries one convention (AE base, infra) — ADDED 01:4xZ on the measured time-shape

**WHY THIS CELL EXISTS (the §1 time-shape was WRONG and was corrected by measurement, DS~N 84104):** 2026-08-30 is SUNDAY; c02's ONLY executor is `chain_49f_entrypoint.py:181-186`, dispatched by EventBridge SCHEDULER schedule **`advi-49f-gold-floor`** (State ENABLED, `cron(45 12 * * ? *)` UTC, every day incl. weekends; APPLIED == DECLARED at `infra/aws/terraform/opal-assets/advi_49f_floor.tf:279-291`) → `advi-49f-gold-dispatch` → SSM `advi-49f-chain-dispatch` → `i-01003b035d2988dfb` `--production`. `--production` derives D = prev_trading_day(now): **SUN 08-30 → D=2026-08-28 (EXISTS), MON 08-31 → D=2026-08-28 AGAIN, TUE 09-01 → D=2026-08-31, the first NEW date.** `runner_common.py:123-125` puts unconditionally, so today's 12:45Z fire would OVERWRITE the served `date=2026-08-28` partition in place (r_gross flips, r_net unchanged, no vintage) while 533 keep the inverted convention. The bd-49f-*-session-daily rules do NOT reach c02. comp-trigger v1's name-match did not surface the schedule — this issuer's instrument miss.

**DECLARED DOMAIN:** the `State` of the ONE schedule `advi-49f-gold-floor`, declared in TF and landed by `safe-apply`. **Outside the domain:** every other rule/schedule (no session-daily hold — CVO's exclusion); the entrypoint's code (a c02-only skip would be a production edit under an 11h clock — wider, not narrower, CTO 84164); the accelerator (`C02-g-4` names its coupling, it does not move it).

**OWNER:** `0.7.0_AE_CloudOps` (base), Rule 13 infra. **NEVER-WIDEN SIGN-OFF COMPLETE:** COO half 84135, CTO half 84164. **This is CVO 84079's own fallback** ("the HOLD goes on the c02 DISPATCH specifically") applied to the finest knob that exists. It does not contradict Andrew's LD-0477 A2 word: SUN + MON fires re-derive an existing date, so the hold costs ZERO new data through Monday.

#### Acceptance criteria
- **H-1 READ BEFORE HOLD (moots the rest if broken).** The DEPLOYED bytes of `advi-49f-gold-dispatch` and the SSM document's APPLIED state (DS~N residual (a)): a broken dispatcher makes today's fire a no-op. And residual (c): no surviving campaign leg on `i-01003b035d2988dfb` able to run the chain off-schedule (that host is AE's). State both either way.
- **H-2 THE HOLD, TF-DECLARED, -TARGETED.** `advi_49f_floor.tf:279-291` State → DISABLED; plan cut on the `.tools/terraform.exe` 1.9.8 shim; **`safe-apply -target aws_scheduler_schedule.advi_49f_gold_floor`** (the untargeted plan carries the held 08-11 emitter repoint + IAM adds AND the P2F-3b accelerator rows — the exercised precedent 76182/76186 is to target; landing any of them on this authorisation is the c02 "commit is consent" shape again). Applied BEFORE 12:40Z 2026-08-30. Read back with `scheduler get-schedule` State == DISABLED, never tf output.
- **H-3 LEDGERED.** `org/critical_paths/change_management/` entry opened at the apply, carrying: the lift condition, the lift-by, and the NAMED COUPLING that the P2F-3b accelerator (target `advi-49f-gold-dispatch`, a second path into c02) is sequenced AFTER this hold lifts (CTO 84164 (2)); closed at the lift with the State read-back.
- **H-4 THE LIFT CONDITION, ON THIS FACE.** Lift = `C02-g-3` R-5 READ (vintage on 534 of 534, zero at "1.0"), **or the hard lift-by TUE 2026-09-01 12:45Z minus one chain runtime (~12:40Z)**, whichever first. **If the re-emission has not landed by the lift-by, the hold is LIFTED ANYWAY** and the mixed column becomes a repair rather than a prevented state — a missed production date is the larger cost. The lift is the same act in reverse (TF State ENABLED, targeted safe-apply, read-back), by the same seat, on the issuer's word or the lift-by clock, whichever first.

**Owed back:** H-1 first (read-only, can moot the rest); the apply read-back (that message consumes ledger row 17); the lift read-back.

---

### `C02-g-5` — THE NEGATIVE-BMV GUARD: the engine REFUSES a return over a negative base (DS~N, engine) — ADDED 2026-08-30 03:4xZ on the surprise item DS~N 85147, ruled 1.0.0_SA_CTO 85171, channel-filed 3.0.0_SA_CVO 85167 row 31

**The state:** `c02_twr_engine.py:47` says VALUE (`NEAR_ZERO_BMV = 1.00  # a denominator below this is UNCOMPUTABLE`); `:224` tests MAGNITUDE (`abs(float(bmv)) < NEAR_ZERO_BMV`); no negative-BMV branch exists in the file (DS~N swept; CTO confirmed @535c9883b2). So a BMV of −4.62 passes the guard, the engine divides by it and emits **status OK with r_net −3.190476 on an account that went from −$4.62 to +$10.12** (date=2026-07-15, 0096172795). Scale (AE~L 85113): **1,089 of 2,593,321 OK account-days (0.042%) across the 535 partitions**; the 15 R-4 negative-gap rows are the fee-day subset. The leg is **r_net, the SERVED one** — PRF-inv-6 clause 1 HOLDS-BY-FACT is qualified on those rows (CVO annotates).

**The convention, RULED by the gate (1.0.0_SA_CTO 85171 — a P3-3 change to the engine's emission contract, stated as such):** a TWR over a negative base is UNDEFINED; the engine REFUSES it with its OWN status. Rule 24 record for the status enum over the BMV domain: `bmv >= NEAR_ZERO_BMV` → computable; `−NEAR_ZERO_BMV < bmv < NEAR_ZERO_BMV` → `UNCOMPUTABLE-ZERO-BMV` (existing); `bmv <= −NEAR_ZERO_BMV` → **`UNCOMPUTABLE-NEGATIVE-BMV`** (NEW sibling: same grain, one intent "why no value", does not move with the ZERO-BMV remedy). Both refusal rows carry `None` on r_gross AND r_net (the engine's own rule at `:474`).

**Owner:** `0.4.0_DS_ClientPlatform~N` (engine, Rule 13) — **stays on ADVI_49F for this cell; the R-WATCH / INF-ONEWRITER activation of 84981 is therefore RE-ROUTED to the next freed DS lane** (issuer's act, same commit).

#### Acceptance criteria
- **N-1 THE CENSUS FIRST (pre-registered at 85161; the fix's blast radius IS this denominator):** over all 535 partitions at the campaign-completion vintage (03:22:43Z), enumerate every account-day with `bmv < 0`: status distribution (OK-with-served-r_net vs already refused for another reason), `emv` sign (sign-inverted cases = emv > 0), magnitude distribution of bmv, per-partition and per-account counts, and the fee-day subset — printed with the 2,593,321 OK denominator and the 1,089 reconciled to AE~L's figure (agree or explain). **The affected-PARTITION list (with counts) is the first deliverable and is C02-g-6's input.** Whether fees charged on a negative valuation is itself a DATA finding is surfaced as its own line to the channel, not folded in.
- **N-2 THE GUARD:** `:224` tests the VALUE, not the magnitude; the new status `UNCOMPUTABLE-NEGATIVE-BMV` lands with its four-postulate record beside the existing enum; refusal rows carry `None` on both legs and the `gross_leg_vintage` + `schema_version` stamps as every emitted row does (V-1's rule). Docstring + the `:47` comment agree with the code. No other branch of the engine moves.
- **N-3 ARMS THAT CAN FAIL:** `test_c02_twr_engine.py` gains (a) a negative-BMV fixture that REACHES the new branch on REAL bytes (a fixture that cannot represent the failure cannot score it — exercise on one real partition's rows, not a dict literal alone), (b) a polarity arm: an account with `bmv < 0` and `emv > 0` returns REFUSED, never a negative return; (c) the existing zero-BMV and OK arms unchanged and green; mutation: revert `:224` to `abs()` → (a) and (b) FAIL.
- **N-4 NEGATIVE CONTROL ON THE FIX, pre-registered:** an ad-hoc `--local-out` emission of one populated partition before/after — every row with `bmv >= 1` is BYTE-IDENTICAL on r_net, r_gross, status, vintage; the ONLY changed rows are the `bmv <= −1` rows (OK → UNCOMPUTABLE-NEGATIVE-BMV, both legs None); rows in `(−1, 1)` unchanged (ZERO-BMV as before). Denominators printed.
- **N-5 DEPLOY on the DS lane's own path (Rule 13: commit → QA-deploy of `data/*/scripts/gold/*.py`), committed via safe-commit with the vintage constant bumped to the fix commit (V-1's convention-vintage semantics: a new engine convention = a new vintage), proof-of-spec VALID rc=0 positional N-1..N-5.
- **Never-widen:** N-2/N-5 change SERVED r_net on the affected rows (a wrong number → a refusal); sign-off = CTO+COO, given by the CTO's ruling 85171 (condition (iii) added to the serve-gate: no serve while any OK row carries `bmv < 0`) + this amendment. Serve stays behind arm-(a) regardless.

### `C02-g-6` — THE SCOPED RE-EMISSION: the affected partitions re-emitted under the fixed engine on the P14 vehicle (AE~L, campaign) — ADDED with C02-g-5

**Input:** C02-g-5's N-1 affected-partition list (never "all 535" by default — the CTO's ruling: a full re-run is NOT required if the partition set is measured) and the deployed N-5 engine (read on the running artifact, the 84470 lesson). **Vehicle:** the mirror-pull driver `e1141a5905` / runner `c73c047862`, scoped by the list. **Plan names the READERS this time** (85065's read-hazard line): the window is announced to every concurrent consumer of `canonical/twr_daily` (DS~C's BP1-2 table is built on the 03:22:43Z vintage and is NOT rebuilt for this — its input stamp says which vintage it read) before the first write.

#### Acceptance criteria — the CTO's pre-registered bar (85171), verbatim in substance
- **Q-1** after the round, OK rows with `bmv < 0` = **0 of N** (N = account-days over the affected partitions, printed); the refused rows carry `UNCOMPUTABLE-NEGATIVE-BMV` with `None` on both legs.
- **Q-2 NEGATIVE CONTROL:** r_gross / r_net / status on every `bmv >= 1` row BYTE-IDENTICAL to the pre-round version (per partition, against its prior VersionId by time — the `f862baac5a` instrument); vintage on every row = the N-5 fix commit (a NEW vintage value; zero rows left at 946b5c5a3c on the affected partitions; UNaffected partitions untouched — R-6-shaped listing: 0 new versions outside the list).
- **Q-3** mutex re-read before every batch; per-date oracle as C02-g-3; ledger via the tool; L-legs closed; proof-of-spec VALID positional Q-1..Q-3. Graded by `3.0.0_SA_CVO` as a round.

---

## 3. RULE 24 — the four-postulate record

- **(i) MECE over a DECLARED domain.** Two cells, two domains: what the engine WRITES (g-2) vs what is STORED (g-3). The uncovered-member hunt: *downstream tables carrying r_gross-derived values* (c03 lineage, nna, PERFRP b-series) — deliberately OUT and NAMED: g-2/V-3 censuses them into a follow-on candidate list for the issuer; they are not silently inside g-3's "534 partitions". *The nightly's own future emissions* — OUT; they carry the vintage by themselves once the engine is deployed.
- **(ii) SAME GRAIN.** g-2 at the grain of one runner file's emit block + its test module; g-3 at the grain of stored partitions + manifests. V-3 (a census) and R-1 (a measurement) are stated as preconditions, not as acts on another grain.
- **(iii) INTENT COHERENCE.** One axis: *make the stored gross leg carry ONE convention AND its claim.* The serve question is routed OUT (CTO serve-gate limb); the dispatch-path question is a precondition read, not a decision here.
- **(iv) STATE COHERENCE.** g-2 moves the ENGINE and nothing stored; g-3 moves the STORED column and nothing served. Neither moves `r_net` (R-3 is the negative control that proves it). Neither moves the other canonical tables (R-6). Neither moves the serve plane (R-7). A HOLD on the c02 dispatch (R-2 fallback) is the issuer's act, not either seat's.

---

## 4. PROVENANCE

| claim | source | grain |
|---|---|---|
| range = all 534 + forward; vintage field + schema bump PART of the ruling; bar (a)-(d) | `3.0.0_SA_CVO` 84079 / ledger row 16 | verdict, verbatim quoted |
| never-widen sign-off complete; serve-gate limb | `2.0.0_SA_COO` 84019, `1.0.0_SA_CTO` 84038 | two seats, two messages |
| rollback CLOSED by Andrew's word | LD-0477 AMENDMENT 2 item 1, via `0.0.0_AB_MSTR` 84032 | ledger, verbatim |
| emit site, constant, CLI | `c02_twr_engine.py:40,:365-374,:438-452` @`946b5c5a3c` | read at source this sitting |
| trigger plane | comp-trigger 49f, 01:0xZ | live API, denominator 140+18 |
| no stage-scoping on the entrypoint | `ADVI_49F.P14-VEHICLE` face, @`f62e93b9bb` | the AE seat's own measurement; RE-READ at HEAD under R-1 |
| DS~N's G-4 numbers | 83976 | quoted, not re-derived |

⛔ **DISTRIBUTION RESTRICTION, inherited from the D2 sub-program:** nothing on this subject to `4.0.0_SA_CRO`.
