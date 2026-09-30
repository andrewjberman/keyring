# AMGT_RESAPP task order -- `AMGT-ad-1` -- THE NO-SPAN CENSUS IS THE DRY-RUN OF ONE HOLD TRANSFORM

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ad-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~193</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the checks and the dry-run READ opal-data-harvest; this order writes nothing to AWS.
comp-adversary: RUN by the issuer at the cut -- AC1 recounts the 12 stored documents independently (base: 179, no census file); AC2 grades the transform on every stored document in memory with a plant (a span given to one no-span sentence must stay served); both PASSED on a simulated correct transform and FAILED at the base.
EGRESS CLASS, declared: NONE. Opal's own S3, read-only.
</preflight>

## 1. THE CELL -- `AMGT-ad-1` (round 54, decomposition s.62)

The D-1 drafting documents live at `s3://opal-data-harvest/drafting/v1/<key>.json` (12 today). Several were written before
C-VERBATIM-GATE HOLD, so their `sections[].sentences` still carry sentences with NO non-blank `quoted_spans` string (179 in all). The
deployed adapter already holds those at read (`lib/research/api/scoped_amgt.py` ~:1833); the round moves the hold onto the object.

**Build, in `lib/research/filings/drafting_build.py`:**
1. `hold_unspanned(document)` -- PURE (never mutates its input): returns a copy in which every sentence of `sections[].sentences` with no
   non-blank `quoted_spans` string is removed from its section and appended to top-level `held_no_span` in the pipeline's own held shape
   (`lib/research/drafting/pipeline.py:166`: `{"section", "text", "evidence", "reason": HOLD_NO_SPAN_REASON}`, the schema's
   `held_sentence`). Span-carrying sentences stay byte-equal, in order. Every other top-level key is unchanged, except `denominators`,
   which you may recount (keep every key readers use). The result must pass `scoped_amgt._validate_drafting_document`.
2. A CLI mode `--hold-unspanned`, beside `--rebuild-pool` / `--splice-driver`, over every stored `drafting/v1/*.json` of the measured
   population (`--population`), with `--dry-run` (writes nothing to S3), `--pre-act-dir` and `--only-keys` as the other modes have them. The
   live write goes through the ONE writer the other modes use (`analyze.write_outputs(..., drafting_only=True)`); every document is
   validated BEFORE any write, and one refusal writes nothing. You never run it live.
3. `--census-out PATH` with `--dry-run`: writes the census JSON the act will move --
   `{"population_key", "denominator", "names": {<security_key>: {"unspanned": n, "sentences": [[section, text], ...]}}, "total"}`, names
   with 0 omitted. Run it and write it to
   `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~193/D1_UNSPANNED_CENSUS.json`, with `--population` = the newest
   `crosswalk/v1/<date>.json` (list the prefix; today `crosswalk/v1/2026-09-29.json`).
Tests: a no-span sentence moves; a span-carrying one stays; a blank-string span counts as none; the input is not mutated.

## 2. BOUNDS

1. `drafting_build.py`, new test files, the census file. No live `--hold-unspanned`, no S3 write, no change to `lib/research/drafting/`
   or the adapter. Standing: no install, no push, no promote, no deploy, no vendor call, no model call. REFUSE, do not rescue.
2. Python from the repo root with `PYTHONPATH="$(pwd)"`.

## 3. SURFACES

<paths>
lib/research/filings/drafting_build.py
lib/research/filings/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~193/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ad-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round54/checks/ad_1_census.py; echo "exit=$?"</invocation><expect>the population, stored D-1 documents 12, the per-name counts; THE CENSUS EQUALS AN INDEPENDENT RECOUNT: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ad-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round54/checks/ad_1_hold.py; echo "exit=$?"</invocation><expect>12 documents, no BAD line, the plant kept served: True; HOLD_UNSPANNED MOVES EXACTLY THE NON-VERBATIM SENTENCES: YES -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ad-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" timeout 115 python -m pytest lib/research/filings/tests -q; echo "exit=$?"</invocation><expect>N passed and 0 failed, N &gt; 134 (plus your new tests) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~193/AMGT_RESAPP.TO-AMGT-ad-1.no-span-census-and-hold-transform.proof_of_spec.json`. Report once: the census total and per-name counts, what you changed, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-53 analysis item 1 (with item 2's transform, one rule). Base: AC1 FAIL (179 recounted, no census file), AC2 FAIL
(hold_unspanned ABSENT), AC3 PASS 134. Positive arms (ruling 1): AC1 PASS on a census written from the recount, FAIL with one BA sentence
dropped; AC2 PASS on a reference transform, FAIL with one span-carrying sentence dropped.

<status>complete</status>
<round>54</round>
<slot>~193</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
