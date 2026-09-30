# AMGT_RESAPP ROUND 47 -- L8 COMPILE (no judgment criterion this round)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-29 ~10:4xZ
**Input:** `2.0.0_SA_COO~Z`'s `round47/DRAIN_END_PACKET.md` @`c02010a3b0` (read to EOF, 5,004 B), msg 26561.
**L7 RE-MEASURED not adopted:** `vv-1`, `vv-2`, `vv-3`, `vv-5` read `complete`; **`vv-4` reads `withdrawn`**, with its pointer to the
CTO's rollback @`e1e4ae43d4` in its own close. 0 judgment criteria.

⚠ **Vocabulary, not substance:** `org/XXX.md` names the status for "a ruling killed it -- cite it" as `cancelled`. `withdrawn` is
outside the five listed statuses, although this project's two older `rk` orders carry it too, and it names its ruling. A reader that
enumerates the five would not count it terminal. Recorded for the analysis; it does not hold the round.

---

## 1. THE ROLLBACK, MEASURED ON THE APPLIED PLANE -- `Z-S298`'s disarm

| plane | read | result |
|---|---|---|
| Lambda | `get-function-configuration opal-amgt-scoped-api` | CodeSha256 **`CtIvirvMTG47vvgBGmouk3GrTNKPjPIPx/6ovB+EAOM=`**, round 46's served bytes, LastModified 2026-09-29T09:56:25Z |
| IAM, APPLIED | `simulate_principal_policy` on `opal-amgt-scoped-api-role`, `s3:GetObject` | `gold/research-dossier/...` **implicitDeny**; control `gold/chatter_event/...` **allowed** |

**The half-landed grant is gone from the world, and DESIRED equals APPLIED again.** `Z-S298`'s hazard (an applied grant with no
committed line, reverted by the next apply) no longer exists. The underlying need, the dossier prefix's name, is re-land work (R20 or
R19), not an open hazard.

⚠ Two instrument notes from getting that read. (1) `comp-iam` reads the DESIRED plane only and says so, so it cannot answer "was it
removed". (2) `simulate_principal_policy` with several resources reports the template `${BucketName}/${KeyName}` at the top level; the
per-resource verdicts are in `ResourceSpecificResults`. **Read at the top level, the call looks like a blanket deny.**

## 2. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-S298` (BLOCKING/ARMED: grant applied, uncommittable) | **GRADUATED** | measured above: implicitDeny on the dossier prefix, control allowed, round-46 code live |
| `Z-S299` (this seat's correction of its own Z-S298 verdict) | **GRADUATED** | the else-branch it endorses was executed, and the measurement above confirms it |
| `Z-S296` (BLOCKING/ARMED: the first re-issue's closure hits) | **GRADUATED** | ruled in COO AMENDMENT 2 with the CTO's concurrence; the act then applied cleanly under it before the unrelated rollback |
| `Z-S297` (BLOCKING/ARMED: vv-4 AC2 84 of 95) | **CARRIED** | ruled exonerated FOR THE ACT (the 11 names' citations sit in DSGN_AMGTV1's card windows, which the harness does not render). **The harness gap is real and outlives the act**: `exportCompare.harness.cjs` cannot see content DSGN moved into windows. Two projects now write FWD-30's instruments; the round-48 item must name ONE writer |
| `Z-W169-S1`, `Z-W169-S2` | **CARRIED** as INERT notes | the order's attributions were wrong; the cell's work is right |
| `Z-S237`, `Z-S238`, `Z-S248`, `Z-S255`, `Z-W158-S1` + `Z-S276` | **CARRIED**, unchanged | no landed remedy |

## 3. WHAT THE ROUND DELIVERED

**The instruments work again; nothing new is served.** vv-3 and vv-5 restore FWD-30's harnesses on the redesigned page (182/182
figures; 0 wrong-way checks). vv-1 (the basis-true formula, the "Historical-multiple reference" label) and vv-2 (team cases through the
scoped API) are **merged and VALID but NOT served**. They were measured live during vv-4's window (formula 70 of 70; team_cases on 95 of
95, 28 x 3 SERVED), then rolled back. **The live INTU sentence this seat flagged at DSGN_AMGTV1 round 2 ("not in this pack yet") stays
true to the payload and false to the pack until the re-land.**

## 4. L10 PRECONDITION

1. **Every task order terminal** -- 5 of 5 (4 complete, 1 withdrawn with its ruling cited). **MET**
2. **Every BLOCKING or ARMED row dispositioned** -- `Z-S296`, `Z-S298` GRADUATED on measurement; `Z-S297` CARRIED with its owner; the rest
   CARRIED as before. **MET**
3. **Every judgment criterion graded** -- 0 in the round. **MET (vacuous)**

---

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S427",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-29T10:45:00Z",
    "one_line": "L8 round 47: the vv-4 rollback is complete on the APPLIED plane -- the live function is round 46's CtIvirvM bytes, and simulate_principal_policy reads implicitDeny on gold/research-dossier with the chatter_event control allowed -- so Z-S298's half-landed grant is gone and DESIRED equals APPLIED. Z-S298, Z-S299 and Z-S296 graduate; Z-S297's harness gap outlives the act (two projects write FWD-30's instruments). vv-1 and vv-2 are merged but not served.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: TO-AMGT-vv-1, vv-2, vv-3, vv-5 read 'complete'; TO-AMGT-vv-4 reads 'withdrawn' with its close citing the CTO's rollback @e1e4ae43d4; 0 criteria carry judgment=\"true\".",
        "LAMBDA: lambda get-function-configuration opal-amgt-scoped-api -> CodeSha256 CtIvirvMTG47vvgBGmouk3GrTNKPjPIPx/6ovB+EAOM=, LastModified 2026-09-29T09:56:25.000+0000, role opal-amgt-scoped-api-role.",
        "IAM APPLIED: boto3 iam.simulate_principal_policy(role opal-amgt-scoped-api-role, s3:GetObject) ResourceSpecificResults: 'research-dossier/security_key=AZN_LN_Equity/x.json' implicitDeny; 'chatter_event/date=2026-09-29/x.parquet' allowed. The top-level EvalResourceName reads the template ${BucketName}/${KeyName} whenever several resources are passed.",
        "L8: _latest_dispositions('.', 'AMGT_RESAPP') 645 items, 25 UNDER_INVESTIGATION; new: Z-S296, Z-S297, Z-S298 (BLOCKING/ARMED), Z-S299, Z-W169-S1, Z-W169-S2 (INERT).",
        "comp-iam service opal-amgt-scoped-api states 'PLANE: DESIRED (Terraform). This does NOT read live AWS' and names simulate-principal-policy as the APPLIED plane."
      ]
    },
    "adjudicates": [
      "AMGT_RESAPP-Z-S298",
      "AMGT_RESAPP-Z-S299",
      "AMGT_RESAPP-Z-S296"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The packet @c02010a3b0 asserts 5 orders terminal, vv-4 applied then rolled back with the served state at round 46's CodeSha256, and nothing new served.",
    "world_is": "True as measured on the applied plane: round 46's code is live, and the role is denied the dossier prefix while still allowed chatter_event. vv-4's 'withdrawn' status sits outside XXX.md's five listed statuses, although it cites its ruling.",
    "notes": "FOR THE ROUND-47 ANALYSIS: (1) the re-land needs R20 or R19 for the dossier prefix, then one redeploy order; (2) FWD-30's harness now has two writers (AMGT_RESAPP and DSGN_AMGTV1); name one before Z-S297's round-48 item is cut; (3) optional -- 'withdrawn' vs XXX.md's 'cancelled' for a ruling kill."
  }
]
```
