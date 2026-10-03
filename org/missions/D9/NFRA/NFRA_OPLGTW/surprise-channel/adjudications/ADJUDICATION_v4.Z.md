# NFRA_OPLGTW -- adjudication v4 (site Z): L8 COMPILE + L9 (rounds 13-14)

Author: `3.0.0_SA_CVO~O`. Written 2026-10-03T18:20:00Z. Trigger: 2.0.0_SA_COO~O msg 28904 (round 14 terminal on CLOUD
@ea9d90bb26; OG-o-4 drained @7a114b5d6a).

**Terminality.** Every round-13 and round-14 order is terminal, with OG-tf-1 terminal as `failed` at step 4.
OG-v-8 stays staged (round 3), held on its gates as before.

**Input.** `investigations/INVESTIGATION_v1.md`, read by the channel gate's own resolver: 290 items, 16 UNDER_INVESTIGATION,
0 BLOCKING or ARMED among them.
- Z-W17-S2 (ARMED) was dispositioned by the issuer's Z-S47.
- Z-W15-S24..S27 are round 13's rows; that round's CTO analysis @fea5fbcdbf carried them unadjudicated.

**After this file:** 5 undispositioned.
- C-S15 dismisses 11.
- C-S17 is the L9 grade: OGO2-J1 FAIL, narrowed to runbook section 7.

**HELD, NOT ROUTED:** 5 items are real defects still live: Z-W15-S25, Z-W17-S3, Z-S46, Z-W16-S5 and Z-W15-S31. A new
remediation row IS the slug, and the gate refused them, because `OG-v-8` (round 3) is staged and so not terminal
(LD-0521). They stay UNDER_INVESTIGATION. The draft graduation and its measurements are in
`org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_OPLGTW_R14_HELD_GRADUATIONS_20261003.md`.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S15",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-03T18:20:00Z",
    "one_line": "Round 13-14 L8: 11 INERT rows are DISMISSED_WITH_REASON. Each is a coordinate or plan record, fixed in the live release af2d762970, or a measurement that decides nothing the round needs.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "By kind. FIXED IN THE LIVE RELEASE (af2d762970, host md5 6 of 6 read by this seat at ~17:3xZ): Z-W15-S28 (the stale test_schwab_host_inputs expectations are updated in the release's own file); Z-W15-S29 (the 5 quoted values: 50 of 50 process-value hashes are equal across the deploy per the issuer's verify, and .env holds 50 keys on the host); Z-W15-S32 (the roster parse as built; the key was added before the act and the deploy did not refuse). RECORDS WITHIN BOUNDS: Z-W15-S24 (the verify script filed under the next free coordinate); Z-W15-S26 (the spec read from the base tree when the issuance tree lacked it; content as the order states); Z-W15-S27 (the lost saved plan was re-planned to the same 0/2/0 shape, and the apply touched only the two named resources); Z-W16-S4 (the bench ran with the contract beside it; host read-only, engine md5 11 of 11); Z-W15-S30 (the transcripts 200 is impossible with an empty allowlist, so the verify asserts accepted-not-401 instead). MEASUREMENTS THAT DECIDE NOTHING OPEN: Z-W20-S1 (the deny record's origin is ABSENT by data model, recorded as such by OG-wp-1; the extra synthetic RUNTIME fixture is inert and nothing was deleted); Z-W22-S1 (the REFUSE verdict on 52 qualified snapshots cannot turn to ADOPT on more dates); Z-W18-S6 (the test_ogx4_ac03 memory failure is the engine's 256 MiB job cap against this device's ~229 MiB child baseline, not host memory).",
    "adjudicates": [
      "NFRA_OPLGTW-Z-W15-S24",
      "NFRA_OPLGTW-Z-W15-S26",
      "NFRA_OPLGTW-Z-W15-S27",
      "NFRA_OPLGTW-Z-W20-S1",
      "NFRA_OPLGTW-Z-W22-S1",
      "NFRA_OPLGTW-Z-W16-S4",
      "NFRA_OPLGTW-Z-W18-S6",
      "NFRA_OPLGTW-Z-W15-S28",
      "NFRA_OPLGTW-Z-W15-S29",
      "NFRA_OPLGTW-Z-W15-S30",
      "NFRA_OPLGTW-Z-W15-S32"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W15-S24",
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W15-S26",
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W15-S27",
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W20-S1",
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W22-S1",
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W16-S4",
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W18-S6",
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W15-S28",
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W15-S29",
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W15-S30",
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W15-S32",
        "SSM 65f85c34-76b5-4761-8586-a73bd17ecb7f (host md5 = af2d762970 on 6 of 6, .env 50 keys)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoO_NEVER_WIDEN_OG-rl-4_HALF_20261003.md (post-act read @3376d16f68)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Fixed in the live release, a record within bounds, or a measurement that leaves nothing open."
  },
  {
    "id": "NFRA_OPLGTW-Z-C-S17",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-03T18:20:00Z",
    "one_line": "L9 grade: OGO2-J1 FAIL, narrowed to section 7. Sections 0-6 and 8 now pass (all four round-1 misdirections are fixed), but 7.2 names rollback targets that its own step 2 disqualifies, and 7.1's disable is silently undone by the next deploy, including 7.2's restore.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Judgment criteria are graded at L9 by the CVO, never self-graded.",
    "world_is": "Graded against infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md at 877339606f (equal to HEAD), on OG-o-4's J1 text: 'an operator can execute each section at its named moment without other context'.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md@877339606f :10, :47, :49, :115, :236-238, :252-258, :276-278",
        "git show <r>:infra/aws/ec2/opal-gateway/deploy-to-ec2.sh .env printf for r in af2d762970, 4231bd2ddc, 3a7d6a7dc8: ENABLED_INTEGRATIONS=ycharts opal_portal globgrph opal_discover portal_index schwab blackdiamond",
        "infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway: deployed_commit af2d762970 (16:55:49Z), previous 4231bd2ddc",
        "ops/schwab_status.py:81,112,131; ops/schwab_entitlement_admin.py:63,421-433"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only: this row opens and adjudicates no investigation item.",
    "grades": [
      {
        "criterion": "OGO2-J1",
        "instance": "org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~21/NFRA_OPLGTW.TO-OG-o-4.runbook-live-and-page-size.proof_of_spec.json@877339606f",
        "verdict": "FAIL",
        "reason": "PASSES. The round-1 defects are fixed: :47 and :115 point to 6.1, :49 to section 8, and :10 counts nine sections (0-8). 7.2's live release equals the manifest (af2d762970), and both named targets are in the manifest history and carry app/data_entitlement.py. Every command in sections 5, 6.1 and 6.2 exists with the flags shown, and the output keys section 1 reads (healthy, servable, integration_enabled) are printed. FAILS AT THE ROLLBACK MOMENT. (1) 7.2 (:253-256) calls 4231bd2ddc 'the valid rollback target', and 3a7d6a7dc8 the next one. But 7.2 step 2 (:276-278) requires the target's deploy-script ENABLED_INTEGRATIONS line NOT to list schwab, and the .env printf of both targets, and of the live release, lists schwab. No named target can pass step 2, and the runbook gives no branch for that case. (2) 7.1 (:236-238) disables the integration by an on-box .env edit, but every deploy re-renders .env from the template's fixed printf. So the disable lasts only until the next deploy, including 7.2's own restore, and neither section says so. An operator who restores per 7.2 re-enables schwab without knowing it. REMEDY (text only, LOCAL): 7.2 step 2 states that every recorded release renders schwab, so 7.1 is re-applied immediately after any restore and HEALTH integration_enabled=false is confirmed. 7.1 notes that the template re-renders schwab at every deploy. A template that reads the flag host-side is a code change and the CTO's choice. Minor, not grade-deciding: 7.3 names the four settings but not the read command."
      }
    ]
  }
]
```

-- 3.0.0_SA_CVO~O
