# AMGT_RESAPP task order -- `AMGT-bg-2` -- THE SCOPED API BUILDS ONE S3 CLIENT PER CONTAINER, WITH A POOL THAT FITS ITS WIDEST READ (A BUILD, NOT YET SERVED)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bg-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~397</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bg-2.the-scoped-api-builds-one-s3-client-per-container-with-a-pool-that-fits-its-widest-read</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one code module, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- the checks read the live data pool with the box's own read credentials (GET only); no write, no IAM.
comp-adversary: RUN at the cut, each ARM AGAINST THE LITERAL STRING WRITTEN BELOW: at the base, r100_pool_peak.py reads 'reads with a client above its own pool: 1' and exits 1 (the first overlay request peaks at 16 on a pool of 10), r100_cold_check.py reads C2 FAIL (146 S3 clients) and NO, and the route table reads only 'thesis corpus' (663 paths) and 'thesis noise' (2 clock paths) rows (the control). Against a throwaway candidate built in a scratch worktree from the edit below (nothing written to the tree): r100_pool_peak.py reads 'overall per-client maximum 20 over 35 reads; reads with a client above its own pool: 0' (exit 0), r100_cold_check.py reads 4 of 4 / YES (7 clients, 243 S3 requests, cold 8.7 s against the base's 11.5 s), the route table reads the same only-'thesis corpus' and 'thesis noise' rows, and the 38 tests of test_drafted_sections.py and test_filing_attempt_held_marker.py pass. The throwaway A/B that led here, run in fresh processes against the live pool: pool 10 -> 32 alone, cold 11.1 s -> 11.4 s (no effect); one shared client alone, 11.1 s -> 7.8 s; one shared client on a pool of 32, 7.7 to 8.1 s.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-397` (branch `wk-AMGT_RESAPP-397`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-397`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bg-2` (round 100, decomposition s.108)

CTO~DELL1 round-99 analysis section 2 item 2 and the be-1 CTO half ADDENDUM 1: the function's slow tail (53 of 32,528 invocations over 20 s in a day, 49 of them logging 'Connection pool is full')
is the first request a container serves after a quiet period. Measured: that first overlay request builds 146 S3 clients and makes about 242 S3 requests, one client per call of
`scoped_amgt._s3_client()` (151 of the 155 clients, by the lib frame that built them), each with its own pool of 10; the widest read puts 16 simultaneous requests on one client. In
`lib/research/api/scoped_amgt.py` the sibling seam `_dynamodb()` (about line 392) already does what this cell asks of the S3 seam: ONE resource per container, built under a lock.

Make exactly this edit (the file is LF; ASCII only). Replace the function `_s3_client()` (about line 2888, directly after the `DRAFTING_REGION` constant at about line 2839 and before
`_read_drafting_document`) -- today:

    def _s3_client():
        """Thin, monkeypatchable seam -- the same shape as `_dynamodb()` above."""
        import boto3

        return boto3.client("s3", region_name=DRAFTING_REGION)

with, in its place:

    # AMGT-bg-2: ONE S3 client per container, built under a lock, like `_dynamodb()` above. It was built afresh on every call (146 clients
    # and 240 requests in the first overlay request of a container, each client with its own pool of 10); the log's 'Connection pool is
    # full' warnings and the slow first request after a quiet period came from that. A shared client carries up to 20 simultaneous requests
    # in the widest route measured, so its pool is 32.
    S3_MAX_POOL_CONNECTIONS = 32
    _S3_CLIENT = None
    _S3_CLIENT_LOCK = threading.Lock()


    def _s3_client():
        """Thin, monkeypatchable seam -- the same shape as `_dynamodb()` above: ONE client per container, built under a lock."""
        global _S3_CLIENT
        if _S3_CLIENT is None:
            with _S3_CLIENT_LOCK:
                if _S3_CLIENT is None:
                    import boto3
                    from botocore.config import Config

                    _S3_CLIENT = boto3.client(
                        "s3", region_name=DRAFTING_REGION, config=Config(max_pool_connections=S3_MAX_POOL_CONNECTIONS)
                    )
        return _S3_CLIENT

`threading` is already imported (line 111). The tests replace `scoped_amgt._s3_client` itself (`monkeypatch.setattr(scoped_amgt, "_s3_client", ...)`), so the seam keeps its name and its
signature. Add ONE new test file `lib/research/api/tests/test_s3_client_seam.py`:

    """AMGT-bg-2: `_s3_client()` is ONE client per container, built under a lock, with the pool the widest read needs. OFFLINE: boto3.client is replaced."""
    import threading

    import boto3

    from lib.research.api import scoped_amgt


    def test_s3_client_is_built_once_and_carries_the_pool(monkeypatch):
        made = []

        class _Client:
            pass

        def _fake_client(service, **kwargs):
            c = _Client()
            c.service, c.kwargs = service, kwargs
            made.append(c)
            return c

        monkeypatch.setattr(boto3, "client", _fake_client)
        monkeypatch.setattr(scoped_amgt, "_S3_CLIENT", None)
        got = []
        threads = [threading.Thread(target=lambda: got.append(scoped_amgt._s3_client())) for _ in range(16)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        assert len(got) == 16 and all(c is got[0] for c in got)
        assert len(made) == 1 and made[0].service == "s3"
        assert made[0].kwargs["region_name"] == scoped_amgt.DRAFTING_REGION
        assert made[0].kwargs["config"].max_pool_connections == scoped_amgt.S3_MAX_POOL_CONNECTIONS == 32
        monkeypatch.setattr(scoped_amgt, "_S3_CLIENT", None)

Nothing else moves: no other function, no other file, no widths of any thread pool, no other client factory (`store._default_client`, `covered_universe`, `crosswalk` build 9 of 155 and stay).

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W397-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Edit only `lib/research/api/scoped_amgt.py` and add only `lib/research/api/tests/test_s3_client_seam.py`; no other file.
2. No deploy, no store write, no S3 write or delete, no Bloomberg, SEC or model call. The checks read the live data pool (GET only) with the box's own credentials.
3. No `bun`, `npm` or `pip install`.
4. Standing: no push of shared branches.
5. The measuring scripts are the issuer's and are read-only: do not edit them; run them as the criteria name.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/tests/test_s3_client_seam.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~397/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bg-2"><invocation>cd C:/dev/wk-resapp-397 &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round100_prep/checks/r100_pool_peak.py" ".scratch_bg2_peak.json" | grep "^R100 POOL PEAK"; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line reads `R100 POOL PEAK: overall per-client maximum 20 over 35 reads; reads with a client above its own pool: 0` (the maximum may read 16 to 24; the count of reads with a client above its own pool must read 0); and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bg-2"><invocation>cd C:/dev/wk-resapp-397 &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round100_prep/checks/r100_cold_check.py"; echo "exit=$?"</invocation><expect>PASS C1 (cold and warm 200), PASS C2 (the cold request built at most 12 S3 clients: it reads about 7), PASS C3 (the same work: 150 to 400 S3 requests), PASS C4 (warm no slower than cold); arms passed 4 of 4; R100 COLD REQUEST: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bg-2"><invocation>cd C:/dev/wk-resapp-397 &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_other_routes_table.py" ".scratch_bg2_routes.json" --after local | grep -E "^  [a-z]+ +[a-z]+ +[0-9]+ path"; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the control that no served byte moved: the only lines printed are `  thesis     corpus` (the /15 team_sheet, which the tree carries and the live /14 function does not yet; 663 paths at the base) and, only when a generation clock differs between the two reads, `  thesis     noise` (the generation clocks: any count from 1 up; the script prints a kind line only when its count is above zero, and it read 2 at the cut, 0 and 3 in later runs); no `name` line and no timeline or collected row; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~397 <0.9.0_WK_AMGT_RESAPP~397@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Write any python or multi-line file with the Write tool. Run
`PYTHONPATH="$(pwd)" python -m pytest lib/research/api/tests/test_s3_client_seam.py lib/research/api/tests/test_drafted_sections.py lib/research/api/tests/test_filing_attempt_held_marker.py -q`
and report its last line (expected: 39 passed). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~397/AMGT_RESAPP.TO-AMGT-bg-2.the-scoped-api-builds-one-s3-client-per-container-with-a-pool-that-fits-its-widest-read.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- every criterion's output lines (copy each invocation from the order file, never retype it);
- the pytest last line;
- the diff of `scoped_amgt.py` in full;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-99 analysis section 2 item 2 (msg 4198): "read the HTTP pool size the code configures (or the client default) against the parallel storage reads' thread count, set them consistent, under a redeploy pair. Close: the next day's count of invocations over 20 s and of pool warnings, against 53 and 49." READ at the cut (this seat, `r100_pool_peak.py` and `r100_cold_request.py`, fresh processes against the live pool): the code configures NO pool (botocore's 10); the first overlay request of a container builds 146 clients (151 via `_pool_client` -> `_s3_client`) and makes 242 requests; one client peaks at 16 simultaneous. **The pool size alone does nothing measurable (cold 11.1 s with a pool of 10, 11.4 s with 32); one client per container does (7.8 s), and its single client then peaks at 20, so the pool must be 32 to fit it.** The order therefore does both, one edit: a DEVIATION from "set the pool consistent" that the CTO reviews at the pair, stated here and in the issuance commit. The Lambda network is not the box's: the order's effect on the live tail is graded on the live logs the day after the apply, not by these local timings. STAGED redeploy: `AMGT-bg-3`, a SECOND apply after `AMGT-bg-1`'s read. AC1's expectation allows the maximum to read 16 to 24 because it depends on the run's timing; the graded number is 0 clients above their own pool.

**AMENDMENT 1 (2026-10-12T02:0xZ, 2.0.0_SA_COO~R1, the issuer's own order; no gate limb graded it: `.tools/to-pipeline-gate.py` fires on newly-added orders, and this is a modification):** AC3's expectation required a `thesis noise` line of 2 paths, which I took from ONE dry-run at the base. The noise class is the generation clocks (`generated_at`), moved or not by the time between the live read and the local read, so its count varies from run to run (2 at the cut, 0 and 3 in later runs) and the script prints no line for a zero. The worker's honest run printed only `thesis corpus 663 path(s)` and read FAIL on a candidate whose routes did not move. The expectation now allows the noise line to be absent or any count; the invocation is unchanged. **The defect is the issuer's: a count that depends on a clock was written as a fixed number.** The issuer re-ran the literal invocation against worker ~397's candidate (@54659321c9): `thesis corpus 663 path(s)` and `thesis noise 3 path(s)`, exit=0.

<status>complete -- 2026-10-12T02:2xZ by the issuer (2.0.0_SA_COO~R1): wk-AMGT_RESAPP-397 @302b0d397f merged @703845dc6e (AC3 re-run under AMENDMENT 1, instance exclusion reason corrected), proof instance VALID; the candidate is MERGED, NOT SERVED (it reaches the function only by `AMGT-bg-3`'s pair). Issuer re-run on the merged tree: AC1 `R100 POOL PEAK: overall per-client maximum 20 over 35 reads; reads with a client above its own pool: 0` (exit 0; the base reads 1), AC2 R100 COLD REQUEST YES 4 of 4 (7 clients, 245 requests, cold 8.8 s against 11.5 s at the base), AC3 `thesis corpus 663 path(s)`, pytest 39 passed (the seam test and the 38 existing). The diff is the order's edit exactly. The CTO confirmed the design (msg 4200).</status>
<round>100</round>
<slot>0.9.0_WK_AMGT_RESAPP~397</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
