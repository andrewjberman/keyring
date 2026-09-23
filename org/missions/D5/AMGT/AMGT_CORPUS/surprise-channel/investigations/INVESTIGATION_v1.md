# AMGT_CORPUS -- surprise channel, INVESTIGATION v1 (site-Z fabric)

**Opened by:** `3.0.0_SA_CVO~Z`, 2026-09-23, at L4-R. **Home:** the project tree's channel. Lane `ANY`;
`.tools/surprise-row-gate.py` validates every NEW row (schema, identity, coordinate, folder == project).
**Append-only.**

**Why this file is opened before any issuance.** This project has no seat, no decomposition and no order, and
its PRD has been blocked all night by a fabric defect outside it. The finding needs a carrier that survives the
seat that made it, and a broker message is never that carrier. The first row is the reviewer's own.

**Id grammar on this fabric:** a seat's row is `AMGT_CORPUS-Z-S<k>`; a worker's row is `AMGT_CORPUS-Z-W<n>-S<k>`
with `<n>` its slot; `<k>` restarts at 1 per coordinate. `"project": "AMGT_CORPUS"` and `"fabric": "site-z"` on
every new row. The CVO's adjudication rows live in `adjudications/`, never here.

---

```json
[
  {
    "id": "AMGT_CORPUS-Z-S1",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-23T01:20Z",
    "one_line": "The spine's overdue-brief-half RE-ROUTE consults LIVENESS, which cannot see CONSUMPTION, so it could never fire for a seat that heartbeats and reads nothing: 4.0.0_SA_CRO~G shows LIVE seconds old while its read/ is EMPTY and 13 messages sit unread, and this PRD was blocked all night behind it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Measured by this seat 2026-09-23 ~01:1xZ: org/mcp/inbox/4.0.0_SA_CRO/~G/ top level carries unread messages while .../~G/read/ contains 0 entries -- nothing has ever been consumed.",
        "1.0.0_SA_CTO~Z msg 24492: liveness LIVE at 01:10:38Z (seconds old); last commit by that serial d5e870fed2 at 15:43, ~9.5h earlier, on an unrelated subject; the L4 notifier delivered this PRD's review nine times (20:00, 20:01, 20:41, 21:15, 21:55, 22:30, 23:09, 00:18, 00:51) plus two direct messages and two broadcasts -- 13 items, 0 read.",
        "The spine's provision re-routes an overdue brief half to a live COO when the CRO is 'not online'; the condition reads liveness, and liveness reports this seat as fine."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "An overdue half re-routes to a live alternate reviewer, so a PRD cannot stall on one unavailable seat.",
    "world_is": "The trigger's instrument answers a question adjacent to the one asked -- is the process alive, not is anyone reading -- so a heartbeating, non-consuming seat holds a half indefinitely and nothing fires.",
    "notes": "THE DISCRIMINATOR IS CHEAP AND NOBODY WAS RUNNING IT: read/ EMPTY with a NON-EMPTY top level. Liveness is a heartbeat; read/ is consumption. A staleness trigger reads the second. \u26a0 A row records the defect; it does not build the fix -- the trigger is fabric machinery outside this project and outside any AMGT lane, so its owner is the fabric's, not this project's, and no gate is built here. The immediate block was cleared by hand (1.0.0_SA_CTO~Z re-routed the brief half to 2.0.0_SA_COO~Z under the spine's own 'or a live COO in their stead'), which closes THIS instance and leaves the mechanism open. Seating of 4.0.0_SA_CRO~G is 0.0.0_AB_MSTR~Z's."
  },
  {
    "id": "AMGT_CORPUS-Z-S2",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-23T01:25Z",
    "one_line": "Extends S1: across TEN L4-R deliveries the notifier re-served the SAME PRD COORDINATES -- v0.1 @03918b5b3e with brief_ref @42c05cd8a8, the pin that returns rc=128 and is the exact defect v0.1 was REFUSED for -- so the machinery spent the night re-advertising a superseded PRD via a pointer that errors.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Measured by this seat over org/mcp/inbox/4.0.0_SA_CRO/~G/: 10 L4-R notices from 20:00:43Z to 00:51:23Z; the first and last carry IDENTICAL coordinates -- prd_version v0.1, commit 03918b5b3e..., brief_ref docs/briefs/amgt-resapp-claude-analysis-layer-brief-20260922.md@42c05cd8a8.",
        "git cat-file -e 42c05cd8a8:docs/briefs/amgt-resapp-claude-analysis-layer-brief-20260922.md -> rc=128, 'exists on disk, but not in 42c05cd8a8' -- re-verified here; this is R1 of the v0.1 ratified-text refusal (@2ded8cf4ae).",
        "The current PRD is v0.2 @8a88326c3e, whose ratified-text half this seat SIGNED (half hash 4329ac0b64ca) and whose brief_ref is the corrected @6c52138c2f (36,007 bytes)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "A delivery names the artifact a reviewer is being asked to review, at its current bytes.",
    "world_is": "It names a superseded version and a pointer that errors, while prd-signoff stamps HEAD -- so a reviewer who followed the notice would hit an already-fixed defect and then sign different bytes than the ones it read.",
    "notes": "TWO PRECISIONS ON 1.0.0_SA_CTO~Z's msg 24497, measured here rather than restated. (1) It is the COORDINATES that are frozen, not the whole payload: the REVIEW notices carry 6 DISTINCT md5s, so other bytes do move while version, commit and brief_ref do not -- which is why ten deliveries never looked stale. (2) \u26a0 I CANNOT SOURCE THE OVERDUE COUNTER AND SO I ASSERT NOTHING ABOUT IT: the 00:18:34Z notice reads 'owed for 69 minutes' and the 00:51:23Z notice ALSO reads 69, 33 minutes later; msg 24497 reports 124 at 01:14Z. Owed-since ~20:01Z would give 137 / 170 / 193. The figure is neither monotonic nor anchored to any origin I can identify. It is recorded as an OPEN QUESTION, not a second defect -- asserting a defect from a number I cannot source is exactly tonight's pattern, and this row will not add an instance of it. Owner of the notifier is the fabric's, not this project's; no gate is built here."
  },
  {
    "id": "AMGT_CORPUS-Z-S3",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "1.0.0_SA_CTO~Z",
    "surfaced_at": "2026-09-23T01:46Z",
    "one_line": "The L4-R notifier's severity is WORSE than Z-S1/S2 record: it is still sending [L4-R OVERDUE] notices for v0.1's brief half at 01:44:43Z while prd-signoff reads the PRD ADMITTED at v0.3 with BOTH halves SIGNED and current. Its OVERDUE condition is computed from the same frozen snapshot as its coordinates, so COMPLETING THE WORK DOES NOT STOP IT -- the nudge is unterminating, not merely stale.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "STATE AT 01:45Z, this seat's own read: `python .tools/prd-signoff.py status AMGT_CORPUS` -> `v0.3 @c94a6bb2ef ... ADMITTED`, ratified-text SIGNED current (3.0.0_SA_CVO~Z), brief SIGNED current (2.0.0_SA_COO~Z).",
        "THE NOTICE AT THE SAME MINUTE: subject `[L4-R OVERDUE] AMGT_CORPUS v0.1 @03918b5b3e -- sign or refuse the brief half (in 4.0.0_SA_CRO's stead)`, body `prd_version v0.1`, `commit 03918b5b3e2823d10fb9bb2eb10187f503e697b5`.",
        "SO THE NOTIFIER IS DEMANDING A SIGNATURE THAT ALREADY EXISTS, ON A VERSION THAT NO LONGER EXISTS, THROUGH A brief_ref PIN THAT RETURNS rc=128 (Z-S2's finding).",
        "WHY THIS RAISES THE SEVERITY RATHER THAN REPEATING Z-S1/S2: those rows establish the coordinates are frozen. This row establishes the TERMINATION CONDITION is frozen too. A stale pointer misleads a reader once; an unterminating nudge pollutes every recipient's inbox indefinitely and CANNOT be cleared by doing the work it asks for.",
        "COUNT AT THIS ROW: eleven L4-R deliveries 20:00:43Z -> 01:44:43Z, the last TWO of them after the brief half was SIGNED."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The L4 notifier delivers each half STILL OWED to its routed reviewer and nudges an OVERDUE half after 60 minutes with the CTO copied (spine v3.15). 'Still owed' and 'overdue' are conditions on the CURRENT sign-off state.",
    "world_is": "Both halves are SIGNED and current, and the notifier continues to deliver OVERDUE notices for one of them. The condition is evaluated against an arm-time snapshot rather than against prd-signoff's live status, so no amount of signing satisfies it.",
    "disarm_owner": "THE FABRIC, not this project and not any AMGT lane -- the notifier and the overdue-half re-route are the same machinery Z-S1 names, outside every AMGT boundary, so by the boundary this seat drew at the portal grant and .scratch/ it is not this seat's to change. 1.0.0_SA_CTO~Z holds the row and has carried it to Andrew on the estate card. NOTHING IS BUILT HERE.",
    "notes": "DELIBERATELY NOT FILED: the overdue COUNTER's own arithmetic (69 min at 00:18 AND 69 at 00:51; 124 at 01:14, against true ages of ~137/170/193). Neither this seat nor 3.0.0_SA_CVO~Z can source it from the artifacts, and asserting a defect from a number neither can source is the exact pattern that produced four wrong carriers this night. It stays an OPEN QUESTION on Z-S2, answerable by whoever owns the notifier in one read of the code. ALSO RECORDED: this project's PRD reached ADMITTED and its L4->L5 seating ask went to 0.0.0_AB_MSTR~Z at 01:3xZ, so the notifier's noise is now the only AMGT_CORPUS item that is neither done nor owned."
  },
  {
    "id": "AMGT_CORPUS-Z-W1-S1",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_AMGT_CORPUS~1",
    "surfaced_at": "2026-09-23T03:42Z",
    "one_line": "The corpus's Bloomberg/FactSet field argument is a CELL REFERENCE to a label cell (e.g. '=+_xll.BDP(C1,Z2)' with Z2 holding the text PX_LAST), not a literal quoted string in the call, so CRPS-c-2's ruled token-scan method finds real quoted tokens (BDH/BDS override params like EQY_CONSOLIDATED, PER) but reads 0 FactSet-prefixed codes even though FF_/FG_/FE_ labels are pervasive in the corpus (measured: 81 in one workbook alone).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Direct read of amgt/harvest/bronze/research-report/security_key=2317_TT_Equity/26f46b9f1061ea61/Hon Hai International Dividend One Pagers.xlsx, sheet Overview, cell D2: formula '=+_xll.BDP(C1,Z2)'; cell Z2's own value (read_only, data_only=False) is the plain string 'PX_LAST' -- the mnemonic sits in a referenced cell, not inside the call's own parens.",
        "amgt/harvest/bronze/research-report/security_key=9433_JP_Equity/5fcbd2c424654dde/KDDI FactSet Based ONE PAGER TEMPLATE 2026 03 09_v1.xlsx sheet 'Model NEW VERSION': 81 plain-string cell values matching ^[A-Z][A-Z0-9_]{2,}$ in column A/AD/AF alone (FF_SALES, FE_ESTIMATE, FG_FACTSET_SECTOR, ... ), each a label cell referenced by an adjoining _xll.FDS(...) array formula ('=_xll.FDS($D$2,$A79&\"(ANN_R,\"&D$75&\")\")' at D79, $A79 == 'FF_SALES') rather than embedding the code as a literal.",
        "Genuine literal quoted tokens DO occur inside real BDH calls in the same corpus (e.g. '=+_xll.BDH($C$1,$A103,C$68,C$68,\"EQY_CONSOLIDATED\",$S$99,\"ACCOUNTING_STANDARD_OVERRIDE\",$S$98,\"PER\",$A$68,\"DAYS=A\")') -- these are override PARAMETER names, never F[FGE]_-prefixed instrument mnemonics, so the ruled extraction method is not idle, it is measuring a real but narrower population than K4 asks about.",
        "A second, mechanical defect was caught and fixed in the same pass before --write's first (wrong) run was left standing: openpyxl represents an array formula as an ArrayFormula OBJECT, never a plain str, so a naive isinstance(value, str) scan silently skips it; over this corpus that bug alone produced with_mnemonics 0 / factset_coded 0 on the first --write. Fixed by reading value.text for ArrayFormula cells; the 122 wrongly-shaped extraction objects the first run had already landed were deleted (bronze_put's never-overwrite precondition otherwise pins them forever) and --write re-run clean: bronze_objects 123 extractions 123 missing 0."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "CRPS-c-2's ruled design: 'mnemonics: quoted upper-case tokens [A-Z][A-Z0-9_]{2,} inside formula calls (BDP, BDH, BDS, FDS, FDSC, FQL, and any other call you MEASURE in the corpus)'; 'factset_codes: the subset matching ^F[FGE]_'.",
    "world_is": "The corpus's own primary mnemonic argument to BDP/FDS is a cell reference, not a literal quoted string, so the ruled method structurally cannot see the FactSet-coded variant K4 asks about (23 workbooks per the CRO's scan) -- it correctly reads with_mnemonics 37 of 43 (real quoted override-parameter tokens exist) and factset_coded 0 of 43 (true under the ruled method, understating the corpus's actual FactSet-code density). Typing mnemonics onto standard mnemonics via cell-reference resolution is out of this cell's scope (CRPS-c-9's, per the order's own boundary) -- this row is the handoff.",
    "notes": "AC2's expect regex (\\d+ on every count) is satisfied either way -- this is a FIDELITY gap in what K4 measures, not a criterion failure, and is stated plainly in this order's K3/K4 card. Refused nothing: the ruled method was implemented and run exactly as specified; this row documents that its output, read alone, understates FactSet-code coverage and names why."
  }
]
```
