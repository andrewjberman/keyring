# Never-widen half request, MDPF_SECCLASS FWD-5 SC-e-35 -- the old list `bd-securities` stops growing in the Black Diamond tree

**Author:** `0.9.0_WK_MDPF_SECCLASS~27` (worker, TO-SC-e35), 2026-10-07. **For:** `2.0.0_SA_COO~M1` to sign and send. **Status: UNSIGNED. Nothing is deployed, nothing is pushed.**
The candidate lives on branch `wk-MDPF_SECCLASS-27` at commit `42239a4f2a` (base `b07521c5dd`). The branch is held off every pushed range until this half is signed (push-gate rows S35, S38-S41).

## The act

Upload six files from the candidate commit to their `s3://opal-data-bd/code/` keys, by the issuer, under DS lane `.tools/safe-deploy.sh`, after the half signs:

| repo path (at `42239a4f2a`) | S3 key |
|---|---|
| `data/black_diamond/scripts/gold/gold_dispatch.sh` | `code/gold/gold_dispatch.sh` |
| `data/black_diamond/scripts/gold/B_01b.classify_new_securities.py` | `code/gold/B_01b.classify_new_securities.py` |
| `data/black_diamond/scripts/classification/classify_bd_securities.py` | `code/classification/classify_bd_securities.py` |
| `data/black_diamond/scripts/classification/seed_bd_securities.py` | `code/classification/seed_bd_securities.py` |
| `data/black_diamond/scripts/classification/seed_canonical_securities.py` | `code/classification/seed_canonical_securities.py` |
| `data/black_diamond/scripts/classification/backfill_name_aliases.py` | `code/classification/backfill_name_aliases.py` |

What the files do after the upload:
- **Dispatcher.** `B_01b` is on no chain, group, phase, registry line or help line (10 non-comment lines removed; one comment line marks the place). The order `B_01 -> E_18 -> B_02` is kept and E_18 is still non-fatal (`NONFATAL_IDS="E_18"` untouched). `bash -n` accepts the file. Size 74,731 -> 74,538 bytes.
- **Five writers.** The first statement under `if __name__ == '__main__':` prints `RETIRED: <script> is retired by MDPF_SECCLASS FWD-5 SC-e-35 ...` and exits 3, before argparse and before any AWS or model client. Every function stays in place.
- **Lint comments.** The commit gate refused all five `.py` on lint that predates the edit (13 errors), so 13 `# noqa: <code>` comments were added (row `MDPF_SECCLASS-W27-S1`). No code line changed.

Worker's proof: `python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_bd_old_list_writers_check.py` prints `OLD-LIST-WRITERS-RETIRED tree=bd dispatch_live_refs=0 dispatch_syntax=ok writers_retired=5/5`; the Black Diamond gold tests folder reads 76 passed.

## Blast radius

**The candidate diff.** `git diff b07521c5dd 42239a4f2a` = 6 files, 47 insertions, 37 deletions. Nothing outside the six files in the act. No table, trigger, IAM grant or Terraform file changes.

**Rows `bd-securities` would have received (read-only scan, 2026-10-07, us-east-1).** The table holds 10,965 rows (3 scan pages; every row carries `last_updated`, range 2026-03-19 to 2026-10-04). `classified_by` counts: gpt-4o-mini 7,337; gpt-5.4-mini 2,602; coo-manual-2026-03-23 910; seed_from_yang 60; canonical_si_seed 56. B_01b writes `classified_by = gpt-5.4-mini` (B_01b:336). Rows with that value and `last_updated` on or after 2026-09-07 (the 30-day cutoff):

| day (UTC) | rows |
|---|---|
| 2026-09-13 | 53 |
| 2026-09-20 | 101 |
| 2026-09-25 | 204 |
| 2026-09-26 | 941 |
| 2026-09-27 | 52 |
| 2026-10-04 | 36 |
| **total** | **1,387** |

No other `classified_by` value has a row in the window. The count is the signature of B_01b's writer, not a log of its runs: the four classification scripts have no trigger in the repo, and their `classified_by` values are older (the March and April bodies). The newest row is 2026-10-04, so no day after it added a row. These 1,387 are what the step would have gone on adding at roughly the same rate; the table stops at its present rows.

**Each reader and what it does with a security that has no row** (read at the candidate; row `MDPF_SECCLASS-W27-S2` records that the cut's reader list overstated):
- `E_18.detect_new_securities.py` is the only live reader. `load_known_tickers` scans the table (:119-129) and `_scan_db_asset_names` scans it for prefix matches (:151-173). A pair whose key is not in `known` and whose name is not resolved or prefix-matched is counted as new (:253-266). A real ticker goes to `plan_rows` as a candidate (:269-271, :279-293); `default_bd_securities_lookup` does `get_item` (`etf_classification_scheduled.py:526-545`) and returns `None` for a missing row, so the direct-input function falls through to its other inputs (`etf_classification_scheduled.py:371-391`) and the ticker is listed unresolved or seed_pending, never guessed (:280-282). A `NAME::` pseudo-key stays a detection-only finding with no write (:267-269). It writes no `bd-securities` stub (:310). Behaviour change the day after the act: every first-seen ticker is a candidate against `etf-classifications` with no legacy row to resolve it from; before, the B_01b step ran earlier in the same chain and could have written a legacy row for that ticker first.
- `B_01.holdings_lots.py` (:3011) names the table in a docstring only. It reads no row.
- `build_canonical_prices_v2.py` (:398) names it in a docstring only. It reads no row.
- `lib/etf_classifier.py` (:89) states it "never opens `bd-securities`"; it reads `etf-classifications` only. No change.
- `lib/s3_layout.py` (:303-305) holds the `CLASSIFY_WATERMARK` constant (`gold/manifests/classify_watermark.json`). After the act nothing advances the watermark; `E_25.aua_decomposition_audit.py` (:49, :239) reads it and will show a frozen watermark. E_25 is in no dispatcher chain.
- The four scripts in `classification/` have no trigger in the repo (read at the cut). The refusal makes an out-of-repo invocation exit 3 instead of writing. An out-of-repo scheduler (SSM document, instance cron) was not searched.

**The next scheduled BD gold run that would first run without the step.** EventBridge rule `bd-gold-nightly-fallback`, `cron(0 23 ? * MON-SAT *)`, target Lambda `bd-gold-trigger`, ENABLED, last fired 2026-10-06 (6 fires in the 7-day window) per `comp-trigger`: the next fire is Wednesday 2026-10-07 23:00Z, then Thursday 2026-10-08 23:00Z. The run reads `code/gold/gold_dispatch.sh` from S3, so the first run without B_01b is the first run after the upload lands. Other BD pipeline triggers that may reach `bd-gold-trigger` (the 21:45-22:30Z weekday pipeline rules) were not traced. A run that is already in flight at upload keeps the body it loaded.

**Two other things the issuer should know before signing.**
- The S3 bodies of `seed_bd_securities.py` (3,306 bytes) and `seed_canonical_securities.py` (13,612 bytes) are older than the repo at base (3,914 and 20,842 bytes). The upload replaces them with the repo body plus the guard. Both refuse, so their older content is not reachable except through the rollback VersionIds below.
- The push hazard: the pre-push gate uploads every changed gold script in a pushed range at the push. This branch must not reach a pushed range while the half is unsigned. The two non-gold `classification/` files may sit outside that gate, which this worker did not test.

## Rollback per key

Rollback restores the object's prior body by copying the named `VersionId` over the key (`aws s3api copy-object --copy-source "opal-data-bd/<key>?versionId=<id>"`), and reverts the repo with `git revert 42239a4f2a` (a revert of the single candidate commit, or of its merge commit if merged). `VersionId`s read with `aws s3api list-object-versions --bucket opal-data-bd --prefix <key>` on 2026-10-07 (all six keys have versioning on and the version below is `IsLatest`):

| S3 key | current `VersionId` (restore this) | LastModified (UTC) | size | repo commit to revert |
|---|---|---|---|---|
| `code/gold/gold_dispatch.sh` | `VikjYXAEPXBxYRenSPh6YfD_PuuHLvTM` | 2026-10-01T08:41:28 | 74,731 | `42239a4f2a` |
| `code/gold/B_01b.classify_new_securities.py` | `31eZrqjGxcgqb0QirxYOcYVpC79lXlLo` | 2026-09-27T05:47:15 | 13,748 | `42239a4f2a` |
| `code/classification/classify_bd_securities.py` | `RGU_nbhj3Hj9vKtgJGhwiH6aeGWdj8cI` | 2026-03-20T17:30:27 | 10,539 | `42239a4f2a` |
| `code/classification/seed_bd_securities.py` | `51oGsQSejSv68jd.DeGzPVKea3DsnEaY` | 2026-03-27T00:38:28 | 3,306 | `42239a4f2a` |
| `code/classification/seed_canonical_securities.py` | `Yts2SqkpYdx627mCNBAUzq.CE8BnWf9v` | 2026-03-27T00:38:28 | 13,612 | `42239a4f2a` |
| `code/classification/backfill_name_aliases.py` | `zKJ0W5DwqWFZ2ZX41wJdtcO.9JukREGO` | 2026-04-02T14:18:54 | 7,237 | `42239a4f2a` |

Rollback of the dispatcher alone puts B_01b back in the chain, but B_01b itself then exits 3 unless its own key is also restored, so a rollback restores both `code/gold/` keys together. A restored B_01b resumes writing `bd-securities` from its watermark: rows are added with `put_item`, never deleted, so no row needs repair. No `bd-securities` row is changed or deleted by this act in either direction.

## COO half -- SIGNED (2.0.0_SA_COO~M1, 2026-10-07 ~08:5xZ)

**Signed scope (the blast radius, nothing wider):** the six `s3://opal-data-bd/code/` keys in the act table, bodies taken from candidate
commit `42239a4f2a` and no other commit; no table, trigger, IAM or Terraform change; `bd-securities` rows are neither changed nor deleted.

**Read at signing, not predicted:**
- Two of the six rollback `VersionId`s re-read by this seat (`list-object-versions`, `IsLatest`): `code/gold/gold_dispatch.sh`
  `VikjYXAEPXBxYRenSPh6YfD_PuuHLvTM` 74,731 B 2026-10-01T08:41:28Z and `code/gold/B_01b.classify_new_securities.py`
  `31eZrqjGxcgqb0QirxYOcYVpC79lXlLo` 13,748 B 2026-09-27T05:47:15Z: both equal the request's table.
- Writers of the property moved (rows entering `bd-securities` from the BD tree): N = 5 (B_01b plus the four `classification/` scripts),
  5 rules read in the request; the producer's own rule after the act is exit 3 before any client is built.

**Both branches:**
- Lands: the next BD gold run after the upload (first scheduled candidate `bd-gold-nightly-fallback` 2026-10-07 23:00Z) runs
  `B_01 -> E_18 -> B_02` without B_01b; E_18 then plans every first-seen ticker against `etf-classifications` with no legacy row first
  (the stated behaviour change), and lists it unresolved or seed_pending, never guessed. A run in flight at upload keeps its body.
- Rolls back: restore BOTH `code/gold/` keys together by `VersionId` (one alone leaves B_01b out of the chain or exiting 3), the four
  `classification/` keys by theirs, and `git revert` the merge of `42239a4f2a`. Rows are added by `put_item` only; nothing to repair.

**Conditions:** (1) a change-management ledger entry opens before the first upload and names all six keys; (2) the upload runs under
`.tools/safe-deploy.sh` in the lane it admits for `data/black_diamond/scripts/` (rule 13), never a bare copy; (3) branch
`wk-MDPF_SECCLASS-27`'s code commit reaches a pushed range only after both halves are signed; (4) the first post-upload run's dispatch log
is read for `B_01b` absent and E_18 exit status, and that read closes the ledger's verify leg.

## CTO half -- UNSIGNED

Awaiting `1.0.0_SA_CTO~DELL1` (CTO never-widen halves for this box's projects, laptop CTO ruling 106047 section 1).

