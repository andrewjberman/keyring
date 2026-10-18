# AMGT_HARVST round 92 -- L8 drain-end packet

**Issuer and drainer:** `2.0.0_SA_COO~W1`. **For:** `3.0.0_SA_CVO` at L9. **Read by the CTO:** `1.0.0_SA_CTO~DELL1`.
**Read at:** 2026-10-18 03:2xZ (23:2x ET on 10-17). **Push state of everything cited:** `origin box/dell1` read by `git ls-remote` at 03:26Z = `ff8796e0e6ed` (it holds the `HVST-cf-3` merge `04be089e13`; the commits after it, up to `2452c0b9ca`, are LOCAL); `origin rel-amgt-harvst-cg3` = `4257a2aa42`, the deployed gateway release. The silver parts and the fund-form objects are in the harvest bucket, not in git.
**Gate reads:** `round-close-check --project AMGT_HARVST --round 92` = `orders=7 judgment=0 graded=0 verdict=MAY-CLOSE`; `comp-surprise --project AMGT_HARVST` = `armed 1` (`D1-S52`, the CTO's to disarm; section 5), `open 172`, `defects 0`.

## THE ROUND IN ONE LINE

**7 of 7 orders terminal. A report's relation to a fund is now a stored, served fact: every one of the 353 stored research reports carries `fund_relation` (holding 121, candidate 14, initiate 2, interest 2, template 1, none 213), the gateway serves it in `research_reports[]` (MNST, ADBE, SNPS, CLX `candidate`; ML_FP `template`; UNH `holding`), and the fund forms for IDVZ (82 reports) and PFOE (33) now count holding reports only and never the two misfiled Mexico reports. No gold value changed. Four things are NOT closed and are named in section 3: DIVZ still resolves to a stale form, a UNH rebuild would serve the fund of record ABSENT, `AC3` of the last order was re-specified by me, and the stored dossiers still cite the old forms.**

## 1. The cells (all `complete`; no judgment criterion)

| order | what | evidence read by the issuer |
|---|---|---|
| `HVST-cg-1` | `fund_relation` classifier (7 values) in the silver row builder; a read-only census of the stored silver; a dry run of the rewrite | merged `ad116e0037`; AC1 `17 passed`, AC2 `58 passed`; census re-run by me, identical to the worker's; proof VALID |
| `HVST-cg-5` | `reduction` and `adding` read as holding words; one closed alias `RECOMMEDATION` (the CTO's rulings, msgs 7782, 7784) | merged `a9aecdd593`; AC1 `22 passed`, AC2 `58 passed`; the re-census `holding=121 unclassified=0 none=213` (the CTO's expectation), `MOVED_ROWS=4`, re-run by me; the CTO's guard on `adding`: 2 rows, both `CPA`, held; proof VALID |
| `HVST-cg-2` | every stored silver row re-appended with `fund_relation`: 3 NEW parts (84 + 121 + 148 = 353 rows), canary first | seat `0.7.0_AE_CloudOps~SC1`; written 01:00:35Z to 01:01:14Z, each part read back equal; ledger `harvst-cg2-silver-fund-relation-rewrite` CLOSED, committed `8225380445`; pair COO `11cf6bd0...9158` + CTO `b4aac7476a`; site Z cleared (its CTO msg 35578); proof VALID |
| `HVST-cg-4` | the gateway `REPORT_FIELDS` gains `fund_relation` (code and offline tests) | merged `290f2e9e6d`; AC1 `5 passed`, AC2 `43 passed`; proof VALID |
| `HVST-cg-3` | the gateway release (the `cg-4` hunk and the `ce-3` absent-note wording, on the live commit `d077cef043`) | seat SC1; release `4257a2aa42` (3 paths, 2 hunks, md5 `596c2995...`), deployed 02:06:03Z, ledger `harvst-cg3-gateway-fundrel-release` CLOSED (`ee508eb3cb`); pair COO `29d9e1b9...87c4` + CTO `48d6e4e72b`; site Z cleared (its CTO msg 35599); proof VALID |
| `HVST-cf-3` | the fund form counts only reports whose silver row states `holding`, never the misfiled reports; a row without the key raises; method version 2 | merged `04be089e13`; AC1 `7 passed`, AC2 `80 passed`; census re-run by me, identical: `reports_before=139 reports_after=115 dropped_nonholding=22 dropped_misfiled=2` (IDVZ 94 to 82, PFOE 43 to 33, DIVZ 2 to 0); proof VALID |
| `HVST-cf-5` | two `research-fund-form` objects, method version 2: PFOE (33 reports, canary) then IDVZ (82) | seat SC1; written 02:45:48Z and 02:46:39Z; ledger `harvst-cf5-fund-form-v2-rebuild` CLOSED 03:22:12Z, committed (`334218577d`); pair COO `a7c7f05e...8b6f` + CTO `78b98db60d`; site Z cleared (its CTO msg 35606); proof VALID; `AC3` re-specified (section 3) |

## 2. The real runs (each read by the issuer, not taken from a seat's report)

- **The silver after `cg-2`** (`deliverables/2.0.0_SA_COO_W1/round92/cg2_issuer_verify.out`, my read by the gateway's newest-part rule): 8 parts (5 old, 3 new), 353 of 353 reports from the new parts, all with `fund_relation`, counts equal the census, 0 mismatches of any other column against the row each supersedes.
- **The gateway after `cg-3`**, through the redeployed tool in my own session: `MNST_US_Equity` `fund: PFOE` with `fund_relation: candidate`; `ML_FP_Equity` `fund: IDVZ` `template`; `CLX_US_Equity` both class A reports `DIVZ` `candidate`; the control `UNH_US_Equity` `holding`, its `content_sha256` `6bd7cea7...` unchanged (re-read after `cf-5` at 03:23Z, still equal). SC1 read ADBE and SNPS (`candidate`).
- **The fund forms after `cf-5`** (`cf5_issuer_verify.out`, my read): 11 objects (the 9 version-1 forms untouched, the 2 new), both `method_version` 2, `reports` 33 and 82, the recomputed `content_sha256` equal to the stored one; `fund_form.read_latest` returns both new objects.
- **The CTO's own checks of this round:** the `adding` guard, the re-census (121/0/213), the pair halves, the gateway proof names.

## 3. What is NOT established or NOT closed

- **DIVZ still resolves to the STALE version-1 form** (2 reports, counting candidate and the misfiled reports): no holding report names DIVZ, so no version-2 form exists for it, and `substrate._pick_stored` falls back to the last stored object with `current` False. The CTO's condition 2 keeps C-6 (no dossier or continuation `write_one` that reads DIVZ's form) IN FORCE after the `cf-5` close, until a round-93 cell.
- **A UNH dossier or continuation rebuild today would serve `fund_of_record` ABSENT** (row `D1-S52`, ARMED): `substrate._continuation_member` picks UNH's `/3` continuation (fund absent) instead of the `/4` object the gateway serves (PFOE). Only UNH was read; a name in the same state (77 of the 94 were not rebuilt at the current continuation method) may behave the same. No rebuild is ordered; the issuer orders none before the CTO rules.
- **`AC3` of `HVST-cf-5` was mis-specified by me and re-specified.** I wrote that an in-memory dossier preview of CPA would equal the stored dossier except `fund_form_ref`; it also differs in the build date, in the continuation the substrate picks and in a newer Bloomberg pull. SC1 graded it FAIL by my letter and kept that reading as history. The criterion text is unchanged; its reading became a controlled comparison (two previews, the fund form resolved new and old, same inputs) that differ only in `fund_form_ref` and the hash and inputs entry derived from it (AMENDMENT 3). **Please regrade `AC3` on that record if you read the change differently; both readings are in `cf5_served.out`.**
- **The stored dossiers still cite the version-1 forms** in their `fund_form_ref`; none was rebuilt (C-6, and `D1-S52`).
- **Not read:** the 28 `research_reports[]` entries the tool omits for CPA (the response-size cap, row `D1-S50`); any consumer of the silver `fund` beyond the repo's `lib/` and the gateway app (the worker's list of 9 consumers: `fund_form` read `fund` as a named token before this round, which is why the worker marked it "not held"; the CTO's ruling made it the one "held" consumer and `HVST-cf-3` changed it; the others, the gateway copy and the ingest run summary, read `fund` as a named token; `portal/` was not searched); gold values (unchanged; `fund_relation` is a silver field).
- **Two misfiled KMB rows** were not re-appended and carry no `fund_relation`; the gateway excludes them.
- **Rollback of the silver parts and the fund forms is an Andrew-confirmed S3 delete** of the manifest keys; nothing was deleted.

## 4. My errors and decisions, corrected in the record

- **My `cg-2` COO half said `source_keys` and the `research_reports[]` entries stay equal after the rewrite**; the gateway lists the parts it read and names the winning part. SC1 found it and refused to self-grade; I ruled the difference expected (AMENDMENT 2), the CTO accepted (msg 7813).
- **My `cg-3` COO half named the rollback as `previous_deployed_commit` read at the start (`efcc8ae19f`), which would also undo site Z's batch 7**; SC1 asked; I ruled the rollback target is the commit the release was cut on (`d077cef043`, AMENDMENT 2).
- **My `cf-5` half carried three errors:** the store held 9 version-1 forms, not one per fund; UNH's substrate member cannot read the new form (a pre-existing continuation pick); and the `AC3` above. I had also misstated the hazard of changing `fund_form` (I wrote that a dossier build finds NO stored form; it falls back to the stale one with `current` False).
- I left the gateway app folder out of the `cg-5` worker's sparse set (its AC2 read `57 passed, 1 skipped`), the same class as round 90's `ce-6`; and my `cf-3` order said the Mexico reports sat "in KMB's form" (a fund form is per fund; they sat in IDVZ's).
- **A process error:** an act-bearing `cg-4` order was first cut as `LOCAL` under a shared workstream and refused twice by the gate (declared `WORLD`, own workstream; not overridden).
- Decisions: I added the word `adding` to the CTO's two rulings (CPA's line reads `Consider adding ... in IDVZ`) and told the CTO, who kept it (msg 7784); I nudged SC1's terminal after a peek three times when mail sat unread (row `D1-S51`).

## 5. The rows

Mine: `D1-S46` (the silver field; ruled and REMEDIATED this round), `D1-S47` (dismisses the ARMED `D1-W159-S1`, round 91's), `D1-S48` (dismisses the ARMED `D1-W162-S1`), `D1-S49` (silver and gold classifiers differ on two words; round 93), `D1-S50` (the response-size cap shows one fewer entry; the CTO's round-93 row), `D1-S51` (SC1 does not consume inbox mail while idle: three times, the worst 47 minutes; for the CTO and MSTR), **`D1-S52` (ARMED, disarm owner `1.0.0_SA_CTO~DELL1`: the continuation pick)**. Workers' INERT notes for you: `D1-W161-S1`, `-S2`, `-S3`, `D1-W163-S1`, `-S2`, `D1-W164-S1`, `-S2`; earlier rounds' notes are still open for you.

## 6. For the slug

1. **`D1-S52`:** the continuation pick (a rebuild of a name not at the current method serves the older object); decide the rule before any dossier or continuation rebuild, then whether the stored dossiers should be rebuilt so they cite the version-2 forms.
2. **DIVZ:** resolve to a version-2 form with 0 reports and an absent reason, or stop the substrate falling back to a stale form (the CTO's round-93 cell 1).
3. **`D1-S49`:** one classifier shared by silver and gold.
4. **`D1-S50`:** the tool's response-size cap must not drop a `research_reports[]` entry silently (the CTO's round-93 cell 2).
5. **`D1-S51`:** why an idle seat does not read its inbox (the delay cost a 47 minute stall inside a 2 hour write window).
6. The standing candidates of `ledger/ROUND88_ENRICHMENT_CANDIDATES_20261017.md`.

-- 2.0.0_SA_COO~W1
