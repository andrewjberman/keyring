# IRPT_BCKEND: CVO adjudication, round 4 (workstream ~PJ, the TRANSPLANT candidates of the holdings bundles: the CTO's condition for the 580/582/583 half)

<sweep_watermark>2026-10-15T19:51Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T19:51Z, on msg 8586 (shared packet @f7b4555d40). One order, IB-pr-595 (risk SERVED, read-only), complete, merged @5bf120faa2. The record is `deliverables/0.9.0_WK_IRPT_BCKEND~434/IB228-1_holdings_transplant_candidate.json`; the transplanted files are committed under `~434/transplant/<firm>/`. Re-run here at HEAD: IB228-1-AC1..AC3 PASS (exit 0). `round-close-check --round 4 --workstream "~PJ"`: MAY-CLOSE.

**The CTO's condition (msg 8537, @f6519b5d11), re-derived here against the LIVE bundles: MET for all three firms.** Read-only `get-object` of each live bundle; the transplant files from the commit; counts only.

| firm | live VersionId (LastModified) | live members equal to minting pin | six v127 drift files, live = pin | candidate `allow_older_date` / `ONE-DATE BYPASS` | cusip lines live -> candidate | changed lines outside the stripped ABSENT-AT-SOURCE blocks | `publication.py` |
|---|---|---|---|---|---|---|---|
| 49financial | 5eOkwoqs (2026-10-15T15:19:37Z) | 46 of 46 at b1d354cfc9 | yes (6 of 6) | 0 / 0 | **12 -> 12** | 35 | = HEAD's (10 lines vs live) |
| cottonwood | VmEyGROJ (15:20:31Z) | 46 of 46 at 5fad7eaaa8 | yes | 0 / 0 | 2 -> 2 | 35 | = HEAD's |
| inflection | SngSJHRb (15:21:09Z) | 46 of 46 at 5fad7eaaa8 | yes | 0 / 0 | 2 -> 2 | 35 | = HEAD's |

The 35 lines outside the blocks are the same in all three firms, and this seat read each one: the `COT_SILVER_ROOT` constant and its use; the `resolved_scope_fingerprint` helper (sha256 of the SORTED ids) replacing the inline expression; the gate's new optional parameter and docstring; `lost = gone - closed` replacing a repeated expression; blank lines and paren reflow. The fingerprint is value-identical: at both minting pins `unique_account_ids = sorted({...})` already, so sorting again changes nothing. None of the 35 is bypass or CUSIP code. Only `holdings_snapshot.py` and `publication.py` change; the other 44 members are the live bytes. **The diff against live is the exemption alone.** The pair for IB-pr-580/582/583 may be signed ON THESE DIGESTS ONLY: candidate bundle sha256 d2eaf305... (49F) and bc2e8f54... (Cottonwood and Inflection). The IB-pr-589 and IB-pr-590 candidates stay unsignable (v126, v127). A re-measure of 49F's refusal on this tree (IB-pr-602) is in flight and does not bear on the condition.

**The READ of which commit dropped the CUSIP lines.** No order or row in this packet carries it (task orders IB-pr-596..603; channel rows W433-W439, S208). This seat measured it. The probe line `def cusip_key(security_id)` is at 49F's pin and absent at HEAD, and `git log -S` on HEAD's history names **5fad7eaaa8**, "revert(IRPT_BCKEND pin 2 ...): undo the CUSIP port 01e843ce2e". 5fad7eaaa8 IS an ancestor of HEAD. The pin-2 revert was committed on the trunk line, not a side branch. So **trunk carries no CUSIP port for any firm**, while 49 Financial's LIVE bundle carries it. Any future 49F holdings build from HEAD, or any overlay of HEAD's file, reverses 49F's live CUSIP handling. The transplant avoided this by building from each firm's own pin. This is a standing hazard for every later 49F release (`2.0.0_SA_COO~P2` to route: restore the port on trunk for 49F, or make every 49F build pin-based by rule). Carried by this row, ARMED. `D2-S206` is discharged for the transplant candidates by the measurement above.

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S40",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T19:51:00Z",
  "one_line": "~PJ r4. CTO condition (msg 8537) MET for all three firms, re-derived against the live bundles: only holdings_snapshot.py and publication.py change, 44 members equal live, live = each minting pin 46/46, the six v127 drift files unchanged; candidate allow_older_date 0 and no ONE-DATE BYPASS; 49F cusip lines 12 -> 12; 35 lines outside the blocks, read one by one, all exemption plumbing (fingerprint value-identical). Sign the 580/582/583 pair on d2eaf305 (49F) and bc2e8f54 (COT/INF) only. NEW HAZARD: the CUSIP-drop commit is 5fad7eaaa8 (the pin-2 revert), an ancestor of HEAD, so trunk carries no CUSIP port and any HEAD-based 49F build reverses live 49F; ARMED, ~P2. IB228-1-AC1..AC3 PASS. Dismissed (5): D2-S206 (discharged for the transplant), D2-W434-S1..S4 (WARN and process notes).",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~P2",
  "adjudicates": [
   "IRPT_BCKEND-D2-S206",
   "IRPT_BCKEND-D2-W434-S1",
   "IRPT_BCKEND-D2-W434-S2",
   "IRPT_BCKEND-D2-W434-S3",
   "IRPT_BCKEND-D2-W434-S4"
  ],
  "spec_asserts": "CTO msg 8537 (@f6519b5d11): the per-firm diff against live equals the exemption alone; CLAUDE.md rule 22a (compare by content against the build input); never-widen (section 5).",
  "world_is": "The transplant candidates are the exemption alone and signable at their digests. Trunk (HEAD) lacks 49F's live CUSIP port because the pin-2 revert landed on trunk; that will bite the next HEAD-based 49F build unless restored or ruled out.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T19:3xZ of the invocations in IB-pr-595: IB228-1-AC1..3 PASS, exit 0; round-close-check ~PJ round 4 MAY-CLOSE",
    "scratch tp.py, read-only: s3 get-object of irpt/<firm>/code/gold/investor-reporting-holdings.tar.gz (VersionIds 5eOkwoqs, VmEyGROJ, SngSJHRb); live members vs git show <pin>:<path> 46/46 equal; six drift files equal; transplant files vs live: counts and the 35-line diff outside the stripped blocks printed and read",
    "git show b1d354cfc9|5fad7eaaa8:holdings_snapshot.py: unique_account_ids = sorted({...}) at lines 2725 / 2708",
    "git log -S 'def cusip_key(security_id)' HEAD -- holdings_snapshot.py: 5fad7eaaa8 (revert of 01e843ce2e) and 01e843ce2e; git merge-base --is-ancestor 5fad7eaaa8 HEAD: yes",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~434/IB228-1_holdings_transplant_candidate.json: candidate sha256 d2eaf305 (49F), bc2e8f54 (COT, INF)",
    "investigation rows D2-S206, D2-W434-S1..S4",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_PM1_PN2_PN3_PJ4_PJ5_PO8_DRAIN_END_20261015.md @f7b4555d40 (msg 8586)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "S206's widened blast radius is discharged for the transplant candidates by measurement; the four worker rows are WARN and process notes. The trunk CUSIP hazard this round surfaces is carried ARMED on this row with ~P2."
 }
]
```
