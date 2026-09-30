# AMGT_RESAPP task order -- `AMGT-ac-2` -- A D-1 REGENERATION KEEPS EVERY SERVED SENTENCE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ac-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~191</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence (no scheduled task invokes the producer: the CVO scanned 208).
comp-iam: DECLARED-NOT-APPLICABLE -- the check READS the stored objects; this order writes nothing to AWS.
comp-adversary: RUN by the issuer at the cut -- AC1 counts the stored document's served sentences against an in-memory rebuild; base: 8 lost.
EGRESS CLASS, declared: NONE. Opal's own S3, read-only.
</preflight>

## 1. THE CELL -- `AMGT-ac-2` (round 53, decomposition s.61)

`lib/research/filings/drafting_build.py` builds the D-1 drafting document (`build_drafting_document(analysis)`, `:324`) and rebuilds the
pool (`--rebuild-pool`, `_rebuild_pool`). Under C-VERBATIM-GATE = HOLD, `sections[].sentences` carries only SERVED-ON-SPAN sentences and
every HELD-NO-SPAN sentence goes to `held_no_span`. The stored documents were written before today's stricter verbatim gate, so a
regeneration DROPS sentences they serve: for ASML_NA_Equity (stored `drafting/v1/ASML_NA_Equity.json`), company_description 6 -> 1,
investment_thesis 1 -> 0, risks 2 -> 0 (row Z-S313/Z-S314, ARMED: any live `--rebuild-pool` regresses served /thesis sentences).

**Build:** a regeneration keeps every served sentence. Read why each dropped sentence is held under today's gate (the pipeline under
`lib/research/drafting/` and the producer here), and fix it at the cause, so a sentence the stored document serves verbatim-on-span is
still served on rebuild. Never loosen the verbatim gate itself: a sentence whose text is NOT found verbatim in the source stays held. If
the cause is that the stored sentences were served under an older, looser rule and genuinely fail today's gate, STOP and file a row with
the per-sentence evidence -- that is a ruling, not a build. Tests: a stored-served sentence survives a rebuild; a non-verbatim sentence
stays held.

## 2. BOUNDS

1. `drafting_build.py`, files under `lib/research/drafting/` (the drafting pipeline; NOT `schema.json`), and new test files. No live
   `--rebuild-pool`, no S3 write. Standing: no install, no push, no promote, no deploy, no vendor call, no model call. REFUSE, do not rescue.
2. Python from the repo root with `PYTHONPATH="$(pwd)"`.

## 3. SURFACES

<paths>
lib/research/filings/drafting_build.py
lib/research/filings/tests/
lib/research/drafting/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~191/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ac-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round53/checks/ac_2_keep.py; echo "exit=$?"</invocation><expect>every span-carrying stored sentence present in the rebuild; the count without a span printed; A D-1 REGENERATION KEEPS EVERY SPAN-CARRYING SERVED SENTENCE: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ac-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" timeout 115 python -m pytest lib/research/filings/tests -q; echo "exit=$?"</invocation><expect>N passed and 0 failed, N &gt; 127 (plus your new tests) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~191/AMGT_RESAPP.TO-AMGT-ac-2.regeneration-keeps-served-sentences.proof_of_spec.json`. Report once: why the sentences were dropped, what you changed, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-52 analysis item 2 / ruling 3 (disarms Z-S314). Base: AC1 FAIL (8 lost), AC2 PASS 127.

<status>pending</status>
<status>complete</status>
**AMENDMENT 1 (`2.0.0_SA_COO~Z`, 2026-09-30 ~14:0xZ):** the worker STOPPED per the cell's clause (row Z-W191-S1): the 8 sentences a rebuild drops for ASML are stored with `quoted_spans []` (none-found), non-verbatim, served vacuously before C-VERBATIM-GATE HOLD; the 2 span-carrying ones survive. CTO msg 27185: Z-S314 re-classified as HOLD working as designed; AC1 re-scoped to span-carrying stored sentences (`ac_2_keep.py` amended; on CLOUD: 2 of 2 kept, 8 held by design -> YES). The worker's slot closes the order on its branch (its record was not carried by merge 4b472c8249).
<round>53</round>
<slot>~191</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
