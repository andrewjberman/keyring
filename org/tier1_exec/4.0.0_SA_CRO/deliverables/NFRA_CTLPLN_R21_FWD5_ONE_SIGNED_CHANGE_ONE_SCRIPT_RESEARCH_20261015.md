# NFRA_CTLPLN round 21, FWD-5 positive arm (WORLD): one signed change deploys exactly one script -- research

**Author:** 4.0.0_SA_CRO (laptop). **Measured:** 2026-10-15 15:1xZ-15:5xZ, workspace `box/laptop` HEAD after c13fc91edb
(gate fix D1-S8 merged). **Ask:** 2.0.0_SA_COO~C msg 109438. Read-only: no commit outside this file, no push, no
deploy, no AWS write. **Repo paths** are relative to `file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/`.

## Conclusion

1. **Script: `data/black_diamond/scripts/gold/diag_sleeve_fix.py`** (first choice), fallback
   `data/black_diamond/scripts/gold/validate_sl_nightly_gate.py`. Both are diagnostics in the gated bd gold tree that
   `gold_dispatch.sh` never names, nothing imports, and whose S3 object today equals the repo byte for byte (one version
   each, uploaded 2026-05-11). The signed change is a one-line docstring edit; the deploy is one `PutObject` of 4,161 bytes
   to `s3://opal-data-bd/code/gold/diag_sleeve_fix.py`.
2. **Blast radius: one S3 key plus one file on the bd gold runner's disk at its next sync; no execution, no served
   output.** The runner syncs the whole `code/gold/` prefix at 04:00Z daily (`bd-canonical-prices-daily`) and 23:00Z
   Mon-Sat (`bd-gold-nightly-fallback`), then runs only the scripts `gold_dispatch.sh` lists (24 at lines 100-121; the
   candidate is not among them, and no `*.py` glob executes). A diagnostic is never run by a schedule.
3. **Rollback per key:** `opal-data-bd` versioning is Enabled. Record the current `VersionId`
   (`3.yZFEuxxfxUOEMd.NRY7bZucaDccGX.`, ETag `56cb170f95c0b112a36a0ee3973d5473`) at L1; rollback is a copy of that version
   back to the key (no delete), or a second signed entry pinning the prior blob `0e4aec8d80`. If the runner synced in
   between, its copy refreshes on the next sync; nothing executes either copy.
4. **What the push may touch beyond the named script: measured ZERO today.** The hook's pinned-entry step
   (`.tools/git-hooks/pre-push-safe-deploy.sh:50-142`) runs on every push to `box/laptop` and would also deploy any
   other deploy-scope file an OPEN entry pins whose S3 bytes differ. Census at HEAD: 8 OPEN sentinels, 357 top-level
   deploy-scope scripts, **0 LEDGERED** (`.tools/deploy-ledger-names.py --rev HEAD`, all 357 paths). The one open bd
   entry pins `gold/lib/etf_classifier.py`, which the pinned-entry regex (`SCRIPT`, top level only) never admits.
5. **The one hazard to design around: the scheduled box-sync push.** `Opal box-sync` runs every 10 minutes on this
   laptop (`.tools/box-sync-schedule.ps1:30`, `$Every = 10`) and pushes `box/laptop` through the same hook. If U7's
   commit and ledger entry are on `box/laptop` when the slot fires before U7's own push, the deploy happens on MSTR's
   push, once, correctly, but not as U7's act. The cell should have U7 commit, open the entry and push in one
   uninterrupted step, and read `org/safe-deploy-bypass-audit.log` plus the S3 VersionId afterwards to prove which push
   deployed.

## The mechanism the cell exercises (read, not predicted)

| step | where | what it does |
|---|---|---|
| hook entry | `.tools/git-hooks/pre-push-safe-deploy.sh:144-230` | for `refs/heads/box/<this box>`: requires `AGENTBUS_DEVICE` = laptop (`:172-183`), bounds the deploy set to the box's diff against `origin/CLOUD` (`:184-198`, `crossbox-deploy-check.py --list-deployable`) |
| ledger gate | `:211-227` | `deploy-ledger-names.py --rev <tip>`: a path deploys only if an OPEN sentinel in `org/critical_paths/.open_deploys/` names the repo-relative path AND pins this build (blob id 10+ hex, sha256 of the blob, or a commit whose blob equals it; `deploy-ledger-names.py:20-45`). Everything else: `HELD-DEPLOY` row, push goes through |
| deploy | `:226` -> `.tools/safe-deploy.sh --no-pipescript <paths>` -> `safe_deploy_core.py` | `aws s3 cp` to `s3://opal-data-bd/code/gold/<name>` (CODE_TREES black_diamond, `safe_deploy_core.py:576` PIPELINE_MAP), MD5/ETag verify; `--no-pipescript` skips the comp-pipescript confirm in the hook; seat gates apply-who and crossbox are WARN (no `org/mcp/seat-gates.*` switch file exists) |
| pinned-entry step (D1-S8) | `:228`, `:50-142` | for every other top-level deploy-scope script at the tip, if an OPEN entry pins it at this build and the S3 bytes differ, deploy it too; absent object = differs; unreadable = HELD |
| integration | `:231-253` | the later `box-sync` push of `CLOUD` carries the box tip, so it SKIPs the deploy (no second deploy) |

What "signed change" means to the gate: a sentinel `org/critical_paths/.open_deploys/<slug>.json` with `status`
exactly `OPEN` (`deploy_ledger.py open`) whose text, or whose `entry_path` markdown, carries the repo path and the pin.
Shape precedent: `bd-gold-etf-classifier-cash-type-20261014.json` (L1 "commit pin e340e07f4e ... sha256 e7385264...").
A never-widen pair is not owed: the act writes one code object, no served data output moves (CLAUDE.md NEVER-1,
"verified DELTA=0 needs no hold"; the bd etf_classifier entry carried a pair because that script changes served
classifications).

## Candidate table (bd gold top-level, not named by `gold_dispatch.sh`, not imported)

| script | lines | last commit | S3 today | imported by | execution path |
|---|---|---|---|---|---|
| `diag_sleeve_fix.py` | 103 | 2026-05-04 | MATCH (ETag = repo md5, 1 version) | none | none (hand diagnostic, `sys.path` insert of the gold dir) |
| `validate_sl_nightly_gate.py` | 219 | 2026-05-01 | MATCH (1 version) | none | none (hand validator) |
| `E_25.aua_decomposition_audit.py` | 439 | 2026-05-01 | MATCH (1 version) | string mention in `gold/lib/etf_classifier.py` | has `--upload` (writes S3 when invoked); rejected for that reason |

Rejected classes: anything in `gold_dispatch.sh`'s list (24 scripts run daily); anything under `gold/lib/` (imported by
the chain, and outside the pinned-entry regex); inf and cot trees (the cot exporter copies two named bronze scripts at
boot, `cot-exporter/user-data.sh:40-41`, and the inf runners sync `code/bronze/` and `code/gold/` into daily chains);
mdpf (gated in CODE_TREES but absent from the hook's `BUCKETS` map, see gap R3).

Confirmations: `gold_dispatch.sh` has no `*.py` loop (`:675`, `:681` only count synced files); `run-gold-layer.sh:90`
syncs `code/gold/` whole; `comp-pipescript deployed` lists the chain scripts only (the diagnostics are outside its
registry, so parity was read with `s3api head-object` against `git cat-file` md5, above).

## Proposed cell shape (for the issuer; not a cut)

1. U7 edits one docstring line in `diag_sleeve_fix.py`, commits via `safe-commit.sh` (commit-gate: py_compile,
   ds-precommit, ruff), records the new blob id.
2. U7 opens the NEVER-2 entry (`deploy_ledger.py open --slug ctlpln-r21-fwd5-one-script-20261015 ... --window-hours 2`)
   with legs: L1 git (commit + blob pin + sha256), L2 s3-prefix (`s3://opal-data-bd/code/gold/diag_sleeve_fix.py`,
   proof: ETag equals the new md5 and a new VersionId), L3 verify (the audit log shows exactly one `PINNED-DEPLOY`/deploy
   row for this ref and no other path; `list-object-versions` shows 2 versions). Prior VersionId recorded in the title.
3. U7 pushes `box/laptop` itself, within the same minute, with `AGENTBUS_DEVICE=laptop` and `OPAL_AGENT_SERIAL` set so the
   audit row names U7.
4. Proofs: `s3api head-object` ETag = new md5; `list-object-versions` = 2; `org/safe-deploy-bypass-audit.log` tail
   shows one deploy row for this path and zero `PINNED-DEPLOY` rows for any other path; `comp-pipescript deployed`
   unchanged for every chain script (negative arm: the 24 dispatched scripts still MATCH).
5. Close the entry; the 04:00Z runner sync is NOT part of the cell (it is the runner's act, and it executes nothing new).
6. Negative control already carried by round 19: an unsigned deploy-scope push deploys 0 and writes HELD.

## Risk class and uncertainty

- `<risk>` WORLD: a real S3 write to a production code prefix. Blast radius above is the whole write set.
- UNREAD: whether U7's own session carries `AGENTBUS_DEVICE`; the hook blocks the push if not (`:176-179`), which is
  safe. The round-19 fixture stubbed `aws`; this is the first live pass of the pinned-entry code path, so its
  `aws s3 cp` read of a present object (the "equal bytes, nothing to deploy" branch) is exercised for the first time on
  the 0 other pins -- a no-op today.
- The box-sync hazard (conclusion 5) is a timing fact, not a defect; it is also the reason the audit row's `_who`
  must be read, never assumed.

## GAPS (for the issuer's rows)

| # | what | evidence | proposed |
|---|---|---|---|
| R1 | A pinned subdirectory script (`gold/lib/*.py`, `tests/*.py`) is never admitted by the pinned-entry step | hook `SCRIPT = ^data/([^/]+)/scripts/(gold|silver|bronze)/([^/]+\.py)$` (`:62`); the live open bd entry pins `gold/lib/etf_classifier.py`, which `detect_script_files` deploys on the box-diff path but the pinned path cannot | widen the regex to the layer's subtree, or state the top-level bound in the hook comment and D1-S8 |
| R2 | The hook's `BUCKETS` map is a hand copy of three trees | `:61`; CODE_TREES also gates `mdpf -> opal-data-mdpf` (`safe_deploy_core.py` CODE_TREES) | read the map from the core (one writer IRPT_BCKEND, so a row there), or print HELD with the reason for an unmapped tree (today it prints `pinned-s3-target-not-derivable`, correct but silent about why) |
| R3 | Sibling of W113-S1: silver/bronze keys are `code/<layer>/<name>`, which does match CODE_TREES; the row can be disarmed on this read | CODE_TREES layers map `code/gold/`, `code/silver/`, `code/bronze/` for bd, inf, cot | disarm W113-S1 with this citation |
| R4 | Every push from the box runs the pinned-entry step, including the 10-minute box-sync | `:207`, `:228`; `box-sync-schedule.ps1:30` | accepted behaviour (an open pin should land); the cell proves actor attribution by reading the audit row |
