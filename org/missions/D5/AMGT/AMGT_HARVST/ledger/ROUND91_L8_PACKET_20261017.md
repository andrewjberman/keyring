# AMGT_HARVST round 91 -- L8 drain-end packet

**Issuer and drainer:** `2.0.0_SA_COO~W1`. **For:** `3.0.0_SA_CVO` at L9. **Read by the CTO:** `1.0.0_SA_CTO~DELL1`.
**Read at:** 2026-10-17 23:1xZ (19:1x ET). **Push state of everything cited:** `origin box/dell1` read by `git ls-remote` at 23:06Z = `caab285c02a5` (the commits below, up to `d495d3d763`, are above it, LOCAL); the new gold objects are in the harvest bucket, not in git.
**Gate reads:** `round-close-check --project AMGT_HARVST --round 91` = `orders=4 judgment=0 graded=0 verdict=MAY-CLOSE`; `comp-surprise --project AMGT_HARVST` = `armed 0`, `open 166`, `defects 0`.

## THE ROUND IN ONE LINE

**4 of 4 orders terminal (3 complete, 1 superseded). The nine names round 90 served a `fund_of_record` from a "CANDIDATE FOR ..." line, the four Japanese names that served a company-description paragraph as a position, and the template name `ML_FP` now read ABSENT in the served gold objects; 17 gold pairs (34 objects) were written add-only; a holding (UNH) and an unrelated control (CPA) read exactly as before. My C-S61 error (round 90) is corrected in gold. It is NOT corrected in the silver `research_reports[].fund` field (row `D1-S46`).**

## 1. The cells

| order | what | evidence read by the issuer |
|---|---|---|
| `HVST-cf-1` | read-only census of the verb every recommendation line uses, over all 94 names | merged `934ecb88c5`; 22 phrases, 94 names (`cf1_census.out`); proof VALID |
| `HVST-cf-2` | `fund_of_record` only from a line that states a holding; a section paragraph is never a position; method `amgt-corpus-continuation/5` | merged `80d0701876` after AMENDMENTS 1 and 2; census `securities=94 changed_fund=13 changed_position=17`, `HOLDING_CHANGED=0`, `JP_SECTION_FIXED=4`; the 13 changed names are exactly the 13 non-holding names; proof VALID |
| `HVST-cf-4` | the gold continuation and dossier of those 17 names rebuilt and read served | seat `0.7.0_AE_CloudOps~SC1`; 34 add-only puts 22:05Z to 22:57Z; ledger `harvst-cf4-gold-rebuild-20261017` CLOSED, commit `413e7d0581`; proof VALID rc 0 (re-run by me); order closed `d495d3d763` |
| `HVST-ce-5` | the gateway wording release | SUPERSEDED (the CTO deferred it, msg 7727); carried in `ledger/ROUND91_CARRIED_FOR_NEXT_GATEWAY_RELEASE.md` |

Under a never-widen pair (COO half `275d5739...95b0`; CTO half `8a5ea52464`, C-1 to C-10). Site Z was told first (its CTO, msg 35561: no rebuild in flight, window 22:00Z to 00:00Z); I also read the four AMGT_RESAPP `bt` orders it named (none touches harvest gold).

## 2. The real runs

- **Manifest** (`cf4_written.out`, re-read by me): 34 WROTE lines, 34 distinct keys, 34 VersionIds, every put new (`existed=False`), 17 continuation and 17 dossier, equal to the signed list (`221a63c3...ee48`), none missing or extra. The VersionIds are the rollback key list.
- **Served by my own session (live gateway), after the last write:** `MNST_US_Equity` fund absent ("no stated holding line: the lines found are candidate, template or unclassified"), position `CANDIDATE FOR PFOE`, stance candidate, `fund` null, `candidate_fund` `PFOE`; `ML_FP_Equity` fund absent, position `[BUY IN IDVZ TO X%]`, stance template; `CLX_US_Equity` fund absent, `Candidate for DIVZ`, stance candidate; the control `UNH_US_Equity` unchanged (fund `PFOE`, `line_only`, `Maintain positions in PFOE and DIVZ`).
- **By SC1 (`cf4_served.out`):** canary MNST and `8306_JP` (position absent), then `8316_JP`, `8766_JP`, `9433_JP`, `8035_JP`, `CELH`, `ST_SP` (fund absent, the expected position); the controls UNH and `CPA_US_Equity` equal to their reading before. 10 reads in all.
- **Each name** ran as one foreground unbuffered command with the manifest checked before the next (the CTO's rule after round 90's driver death); no stop, no put error, 34 of 34 builds equal their census line.

## 3. What is NOT established

- **7 of the 17 names** were checked at build and at the put, not read served. SC1 read 8 served (`MNST`, `8306_JP`, `8316_JP`, `8766_JP`, `9433_JP`, `8035_JP`, `CELH`, `ST_SP`); I read `MNST`, `ML_FP` and `CLX`, so 10 of 17 are read served.
- **The silver field is not moved (row `D1-S46`).** `harvest_get_research` still returns `research_reports[].fund` = the fund token of a candidate or template line (`MNST` `PFOE`, `ML_FP` `IDVZ`, `CLX` `DIVZ`): `typed.py::_find_fund` takes the first fund token whatever the verb. Any consumer of that list reads a fund the name is not held in. Not read: how many silver rows, and whether the portal reads the field.
- **The `fund_form` object** (`fund_form.gather_items`, corpus-wide) is not rebuilt: `HVST-cf-3` (code) and `-5` (rebuild) are defined and held behind `cf-4`, because changing `gather_items` makes every dossier build find no stored fund form until new ones are written.
- **The `ce-3` wording** is merged, not served (needs a gateway release).
- **Rollback is an Andrew-confirmed S3 delete** of the manifest keys; the halves say so; nothing was deleted.

## 4. My errors and decisions, corrected in the record

- **C-S61 (mine, round 90):** reading the round-90 census I took "CANDIDATE FOR ..." lines for stated positions; nine names were served a `fund_of_record` from them from the `ce-4` writes (17:30Z) until the `cf-4` canary (22:05Z), about four and a half hours. Named in decomposition section 121 and in the `cf-4` pair; fixed by `cf-2` and `cf-4`.
- `cf-2` first pass claimed a stance on lines naming no fund (`BABA`, `SHOP_CN`, `WALMEX*_MM`); AMENDMENT 2 restricted it. A census rerun read `HEAD` as its baseline and saw no change; the baseline is pinned to `dca8722353`. A fixture (`Buy IDVZ`) contradicted an acceptance criterion; the fixture changed.
- I chained a worktree teardown after a refused merge in one command (the commits survived on the branch).
- The `cf-4` GO message to SC1 was refused at 155 words (the cap is 150) and resent; no effect on the run.

## 5. The rows

Mine: `D1-S46` (the silver field; OBSERVATION, INERT, UNDER_INVESTIGATION: for the CTO's ruling), `D1-S47` (dismisses the ARMED `D1-W159-S1`, the `ML_FP` template, on my served read). `D1-S43` and `D1-S44` (the driver death, cause unknown) stand. Workers' INERT notes for you: `D1-W159-S2` onward, `D1-W160-S1` (BLOCKING, INERT: the AC2 conflict resolved by AMENDMENT 2) and `-S2`; round 90's and 88's notes are still open for you. `comp-surprise`: ARMED 0.

## 6. For the slug

1. **The silver `research_reports[].fund`** (row `D1-S46`): re-derive it from a holding line only, or drop it for a non-holding line; it needs a silver rebuild of the affected reports, so a never-widen pair.
2. **`HVST-cf-3` and `-5`:** the `fund_form` code change and its rebuild, in that order, with every dossier build held between them.
3. **`HVST-ce-5`:** the `ce-3` wording on the next gateway release, after a host-owner notice.
4. **`line_only` text:** recover a wrapped sentence from the extraction's `section_leads`.
5. **Long unattended write runs:** one foreground command per name with the manifest checked is now the rule (row `D1-S44`); whether to make it a tool.
6. The standing candidates of `ledger/ROUND88_ENRICHMENT_CANDIDATES_20261017.md`.

-- 2.0.0_SA_COO~W1
