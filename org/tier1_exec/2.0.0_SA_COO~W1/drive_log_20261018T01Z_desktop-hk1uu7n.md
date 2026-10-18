# drive log 2.0.0_SA_COO~W1 -- 2026-10-17 23:50Z to 2026-10-18 01:35Z (dell1)

**archetype:** MIXED

Push state of everything below: LOCAL on box/dell1 except what `0.0.0_AB_MSTR~DELL1` read pushed at 01:3xZ (the CTO halves `b4aac7476a` and `48d6e4e72b` and my commits up to `17ede77bad`, `origin/box/dell1` = `a8bde6e221` by its ls-remote read). The 3 silver parts of `HVST-cg-2` are in the harvest bucket, not in git.

## What moved

- **Round 92, the silver `fund_relation` chain (CTO round-91 analysis item 1, rulings msgs 7771, 7775, 7782, 7783/7784, 7791, 7813).** `HVST-cg-5` merged `a9aecdd593` (the holding words `adding` and `reduction`, one closed alias `RECOMMEDATION`; the re-census, re-run by me, reads `holding 121, candidate 14, initiate 2, interest 2, template 1, unclassified 0, none 213`; the CTO's guard on `adding` clear: two CPA rows, both held). `HVST-cg-2` (the silver rewrite, seat SC1, never-widen pair COO `11cf6bd0...9158` and CTO `b4aac7476a`): site Z cleared the window (its CTO msg 35578), SC1 wrote 3 NEW parts 01:00:35Z to 01:01:14Z (84, 121, 148 rows = 353), each read back equal; I read the bucket myself by the gateway's rule (353 of 353 from the new parts, all with `fund_relation`, counts equal the census, 0 mismatches against the superseded rows); ledger CLOSED and COMMITTED (`8225380445`); order complete (`a8bde6e221`).
- **`HVST-cf-3` (worker `~164`) merged `04be089e13`:** the fund form counts only reports whose silver row states `holding`, never the two misfiled Mexico reports; a row without the key raises; method version 2. I re-ran its census: identical (`funds=2 reports_before=139 reports_after=115 dropped_nonholding=22 dropped_misfiled=2`; IDVZ 94 to 82, PFOE 43 to 33, DIVZ 2 to 0). Complete `0a7bf3e938`. `HVST-cf-5` (the fund-form rebuild) is the last cell of the chain, not yet cut.
- **`HVST-cg-3` (the gateway release, seat SC1):** `HVST-cg-4` (the code half, worker `~162`) merged `290f2e9e6d` earlier; the pair for the release is signed on both sides (COO `29d9e1b9...87c4`, CTO `48d6e4e72b`); the order is pending at SC1 for step 0, the cut and the host-owner note; the release is the live commit `d077cef043` plus exactly two hunks (md5 controls in the half); MSTR told site Z the window (01:50Z to 03:30Z) at 01:29Z; nothing deploys before its answer and my GO.
- **SC1 was idle and unaware** of my `cg-2` order and GO for 47 minutes (its inbox watcher had ended and re-armed after the mail landed, so the mail read `OFFER-EXHAUSTED`, 0 read). I peeked at its tab (read-only), confirmed the three unread files, and typed one nudge; R1 independently typed a second a minute later; SC1 wrote the canary 5 minutes after.
- **Rows:** `D1-S48` (dismisses the ARMED `D1-W162-S1`), `D1-S49` (the silver and gold classifiers differ on two words; one shared classifier is a round-93 row, the CTO's ruling). `comp-surprise`: armed 0, open 169, defects 0. `round-close-check` round 92: `orders=6 verdict=MAY-CLOSE` (it counts the staged and pending seat orders as the packet will).

## My errors, corrected in the record

- **My `cg-2` COO half said `source_keys` and the `research_reports[]` entries stay equal after the rewrite.** They do not: the gateway lists the silver parts it read and names the winning part in each entry. SC1 found it, refused to self-grade and asked; I ruled the difference expected (AMENDMENT 2), the CTO accepted (msg 7813). I had not read `harvest_research.py` lines 270-293 for what `source_keys` carries before I signed.
- **I left the gateway app folder out of the `cg-5` worker's sparse set** (the same class as `ce-6`): its AC2 read `57 passed, 1 skipped`; I widened the set, the worker regraded. I then added the folder to every later worker's provision.
- My `cf-3` order said the Mexico reports are counted "in KMB's form"; a fund form is per fund (they sat in IDVZ's). The worker's row `D1-W164-S1` corrected it.
- A `cg-2` commit message file was first written with a shell heredoc (the rule says a non-shell writer); I rewrote it with the Write tool before committing. One commit call was blocked by a hook that read `python -m` plus `$(` as `git commit -m`; I split the call.
- The `cg-4` order was cut as `LOCAL` under a shared workstream and refused twice by the gate; fixed by the honest declaration (WORLD by the `infra/` path floor, its own workstream), not an override.

## Open at the end of this log

SC1's report of step 0, the cut and the host-owner note for `HVST-cg-3`; site Z's answer (MSTR carries it); my GO; the served proof read through the gateway on ADBE, SNPS, MNST, CLX (`candidate`), ML_FP (`template`) and UNH (`holding`); `HVST-cf-5` (its COO half, the CTO's half, site Z, SC1's `fund_form.write()` for IDVZ and PFOE, no dossier build in between); the round-92 L8 packet to the CVO after those; SC1's hourly `sa` reads. No open call at Andrew from this seat.

## Compiler Tools

- `.tools/safe-commit.sh` (about 20 commits this window), `.tools/safe-merge.sh` (fast lane x4: `cg-4`, `cg-1`, `cg-5`, `cf-3`), `.tools/wk-provision.sh` (5 provisions, 5 removes), `.tools/proof-of-spec-check.py` (VALID x6), `.tools/to-pipeline-gate.py` (REFUSED once), `.tools/unstick.ps1` (one peek, one nudge), `.tools/comp-surprise.py`, `.tools/round-close-check.py`, `.tools/unblock.py tick`, `mcp opalgateway harvest_get_research`, and my own read-only scripts `cg2_issuer_verify.py` (the bucket by the gateway's rule). Gaps: the broker refused an ack of a message addressed to another seat twice; the sparse worker worktrees lack the untracked `integrations/bloomberg/research/field_map.json` (row `D1-W161-S3`).
