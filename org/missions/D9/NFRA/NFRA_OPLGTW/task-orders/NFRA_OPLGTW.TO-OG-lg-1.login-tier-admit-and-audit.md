# NFRA_OPLGTW task order -- `OG-lg-1` -- /login admits by tier (R24) and writes its own audit record

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-lg-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~22</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code change with tests; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the audit record uses the gateway's existing audit sink.
comp-adversary: DECLARED-NOT-APPLICABLE -- the spec is the CTO's (R22 item 2 and R24).
EGRESS CLASS, declared: NONE (local tests; no live call).
</preflight>

## 1. THE CELL -- `OG-lg-1` (decomposition addendum R3-T.13, item 1; CTO R22, R24)

Read first:
- `org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round18.md` section 6 (R22);
- `ROUND_ANALYSIS.round19.md` section 3 (R24);
- OA-e-10's own order and record under `org/missions` (NFRA_OPALAI), and its reverted commit `8ed37b3266`.

Background, in `infra/aws/ec2/opal-gateway/app/token_broker.py`:
- `/login` is the ONLY path that grants a person delegated Graph scopes (`:263-265`, `:365-385`).
- `NeedsLogin` (`:55-62`) sends a user there.
- `redeem_consent` writes the principal-keyed cache.

Build, on CLOUD source (`app/server.py` `login()`, the audit write site, and tests):
1. **The admit set.**
   - `/login` admits the server-held identities (`OTP_MAILBOX`, `MS_INGEST_IDENTITY`), PLUS every principal whose
     `tier.resolve_tier(...)` result carries at least one Graph-using tool. Define "Graph-using" from the tool
     registry; do not hand-list tools.
   - Restricted profiles are REFUSED (403).
   - An unresolvable tier REFUSES (fail closed).
   - Name the Analyst's service identity and prove the tier rule refuses it.
2. **The audit record.** Every `/login` request writes exactly ONE audit record through the gateway's existing audit
   sink. It carries:
   - an outcome of `admitted`, `refused` or `consent`;
   - the principal key, or the email as a digest;
   - the reason.

   Never write a token or a secret.
3. **Tests.** Write `tests/test_login_admit_r24.py` with six named tests:
   - `test_oglg1_ac01`: a non-restricted principal: NeedsLogin -> `/login` -> consent, and its principal cache is
     written;
   - `test_oglg1_ac02`: a restricted principal gets 403, audited;
   - `test_oglg1_ac03`: the server-held identity is admitted, as before;
   - `test_oglg1_ac04`: empty settings plus an unresolvable tier admit nobody;
   - `test_oglg1_ac05`: AS AMENDED BY A1 (R25.1). opalbloomberg@ (the Teams concierge, the `identity_scope` key) is
     ADMITTED at `/login`, AND its allowlist still DENIES an out-of-scope tool at dispatch;
   - `test_oglg1_ac06`: one audit record per request, with outcome, digest and reason.

   Negative control: with the tier clause removed, ac01 fails. Record that run.
4. **Admit-set computation, for the release.** Write `deliverables/0.9.0_WK_NFRA_OPLGTW~22/LG1_ADMIT_SET.md`, which
   explains how to compute the admit set BEFORE and AFTER over the current principal population, reading the access
   state READ-ONLY. OG-rl-8 runs it.

## 2. BOUNDS

- No release and no host write.
- No change to `token_broker.py` beyond what the audit record needs. If it needs more, file a row.
- No grant or state-store write.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/server.py
infra/aws/ec2/opal-gateway/app/audit.py
infra/aws/ec2/opal-gateway/app/token_broker.py
infra/aws/ec2/opal-gateway/tests/
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~22/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W22-S<k>` (next unused), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-lg-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r20/checks/lg1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)named tests passed 6 of 6; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-lg-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r20/checks/lg1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)test_principal_cutover.py rc=0 .*test_data_entitlement_guard.py rc=0 .*test_browser_oidc.py rc=0 .*test_login_admit_r24.py rc=0 .*one-process schwab floor \(ti2.AC1\) yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~22/NFRA_OPLGTW.TO-OG-lg-1.login-tier-admit-and-audit.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance>`, and on PASS edit this order's ONE `<status>` tag IN
PLACE to `complete`. Report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 20 (R3-T.13, item 1). Chain: `OG-lg-1` -> `OG-rl-8`.
- Pre-cut: see the issuance commit.

- **A1 (2026-10-06 ~07:1xZ, issuer, on CTO R25 @ec022d2734, msg 29941): REOPENED.** Drain 67bcd6d519 refused
  opalbloomberg@ through a `scoped_service_identity` clause, per R24. R25.1 withdraws that: opalbloomberg@ is the Teams
  concierge, whose allowlist is Graph tools, and a 403 at `/login` dead-ends it.
  - (a) Strike the `scoped_service_identity` refusal from `login_admit_decision`.
  - (b) Restate `test_oglg1_ac05`: opalbloomberg@ is ADMITTED, and its allowlist still DENIES an out-of-scope tool.
  - (c) R25.4: correct the docstring to the semantics in effect. `/login` has no principal on the GUI path, so
    `resolve_tier(None)` is the READ_ONLY floor, which carries read Graph tools. The rule in effect is "admit every
    verified, non-email-denied tenant identity". Restricted profiles are refused by the email-deny guard (W3-S22). The
    tier clause is a fail-closed backstop: an unverified provider, an unresolvable tier, or no Graph tool.
  - The audit record stays as built. Criteria are unchanged; `lg1.AC1` re-reads ac05's new meaning.

<status>complete</status>
<round>20</round>
<slot>~22</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
