# TO ADVI_BILLING.TO-AB-e-1 -- E1: five live GET probes of the edge book check for household z08219260, with five synthetic 10-minute tokens minted under a ledger (CTO ADDENDUM 2)

<to_id>ADVI_BILLING.TO-AB-e-1</to_id>
<project>ADVI_BILLING</project>
<issued_to>0.7.0_AE_CloudOps~AB2</issued_to>
<issued_by>2.0.0_SA_COO~B2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>EDGEPROBE</workstream>

**Directive:** D8 | **Fabric:** dell2 | **PRD:** v0.2 @d45dc8a52f | **Decomp cell:** `AB-e-1` (decomposition section 3, round 2) | **outcome_ref:** FWD-1 (E1) | **depends_on:** none. **Authority:** CTO round-1 analysis ADDENDUM 1 @e5371f3e39 (msg 2825) and ADDENDUM 2 @abbf204c7e (msg 2920).

---

## WORKER FACE

**The cell.** The portal's CloudFront edge (`EVTSA9VEHNZVH`, behavior `/api/scoped/partners/*`, `auth-validator-edge:22`, source
`infra/aws/lambda-edge/auth-validator-edge/index.mjs:120,466-539`) admits an advisor to `/api/scoped/partners/books/relationship/{id}/*` only if
`{id}` is in `s3://opal-data-bd/platinum/49financial/ownership_map.json` under the JWT's `advisorId`; `role` or `firmRole` `admin` bypasses.
The API authorizer `opal-portal-authorizer` (`infra/aws/users/lambda/portal-authorizer/index.mjs:340-414`) refuses a request that did not come
through CloudFront. Prove both live, for household `z08219260`, with five GET probes.

1. **Open the ledger FIRST:** `python .tools/deploy_ledger.py open --slug advi-billing-edge-probes-r2-20261009 ...` with one `verify` leg
   per probe. `deploy_ledger.py` STAGES without committing: commit the sentinel and entry right after `open` and again after each
   `close-leg` and `close`, or the shared tree's drains are held.
2. **Mint five synthetic tokens** with the shared human-token signing secret (`infra/aws/lambda/shared/opal_auth/__init__.py` `SECRET_ID`),
   in the claim shape the auth handler mints (`infra/aws/opalinvest_dev/lambda/auth-handler/src/jwt.ts:168-185`; issuer `opal-portal-auth`,
   audience `opal-portal-api`, RS256), each expiring in 10 minutes, each `sub`/`email` synthetic `advi-billing-probe-<n>@example.invalid`:
   - `in_book`: `firmId` 49financial, `role` user, `firmRole` user, `advisorId` = one advisor whose map entry lists `z08219260`;
   - `out_of_book`: same, `advisorId` = a mapped advisor whose entry does NOT list it;
   - `firm_admin`: `firmId` 49financial, `role` user, `firmRole` admin;
   - `other_firm`: `firmId` mockadv, `role` user, `firmRole` user;
   - `execute_api_bypass`: the `out_of_book` claims, sent to the execute-api URL instead.
   Read the map once to pick the two advisorIds (advisorIds may be recorded; nothing else from the map).
3. **Probe, GET only:** the first four through `https://opalinvest.dev/api/scoped/partners/books/relationship/z08219260/fee-quarter/2026Q3`
   with the token as the portal sends it (read `infra/aws/lambda-edge/auth-validator-edge/index.mjs` for the cookie/header it reads); the fifth
   straight at `https://7k3ed8px20.execute-api.us-east-1.amazonaws.com/api/scoped/partners/books/relationship/z08219260/fee-quarter/2026Q3`.
   Record the status code only (no body beyond its first 80 characters of an error; never a 200 body).
4. **Never store or log a token or key byte** (not in a file, not in a commit, not in shell history you leave behind); discard them after use.
5. **Record** `AB_E1_PROBES.json` in `org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.7.0_AE_CloudOps~AB2/`: `ledger_slug`,
   `minted_at`, `minted_by`, `key_read_at`, `probes` = five objects `{class, method: "GET", route, via (cloudfront | execute_api), advisor_id
   (or null), status, error_head}`. Close each ledger leg with its status and the ledger itself.
   Expectations (stated, not graded here; the issuer reads the outcome): in_book 200, out_of_book 403, firm_admin 200, other_firm 401 or 403,
   execute_api_bypass refused (401/403).

<criterion id="AB2-1-AC1" cell_refs="AB-e-1"><invocation>python org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/checks/r2/r2_checks.py . AB2-1-AC1</invocation><expect>AB2-1-AC1 PASS</expect></criterion>
`AB2-1-AC1` -- five probes recorded (one per class, GET, an integer status, no token bytes) and the ledger closed. Base: FAIL.

<expected_criteria>AB2-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- GET only; five probes; one read of the signing secret, reported in the ledger and the record (time, actor), never its bytes; one read of the
  ownership map. No write to any AWS resource, no deploy, no change to any user, role or table.
- **Refusal clause.** A non-GET request, a stored or logged token or key byte, a sixth probe, or a 200 body in any file is a defect: stop and
  file a row.

<paths>
org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.7.0_AE_CloudOps~AB2/
org/critical_paths/change_management/advi-billing-edge-probes-r2-20261009.md
org/critical_paths/.open_deploys/advi-billing-edge-probes-r2-20261009.json
org/missions/D8/ADVI/ADVI_BILLING/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D8/ADVI/ADVI_BILLING/task-orders/ADVI_BILLING.TO-AB-e-1.edge-book-probes.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_BILLING/decompositions/ADVI_BILLING_DECOMP.md</decomp_doc> section 3 (round 2), cell `AB-e-1`.
<owned_cells>AB-e-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AB2-1-AC1. The instance goes at
`org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.7.0_AE_CloudOps~AB2/ADVI_BILLING.TO-AB-e-1.edge-book-probes.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> AB2-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the five statuses by class, the ledger slug and its closing commit, and every row id.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- reads only (five GET requests, one secret read, one map read); nothing written to any served surface.
comp-iam: RUN as a reading -- the signing-secret read is the act ADDENDUM 2 authorises; it is reported after the fact in the ledger.
comp-routes: RUN as a reading -- the probed route and the edge behaviour are the existing ones; none is modified.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: GET probes through the existing behaviour; no cache surface changes.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: the probe IS the measured read of the gate.
checks dry-run at base: AB2-1-AC1 FAIL as expected.
lane: the <paths> block IS the grant. Reassigned from the issuer's own act to 0.7.0_AE_CloudOps~AB2 (a fresh lane, seated by 0.0.0_AB_MSTR~DELL2 msg 2931) per ADDENDUM 2 (the minter runs the probes so
no token leaves its session).
</preflight>
