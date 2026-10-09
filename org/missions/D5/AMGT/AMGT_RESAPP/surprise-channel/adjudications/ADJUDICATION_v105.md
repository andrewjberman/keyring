# AMGT_RESAPP -- round 87 L9: the ll-4 ledger applied, and NU's empty description (dell1)

<sweep_watermark>2026-10-09T20:14Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T20:14:00Z. L8 packet: 2.0.0_SA_COO~R1 msg 3114, round87/DRAIN_END_PACKET.md @11e12f0abe.
ll-4 ledger: sampled 17 of 66 CLOSED (17 hold) plus every DISMISSED reason class; applied 66 REMEDIATED, 30 CLOSED_UNREMEDIATED,
29 CARRIED left OPEN; 20 ARMED rows disarmed in the same write. Open remediation rows after the pass: 29. ll-2 / condition 4: NU's description empty -- MET at the API.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S37",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T20:14:00Z",
    "one_line": "AMGT_RESAPP.TO-AMGT-ll-4 ledger graded and applied (round-87 judgment item 2): 17 of 66 CLOSED rows sampled across evidence types (code at HEAD, gate code, tests, served read), 17 of 17 hold; every cited commit of 20 sampled is an ancestor of HEAD; the DISMISSED reason classes (object is a criterion of a terminal order; superseded or moot; worker environment since fixed; ARMED with no live instance; site-Z-only instance) hold on spot reads (AMGT-s-2 and s-7 complete; portal/package.json pins packageManager bun and a typecheck script). Applied in place: 66 OPEN->REMEDIATED, 30 OPEN->CLOSED_UNREMEDIATED (closure NOT_A_DEFECT, pointer the ledger @4c3f3fcb2e plus its reason), 29 CARRIED left OPEN with owners unchanged (an owner change is not an in-place clock). Open remediation rows after the pass: 29. Of the closed rows, 20 were still ARMED (hazard_standing ARMED, disarm never recorded); each one's disarm is recorded in the same write (disarm ARMED->DISARMED, at 2026-10-09T20:19:00Z), because the fix or the dismissal that closes it is also what removes the live hazard: Z-W1-S2, -W1-S3, -W2-S2, -W2-S4, -W3-S1, -W3-S2, -W3-S4, -W4-S1, -W7-S1, -W7-S5, -W7-S6, -W7-S7, -S1, -W31-S2, -W42-S5, -W88-S1, -S242, -W117-S5, -C-S35, -C-S372.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): a worker's disposition ledger is a self-report, graded on a sample before it is applied; every judgment graded by a seat that did none of the work.",
    "world_is": "AMGT_RESAPP.TO-AMGT-ll-4 ledger graded and applied (round-87 judgment item 2): 17 of 66 CLOSED rows sampled across evidence types (code at HEAD, gate code, tests, served read), 17 of 17 hold; every cited commit of 20 sampled is an ancestor of HEAD; the DISMISSED reason classes (object is a criterion of a terminal order; superseded or moot; worker environment since fixed; ARMED with no live instance; site-Z-only instance) hold on spot reads (AMGT-s-2 and s-7 complete; portal/package.json pins packageManager bun and a typecheck script). Applied in place: 66 OPEN->REMEDIATED, 30 OPEN->CLOSED_UNREMEDIATED (closure NOT_A_DEFECT, pointer the ledger @4c3f3fcb2e plus its reason), 29 CARRIED left OPEN with owners unchanged (an owner change is not an in-place clock). Open remediation rows after the pass: 29. Of the closed rows, 20 were still ARMED (hazard_standing ARMED, disarm never recorded); each one's disarm is recorded in the same write (disarm ARMED->DISARMED, at 2026-10-09T20:19:00Z), because the fix or the dismissal that closes it is also what removes the live hazard: Z-W1-S2, -W1-S3, -W2-S2, -W2-S4, -W3-S1, -W3-S2, -W3-S4, -W4-S1, -W7-S1, -W7-S5, -W7-S6, -W7-S7, -S1, -W31-S2, -W42-S5, -W88-S1, -S242, -W117-S5, -C-S35, -C-S372.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "sampled CLOSED rows, each read by 3.0.0_SA_CVO at HEAD: Z-W1-S3 (.gitignore:47-48, no blanket lib/); Z-W18-S8 (scoped_amgt.py HELD_BASIS_OBJECT/_held_uncited, 5 hits); Z-W20-S7 (comp-secrets --value-only requires --reveal); Z-W20-S13 (membership.py held None third value); Z-S341 (to-decomp-ref-lint TERMINAL_STATUS has WITHDRAWN); Z-W88-S1 and Z-C-S372 (bright_data_serp raises for max_pages != 1); Z-S242 (git ls-files --eol etf-classifications.tf i/lf); Z-S366 (research_pulls.py NO_BLOOMBERG_LIBRARY exit 6); D1-S8 (record-terraform-deploy.sh exists at the SKILL path); D1-S9 (to-check.py reads the last line-anchored status); Z-S78 (build_lists.py:129,156 ASSIGNED); Z-W21-S3 (comparable.py COMPANY_ID_FIELDS); Z-W21-S5 (engine.py 'NO FX rate'); Z-W7-S7 and Z-C-S35 (watchlist conftest socket blocker); Z-W32-S3 (test_slash_safe_key_sites with the bright_data tests: 80 passed)",
        "served: round87_prep/checks/r87_withheld.py --crit AC1 on the live function -> R87 WITHHELD AC1: YES (5 of 5)",
        "ledger org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~348/DISPOSITION_LEDGER.json @4c3f3fcb2e: 125 rows, CLOSED 66 / DISMISSED 30 / CARRIED 29; every row found exactly once in remediations/, all OPEN before the pass"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 record of a graded and applied disposition ledger, not a hazard."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S38",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T20:14:00Z",
    "one_line": "AMGT_RESAPP.TO-AMGT-ll-2 / CTO condition 4 (R2), round-87 judgment item 1, MET at the served API: the live opal-amgt-scoped-api /thesis for NU_US_Equity serves company_description sentences [], description_verdict_state NO_SENTENCES, reason 'no served D-1 company_description sentence passing the describes-the-business test'; ASML reads the same. No page walk this round: the empty card's page wording was last read for ASML in round 83 as 'No company description is on file yet.', which misstates the reason (withheld for failing the test, not missing); that wording is DSGN_AMGTV1's and stays carried. ll-1's FAILED-withhold path is not exercised live, as no name reads FAILED now; under the ruled bound (msg 3091) it rests on the byte read of the deployed scoped_amgt.py.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): a worker's disposition ledger is a self-report, graded on a sample before it is applied; every judgment graded by a seat that did none of the work.",
    "world_is": "AMGT_RESAPP.TO-AMGT-ll-2 / CTO condition 4 (R2), round-87 judgment item 1, MET at the served API: the live opal-amgt-scoped-api /thesis for NU_US_Equity serves company_description sentences [], description_verdict_state NO_SENTENCES, reason 'no served D-1 company_description sentence passing the describes-the-business test'; ASML reads the same. No page walk this round: the empty card's page wording was last read for ASML in round 83 as 'No company description is on file yet.', which misstates the reason (withheld for failing the test, not missing); that wording is DSGN_AMGTV1's and stays carried. ll-1's FAILED-withhold path is not exercised live, as no name reads FAILED now; under the ruled bound (msg 3091) it rests on the byte read of the deployed scoped_amgt.py.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO read the live function via round86_prep/checks/r86_description._thesis(key, 'deployed') at ~20:1xZ: NU_US_Equity and ASML_NA_Equity company_description sentences [], NO_SENTENCES",
        "round87/DRAIN_END_PACKET.md @11e12f0abe s.1 ll-2 and ll-3 (live b7Lj1J)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record, not a hazard."
  }
]
```
