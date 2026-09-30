# AMGT_HARVST task order -- `HVST-ac-2` -- ROUND 30 chain 2: THE SEEKING ALPHA PROBE ON RESOLVED SECURITIES -- AN ACCOUNT READ WITH THE STORED TOKEN FIRST, THEN ONE LISTING FOR ONE RESOLVED NAME, UNDER A PAIR (FWD-1, FWD-9)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ac-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~85</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- the collector task is Disabled; one sa account read and one sa listing job, and its upload. It enables nothing.
comp-iam: RUN at L5 -- vendor egress to Seeking Alpha by the collector's own code only (R-21 @b390c36444); the stored sa token (the newest of the Secrets session and the saved-session file). S3 PUTs: the persisted run record, and the upload's sa bronze and silver. NO DELETE, NO other publisher, NO gold write, NO deploy, NO sign-in.
comp-adversary: RUN at L5 -- the adversary is a probe that never touches the account (round 29's vacuous probe, row Z-S47), or a refusal read as expiry. AC1 requires an account-read attempt row with its status before any listing row; AC2 reads Z-W37-S4's standing from that status.
</preflight>

## 0. BEGIN ONLY WHEN ALL THREE HOLD

1. BOTH never-widen halves are COMMITTED and named in the dispatch:
   - the COO half, `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round30/NEVER_WIDEN_HALF_COO_AC2.md`;
   - `1.0.0_SA_CTO~Z`'s half.

   **Act only inside them.**
2. The issuer's checks exist at `.../round30/checks/`, and the act-start gate there prints OK.
3. No other WORLD act of this project is in flight.

## 1. THE ACT (each command that reaches a put is named in the halves)

1. **The account read, FIRST and ALONE:** with the stored sa token, read the sa account endpoint through the collector's own
   client. Record the status and the attempt class.
   - A 402, 401 or bot check STOPS the leg: no sign-in, and the status is recorded.
   - This gives row `Z-W37-S4` its measured standing.
2. **Only on an account 200:** ONE collector `run` for ONE security from the collector's RESOLVED universe (a non-empty
   `sa_symbol`), `--publishers sa --max-jobs 1`. The halves name the security and the argv. Never use the gold universe file.
3. **Upload, ONCE,** capped at the printed pending count.
4. **Run AC1 and AC2.**

Rollback is forward only.

## 2. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~85/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 3. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ac-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round30/checks/ac-2.AC1.py</invocation><expect>AC1 RESULT: PASS</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-ac-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round30/checks/ac-2.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- `ROUND_ANALYSIS.round29.md` @`d0bc0a79f0` section 4 item 2, ruling 3.
- **`Z-S47` is closed by construction:** the security comes from the collector's resolved universe (`universe()`, via
  `--all-securities`), which carries `sa_symbol` from the resolved-symbols file (`__main__.py` ~:16). The gold universe file
  is never used.
- **The checks and halves are issuer-written before dispatch.** The halves name the account endpoint (from `contracts.json`
  sa `auth_check`) and the one security.
- **AC1:** no pre-existing object moved; no write outside the sa root and one run record; the account-read attempt row
  precedes any listing row; the outbox is empty after the upload.
- **AC2:** the account status and class; `Z-W37-S4`'s standing (402 PERSISTS / CLEARED); the one job's status, span,
  measured pages and stored articles, or its refusal class.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>30</round>
<slot>~85</slot>
<fabric>site-z</fabric>
