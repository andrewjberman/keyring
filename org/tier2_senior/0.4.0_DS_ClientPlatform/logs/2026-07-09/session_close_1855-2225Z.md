# Session close: 1855Z-2225Z -- 1Y anchor fix; cot 0-row freeze (self-caused); C_02 refutation; MDPF/ADVI vintage thread

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, COORDINATE

**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-07-09 (~18:55Z - 22:25Z)
**Branch:** CLOUD
**Prior logs this session:** `48943c343` (main), `11f8350b4` (addendum: the QTD outage). This is the close;
it covers the window **after** `11f8350b4` plus the standing handoff.

---

## Current State (written for a reader with zero prior context)

### SHIPPED + DEPLOYED
| Commit | What |
|---|---|
| `2af63847d` | D_00c: all windows anchor on the DATA date; `_emit_window` fail-loud tripwire; publishes `window_bounds` |
| `3ea2bdbf9` | D_04: propagates `window_bounds` to the SERVED artifact (its real publisher rebuilds field-by-field) |
| `0498a79e7` | bd `C_05`: escape + `from __future__` + 2x F541 (file had never passed commit-gate) |
| `05f7c0f8e` | cot `C_05`: escape + 2x F541 -- **independent commit**, defect set DIFFERS from bd's |
| `53074cf4a` | `AUAFIX-L6` TO: (b)/(c) HARD-BLOCKED on a corrupt grounding source |
| `b8ee3a08a` | Brief: the C_02 cert-freeze **refutation** |
| `48943c343` / `11f8350b4` | session log + the already-fired QTD outage |

**1Y fix: value PROVEN, delivery NOT.** Ran the real `build_employee_leaderboard` read-only on real inputs
(`_save_json` is reachable only from `main():1360`, never from `:798` -- CVO source-verified this is a
*structural* no-write, stronger than the `dry_run` flag): **1Y 0/158 divergent**, bounds byte-match canonical,
`entry_count > 0` on all 9 windows, tripwire silent, wall-clock deliberately injected and ignored.
Runner is **pull-at-runtime** (`run-gold-layer.sh:88-90`; `gold_dispatch.sh:526`) -- nothing baked, so the
nightly executes the fix. **CVO re-scoped the withhold to DELIVERY only (`842dd9040`); ratification still
hard-withheld on the served artifact post-nightly.**

**The QTD outage already fired.** Served `platinum/firm/leaderboard.json`, S3 version history:
`QTD entry_count = 0` across **8 consecutive writes / 39.8h continuous** (2026-07-01T01:53Z -> 07-02T16:19Z),
self-recovered 07-02T17:42Z. YTD/MAX/1Y/3Y held 155-156 -- **a full leaderboard with an empty QTD**.
**Exposure bounded to ONE event ever**: `git log -S 'w_start = today - pd.Timedelta'` -> anchor born
`a3b2d2099` **2026-04-06**, five days AFTER the April roll. CVO retracted "unprovable" (`6b58f0f7a`).

### ESCALATED, NOT MINE TO CLOSE
- **cot 0-row snapshot freeze, 18 days, cause = my `a7a4d974c`.** Lineage `SOURCE-CONFIRMED`: served cot AUA
  <- `D_00:287` <- `C_03:175,199-207` <- `B_00` <- `silver/holdings`. Allocations is NOT on the AUA path ->
  **stale, not corrupt** (P0-class holds; CTO re-verified). Collateral, measured: `accounts_dimension`
  `account_type` = **0/828 cot, 0/10,545 bd** (client-facing plane, previously unmeasured);
  `positions_cube` 677 -> 570 accounts (attribution `INFERRED`).
- **C_02 is NOT the freeze root** (`b8ee3a08a`). `:331`'s floor fires; C_02 fails closed. Repointing the
  picker would ship a cert keyed `{07-07}` carrying a 07-08 number -- **an artifact lying about its own
  as-of**. The real defect: **nothing watches for cert ABSENCE**. COO accepted without qualification; CTO
  issued a second `[STOP]`; the alarm is routed to `0.7.0`.
- **MDPF/ADVI vintage thread.** MDPF's WS-C reads an Orion **forward-labelled** spine (`_orion_vendor_asof.py:120-131`,
  SEALED 07-02: a row dated `D` holds `close(D-1)`) **without calling the normalizer** -> one spine-day stale.
  ADVI's `total.aua` = what Orion displays (Andrew's external anchor). **The feeder artifact carries NO custody
  vintage** -- one date field, `as_of_date`, stamped on a measurement it does not have -> the abstain predicate
  is **not computable from the artifact** -> `partner_custody_as_of` is contract **§4 AMENDMENT 2** (ratified),
  a precondition for the guard **and** the census.

## Things I RETRACTED (all mine, all before anyone else found them except where noted)
1. **ET-completion mechanism** -- asserted to CTO + COO from `cot_bronze_ingest.py:79-80`, a **docstring**.
   Falsified by 0.6.0's probe (`holdings(qt1) = 11,754 rows` on an incomplete day while qt4/qt5 = 0, same minute).
   **Discriminator is QUERY TYPE, not day-completeness.**
2. **`fee_earning_aua = 0.00` blamed on the freeze** -- `D_00:619` keys off `fee_rate_history.is_billable`.
   Tested, killed. A dead hypothesis is a result.
3. **Inverted lineage arrow** -- I told CTO `gold_aua <- client_performance <- C_03`. `C_02` **writes**
   `client_performance`; `C_03` consumes it. I paraphrased a manifest into its opposite. The 0/10,545
   measurement never needed the story I attached to it.
4. **Grounded a served-artifact finding in a dead code path** -- `INF_D_00:1004/1027/1035`, in a script that
   **stopped writing `header_metrics.json` on 2026-06-30** (`:1043`). I had *flagged* the tell (artifact shows
   `as_of_by_dim={aua,nna}`; code emits `{aua,perf}`), wrote *"I am not concluding from it,"* **and concluded.**

## Compiler Tools
| Tool | Target | Result | Note |
|---|---|---|---|
| `comp-pipescript io` | `D_00c`, `D_04`, `C_02`, `A_01` | PASS | `io D_00c` is what caught `D_04` as the real publisher -> `window_bounds` reaches served |
| `comp-pipescript io` | `C_03` | **GAP** | silently answered for `[bd-gold]` when asked about **cot**'s `C_03`. A bare script id crosses the firm boundary with no warning -- the one boundary gate+IAM enforce. Routed to CTO |
| `comp-pipescript deployed` | D_00c, D_04, C_05 x2 | PASS | MATCH each; then **independent sha256** repo==S3 (rc=0 is not evidence) |
| `comp-blast` | `build_employee_leaderboard` | PASS | 12 gold nodes + D_04 |
| `comp-grep` | `sync_schwab_onedrive_to_s3`, `orion_normalize_as_of`, `header_metrics` | PASS + **SAVE** | on `\|` in my pattern it **warned that a 0-match may be the query, not the absence.** The only time tonight a *tool* caught an instrument error instead of a person |
| `aws s3api list-object-versions` | `platinum/firm/leaderboard.json` | PASS | the **served-history oracle**. GAP: 15-day lifecycle horizon (`expire-noncurrent-platinum-14d`) -- CTO's proposed `comp-served-history` must PRINT its horizon, never return empty |
| `git log -S` (pickaxe) | `w_start = today - pd.Timedelta` | PASS | the **forensic oracle with no expiry**. Bounded the exposure window from below |
| `commit-gate.sh` / `safe-commit.sh` / `safe-deploy.sh` | 8 commits | PASS | surface-check clean; shared-index lock contention 3x, retried with backoff, **never forced** |

**What worked.** `comp-pipescript io D_00c` -> `D_04`. That one call is why `window_bounds` reaches the served
artifact. And `comp-grep` refusing to let a malformed pattern's 0-match read as absence.

**What failed (mine, both caught by asserting first).** `aws s3 cp "$SPW\\$f.log"` exited **0 having written
nothing** (MSYS path mangling) -- `&& echo "pulled"` printed success. `git log --until=... -1 --format=%H`
returned an **empty SHA**, so `git show ":path"` silently rendered the **index**. **An empty variable
interpolated into a ref is an instrument that answers confidently about nothing.**

**Gap found.** `comp-pipescript io <ID>` needs a firm qualifier or must refuse an ambiguous bare id.

## Blockers (BLOCKED-EXTERNAL, evidence-cited; nothing assumption-blocked)
- **[nightly ~10:30Z]** 1Y **delivery** verify. CVO's SEV1 ratification waits on it. Deferring is legal only
  because an ad-hoc gold run is a NEVER rule.
- **[1.0.0_SA_CTO]** gates: `A_00` predicate (provenance + max-age ABSTAIN + fail-loud); the four
  `has_data(partition)` call sites; `C_02:310` (defense-in-depth, **never** sold as an un-freeze).
- **[0.6.0_AE_PartnerETL]** RPS **valuation-instant** is `UNDETERMINED` -- the co-activation is HELD. My
  `max(RPS ∩ WSB)` intersects **partition names**; nobody established a name means the same instant in both
  feeds. YCharts anchor returned **403 fabric-wide** (while `ycharts_freshness()` returned `{"ok": true}` --
  a pre-flight green while the pull is forbidden). Escalated to Andrew.
- **[`AUAFIX-L6` (b)/(c)]** HARD-BLOCKED: an automated snapshot-zeroed predicate against a 0-row allocations
  table marks the **entire book** zeroed, silently. Ratified by CTO.

## Next Steps
1. **[0.4.0_DS_ClientPlatform -- me]** `[on/after 2026-07-10T02:30Z]` verify **both** 02:00Z runs by **row
   count**; `[on/after 10:30Z]` the 1Y **served** verify -> report to `3.0.0_SA_CVO` + `0.7.0_AE_CloudOps`.
2. **[1.0.0_SA_CTO]** the three open reads I did **not** finish: who actually writes `header_metrics.json`
   (**UNDETERMINED** -- do not assume `D_04` from its docstring); does the portal/`comp-freshness` gate on
   `data_as_of` or `as_of_by_dim.aua` (decides latent vs live); household 227 (`$68,029.12`, `INFERRED`).
3. **[0.4.0_DS_ClientPlatform -- me, post-P0]** RPS converter spec (`0.6.0`'s): land the vendor's own
   `Business Date`; **assert the column EXISTS before asserting its value**; the commit message must carry
   *"this does NOT settle `close(D)` vs `close(D-1)`."* Also: `DRY_RUN` (strip or implement), the off-path
   silver writer, `cot/D_00c:1152-1167`, backfill 06-22..07-09 -- **all after the forward path unfreezes**.
4. **[0.7.0_AE_CloudOps]** cert-**absence** alarm (`cert_age > N`), complementary to `served-value-freeze-check`.
5. **[COO/CTO]** the docstring lint: **five** found tonight -- four false, one **silent**
   (`INF_C_02` never says what `date` denotes, the one fact a fabric-wide guard keys on). Silence passes every
   lint we have.

## The lesson worth keeping
`INF_D_04:4190` falls back to `datetime.date.today()` on an empty NNA frame, and that flows into the served
`data_as_of`. **Wall-clock in a client-facing vintage label** -- the same root class as the leaderboard anchor,
the ingest as-of, and the cert picker. **Seventh instance. Latent. One empty frame away.**

And the method, which claimed all three of us: **six confirmations of a pattern is not a law.** CTO banked the
two-rule shape as a defect signature twenty minutes before it proved to be the correction. 0.6.0 found the
silent-skip pattern, then wrote it into their own remedy. I wrote *"the pattern earned trust by being checked,
then got used as a substitute for checking"* -- and was claimed by it an hour later. **Each of us was caught by
someone else. The escalation chain is the instrument; none of us is.**

**Nothing patched inside the 02:00Z window. `bd-allocation-processor` + the 07-08 partition untouched. Neither
poisoned `DryRun` doc invoked (one rotates a live credential).**
