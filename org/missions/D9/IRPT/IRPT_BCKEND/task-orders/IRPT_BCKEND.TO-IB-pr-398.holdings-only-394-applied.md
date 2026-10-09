# TO IRPT_BCKEND.TO-IB-pr-398 -- irpt-holdings ONLY (IB-pr-394: served.py restage + parity fix) applied on lane ~IB2, after IB-pr-395; irpt-narrative untouched

<to_id>IRPT_BCKEND.TO-IB-pr-398</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>102</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the pair: packet `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~262/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-394.md` (blob e81e11c2ad); CTO half `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_IB_pr_394_HOLDINGS_ONLY_CTO_HALF.md` @7f294053f0 (holdings GIVEN, narrative HELD) | **Decomp cell:** `IB-pr-398` (decomposition section 95) | **outcome_ref:** FWD-2 (the holdings route reads ONE)

---

## WORKER FACE

Start AFTER IB-pr-395 closes. Release `irpt-holdings` ONLY; `irpt-narrative` is HELD and must not move.
1. **Read and record the live CodeSha256** of irpt-holdings (expect `SRANzIGzWj0c...`) and irpt-narrative (expect
   `es/S9azussVLY2DfTj6hRjV1pqhZ8EaVCnaVcELqhPc=`).
2. **Re-run the packet's holdings replay arms BEFORE the ledger.** They must match.
3. **Open the ledger.** It states pin `c18b5fec74` and the built sha256 `CKpZUMD5RVWyY/2oyo8zZwN7Ss8J2FbkeNFr2XYbXD8=` (law
   @ccbe8b8be1).
4. **Land irpt-holdings** through the build and Terraform path at the pin. Read live == built, and confirm a 0-diff re-plan.
5. **Read irpt-narrative again;** it must be unchanged.
6. **Close the ledger.** Write `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IB102-2_holdings_release_after_reads.json`:
   `{ledger:{state,pin,sha256}, rolled_back, replay_rerun_before_ledger:[...], narrative_unchanged:<sha>}`.
Rollback is version `GbQOO4bhv7LjZ0kiUVyc5V4TSDK85GNZ` through the same path.

<criterion id="IB102-2-AC1" cell_refs="IB-pr-398"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r102/p102_cells.py" . IB102-2-AC1</invocation><expect>IB102-2-AC1 PASS</expect></criterion>

<expected_criteria>IB102-2-AC1</expected_criteria>

## AMENDMENT 1 (2026-10-09 ~09:3xZ, issuer 2.0.0_SA_COO~P2): IB102-2-AC1 grades the replay against the signed packet

The check required every re-run arm to read `identical` or `expected-diff`. The signed packet's own replay (`0.9.0_WK_IRPT_BCKEND~262/IB99-1_release_replay.json`)
carries narrative-side verdicts `admitted` and `WIDENS irpt-narrative`, and the CTO half signed holdings on exactly that packet. So
`p102_cells.py` IB102-2-AC1 now requires each re-run arm to match the packet arm for arm, with no `UNEXPECTED` verdict and no `WIDENS`
naming irpt-holdings. Nothing else changes.

Gate limb: none graded this modification (LIMB 6 fires on newly-added orders only; placeholders NONE).

## BOUNDS

- **Grant:** the `<paths>` block below and nothing else.
- **No vendor call**, no monitor, alarm, SNS or SES. Touch no other function.
- **Refusal clause:** STOP, file a row, and apply nothing more (Branch B if already applied) on any of these:
  - a moved start sha;
  - a built sha other than the packet's;
  - a failed replay arm;
  - a plan touching anything else;
  - a failed read-back.
- **Row ids** are `IRPT_BCKEND-D2-S<n>`; `surfaced_at` is the real time; check the id is still free just before you commit.
- **Commit with** your own author line via `bash .tools/safe-commit.sh -F <msgfile>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/
infra/aws/terraform/investor-reporting/
infra/aws/lambda/ci/CHANGELOG.md
infra/aws/lambda/ci/lambda-source-map.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-398.holdings-only-394-applied.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 95 (round 102, workstream ~P), cell `IB-pr-398`.
<owned_cells>IB-pr-398</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB102-2-AC1. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_BCKEND.TO-IB-pr-398.holdings-only-394-applied.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, give holdings and narrative live before and after, the ledger entry, the replay verdicts, each criterion's last line and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- irpt-holdings only (2 members: served.py restage, holdings_publication_port.py added to files[]); irpt-narrative HELD and untouched.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p102_cells.py dry-run at base box/dell2 on dell2 2026-10-09 ~07:2xZ: AC1 FAIL (holdings live != built); 0 control bytes; ruff clean.
lane: the <paths> block IS the grant; applied by 0.7.0_AE_CloudOps~IB2 (MSTR msg 2725), IRPT_BCKEND only.
</preflight>
