# AMGT_HARVST task order -- `HVST-q-6` -- ROUND 27 chain 6: barrons B2 (the repair may follow a same-job reauth) + ft F1 (keep the 403 body) -- CODE AND TESTS ONLY, no request sent (FWD-1, FWD-9)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-q-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~75</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- the collector task is Disabled; no run in this cell.
comp-iam: RUN at L5 -- no network at all: every proof runs on stub transports with sockets blocked. NO vendor call, NO S3 write, NO login, NO browser.
comp-adversary: RUN at L5 -- the adversary is a guard edit that loops (repair -> reauth -> repair forever) or a kept 403 body that leaks credentials. AC1 bounds the attempts (one repair after one reauth) and AC2 asserts the stored body carries no cookie/authorization header values.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO REQUEST TO ANY PUBLISHER.** Sockets are blocked in every test and script (assert it). No login, no browser, no
   challenge solving. The RUNS these fixes enable are Andrew's per-use word (`C-HV-EGRESS`).
2. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~75/scripts/`; outputs named `q6_*`.
3. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~75/AMGT_HARVST.TO-HVST-q-6.barrons-guard-and-ft-403-body.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-q-6.barrons-guard-and-ft-403-body`.

<paths>
lib/opal_data_harvest/worker.py
lib/opal_data_harvest/transport.py
lib/opal_data_harvest/test_q6_barrons_guard_ft_body.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~75/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE FINDINGS AND THE CHANGES (`HVST-p-4` @`81fd5632c2`; `ROUND_ANALYSIS.round26.md` ruling 5)

**barrons (B2):**
- **Measured:** the saved session was logged out. The collector's scripted reauth ran at attempt 0, and the first `/search`
  after it returned 401 with a DataDome challenge marker.
- `worker.py` ~:393 (`if attempt or publisher not in {"bbg","barrons"}: raise`) refuses the contracted challenge repair
  (`contracts.json:80`) at attempt 1. So every logged-out barrons start fails the same way (2 of 2 on the ledger).
- **The change:** within ONE job, the contracted repair may run once after a reauth. The number of attempts is bounded and
  there is no loop. Nothing else about the repair changes.

**ft (F1):**
- **Measured:** ft returned 403 on 09-23 and 09-30 to a request unchanged since the 09-15 200s. The 403 body is never kept
  (`transport.py:95`, `worker.py:426`), so the cause cannot be separated.
- **The change:** a rejected response's body is kept in the job's local run artifacts (the runtime root, never S3). It is
  size-capped and has request credentials removed, so the next ft job's refusal can be classified.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 600). THREE mechanical

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-q-6"><invocation>python -m pytest lib/opal_data_harvest/test_q6_barrons_guard_ft_body.py -rA --tb=line</invocation><expect>passed</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-q-6"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~75/scripts/q6_ac2_replay_recorded_shapes.py</invocation><expect>NETWORK CALLS MADE: 0</expect></criterion>

  <criterion id="AC3" cell_refs="HVST-q-6"><invocation>python -m pytest lib/opal_data_harvest/ -rA --tb=line</invocation><expect>0 failed</expect></criterion>
</proof_of_spec>

**What each criterion must prove or print:**
- **AC1:**
  - on a stub: a logged-out barrons start reauths, meets a challenge, runs the repair ONCE, and stops. No loop; the attempts
    are counted.
  - a stub ft 403 keeps its body in the run artifacts: capped, with no cookie or authorization values.
  - mutants restoring either base behaviour fail.
- **AC2:** replay `p-4`'s recorded event shapes (09-23 and 09-30 barrons; ft 403) through the new code on stubs. It prints
  the path each takes and `NETWORK CALLS MADE: 0`.
- **AC3:** the base is commit `ff4405d3d5`, pinned. It prints the base and after counts, and `0 failed`.

## 3. MERGE ORDER

This cell merges only after `HVST-q-1` drains (ruling 6).

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- `ROUND_ANALYSIS.round26.md` s.4 item 6, and ruling 5.
- The barrons run B1 and the ft credential re-harvest F2 are Andrew's acts. This cell is the code only.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>27</round>
<slot>~75</slot>
<fabric>site-z</fabric>
