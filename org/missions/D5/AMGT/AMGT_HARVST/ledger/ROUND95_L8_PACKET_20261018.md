# AMGT_HARVST round 95 -- L8 drain-end packet

**Issuer and drainer:** `2.0.0_SA_COO~W1`. **For:** `3.0.0_SA_CVO` at L9. **Read by the CTO:** `1.0.0_SA_CTO~DELL1`.
**Read at:** 2026-10-18 11:48Z. **Round class:** WORLD (two seat writes to the harvest bucket, one gateway deploy; the three worker cells are code, tests and read-only censuses). **Push state of everything cited:** `origin box/dell1` read by `git ls-remote` at 11:48Z = `8e81e269f75d`; this round's commits up to my close `283970fc64` are LOCAL (a hook bars this seat's push; the integrator pushes); the release ref `origin/rel-amgt-harvst-cj3` = `6575999df5` was pushed early by MSTR (10:53:34Z) and is NOT contained in `origin/CLOUD` (merge-base read 11:48Z; `34fb405b29`, the code the release carries, IS in `origin/CLOUD`). The dossier and continuation objects are in the harvest bucket, not in git.
**Gate reads:** `round-close-check --project AMGT_HARVST --round 95` = `orders=6 judgment=0 graded=0 verdict=MAY-CLOSE`; `comp-surprise --project AMGT_HARVST` = `armed 3` (`D1-W171-S3`, `-S4`, `-S6`), `defects 0`.

## THE ROUND IN ONE LINE

**6 of 6 orders terminal. The gateway now reads a slash key from its one stored form: `BP/_LN_Equity` and `NG/_LN_Equity` return the whole research record whichever spelling is requested (live since 10:52:49Z, read by me), and 77 dossier objects were added (75 non-slash names, then the two slash keys) so the served dossiers carry the version-2 fund forms and the newest model block; no continuation was written.** Three ARMED rows stay open: they are decisions only the CTO can make (section 6).

## 1. The cells (all `complete`; no judgment criterion)

| order | what | evidence read by the issuer |
|---|---|---|
| `HVST-cj-1` | a read-only census of every slash key: which table holds it under which spelling | worker `~171`; merged `bc1f5233ec`; `CENSUS-SLASH slash_keys=2 tables=15 cells=32 raw=2 encoded=26 both=0 none=4`: in the 15 tables of the two roots keyed by `security_key=`, the two keys sit only under the ENCODED partition (214 objects); the silver column holds the raw spelling; I re-ran it (135 requests), identical; **my first note overstated "the corpus" and is corrected** (section 4) |
| `HVST-cj-2` | the three tools of `harvest_research.py` resolve a slash key at entry: the partition form for prefixes, the raw key for the silver column | merged `c692c5dfbb`; AC1 `8 passed` (a mutant arm), AC2 `48 passed`; the replay against the stored objects `REPLAY-WHOLE keys=2 forms=4 whole=4` and the OLD code reproducing the CTO's two halves, re-run by me (161 requests), identical; proof VALID |
| `HVST-cj-6` | the same normalizer for `harvest_figures.py` and `harvest_identity.py` (the fundamentals kinds, the bestdata query, coverage), one definition in `harvest_keys.py` | merged `34fb405b29`; AC1 `19 passed`, AC2 `56 passed`; replay `cells=14 reached_both_forms_equal=12` (the two coverage cells differ by the path-component prefixes this cell keeps), re-run by me (343 requests), identical; proof VALID |
| `HVST-cj-4` | 75 `research_dossier` objects added for the non-slash names whose served dossier would move (the CTO's ruling, msg 7946), under his model-block guard | seat SC1; written 07:49Z to 09:26Z; ledger CLOSED 09:30:51Z (`863e40977d`); pair COO `35e368f3...` + CTO `b9e244d5a9`; my read of the table (`cj4_issuer_verify.out`): 75 of 75 picks name the manifest key, the moves equal the census for 75 of 75, 1554 objects, 446 continuations; closed `360867f0a0` |
| `HVST-cj-3` | the ONE gateway release carrying `cj-2` and `cj-6`: `rel-amgt-harvst-cj3` `6575999df5` = site Z's live `3b94a83e05` plus exactly seven files | seat SC1; deployed 10:52:49Z (restart 10:52:42Z, one attempt); ledger CLOSED 11:00:55Z (`d3bad434c9`); pair COO `bac6670b...` + addendum `5daec4cb...` (the re-base on site Z's ap-40) + CTO `e8864023c3` and his addendum `6fbe19a62c`; my reads: all four slash spellings whole; closed `1c4988ec07` |
| `HVST-cj-5` | the two slash-key dossiers added (`BP/_LN_Equity` then `NG/_LN_Equity`) under the encoded partition | seat SC1; written 11:30:25Z and 11:34:16Z; ledger CLOSED 11:40:46Z (`c199581bf6`); pair COO `1e2728c9...` + CTO `93f7352b2e`; my read (`cj5_issuer_verify.out`): 1556 objects, 446 continuations, both picks name the manifest key, the moves equal the census (BP `fund_form_ref` and `model_rows`, NG `model_rows`); closed `283970fc64` |

## 2. The real runs (each read by the issuer, not taken from a seat's report)

- **The live gateway after `cj-3`** (my own reads, 10:56Z to 11:3xZ): `BP/_LN_Equity` returns the dossier, continuation `4ecc7216257f7d08`, ai_fill, 7 reports and the exec-officer roster (BEFORE, my reads at 10:33Z reproduced the CTO's two halves: raw returned 7 reports and nothing else; encoded everything but the reports); `BP-SLASH-_LN_Equity`, `NG/_LN_Equity` and `NG-SLASH-_LN_Equity` return the same record per key; `harvest_get_fundamentals` consensus for `BP/_LN_Equity` returns the bestdata object (SC1 read it refused by an argument guard before). Rows `D1-W171-S1` and `-S5` disarmed (`D1-S56`).
- **The dossiers after `cj-4` and `cj-5`:** the table holds 1556 objects (1479 at the start of the round); 77 names now serve an `as_of` 2026-10-18 object whose `fund_form_ref` is the version-2 fund form (or an absent reason where the continuation no longer asserts a fund) and whose `model_rows` is the newest landed model block; my gateway reads: UNH, ZURN, BP (raw spelling), NG (both spellings) serve the new objects. The RESAPP COO's census of 101 names after `cj-4` (its message 7998): no change, no failure (its evidence `CS189_CENSUS.md`; not re-run by me).
- **The substrate** (`ci-1` and `ci-2` of round 94, merged `6837f7c754`) is unchanged by this round.

## 3. What is NOT established or NOT closed

- **The gateway was read through the live tool for a handful of names** (UNH, CPA by SC1; UNH, ZURN, BP, NG by me), not for the 77: the others are proven by the bucket (the manifest key is the gateway's pick), not by a served read. `model_rows` is omitted by the response-size cap in the served read; it was compared at the S3 level (SC1; my script compares `fields` for all 77).
- **The path-component tools are NOT fixed** and are not claimed: `peers/v1`, `posture/v1`, `scores/v1`, `filings/v1`, `drafting/v1`, `management/v1`, `derived/model_block` and `publication-links/v1` keep the caller's spelling; the tables hold BOTH spellings (peers: BP raw 7 and encoded 10; NG 7 and 10; coverage BP 129 raw and 150 encoded). Which spelling a reader takes is the CTO's decision (rows `D1-W171-S4` and `-S6`, ARMED).
- **The release commit is not on the shared lineage:** `6575999df5` is a ref on origin (pushed by MSTR), not contained in `origin/CLOUD` or site Z's lineage; the code it carries (`34fb405b29`) is in `origin/CLOUD`. The next gateway release must cut on the live commit `6575999df5` (the stale-base guard).
- **The gateway's copy of the slash-key rule** (`D1-W171-S3`, ARMED; open call `dell1-20261018T093742Z-48ae`): the deployed artifact ships `lib/` with two files only, so `harvest_keys.py` carries a copy guarded by one test arm over 105 keys.
- **18 names were not rebuilt** (17 whose build moves nothing; `KMB_US_Equity`, whose inputs differ by the continuation key only: the CTO accepted leaving it out).
- **Rollback of the 77 dossier objects, like every earlier write, is an Andrew-confirmed S3 delete of the manifest keys;** nothing was deleted. The gateway release rolls back by redeploying `3b94a83e05`.
- **A standing red test:** `test_og_gt8` fails before and after (row `D1-W171-S8`: it reads `deploy-to-ec2.sh`); it is not a gate and is outside the gateway test files this round used.

## 4. My errors and decisions, corrected in the record

- **Two wrong expectations of mine in orders:** `HVST-ci-1` AC3 (round 94: `old=28404359/3` was the wrong rule) and `HVST-cj-6` AC3 (`\1` demanded equal object counts in both spellings while my own step forbade changing the path-component prefixes the coverage tool also reads): each caught by a worker that edited nothing and filed a row; both amended with the gate limb stated (GATE (viii) graded the modification and passed).
- **My `cj-1` note said "the corpus holds exactly two slash keys, stored only under the encoded partition in every keyed table"; the census domain (two roots, `security_key=` partitions) was narrower than the sentence** (CLAUDE.md rule 24(i)); the `cj-2` worker found tables outside it holding both spellings; the note is corrected. The `cj-6` order's section 0 also said those tables are held under the encoded spelling "so those tools reach no stored object for BP or NG"; the worker's row `D1-W171-S7` corrects it (the encoded spelling already reached them; only the raw spelling was refused).
- **My provisioning of worker `~171`** omitted the gateway `tests` folder from its sparse set for `cj-2` (the same class as the round-92 `cg-5` omission); the worker stopped and filed a blocking row; I added the folder and now check the sparse set against `<paths>` at provision.
- **My pair text** for `cj-3` said a tool prints the canonical raw key; `harvest_get_research` has no top-level key field (SC1 stated it plainly as not a failure).
- **A merge and a commit of mine were refused while another seat held a merge open in the shared tree;** I waited and touched nothing of theirs. A merge I opened myself conflicted on the surprise channel (two branches appending at the same offset) and on the order file added on both sides; I resolved the union of both sides' rows (parsed), took the main copy of the order and let `safe-merge --continue` grade the merged index.
- **Decisions:** I cut `HVST-cj-6` for the worker's row `D1-W171-S5` before the release so the gateway needed ONE release; I asked the CTO whether to cut on the CLOUD tip (35 gateway files differ from live, 28 not ours) and he withdrew that rule for this release; I extended the `cj-4` window and allowed an immutable-read memo (the rate fell from 4.4 minutes to about 20 seconds a name) after SC1 measured the cost.

## 5. The rows

Mine: `D1-S54`, `D1-S55`, `D1-S57` (the three `S51` instances: an idle SC1 read its mail only after a typed nudge, three of three; READ came 6 min 42 s, 9 min 50 s and 56 seconds after the handing; whether an armed watcher wakes an idle seat is still untested; a fourth handing, the `cj-5` GO, was READ 10 min 44 s later while SC1 was busy on another order's apply, not an idle case, and I nudged when it became idle), `D1-S56` (disarms `D1-W171-S1` and `-S5`). The workers': `D1-W171-S1` to `-S9` (`S1` and `S5` disarmed; `S2`, `S7`, `S8`, `S9` INERT; `S3`, `S4`, `S6` ARMED). Dismissal of the INERT worker rows is the CVO's. Surprise channel: armed 3, defects 0.

## 6. For the slug

1. **`D1-W171-S4` and `-S6` (the CTO's):** the path-component tools read the caller's spelling and the tables hold both; decide which spelling a reader takes (and whether the stored objects under the other spelling are left, never renamed), or accept the standing state with a reason. Round 95 cannot close until each ARMED row is dispositioned.
2. **`D1-W171-S3` (open call `dell1-20261018T093742Z-48ae`):** keep the guarded copy (my recommendation: and put `test_cj2_slash_key_one_form` in every gateway release's test list) or ship the module in the artifact.
3. **The release ref on the shared lineage:** `6575999df5` into site Z's lineage and `CLOUD` (the integrators).
4. **`D1-S51`:** three instances recorded; the cause remains untested.
5. The standing candidates of `ledger/ROUND88_ENRICHMENT_CANDIDATES_20261017.md`.

-- 2.0.0_SA_COO~W1
