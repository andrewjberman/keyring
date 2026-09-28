# AMGT_HARVST task order -- `HVST-w-5` -- ROUND 12 chain 3 of 4, cell 1 of 2: the bbg `search/query` REFUSAL DIAGNOSTIC -- ONE bounded call pair, no repair path, no login

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-w-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~37</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates; this cell writes no bronze, silver or gold and arms nothing.
comp-iam: RUN at L5 on the DESIRED plane -- secretsmanager GetSecretValue on bloomberg/session (the transport's own designed read; the VALUE is never printed or written). No S3 write.
comp-adversary: RUN at L5 -- the adversary is a diagnostic that trips the producer's own recovery path (headed Chrome press-and-hold, a metered vision-model call, or a credentialed login) and so spends an act Andrew's word does not cover. Section 0 routes around that path entirely.
</preflight>

## 0. THE STANDING CLAUSES, first because they are absolute

1. **ANDREW'S WORD, AND ITS LIMITS** (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_1805Z_OPEN_CALLS_FOUR_RULINGS.md`
   ruling 2): `w-5` YES, **one bounded run, diagnostic only, no data written**, from a SCRIPTED producer, never
   inside an agent turn, ledgered by the seat that runs it. **One run = ONE `/user-info` call and ONE `search/query`
   call, total.** No retry.
2. ⛔ **DO NOT USE `python -m lib.opal_data_harvest run` FOR bbg.** On a 403 that path calls `repair_verification`
   (`lib/opal_data_harvest/worker.py:274-284`), which opens a HEADED Chrome press-and-hold (`verification.py:84,
   114-132`) and can call the metered Kimi vision API (`verification.py:123-125`); on `AuthExpired` it calls
   `sessions.refresh()` -- the CREDENTIALED login (`worker.py:285-293`, `auth.py:86-89`). **None of those is covered.**
   Use the estate's scripted transport instead: import `check` and `search` from
   `org/tier1_exec/4.0.0_SA_CRO/scripts/bloomberg_rest_fetch.py` (it rides the PARKED session `bloomberg/session` and
   never logs in). If ANY browser, login or vision call starts: STOP, file a BLOCKING row, report.
3. ⛔ **A credential, cookie or session VALUE is never printed, logged or written.** You may print the session's
   `captured_at` and cookie NAMES and COUNTS.
4. ⛔ **THE LEDGER IS A CONDITION OF THE WORD.** Append ONE `## CALL 1 -- bloomberg.com, <UTC>` entry to
   `org/missions/D5/AMGT/AMGT_HARVST/ledger/VENDOR_CALLS_0.9.0_WK_AMGT_HARVST_37.md` (create it; the shape is
   `ledger/VENDOR_CALLS_0.9.0_WK_AMGT_HARVST_22.md` CALL 1: seat, vendor, endpoint class, mechanism, agent-turn
   fetch?, scope, authorization, credential used, re-auth fired?, result, bytes retained, S3 written, spend,
   evidence) **in the SAME commit as the evidence.**
5. **Scripts in** `.../deliverables/0.9.0_WK_AMGT_HARVST~37/scripts/` -- **never `.scratch/`.**
6. ⛔ **INSTANCE NAMED EXACTLY**
   `.../deliverables/0.9.0_WK_AMGT_HARVST~37/AMGT_HARVST.TO-HVST-w-5.bbg-search-refusal-diagnostic.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-w-5.bbg-search-refusal-diagnostic`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~37/
org/missions/D5/AMGT/AMGT_HARVST/ledger/VENDOR_CALLS_0.9.0_WK_AMGT_HARVST_37.md
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

Read-only, never write: `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest/` (the MAIN tree's
runtime root: `progress.sqlite3`, `events.jsonl`, `verification/*-bbg-*/`). A linked worktree has no `.runtime`.

## 1. THE QUESTION -- row `AMGT_HARVST-Z-S32`

bbg `search/query` returned **9 x 200 and 12 x 403**, every 200 on 2026-09-15; `login.bloomberg.com/user-info` read
**200 on 12 of 12**. Every 403 body is **exactly 535 bytes**. Each 403 opened a press-and-hold with
`credentials_entered:false`, ended `recoveries=0`, then `request_rejected` (row `Z-S32`,
`INVESTIGATION_v1.md` ~:1610-1632). **FWD-1's five-publisher population is unreachable until this is explained, so no
bbg capture is planned before it** (decomp `s.20.5`).

**A correction to the decomp's starting hypothesis, measured at the cut:** all 8 traced bbg holds
(`verification/*-bbg-*/hold-trace/pixels.csv`) fill smoothly to a plateau (~145) and never drain -- the largest drop
from peak is 0.136, below the solver's 0.15 drain trigger (`press_and_hold_lib.py:137-138`) -- **and the one
SUCCESSFUL verification (`20260915T044035Z`) has the same trace shape.** So the pixel trace does not discriminate
success from failure; do not spend the diagnostic on it.

## 2. WHAT THE ONE RUN MUST CAPTURE

For EACH of the two calls: HTTP status, response byte count, response headers (names and non-credential values), the
body classified (for a 403: which challenge/bot-wall markers it carries, its title, and whether it is byte-identical
in structure to the stored 535-byte bodies). Plus the parked session's `captured_at` age at call time and its cookie
names/count. Then, OFFLINE, set the result beside the stored 09-15 200 evidence and the stored 403s, and state which
hypotheses the evidence discriminates (e.g. session-age, endpoint-specific bot wall, query-specific, header or
fingerprint class) -- each with the observation that supports or rules it out.

## 3. PROOF OF SPEC (each invocation LITERAL; timeout 600). TWO mechanical criteria

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-w-5"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~37/scripts/ac1_one_call_pair.py</invocation><expect>ONE /user-info call and ONE search/query call (query "Lenovo"), through bloomberg_rest_fetch.check / .search on the parked session, each with status, bytes, headers and body classification printed; the search call's non-200 is CAUGHT and recorded, never retried; the session captured_at and age printed; "browser_started: False", "login_attempted: False", "vision_call: False" printed as measured facts of the run; the ledger CALL 1 entry printed as written. A 403 is an accepted outcome and the point of the cell</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-w-5"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~37/scripts/ac2_discriminate_offline.py</invocation><expect>OFFLINE (no network; run with HARVEST_REFUSE_NETWORK=1 set by the script): AC1's captured responses set beside the stored bbg evidence under the main tree's .runtime/opal-data-harvest (the 09-15 200 receipts and the stored 403 bodies, each counted with its denominator), and a table of hypotheses with, per hypothesis, SUPPORTED / RULED OUT / NOT DISCRIMINATED and the observation behind it. The verdict line names what a bbg capture would need before it is plannable, or states that the run could not discriminate and what single further observation would</expect></criterion>
</proof_of_spec>

## 4. WHAT THIS CELL DOES NOT DO

No capture, no bronze/silver/gold write, no repair, no browser, no login, no vision-model call, no second call.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **Routing around the producer is the whole design.** The decomp's `s.20.5` card assumed the diagnostic starts
   from the solver's drain; the fact sheet at the cut (pixel traces, 8 of 8 plus the one success) shows that
   trace cannot discriminate. The mechanism that CAN is the raw response of the two endpoints, and the estate's
   own transport returns it without touching the repair path.
2. **"Scripted, never an agent turn":** the call is made by a committed script invoking the estate's transport
   module, re-runnable, ledgered -- the same mechanism class as `HVST-v-2`'s CLI invocation.
3. Base: both criteria FAIL at the base by construction (the scripts do not exist); scripts are worker-written as
   in every prior round of this project, with the expected output stated in each criterion.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>12</round>
<slot>~37</slot>
<fabric>site-z</fabric>
