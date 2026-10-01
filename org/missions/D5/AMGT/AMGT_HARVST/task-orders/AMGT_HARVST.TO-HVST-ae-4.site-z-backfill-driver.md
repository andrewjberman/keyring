# AMGT_HARVST task order -- `HVST-ae-4` -- ROUND 32 chain A: THE SITE Z BACKFILL DRIVER -- ALL 89 NAMES, BUDGET PRINTED FIRST, CHECKPOINT AND RESUME, UPLOADS ON, sa FIRST, THE STOP SET HONOURED (FWD-15; the depth table toward FWD-14)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ae-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~92</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched; the driver is a process started by hand, never a Scheduled Task in this order.
comp-iam: RUN at L5 -- phase A is LOCAL (code, tests with a stubbed collector, a dry run that refuses sockets). Phase B is the sa run (sa egress on its existing route, new bronze/silver objects and uploads in opal-data-harvest), only under the signed never-widen pair, and only after HVST-ae-1's phase B.
comp-adversary: RUN at L5 -- the adversary is a resume that re-fetches (the checkpoint written before the job, or keyed on the wrong grain) and a budget printed after the first request. AC1's plants and AC2's guarded dry run catch both.
</preflight>

## 0. THE CELL (decomposition section 45, cell `HVST-ae-4`; PRD v0.13 FWD-15)

**FWD-15, verbatim:** a site Z backfill driver collects the whole universe and survives interruption. DONE WHEN,
EXERCISED: a driver run over all 89 names on the site Z box (a) prints each publisher's daily request budget before it
starts; (b) is stopped mid-run and resumed from its checkpoint with no article fetched twice; (c) uploads what it
collects to the store in the same run; (d) runs sa first; (e) for bbg and wsj, discovers articles in date order back to
2026-01-01 rather than by search relevance [NOT this order: it is cell `HVST-ae-5`'s]; (f) honours the existing STOP set.

**Rulings that bind this order:** the STOP set is `bot_check`, `unclassified`, `account_or_harvester_unavailable`,
`sign_in_refused`, `throttled`, `upstream_unavailable`, `cooldown` and **`error`** (round-31 analysis ruling 2). The
105-page sa ceiling is VOID. Andrew's depth bar (50+ articles per security since January, ideally 100+) is never
re-based by any seat.

**What exists (measured at the cut):**
- The collector CLI: `python -m lib.opal_data_harvest [--publishers ...] [--security-json FILE] [--retrieval-mode
  backfill] [--floor DATE] [--new-only] [--harvest-grammar] [--no-sign-in] [--max-jobs N] {run,plan,universe,upload-harvest,...}`.
- `python -m lib.opal_data_harvest universe` prints JSON `{"denominator": 89, "securities": [{"key", "company",
  "ticker", "aliases", "sa_symbol", ...}, ...]}` in the collector's universe order. A security file for `--security-json`
  is one of those rows, verbatim.
- Round 31's per-name invocation (the shape to drive): `run --harvest-grammar --retrieval-mode backfill --floor
  2026-01-01 --new-only --no-sign-in --security-json <file> --publishers <pub> --max-jobs 1`, then ONE
  `upload-harvest` capped at the printed pending count. Each job writes a run record whose job `status` is the outcome.
- Pacing: 15 s per request plus up to 10 s jitter (read the real values from the collector's config; never type them).
  The collector keeps a runtime cooldown table (find it in `lib/opal_data_harvest/worker.py`).

## 1. PHASE A (LOCAL) -- the code, now

1. **`lib/opal_data_harvest/backfill_driver.py` (new), run as `python -m lib.opal_data_harvest.backfill_driver`.**
   Flags: `--checkpoint PATH` (required), `--publishers` (default `sa ft wsj bbg barrons`, sa ALWAYS first whatever the
   order given), `--names KEY ...` (optional subset), `--dry-run`.
   - Prints `UNIVERSE: <n>` from the collector's own universe.
   - Prints one `BUDGET <pub>: <requests/day> requests/day (<basis>)` line per publisher BEFORE any job: the basis is
     the pacing from config (86400 / (minimum + jitter/2)) and any per-publisher daily cap the config or contracts carry.
   - Prints one `PLAN <pub> <security_key>` line per (publisher, name) still to run, in run order.
   - `--dry-run` stops there, prints `NETWORK CALLS: 0`, starts no collector process and exits 0.
   - A real run: per (pub, name), check the cooldown table first (a publisher under cooldown waits for it, never starts
     into it); run the round-31 invocation shape; read the job's run-record status; then ONE `upload-harvest` for what
     that job stored. On a STOP-set status the driver stops THAT publisher's leg and moves to the next publisher.
   - **Checkpoint:** after each (pub, name) job ends, atomically rewrite the checkpoint JSON (`{"done": [[pub, key,
     status, run_id], ...], "stopped": {pub: status}, "started_at", "updated_at"}`); a restart skips every done pair and
     every stopped publisher, so a resumed run fetches no article twice (`--new-only` keeps the in-job dedupe).
   - At the end (or on Ctrl-C after the current job), writes a run summary JSON beside the checkpoint
     (`started_at`, per-publisher pairs done / stopped status, articles stored) and prints a per-name depth table.
2. **`lib/opal_data_harvest/test_ae4_backfill_driver.py` (new), the plants, with the collector STUBBED** (no process,
   no network): (i) every BUDGET line precedes the first PLAN line; (ii) sa jobs run first even when `--publishers
   ft sa` is given; (iii) a run interrupted after 2 jobs and resumed runs the remaining jobs only, and no pair runs
   twice; (iv) a job status `error` (and each other STOP status) stops that publisher's leg and the next publisher
   proceeds; (v) an upload is invoked once after each job that stored anything; (vi) a publisher under cooldown is not
   started.
3. Report and STOP at the end of phase A. Phase B is handed to you by the issuer after `HVST-ae-1` phase B lands and the
   never-widen pair for the sa run is signed.

## 2. PHASE B (WORLD) -- only when the issuer hands it to you

Run the driver for `sa` over all 89 names with `--checkpoint org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~92/ae4_checkpoint.json`;
stop it once mid-run and resume it (FWD-15 b); copy the run summary to
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~92/ae4_run_summary.json`; then run AC3.

<paths>
lib/opal_data_harvest/backfill_driver.py
lib/opal_data_harvest/test_ae4_backfill_driver.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~92/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

**Reads you may need (no write):** `lib/opal_data_harvest/__main__.py`, `worker.py`, `publishers.py`, `contracts.json`,
the collector config it loads, `conftest.py`, and the issuer's checks in
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round32/checks/` (`ae-4.AC2.py` is the dry-run
interface). **Never in phase A:** a collector run, a publisher request, an S3 write.

## 3. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ae-4"><invocation>python -m pytest lib/opal_data_harvest/test_ae4_backfill_driver.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ae-4"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round32/checks/ae-4.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-ae-4"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round32/checks/ae-4.AC3.py</invocation><expect>AC3 RESULT: PASS</expect></criterion>
</proof_of_spec>

- AC1 and AC2 pass at the end of phase A; AC3 FAILS until phase B -- record it FAIL with `status_reason: phase B
  pending`, never PASS.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~92/AMGT_HARVST.TO-HVST-ae-4.site-z-backfill-driver.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ae-4.site-z-backfill-driver`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Analysis `ROUND_ANALYSIS.round31.md` @`309b2da963` section 4 item 4 (after item 1); brief IV.4 (no driver exists;
  scheduled task Disabled; uploads off).
- Chain A's edge is DATA: the sa run (phase B) waits on `ae-1` phase B; the code (phase A) has none, so it takes slot ~92
  now (decomp section 45).
- AC3 reads the collector's own silver keyed by `discovered_for` (row `Z-S51`: universe and gold share 0 keys);
  baseline 20 distinct sa articles since January.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>open</status>
<round>32</round>
<slot>~92</slot>
<fabric>site-z</fabric>
