# NFRA_OPLGTW task order -- `OG-e-1` -- ROUND 2 (R2-k): the email-keyed deny record and its guard (row W3-S22), BUILD only

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-e-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~7</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code change; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the operator role and grant-writer Lambda already hold PutItem on POLICY#* (terraform/opal-gateway/schwab_access_state.tf:154-158, mcportal_grant_writer.tf:87-91); runtime GetItem is unconditioned (:99).
comp-adversary: DECLARED-NOT-APPLICABLE -- the design and its five calls are ruled (RULING_R2-k_FIVE_CALLS_20260927.md @2ae58221ab).
EGRESS CLASS, declared: NONE. No AWS call, no deploy, no data write.
</preflight>

## 1. THE CELL -- `OG-e-1`

**The defect (row W3-S22).** The restricted profile is keyed by Entra tid/oid. But five browser routes and one branch identify the
caller only by the ALB email, before any read or credential exchange:
- the routes `/login`, `/sprint`, `/sprint/`, `/sprint/archive` and `/sprint/{day}`;
- the legacy-consent branch of `/callback`.
So a person holding a restricted profile can reach them with an ALB session.

**The ruled fix.** Read these two files in full first (paths relative to the repo root):
- `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/R2-k_EMAIL_DENY_CELL_DESIGN_20260927.md`, the design with file:line citations;
- `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/1.0.0_SA_CTO~O/RULING_R2-k_FIVE_CALLS_20260927.md`, the five rulings.
Build it exactly as designed. `GW` = `infra/aws/ec2/opal-gateway`.
1. **Record** (`GW/app/access_state.py`).
   - Add `email_deny_key(email)`: pk `POLICY#EMAILDENY#<sha256hex("og-email-deny/v1|" + email.strip().lower())>`, sk `email_deny`.
   - Add the POLICY record type `email_deny`, body `{tid, oid, status:"active"}`, no TTL.
   - Relax the one-partition transaction rule to "the principal's partition plus at most `email_deny` puts".
   - Runtime writes stay refused.
2. **Guard** (`GW/app/data_entitlement.py`): `email_denial(email, store)` returns 403 when a deny record exists, 503 with `Retry-After` when the table is unreadable (FAIL CLOSED, ruled), and None otherwise. Run the lookup in the thread pool under a time budget, as `GW/app/browser_oidc.py:170-175` does.
3. **Hooks.**
   - `GuardMiddleware`, right after `enforce(email)` (`GW/app/server.py`, near :206). One hook covers `/login` and the four `/sprint*` routes, before any S3 read or consent URL.
   - The legacy `/callback` branch, before `redeem_consent` (near :483-485).
   - A second check on the validated principal email inside `GW/app/token_broker.py` `redeem_consent`, after the principal is validated and BEFORE the cache writes (near :337-340).
4. **Writer** (`GW/ops/schwab_entitlement_admin.py`).
   - A restricted `activate` puts one deny record per supplied email, one record per alias as ruled, in the SAME single transaction. The condition is `attribute_not_exists(pk) OR (tid=:tid AND oid=:oid)`.
   - Emails come from the candidate (repeatable) or else the stored profile. With neither, it refuses.
   - `revoke` KEEPS the deny records (ruled).
   - A new one-shot mode `deny-backfill --tid --oid --email (repeatable) --approver --source-authorization` strongly reads an existing profile of any status. It writes its deny record(s) plus one audit item in one transaction, and refuses when no profile exists.
5. **Tests** (moto is NOT installed and may not be installed).
   - New `GW/tests/test_email_deny.py`, exactly 10 tests, through the existing seams: `AccessState(client=stub)`, the `store=` arguments, and `server.app` in a Starlette TestClient with the ALB check stubbed (the `GW/tests/test_owner_gate.py:36-93` pattern):
     - key shape and normalisation;
     - a runtime write is refused;
     - the 5 routes return 403, with S3 and the consent URL untouched;
     - a non-denied email gets 200;
     - a store error gives 503 on all 5 routes;
     - legacy `/callback` returns 403 with `redeem_consent` never called;
     - a restricted `activate` puts the deny record in the same single transaction;
     - revoke leaves the deny record;
     - backfill writes one transaction;
     - backfill refuses when no profile exists.
   - Give `GW/tests/test_owner_gate.py` a stub store where `/sprint` now reads the table (near :152-163). Do not weaken any assertion.

## 2. BOUNDS

1. Code and tests only. No AWS call, no deploy, no Lambda build, no data write. The contract (`org/standards/NFRA_OPLGTW_CONTRACT.json`) is already amended by the CTO; do not edit it.
2. Every test run sets `AUDIT_PATH` to a temp file, or the suite appends to the TRACKED `GW/audit.jsonl`. If that file is ever dirtied, restore it to HEAD and never commit it.
3. Standing: no push, no vendor call, never `git stash`. REFUSE a criterion you cannot meet as written, and report it with its measurement. Never repair or widen a criterion.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/access_state.py
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/app/server.py
infra/aws/ec2/opal-gateway/app/token_broker.py
infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py
infra/aws/ec2/opal-gateway/tests/test_email_deny.py
infra/aws/ec2/opal-gateway/tests/test_owner_gate.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~7/**
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/**
</paths>

Rows: `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md`, id `NFRA_OPLGTW-Z-W7-S<k>`,
fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-e-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/ek.AC1.sh; echo "exit=$?"</invocation><expect>10 passed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-e-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/ek.AC2.sh; echo "exit=$?"</invocation><expect>24 or more passed, none failed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-e-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/ek.AC3.sh; echo "exit=$?"</invocation><expect>deny-backfill --help rc=0 flags missing=0 of 5 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance to `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~7/NFRA_OPLGTW.TO-OG-e-1.email-deny.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>`. Report once:
- the diff stat per file;
- the 10 test names;
- AC1-AC3 literal output;
- that GW/audit.jsonl is clean at HEAD;
- commit hashes;
- rows.

<!-- ===================== RECORD FACE ===================== -->

# pipeline-override: supplementary round-2 cell on the CTO's ruling (97251, re-affirmed @244cd0d80f, five calls @2ae58221ab) after the re-seat @6fba157e76 made this seat OPLGTW's COO; W3-S22 is due before the next restricted grant. Round 1's OG-v-4/OG-v-5 are HELD behind it per the 09-18 ordering.

**ISSUER NOTES:** Dry-run at base (CLOUD @2ae58221ab+):
- AC1 FAIL ("no tests ran": the suite does not exist);
- AC2 PASS at 24 passed, the regression guard's base value, measured 13:41Z;
- AC3 FAIL (rc=2, flags missing 5 of 5).
The checks isolate AUDIT_PATH; the tree was clean after the dry run. The prd-signoff status reads both halves SIGNED at @2ae58221ab (the CTO, msg 20260927T133904Z). Build only: the narrow release, the Lambda rebuild and the backfill are separate cells, each under never-widen. The backfill for the one live profile waits on Andrew's open card.

<status>pending</status>
<direct_act>true</direct_act>
<round>2</round>
<slot>~7</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
