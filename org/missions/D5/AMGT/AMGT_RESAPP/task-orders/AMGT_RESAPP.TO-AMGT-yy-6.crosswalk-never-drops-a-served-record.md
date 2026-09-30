# AMGT_RESAPP task order -- `AMGT-yy-6` -- THE CROSSWALK NEVER DROPS A SERVED RECORD

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-yy-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~179</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- local build; the served pool is READ (s3:GetObject), nothing is written by this order.
comp-adversary: RUN by the issuer at the cut -- AC1 plants a served record and retires it (difference control); AC2 is the measured fork; AC3 the digest-equal round trip.
EGRESS CLASS, declared: NONE. Opal's own S3, read-only.
</preflight>

## 1. THE CELL -- `AMGT-yy-6` (round 50, decomposition s.58)

`lib/research/identity/crosswalk.py` builds the served identity crosswalk (`build_crosswalk(as_of, coverage_doc=None, pilots=None,
coverage_source=None, registrations=None, ...)`, `:645`) from this tree's inputs (the coverage list, `registrations.json`, the
harvester config, the identity universe) and writes it with `write_pool` (`:1231`) to `s3://opal-data-harvest/crosswalk/v1/<date>.json`;
`_read_pool_latest()` (`:1091`) returns `(document, record)` for the latest served one. **A build replaces the pool with whatever its
inputs hold**, so a record added from another checkout (a pinned side) is dropped by the next CLOUD-side write. Measured at the cut:
the plain `build_crosswalk()` on CLOUD REFUSES -- `ENRICH row names security_key 'BZLFY_US_Equity', which matches no coverage
record` -- while the served pool (`crosswalk/v1/2026-09-29.json`, 237 records) HOLDS `BZLFY_US_Equity`.

**Build the invariant (CTO round-49 s.4 cell 5; AMGT_CORPUS round-16 ruling 1):** `build_crosswalk` gains `served=None` and
`retire=()`. When `served` (a served crosswalk document) is given, the build is UNION-FIRST: every served record whose
`security_key` this tree's inputs do not hold is carried verbatim, before ENRICH rows apply (so an ENRICH row may target a carried
record), EXCEPT a key named in `retire` -- the ONLY way a record leaves. `main --write-pool` passes `_read_pool_latest()`'s document
and a `--retire KEY` option (repeatable). A carried record is counted in the document's `denominators` as carried, never silently.
Tests (stubbed pool) pin: carry, retire, ENRICH on a carried record, and a build with `served=None` byte-identical to today's.

## 2. BOUNDS

1. `crosswalk.py` and its tests only. NO `write_pool` call and no S3 write from this order. Standing: no install, no push, no
   promote, no deploy, no vendor call. REFUSE, do not rescue.
2. Python from the repo root with `PYTHONPATH="$(pwd)"`.

## 3. SURFACES

<paths>
lib/research/identity/crosswalk.py
lib/research/identity/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~179/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-yy-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round50/checks/yy_crosswalk.py --arm plant; echo "exit=$?"</invocation><expect>(a) planted served record survives: True; (b) retirement removes it: True; THE CROSSWALK NEVER DROPS A SERVED RECORD (plant): YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-yy-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round50/checks/yy_crosswalk.py --arm fork; echo "exit=$?"</invocation><expect>(d) served records the CLOUD-side build+union drops: 0, BZLFY_US_Equity kept; THE CROSSWALK NEVER DROPS A SERVED RECORD (fork): YES -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-yy-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round50/checks/yy_crosswalk.py --arm roundtrip; echo "exit=$?"</invocation><expect>(c) records in 237 out 237 (the served count, whatever it reads); digest in == digest out; THE CROSSWALK NEVER DROPS A SERVED RECORD (roundtrip): YES -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 carry + retirement (the difference control); AC2 the exact fork; AC3 today's pool round-trips as a no-op.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~179/AMGT_RESAPP.TO-AMGT-yy-6.crosswalk-never-drops-a-served-record.proof_of_spec.json`. Report once: what you changed, how carried records are counted, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-49 analysis s.4 cell 5 (@61ed59c609), CORPUS round-16 ruling 1 (CORPUS row Z-S63). Base: AC1/AC2/AC3 FAIL
(build_crosswalk takes no served=/retire=). No served move: the round trip is a digest-equal no-op; CORPUS re-signs its r-1 on this
cell's drain.

<status>complete</status>
<round>50</round>
<slot>~179</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
