# J359 addendum 2: satellite trailing returns = models blended with GLD, served and on PROD -- 2.0.0_SA_COO~J1

**archetype:** MIXED
**tag:** adhoc-remote-job
**Date:** 2026-10-14
**Task Order:** ad-hoc remote job J359 (second attempt of work on the same job; the MSTR holds the job open, attempt 1); deploy leg `ADHOC.j359-addendum2-satellite-returns-deploy`, promote leg `ADHOC.j359-addendum2-footnote-deletion-promote`
**Status:** COMPLETE (the reviewer's grade and the requester's check are the MSTR's)

---

## Objective

After the first close note, Andrew changed the satellite trailing-returns rule (CRO spec addendum 2 @`0c6d3d2f94`): the weighted average of the
underlying Opal models' realized returns, blended with GLD at its weight, no holdings backcast, and only the two sentences describing the
old method deleted from the page. He then confirmed the formula, approved the deletion, and asked for one PROD promote carrying it with the
TRSB Excel fix.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-rail (hook) | a grep over `*.ts` and a `grep -r` | PARTIAL | denied once with a RUN NEXT; I used the native Grep tool, which the rail admits |
| `.tools/naming-gate.py` (via safe-commit) | producer commits | PASS | the new S3 key literal passed because the CRO's legacy-address row `724b84f846` was already on box/dell1; a worktree based before it would have refused |
| `.tools/open-calls.py` | `approval-status`, `add --check-only`, `add`, `hold`, `close --by andrew` | PASS | the held row closed on Andrew's recorded word |
| `.claude/skills/ui-walk/walk.mjs` | `--probe-get` on the served satellites route | PARTIAL | 200 at 45645 B = the new object; no 2xx body kept, so identity by size; used another seat's dev-live server on 5174, GET only |
| `verify_producer_returns.py` (own) | difference control, oracle, null-GLD arm, negative controls | PASS | the old side is read from the deployed pin `efb3f6550f`, never HEAD |

**What worked:** exact-key S3 reads; the old-versus-new difference control against the deployed commit; reading the registry-literal gate before committing; verifying a "string absent after deploy" control by first reading it present.
**What failed:** the send gate refused three of my messages to Tier-2 seats (no order path cited, or an ask marker in information text); I re-sent each with the order path or as plain information. I parked the DT promote for a 21:00Z restart that Andrew had already held; the CTO and MSTR told me and I un-parked it within minutes.
**Gap found:** none new (the CRLF line endings in a portal worktree defeated my first scripted edit; fixed by detecting them).

---

## Work Completed

### 1. The producer
`build_satellites_characteristics.py` @`7337fdfa6d` (origin `wk-remote-J359b`): `R(w) = (1 - g) x sleeve-weighted model returns + g x GLD return`, models from the Model Portfolios benchmarks object. Never-widen pair: COO half @`5500bce348`, CTO half @`675488ce32` (C1 to C5). Deployed by `0.7.0_AE_CloudOps~DELL1`: served `characteristics.json` VersionId `Qh56dS_IliDOh0owKxjToBgEjgJ0pb8v`, 2026-10-14T20:15:50Z (prior `6z8c7qDD...`). Landed on box/dell1 @`bc78b9c53e` (LOCAL) with its POSN_ASTTAX provenance record.

### 2. The reads (mine)
72 of 72 return cells equal the addendum table; Satellites 90 and 98 equal the served ULT returns 8 of 8; tickers block, input notes, scalars, totals and sources unchanged; coverage absent; 0 partial-sleeve windows; GLD 0 of 8 windows moved (AE read). Served route signed in as the walker: 200, 45645 B (old 66835). Not read as a CW login.

### 3. The portal
`cand/dell1/satellite-returns-method` @`714f8e48c8`, one commit on PROD `5ab67a651a62`: deletes the hypothetical disclaimer and the exclusions footnote, and the builder code that only fed the footnote. Andrew: "go ahead with the deletion" (record `ANDREW_DIRECT_20261014_J359_ADDENDUM2_DELETION_GO.md` @`50234ae112`); row `dell1-20261014T202134Z-fbdf` closed approved by andrew. Promoted by DT~H1 with the TRSB fix as one release on Andrew's word: DEV `e578b378d3`, PROD `5d6464189120`, tag `portal-v2.1.222`, CI run 38637040693 success. I verified: PROD head by `ls-remote`, the three candidates (factsheet `6e69a05e43`, deletion `714f8e48c8`, TRSB `040b152f41`) are ancestors of PROD, `gh run view` conclusion success on that sha. DT's bundle read: before `holdings at today` 1 and `download_url` 0, after 0 and 1, chip and Trailing Returns present, negative control 0, 62 files read.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Builder code for the exclusions footnote removed with the footnote | dead once the footnote is gone; no visible change |
| Used the comma form for `--features` | the release builder's own usage line gives it; the CTO's message wrote it space-separated |
| Did not register the deletion row before the served read | the CTO's C5 held it for Andrew's word after the read; a promote first would have shown old figures without a disclaimer |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/assets/scripts/gold/build_satellites_characteristics.py` | models blended with GLD | Yes `bc78b9c53e` (LOCAL on box/dell1) and `7337fdfa6d` (origin) |
| `org/missions/D4/POSN/POSN_ASTTAX/ledger/J359_ADDENDUM2_SATELLITE_RETURNS_PRODUCER_PROVENANCE_20261014.json` | landing record | Yes `bc78b9c53e` |
| `org/tier1_exec/2.0.0_SA_COO~J1/deliverables/` (COO half 2, evidence `J359_evidence2/`, the two Andrew-direct records) | the pair and its proofs | Yes, origin `wk-remote-J359b` @`5500bce348`; the records on box/dell1 |
| the two ADHOC orders (AE deploy, DT promote) | orders and amendments | Yes, LOCAL on box/dell1 (`5598c3f766`, `ab66c8b6e0` to `2ab8ecb074`) |
| portal `src/components/{SatelliteFactsheetSections.tsx, satelliteFactsheet.ts, satelliteFactsheet.test.ts}` | the deletion | Yes, on PROD `5d6464189120` |

---

## Blockers

None. Commits on box/dell1 are LOCAL until `box-sync` pushes them.

---

## Current State

The satellite popup on PROD shows the factsheet with the models-blended-with-GLD trailing returns and no method footnotes; the served `characteristics.json` is VersionId `Qh56dS_I`; PROD is `5d6464189120` (tag `portal-v2.1.222`) with the TRSB fix. Both of my worktrees are removed (junction unlinked first, real `node_modules` checked intact); branches `wk-remote-J359`, `wk-remote-J359b`, `cand/dell1/satellite-factsheet-prod` and `cand/dell1/satellite-returns-method` stay on origin because the records cite them. My dev server on 5174 is stopped.

---

## Next Steps

1. **Requester's check** -- Yang Liu / CW open each satellite popup on Positioning.
2. **MSTR** -- the reviewer's grade, then `remote-job.py complete` with the final evidence, then the close word.
3. **Stand down** after the MSTR's close word.
