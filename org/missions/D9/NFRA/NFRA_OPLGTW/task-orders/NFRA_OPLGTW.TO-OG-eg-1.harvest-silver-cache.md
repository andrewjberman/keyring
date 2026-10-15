# NFRA_OPLGTW task order -- `OG-eg-1` -- the harvest runner stops re-reading whole silver prefixes, and its cycle record counts its S3 GETs (PRD v3.10 E1 + E2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-eg-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-eg-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~98</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and offline tests only; the runner re-registration is a later applier order (NFRA_OPLGTW.TO-OG-eg-2).
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call is added: the change REMOVES repeated GetObject calls and adds none; no IAM.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is `1.0.0_SA_CTO~Z`'s decision (msg 34372, PRD v3.10 @c3b76c142b) on the CRO's findings `S3_EGRESS_ANOMALY_20261011_14_FINDINGS_20261015.md` @b05fee1182 (DataTransfer-Out $67.99 for 2026-10-11..14; 72% from `opal-data-harvest`, 541 GB out of an 8 GB bucket).
EGRESS CLASS, declared: NONE new; this cell REDUCES S3 egress.
</preflight>

## 1. THE CELL -- `OG-eg-1` (decomposition addendum R3-T.68, workstream EGRESS, FWD-22 defect cell)

All paths relative to the repo root. The harvest runner (Windows task "Opal Data Harvest - Continuous Cycle", `lib/opal_data_harvest/cycle_runner.py`, one process, cycles of the four publishers without end) re-reads a WHOLE silver prefix on every call of two code paths:
`store.silver_latest(source, table, record_key_fields, client=None)` in `lib/research/harvest/store.py` (about lines 373-397: it lists every `part-*.parquet` under the table prefix and GETs each one), called (a) by `store.silver_append` on every append (about lines 431-440) and
(b) by `harvest_grammar.watermark(security_key, publisher_code, client=None)` in `lib/opal_data_harvest/harvest_grammar.py` (about lines 140-153) once per (security, publisher) job. A bbg cycle is 242 pairs and the bbg article silver is 0.21 GB, so one cycle re-reads it about 242 times (~50 GB) before any append: quadratic in what is stored, and still running.
Silver parts are WRITE-ONCE (`silver_append` puts them under `IfNoneMatch="*"`), so a part's content never changes after it is written. Use that.

1. **E1: a cycle-scoped incremental cache in `store.py`.** Add a context manager `silver_cache(max_entries=2)` (a module-level, thread-safe holder; entering sets a flag, leaving clears it). INSIDE the context, `silver_latest` keeps per `(source, table, tuple(record_key_fields))` an entry holding `{key -> (etag or size)} of the parts already folded in`, the `latest` dict and the `held_part` dict (the structures the function already builds).
   On each call it still LISTS the prefix (a listing returns names, not bytes) but GETs and folds in ONLY parts not yet seen, using the SAME `supersedes(fetched_at, part_key, prior_fetched_at, prior_part_key)` rule, so the result equals a full scan EXACTLY (a part is never re-read; a part that vanished from the listing is dropped from the entry by rebuilding it once from scratch). Return a COPY-ON-READ safe value: the caller must not be able to mutate the cached dict (return a shallow copy of `latest`, or document and test that callers only read; `silver_append` and `watermark` only read).
   Keep at most `max_entries` entries (least recently used out) so the process memory stays bounded (the cycle works one publisher's tables at a time). `silver_append`, after its successful `put_object`, does NOT need to update the cache (the next call's listing picks the new part up), but must not leave a stale entry that hides it.
   OUTSIDE the context, `silver_latest` behaves EXACTLY as today (no cache): other callers (`publication_gold`, filings, corpus, by-hand tools) are untouched.
2. **E1b: the runner uses it.** In `cycle_runner.py` wrap each publisher cycle's job loop in `with store.silver_cache():` (the one process cycles forever, so the cache lives for the cycle and is cleared at its end). `harvest_grammar.watermark` needs no change unless the test shows it must; it keeps calling `store.silver_latest`.
3. **E2: the proof instrument.** `store.py` counts every S3 `get_object` it issues through its client wrapper: module-level counters `get_count` and `get_bytes` (bytes of the body actually read), thread-safe, with `store.get_stats_snapshot()` and `store.get_stats_reset()`. Wrap the client calls inside `silver_latest` (and any other `get_object` in `store.py`) so they count; a caller-supplied fake client is counted the same way. In `cycle_runner.py` the cycle record (`<state-dir>/cycles/<P>/<cycle_id>.cycle.json`) gains two integer fields, `s3_get_count` and `s3_get_bytes`, for that cycle (snapshot at start, delta at end). It is a RECORD: send no message, raise no alert, write no other object (the standing moratorium on alerts and monitors).
4. **Tests** in `lib/opal_data_harvest/test_eg1_silver_cache.py` (offline; a counting fake S3 client holding in-memory parquet parts), named exactly: `test_eg1_ac01` (equality), `test_eg1_ac02` (the fixed-pair-count GET arithmetic: 30 parts, 50 `watermark` calls and 10 appends; inside the context the GETs are 30 + the parts written during the sequence; outside, 60 x 30), `test_eg1_ac03` (no context = unchanged: every call is a full scan), `test_eg1_ac04` (the two-entry cap; a third table evicts the least recently used and a re-read rebuilds it with the same result), `test_eg1_ac05` (the cycle record's integer `s3_get_count` and `s3_get_bytes` equal the counting client's totals and nothing else is written or sent).
   The silver bytes written by `silver_append` must be IDENTICAL with and without the cache (assert equality of the written part bodies in `test_eg1_ac01`).

## 2. BOUNDS

- The files in `<paths>` only. No release, no deploy, no runner re-registration, no S3 write to any real bucket (tests use fakes), no live cycle run.
- Change no silver schema, no record_hash, no part naming, no tie-break rule.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a person's name or a full email address; build any alert, alarm, notification or monitor; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
lib/research/harvest/store.py
lib/opal_data_harvest/harvest_grammar.py
lib/opal_data_harvest/cycle_runner.py
lib/opal_data_harvest/test_eg1_silver_cache.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~98/`. Rows: id `NFRA_OPLGTW-Z-W98-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-eg-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/eg1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 5 of 5; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-eg-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/eg1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)existing silver suites: rc=0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the cached read equals the full scan exactly and costs the arithmetic above, the default is unchanged, the cache is bounded, and the cycle record counts its GETs. `AC2`: the existing silver suites still pass, so the silver output is unchanged.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-eg-1.harvest-silver-cache.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once. Your report states the measured GET counts of `test_eg1_ac02` (cached and uncached) and anything in the two modules that calls `silver_latest` and would NOT benefit.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream EGRESS (decomposition addendum R3-T.68; PRD v3.10 @c3b76c142b; CTO msg 34372: FIRST in the queue after the release in flight). The applier half is `OG-eg-2` (stop at a cycle boundary, `-Plan` first, re-register; carries the `sa` re-registration if still pending; the live proof is the first cycle record's `s3_get_bytes` against the CUR baseline of 4-6 GB an hour for the harvest bucket).
- Pre-cut: eg1.AC1 base FAIL as expected (test file absent); eg1.AC2 passes at base (it is the regression guard).

<status>complete</status>
<round>37</round>
<workstream>EGRESS</workstream>
<slot>~98</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
