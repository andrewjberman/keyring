# AMGT_RESAPP -- round 81 remediations (dell1)

<sweep_watermark>2026-10-09T06:39Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T06:39:00Z. Graduated at ADJUDICATION_v99: 4 rows, all INERT.

```json
[
  {
    "id": "AMGT_RESAPP-D1-W321-S1",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The merged 20-F cutter (opal-filings-fetch/2.0.0) cuts no item from ASML NA's real 2025 20-F: every pattern matches only a contents line, so the fetch returns UNRESOLVED-SOURCE and writes a state marker (amgt/harvest/state/filing_attempt/security_key=ASML_NA_Equity/UNRESOLVED-SOURCE.json, a key outside the pair's three, not served while ASML's drafting reads SERVED).",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W321-S1 (BLOCKING, INERT); ee-4 CANCELLED @9c85a18c4c, ledger CLOSED @24435e4c59, no served key moved",
      "packet s.5 item 1"
    ],
    "remedy": "Repair the 20-F patterns to match each stored filing's own item headings (ASML NA first), proven on the five real filings before any write; a site-Z producer deploy; then the store half and the FWD-18 walk. Close when: ASML NA's 20-F cuts business, risk and mdna on a real fetch and the stored source moves past parser 1.0.0",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v82",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v82"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": null
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-D1-S7",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "record-terraform-deploy.sh sets last_deployed_commit from the function's source_dir; opal-amgt-scoped-api's shipped code is the vendored delegate under lib/research/, outside source_dir, so the field is stale by construction for this function (it reads dd-4's commit after ee-6).",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-S7",
      "kin of row D1-S6 (REMEDIATION_v26)"
    ],
    "remedy": "The recorder derives last_deployed_commit from the build input (the packaged closure), not source_dir. Close when: a code-only deploy of this function moves the field to its own commit",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v82",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v82"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-D1-S8",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The /cloud-ops skill's on-box wrapper table names .tools/record-terraform-deploy.sh, which does not exist; the script is infra/aws/lambda/ci/record-terraform-deploy.sh.",
    "evidence": [
      "3.0.0_SA_CVO read: ls .tools/record-terraform-deploy.sh -> No such file; ls infra/aws/lambda/ci/record-terraform-deploy.sh -> present",
      "investigation row AMGT_RESAPP-D1-S8"
    ],
    "remedy": "Correct the path in .claude/skills/cloud-ops/SKILL.md. Close when: the table's path resolves",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v82",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v82"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-D1-S9",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "to-check.py reads the FIRST paired <status> while order files append each new status, so 331 of 5,020 tracked orders whose last status is terminal read ACTIVE, with no warning.",
    "evidence": [
      "3.0.0_SA_CVO read: .tools/to-check.py:120 re.search(r'<status>(.*?)</status>', ...) -- the first match",
      "investigation row AMGT_RESAPP-D1-S9"
    ],
    "remedy": "to-check reads the LAST paired status (as round-close-check's issuer ruling asks). Close when: ee-6 and dd-4 read complete in to-check --all",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v82",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v82"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  }
]
```
