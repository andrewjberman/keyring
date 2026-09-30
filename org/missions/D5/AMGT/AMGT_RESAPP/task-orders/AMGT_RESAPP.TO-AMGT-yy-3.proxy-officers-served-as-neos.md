# AMGT_RESAPP task order -- `AMGT-yy-3` -- THE PROXY'S OFFICERS SERVED AS NAMED EXECUTIVE OFFICERS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-yy-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~177</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE for this cell's own acts: the dry-run writes nothing; the real M-1 writes are yy-5's act under the pair, into the SAME management/v1 prefix the Lambda already reads.
comp-adversary: RUN by the issuer at the cut -- AC1 reads the planned object on both pointer names; AC2 reads it through this tree's read_management; AC3 is the bound.
EGRESS CLASS, declared: EDGAR (data.sec.gov, www.sec.gov) through lib/research/filings/fetch.py only, from committed code -- Andrew-direct R-21 (vendor egress for AMGT, scripted, never an agent turn).
</preflight>

## 1. THE CELL -- `AMGT-yy-3` (round 50, decomposition s.58)

Round 49 built `lib/research/management/proxy_officers.py`: `officers_from_proxy(key)` reads the latest proxy (DEF 14A) through
`fetch.py` for a name whose annual report's officer section points elsewhere, and `census()` found two such names, `HAL_US_Equity`
and `INTU_US_Equity`, each gaining 5 officers. A proxy lists the NAMED EXECUTIVE OFFICERS -- a subset of the full roster (row
Z-W175-S1). The page shows management from the M-1 pool object `management/v1/{key}/{as_of}.json`, read by
`lib/research/api/scoped_amgt.py` `read_management(security_key)` (`:2736`); `management/bloomberg_fallback.py` is the precedent for a
fallback source writing into that SAME object.

**Build (CTO round-49 ruling 3 -- labelled for what it is, never presented as the whole roster):**
1. `python -m lib.research.management.proxy_officers --persist --security-key <K> [--dry-run]` -- builds the M-1 object for a pointer
   name from `officers_from_proxy`: the officers, plus `officer_set: "named_executive_officers"`,
   `officer_set_label: "Named executive officers, from the company's latest proxy statement (DEF 14A)"`, `source_form: "DEF 14A"`,
   `source_accession`, `source_url`, `retrieved_at`, `document_sha256`, and the object's own `as_of`. With `--dry-run` it prints that
   ONE object as JSON on stdout and writes NOTHING. Without it, it writes through the SAME pool writer the roster batch uses (the key
   is that writer's output, never typed). A name whose section does NOT point elsewhere, or whose proxy read is not SERVED, is
   REFUSED with its reason -- a RESOLVED roster is never overwritten.
2. `read_management` passes `officer_set`, `officer_set_label`, `source_form`, `source_accession` through to the payload when the object
   carries them (null otherwise). Nothing else in its output moves.
3. Tests (no network; stubbed fetch and pool) pin: the planned object's label and source; the refusal on a RESOLVED name; the
   pass-through; a roster object without these fields reads them null.

## 2. BOUNDS

1. No real write in this order (the M-1 writes are yy-5's act). `fetch.py`, `roster.py` and the page are READ-ONLY.
2. EDGAR only through fetch.py from committed code; no agent-side HTTP call (no curl, wget, browser or ad-hoc request).
3. Standing: no install, no push, no promote, no deploy. REFUSE, do not rescue.
4. Python from the repo root with `PYTHONPATH="$(pwd)"`. yy-2 (your slot's previous order) already edited `scoped_amgt.py`; keep it.

## 3. SURFACES

<paths>
lib/research/management/proxy_officers.py
lib/research/management/management.schema.json
lib/research/management/tests/
lib/research/api/scoped_amgt.py
lib/research/api/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~177/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-yy-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round50/checks/yy_neo.py --plane plan; echo "exit=$?"</invocation><expect>INTU_US_Equity and HAL_US_Equity each officers &gt;= 3, set 'named_executive_officers', source 'DEF 14A' + an accession, each planned object validates against management.schema.json (AMENDMENT 1); THE PROXY'S OFFICERS ARE SERVED AS NAMED EXECUTIVE OFFICERS (plan): YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-yy-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round50/checks/yy_neo.py --plane local; echo "exit=$?"</invocation><expect>the same through this tree's read_management; THE PROXY'S OFFICERS ARE SERVED AS NAMED EXECUTIVE OFFICERS (local): YES -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-yy-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round48/checks/api-suite.sh; echo "exit=$?"</invocation><expect>pytest reports N passed and 0 failed -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 the planned object; AC2 the served pass-through; AC3 the bound.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~177/AMGT_RESAPP.TO-AMGT-yy-3.proxy-officers-served-as-neos.proof_of_spec.json`. Report once: what you changed, the planned M-1 key for each name, the EDGAR request count, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-49 analysis s.4 row 3, ruling 3. Base: AC1 FAIL, AC2 FAIL (no --persist), AC3 PASS. Continues ~177 after yy-2
drains (file edge). The two real M-1 writes are yy-5's, under the pair.

**AMENDMENT 1 (2026-09-30 ~00:0xZ, issuer 2.0.0_SA_COO~Z): REOPENED before its drain.** Row Z-W177-S2 (the worker's): `management.schema.json` has `additionalProperties: false` and admits only `filing` / `bloomberg` officer sources, so the object yy-5 would write into the served M-1 store fails that store's own schema (inert only because `enrich.write_document` does not validate). Ruled: the planned object MUST validate. `lib/research/management/management.schema.json` joins `<paths>`; widen it to admit exactly the proxy source and the four NEO fields (`officer_set`, `officer_set_label`, `source_form`, and the source fields the object already carries) -- nothing else widened; a filing or Bloomberg object must validate exactly as before. AC1's check now runs `enrich.validate` on each planned object. The worker's yy-3 commits (58a7b5b7d1, af80b4b90c) stand. Gate: GATE (viii) grades this modified order.

<status>complete</status>
<round>50</round>
<slot>~177</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
