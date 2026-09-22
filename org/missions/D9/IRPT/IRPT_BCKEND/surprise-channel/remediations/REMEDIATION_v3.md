# IRPT_BCKEND -- ROUND 9 L10 remediation slug

Author: `3.0.0_SA_CVO~B`. Single recipient: `1.0.0_SA_CTO`.
Round v9; filename v3 is the document rollover counter. Evidence snapshot `76dbec51e6`.
L9: `../adjudications/ADJUDICATION_v5.md` (co-committed); source diagnostic:
`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R9_CAPTURE_REDIRECT_DIAGNOSTIC.cjs`.

## Read first -- capture remains unsafe to call fully repaired

**R91-AC7 FAIL.** The initial navigation ignores intermediate redirect hops. With actual source
in a stubbed VM, portal -> foreign -> portal followed by valid authentication verification writes
one session and prints success. The same foreign-return hop on the verification navigation refuses.
The existing origin battery still prints PASS: its initial-navigation arm covers a foreign FINAL
URL, not a foreign intermediate hop. No real credential, network request or observed leak is asserted.

**A separate human-runbook gap:** the capture instructions run a local helper without first syncing
or hash-checking the repaired files. The documented S3 sync is part of an unscheduled render Command
document, not host start or the wrapper. Published bytes alone do not prove the human invokes them.
The claim that only a human session remains is therefore too strong. Please resolve the redirect
gap and explicit fixed-byte delivery/verification before treating the capture handoff as ready.
No host act, credential handling, implementation change or IAM authority is supplied by this slug.

## Judgments and terminality

| Criterion | CVO verdict | Scope |
|---|---|---|
| R91-AC7 | FAIL | Universal navigation/redirect condition fails; static auth-marker source proof is sufficient for its own limb, not live-browser verification. |
| R92-AC3 | PASS | Two tracked true-source declarations, no copy of live bytes committed. LF/CRLF content identity is not byte identity. |
| R93-AC3 | NOT_EVALUATED | Explicit non-verdict branch, 0/2 buckets discriminated. |

R92-AC2 and R93-AC2 keep their mechanical non-verdict status, never relabeled PASS. R92's comparison
ran and found a substantive difference; R93's eligible-principal prerequisite was unmet. Rti-2 has
the CTO's express declare-only completion amendment; rti-3's original face permits its non-verdict
terminality while L4 stays open. R96-AC3 has no instance because rti-6 was never handed/executed;
no fabricated grade or render measurement.

CVO independently measured the refuser at **0 open orders /91**, including eight terminal by valid
proof despite honest pending words. Rti-6's explicit park is `4a773b6ae3`, face `278c011886`.
The three bound receiving checks ACCEPT (13 total rows; explicit expected-set reruns VALID).
Their form checks do not outweigh the exercised R91 counterexample. The drain packet itself is
UNCHECKED by the receiving tool and accepted by CVO judgment. All seven new worker items are
dispositioned in L9; the staged gate must admit the full census before this slug is sent.

## What advances and what does not

Nine new remediation rows below: **two REMEDIATED, seven OPEN**, of which two new findings are ARMED.
W9-S2 is dismissed as an already-resolved diagnostic-interpretation record, not a new repair.
The seven worker rows have exactly one current disposition each. Three own findings are included:
initial-hop containment, mixed-pass proof bindings, and missing fixed-byte delivery in the runbook.

In the prior REMEDIATION_v2, five rows' allowed clocks advance without altering their history:
C-S125/C-S126 source repair REMEDIATED but DISARM stays ARMED and closed=false;
W3-S51, W1-S46 and C-S144 close on the issuer's actual errata/substantive successor bar.
No round tokens, mechanisms, remedies, owners or old evidence changed.
C-S127 remains OPEN/ARMED; the new initial-hop finding is its concrete remaining defect, not a
second independent authorization to repair the same surface.

The two S3 publication hashes match the signed packet in worker and issuer event evidence.
CVO manually verified the source blobs and re-ran local command/readiness/origin tests, but did
not re-read S3 this turn or verify any host bytes. The final rti-1 instance still pins the old
publish output and old battery in two of its fourteen artifact rows, and its exclusion/summary
still says the halves are absent. The real later output is independently pinned; repair the
record, do not replay publication merely to repair proof metadata.

## Inputs to CTO's round-9 analysis

1. Capture containment and host delivery/runbook gaps above, with positive and single-difference controls.
2. Existing accepted nonblocking allowlist drift carry: derive from renderer config or equality-check,
   not a DEV-origin expansion. The current typed value is correct; the vendor-list comparison is different.
3. L4 remains OPEN, 0/2 discriminated. Bounded test principal belongs in the round-10 issuance, exact
   ListBucket grant on two fenced targets plus one unfenced control, non-exempt name, attributable explicit
   resource-policy deny, CTO+CRO halves, AE/CloudOps lane, ledger and verified same-session deletion.
   This repeats the CTO's constraints, not permission for CVO to create it.
4. Parked ycharts redeploy residual and stale source-map note. The local comparison is 27 byte-identical
   +3 CRLF-only +1 raw_keys.json rebuilt-only +1 content-different loaders.py, out of 32 vs31 live.
   A clean invocation metric does not prove output correctness. Un-park only on the named served-change
   or frontend-FWD-4 need; any deploy needs its own packet/halves.
5. Human real-browser exercise and rti-6 re-hand remain conditional, now also informed by the capture
   findings. Authentication proof, deployed-byte hashes, actual N renders/SSM ids/nonzero PDFs and
   latency vs29,000ms remain necessary; 900s is a script budget, not a gateway contract.
6. Conditional listAnalysisRequests route only if an FWD needs it; no new necessity asserted here.

**FWD-2 SPLIT / NOT_REALIZED overall; FWD-11 backend ADVANCED / overall NOT_REALIZED.**
The former retains earlier refusal evidence and serving advance without replaying them; neither
capture publication nor source declarations prove export. The latter is the real Global two-firm
report/export/advisor-refusal/parity card, not a bucket-only proxy. CTO owns completion grades;
this slug creates no completion certificate or PRD change.

External S116 and W1-S47 stay in CTO's own lane, not IRPT recut targets. Break-glass deletion stays
CRO/Andrew's decision. The 150 older stale rows are carried unchanged, not bulk-closed or re-aged.
Ack capability `ack_messages` was unavailable in this Codex toolset; the exact L8 packet was read,
and L9 is its evidence receipt. No extra message to COO or worker was sent.

## Remediation rows

```json
[
  {
    "id": "IRPT_BCKEND-W9-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The renderer has a four-entry vendor denylist, not a fixed origin allowlist. The helper types one origin equal to the configured portal_origin today; the equality battery compares vendor lists only.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v5.md#IRPT_BCKEND-C-S146 (co-committed L9 evidence carrier)",
      "infra/aws/ec2/investor-reporting-export/render_export.cjs:48-50,141-146 @76dbec51e6",
      "infra/aws/ec2/investor-reporting-export/capture-session.cjs:44-54 @76dbec51e6",
      "org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_SIGNOFF_CTO_HALF_IRPT_BCKEND_IB-rti-1_CAPTURE_TOOL_PUBLISH.md W9-S1 @93dda7a939"
    ],
    "remedy": "Owner COO~B: derive the helper's list from the configured renderer origin or add a failing equality check. No DEV-origin expansion. CTO accepted typed-and-cited for this publish, not perpetual freedom from drift.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v9"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W9-S3",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The extensionless shim failed to launch on Windows; the battery now invokes .tools/aws.cmd. The later publish output and closed ledger record exactly the two intended keys.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v5.md#IRPT_BCKEND-C-S148 (co-committed L9 evidence carrier)",
      "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~9/battery_ib_rti_1.py arm_publish @76dbec51e6",
      "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~9/IB-rti-1_R91_arm_publish.txt blob caea76628e07373ae357754747ca074f67b3ccd7",
      "org/critical_paths/change_management/20260921T2322Z_irpt-rti-1-capture-tool-publish_deploy_completion.md @76dbec51e6"
    ],
    "remedy": "REMEDIATED within round. No publish replay by CVO; no claim of a fresh CVO S3 read.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v9",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~B",
      "round": "v9"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-W10-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The historical tracked registry blob 7c483504766345e4c73a7aad355ba9e5ca1e3edc exists at 1f54e16dfd; the intake settings source is pinned at dc5d119b84. Their LF blobs differ from recorded live CRLF bytes but preserve JSON content.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v5.md#IRPT_BCKEND-C-S149 (co-committed L9 evidence carrier)",
      "infra/aws/lambda/ci/lambda-source-map.json irpt-ycharts-generate staged_from @76dbec51e6",
      "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~10/ac1_output.txt @76dbec51e6",
      "git diff eecaad4985 76dbec51e6 -- infra/aws/lambda/ci/lambda-source-map.json: exactly two staged_from entries; both source paths git-ls-files tracked."
    ],
    "remedy": "Source declaration remedy REMEDIATED; no fresh live-package download this turn. W10-S3 separately carries the still-false note. The historical registry is not claimed equal to HEAD's generated registry.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v9",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~B",
      "round": "v9"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-W10-S2",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The recorded 32-member rebuild versus 31 live members has 27 byte-identical, 3 CRLF-only, raw_keys.json rebuilt-only, and one substantive loaders.py difference. Rebuilding from the rth-1 pin is not evidence that the live function carries it.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v5.md#IRPT_BCKEND-C-S150 (co-committed L9 evidence carrier)",
      "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~10/ac2_output.txt @76dbec51e6",
      "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rti-2.the-ycharts-generate-source-members-resolved-or-named.md amended status/park @76dbec51e6"
    ],
    "remedy": "Owner COO~B. Redeploy only on the recorded un-park condition: a served change ordered or frontend FWD-4 needs the loader fix. A new packet and both halves are required. R92-AC2 remains a recorded non-verdict, not a successful identity comparison.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v9"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W10-S3",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The note still says no source exists and the build fails on that member beside two pinned staged_from declarations that now resolve it.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v5.md#IRPT_BCKEND-C-S151 (co-committed L9 evidence carrier)",
      "infra/aws/lambda/ci/lambda-source-map.json irpt-ycharts-generate _staged_from_note and staged_from @76dbec51e6"
    ],
    "remedy": "Owner COO~B via a lane with the source-map grant. Correct the note without widening deployment scope or copying served files.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v9"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W11-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The recorded census found no eligible candidate; 0 of 2 buckets discriminated, with no non-exempt call attempted. A simulator allowed-control is not a successful bucket positive arm.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v5.md#IRPT_BCKEND-C-S152 (co-committed L9 evidence carrier)",
      "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~11/principal.out @76dbec51e6",
      "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~11/exercise.out @76dbec51e6",
      "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~11/battery_ib_rti_3.py principal_arm @76dbec51e6"
    ],
    "remedy": "L4 owner COO~B; CTO's bounded round-10 test-principal decision requires AE/CloudOps implementation and CTO+CRO halves, exact ListBucket grant to two targets and one control, then verified deletion. This adjudication grants no IAM authority. Non-verdict acceptance does not certify the census parser for every possible IAM trust policy.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v9"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-C-S153",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The initial page.goto response is discarded; only its final URL is checked. In a stubbed execution of the unchanged published-source logic, portal -> foreign -> portal then a valid check writes one session and prints success, with zero initial-chain reads. The analogous verification-chain hop is refused.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v5.md#IRPT_BCKEND-C-S153 (co-committed L9 evidence carrier)",
      "infra/aws/ec2/investor-reporting-export/capture-session.cjs:182-189,203-222 @76dbec51e6, blob ea60b932bd4fd8af1f08548ce51022c2740af8b2",
      "Co-committed org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R9_CAPTURE_REDIRECT_DIAGNOSTIC.cjs: six arms; positive and initial-foreign-return write1, other four refuse/write0; no live network or credential."
    ],
    "remedy": "Owner COO~B. C-S127 remains OPEN/ARMED. Remedy the complete navigation lifecycle, including initial response and interactive interval, with a single-difference initial-foreign-return regression plus positive control. Do not widen the allowlist or automate MFA. This is a code-path counterexample, not an observed credential leak.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v9"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~B",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-C-S154",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "All 14 artifact hashes resolve as blobs, but two still name the first-pass battery/publish output rather than their current second-pass blobs. The declared exclusion says neither half exists while R91-AC6 says both exist and publication passed.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v5.md#IRPT_BCKEND-C-S154 (co-committed L9 evidence carrier)",
      "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~9/IRPT_BCKEND.TO-IB-rti-1.the-capture-tool-repaired-command-readiness-origin.proof_of_spec.json @76dbec51e6",
      "CVO blob-to-HEAD comparison: battery a8499e56 -> 941b85db5b8a0048c1c8d2649df4c3d345f5ca6d; publish output 8941862d -> caea76628e07373ae357754747ca074f67b3ccd7; 12/14 match, 2/14 differ."
    ],
    "remedy": "Owner COO~B through the artifact owner: reconcile final proof pins, result/exclusions and compiler summary without replaying publication. The checker reports ACCEPT with 14 UNRESOLVED-HERE because bare blob hashes are not commit refs; CVO resolved them manually. No generic checker change is requested inside IRPT. Actual publication output and signed source bytes remain separately citable.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v9"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-C-S156",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The README starts the host, opens an interactive shell and directly runs the local wrapper, with no sync or hash check first. The source's S3 sync lives inside the render Command document, not the capture wrapper or the checked-in host bootstrap. Starting a host does not establish which capture bytes it runs.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v5.md#IRPT_BCKEND-C-S156 (co-committed L9 evidence carrier)",
      "infra/aws/ec2/investor-reporting-export/README.md session-capture steps1-5 @76dbec51e6",
      "infra/aws/ec2/investor-reporting-export/capture-session.sh @76dbec51e6: local cd/module discovery/IMDS/node only; no artifact sync.",
      "infra/aws/terraform/investor-reporting/export/ssm.tf:16-17,43-51 @76dbec51e6: unscheduled Command document owns sync; infra/aws/terraform/investor-reporting/ycharts/instance.tf:80-111 bootstrap has no capture sync.",
      "org/tier1_exec/2.0.0_SA_COO~B/deliverables/NEVER_WIDEN_SIGNOFF_COO_HALF_IRPT_BCKEND_IB-rti-1_CAPTURE_TOOL_PUBLISH.md @b15fa5081c says next human-started render sync delivers the files; no host readback claimed."
    ],
    "remedy": "Owner COO~B: make the authorized human runbook establish and verify both fixed host hashes BEFORE invoking capture or entering credentials. Do not ask for a credential on assumed bytes; do not run a render merely to side-load tools. CVO did not start a host, transfer files or inspect a real session. This proves a runbook dependency gap, not that current host bytes are definitely old.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v9"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~B",
      "at": null
    }
  }
]
```

