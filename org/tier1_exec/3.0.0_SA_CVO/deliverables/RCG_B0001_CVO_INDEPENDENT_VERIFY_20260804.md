# RCG B-0001 — CVO INDEPENDENT PROGRAM-LEVEL VERIFY

**Seat:** `3.0.0_SA_CVO~B` (provisioned for this verify; commission Andrew-ferried per R-0001/D-0002/D-0005)
**Date:** 2026-08-04 ~03:15Z
**Scope:** the full B-0001 chain — execute `099eb31879` → revert `48db734d1b` → re-apply `d1c3980c4a` — re-derived from commits and ledgers only; no claim accepted from the executor's (`4.0.0_SA_CRO`) or the gate seat's (`1.0.0_SA_CTO~B`) reports.
**Method:** scripted 26-check battery (git diff-tree/ls-tree/merge-base + ledger parses, denominators printed on every scan) + audit-trail corroboration. Verifier authored neither the batch nor the gate.

## VERDICT: CLEAN — 26/26 checks PASS, zero contradictions with the commissioned claims.

Effect per CTOB-RCG-001 s.7.2 item 3: this clean close discharges the outstanding **CVO precondition** on the ramp
(B-0001 had already discharged the REVERT precondition). Cap 500 moves from authorized-on-close to in force for
batch 2 by the ruling's own text — no further human step. Batch 2 drains the remaining ARCHIVE queue
(R-0023 denominator 2,944 − 93 executed = 2,851; the commission's figure re-derives exactly).

## Claims verified, each re-derived

**1. Execute `099eb318799d8bb283b5a4c2e266dd73e5e44fe2`** (author `4.0.0_SA_CRO~SWEEP`, 2026-08-04T02:07:23Z)
- `diff-tree --no-renames`: **93 D, 0 non-D** (A/M/C/R/T all zero). C1 held in the wild.
- Exact set equality with the ledger's declared 93, both directions: missing=0, extra=0.
- Parent is `67bbb6981d1838c0ff94e077131cb0a345f33ae2` as claimed. Shortstat: 93 files, **25,243 deletions** — matches the EXECUTED row's note verbatim.

**2. Revert `48db734d1b1d1bd8e8f12b594df7be8bb12c239f`** (02:08:53Z)
- **93 A, 0 non-A**; set-equal both directions.
- **Blob identity 93/93** vs the parent of execute: every restored path's git object id equals its id at `67bbb6981d18`
  (byte-identity by content-addressing), plus a scoped `diff-tree 67bbb6981d18 48db734d1b -- <cohort>` returning
  **empty** — the whole directory tree is identical, no extra files smuggled in.

**3. Re-apply `d1c3980c4ac66b1770dcbe14c13c9dbecca77ff3`** (02:11:34Z)
- **93 D, 0 non-D**; set-equal both directions.
- Cohort untouched between revert and re-apply's parent (`fec27f05e9`, scoped diff empty) — what was re-deleted is exactly what was restored.
- Ancestry ordered: `67bbb698` → execute → revert → re-apply, and re-apply is an **ancestor of HEAD**.
- Absence at HEAD verified on three layers: `ls-tree -r HEAD` = 0 tracked entries; index porcelain = 0; directory absent on disk.

**4. Ledger `rcg/ledger/BATCHES.jsonl`**
- **Append-only verified across all 8 committed versions** (each prior version is a byte-prefix of the next; worktree included). Not asserted from the schema note — exercised.
- 9 rows total, 8 for B-0001. All 7 path-carrying rows are set-equal (the archaeology's two honest corrections changed
  `reapply_commit`/cap prose, never the path set). `sha256_sorted_list` identical across all rows and **re-derived**:
  sha256 of the newline-joined sorted path list = `564dad6d…acc35`. Count field = 93 = unique paths.
- Final row's `cap_status` honestly records 100 IN FORCE / 500 authorized-on-close — the seam this verify closes.

**5. Labels (C4 re-derivation)** — `LABELS.jsonl` **at HEAD**, last-row-per-path (R-0022 semantics): **93/93 = ARCHIVE**,
0 absent. Denominator: 21,624 rows, 17,512 distinct paths (matches the program's stated corpus).

**6. Charter (C5 re-derivation)** — longest-prefix over `charters.yaml`: all 93 under `data/` → `{DATA, SCORE}`.
**0 PROTECT / APPEND_ONLY / EXCLUDE.** No more-specific charter key exists for the cohort (the glob-form keys are all
`org/`-side and cannot match). Firm fence respected: single-firm cohort (black_diamond only).

**7. Separation of duties, measured not read**
- `git log --all --author=4.0.0_SA_CRO~SWEEP`: **exactly 3 commits in existence** — the chain. The sweep identity has
  never authored anything else, on any ref.
- All 8 commits touching `BATCHES.jsonl`: authored by base `4.0.0_SA_CRO`, zero by `~SWEEP`. The executor never wrote
  its own authorization.

**8. Audit trail `org/rcg-sweep-audit.log`** — 4 PERMITs (02:05:20 execute / 02:07:27 execute / 02:08:57 revert /
02:11:36 execute), 8 DENYs. The one narrative gap I chased: the **extra 02:05:20Z execute PERMIT**. Corroborated
against `org/mass-deletion-audit.log`: `02:05:24Z BLOCKED … attribution=UNRESOLVABLE trailer` — the sweep gate
permitted and the independent mass-deletion gate then blocked the same commit on a malformed trailer; **no commit
landed** (proven by the exactly-3 sweep-author census above, not by absence of memory). Corrected-trailer retry
ATTRIBUTED at 02:07:30Z via `ledger-file rcg/ledger/BATCHES.jsonl`. Two gates composed; neither blinded the other.
The revert correctly produces no mass-deletion entry (0 deletions < threshold 25). The 02:10:04Z DENY is the C3
re-ratification protocol working as ruled (fresh complete RATIFIED row required for the re-apply leg — landed, then
02:11:36Z PERMIT).

**9. Rulings grounding** — R-0017 (data/* S1 ARCHIVE confirmed, deck_generation carve-out), R-0019 (batch-1
ratification incl. black_diamond diagnostics ARCHIVE), R-0020 (delegation, Andrew override retained, labels marked
`assessed_ratified_by_delegation`), R-0022 (last-row-per-path resolution law) all present in `rcg/rulings/RULINGS.jsonl`
and coherent with the batch's `citing_rulings`.

## Honest scope bounds

- "Byte-identical" rests on git content-addressing (object-id equality). I did not independently sha256 file contents;
  the ledger pins the path list, not content hashes. This is the same oracle R4 itself uses, and object-id equality is
  byte-equality by construction of the object store.
- The substantive rightness of the ARCHIVE labels is delegated ground (R-0020) — outside this verify by design; that
  residual is named in CTOB-RCG-001 s.9.1 and remains covered by Andrew's standing override.
- My charter check re-implemented longest-prefix matching over the read `charters.yaml`; the gate's own matcher was not
  re-executed by me. Consistent results on all 93; the two implementations were independent.
- s.9 residuals (gate not installed-by-default off the primary laptop; C7 covers the Python-package shape only) stand
  as recorded — pre-existing, not new findings, unchanged by this verify.

## Findings

None. Zero contradictions between the record and the commissioned claims. The two ledger corrections (wrong
`reapply_commit` captured from an un-moved HEAD; "cap lifts to 500" overstated then walked back to
authorized-on-close) were both **self-caught and superseded in-ledger before this verify ran** — archaeology, not
defects, and both re-derived here as correctly resolved.

— 3.0.0_SA_CVO~B
