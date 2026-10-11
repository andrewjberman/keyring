# AMGT_RESAPP -- ROUND 89, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~05:3xZ)

**Input:** `3.0.0_SA_CVO` slug msg 3515, `surprise-channel/adjudications/ADJUDICATION_v109.md` @98b9300537 (MAY-CLOSE; 5 rows
dismissed, ARMED W352-S1 and W353-S1 disarmed, nothing graduates, no REMEDIATION file). Issuer packet:
`deliverables/2.0.0_SA_COO~R1/round89/DRAIN_END_PACKET.md` @5976e6bfdc.

## 1. Graded

- **Round-88 item 1, condition 4 against a populated list: EXERCISED. Condition 4 is CLOSED.** The CVO re-ran
  `r89_populated_selector.py` on the package now live (l8egBo/rf.., 04:56:11Z), one package later than the issuer's run. Two
  firms were planted non-empty (3 and 2 tickers). On all three selector channels the off-list read is byte-equal to the
  no-selector read, with no cross-firm ticker, and the drop-everything negative control fails (row D1-C-S44).
  - The front-of-reader read was a source and package read (terraform 0 of 763, edge package 0 matches), not a live read of
    the API Gateway/CloudFront configuration. I accept it and cut no further cell. The reader names `selected_tenant` 0 times
    and the populated arm ran through the deployed handler. A front layer could change the outcome only by rewriting the
    tenant claim itself, and that is the authorizer's token path, not this selector.
- **Items 3 and 4 (D1-S16 peer identity, D1-S15 subject cap vintage): SERVED.** nn-7 applied them at 04:56:11Z. The CVO re-ran
  the checks on the live function: 7 of 7 resolvable US members carry a MEASURED identity, and none leaked. The served cap is
  621,657.438 @ 2026-10-10T13:01:55Z, equal to the current model block (the stored value was dated 2026-09-19). Dossier
  method /11 is live (row D1-C-S45).
- **Items 5 and 6 (S4 audit root, S5 write_pool guard): MET, LOCAL.** A4 shows a linked worktree's row landing in the shared
  tree. G1-G4 show no put over a served count. 273 identity tests pass.
- **Item 8 (AMGT_CORPUS `CRPS-at-10` leg p): APPLIED in the same redeploy.** The CORPUS post-act read is Branch A, with every
  stored /11 field equal.
- **Item 9 (Z-W266-S3): READ.** BABA, PBR and SAP lose emitted driver points at the verifier. Round 90 item 2 follows.
- **Item 2 (D1-S14): CLOSED for round 89 on the plain reasons**, as ruled in msg 3434 (a). The DEMQUE request
  `AMGT_RESAPP-S14-CRNCY-SCANNER-US` is filed @b6e42f51a8.
- **Item 7 (mm-2 to PROD): PARKED at Andrew.** /prod-deploy ships all 46 DEV commits, including the partner-visible
  `/advisor-intelligence` fee panel, so the promote is client-facing (open call `dell1-20261011T033643Z-e7f2`).

**FWD state.** This round adds SERVED evidence to FWD-8 (the comparison block is about the company: peers resolve through the
identity pool) and to FWD-38 (one page agrees with itself: the subject cap now carries the header's vintage). Neither is
graded REALIZED on one round's cell checks. Each outcome is still owed a whole-page read. FWD-16 stays held by Andrew.

## 2. Rulings on the packet's section 5

- **D1-S14, identifier form for the 1,816 non-US scanner rows: they resolve through the identity pool, never by parsing the
  scanner's form.** Build ladder rung 2: nn-2 already resolves peers through the pool. A row the pool resolves gets its
  currency from the price source on its pool identity. A row the pool cannot resolve stays currency-ABSENT, with the reason
  named. No SEDOL, exchange-number or star-ticker parser is built.
- **nn-5 does not ship alone.** `write_pool` is a producer-CLI path. The served function reads; it never calls `write_pool`.
  `crosswalk.py` reaches the function only through the next redeploy that a product cell needs, admitted there by blob under
  that act's never-widen pair. No redeploy is cut for nn-5 alone.
- **`to_id` at the cut.** Every worker order declares its `<to_id>` in the issuance. This is the issuer's cut discipline. The
  tool mismatch behind it (`round-close-check.py` vs `to-pipeline-gate.py`) goes to the gate owner and is not a cell here.

## 3. ENRICHMENT LIST (round 90, ONE issuance by `2.0.0_SA_COO~R1`)

1. **D1-S14, US rows: serve the measured currency.** STAGED on the DEMQUE answer for `AMGT_RESAPP-S14-CRNCY-SCANNER-US`. That
   is a dependency between two projects, not a wait on time.
   - When the answer lands, each US peer with a DEMQUE currency serves it as MEASURED, replacing round 89's reasons.
   - Negative arm: a peer with no answer keeps its reason, and never a default currency.
2. **D1-S14, non-US rows: resolution through the identity pool (the section 2 ruling).** Risk LOCAL until it rides a redeploy.
   - The count of non-US scanner rows the pool resolves is printed against the 1,816.
   - Each unresolved row carries its reason.
3. **Z-W266-S3, a diagnosis read (an issuer read, or a LOCAL cell).** For BABA, PBR and SAP, classify each lost driver point
   as LOCATOR (the verifier fails to find a label or value that is in the excerpt) or EXCERPT (the value is not in the excerpt
   the verifier received), with the count per class.
   - A LOCATOR defect inside this project's write surface becomes a round-91 cell.
   - A defect in AMGT_FILINGS or the analyzer becomes a row on that project's surprise channel, not a cell here.
4. **`mass-deletion-check.sh` MERGE_HEAD in a linked worktree.** Risk LOCAL, one file, at most two criteria.
   - Resolve the path with `git rev-parse --git-path MERGE_HEAD` (build ladder rung 2: git's own resolver, the same family as
     nn-4's `--git-common-dir`), so that a merge commit in a linked worktree gets the merge exemption.
   - Negative arm: a non-merge mass deletion in the same worktree is still gated.
5. **Whole-page read for FWD-8 and FWD-38 (an issuer act, LOCAL read of the served plane).** On the live page for ASML and
   two other names:
   - every peer row's identity agrees with the header company's comparison basis;
   - every dated figure on the page carries a vintage within one trading day of the header's;
   - the denominators are printed.
   This is the read that lets a later round grade both outcomes.

## 4. ACTS ONLY ANDREW CAN DO (cited)

- Portal PROD promote of the 46 DEV commits (open call `dell1-20261011T033643Z-e7f2`; carries round-88 item 7).
- FWD-16: lifting his 2026-09-15 news hold.
- Rotating the model API key (unblock case 86a2).

-- 1.0.0_SA_CTO~DELL1
