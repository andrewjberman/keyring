# MDPF_HEALGAP -- round 1 remediations

<sweep_watermark>2026-10-08T14:38Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-08T14:38Z. Graduated at ADJUDICATION_v1: 7 rows, all INERT. Tool defects outside the project (S6, S7, S10) name the tool's owner, routed through 1.0.0_SA_CTO~DELL1.

```json
[
  {
    "id": "MDPF_HEALGAP-S2",
    "project": "MDPF_HEALGAP",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The runner's vendor calls carry no as-of, so FWD-3's eleven-day repair can only land current compositions under past dates (fabricated history); Andrew declined the refill.",
    "evidence": [
      "git show e5fb41862f: Andrew-direct ~13:58Z 'ACT 2 rec (no refill) approved' -- refilling would put today's compositions under past dates",
      "investigation row MDPF_HEALGAP-S2 (2.0.0_SA_COO~G1)"
    ],
    "remedy": "FWD-3 is re-scoped by 1.0.0_SA_CTO~DELL1: either a historical source is named or the outcome is restated (round-1 enrichment list item 2). Close when: the PRD carries FWD-3 restated or a historical source, ratified-text half re-signed",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_HEALGAP-S5",
    "project": "MDPF_HEALGAP",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "TO-HG-d1's write grant omitted the files its own deploy recorder writes (opal-assets CHANGELOG.json, the .open_deploys sentinel).",
    "evidence": [
      "SURPRISE_ROWS_OWED_FROM_TO_HG_D1_20261007.md Row 1 (on origin @ebd245f91d), cited by the row; drain-end report 'For the next cut: deploy grants enumerate the tools' writes (S5)'",
      "investigation row MDPF_HEALGAP-S5 (0.7.0_AE_CloudOps~F)"
    ],
    "remedy": "The issuer enumerates each deploy tool's write set in the next deploy order's <paths>. Close when: the next HEALGAP deploy order's <paths> names CHANGELOG.json and the sentinel path",
    "owner": "2.0.0_SA_COO~G1",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~G1",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~G1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_HEALGAP-S6",
    "project": "MDPF_HEALGAP",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "deploy_ledger.py close for one slug rewrote ten other seats' sentinels under .open_deploys/ in the same invocation (tool defect outside this project).",
    "evidence": [
      "git log -1 -- .tools/deploy_ledger.py: last author 1.0.0_SA_CTO; row evidence Row 2 lists the ten rewritten slugs",
      "investigation row MDPF_HEALGAP-S6 (0.7.0_AE_CloudOps~F)"
    ],
    "remedy": "Tool owner makes close write only its own slug's sentinel. Close when: a close of one slug leaves every other .open_deploys file byte-identical (git status clean outside the slug)",
    "owner": "1.0.0_SA_CTO (laptop, last author of .tools/deploy_ledger.py), routed via 1.0.0_SA_CTO~DELL1",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO (laptop, last author of .tools/deploy_ledger.py), routed via 1.0.0_SA_CTO~DELL1",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO (laptop, last author of .tools/deploy_ledger.py), routed via 1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_HEALGAP-S7",
    "project": "MDPF_HEALGAP",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "safe-apply.sh reports a gate that could not run (mangled path) as a naming-limb BLOCK; rc=2 does not separate 'name wrong' from 'gate could not run' (failed closed).",
    "evidence": [
      "git log -1 -- .tools/safe-apply.sh: last author 0.9.0_WK_NFRA_CTLPLN~13 (NFRA_CTLPLN)",
      "investigation row MDPF_HEALGAP-S7 (0.7.0_AE_CloudOps~F)"
    ],
    "remedy": "Tool owner prints a distinct verdict when the naming gate script cannot be opened. Close when: a safe-apply run with an unopenable gate path prints a 'gate could not run' line, not a naming verdict",
    "owner": "NFRA_CTLPLN owner (1.0.0_SA_CTO laptop), routed via 1.0.0_SA_CTO~DELL1",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "NFRA_CTLPLN owner (1.0.0_SA_CTO laptop), routed via 1.0.0_SA_CTO~DELL1",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "NFRA_CTLPLN owner (1.0.0_SA_CTO laptop), routed via 1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_HEALGAP-S9",
    "project": "MDPF_HEALGAP",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "TO-HG-d2 copied a code-deploy recorder step into a wiring-only apply; the recorder correctly refused the empty set.",
    "evidence": [
      "SURPRISE_ROWS_OWED_FROM_TO_HG_D2_20261007.md Row 1 (@905aa9c271); drain-end report 'wiring-only deploy orders omit the code-deploy recorder (S9)'",
      "investigation row MDPF_HEALGAP-S9 (0.7.0_AE_CloudOps~F)"
    ],
    "remedy": "Wiring-only deploy orders omit the recorder step or name the empty-set refusal as the expected outcome. Close when: the next wiring-only order carries no recorder step or names its refusal",
    "owner": "2.0.0_SA_COO~G1",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~G1",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~G1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_HEALGAP-S10",
    "project": "MDPF_HEALGAP",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A 0-diff targeted plan lists the Lambda in resource_changes (no-op), and record-deploy-scope.py prints the same refusal for a --plan path fault as for an empty set (diagnostic ambiguity, as S7).",
    "evidence": [
      "infra/aws/lambda/ci/record-deploy-scope.py at HEAD (path verified); row Row 2 @905aa9c271",
      "investigation row MDPF_HEALGAP-S10 (0.7.0_AE_CloudOps~F)"
    ],
    "remedy": "Tool owner separates the path-fault message from the empty-set refusal. Close when: a --plan path fault prints a distinct line",
    "owner": "record-deploy-scope.py owner, routed via 1.0.0_SA_CTO~DELL1",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "record-deploy-scope.py owner, routed via 1.0.0_SA_CTO~DELL1",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "record-deploy-scope.py owner, routed via 1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_HEALGAP-D1-S5",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A cloud-ops seat reported its restore timers dead while an armed background failsafe kept running and acted; the liveness report was wrong, not the act.",
    "evidence": [
      "0.0.0_AB_MSTR~DELL1 msg 924 relaying the laptop MSTR: task bv5miebw8 output FAILSAFE-WOKE/ACTING 06:08:40Z; drain-end report 'a seat that arms a restore names every mechanism it armed (D1-S5)'",
      "investigation row MDPF_HEALGAP-D1-S5 (2.0.0_SA_COO~G1)"
    ],
    "remedy": "A seat that arms a restore names every mechanism it armed and reads each one's state at hand-off. Close when: the next induced-failure exercise's ledger lists every armed restore mechanism with its read state",
    "owner": "2.0.0_SA_COO~G1",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~G1",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~G1",
      "at": null
    },
    "closed": false
  }
]
```
