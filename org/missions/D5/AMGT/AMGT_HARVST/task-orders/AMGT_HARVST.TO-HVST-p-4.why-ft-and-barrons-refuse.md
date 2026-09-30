# AMGT_HARVST task order -- `HVST-p-4` -- ROUND 26 chain 4 of 4: WHY ft AND barrons REFUSE THE COLLECTOR -- a LOCAL read of the request path, headers, challenge handling and signed-in session path, with NO request sent (FWD-1, FWD-9)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-p-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~69</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- the collector's Scheduled Task is Disabled with 0 triggers; this cell runs nothing.
comp-iam: RUN at L5 -- local reads only (code, recorded events and run artifacts; session files are read for SHAPE and age only, never decrypted content). NO request to any publisher, NO browser opened, NO login, NO S3 write.
comp-adversary: RUN at L5 -- the adversary is a cause asserted without the recorded response (e.g. "cookies expired" with no evidence), or a "route to a clean fetch" that is really a challenge bypass. AC1 prints the recorded response evidence for every refusal it explains; the route must stay inside the collector's own scripted session path (R-21) with no challenge solving.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO REQUEST TO ANY PUBLISHER.** No browser opened, no login, no challenge solved, no collection run, no S3 write.
   - The runtime root `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest` is READ-ONLY.
   - Read session and credential files for their presence, age and shape only. Never print their contents.
2. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~69/scripts/`; outputs named `p4_*`
   -- **never `.scratch/`.**
3. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~69/AMGT_HARVST.TO-HVST-p-4.why-ft-and-barrons-refuse.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-p-4.why-ft-and-barrons-refuse`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~69/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE QUESTION (`ledger/ROUND_ANALYSIS.round25.md` @`300ea99310`, ruling 4)

**Recorded (HVST-o-5, 2026-09-30):**
- barrons (attempt 1, `runs/20260930T040818Z-barrons-cfedbf8fb4.json`): `request_rejected`, "Publisher verification challenge from
  www.barrons.com". The collector's own scripted reauth ran once, and the retry was rejected.
- ft (run `20260930T044003Z-run-b75f9299`): `request_rejected`.
- bbg and wsj fetched cleanly in the same runs.
- The collector's rejection branch is `lib/opal_data_harvest/worker.py` ~:427. Its request and session code is under
  `lib/opal_data_harvest/` (`publishers.py`, `transport.py`, `auth.py`).
- The HARVST commissioning record (`org/tier1_exec/4.0.0_SA_CRO/deliverables/HARVEST_COMMISSIONING_20260915_W.md`) describes the
  barrons recovery path and its limits.

**Measure, and change nothing:**
1. For ft and for barrons: the recorded response (status, host, path, size, the challenge marker) from `events.jsonl` and the
   `runs/*.json` files. Put it beside bbg's and wsj's successful responses in the same runs.
2. The request each publisher's code sends: headers, the session envelope's source and age, and the transport. Name where ft
   and barrons differ from bbg and wsj, by file:line.
3. **The cause**, and the SMALLEST route to a clean fetch inside the collector's own scripted session path (R-21: scripted,
   never an agent turn; no challenge solving, no login by an agent). Or a stated limit with its reason.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 600). TWO mechanical

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-p-4"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~69/scripts/p4_ac1_refusals.py</invocation><expect>for each of ft and barrons: every recorded request/response event of the o-5 runs for that publisher (count printed, 0 named as 0) beside bbg's and wsj's, the session envelope's presence/age/source (no content), and the request difference from bbg/wsj by file:line</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-p-4"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~69/scripts/p4_ac2_route.py</invocation><expect>per publisher, the cause stated with the evidence line it rests on, and either the smallest scripted route to a clean fetch (the code or session step, and what act it would need: a pair, Andrew's word, or none) or a stated limit; the script makes no network call (it asserts socket creation is blocked while it runs)</expect></criterion>
</proof_of_spec>

## 3. WHAT THIS CELL DOES NOT DO

No request, no login, no fix. The route it names is cut in a later round.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):** `ROUND_ANALYSIS.round25.md` s.4 item 4 and ruling 4. This is a read-only cell, so no pair is needed.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>26</round>
<slot>~69</slot>
<fabric>site-z</fabric>
