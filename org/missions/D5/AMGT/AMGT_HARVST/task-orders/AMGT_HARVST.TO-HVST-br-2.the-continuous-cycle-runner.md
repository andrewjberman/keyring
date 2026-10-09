# AMGT_HARVST task order -- `HVST-br-2` -- ROUND 74 (PRD v0.22 FWD-18, both halves SIGNED; `1.0.0_SA_CTO~Z` msg 31923): ONE PROCESS CYCLES THE FOUR PUBLISHERS WITHOUT END, ONE RECORD PER CYCLE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-br-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~127</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule registered by this cell (cell `HVST-br-3` writes the installer; the issuer registers it).
comp-iam: RUN at L5 -- LOCAL code and tests with the package's fakes. NO real collector job, NO publisher call, NO S3 call, NO upload. A `--dry-run` makes no network call. `config.json`, the identity files and the aliases are NOT changed. A collection leg is LIVE from the shared tree; your branch is not merged while it runs.
comp-adversary: RUN at L5 -- the adversary is a runner that runs the FT, one that stops for good when a publisher refuses, one whose "since" moves forward after a cycle that did not complete, one that fetches a held article's body, or a test that runs a real job.
</preflight>

## 0. THE CELL

The outcome (PRD FWD-18): ONE process on this box, with no agent session in its path, runs without end. A CYCLE is one
pass over the covered list for ONE publisher: it asks that publisher for what it published about the list since that
publisher's last COMPLETED cycle, stores each new article once (a held article is never fetched again), and writes ONE
cycle record. The process moves to the next publisher at the collector's existing pace and starts again at the end. The
publishers are Bloomberg.com (`bbg`), WSJ (`wsj`), Barron's (`barrons`) and Seeking Alpha (`sa`); the FT is never run.
A publisher that published nothing records zero new, never a missing record; a publisher that cannot run without a hand
(a bot check, a refused sign-in) records that by name and the process goes on to the next publisher.

The collector already does one cycle's work: `lib/opal_data_harvest/backfill_driver.py` runs one publisher over the whole
universe, one job per name, with `--floor <date>`, `--new-only` (held articles skipped before any body request; each job
record lists them in `skipped_keys`), `--no-sign-in` (a 401 ends the job `sign_in_refused`), the per-publisher cooldown
(the existing pace), a checkpoint, a `--stop-file`, and a `<checkpoint>.run_summary.json` at the end. Read
`backfill_driver.py`, `test_ae4_backfill_driver.py` and `README.md` first. BUILD ON IT; do not copy it.

## 1. THE BUILD

1. `lib/opal_data_harvest/cycle_runner.py`, run as `python -m lib.opal_data_harvest.cycle_runner`. Arguments:
   `--state-dir <dir>` (required), `--runtime-root <dir>`, `--publishers` (default exactly `bbg wsj barrons sa`, in that
   order), `--stop-file <path>`, `--once` (one pass over the publishers, then exit), `--dry-run` (print the plan, no job).
   `ft` given in `--publishers` is refused at parse time, exit 2, the message naming FWD-18.
2. A cycle for publisher P, in order:
   - `floor` = the UTC date `started_at` of P's last cycle record whose `completed` is true; when there is none, the UTC
     date of yesterday. A cycle that did not complete never moves P's floor.
   - run the backfill driver for P alone over the full universe with a FRESH checkpoint
     `<state-dir>/cycles/<P>/<cycle_id>.checkpoint.json` (`cycle_id` = UTC `%Y%m%dT%H%M%SZ`), `--floor <floor>`, the
     same `--runtime-root` and `--stop-file`, `--auto-resume-transient 2`. Call it through `backfill_driver.main(argv)`
     or one subprocess per cycle -- your choice, said in your report.
   - write ONE record `<state-dir>/cycles/<P>/<cycle_id>.cycle.json` with the keys, exactly: `publisher`, `cycle_id`,
     `started_at`, `ended_at`, `floor`, `asked` (pairs planned), `new` (articles stored), `already_held` (the sum of
     `len(skipped_keys)` over the cycle's job records; say in your report where you read them), `failed` (pairs that gave
     up or are left for retry), `stopped` (null, or the publisher's named stop status such as `sign_in_refused`),
     `completed` (true only when every planned pair is done and `stopped` is null). Written atomically, also when the
     driver raised (then `completed` false and `stopped` names the exception class).
   - print one line `CYCLE <P> <cycle_id> floor <date> asked <n> new <n> held <n> failed <n> stopped <x> completed <b>`.
   Then the next publisher. After the last, start again with the first, until the stop file exists (checked between
   cycles as well as by the driver between jobs) or `--once` is given.
3. `--dry-run` prints, per publisher, `CYCLE PLAN <P> floor <date> pairs <n>` (n = the universe size the driver would
   plan), then `NETWORK CALLS 0`, and exits 0 after one pass.
4. `lib/opal_data_harvest/test_br2_cycle_runner.py`, no network, with a fake driver in place of real jobs:
   (i) a publisher with nothing new: a record exists, `new` 0, `completed` true;
   (ii) a publisher whose job ends `sign_in_refused`: its record names `sign_in_refused`, `completed` false, and the NEXT
   publisher's cycle runs in the same pass;
   (iii) THE NEGATIVE ARM: a planted held article is counted in `already_held` and NO body request is made for it (use the
   package's existing fakes for `--new-only`; name them in your report);
   (iv) `ft` refused, exit 2;
   (v) the floor: after a completed cycle started on day D, the next cycle's floor is D; after a stopped cycle it is not
   moved;
   (vi) the stop file present after the first cycle ends the run with no further cycle;
   (vii) a driver that raises: a record with `completed` false and the exception class named, and the pass goes on.
5. Change `backfill_driver.py` only if a count the record needs is not reachable otherwise; list each change.

<paths>
lib/opal_data_harvest/cycle_runner.py
lib/opal_data_harvest/test_br2_cycle_runner.py
lib/opal_data_harvest/backfill_driver.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~127/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-br-2"><invocation>python -m pytest lib/opal_data_harvest/test_br2_cycle_runner.py -rA --tb=line -p no:cacheprovider</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-br-2"><invocation>python -m lib.opal_data_harvest.cycle_runner --dry-run --state-dir .scratch/br2_dry</invocation><expect>NETWORK CALLS 0</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-br-2"><invocation>python -m pytest lib/opal_data_harvest -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; your next row id is `AMGT_HARVST-Z-W127-S1`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~127/AMGT_HARVST.TO-HVST-br-2.the-continuous-cycle-runner.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-br-2.the-continuous-cycle-runner`. Pin every artifact row to the commit that carries it.
- Run every script from the repo root of YOUR worktree as `PYTHONPATH=. python <file>`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: PRD v0.22 FWD-18 @e30fb3e610, `prd-signoff.py status AMGT_HARVST` read 21:1xZ: ratified-text SIGNED
  (3.0.0_SA_CVO~Z, current), brief admitted (CRO wrote it). `1.0.0_SA_CTO~Z` msg 31923: "cut it after that sign; until
  Barron's is signed in, its cycle records the refused sign-in by name and the run moves on." Andrew's records:
  `ANDREW_DIRECT_20261008_164xZ_DAILY_NEWS_PULL_NONSTOP_ON_THIS_BOX.md`, `ANDREW_DIRECT_20261008_171xZ_OPEN_CALLS_SIX_ANSWERED_AND_CELL_TRACKING_ASK.md`.
  Decomposition section 87.
- FWD-18's hops: (1) the runner, this cell; (2) start with the box, `HVST-br-3`; (3) the page an analyst reads ("can tell
  from the page's own words when a publisher did not run") -- NOT cut this round: it needs cycle records that exist, and
  is the next enrichment.
- ACTIVATION at close, by the issuer: the live r47 Seeking Alpha backfill leg (relaunched 21:20:38Z) must end or be
  stopped before the runner runs `sa`, so one publisher is never asked twice at once. The runner runs from a PINNED
  checkout, never the shared tree (Scheduled Tasks run whatever is checked out).
- <risk> SERVED (the running process writes bronze and silver through the existing upload path). Chain of one, slot
  ~127. **Checks dry-run at the base:** AC1 base FAIL as expected (the test is absent); AC2 base FAIL as expected (no such
  module); AC3 base PASS expected (the package suite on HEAD).

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>issued</status>

COMPLETE 2026-10-08 ~22:2xZ (issuer 2.0.0_SA_COO~H): worker ~127 @ad829c5290, @301945614a, @13dfb79a0d, drained @5a2d54eb4a (surprise channel resolved as a union). Re-run by the issuer from the worktree: AC1 12 passed; AC2 four 'CYCLE PLAN <P> floor 2026-10-07 pairs 242' lines then 'NETWORK CALLS 0', no state dir written; 'ft' refused at parse. The hold 'not merged while a collection leg runs' is LIFTED by the issuer for this branch: its diff adds two new files and changes no file a live process imports (backfill_driver.py unchanged). Row Z-W127-S1 RULED: --idle-seconds (default 300, after a pass in which no cycle completed) is accepted as the polite pace FWD-18's source names. Activation (task registration against a pinned checkout, after the sa backfill leg ends) is the issuer's act at close.
<status>complete</status>
<round>74</round>
<slot>~127</slot>
<fabric>site-z</fabric>
