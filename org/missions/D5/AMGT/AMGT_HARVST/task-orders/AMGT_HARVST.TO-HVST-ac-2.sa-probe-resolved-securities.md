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

## 1a. THE PROBE, AS AMENDED (AMENDMENT 1) -- it replaces section 1's steps 2-3

- **The probe is ONE script,** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~85/scripts/ac2_probe.py`,
  driving the collector's OWN client OUTSIDE the `Worker`:
  - `sessions.TokenFirstSessions(...).get("sa")` gives the stored token, the newest one. It never calls `refresh`.
  - It builds `publishers.Publisher("sa", envelope, record, ...)`.
- **Step 1, the account read, FIRST and ALONE:** `Publisher.check_auth()` (the sa account check, `contracts.json` sa
  `auth_check`). Record the status, the class and `authorized`.
- **Step 2, only on an authorized 200:** ONE live listing page, `Publisher.seeking_alpha(<Lenovo>, limit)`, live mode, page 1.
  - `<Lenovo>` is the collector's RESOLVED universe row: `universe(config)`, the row whose company is Lenovo, `sa_symbol`
    `LNVGY`.
  - Record the status, the class, hits, dated hits and pre-floor hits.
- **Any refusal STOPS the probe:** a 402, 401, bot check or no body. There is no `Worker`, so no sign-in path exists. The body
  is kept by the transport's own keeper, and the class is recorded.
- **Output:** `~85/ac2_probe.json` as {"security": {...}, "token_source": ..., "account": {"seq", "status", "class", "authorized",
  "body_kept"}, "listing": {"seq", "status", "class", "hits", "dated", "pre_floor"} or null, "sign_in_calls": 0, "refresh_calls": 0, "hosts": [...]}.
- **NO S3 write, NO upload, NO run record.** Stored articles are round 31's, on the cloud route.

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

**AMENDMENT 1 (issuer, 2026-09-30 ~18:0xZ, before the pair) -- the probe runs OUTSIDE the Worker (section 1a).**
- **Measured at `0814b408e4`:** inside the `Worker`, an sa account check that fails raises `AuthExpired`, and `ab-1` A2
  answers with a sign-in. A 402 raises `AccountUnavailable`, and `ab-3` A0 answers with a fresh sign-in. The analysis's condition
  is "a 402, 401 or bot check stops the leg (no sign-in)". A collector `run` would therefore contradict it.
- **Ruling:** the probe drives the collector's own `Publisher` on the stored token with no `Worker`, so no sign-in path exists.
- **Scope narrowed:** the `run` and the upload are dropped. The cell MEASURES the account and one listing page; storing articles
  is round 31's cloud collection (`CTO_RULING_CLOUD_COLLECTION_DESIGN_20260930.md`).
- **The security:** Lenovo, from the collector's resolved universe (89 rows, all with `sa_symbol`; Lenovo is `LNVGY`, INFERRED).
  The batch-1 names are absent there except Hon Hai and KDDI (ADR symbols).
- **`<paths>`:** add the probe script under `~85/scripts/` (already inside `~85/`). **Criteria:** the same two invocations.
- **Gate limb:** `to-pipeline-gate` grades a modified order's `<placeholders>` only (NONE).

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>30</round>
<slot>~85</slot>
<fabric>site-z</fabric>
