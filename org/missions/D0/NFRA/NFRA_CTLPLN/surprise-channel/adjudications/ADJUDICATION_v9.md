# NFRA_CTLPLN: CVO L9 grade and L8 dispositions at the round-7 close (2026-10-12)

L9/L8 by `3.0.0_SA_CVO~L` (laptop), on 2.0.0_SA_COO~C msg 108492. HEAD e0c0cc38f2.

**L9.** TO-CT-v-2 CTv2-AC2 MET (C-S23).

**L8.** Seven of the eight new rows are DISMISSED: W63-S1 to W63-S6 and W64-S1 (C-S24 to C-S30).
**D1-S10 is HELD to GRADUATE**, like D1-S8: TO-CT-u-3, u-4 and u-5 still read `staged`, so the row gate refuses a new
remediation row. Both graduations land together when those three orders are terminal.

Still ARMED and Andrew's: W61-S1. The laptop's sshd stays open to the Public Wi-Fi with password login on (ADJUDICATION_v8).

The PRD v0.25 ratified half is already SIGNED and current (@4af2d1a4f1; `prd-signoff.py status` reads ADMITTED).

<sweep_watermark>2026-10-12T08:10Z</sweep_watermark>

```json
[
  {
    "id": "NFRA_CTLPLN-C-S23",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~L",
    "surfaced_at": "2026-10-12T08:10Z",
    "one_line": "L9: NFRA_CTLPLN.TO-CT-v-2 CTv2-AC2 MET -- a new registry file read by the generator is the right single source, and the section-4 handler patch carries no firm token, so the naming gate would pass it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "CTv2-AC2: the recommendation in section 1 of PROPOSAL_FIRM_ACCESS_REGISTRY_ROW.md is the right single source, and the handler patch in section 4 would pass the naming gate.",
    "world_is": "Section 1 recommends (a), infra/logic/registry/firm_pages.json generated into the Lambda module and later the portal carrier. It rejects (b), parsing TypeScript off a checkout that is ahead of its gitlink pin, and (c), a scopes.json column that would re-stamp the deployed edge firm-config. The basis holds at HEAD: lib/opal_naming.py _tenants() returns 5 tenants against the portal's 4 firm keys, so a derived set would admit the test tenant. The CTO approved points 1, 2, 4 and 5 and amended point 3 (no ALL token) in msg 108481. Point 3 changes a row value, not the source. Section 4: .tools/naming-gate.py:748 builds its target list from mod.VIEWS, so the generated module is governed by the generated-mark check. A scan of the patch's added lines against the 16 FIRM-class spellings in infra/logic/registry/scopes.json finds 0 hits. The route key f'{http_method} {path}' is the form the live handler already matches (lambda_function.py:2108).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~64/PROPOSAL_FIRM_ACCESS_REGISTRY_ROW.md sections 0, 1 and 4",
        ".tools/naming-gate.py:745-760 read at HEAD e0c0cc38f2",
        "python -I: opal_naming._tenants(load_registry()) -> 5",
        "infra/aws/lambda/portal_data_proxy/lambda_function.py:2088-2116",
        "1.0.0_SA_CTO msg 108481"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade, not a hazard: the judgment criterion is MET."
  },
  {
    "id": "NFRA_CTLPLN-C-S24",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~L",
    "surfaced_at": "2026-10-12T08:10Z",
    "one_line": "W63-S1 is a method record: candidate (b) was measured through PIP_CONFIG_FILE, and the per-user file is inferred to behave the same.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "CT-v-1: measure candidate (b), the pip per-user config.",
    "world_is": "The row states the limit itself: same option parser, different file location, and the real per-user file neither read nor changed. The CTO ruled PIP_NO_INDEX=1 as dell1's stop (msg 108481), so candidate (b) is not the chosen mechanism.",
    "grounding": {"status": "GROUNDED", "evidence": ["INVESTIGATION_v1.md NFRA_CTLPLN-W63-S1", "1.0.0_SA_CTO msg 108481 (last line)"]},
    "adjudicates": ["NFRA_CTLPLN-W63-S1"],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The row records its limit, and the chosen stop is a different candidate."
  },
  {
    "id": "NFRA_CTLPLN-C-S25",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~L",
    "surfaced_at": "2026-10-12T08:10Z",
    "one_line": "W63-S2 overtaken: the dead-loopback candidate (c) fails the zero-request rule by construction under the proxy redirect, and the CTO chose PIP_NO_INDEX=1.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "CT-v-1 zero-request rule over the candidates.",
    "world_is": "The tool records (c) as FAIL and does not reclassify it, and no public host was contacted. Whether proxy lines to loopback should count is moot, because (c) was not chosen.",
    "grounding": {"status": "GROUNDED", "evidence": ["INVESTIGATION_v1.md NFRA_CTLPLN-W63-S2", "1.0.0_SA_CTO msg 108481"]},
    "adjudicates": ["NFRA_CTLPLN-W63-S2"],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The candidate was not chosen; there is no exposure."
  },
  {
    "id": "NFRA_CTLPLN-C-S26",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~L",
    "surfaced_at": "2026-10-12T08:10Z",
    "one_line": "W63-S3 is a measurement note: pip routes the loopback index through HTTP_PROXY, so redirect A's own count is proven only by the selfcheck. The bound holds.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "CT-v-1: two independent redirects, each counting requests.",
    "world_is": "The positive arm met the bound through the proxy listener. Only the independence of the two redirects is weaker than described, and the row says so.",
    "grounding": {"status": "GROUNDED", "evidence": ["INVESTIGATION_v1.md NFRA_CTLPLN-W63-S3"]},
    "adjudicates": ["NFRA_CTLPLN-W63-S3"],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The bound holds; the weaker independence is recorded, not a defect."
  },
  {
    "id": "NFRA_CTLPLN-C-S27",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~L",
    "surfaced_at": "2026-10-12T08:10Z",
    "one_line": "W63-S4 accepted: the kit refuses more than the order's allowed list (list --outdated, direct URLs, VCS sources, requirement files, --proxy, non-file schemes, unlisted verbs). Each would egress.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "CT-v-1: the wrapper's allowed list.",
    "world_is": "Each of the four named shapes makes a request under pip's own semantics, so refusing them is stricter than the literal list and serves the order's purpose (no egress). Default-deny of unlisted verbs is the safe reading.",
    "grounding": {"status": "GROUNDED", "evidence": ["INVESTIGATION_v1.md NFRA_CTLPLN-W63-S4"]},
    "adjudicates": ["NFRA_CTLPLN-W63-S4"],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Stricter than ordered and aligned with the order's intent. Accepted."
  },
  {
    "id": "NFRA_CTLPLN-C-S28",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~L",
    "surfaced_at": "2026-10-12T08:10Z",
    "one_line": "W63-S5 accepted as written: the wrapper's refusal text names the laptop because C-INTAKE makes the laptop the approving box. A message string is not device logic.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "CT-v-1 fixes the refusal text verbatim; the workspace rule bars device-specific logic.",
    "world_is": "The word sits in operator-facing text naming where a package is approved (PRD C-INTAKE, the laptop admins packages). It selects no behavior by device, and the order fixes the product string.",
    "grounding": {"status": "GROUNDED", "evidence": ["INVESTIGATION_v1.md NFRA_CTLPLN-W63-S5", "NFRA_CTLPLN_PRD.md ADDENDUM v0.15 (C-INTAKE)"]},
    "adjudicates": ["NFRA_CTLPLN-W63-S5"],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "No device-specific logic, and the order fixes the text."
  },
  {
    "id": "NFRA_CTLPLN-C-S29",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~L",
    "surfaced_at": "2026-10-12T08:10Z",
    "one_line": "W63-S6 accepted: --retries 0 --timeout 5 on every pip arm keeps the bound measurable, and the arms stay comparable.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "CT-v-1: the order's pip command text.",
    "world_is": "pip's default retries on a 502 would exceed the time bound over about 14 arms. Every arm carries the same two options, so the comparison holds. The options reduce requests and do not add any.",
    "grounding": {"status": "GROUNDED", "evidence": ["INVESTIGATION_v1.md NFRA_CTLPLN-W63-S6"]},
    "adjudicates": ["NFRA_CTLPLN-W63-S6"],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Uniform across arms and request-reducing. Accepted."
  },
  {
    "id": "NFRA_CTLPLN-C-S30",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~L",
    "surfaced_at": "2026-10-12T08:10Z",
    "one_line": "W64-S1 ruled: the test tenant is admitted to no page (CTO msg 108481 point 2), so explicit firm rows, not a set derived from _tenants(), are correct.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "W64-S1 asks the CTO whether the test-kind tenant ever reaches a partner page.",
    "world_is": "CTO msg 108481 point 2: 'test tenant admitted to no page CONFIRMED'. This seat measured _tenants() at 5 against 4 portal firm keys.",
    "grounding": {"status": "GROUNDED", "evidence": ["1.0.0_SA_CTO msg 108481", "python -I opal_naming._tenants -> 5"]},
    "adjudicates": ["NFRA_CTLPLN-W64-S1"],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The question the row asked has been answered."
  }
]
```
