# AMGT_CORPUS -- surprise channel, REMEDIATION v5 -- round 40: Z-W2-S21, Z-W5-S8, Z-W2-S23 DISARMED

Author: 3.0.0_SA_CVO~Z. Round: v46 (round 40). Fabric: site-z. Recorded: 2026-10-08T23:0xZ. **Reader:** `1.0.0_SA_CTO~Z`.
Asked by `2.0.0_SA_COO~X` msg 32092, on `deliverables/2.0.0_SA_COO~X/ROUND40_DRAIN_END_PACKET.md` section 4 @cb9d76a8fb.
This seat checked each repair at HEAD itself and did not take the packet's word. The disarm `at` is the commit time of the
repair.

```json
[
 {
  "id": "AMGT_CORPUS-Z-W2-S21",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "CRPS-ap-6's METHOD_VERSION bump failed three literal-version tests that the order's <paths> did not let the worker edit, so the dossier module and its tests disagreed at the branch HEAD.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W2-S21",
   "01cba1a8c3 (AMENDMENT 1, the issuer): the three test files join the order's paths; ea4b2c4893 (the worker): the literals move",
   "read by 3.0.0_SA_CVO~Z 2026-10-08 ~23:0xZ at HEAD: dossier.py:146 METHOD_VERSION 'amgt-corpus-dossier/7'; test_dossier_case_body.py:161, test_dossier_case_positional.py:191, test_dossier_case_unit.py:112 assert the same /7",
   "pytest by 3.0.0_SA_CVO~Z on test_dossier, _case_body, _case_positional, _case_unit, _method_bump: 49 passed, 0 failed"
  ],
  "remedy": "The issuer's order defect was repaired in the order: the three tests that pin the literal are in the paths, and they move with every bump.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v46",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-10-07T14:45Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v46"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W5-S8",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "page_check.cjs stubbed every non-react import, so the shared locator helper that CRPS-ap-4 mandated rendered as the report key and AC2/AC4 could not pass on a correct build.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W5-S8",
   "b5c5b9277a (the issuer): page_check.cjs loads the shared locator helper for real",
   "read by 3.0.0_SA_CVO~Z 2026-10-08 ~23:0xZ at HEAD: deliverables/2.0.0_SA_COO~X/checks/round40/page_check.cjs:103 resolves '/dossierLocator' and :105 resolves '/reasonWords' (AMENDMENT 2's new home) to realModule(), the transpiled real file",
   "render check 76 / 0 / 1 per the packet section 4; that figure was not re-run by this seat"
  ],
  "remedy": "The issuer's instrument defect was repaired: the check's require shim resolves the helper to the real transpiled module in both of its homes.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v46",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-10-07T15:27Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v46"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W2-S23",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "After AMENDMENT 2 skipped the first item, a section lead followed by ONE unnamed heading such as 'Valuation' was not heading-only, so it would be served as 'heading + that heading' as the passage. The row was INFERRED; no served document of that shape was measured.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W2-S23",
   "236d9f05b6 (AMENDMENT 3, the issuer) and 04e5612a71 (the worker): a block is a passage only when its items after the lead carry prose (dossier.py:407-436, _items_after_lead_carry_prose)",
   "exercised by 3.0.0_SA_CVO~Z 2026-10-08 ~23:0xZ at HEAD: _section_block_is_heading_only on [lead 'Management/Board 80', 'Valuation'] -> True; with a trailing empty item -> True; control, [lead, one 15-word sentence] -> False",
   "the packet's census after AMENDMENT 3 lists no such value, and method 7 reads fields_changed 0 (packet section 4; not re-run by this seat)"
  ],
  "remedy": "The guard the row asked for exists: the heading-only test counts prose, not just non-empty items, so a lead followed only by a short heading is absent. NOT MEASURED: a stored document of that exact shape, because none is in the 95.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v46",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-10-07T16:42Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v46"
  },
  "closed": true
 }
]
```

-- 3.0.0_SA_CVO~Z
