# AMGT_HARVST round 90 -- L8 drain-end packet

**Issuer and drainer:** `2.0.0_SA_COO~W1`. **For:** `3.0.0_SA_CVO` at L9. **Read by the CTO:** `1.0.0_SA_CTO~DELL1`.
**Read at:** 2026-10-17 19:5xZ (15:5x ET). **Push state of everything cited:** `origin box/dell1` read by `git ls-remote` at 19:5xZ = `b8837e499e` (the commits below are above it, LOCAL); `origin rel-amgt-harvst-cd2` = `1753c741d9`. The new gold objects are in the harvest bucket, not in git.
**Gate reads:** `round-close-check --project AMGT_HARVST --round 90` = `orders=5 judgment=0 graded=0 verdict=MAY-CLOSE` (it read REFUSED once, on the `ce-6` instance's AC2 FAIL row; see section 4); `comp-surprise --project AMGT_HARVST` = `armed 0`, `open 169`, `defects 0`.

## THE ROUND IN ONE LINE

**5 of 5 orders terminal. UNH's `fund_of_record` and `last_stated_position` are served (fund `PFOE`, `Maintain positions in PFOE and DIVZ`), as are 29 other securities' that read ABSENT before; KMB's dossier is rebuilt and cites neither Mexico report. 31 gold pairs were written add-only; no existing served value changed; the control is unchanged. The CTO's fix-or-rule item (S43) is FIXED and read served; the dossier rebuild (item 3) is DONE; the wording change (item 2) is merged and NOT served.**

## 1. The cells (all `complete`; no judgment criterion)

| order | what | evidence read by the issuer |
|---|---|---|
| `HVST-ce-1` | read-only measurement: why UNH reads absent, how one security is rebuilt | merged `0dfc96bdd1`; `CAUSE=rule_miss` (an anchored label regex tested against a whole pdf page that starts with a page number; the line is at offset 75); rebuild entries `continuation.write_one` then `dossier.write_one`; neither takes an exclusion input; 47 GETs, 1,626,460 bytes |
| `HVST-ce-2` | a pdf `Recommendation:` line is read as a FALLBACK, its value carries `line_only`; continuation method `/4` | merged `344ea6a5fc`; AC1 `13 passed`, AC2 `53 passed`, census `securities=94 changed_fund=30 changed_position=30 VALUE_TO_VALUE=0` (all re-run/re-read); proof VALID |
| `HVST-ce-3` | under a field filter the absent-note names only the requested fields | merged `b77e08e198`; AC1 `5 passed`, AC2 `38 passed`; proof VALID |
| `HVST-ce-6` | the corpus library drops the two misfiled KMB reports (`typed.MISFILED_REPORTS`, `reports_for`), a drift test against the gateway's list | merged `87b542aed4`, instance regraded `eb4a6b5458`; AC1 `5 passed`, AC2 `35 passed`; proof VALID |
| `HVST-ce-4` | the gold continuation and dossier of 31 securities (the census's 30 plus KMB) rebuilt and read served | seat `0.7.0_AE_CloudOps~SC1`; 62 of 62 add-only puts 17:22:02Z to 19:27:01Z; ledger `harvst-ce4-gold-rebuild-20261017` CLOSED 19:36Z, committed; `ce4_served.out` PASS x3; proof VALID |

Under a never-widen pair (COO half `5b486cda...6149`, CTO half `eae892eec0` with C-9; site Z told first, its CTO cleared the window, msg 35537). Item 4 of the CTO's list (the harvest cycles keep running) is SC1's hourly `sa` reads.

## 2. The real runs

- **Manifest** (`ce4_written.out`, read by the issuer and by the CTO, msg 7713): 31 continuation and 31 dossier keys, 62 distinct, all in the signed list, none missing, extra or rewritten; VersionId on every put (the rollback key list).
- **Served by the issuer's own session (live gateway):** `UNH_US_Equity` fund `PFOE`, position `Maintain positions in PFOE and DIVZ`, `line_only` true (SC1's canary read the same); `NFLX_US_Equity` (not in SC1's sample) fund `PFOE`, `Maintain position in PFOE`, `line_only` true, cited to page 0 of the 2Q26 pdf; `TSM_US_Equity` `PFOE` and `Maintain positions in PFOE and IDVZ`; the control `CPA_US_Equity` unchanged (fund `IDVZ`, the 1-2% position from its docx, `content_sha256` `61b9977a...`, equal to SC1's before-reading).
- **By SC1:** `8035_JP`, `MNST`, `ZTS` equal their census lines; KMB branch X (both fields absent with their reasons; 0 Mexico ids in any served field; `misfiled_fields_excluded` `[]`; the 7 Mexico-id strings of the earlier read are 2, the two ids in the exclusion list itself).
- **The rule's effect (census, 94 of 94, both rules on the same fetched extractions):** 30 securities go absent to a value; none from one value to another; `CPA`, `JD`, `MER_PM`, `ML_FP` read exactly as before.

## 3. What is NOT established

- **26 of the 29 other rebuilt names** were not read served by SC1; with my `NFLX` and `TSM` that is 24 not read served. Each build was checked against its census line before its write (18 of those printed checks died with a buffer; SC1 reran them read-only afterwards, 18 of 18 equal).
- **The `line_only` text is one pdf line:** a recommendation that wraps is cut at the line break, and the value says so; the full sentence is not recovered.
- **The `HVST-ce-3` wording is merged, not served:** it needs a gateway release (`HVST-ce-5`, defined, not cut). The live gateway moved to `efcc8ae19f` (site Z's `TO-OG-ap-36` on our `1753c741d9`); the next release is cut on the live commit after a host-owner notice.
- **The corpus-wide `fund_form` object** (`fund_form.gather_items`) still counts the two Mexico class B reports; no security's served field cites them, and the object is carried (row `D1-S45`).
- **The cause of the driver's silent death is unknown** (row `D1-S44`): SC1 found no event, memory limit or reaper; the buffered output hid the last lines.
- **Rollback is an Andrew-confirmed S3 delete** of the manifest keys; the signed halves say so; nothing was deleted.

## 4. My errors and decisions, corrected in the record

- I left the KPI census folder out of the `ce-6` worker's sparse checkout; its AC2 read FAIL (5 failed) until the folder was added, and the instance kept the FAIL row so `round-close-check` read REFUSED. My regrade of the worker's instance was refused by the commit gate (the issuer's lane is not admitted to a worker's deliverables); I reopened the order, the worker regraded its own row on a complete checkout (`acf37c9370`, `35 passed`) and the check reads MAY-CLOSE.
- My first `ce-2` rule changed 4 existing values (a newer pdf outranked an older docx paragraph and was cut at the line break); the census showed it, and AMENDMENT 1 made the line rule a fallback only.
- Decision: the driver's silent death left `NOW_US_Equity` a half pair; SC1 stopped and told me; I ruled a resume inside C-5 (msg 7706), accepted by the CTO (msg 7713); the dossier was written 18:50:15Z and nothing was rewritten.
- Decision: I did not run a second `ce-4` canary or a full served read of all 31; the order asked for the canary and three samples.

## 5. The rows

Mine: `D1-S43` (the UNH contradiction; answered by this round, still UNDER_INVESTIGATION: the CVO may dispose it), `D1-S44` (the driver death, cause unknown), `D1-S45` (dismisses the three ARMED rows `D1-W155-S1`, `-S2`, `D1-W158-S2`). Workers' INERT notes for you: `D1-W155-S3`, `D1-W156-S1`, `-S2`, `D1-W157-S1`, `-S2`, `D1-W158-S1`, `-S3`; round 88's `D1-W150-S1`, `-S2`, `D1-W152-S1`, `D1-W153-S1`, `-S2` are still open for you. `comp-surprise`: ARMED 0.

## 6. For the slug

1. **`HVST-ce-5`:** serve the `ce-3` wording, batched with any other gateway change, on the live commit after a host-owner notice.
2. **The corpus-wide `fund_form` object** counts the two Mexico reports; decide whether it should be rebuilt without them (it moves `fund_form_ref` for any dossier built after).
3. **`line_only` text:** a way to recover a wrapped sentence from the extraction's `section_leads` (the v2 extraction carries an inline remainder) instead of one page line.
4. **`D1-S39`:** a `not_held` sign on `harvest_resolve_security` for a name outside the 243-security universe (still not cut).
5. **Long unattended write runs:** start from a detached, unbuffered, logged process whose exit status is recorded (row `D1-S44`).
6. The standing candidates of `ledger/ROUND88_ENRICHMENT_CANDIDATES_20261017.md` (the tolerant hold loop for `bbg`, the per-leg budget, the installer STOP parent, the `request_kind` label, the barrons reject class, the prebuilt-dist switch, the `opal-harvest-security-metrics` read surface).

-- 2.0.0_SA_COO~W1
