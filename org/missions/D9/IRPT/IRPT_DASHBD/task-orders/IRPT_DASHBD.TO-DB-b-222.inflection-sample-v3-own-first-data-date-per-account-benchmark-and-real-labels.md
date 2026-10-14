# TO IRPT_DASHBD.TO-DB-b-222 -- the INFLECTION SAMPLE v3 (data half of the render remedy): each account's own first-data date and window statuses, its own since-inception benchmark, the gain/loss Ending Value filled, the household return from Orion's client grain with its source claimed, the custodian number's real last four as the account label; private folder only

<to_id>IRPT_DASHBD.TO-DB-b-222</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~175</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>110</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2, ROUND-110 ANALYSIS section 2 cell 1 (the CVO's four-line remedy, lines 1 and 2, and the label rule W173-S9) | **Rows:** IRPT_DASHBD-D2-W175-S<k> (continue your numbering) | **Decomp cell:** `DB-b-222` (decomposition section 112) | **outcome_ref:** FWD-2, FWD-21 | **depends_on:** `DB-b-217` (its status is complete on your branch: the contract 0.5.0 exists; this order is `staged` until the issuer flips it by continuation)

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-175` (branch `wk-IRPT_DASHBD-175`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~175/`; the private sample goes under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~175/` and ONLY there. Commit with `.tools/safe-commit.sh` and your author line; never push. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: an account's last four characters, any account, household or client id, and any figure from the silver are never written in the repo, a row or your report (counts, hashes and words only; a last four is `####`).

**Why.** The CVO graded the first Inflection render FAIL (`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_ROUND_109_L9_GRADE_20261014.md`). The data half of the remedy: (1) four accounts printed a "Since <their own first date>" column whose four benchmark rows were the HOUSEHOLD's since-inception figures (a four-month account carrying a two-year benchmark): each account's since-inception benchmark must be compounded over the account's OWN window, from its own first-data date; (2) the gain/loss Ending Value was absent while the overview printed it: it is the same quantity as `avs.<window>.ending_value` (the contract's `ENDING_VALUE_ACCOUNT` class, contract 0.5.0) and must be filled; (3) a window an account did not span is NOT_SPANNED and its benchmark cells carry INSUFFICIENT_HISTORY in not-spanned words, never "needs more history"; (4) the account label is the custodian number's real last four characters (the CTO: a client's own statements show it, alphanumeric allowed), never an ordinal; (5) the household return comes from Orion's `fact_performance` at the client grain with its source claimed (the CTO's ruling; contract 0.5.0 names the windows).

**The cell (`DB-b-222`).**
1. **Read first.** The issuer's check `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r110/p110_inflection.py` (function `check_sample` is your criterion; read it fully), the contract `org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json` (0.5.0: `equivalences`, `firm_sources`, `firm_absent`, `document.windows`, `document.filled_report` with `window_status_rule` and `first_data_date_rule`), your own records `~175/CONTRACT_R110.json`, and the previous sample's builder `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~173/build_sample_inflection.py` with its record `~173/BUILD_R109.json` (copy the builder to `~175/build_sample_inflection_r110.py` and edit YOUR copy only), the adapters under `data/assets/scripts/gold/irpt_reporting/adapters/` (`inflection_account_dim.py`, `model_series_windows.py`), and round 109's positions cache `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~174/work/positions_daily_cache.parquet` (READ-ONLY private data: one row per account per partition day; an account's first data date is the first day it has positions rows, `n_rows > 0`).
2. **Build the sample v3** into `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~175/HOUSEHOLD_SAMPLE.json` (a NEW file; never overwrite the round-109 sample), the same household as round 109 (the hash rule), the same `as_of` rule, and these changes against it: (a) each account's `first_data_date` is the first date it has positions rows, the household's the earliest of its accounts'; (b) each account's `window_status` for `qtd`, `ytd` and `last_12_months` is `NOT_SPANNED` when the account's first data date is after the window's start day (the contract's `start_rule`), otherwise `MEASURED` (or `BREAK` only where the contract's rule says so); `since_inception` opens on the account's own first date; (c) for each account and each NOT_SPANNED window, every `avs.<window>.benchmark_*` entry is the absent form `{absent, kind: INSUFFICIENT_HISTORY}` with the not-spanned words "This account did not exist at the start of this period." and nothing else (the words must not contain "needs more history"); (d) each account's `avs.since_inception.benchmark_*` entry is the served series compounded from the account's OWN first date (use `model_series_windows` the way the household's since-inception figure is built, with the account's first date as the start); (e) `glr.ending_value` is filled for every account with the same figure as `avs.since_inception.ending_value` for that account (they are one quantity); the other `glr.*` and all `trgl.*` members stay the lot absent form with the words "Lot-level detail is not available for this account yet." exactly as in round 109; (f) each `pvs.<window>.return_cumulative` that contract 0.5.0 sources for Inflection (`firm_sources.inflection`) is the household's client-grain figure from Orion's newest `fact_performance` partition, in PERCENT POINTS per the member's `fold`, and each window the contract marks `firm_absent` stays the absent form NO_SOURCE_YET with the contract's reason; the account returns `avs.<window>.return_cumulative` stay NO_SOURCE_YET with "Account-level returns are not available for this firm yet."; (g) each account's `last4` is the last four characters of its custodian number as the silver stores it (letters allowed, nothing else changed), distinct within the household; if two accounts of the household share a last four, file a BLOCKING row stating only the count and stop; (h) everything else as round 109. The positions cache is read-only private input: do not write it.
3. **Record** `BUILD_R110.json` in your folder with exactly the fields the checker reads (read `check_sample`): `sample` {`path`, `sha256`, `contract_sha256`}, `whole_document` {cells_scanned, absent_cells, keys, unmapped 0, conflicts 0}, `equivalence` {classes, conflicts 0}, `household_ref_sha256`, `as_of`, `benchmark_data_as_of`, `not_spanned_account_windows` (the integer count of NOT_SPANNED account windows among qtd, ytd, last_12_months), `household_return_source` {`windows`, `claim` (words: reported by Orion at client grain), `newest_partition_only` true, `partition_date`}, `last4_source` (words: the custodian number's last four characters as stored), `benchmark_members` {total 32, filled}, `orion_guard` (copy the issuer's read-gate state from `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/ALIEN_READ_R109.json` `result.guard_state_for_render_record`), `builder` {`file` "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~175/build_sample_inflection_r110.py", `sha256`, `tracked` true}, `reads` {`s3_reads` integer, `s3_writes` 0, `dynamodb_writes` 0, `vendor_calls` 0, `secret_reads` 0}, and the false flags `files_in_repo`, `served_values_changed`, `pushed`, `deployed`. Counts, hashes and words only; the record holds no run of 8 or more digits.
4. **Earlier criteria.** After your build run `python -I ".../checks/r109/p109_round109.py" . DB109-1-AC1`: it binds the OLD sample and must still read PASS; report its verdict.

<criterion id="DB110-2-AC1" cell_refs="DB-b-222"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r110/p110_inflection.py" . DB110-2-AC1</invocation><expect>DB110-2-AC1 PASS</expect></criterion>
`DB110-2-AC1` -- the sample v3 is bound to the contract 0.5.0 bytes; passes the kind carrier and the whole-document rule (denominator equal to the record's, a planted conflict caught) and the equivalence rule (0 conflicts, a planted pair caught); is the hash-rule household; each account's first-data date equals the first date it has positions rows (the checker reads the cache) and the household's is the earliest; each NOT_SPANNED account window (by the start-day rule) carries INSUFFICIENT_HISTORY benchmark cells in the not-spanned words and never "needs more history"; an account that opened after the household's inception carries a since-inception benchmark that differs from the household's, and one that opened on the inception date carries the same; `glr.ending_value` is filled for every account; lots and account returns stay words; the household return is filled in exactly the windows the contract sources for Inflection and NO_SOURCE_YET elsewhere; each last4 is four letters or digits, distinct, never the ordinal 0001, 0002, ...; the record's builder is tracked and hashed, uses the Inflection adapter, names no other firm and holds no write call; zero writes, vendor calls and secret reads; the false flags. Base: FAIL (no record).

<expected_criteria>DB110-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the contract, the round-109 sample and builder, every adapter and test, the issuer's check files and the positions cache.
- **Reads and writes.** Reads: repo files; the S3 LIST and GET of the two granted Inflection prefixes ONLY through the adapter's GET-only reader; the one served-series GET through `model_series_windows`; the private positions cache. Writes: the repo files of the grant and the private folder named above. No write to AWS of any kind, no deploy, no push, no vendor call, no secret read, no read of any other firm's place.
- **Client data.** The silver, the cache and the sample are client data: counts, hashes and words only in the repo, a row or your report.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A pair of cells that GENUINELY disagree is a finding: file a row naming the key and stop on that point; never plug a value. If a member's source does not exist in Inflection's silver, it is absent with its true kind, never a guess. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W175-S<k>` (continue your numbering), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~175/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-222.inflection-sample-v3-own-first-data-date-per-account-benchmark-and-real-labels.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 112 (round 110), cell `DB-b-222`.
<owned_cells>DB-b-222</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB110-2-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~175/IRPT_DASHBD.TO-DB-b-222.inflection-sample-v3-own-first-data-date-per-account-benchmark-and-real-labels.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB110-2-AC1` BEFORE the flip; pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the counts (accounts, NOT_SPANNED account windows, benchmark members filled, cells scanned, absent cells); which household return windows are filled and the partition date; that the round-109 criterion DB109-1-AC1 still reads PASS; reads and writes. Counts, hashes and words only: no client or account id, no last four, no figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a private sample built in memory from granted read-only prefixes; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: the adapter's GET-only reader under the two granted Inflection prefixes; no grant is changed and no AWS write.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; DB110-2-AC1 FAILS at base (no record) and its controls (a planted whole-document conflict, a planted equivalence pair) are exercised by the checker's self-test.
lane: the <paths> block IS the grant.
</preflight>
