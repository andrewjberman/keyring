# IRPT_BCKEND Round 17 — independent CVO review, 2026-09-22

Author: 3.0.0_SA_CVO~B. Input COO~B messages99540/99541 and L8 packet
org/missions/D9/IRPT/IRPT_BCKEND/ledger/IRPT_BCKEND_ROUND17_L8_COMPILE.md@bf671dc413.
This L8/L9 record supports REMEDIATION_v8; sole formal recipient CTO.

## Decision and grain

**The render contract is NOT PROVEN.** Recommend bounded offline repair/integration
before considering provisioning/deployment. Actual-module probes refute several
claims. This is not authorization to deploy, change keys, edit production source,
widen a worker grant or restart another project. All CVO execution was local and
synthetic; SDK sends in the companion harness throw NETWORK FORBIDDEN.

R17: signed PRD v0.17, text1450e05178, admitted stamp4f942b7657; decomp v0.21,
issuance86ba92ceb556a719dd523ee1036e53de873e5505, fanout3/3 cap8.
Review HEAD f05127795a88c899a0171a2ba8e9a020483239df; later census HEAD
a0e7fe8b3918f65a38d5feef764b2f9b03828f63. Relevant source pins below.

## Independently exercised component evidence

| Cell | Own fresh result | Meaning |
|---|---|---|
| IB-rtq-1 / R117-AC1 | pytest test_render_mint.py:14 passed | Mechanical PASS; not applied IAM/export-job wiring |
| IB-rtq-2 / R117-AC2 | worker wrapper19 passed/1 failed; direct resolver28 passed/1 failed | FAIL on merged trusted-header citation regression |
| IB-rtq-2 V2 supplementary | unmodified worker Node suite11/11 with one shared offline SDK identity | Component controls pass; probes expose omissions |
| IB-rtq-3 / R117-AC3 | node --test test_edge_render_delegate.mjs:19/19 | Invocation PASS; actual-V1/pre-existing-suite clauses NOT fulfilled |
| Existing _authz suite |141 passed | Existing assertions pass, not proof of new seams |

Wrapper subprocess:49 passed/1 failed in scope leg.
test_every_trusted_header_is_actually_injected_at_the_line_it_claims fails:
resolve.py's x-user-email citation says edge line400, now console.warn after V3
insertion. Isolated-worker and pre-merge passes do not establish merged pass.

First direct V2 test could not resolve bare jsonwebtoken. Companion --worker-v2
loads the unmodified worker test and maps SDK imports to one fake module identity.
No CVO install, live Secrets Manager call or production edit. This environment
issue is separate from the actual Python regression.

All three explicit-ID/governing-order-bound proof checks: VALID rc0, one acceptance
row each, zero violations. Worker14/15 resolve6/6 and8/8 refs. Worker16 checker
reports5 UNRESOLVED-HERE because refs are blobs, not commits; own git cat-file and
rev-parse verify5/5 real blobs exactly matching announced commits. Artifacts are
not missing; structural VALID is not behavioral PASS.

## PRD item7 compound judgments

Actual arms(a)-(k), PRD lines231-241, not invented J ids. PASS below is local/synthetic.

| Arm | Judgment | Evidence / limit |
|---|---|---|
| (a) minted token reads three routes | FAIL to establish required behavior | Real minter reaches both verifiers, but V3 output cannot resolve and published operations refuse; no three-object served read |
| (b) fourth route, swapped id, non-print refusal | PASS at component grain | Worker controls plus actual-minter swapped-id V2=false and non-print V3=401; no deployed request claim |
| (c) past-exp token refused | FAIL literal boundary at V3 | Token5s past exp accepted by V3, denied by V2;120s-past refused by V3. clockTolerance60 extends exp too. Missing exp accepted by both |
| (d) V3 poisoned admin/internal refused | PASS | V3 rejects all4 forbidden variants; V2's separate item2 failure remains |
| (e) V1 refuses render token | NOT_EVALUATED at required path | Copied library verify parameters, not actual verifyAccessToken execution |
| (f) unchanged human behavior | NOT fully established | Five new real-edge human controls and V2 controls pass; literal pre-existing full-suite baseline absent |
| (g) applied runner policy cannot read human signing key | NOT_EVALUATED | No applied policy inspected; no AWS permitted. Separate minter code does not prove IAM |
| (h) principal resolves and reads three objects | FAIL | Actual-edge headers UNKNOWN; marker repair control only proves classification |
| (i) post-mint revocation refuses next read | PASS at enforcer-fixture grain only | Real Enforcer positive control then EMPTY_GRANT after deps.revoke; whole chain unproven |
| (j) renderer without marker UNKNOWN | PASS at resolver grain | Worker actual classifier/trusted_only tests; origin marker still required |
| (k) outside pinned ids/operations refused | FAIL | Unlisted same-account report covered; mismatched bundle name accepted; allowed served names incorrectly refused |

Item2 separately fails at V2 for role=admin, firmRole=admin, tier=internal,
userType=Dev. Item6 audit fails: V2 accept/refusal records omit jti/render id.
Observed V3 expired record also omits jti; do not treat an unverified decoded id as
authenticated evidence. No existing-human aud/iss change rides on render remedies.

## Reproduction and controls

Companions (co-committed) at org/tier1_exec/3.0.0_SA_CVO/deliverables/:
IRPT_BCKEND_R17_PROBE.py and IRPT_BCKEND_R17_PROBE.mjs.
Run from root with py -3.12 / node respectively.
**Exit0 means counterexamples reproduced, NOT acceptance.**

Node harness uses existing edge-local jsonwebtoken, fresh RSA keys held in memory,
real minter via stdin/stdout pipes, real edge handler, real V2 branch and Python
resolver. No token/private key printed or saved; no production keys.

1. Actual-minter token accepted by V2/V3. Forwarded V3 headers -> UNKNOWN;
   adding only X-Origin-Verify=cloudfront -> RENDER_DELEGATE.
2. V2 accepts4/4 bypass-poisoned tokens; V3 rejects4/4. Both accept missing exp.
   V3 accepts5s-past expiry; V2 denies it; V3 denies120s-past expiry.
3. V3 forwards POST on allowed API URI. V2 restricts GET: boundary gap,
   **not evidence of served POST authorization bypass**.
4. V3 refuses /assets/index-fixture.js. portal/vite.config.ts has no base/assetsDir
   override. Available local dist/index.html references /assets/ chunks,
   /logos/opal-icon-color.svg and /favicon.png. This is an **unversioned local
   build**, not certified current or live. Require pinned manifest and page fixture.
5. Enforcer positive advisor-id-shaped delegator resolves. Same normal human
   resolves with actual advisor id/email subject, but email delegator refuses
   EMPTY_GRANT. _resolve_render_delegate reconstructs subject/advisor headers
   from one string instead of authoritative current identity.
6. Bundle loader sees tenant/revision only, not bundle id. Another bundle name
   accepted against same result. Different revisions produce equal cache keys.
   An unlisted same-account report is covered. This is identity/pinning/key
   evidence, not an observed live cache replay.
7. Actual normalized operations performance_report, analysis_report,
   narrative_packet each refuse OBJECT_NOT_COVERED. New allowlist uses
   performance, analysis_sections, narrative.
8. Revocation control refuses EMPTY_GRANT.
9. Naming(load_opal()).classify returns IAM_ROLE for all3 of x-user-role,
   x-advisor-role, x-firm-role. LGIC_ENFORCE register names COO~G.

## Source and evidence pins

| Artifact | Vintage / blob |
|---|---|
| minter mint.py and14-test suite |build bf31746c43; proof91d7a39b1a; drain5c00ec783a |
| _scope/resolve.py |4bca50737e /2943c14ca687f84dc6b59e9660a0c12b3aa352ed |
| _authz/enforce.py |4bca50737e /099f02eebcd525d02dee1c4829720401b77d5427 |
| portal-authorizer/index.mjs |4bca50737e /ed497753fdaaa84c58cf95ce8d1bb0753250d1bd |
| W15 proof/drain |c8561e2a69 /97e30deeb7 |
| edge/render_auth.mjs |b037f38d9d /60d9543bac8e38383e55ce97d074a1224a2e6f4f |
| edge/index.mjs |b037f38d9d /0d324cd8faadd1e8e9cbe69f2ec7048a17ccd9fb |
| W16 test |b037f38d9d /e8d63ce01a3bd1975166b0d515602f019ce42c6c |
| W16 result |b037f38d9d /bc547db7241430c50a8bf2613799682d8f3657d4 |
| W16 investigation artifact |5753678069 /7c94dd288046bc9bb04aad812a6d716ed1b26baf |
| W16 proof/drain |d7f02300a3 /66a73beea1 |

Also inspected: docs/contracts/investor-reporting/v1/routes.json;
infra/aws/lambda/investor-reporting/_authz/served.py key_operation and:635;
infra/aws/lambda/investor-reporting/export/bundle.py freeze:86-126
(real revisions/sections/assets, not new fixture identity shape);
.tools/naming-gate.py Naming.classify;
org/missions/D14/LGIC/LGIC_ENFORCE/project.json.
Portal source local HEAD a616b8d1fe2f2a88de72bcfeef009d02ba288767.
No portal source/build changed.

## L8 census and dispositions

Own terminal refuser0/103 open;8 unchanged terminal-by-proof/status-word exceptions:
rt-6,rtf-10,rtf-12,rtf-14,rtf-3,rtf-4,rtf-7,rth-7.
After append-only review, comp-surprise:354 investigation items,210 adjudication
rows,220 remediation rows,0 undispositioned,0 duplicate ids,177 ARMED row occurrences
across178 files. Intake354/198/208,11 open,176 ARMED occurrences across176 files.
Extra ARMED occurrence is C207 adjudicating the **same W16-S4 naming defect**,
not a second new hazard.171 OPEN rows at v15-or-earlier remain stale, unchanged.

W14-S1,W15-S3,W15-S4 dismissed with reasons. W15-S1/S2/S5/S6 and W16-S1/S2/S3/S4
graduated:8 worker remedies. C200/C201/C203/C210 add4 independent code remedies.
ADJUDICATION_v12 holds C199-C210; REMEDIATION_v8 holds12 new rows. No old clock moved.

FWD-2/3/4/8/11 NOT_REALIZED; other prior grades unchanged.
Five packet judgment calls answered: identity/bundle assumptions not accepted;
newly authored suite not called pre-existing; asset-prefix guess not accepted;
copied V1 parameters not actual-path proof; naming disarm owner COO~G.
W10-S2, S116/W1-S47, break-glass and existing stale clocks carry.
CTO alone receives formal slug after commit. Frontend remains its own team's scope;
IB-rti-6 latency follows frontend print branch and a functioning render-token chain.

