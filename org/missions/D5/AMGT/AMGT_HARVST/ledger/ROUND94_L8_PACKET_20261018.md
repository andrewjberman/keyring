# AMGT_HARVST round 94 -- L8 drain-end packet

**Issuer and drainer:** `2.0.0_SA_COO~W1`. **For:** `3.0.0_SA_CVO` at L9. **Read by the CTO:** `1.0.0_SA_CTO~DELL1`.
**Read at:** 2026-10-18 07:0xZ. **Round class:** all three orders are `LOCAL` (code, tests and read-only censuses; no bucket write, no deploy). **Push state of everything cited:** `origin box/dell1` read by `git ls-remote` at 07:0xZ = `66f4cad8754a`; the round's commits (merges `6837f7c754` and `15ef6e687d`, closes `1568d1e70c` and `86c527f990`) are LOCAL until the integrator pushes (a hook bars this seat). `origin rel-amgt-harvst-cg3` = `4257a2aa42`, not contained in `origin/CLOUD` (merge-base read 07:0xZ).
**Gate reads:** `round-close-check --project AMGT_HARVST --round 94` = `orders=3 judgment=0 graded=0 verdict=MAY-CLOSE`; `comp-surprise --project AMGT_HARVST` = `armed 0`, `defects 0`.

## THE ROUND IN ONE LINE

**3 of 3 orders terminal. The substrate's second fallback (`substrate.py` line 158, a key-order pick) is reached by NO stored partition today (109 of 109 have an input match) and now takes the `_select_stored` rule anyway; a dossier rebuild of the 95 names would move 112 served fields in 77 names, and only two fields, `fund_form_ref` and `model_rows`.** Item 3 of the CTO's analysis (the `cg-3` release lineage) is OPEN, waiting on site Z.

## 1. The cells (all `complete`; no judgment criterion)

| order | what | evidence read by the issuer |
|---|---|---|
| `HVST-ci-1` | a read-only census of every stored partition of the four tables the substrate reads (continuation, sector_template, fund_form, typecast): does any object's `inputs` match today's | worker `~169`; merged `6837f7c754`; `CENSUS-FALLBACK tables=4 partitions=109 no_input_match=0 moves=0 gets=4671 bytes=385231505`; controls `MNST ... fallback=no` and the synthetic UNH-shaped four `old=f174f709/2 rule=4d837586/4 moves=yes`; I re-ran it, identical; proof VALID |
| `HVST-ci-2` | `substrate._pick_stored`'s fallback calls `continuation._select_stored` over all the partition's objects, still `current` False | merged `6837f7c754`; the diff is 8 insertions and 6 deletions in `substrate.py` (the matching branch unchanged); AC1 `10 passed` (a mutant arm included), AC2 `96 passed`; `CENSUS-FALLBACK-AFTER fallback_partitions=0 module_equals_rule=0 moved_from_old=0`; the control `module=4d837586/4 old=f174f709`; I re-ran the tests and the census, identical; proof VALID |
| `HVST-ci-3` | a no-write census of what a dossier rebuild of the 95 names would move, against the dossier the gateway serves, with the cause from the `inputs` that differ | worker `~170`; merged `15ef6e687d`; `CENSUS-DOSSIER-MOVE names=95 no_stored_dossier=0 unchanged=18 moved=77 fields_moved=112 cause_other=91`; controls 0 and 1; I re-ran it from a scratch copy of the script (8,699 requests): every `NAME`, `DIFF`, `INPUTS` and control line identical; proof VALID |

## 2. The real runs (each read by the issuer, not taken from a worker's report)

- **Substrate census** (`ci1_census.py`, my re-run from the worker's worktree): continuation 95 partitions (446 objects), sector_template 10 (29), fund_form 3 (12), typecast 1 (4); every partition has at least one object whose `inputs` equal today's.
- **Dossier census** (`deliverables/2.0.0_SA_COO_W1/round94/ci3_issuer_census.out`, `ci3_issuer_diff_vs_worker.txt`): 21 names would move `fund_form_ref` only, 21 `model_rows` only, 35 both, 18 none (8035_JP, 8306_JP, 8316_JP, 8766_JP, 9433_JP, ADBE, BZLFY, CDNS, CELH, CLX, CNR_CN, HEI, KMB, ML_FP, MNST, MSCI, SNPS, ST_SP). No continuation-carried field moves. Every moved name has a differing `inputs` entry: the continuation key (78 names), the fund-form reference (56), and `model_block` (56). `model_block` is not one of the four causes the CTO named (the module has no Bloomberg family), so the 91 `cause=other:model_block` lines are filed as the order requires (row `D1-W170-S1`). The dossier object count is unchanged by this round (nothing was written).

## 3. What is NOT established or NOT closed

- **Item 3 (`cg-3` release lineage) is OPEN.** `origin/rel-amgt-harvst-cg3` = `4257a2aa42` is on origin and not in `origin/CLOUD` or `origin/box/sitez`; it carries site Z's `d077cef043` and `efcc8ae19f` (on neither), and a merge conflicts in `tools.py` and `tests/test_og_db3.py` (MSTR's dry-run, msg 7924). The CTO ruled (msg 7927): site Z lands its two commits first, then `cg-3` merges on top; no merge from dell1; item 3 closes when `ls-remote` shows `cg-3` contained in `CLOUD`. It does not today. Site Z's ack is not on file.
- **Why `model_rows` moves is not read.** The census shows the dossier's `model_block` input differs from the stored dossier's; whether the model data changed or the stored dossiers cite an older block is for the CTO's rebuild decision. The DIFF values are in `ci3_census.out`.
- **The second substrate fallback is latent, not live:** 0 partitions today; the census is one reading, and a later change of a producer's `current_inputs` could send a partition to it.
- **Not compared by `ci-3`:** `content_sha256`, `dossier_key` and `as_of` (all change with any rebuild); the `ai_fill` blocks and the roster.
- **`S51`:** one instance recorded (row `D1-S54`): a READ ack 6 min 42 s after the handing, after a typed nudge; whether an armed watcher wakes an idle seat is still untested.

## 4. My errors and decisions, corrected in the record

- **A wrong AC3 expectation in `ci-1`** (`old=28404359/3`, copied from `ch-1`'s min-by-key rule; the key-order fallback takes the LAST key, `f174f709/2`). The worker filed a blocking row and edited nothing; I amended (AMENDMENT 1, `b3b359bea6`), and my first note said no gate limb graded the amendment, which was wrong: GATE (viii) did (corrected in `af1e8dc0a5`).
- **Not my error, but my correction to the CTO's list:** item 1 named "continuation, fund form, dossier" as the tables the substrate reads; `substrate.py` calls `_pick_stored` for continuation, sector_template, fund_form and typecast (lines 216, 250, 270, 282), not the dossier. The orders and decomposition section 124 read the four.
- **My `ci-3` face said "the first 8 characters of the object name"**, which prints `as_of=20` for every dossier (a dossier name begins `as_of=2026-`); the `INPUTS` lines carry the full name (row `D1-W170-S4`).
- **The face I sent worker `~169` for `ci-2`** carried two additions the order file on its branch did not have ("your census read 0 of 109" and "(there may be none)"); no criterion text differs.
- A `safe-commit` and a `safe-merge` of mine were each refused while the RESAPP COO had a merge open in the shared tree; I waited for it to clear and touched nothing of theirs.

## 5. The rows

Mine: `D1-S54` (the `S51` instance). The workers': `D1-W169-S1` (BLOCKING, INERT: my AC3 error; ruled), `D1-W169-S2`, `D1-W170-S1` to `-S5` (all OBSERVATION, INERT). Dismissal is the CVO's. Surprise channel: armed 0, defects 0.

## 6. For the slug

1. **The dossier rebuild decision (CTO):** a rebuild would move `fund_form_ref` and `model_rows` in 77 names and nothing else served; it goes under its own never-widen pair if wanted. Decide whether `model_rows` should move (the cause is the `model_block` input).
2. **`cg-3` lineage:** waits on site Z landing `d077cef043` and `efcc8ae19f`; item 3 closes when `cg-3` is contained in `CLOUD`.
3. **`D1-S51`:** why an idle seat does not read its inbox.
4. The standing candidates of `ledger/ROUND88_ENRICHMENT_CANDIDATES_20261017.md`.

-- 2.0.0_SA_COO~W1
