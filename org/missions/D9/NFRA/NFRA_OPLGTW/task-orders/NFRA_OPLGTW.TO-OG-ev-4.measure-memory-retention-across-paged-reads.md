# NFRA_OPLGTW task order -- `OG-ev-4` -- MEASURE: where the host memory goes between paged 49F reads, and which release makes it flat (round 40; found by `OG-ap-32` Phase B, row Z-S338)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ev-4</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ev-4</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- read-only measurement; no schedule or trigger.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change. The reads run on the gateway host in a scratch process under the dedicated role `gateway-49f-blackdiamond-live-read-role` (live from `OG-ap-29`), dispatched by SSM; a read denied is a STOP.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act measures what your own Phase B found (`OG-ap-32`, row Z-S338: host memory 27.8 percent before, then 52.4, 58.3, 64.5, 73.3 after pages 1 to 4 of the transactions chain, peak 87.1, not returned between pages; the release was rolled back to `d3ae88be46`).
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ev-4` (decomposition addendum R3-T.106, round 40, workstream ENRICH-R40-M)

WHY. The cursor release `b124377b41` keeps only the account's rows per partition, yet a page chain on the host kept growing: about 110 to 165 MB per page, 1846 MB host, no swap. Before any code is written, the world must say WHERE the memory sits and WHICH mitigation makes it flat. The candidates are named in your row: the allocator keeping freed memory per thread (glibc arenas), pyarrow's memory pool, and a cache on the ctx.

DO (read-only; numbers and fixed words only; never print, commit or message a client value, an account id, an amount or a name):
1. Stage the app of the release at `release_sha` `b124377b41caf5665b999378fd0ca08ad8a1fb7d` (`git show` from your release tree) in a SCRATCH folder on the host (not the service folder; remove it at the end). Run it from there in the gateway's own venv under the gateway role. The service is not touched; no deploy.
2. For each variant below, in a FRESH process, read the same transactions page chain one call at a time (`get_transactions` for the one test account you used in `OG-ap-32` Phase B, 13-month window, `to_date` = the previous `next_cursor`), THREE pages (the page size is the release's 30). Before the first page and after each page record the process RSS (`VmRSS` from `/proc/self/status`, in MB), the host percent used (1 - available/total), and the page's wall seconds. Between variants wait until the host percent is back within 3 points of its idle level (record it). STOP a variant at 75 percent host used (set `stopped_at_host_pct` true; two pages are then enough) and never exceed 80.
   - A: the release as is.
   - B: A, plus after each page `gc.collect()` and `pyarrow.default_memory_pool().release_unused()` (if pyarrow is imported by the reader; say if not).
   - C: B, plus `ctypes.CDLL("libc.so.6").malloc_trim(0)` after each page.
   - D: A with the environment variable `MALLOC_ARENA_MAX=2` set for the process.
   - E: A with `ARROW_DEFAULT_MEMORY_POOL=system` set for the process.
   - F: A with `app.client_adapter_bd49f.READ_WORKERS` set to 4 for the process.
3. Write `W/MEMORY_RETENTION.json` (`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/`) = `{"body": {"read_at": "<iso>", "release_sha": "<40 hex>", "host_total_mb": <int>, "threshold_mb_per_page": 20, "variants": {"A": {"label": "<fixed words>", "rss_before_mb": x, "pages": [{"page": 1, "rss_mb": x, "host_pct": y, "wall_s": z}, ...], "median_growth_mb": m, "stopped_at_host_pct": false}, "B": {...}, ... "F": {...}}, "flattening_variant": "<letter or none>"}}`. `median_growth_mb` is the median of the page-to-page RSS growth over pages 2 to n. `flattening_variant` is, among B to F, the variant with the lowest median growth when that median is 20 MB per page or less, else `none`. Also record which of the three candidates your numbers support, in your report and in a surprise row (the file holds numbers and letters only).
4. Run `ev4.AC1`, write the proof instance, flip the status, REPORT once: the six medians, the flattening variant (or none), the idle host percent, and any surprise (a variant that changed the wall time by more than 20 percent, a read error).

## 2. BOUNDS

- Read-only: no write to any bucket or table, no deploy, no code change in the repository, no change to the gateway service or its environment. One chain of three pages per variant, no loops. A read denied is a STOP and a BLOCKING row. Stop at 75 percent host used.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print or commit a client value, an account id, an amount or a name.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` as above (the tree convention grants it; it needs no entry). Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ev-4"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/ev4.AC1.sh; echo "exit=$?"</invocation><expect>(?s)variant A: pages \d+.*variant F: pages \d+.*flattening: threshold 20 MB per page, variant (\w+) \(rule says \1\).*release_sha is 40 hex and host_total_mb is an int: yes.*content hygiene: long digit runs 0 \(want 0\); e-mail addresses 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the record is complete and self-consistent: six variants with numeric pages (three, or two when stopped at 75 percent), each median recomputed from its pages, the flattening variant following the stated rule, and nothing but numbers and fixed words in it.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ev-4.measure-memory-retention-across-paged-reads.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if AC1 PASSes, and report once. The code cell `OG-en-20` is cut on your answer.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 40, workstream ENRICH-R40-M (decomposition addendum R3-T.106). Risk SERVED. The release `OG-ap-32` was rolled back to `d3ae88be46` (ledger CLOSED, tarball sha256 recorded); the host runs the pre-round adapter with the three harvest files.
- The 20 MB per page line is the issuer's reading of "flat" (the page chain of 12 pages would then add at most 240 MB); the CTO may move it. The numbers, not the verdict word, are the evidence.
- Pre-cut: `ev4.AC1` base FAIL as expected (record absent); PASS arms on synthetic records (C flattening; none flattening; a stopped variant with two pages); controls FAIL (a verdict naming B when C is flatter; `none` though C is flat; A with two pages and not stopped; a median that differs from the pages; F missing; an e-mail in the record).

<status>staged</status>
<round>40</round>
<workstream>ENRICH-R40-M</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
