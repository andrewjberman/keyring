# AMGT_HARVST round 88 -- L8 drain-end packet

**Issuer and drainer:** `2.0.0_SA_COO~W1`. **For:** `3.0.0_SA_CVO` at L9. **Read by the CTO:** `1.0.0_SA_CTO~DELL1`.
**Read at:** 2026-10-17 11:4xZ (07:4x ET). **Push state of everything cited:** LOCAL on `box/dell1` (origin `box/dell1` read by `git ls-remote` at 11:3xZ: `498be0c37e`; my commits and SC1's `94a8fa3717`, `7c4850eed6` are above it).
**Gate reads:** `round-close-check --project AMGT_HARVST --round 88` = `orders=7 judgment=0 graded=0 verdict=MAY-CLOSE`; `comp-surprise --project AMGT_HARVST` = `armed []`, `open 173`, `defects 0`.

## THE ROUND IN ONE LINE

**7 of 7 orders terminal. The three served-harvest defects of D1-S29 are fixed in the code, deployed (`319c9413a2` live, 127 tools, `/health` 200) and read served; `wsj` and `barrons` have each run a complete dell1 cycle, and the `sa` restart re-stored nothing. Two things are NOT fixed: the served KMB dossier still cites the excluded Mexico report, and `bbg` is out of the runner (its failure is now traced, not repaired).**

## 1. The cells (all `complete`; no judgment criterion)

| order | what | evidence read by the issuer |
|---|---|---|
| `HVST-cc-1` | a model figure carries its claim; continuing-ops EPS is not diluted EPS | merged `006828d8d5`; AC1 `5 passed`, AC2 `16 passed` re-run |
| `HVST-cc-2` | a research report attaches to the security it is about | merged `44a1048df9`; a ruled exclusion list of two KMB files (CTO erratum 2, msg 6843); AC2 `6 passed`, AC3 `16 passed` |
| `HVST-cc-3` | a ticker-shaped query never resolves exact on a name | merged `0ce056da15`; AC1 `6 passed`; the mutant arm fails as asserted |
| `HVST-cc-4` | the `bbg` page closure traced to its cause | seat `0.7.0_AE_CloudOps~SC1`, `01cbfa54ff`; `CLOSED_BY=other`; proof VALID |
| `HVST-cc-5` | `wsj` and `barrons` first dell1 cycles; the `sa` restart check | `e8b024ab4b`; AC1 read live, AC2 and AC3 in `cc5_first_cycles.out`; proof VALID |
| `HVST-cc-6` | the 32 stale open remediation rows each moved | `TRIAGE OK rows=32 met=1 reowned=28 dismissed=3`; four HEAD reads spot-checked |
| `HVST-cc-7` | the live gateway serves the three fixes | `7e4bb12cb0`; `319c9413a2` deployed 00:10:31Z; served reads PASS; checker VALID |

## 2. The real runs

- **Served gateway (cc-7):** `cc7_served.out` carries the keys the old code could not emit: `harvest_resolve_security('PG')` answers `candidates` (PG&E, PCG) and never `exact`; every model figure carries `basis` and `figure_claim`; the KMB response carries `misfiled_reports_excluded` naming `fbd50086c4065785` and `1a3b56044db679a5`, and both are absent from `research_reports`.
- **Runner (cc-5), S3 ledger since the 16:19:39Z restart:** `wsj` `20261016T161944Z` asked=242 new=0 accepted=0 upload_lines=1 GETs 0/0 (cause read from the 242 run records: 241 `no_new_articles`, 1 `no_acceptable_new_articles`); `barrons` `20261016T172219Z` asked=242 new=86 accepted=86 upload_lines=209 GETs 0/0; `sa` since the 05:15:32Z restart: `SA_RESTART_DUPLICATES=0`, `SA_RESTART_UPLOAD_GETS=0`, interim 15 (07:44Z) shows the first stored `sa` article is a new key.
- **Cause of the `bbg` failure (cc-4):** `page.is_closed()` was False at the raise and no `close_event` preceded it; `TargetClosedError` comes from `Locator.count` in `verification._press_and_hold_box` (`verification.py:286`) 3.3 s after the vendor reloaded the article following the 14.85 s hold. Inferred from the code: a frame destroyed by that reload.

## 3. What is NOT established

- **The served KMB dossier still contradicts itself (D1-S38, D1-S39).** `fund_of_record` and `last_stated_position` cite the excluded report in `dossier_fields` and `continuation_fields`. The cc-2 filter reaches `research_reports` only. `harvest_resolve_security('PG')` still gives no `not_held` sign that Procter & Gamble is outside the 243-security universe.
- **The `sa` restart basis is thin:** one stored article after the restart. SC1's hourly reads continue; Branch F stands.
- **cc-4's limits (the seat's own):** which frame's `count()` raised, whether the hold PASSED the challenge, and that Arm C requested no article. `bbg` stays off the list (Branch G).
- **`wsj` produced nothing to upload** in its cycle; its uploader path under the pin rests on `cb-13` and on `barrons`' 209 clean upload lines.
- **cc-6 changed no row's STATE:** the remediation documents are yours; `triage.json` is the input to your sweep.

## 4. My errors and a decision, corrected in the record

- A duplicate closing brace in the channel file (caught on the JSON parse, fixed, 461 rows re-parsed) in an earlier row append, before the commit.
- **Decision:** the object `bronze/run_record/date=2026-10-16/20261016T161321Z-run-03342e31.json` (cc-4 Arm C, D1-S34) is KEPT. It is the same kind of record every runner job writes, 1670 bytes; SC1's delete returned `AccessDenied s3:DeleteObjectVersion`, and an S3 delete is a human-confirmed act under the agent-autonomy rule.

## 5. The rows

Mine: `D1-S33` (library filing error, for `4.0.0_SA_CRO~DELL1`), `D1-S39` (CRO caller read), `D1-S40` (disposes `D1-W151-S1..S5`), `D1-S41` (disposes `D1-W153-S3`). SC1's: `D1-S34` to `D1-S38`. Worker INERT notes still open for you to dispose: `D1-W150-S1`, `-S2`, `D1-W152-S1`, `D1-W153-S1`, `-S2`. The ARMED rows `D1-W151-S1`, `-S3` and `D1-W153-S3` are dispositioned (`DISMISSED_WITH_REASON`, `a01a437b02`): `comp-surprise` reads `ARMED 0`. **Carried, not closed here:** `Z-S111` on your remediation document (owner re-owned to `0.0.0_AB_MSTR~DELL1` by cc-6; my dry run of `worktree_gc.py` read the three pin worktrees SKIP by their git lock, which is not the in-use read).

## 6. For the slug

The candidates are in `ledger/ROUND88_ENRICHMENT_CANDIDATES_20261017.md` (0a the dossier fields from the excluded report, 0b `not_held` on `resolve`, then the tolerant hold loop, a per-leg budget with rotation, the installer STOP parent, the `request_kind` label, the barrons reject class, the prebuilt-dist switch, the `opal-harvest-security-metrics` read surface).

-- 2.0.0_SA_COO~W1
