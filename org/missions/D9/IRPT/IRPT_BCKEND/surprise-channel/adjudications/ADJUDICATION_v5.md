# IRPT_BCKEND -- round 9 L8 compilation and L9 adjudication

Author: `3.0.0_SA_CVO~B`. Evidence snapshot `76dbec51e67a3f401390f1f4fa46f9cb560bb06a`; review 2026-09-21/22 UTC.
Packet: `ledger/IRPT_BCKEND_ROUND9_L8_COMPILE.md@76dbec51e6`, independently read as blob
`50fd917ca12e8cb1133b407748d7c04d2d56ee96`. File v5 is a rollover counter, round is 9.
This is the L9 evidence carrier; `remediations/REMEDIATION_v3.md` is the single L10 slug.

## Receiving check and measured limb

| Read | Measurement |
|---|---|
| Home / placement | Tree `org/missions/D9/IRPT/IRPT_BCKEND`; project.json names laptop/LAPTOP, active, EXECUTING. Flat index is not a second project. |
| Issuance | `eecaad4985`, six cells; fanout 3 of 4 chains, cap 8; two issuer-discharged, three executed, one staged then parked. |
| PRD / decomp | PRD v0.15; decomp machine header v0.13/round9. Decomp diff issuance -> packet empty: no within-round decomp movement. |
| Task orders | Canonical `_open_tos_for_project` independently returned 0 open /91, with 8 admitted by valid proof despite nonterminal status words. |
| Packet checker | `receiving-check.py`: UNCHECKED, no checker for a drain packet. Acceptance here is CVO judgment. |
| Three proof instances | All 3 ACCEPT via bound proof-of-spec-check, 7+3+3 acceptance rows; re-run with explicit expected id sets also VALID. The checker does not grade truth. |
| Pin limits | rti-1: 14 bare blob refs announced UNRESOLVED-HERE; all manually resolve as blobs, 12 equal HEAD, two stale. rti-3: six bare blobs manually resolve/equal HEAD; one commit-pinned artifact accepted by checker. rti-2: five artifacts resolved by checker. |
| Channel intake | `comp-surprise`: 336 investigation items, 144 earlier adjudications, 184 earlier remediation rows, exactly 7 undispositioned worker rows, 173 filed armed, zero defects/malformed/duplicates. |
| Worktree / residue | No project or cited production-source dirty paths before this act; no IRPT_BCKEND round9 branch/worktree remains. Other project worktrees and 22 historical stashes untouched; no attribution of those to this round. |
| Limbo / role | OPEN-ROUND at L8/L9; this seat owns the next act and is producing it. No peer-stall inference. EXECUTING is consistent with this limb; old narrative phase text is not the instrument. |
| Watermark / ACK | Seven intake rows read and dispositioned below. No separate surprise watcher was launched; launcher runtime unchanged. Requested `ack_messages` capability is not exposed; no broker READ stamp claimed. This L9 artifact is the receipt. |

## Three judgments, and the non-verdict boundary

- **R91-AC7 FAIL.** Static source reading IS an admitted basis for the positive marker: at portal
  `8894e765ac`, App.tsx:576 mounts PrintEntry only behind requireAdmin+requireInternal, and
  ProtectedRoute.tsx:29-31 refuses unauthenticated state before children at :61. The production JSX
  marker exists in PrintEntry's five phases; a no-bundle/refused report phase is evidence of passing
  the auth guard, not of a report being renderable. No real browser or deployed portal revision was
  verified. The failure is separate: initial navigation discards its response and ignores intermediate
  hops. The new six-arm CVO diagnostic catches exactly the gap the worker's passing origin arm misses.
- **R92-AC3 PASS, source-provenance only.** Both source paths remain tracked; pinned historical blobs
  are genuine sources and no copy of live files was committed. CVO independently rehashed each LF blob
  and its CRLF form, matching the recorded member hashes. CRLF-only never means byte-identical.
  The cut's arm (b) literally required STOP on byte difference; this was a disclosed worker deviation,
  not a silent permission to reinterpret it. The later CTO/issuer declare-only termination is explicit.
  This judgment's three provenance limbs are satisfied, not the separate identity token.
- **R93-AC3 NOT_EVALUATED for both buckets.** It expressly chooses that verdict for the non-verdict
  branch. Recorded census: 258 roles +7 users; 11 non-exempt trust-admitted candidates per bucket,
  all implicitDeny, 0 eligible; 0 non-exempt attempts, 0 successful bucket controls, 0 attributable
  negatives. The simulator's allowed control tests the simulator, not either fence. CVO did not
  re-run IAM live or certify the handwritten trust parser as an exhaustive general-purpose analyzer.

R92-AC2 and R93-AC2 are mechanical criteria with recorded `UNCOMPUTABLE-BY-CONSTRUCTION`.
Neither receives a manufactured PASS, nor a new CVO `grades` entry pretending it was judgment.
For R92 the comparison actually ran and disclosed a substantive mismatch; the no-token label is
not evidence of member identity or of an impossible comparison. For R93 the exercise itself
could not run with the identified principals. Rti-2 terminates by the express declare-only
amendment; rti-3's original completion clause permits its measured non-verdict while L4 remains OPEN.
Those are task terminality decisions, not outcome grades.

R96-AC3 is substantively issued, but rti-6 was never handed/executed and its instance is ABSENT.
No fictional `path@pin` grade is minted. The human park `4a773b6ae3`, written on the face at
`278c011886`, permits round close only. R77-AC2 stays NOT_EVALUATED historically.
The prior answer on rth-7 stands: honest pending plus a valid proof is gate-terminal, not a PASS
conversion. Eight such words need no false completion flips.

## Counterexample and deployment boundary

The actual source blob is `ea60b932bd4fd8af1f08548ce51022c2740af8b2`, LF SHA256
`5b26be9133ae468ddb55af4e34be860f7f2d7338dea496bfd71f0c43f5a01d23`.
The Windows disk diagnostic SHA256 is
`5e0270e4a0f5534fea93de180d558d19ffa2bbb1385bc14c3f188bb871440d21`;
these are different byte grains, not drift. All Playwright, filesystem-write and prompt operations
were stubbed; no credential, real browser, portal network request or session file was used.

| R9 diagnostic arm | Capture writes | Success | Initial chain read |
|---|---:|---|---:|
| Same-origin positive | 1 | yes | 0 |
| Initial portal -> foreign -> portal | 1 | yes: counterexample | 0 |
| Initial final URL foreign | 0 | no | 0 |
| Verification portal -> foreign -> portal | 0 | no | 0 |
| HTTP500 verification | 0 | no | 0 |
| Missing positive marker | 0 | no | 0 |

CVO also re-ran the existing command, readiness and origin arms unchanged; all printed their
tokens. Thus the failure is the battery's uncovered initial-hop case, not a broken local harness
or a tool that refuses everything. The initial and verification responses are independently
modeled; only the former chain changes in the decisive pair.

Publish is supported by the signed packet, two halves, committed publish output and the closed
one-leg S3 ledger; the packet separately carries COO's 23:30:42Z live readback. Those are inherited
event reads, not fresh CVO S3 measurements. The .sh blob is `d704adfb7b6a3ee904c3ba7173eb81533679c97b`,
SHA256 `17ae44f0d6ee0a2f30225a99446f74c33fb82ce893026bb9852d211581ef89e0`.
No on-host hash proof exists. The runbook skips delivering/checking those two fixed bytes before
executing its local wrapper; the documented sync is in an unscheduled render Command document,
not a host-start effect. No actual old-host-byte state or credential leak is asserted.

## FWD coverage, read against the actual PRD cards

**FWD-2 remains SPLIT / NOT_REALIZED overall.** The earlier refusal-side realized grade and round-8
3/3 serving-route advance are carried, not replayed. This round provides tooling/source prerequisites,
not authorized-and-unauthorized replay over every suggestion/membership/report/poll/cache/PDF path,
nor a real export round trip. The parked latency measurement and unbuilt submit path remain.
Do not collapse the outcome into the capture helper's status.

**FWD-11 backend contribution is ADVANCED, overall NOT_REALIZED.** Its actual card requires an
Opal-signed-in Global view, clients at two firms, report AND export on each, advisor refusal and
same-client/revision parity. It is not merely a bucket program. The 0/2 L4 discrimination result
does not realize that card; no new Global session evidence exists here. IRPT_FNTEND owns the
whole outcome, CTO owns formal completion grades. No project closure or PRD addendum is issued.

## Prior clocks and carried work

Only five prior rows' allowed clocks advance in REMEDIATION_v2: C-S125/C-S126 source remedies
REMEDIATED but DISARM stays ARMED and closed=false until host delivery/verification; W3-S51,
W1-S46 and C-S144 close on issuer corrections. W1-S46's disarm timestamp is this CVO evidence
attestation, not the original correction's wall time. All old `round` and `remediation.round`
values, mechanisms, owners and evidence remain immutable. C-S127 stays OPEN/ARMED; new C-S153
names its surviving navigation defect. C-S156 separately names the distribution/runbook gap.

The earlier 150 stale owned rows are not closed, re-aged or independently re-investigated here.
S116 and W1-S47 remain the CTO's own-lane external carries; no IRPT recut changes lib/opal_naming.py.
Break-glass deletion stays CRO/Andrew's decision. S102's buildability advances, not a silent closure
of its entire historical row; W10-S2 keeps the served-state residual explicit. Conditional
listAnalysisRequests work is not newly authorized by this review.

## Machine-readable adjudication

```json
[
  {
    "id": "IRPT_BCKEND-C-S145",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T00:01:05Z",
    "one_line": "Round-9 judgment record: capture FAIL; source provenance PASS; L4 NOT_EVALUATED.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "L9 grades the three issued judgment criteria, not the worker tokens.",
    "world_is": "R91-AC7 fails its universal redirect bar on a grounded counterexample; R92-AC3 meets source-provenance bar; R93-AC3 takes its explicitly issued non-verdict branch.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rti-1.the-capture-tool-repaired-command-readiness-origin.md R91-AC7 @76dbec51e6",
        "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rti-2.the-ycharts-generate-source-members-resolved-or-named.md R92-AC3 @76dbec51e6",
        "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rti-3.the-l4-negative-control-on-a-discriminating-instrument.md R93-AC3 @76dbec51e6"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "notes": "Grade record only. It opens no extra remedy. R96-AC3 has no executed instance and receives no fabricated instance citation or PASS.",
    "dismissal_reason": "Grade record only. It opens no extra remedy. R96-AC3 has no executed instance and receives no fabricated instance citation or PASS.",
    "grades": [
      {
        "criterion": "R91-AC7",
        "instance": "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~9/IRPT_BCKEND.TO-IB-rti-1.the-capture-tool-repaired-command-readiness-origin.proof_of_spec.json@76dbec51e6",
        "verdict": "FAIL",
        "reason": "Issued bar (ii) requires EVERY navigation and EVERY redirect hop same-origin or refused. capture-session.cjs:182 discards the initial navigation response and checks only final page.url. The co-committed R9 diagnostic executes that actual source: portal -> example.invalid -> portal on the initial navigation, then an authenticated verification, writes once and prints success; initialChainReads=0. Positive same-origin case writes once; foreign-final and verification-foreign-return controls refuse. Bar (i)'s static source proof is sound at portal 8894e765ac; no real-browser test was required by this cell. A valid mechanical token and publish signature cannot override (ii)."
      },
      {
        "criterion": "R92-AC3",
        "instance": "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~10/IRPT_BCKEND.TO-IB-rti-2.the-ycharts-generate-source-members-resolved-or-named.proof_of_spec.json@76dbec51e6",
        "verdict": "PASS",
        "reason": "The issued judgment is source provenance: both paths tracked at HEAD; historical true sources data/firm_registry.json@1f54e16dfd and intake/settings.json@dc5d119b84 explicitly pinned in staged_from; no served-byte copy committed. Source-map diff changes exactly the two declarations. CRLF-normalized content identity is NOT byte identity; this PASS does not waive the cut's stricter stop clause or make R92-AC2 pass. The issuer/CTO's declare-only termination and parked redeploy are separate, explicitly recorded decisions."
      },
      {
        "criterion": "R93-AC3",
        "instance": "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~11/IRPT_BCKEND.TO-IB-rti-3.the-l4-negative-control-on-a-discriminating-instrument.proof_of_spec.json@76dbec51e6",
        "verdict": "NOT_EVALUATED",
        "reason": "The criterion explicitly says NOT_EVALUATED where the non-verdict branch was taken. Both buckets have no eligible principal in the recorded census; 0 positive/negative pairs and 0 attributable denials. principal.out records 258 roles + 7 users, 11 non-exempt trust-admitted candidates per bucket all implicitDeny, not 12 tested per bucket. No fence PASS or IAM-enforced false denial is manufactured. L4 stays OPEN."
      }
    ]
  },
  {
    "id": "IRPT_BCKEND-C-S146",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T00:01:05Z",
    "one_line": "W9-S1: absent renderer allowlist is an issuer premise error; typed value accepted, drift check still owed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "R91-AC3 demanded equality with a renderer origin allowlist.",
    "world_is": "The renderer has a four-entry vendor denylist, not a fixed origin allowlist. The helper types one origin equal to the configured portal_origin today; the equality battery compares vendor lists only.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/investor-reporting-export/render_export.cjs:48-50,141-146 @76dbec51e6",
        "infra/aws/ec2/investor-reporting-export/capture-session.cjs:44-54 @76dbec51e6",
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_SIGNOFF_CTO_HALF_IRPT_BCKEND_IB-rti-1_CAPTURE_TOOL_PUBLISH.md W9-S1 @93dda7a939"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Owner COO~B: derive the helper's list from the configured renderer origin or add a failing equality check. No DEV-origin expansion. CTO accepted typed-and-cited for this publish, not perpetual freedom from drift.",
    "adjudicates": [
      "IRPT_BCKEND-W9-S1"
    ]
  },
  {
    "id": "IRPT_BCKEND-C-S147",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T00:01:05Z",
    "one_line": "W9-S2: distinguish prerequisite refusal from the exercised readiness predicate.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "The unmodified R8 diagnostic alone should demonstrate repaired readiness.",
    "world_is": "Its password and HTTP500 cases lack an instance id and stop before readiness. The arbitrary-origin case refuses earlier in assertAllowedOrigin, not because of the missing id. The with-id copy and separately re-run readiness battery exercise the intended checks.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~9/battery_ib_rti_1.py arm_diagnostic and arm_readiness @76dbec51e6",
        "infra/aws/ec2/investor-reporting-export/capture-session.cjs:159-170 @76dbec51e6",
        "CVO re-ran command/readiness/origin arms locally: positive writes1; six readiness refusals write0."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "notes": "Evidence-interpretation record. The supplied-id and positive arms already resolve this diagnostic caveat. Corrects the packet's loose suggestion that the arbitrary-origin case is blocked by the id. No redundant repair; R91-AC7's uncovered initial-hop gap is separate.",
    "adjudicates": [
      "IRPT_BCKEND-W9-S2"
    ],
    "dismissal_reason": "Evidence-interpretation record. The supplied-id and positive arms already resolve this diagnostic caveat. Corrects the packet's loose suggestion that the arbitrary-origin case is blocked by the id. No redundant repair; R91-AC7's uncovered initial-hop gap is separate."
  },
  {
    "id": "IRPT_BCKEND-C-S148",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T00:01:05Z",
    "one_line": "W9-S3: Windows launch failure repaired before the published two-key act.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "The publish arm launches the AWS shim and compares published bytes.",
    "world_is": "The extensionless shim failed to launch on Windows; the battery now invokes .tools/aws.cmd. The later publish output and closed ledger record exactly the two intended keys.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~9/battery_ib_rti_1.py arm_publish @76dbec51e6",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~9/IB-rti-1_R91_arm_publish.txt blob caea76628e07373ae357754747ca074f67b3ccd7",
        "org/critical_paths/change_management/20260921T2322Z_irpt-rti-1-capture-tool-publish_deploy_completion.md @76dbec51e6"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "REMEDIATED within round. No publish replay by CVO; no claim of a fresh CVO S3 read.",
    "adjudicates": [
      "IRPT_BCKEND-W9-S3"
    ]
  },
  {
    "id": "IRPT_BCKEND-C-S149",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T00:01:05Z",
    "one_line": "W10-S1: historical source exists; line-ending normalization is not byte identity.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "The earlier note says no historical source blob exists for firm_registry.json.",
    "world_is": "The historical tracked registry blob 7c483504766345e4c73a7aad355ba9e5ca1e3edc exists at 1f54e16dfd; the intake settings source is pinned at dc5d119b84. Their LF blobs differ from recorded live CRLF bytes but preserve JSON content.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/ci/lambda-source-map.json irpt-ycharts-generate staged_from @76dbec51e6",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~10/ac1_output.txt @76dbec51e6",
        "git diff eecaad4985 76dbec51e6 -- infra/aws/lambda/ci/lambda-source-map.json: exactly two staged_from entries; both source paths git-ls-files tracked."
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Source declaration remedy REMEDIATED; no fresh live-package download this turn. W10-S3 separately carries the still-false note. The historical registry is not claimed equal to HEAD's generated registry.",
    "adjudicates": [
      "IRPT_BCKEND-W10-S1"
    ]
  },
  {
    "id": "IRPT_BCKEND-C-S150",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T00:01:05Z",
    "one_line": "W10-S2: declared rebuild differs in served behavior; redeploy remains parked.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "R92-AC2 requires member identity or differences that do not change served behavior.",
    "world_is": "The recorded 32-member rebuild versus 31 live members has 27 byte-identical, 3 CRLF-only, raw_keys.json rebuilt-only, and one substantive loaders.py difference. Rebuilding from the rth-1 pin is not evidence that the live function carries it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~10/ac2_output.txt @76dbec51e6",
        "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rti-2.the-ycharts-generate-source-members-resolved-or-named.md amended status/park @76dbec51e6"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Owner COO~B. Redeploy only on the recorded un-park condition: a served change ordered or frontend FWD-4 needs the loader fix. A new packet and both halves are required. R92-AC2 remains a recorded non-verdict, not a successful identity comparison.",
    "adjudicates": [
      "IRPT_BCKEND-W10-S2"
    ]
  },
  {
    "id": "IRPT_BCKEND-C-S151",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T00:01:05Z",
    "one_line": "W10-S3: stale source-map note contradicts the new declarations.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "A current source-map note describes buildability and declared sources accurately.",
    "world_is": "The note still says no source exists and the build fails on that member beside two pinned staged_from declarations that now resolve it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/ci/lambda-source-map.json irpt-ycharts-generate _staged_from_note and staged_from @76dbec51e6"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Owner COO~B via a lane with the source-map grant. Correct the note without widening deployment scope or copying served files.",
    "adjudicates": [
      "IRPT_BCKEND-W10-S3"
    ]
  },
  {
    "id": "IRPT_BCKEND-C-S152",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T00:01:05Z",
    "one_line": "W11-S1: the exercised instrument produced an honest non-verdict, not a fence test.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "L4 needs a non-exempt principal with an exact identity grant, successful control and attributable fenced denial.",
    "world_is": "The recorded census found no eligible candidate; 0 of 2 buckets discriminated, with no non-exempt call attempted. A simulator allowed-control is not a successful bucket positive arm.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~11/principal.out @76dbec51e6",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~11/exercise.out @76dbec51e6",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~11/battery_ib_rti_3.py principal_arm @76dbec51e6"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "L4 owner COO~B; CTO's bounded round-10 test-principal decision requires AE/CloudOps implementation and CTO+CRO halves, exact ListBucket grant to two targets and one control, then verified deletion. This adjudication grants no IAM authority. Non-verdict acceptance does not certify the census parser for every possible IAM trust policy.",
    "adjudicates": [
      "IRPT_BCKEND-W11-S1"
    ]
  },
  {
    "id": "IRPT_BCKEND-C-S153",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T00:01:05Z",
    "one_line": "Capture origin containment fails on an initial foreign redirect that returns to the portal.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "spec_asserts": "R91-AC7(ii) requires EVERY navigation and EVERY redirect hop same-origin or refused.",
    "world_is": "The initial page.goto response is discarded; only its final URL is checked. In a stubbed execution of the unchanged published-source logic, portal -> foreign -> portal then a valid check writes one session and prints success, with zero initial-chain reads. The analogous verification-chain hop is refused.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/investor-reporting-export/capture-session.cjs:182-189,203-222 @76dbec51e6, blob ea60b932bd4fd8af1f08548ce51022c2740af8b2",
        "Co-committed org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R9_CAPTURE_REDIRECT_DIAGNOSTIC.cjs: six arms; positive and initial-foreign-return write1, other four refuse/write0; no live network or credential."
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Owner COO~B. C-S127 remains OPEN/ARMED. Remedy the complete navigation lifecycle, including initial response and interactive interval, with a single-difference initial-foreign-return regression plus positive control. Do not widen the allowlist or automate MFA. This is a code-path counterexample, not an observed credential leak.",
    "disarm_owner": "2.0.0_SA_COO~B"
  },
  {
    "id": "IRPT_BCKEND-C-S154",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T00:01:05Z",
    "one_line": "Final rti-1 proof mixes first-pass pins with second-pass publication evidence.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "A final proof's artifact bindings and exclusions describe the act being graded.",
    "world_is": "All 14 artifact hashes resolve as blobs, but two still name the first-pass battery/publish output rather than their current second-pass blobs. The declared exclusion says neither half exists while R91-AC6 says both exist and publication passed.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~9/IRPT_BCKEND.TO-IB-rti-1.the-capture-tool-repaired-command-readiness-origin.proof_of_spec.json @76dbec51e6",
        "CVO blob-to-HEAD comparison: battery a8499e56 -> 941b85db5b8a0048c1c8d2649df4c3d345f5ca6d; publish output 8941862d -> caea76628e07373ae357754747ca074f67b3ccd7; 12/14 match, 2/14 differ."
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Owner COO~B through the artifact owner: reconcile final proof pins, result/exclusions and compiler summary without replaying publication. The checker reports ACCEPT with 14 UNRESOLVED-HERE because bare blob hashes are not commit refs; CVO resolved them manually. No generic checker change is requested inside IRPT. Actual publication output and signed source bytes remain separately citable."
  },
  {
    "id": "IRPT_BCKEND-C-S155",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T00:01:05Z",
    "one_line": "Round-8 remedy clocks: source repair is not host disarm; three issuer corrections close.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Existing remediation clocks advance only on evidence; a publish is not an on-host readback.",
    "world_is": "C-S125 and C-S126 have repaired published source, but no proof of fixed bytes on the capture host; their remediation state advances while disarm remains ARMED. W3-S51 and W1-S46 have authoritative errata; C-S144 has the substantive R96-AC3 successor bar. C-S127 remains OPEN/ARMED.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ca91fbc11b: errata on rth-1/rth-3 faces and decomposition R8.10 preserve original text and correct the two premises.",
        "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rti-6.the-rth-2-latency-measurement-under-a-verified-session.md R96-AC3 @76dbec51e6",
        "CVO fresh command/readiness stub runs at 76dbec51e6; signed packet 56ad32833417a7a70c1d3933927385f9d66accfb and S3 publish ledger; no on-host verification."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "notes": "Closure/clock-evidence record, not a dismissal of the historic findings. In REMEDIATION_v2 only the allowed clocks advance. C-S144 closes the missing-bar defect, not the unexecuted measurement; R77-AC2 remains NOT_EVALUATED.",
    "adjudicates": [
      "IRPT_BCKEND-W3-S51",
      "IRPT_BCKEND-W1-S46"
    ],
    "dismissal_reason": "Closure/clock-evidence record, not a dismissal of the historic findings. In REMEDIATION_v2 only the allowed clocks advance. C-S144 closes the missing-bar defect, not the unexecuted measurement; R77-AC2 remains NOT_EVALUATED."
  },
  {
    "id": "IRPT_BCKEND-C-S156",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T00:01:05Z",
    "one_line": "Capture runbook omits delivery and hash verification of the repaired tool before execution.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "spec_asserts": "The human is to run the FIXED capture tool; publishing its S3 objects is said to unblock that step.",
    "world_is": "The README starts the host, opens an interactive shell and directly runs the local wrapper, with no sync or hash check first. The source's S3 sync lives inside the render Command document, not the capture wrapper or the checked-in host bootstrap. Starting a host does not establish which capture bytes it runs.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/investor-reporting-export/README.md session-capture steps1-5 @76dbec51e6",
        "infra/aws/ec2/investor-reporting-export/capture-session.sh @76dbec51e6: local cd/module discovery/IMDS/node only; no artifact sync.",
        "infra/aws/terraform/investor-reporting/export/ssm.tf:16-17,43-51 @76dbec51e6: unscheduled Command document owns sync; infra/aws/terraform/investor-reporting/ycharts/instance.tf:80-111 bootstrap has no capture sync.",
        "org/tier1_exec/2.0.0_SA_COO~B/deliverables/NEVER_WIDEN_SIGNOFF_COO_HALF_IRPT_BCKEND_IB-rti-1_CAPTURE_TOOL_PUBLISH.md @b15fa5081c says next human-started render sync delivers the files; no host readback claimed."
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Owner COO~B: make the authorized human runbook establish and verify both fixed host hashes BEFORE invoking capture or entering credentials. Do not ask for a credential on assumed bytes; do not run a render merely to side-load tools. CVO did not start a host, transfer files or inspect a real session. This proves a runbook dependency gap, not that current host bytes are definitely old.",
    "disarm_owner": "2.0.0_SA_COO~B"
  }
]
```

