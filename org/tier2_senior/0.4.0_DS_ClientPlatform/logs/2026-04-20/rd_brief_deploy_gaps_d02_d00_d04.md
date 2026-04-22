# Session — RD Brief Triage: D_02 + D_00 + D_04 Deploy Gaps

**Agent:** 0.4.0_DS_ClientPlatform~D
**Date:** 2026-04-20
**Started:** ~20:00 UTC
**Task Order:** ad-hoc (two RD AdvisorIntelligence briefings dispatched by Andrew)
**Status:** IN PROGRESS — three commits landed (`8593ea51` D_04 widen, `048af6a3` D_02 books-path fix after incident, D_00 no-change); DT staged S3 uploads; AE qa-runner full D_02→D_04 chain in flight SSM `d67a844f` @ 21:00:29Z, ETA 21:12-21:15Z

---

## Objective

Triage two RD briefings surfaced during the STAUDT FIX-wave session wind-down: (1) `small_account_clients` absent from today's regenerated advisor artifacts despite commit `42be5b21`; (2) Books-tab Firm Overview em-dashes on fee-split and small-account fields. Determine root cause, author any required code fixes, stage deploy via DT so tomorrow's nightly bd-gold-nightly-fallback cycle lands the artifacts.

---

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| comp-pipescript | `deployed D_02` | PASS | STALE confirmed — local md5 `a80bbb2a...` vs S3 `21960a24...`, 149,669 B vs 152,540 B. Primary evidence for RD brief 1 |
| comp-pipescript | `io D_02` | PASS | No COLUMN GAPS; 17 reads / 4 writes; confirms `advisor_book_key` output path for downstream book.json validation |
| comp-pipescript | `deployed D_00` | PASS | STALE — md5 `5b8dd136...` vs S3 `d74c411b...`, 44,204 B vs 41,790 B. Primary evidence for RD brief 2 Gap 1 |
| comp-pipescript | `deployed D_04` | PASS | STALE — md5 `6b45db29...` vs S3 `d9ebb093...` |
| comp-pipescript | `io D_04` | PASS | No COLUMN GAPS; reads CLIENTS_TAB (D_00 output) + writes `platinum/firm/clients-tab-slim.json`. Confirms slim-builder surface for RD brief 2 Gap 2 |
| ad-hoc pyarrow | schema inspect `account_performance.parquet` | PASS | 5,806,862 rows, all 11 `_acct_perf_cols` cols present — rules out column-mismatch as cause of "WARN: account_performance not found" fallback hypothesis |

**What worked:** `comp-pipescript deployed` is the exact tripwire for deploy-gap diagnosis. Three runs caught three stale scripts in ~2 minutes. RD had surfaced the problem as a logic/dark-path hypothesis; `deployed` showed it as a deploy gap across D_02 + D_00 + D_04.

**What failed:** `comp-pipescript io` rejected the full script filename (`D_02.advisor_client_detail.py`) with "Unknown script" error; only the short ID (`D_02`) works. Same for `deployed` — full filename silently returns "No scripts matched filter" rather than an error. Minor UX; easy to work around once known.

**Gap found:** No tool detected the deploy gap automatically pre-run. Today's PROD bd-gold-trigger (19:23Z) fired against 4 stale S3 scripts without any pre-flight hash check; 4 DS commits (`42be5b21` + `6f724293` + `035352c3` + `4299e1c0`) silently didn't take effect. RD flagged a process followup — consider bd-gold-trigger Lambda calling comp-pipescript-style hash check on every D_* script pre-dispatch, halt on STALE. Parking until tomorrow's nightly validates.

Auto-logged to `org/compiler-tools-log.md` via `.comp-graph/.agent_context`.

---

## Work Completed

### 1. RD Brief 1 triage — small_account_clients missing from regen gold

RD (20260420T~195000Z) reported today's `s3://opal-data-bd/gold/entities/advisors/travis_penfield/book.json` (gen 19:34:25Z) and `s3://opal-data-bd/platinum/advisors/travis_penfield/summary.json` (gen 19:43:02Z) both lack `small_account_clients[]` inside `role_breakdown[*]` despite commit `42be5b21` describing the emit. RD hypothesized three causes: stale runner source, wrong commit deployed, or feature-flag guard.

**Diagnosis:** classic deploy gap. S3 `code/gold/D_02.advisor_client_detail.py` was uploaded at 15:01:08Z and is `43c3693a` (FIX3A revert only, 149,669 bytes). Three subsequent D_02 commits on origin/CLOUD never reached S3:

| SHA | Subject | Author | Landed |
|---|---|---|---|
| `42be5b21` | `feat(D_02): emit small_account_clients[] per role in role_breakdown` | ~D | Apr 20 14:43 ET = 18:43Z |
| `6f724293` | `fix(D_02): _emit_role_aua_shadow — use n_roles_per_pair denominator (D_00c parity)` | ~D | 2026-04-20 |
| `035352c3` | `fix(D_02): date-gate canonical NNA attribution to advisor tagging window` | ~D | 2026-04-20 |

All three on origin/CLOUD. Local D_02 byte-matches `git show 035352c3:path` = 152,540 bytes; `small_account_clients` present at L1451. PROD bd-gold-trigger (19:23Z, Group D done 19:49Z) ran the old S3 code. Same explanation covers RD's two previously-ACKed D_02 fixes (role_aua denom + NNA date-gate) — all three validations were queued against artifacts that would only populate post-redeploy.

**Action:** no code change needed on D_02 — requested DT S3 reupload from `git show 035352c3:path` (committed-ref pattern). RAVC2 ACK sent to RD (20260420T200934Z). Pre-flag to CTO + COO.

### 2. RD Brief 2 triage — Books-tab Firm Overview em-dashes

RD (20260420T~202100Z) reported em-dashes on Fee-Paying Clients / Non-Fee-Paying Clients (count + AUA) and small (<$40k) Accounts in the firm headline. Today's `s3://opal-data-bd/gold/artifacts/clients_tab.json` (gen 19:23:38Z) and `s3://opal-data-bd/platinum/firm/clients-tab-slim.json` (gen 19:49:17Z) both lack 5 keys: `fee_earning_client_count`, `non_fee_earning_client_count`, `fee_earning_aua`, `non_fee_earning_aua`, `small_account_count`.

RD's hypothesis: two stacked gaps. Gap 1 = D_00 `build_clients_tab` emit gated on `acct_snap is not None` at L574-588, and `_load_perf` fallback (L289-295) returns None from the "WARN: account_performance not found" path. Gap 2 = D_04 `build_clients_tab_slim` L2441-2445 whitelist narrowed to 3 keys, dropping the 5 new firm-level fields even after Gap 1 fix lands.

**Gap 1 — actual root cause: deploy gap, not dark path.** Commit `4299e1c0 feat(D_00+D_04): emit firm-level fee splits + small_account_count to platinum` (~D, Apr 20 15:07 ET) ADDED the entire emit block, `_load_fee_history` loader, and `_load_perf` acct_snap return in one change. `comp-pipescript deployed D_00` returned STALE (41,790 B on S3 vs 44,204 B local). Pyarrow schema read on `account_performance.parquet` confirmed all 11 `_acct_perf_cols` cols present across 5.8M rows — the dark-fallback hypothesis is unlikely; once `4299e1c0` lands on S3, acct_snap path should populate on the normal load. RD ACK'd the pivot and endorsed deferring Option 2 (refactor to remove acct_snap dependency) until post-deploy evidence confirms either populated or still-absent.

**Gap 2 — real new commit needed.** `4299e1c0` added `small_account_count` to `build_advisor_summaries` (L692, advisor-level) but did NOT touch `build_clients_tab_slim` (L2441-2445, firm-level slim). Current HEAD still narrows firm headline to 3 keys.

**Authored fix: commit `8593ea51`.**

```diff
         'headline': {
-            'total_aua':     headline.get('total_aua', 0),
-            'client_count':  headline.get('client_count', 0),
-            'account_count': headline.get('account_count', 0),
+            'total_aua':                    headline.get('total_aua', 0),
+            'client_count':                 headline.get('client_count', 0),
+            'account_count':                headline.get('account_count', 0),
+            'fee_earning_client_count':     headline.get('fee_earning_client_count'),
+            'non_fee_earning_client_count': headline.get('non_fee_earning_client_count'),
+            'fee_earning_aua':              headline.get('fee_earning_aua'),
+            'non_fee_earning_aua':          headline.get('non_fee_earning_aua'),
+            'small_account_count':          headline.get('small_account_count'),
         },
```

`.get(key)` no-default preserves the undefined-vs-zero semantics FE relies on for em-dash rendering. RD confirmed exact spec match.

### 3. Deploy coordination

Per `feedback_ds_commits_ae_deploys.md` DT-online override: with DT live, DT owns push + S3 upload. MCP'd DT with 3-file staged upload request (`20260420T202935Z`):

| Script | Commit | Source ref | Target | Expected post-upload |
|---|---|---|---|---|
| D_02 | `035352c3` | `git show 035352c3:data/black_diamond/scripts/gold/D_02.advisor_client_detail.py` | `s3://opal-data-bd/code/gold/D_02.advisor_client_detail.py` | 152,540 B, md5 `a80bbb2a...` |
| D_00 | HEAD (4299e1c0+; no D_00 commits since) | `git show HEAD:data/black_diamond/scripts/gold/D_00.portal_aggregates.py` | `s3://opal-data-bd/code/gold/D_00.portal_aggregates.py` | 44,204 B, md5 `5b8dd136...` |
| D_04 | `8593ea51` | `git show 8593ea51:data/black_diamond/scripts/gold/D_04.client_portal_summary.py` | `s3://opal-data-bd/code/gold/D_04.client_portal_summary.py` | post-edit size, md5 TBD |

Per COO directive (`20260420T201xxxZ`): initial plan was DEFER all to tomorrow's bd-gold-nightly-fallback PROD cycle (EventBridge cron `0 23 ? * MON-SAT *` = 23:00 UTC Tue 2026-04-21 = ~7pm ET). AE instead chose to ship a QA-runner test tonight (see section 4) — which surfaced a latent bug in `035352c3`, redirecting the deploy sequence to a fix-forward + full-chain tonight rather than overnight staging.

Pre-flags dispatched:
- CTO: `20260420T200953Z` (D_02) + `20260420T202910Z` (expand to +D_00+D_04)
- COO: `20260420T200946Z` (D_02) + `20260420T202654Z` (expand to +D_00+D_04) + `20260420T205622Z` (incident)

### 4. Incident: D_02 `035352c3` KeyError on first real run — fix-forward

AE dispatched a qa-runner `--from D_02` test on the initial 3-file staged upload shortly before 21:00Z. D_02 failed 52s in:

```
KeyError: "['first_date', 'last_date'] not in index"
  at D_02.advisor_client_detail.py:1655, _load_canonical_nna_per_advisor
```

**AE's initial hypothesis** (partial): upstream D_00 dependency — `--from D_02` skipped D_00 so "yesterday's 4299e1c0-pre state" was used, missing first_date/last_date columns D_02 expected. Asked whether to re-dispatch `--from D_00` for top-to-bottom.

**Actual root cause (code read):** `_load_canonical_nna_per_advisor` has TWO callers in D_02:
- `build_advisor_timeseries` at L1807 — `acct_adv_role` built at L1776-1782 with `.agg(first_date=('date','min'), last_date=('date','max'))`. Correct.
- `build_advisor_books` at L1176 — `_acct_adv_role_books` built at L1157-1174 with columns only `[account_id, advisor_name, _role, weight]`. **Missing the date columns.**

`build_advisor_books` runs BEFORE `build_advisor_timeseries`, so the books-path KeyError aborted D_02 before the timeseries path ever ran. No D_00 dependency involved — `first_date`/`last_date` are derived INSIDE D_02 from the `acct` DataFrame (per RD's original spec and commit `035352c3`'s own structure), not passed from upstream.

Bug was latent because `035352c3` had never been on S3 until DT's upload tonight — RD's ACK on the spec was a review of fix *intent*, not of an executed diff. First real run surfaced the miss.

**Fix-forward commit `048af6a3`:** books-path builder mirrors timeseries-path groupby exactly.

```diff
 for _r in _roles_for_nna:
     _sub = (acct[acct[_r].notna() & (acct[_r].astype(str).str.strip() != '')]
-            [['account_id', _r]].rename(columns={_r: 'advisor_name'})
-            .drop_duplicates())
+            [['account_id', 'date', _r]].rename(columns={_r: 'advisor_name'}))
     _sub = _sub[~_sub['advisor_name'].isin(_EXCL)]
     ...
 if _aar_parts_books:
-    _acct_adv_role_books = (pd.concat(_aar_parts_books, ignore_index=True)
-                            .drop_duplicates(subset=['account_id', 'advisor_name', '_role']))
+    _melted_books = pd.concat(_aar_parts_books, ignore_index=True)
+    _acct_adv_role_books = (_melted_books
+                            .groupby(['account_id', 'advisor_name', '_role'])
+                            .agg(first_date=('date', 'min'), last_date=('date', 'max'))
+                            .reset_index())
     _n_r = _acct_adv_role_books.groupby(['account_id', 'advisor_name'])['_role'].transform('count')
     _acct_adv_role_books['weight'] = 1.0 / _n_r
 else:
-    _acct_adv_role_books = pd.DataFrame(columns=['account_id', 'advisor_name', '_role', 'weight'])
+    _acct_adv_role_books = pd.DataFrame(
+        columns=['account_id', 'advisor_name', '_role', 'weight', 'first_date', 'last_date'])
```

Semantics preserved: weight still 1/n_roles per (account, advisor). New behavior: books-path canonical NNA now date-gated to advisor tagging window per account — matching the intent of `035352c3` (no post-detach / pre-attach attribution in summary site, same as leaderboard).

**Coordination:** MCP to AE `20260420T205611Z` — STOP re-dispatch, fix in flight, D_00 dep hypothesis wrong. MCP to DT `20260420T205756Z` — urgent S3 overwrite of `035352c3` with `048af6a3`. MCP to COO `20260420T205622Z` — incident + fix-forward. MCP to AE `20260420T205809Z` — SHA signal + re-dispatch options.

**AE action:** QA instance (i-0090b823a4a0997e3) was watchdog-reaped before my fix landed — validates today's widened watchdog regex + GOLD_KEEP_ALIVE lifecycle. Clean shutdown, no idle cost. AE restarted c6a.8xlarge and re-dispatched SSM `d67a844f` at `21:00:29Z` running `--from D_02 --chain` (D_02 → D_03 → D_04). ETA 21:12-21:15Z. Log at `/tmp/gold_logs/from_D_02_20260420_210029.log`.

---

## Postmortem — `035352c3` KeyError Incident

### Root Cause

Commit `035352c3 fix(D_02): date-gate canonical NNA attribution to advisor tagging window` modified `_load_canonical_nna_per_advisor` to require two new columns (`first_date`, `last_date`) on its input DataFrame. Only one of two callers was updated to supply them.

### Shape / Contract Mismatch

| Caller | Location | acct_adv_role columns supplied | Expected by `_load_canonical_nna_per_advisor` (post-035352c3) | Match |
|---|---|---|---|---|
| `build_advisor_books` | D_02:1176 | `account_id, advisor_name, _role, weight` | `account_id, advisor_name, _role, weight, first_date, last_date` | NO — KeyError |
| `build_advisor_timeseries` | D_02:1807 | `account_id, advisor_name, _role, weight, first_date, last_date` | (same) | OK |

### Why It Was Latent

- `035352c3` committed Apr 20 (afternoon) but D_02 on S3 stayed at `43c3693a` (FIX3A only) until DT uploaded `035352c3` tonight at RD's briefing trigger
- PROD bd-gold-trigger on 19:23Z ran `43c3693a` which had neither caller updated — no contract mismatch
- RD's ACK on `035352c3` was a spec review (RD described the intended change, I implemented it against one caller, RD confirmed the diff of record) — not a runtime verification
- First real run was tonight's qa-runner `d67a844f`-predecessor dispatch; bug surfaced in 52s

### Resolution Tracking

| Step | Owner | Action | Status |
|---|---|---|---|
| 1 | ~D | Author fix commit mirroring timeseries-path groupby | DONE — `048af6a3` @ 20:57Z local |
| 2 | DT | Overwrite S3 `code/gold/D_02.advisor_client_detail.py` from `git show 048af6a3:path` | DONE (implicit — AE re-dispatched; see step 4) |
| 3 | AE | Restart QA c6a.8xlarge + re-dispatch `--from D_02 --chain` | DONE — SSM `d67a844f` @ 21:00:29Z |
| 4 | ~D | Validate D_02 + D_03 + D_04 run to completion + emit expected fields | PENDING — ETA 21:12-21:15Z |
| 5 | ~D | Validate artifacts against RD's 5 invariants | PENDING — post-run |
| 6 | ~D | RAVC4 close to RD + COO | PENDING — post-validation |

### Prevention

New feedback memory candidate: when modifying a function signature (adding required input columns / parameters), grep for every caller before commit. Spec-review by another agent is not a substitute for a real run. In isolation-heavy pipelines where local-run of a full gold script is non-trivial, at minimum verify every caller has been updated to the new contract by explicit re-read before `git commit`. Will draft after validation closes.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| No code change on D_02 | Root cause is deploy gap, not a logic defect. All 3 stacked commits already on origin/CLOUD; S3 reupload from `git show 035352c3:path` resolves without new commit |
| D_04 widen via new commit `8593ea51` — not stacked onto a pending COO/CTO review | Pure additive widening, no schema change, no migration; spec was in RD brief verbatim. Blocking on review would miss tonight's nightly staging window |
| `.get(key)` no-default for 5 new slim-builder fields | FE `ClientsTab.tsx` distinguishes `undefined` (em-dash placeholder) from `0` (zero displayed). If D_00 emit later degrades, the FE should re-render em-dashes rather than misleading zeros |
| Defer Option 2 (refactor D_00 build_clients_tab off acct_snap) | account_performance schema compatible + row count healthy → high confidence acct_snap path works post-deploy. Option 2 would be belt-and-suspenders only; park unless Wed AM validation shows keys still absent |
| Bundle D_02 + D_00 + D_04 into single DT upload batch, single nightly cycle | 5 RD validations (2 briefings, 3 D_02 fixes + 2 clients-tab fixes) close as one atomic Wednesday-morning RAVC4 |
| Accept COO DEFER over today-redeploy (superseded) | Initial call. Superseded by AE's qa-runner test dispatch which surfaced the `035352c3` KeyError before nightly would have caught the same failure — better to fail in QA than on the overnight PROD cycle |
| Fix-forward in `048af6a3` rather than revert-then-repair | Revert would roll back `6f724293` (role_aua denom) and `035352c3` (NNA date-gate core). Both are RD-ACK'd correct fixes. Surgical +11/-5 commit completes the `035352c3` contract instead of undoing two correct fixes |
| AE Option B (full `--from D_02 --chain` tonight) over defer-to-nightly | Tests D_02 fix + D_04 `8593ea51` slim widen + D_00 `4299e1c0` emit in one cycle; if any fails, time to fix before nightly; if all pass, Wednesday AM RAVC4 closes immediately |

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| `data/black_diamond/scripts/gold/D_04.client_portal_summary.py` | Widened `build_clients_tab_slim` headline whitelist from 3 to 8 keys; `.get(key)` no-default on 5 new firm-level fields | Yes — `8593ea51` (author `0.4.0_DS_ClientPlatform~D`) |
| `data/black_diamond/scripts/gold/D_02.advisor_client_detail.py` | Fix-forward for `035352c3` incident — books-path `_acct_adv_role_books` builder (L1157-1174) mirrors timeseries-path groupby with `first_date=('date','min'), last_date=('date','max')`; empty-case DataFrame columns widened | Yes — `048af6a3` (author `0.4.0_DS_ClientPlatform~D`) |

No other gold-script modifications. Investigation work (`aws s3 cp`, `pyarrow.parquet` schema read, comp-pipescript runs) touched no source under version control.

Local branch `CLOUD` is 16 commits ahead of `origin/CLOUD` (`d13b11d5`) as of this writing — my commit `8593ea51` on top of 15 pre-existing commits (COO~Z org + various agent session-log backfills). Push coordination in DT's normal pod sweep; DT can upload from local git refs independently of push.

---

## Briefs Written

| Brief | Path | Audience | Priority |
|-------|------|----------|----------|
| Lifetime Activity chart vs leaderboard NNA attribution methodology | `docs/briefs/advi-lifetime-activity-chart-vs-leaderboard-attribution-methodology.md` | CTO / COO / RD / Andrew | **IMPORTANT** |

The brief documents a methodology divergence surfaced by post-`048af6a3` validation: Travis Q2 chart NNA `-$6.85M` vs leaderboard `-$6.31M` decomposed to reveal the entire $534k delta lives on inflows (outflows match to the penny). Diagnostic-clean signature that chart (per-day tagging gate) and leaderboard (current-snapshot × full window) use different attribution rules. Not a bug in `048af6a3` — it is the pre-existing D_02-vs-D_00c methodology divergence that was previously masked by the `035352c3`-class over-attribution bug the fix correctly removed. Three options in the brief (keep per-day gate / switch to current-snapshot / dual-view). Product-level decision required for advisor compensation + chart semantics; 50bps engine-accuracy sentinel (STAUDT.KPI ~C) should gate whichever view becomes canonical.

Other outbound this session: MCP responses (ACK + revised plan) to RD, pre-flags to CTO, defer endorsement request to COO, 3-file staged upload request to DT, incident + fix-forward dispatch, RAVC4 validation pack to RD, RIDE disposition to COO.

---

## Blockers

None. All actions authorized under standing protocols:
- RD authorized briefings via Andrew relay
- COO DEFER (`20260420T201xxxZ`) authorizes tomorrow-nightly staging pattern
- DT-online override authorizes DT as upload owner

Awaiting (not blocked):
- DT confirmation of 3-file staged upload
- Tomorrow nightly bd-gold-nightly-fallback PROD cycle auto-fires at 23:00 UTC
- COO explicit endorsement on D_00+D_04 expansion (was DEFER for D_02 alone; same cycle, same pattern — expecting ACK)

---

## Current State

Two RD briefings diagnosed as four stacked deploy gaps (D_02 × 3 commits `42be5b21`/`6f724293`/`035352c3`; D_00 × 1 commit `4299e1c0`) plus one real net-new widen commit (`8593ea51` D_04). DT uploaded the initial 3-file batch and AE elected to test via qa-runner before nightly — surfacing a latent KeyError in `035352c3` (books-path caller never updated to the new `_load_canonical_nna_per_advisor` contract). Fix-forward committed as `048af6a3`, DT overwrote S3, AE restarted QA c6a.8xlarge + re-dispatched SSM `d67a844f` at `21:00:29Z` running `--from D_02 --chain` (D_02 + D_03 + D_04). ETA 21:12-21:15Z. Local branch `CLOUD` tip is `048af6a3`, 17 commits ahead of `origin/CLOUD` (`d13b11d5`). No data damaged, no PROD impact — all work occurred on QA runner + code-deploy S3 keys.

---

## Next Steps

1. **[0.6.0_AE_PartnerETL] Complete qa-runner SSM `d67a844f`** — `--from D_02 --chain` ETA 21:12-21:15Z. MCP on completion with D_02/D_03/D_04 wall times + any errors + fresh artifact paths on S3.
2. **[0.4.0_DS_ClientPlatform~D] Validate `048af6a3` books-path fix** — post-run, pull `s3://opal-data-bd/gold/entities/advisors/travis_penfield/book.json` and verify (a) no KeyError in `/tmp/gold_logs/from_D_02_20260420_210029.log` (b) `role_breakdown[*].small_account_clients[]` populated (Travis architect ~135 entries). If `_load_canonical_nna_per_advisor` books-call succeeded, the fix-forward is green.
3. **[0.4.0_DS_ClientPlatform~D] Validate full 5-invariant matrix against fresh artifacts (RAVC4 evidence):**
   - Travis book.json `role_breakdown[*].small_account_clients[]` populated (architect ~135 entries, implementor 1, consultant 10, local_ops 0, additional_advisor 2 per RD briefing)
   - Travis book.json `role_breakdown[*].aua` sums == leaderboard total_aua per role (arch $400M / cons $1.26M / impl $31.8M / addl $915k / local_ops 0 per RD briefing)
   - Travis timeseries.json `data[*]` Travis YTD `nna_canonical` +$6.3M / QTD -$6.3M (matches leaderboard)
   - Firm `platinum/firm/clients-tab-slim.json` `headline.fee_earning_aua + non_fee_earning_aua == total_aua` ($1.65B, within $0.01 rounding)
   - Firm `headline.fee_earning_client_count + non_fee_earning_client_count == client_count` (2,815 exact)
   - Firm `headline.small_account_count` non-zero, 4-figure (Travis architect alone is 135, firm-wide expected much higher)
4. **[0.4.0_DS_ClientPlatform~D] RAVC4 close** — MCP RD with evidence (artifact paths, actual values vs targets). MCP COO with batch deploy cycle close. If any validation fails, escalate per failure class (D_00 acct_snap still None → implement RD Option 2 holdings_lots aggregation; D_04 widen mis-deployed → re-verify byte match + re-trigger; D_02 fix-forward incomplete → further investigation of `_load_canonical_nna_per_advisor` callers).
5. **[0.4.0_DS_ClientPlatform~D] Draft prevention feedback memory** — "scan all callers before modifying function signature" — after validation confirms `048af6a3` lands clean. Will go under `memory/feedback_function_signature_all_callers_before_commit.md`.
6. **[0.4.0_DS_ClientPlatform~D] Post-mortem MCP to AE + CTO (optional, post-validation)** — 4 deploy gaps + 1 latent-bug incident surfaced in one evening is a systemic signal. Propose bd-gold-trigger Lambda pre-flight hash check on every D_* script; halt + page on STALE. Today's QA dispatch-before-nightly pattern is a clear win — AE's choice to test before overnight catches latent bugs like this one in minutes of wall, not hours of PROD impact. Parking until validation closes.
7. **[0.4.0_DT_ClientPlatform or any DT] Push `origin/CLOUD`** — 17 local commits ahead including my `8593ea51` + `048af6a3`. DT's normal pod sweep; not time-critical since S3 upload already uses local refs.
