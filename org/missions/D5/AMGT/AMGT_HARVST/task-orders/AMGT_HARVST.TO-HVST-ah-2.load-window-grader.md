# AMGT_HARVST task order -- `HVST-ah-2` -- ROUND 35: THE PER-MINUTE LOAD GRADER -- VOID EVERY HUMAN-INPUT MINUTE, GRADE FWD-11 LIMB 2a PER PUBLISHER

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ah-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~90</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL, read-only over runtime files; no network.
comp-adversary: RUN at L5 -- the adversary is a challenge solved in a minute with human input counted as unattended, or a whole window with hardware input but no per-minute buckets graded clean. AC2 requires both cases VOID.
</preflight>

## 0. THE CELL (decomposition section 48, `HVST-ah-2`; CTO ruling msg 27860 limb 2a; round-34 analysis item 2)

FWD-11 limb 2a: collection at backfill volume (a full driver day for that publisher, its request count printed) under
the input-source monitor, with every presented challenge passed and no human hand. Zero challenges reads
MET-BY-ABSENCE. The round-34 analysis adds that any window with human input is VOID.

**Inputs that exist:**
- `.runtime/harvest-backfill/runtimes.json`: the live runtime root per publisher, plus the monitor window files.
- Monitor windows written by `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round34/load_monitor.py`. Read it.
  - Window 1 has only totals: hardware 12,795.
  - Window 2 adds `hardware_events_per_minute` keyed `YYYY-MM-DDTHH:MM`, plus `hardware_event_times`.
- Each runtime's `events.jsonl`: `{"event": "http", "publisher", "status", "at", "path"}`, `challenge_passed`,
  `job_finished`, and others.
- Each runtime's `runs/*.json`, whose `request_attempts` carry a `class` field (`ok` / `bot_check` / ...).

## 1. THE BUILD (LOCAL)

New module `lib/opal_data_harvest/load_window_grade.py`. Run as `python -m lib.opal_data_harvest.load_window_grade
[--json] [--runtimes <file>]`; the defaults come from `runtimes.json`, resolved against the repo root (derived, never
typed).

1. **windows:** one entry per monitor file. Each entry carries `window_start`, `window_end`, `hardware_input_events`,
   `has_minutes`, `void_minutes` (minutes with hardware input greater than 0) and `void`. `void` is true when the window
   has hardware input and no per-minute buckets: the WHOLE window is then void.
2. **Coverage:** a minute outside every monitor window is UNMONITORED and counts as void.
3. **Per publisher, all five** (bbg, wsj, barrons, ft, sa; a publisher with no runtime reads zeros):
   - `requests`: http events;
   - `challenges_presented`: bot_check-class attempts or challenge events; state the rule you use and test it;
   - `challenges_passed`;
   - `challenges_in_void_minutes`: these never count toward MET;
   - `clean_hours`: clock hours with at least 1 request and no void or unmonitored minute;
   - `verdict`, decided in this order:
     - INSUFFICIENT if `clean_hours` < 24;
     - else NOT-MET if any challenge presented in a clean minute was not passed;
     - else MET-BY-ABSENCE if none was presented in clean minutes;
     - else MET.
4. Human output prints the denominators. `--json` prints the object the AC2 check reads (open it:
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round35/checks/ah-2.AC2.py`).
5. Plants in `lib/opal_data_harvest/test_ah2_load_window_grade.py`. Use tmp-dir fakes for the runtimes and monitor
   files. Cover:
   - a window with hardware input and no buckets reads VOID;
   - a challenge inside a void minute does not count;
   - a clean failed challenge reads NOT-MET;
   - 24 clean hours with no challenge reads MET-BY-ABSENCE;
   - 23 clean hours reads INSUFFICIENT;
   - an unmonitored minute is void.

<paths>
lib/opal_data_harvest/load_window_grade.py
lib/opal_data_harvest/test_ah2_load_window_grade.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~90/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ah-2"><invocation>python -m pytest lib/opal_data_harvest/test_ah2_load_window_grade.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ah-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round35/checks/ah-2.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~90/AMGT_HARVST.TO-HVST-ah-2.load-window-grader.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ah-2.load-window-grader`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-34 analysis @`6cbef26707` item 2. The verdict is the grader's; the unattended day itself is the
issuer's driver runs under the monitor.

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>open</status>
<round>35</round>
<slot>~90</slot>
<fabric>site-z</fabric>
