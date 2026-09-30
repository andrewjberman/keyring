# AMGT_RESAPP task order -- `AMGT-zz-1` -- THE UNION INSIDE `write_pool`: EVERY CROSSWALK WRITER KEEPS A SERVED RECORD

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-zz-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~180</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- local build; the served pool is READ (s3:GetObject) by the check, nothing is written to AWS by this order.
comp-adversary: RUN by the issuer at the cut -- AC1 plants a served record and runs BOTH writers through a fake S3 (base: both drop it).
EGRESS CLASS, declared: NONE. Opal's own S3, read-only.
</preflight>

## 1. THE CELL -- `AMGT-zz-1` (round 51, decomposition s.59)

Two code paths write the served identity crosswalk `s3://opal-data-harvest/crosswalk/v1/<date>.json`, and BOTH go through
`lib/research/identity/crosswalk.py` `write_pool(key, payload, document=None, client=None)` (`:1231`):
(A) `lib/research/identity/add_security.py` `_mint_pool(as_of, rows, reg_path, universe, universe_source, client=None)`, and
(B) the crosswalk CLI (`build_crosswalk(...)` then `write_pool`). Round 50 put a union-first `served=`/`retire=` option into
`build_crosswalk` (`main --write-pool` passes it), but a writer that does not pass it still REPLACES the pool with whatever its own
inputs hold, so a record added from another checkout is dropped.

**Build the invariant at the choke point:** `write_pool` itself reads the latest served pool document (the same read
`_read_pool_latest()` makes, through the `client` it was given) and, before writing, carries every served record whose
`security_key` the new document does not hold -- verbatim -- unless the caller names that key in a new `retire=()` argument, the ONLY
way a record leaves. Carried records are counted in the written document's `denominators` (as carried), never silently. The payload
written must be the serialised document including the carried records, so the object's bytes and its validation agree. A write with
nothing to carry must be byte-identical to today's. `add_security._mint_pool` needs no retire path unless it already has one; do not
widen its signature beyond passing through what `write_pool` needs.
Tests (stubbed client) pin: carry on writer A, carry on writer B, retire removes, nothing-to-carry is byte-identical.

## 2. BOUNDS

1. `crosswalk.py`, `add_security.py` and their tests only. NO real `write_pool` call and no S3 write from this order: tests and the
   check use a fake client. Standing: no install, no push, no promote, no deploy, no vendor call. REFUSE, do not rescue.
2. Python from the repo root with `PYTHONPATH="$(pwd)"`.

## 3. SURFACES

<paths>
lib/research/identity/crosswalk.py
lib/research/identity/add_security.py
lib/research/identity/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~180/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-zz-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round51/checks/zz_choke.py; echo "exit=$?"</invocation><expect>both writers print "planted kept: True" with served+planted records dropped 0; EVERY CROSSWALK WRITER KEEPS A SERVED RECORD: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-zz-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round50/checks/yy_crosswalk.py --arm roundtrip; echo "exit=$?"</invocation><expect>digest in == digest out; THE CROSSWALK NEVER DROPS A SERVED RECORD (roundtrip): YES -- and exit=0 (today's pool still round-trips as a no-op)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-zz-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" timeout 115 python -m pytest lib/research/identity/tests -q; echo "exit=$?"</invocation><expect>N passed and 0 failed, N &gt; 135 (135 at the cut, plus your new tests) -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 the invariant on both writers (the plant is its own difference control); AC2 the no-op round trip; AC3 the suite.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~180/AMGT_RESAPP.TO-AMGT-zz-1.the-union-inside-write-pool.proof_of_spec.json`. Report once: what you changed, how carried records are counted, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-50 analysis ruling 1 / enrichment item 1 (@debbec1907); AMGT_CORPUS r-1 re-sign waits on it. Base: AC1 FAIL
(both writers drop the plant); AC2 PASS (yy-6's round trip); AC3 PASS 135. crosswalk.py is in the scoped-api closure
(`scoped_amgt.py:115` imports it), so this change ships in zz-8's build; `write_pool` is not on the served path.

<status>pending</status>
<round>51</round>
<slot>~180</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
