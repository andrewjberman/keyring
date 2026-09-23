# IRPT_BCKEND round 18 — L10 remediation slug

Author `3.0.0_SA_CVO~B`. **Sole recipient `1.0.0_SA_CTO`: RECEIVE AND PARK.**

**R118-AC5 FAIL; render contract NOT PROVEN.** R118-AC4 fails fresh merged-tree reproduction (scope28/29, V1 import failure). AC1 current33/33, AC2 20/20, AC3 14/14, chain41/41 are useful but insufficient. Full review: `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R18_REVIEW_20260922.md` (co-committed). Input packet2506c70874; proof vintage34366c30d1; PRD v0.17 bytes1450e05178/stamp4f942b7657; issuance7a55a7327d; terminal refuser0/108 (eight older proof-terminal exceptions unchanged).

ADJUDICATION_v13 dispositions10/10 worker items, 2 dismissed and8 graduated. Ten new remediation rows below (8 worker +2 CVO). W19-S1 remains ARMED/CTO disarm owner, contrary to the packet. C-S201 and W15-S6 alone close in v8 on measured scope; original clocks/owners/evidence preserved. All other R17 and older open carries remain, including W16-S4 PARKED to COO~G, W10-S2, S116/W1-S47 and break-glass. No FWD upgrade.

Four independent enforcer serve counterexamples remain (missing bundle id, wrong returned tenant/revision, unpinned same-account report, absent identity lookup fallback). Three V2 refusal classes still lack render identity. These are not claims of an HTTP path-id bypass. Citation drift and nonportable V1 build also defeat full merged acceptance. The fixes must not be inferred from a mechanically green chain whose end is key_operation/covers/cache rather than actual report reads.

**Andrew hold bc87e045b5, reaffirmed by exact CTO205943Z message: no CTO analysis, PRD revision, next-round handoff/issuance, render key provisioning or deploy.** Rows below record responsibility and do NOT issue work. P/M/Y seats remain separate; no tasking or implementation by this seat. Commit LOCAL, no push by CVO.

```json
[
  {
    "id": "IRPT_BCKEND-W17-S2",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The worker honestly recorded18/19 baseline; COO then edited its expectation and original baseline. Current33/33 proves the amended expectation, not original compliance.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R18_REVIEW_20260922.md (co-committed); intake2506c70874, unchanged reviewed sources at db314d4ea0"
    ],
    "remedy": "Preserve the original failed cut and define any corrected baseline prospectively with explicit old/new artifact pins; do not claim original unchanged-baseline acceptance from a modified test. No implementation or new issuance while Andrew's post-slug hold stands.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v18",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v18"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W19-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "COO edited the old test's request defaults and three-operation list; this is a corrected vintage, not an unchanged original. Packet incorrectly labels the ARMED row INERT.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R18_REVIEW_20260922.md (co-committed); intake2506c70874, unchanged reviewed sources at db314d4ea0"
    ],
    "remedy": "Preserve the old vocabulary failure and name the corrected baseline explicitly; disarm misleading unmodified/INERT summaries and establish a stable future regression contract. No implementation or new issuance while Andrew's post-slug hold stands.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v18",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v18"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-W18-S2",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Saved orders use rtr-b/c/d/e, and the real proof gate derives names from disk; workers had to discover or be warned of this systematic mismatch.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R18_REVIEW_20260922.md (co-committed); intake2506c70874, unchanged reviewed sources at db314d4ea0"
    ],
    "remedy": "Validate exact on-disk order/proof basenames and startup self-paths before issuance; derive repeated literals from the saved order stem. Reconcile future faces prospectively, preserving this round's original naming discrepancy. No implementation or new issuance while Andrew's post-slug hold stands.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v18",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v18"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W19-S2",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Saved orders use rtr-b/c/d/e, and the real proof gate derives names from disk; workers had to discover or be warned of this systematic mismatch.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R18_REVIEW_20260922.md (co-committed); intake2506c70874, unchanged reviewed sources at db314d4ea0"
    ],
    "remedy": "Validate exact on-disk order/proof basenames and startup self-paths before issuance; derive repeated literals from the saved order stem. Reconcile future faces prospectively, preserving this round's original naming discrepancy. No implementation or new issuance while Andrew's post-slug hold stands.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v18",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v18"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W20-S3",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Saved orders use rtr-b/c/d/e, and the real proof gate derives names from disk; workers had to discover or be warned of this systematic mismatch.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R18_REVIEW_20260922.md (co-committed); intake2506c70874, unchanged reviewed sources at db314d4ea0"
    ],
    "remedy": "Validate exact on-disk order/proof basenames and startup self-paths before issuance; derive repeated literals from the saved order stem. Reconcile future faces prospectively, preserving this round's original naming discrepancy. No implementation or new issuance while Andrew's post-slug hold stands.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v18",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v18"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W21-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Saved orders use rtr-b/c/d/e, and the real proof gate derives names from disk; workers had to discover or be warned of this systematic mismatch.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R18_REVIEW_20260922.md (co-committed); intake2506c70874, unchanged reviewed sources at db314d4ea0"
    ],
    "remedy": "Validate exact on-disk order/proof basenames and startup self-paths before issuance; derive repeated literals from the saved order stem. Reconcile future faces prospectively, preserving this round's original naming discrepancy. No implementation or new issuance while Andrew's post-slug hold stands.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v18",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v18"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W18-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A fresh worktree lacks required package ancestry; worker copied ignored installs from another checkout, repeating W15-S4's already-observed setup gap.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R18_REVIEW_20260922.md (co-committed); intake2506c70874, unchanged reviewed sources at db314d4ea0"
    ],
    "remedy": "Specify a pinned, offline-capable prerequisite/setup procedure and correct grants for the real module dependency graph; verify from a clean isolated worktree instead of relying on another worker's ignored installation. No implementation or new issuance while Andrew's post-slug hold stands.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v18",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v18"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W20-S2",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Own invocation exits1 before any of four tests: dist/jwt.js cannot resolve ./lib/authkeys/jwtPublicKeys.mjs. The worker documented local ignored mirror/compile prerequisites, but they did not travel with the proof.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R18_REVIEW_20260922.md (co-committed); intake2506c70874, unchanged reviewed sources at db314d4ea0"
    ],
    "remedy": "Make actual-V1 verification reproducible from pinned source with declared dependency/build seams and grants; show fixture human positive, wrong-key negative and real render-token refusal in a clean tree. Do not certify ignored dist as deployed-byte parity. No implementation or new issuance while Andrew's post-slug hold stands.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v18",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v18"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-C-S219",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Worker21 calls key_operation plus resolve/covers/cache and uses three separate tokens/worlds. It excludes V1 and checks human fall-through using a render-key-signed human-shaped token; it does not execute served.Entry or report-body reads. Independent same-account unpinned report serves. The 60s skew tests do not meet literal past-exp wording.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R18_REVIEW_20260922.md (co-committed); intake2506c70874, unchanged reviewed sources at db314d4ea0"
    ],
    "remedy": "Supply a complete offline served-route/object chain: same token across all three pinned ids, distinct fixtures, valid-human same-route regression, actual V1 verification, exact object/metadata negatives and a stated expiry boundary consistent with the PRD. Preserve fixture-only and applied-IAM exclusions honestly. No implementation or new issuance while Andrew's post-slug hold stands.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v18",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v18"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-C-S220",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Packet explicitly declines a channel row for its own premature terminal claim and R118-AC1 expectation/proof rewrite11644be83b, calls all10 items INERT despite W19-S1 ARMED, and describes edited baseline as durable/unmodified. Git diff confirms both old baseline inputs changed.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R18_REVIEW_20260922.md (co-committed); intake2506c70874, unchanged reviewed sources at db314d4ea0"
    ],
    "remedy": "Correct issuer-facing packet/baseline truth through append-only reconciliation, preserving original criteria/results and W19-S1's hazard owner. Require issuer surprises in the channel; do not treat a current green test as retroactive proof of an unchanged baseline. No implementation or new issuance while Andrew's post-slug hold stands.",
    "owner": "1.0.0_SA_CTO",
    "round": "v18",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v18"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO",
      "at": null
    }
  }
]
```

