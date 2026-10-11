# AMGT_RESAPP -- round 89 L8/L9 adjudication, packet FINAL (dell1)

<sweep_watermark>2026-10-11T05:22Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T05:22:00Z. L8 packet: 2.0.0_SA_COO~R1 msg 3508,
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round89/DRAIN_END_PACKET.md @5976e6bfdc (blob 38b204fbe1, verified).
5 of 5 orders complete; nn-6 (mm-2 to PROD) PARKED at Andrew as an issuer act. No JUDGMENT criterion in the cells; the packet's two
L9 items are graded here on this seat's own runs: condition 4 EXERCISED (C-S44) and the nn-7 WORLD cell HOLDS (C-S45).
5 rows swept since v108 (watermark 2026-10-11T02:45Z; 5 of 1029 investigation rows surfaced after it): all 5 dismissed, the two
ARMED rows (W352-S1, W353-S1) disarmed on this seat's re-run. Nothing graduates; no REMEDIATION file this round. No BLOCKING or
ARMED row is open from this round.

**L9 -- condition 4: EXERCISED. nn-7: HOLDS.**

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S44",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:22:00Z",
    "one_line": "L9 item 1 (round-88 condition 4): EXERCISED. This seat re-ran r89_populated_selector.py against the package now LIVE (CodeSha256 l8egBo/rf.., LastModified 2026-10-11T04:56:11Z; reader scoped_amgt.py 377579 bytes, sha256 ee27bda3b1df7eaf), one package later than the issuer's nn-1 run on KlosR/ap8O3. Two firms planted non-empty (3 and 2 tickers): the off-list selector on all three channels (query selected_tenant, query selectedTenant, header x-selected-tenant) is byte-equal to the no-selector read, with no cross-firm ticker (S1-S3 PASS), and the drop-everything negative control fails S2 (S4 PASS); R89 POPULATED SELECTOR: YES, exit 0. Limit carried from the issuer's arm 2: the store is an in-memory copy driven through the deployed handler, and the deployed API Gateway/CloudFront router between the edge and the function was not read (terraform source 0 of 763, edge package 0 matches).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "L9 item 1 (round-88 condition 4): EXERCISED. This seat re-ran r89_populated_selector.py against the package now LIVE (CodeSha256 l8egBo/rf.., LastModified 2026-10-11T04:56:11Z; reader scoped_amgt.py 377579 bytes, sha256 ee27bda3b1df7eaf), one package later than the issuer's nn-1 run on KlosR/ap8O3. Two firms planted non-empty (3 and 2 tickers): the off-list selector on all three channels (query selected_tenant, query selectedTenant, header x-selected-tenant) is byte-equal to the no-selector read, with no cross-firm ticker (S1-S3 PASS), and the drop-everything negative control fails S2 (S4 PASS); R89 POPULATED SELECTOR: YES, exit 0. Limit carried from the issuer's arm 2: the store is an in-memory copy driven through the deployed handler, and the deployed API Gateway/CloudFront router between the edge and the function was not read (terraform source 0 of 763, edge package 0 matches).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO ran deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_populated_selector.py 2026-10-11T05:16Z: R89 POPULATED SELECTOR: YES, exit=0",
        "round89_prep/NN1_POPULATED_RUN_20261011.txt @fc54cef755 (issuer, against KlosR/ap8O3)",
        "3.0.0_SA_CVO aws lambda get-function-configuration opal-amgt-scoped-api 2026-10-11T05:15:51Z: l8egBo/rfEH4ddCEFyWnUOb9BvN3bGu/azarul5Ho0g=, Active, Successful"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "L9 item 1 (round-88 condition 4): EXERCISED. This seat re-ran r89_populated_selector.py against the package now LIVE (CodeSha256 l8egBo/rf.., LastModified 2026-10-11T04:56:11Z; reader scoped_amgt.py 377579 bytes, sha256 ee27bda3b1df7eaf), one package later than the issuer's nn-1 run on KlosR/ap8O3. Two firms planted non-empty (3 and 2 tickers): the off-list selector on all three channels (query selected_tenant, query selectedTenant, header x-selected-tenant) is byte-equal to the no-selector read, with no cross-firm ticker (S1-S3 PASS), and the drop-everything negative control fails S2 (S4 PASS); R89 POPULATED SELECTOR: YES, exit 0. Limit carried from the issuer's arm 2: the store is an in-memory copy driven through the deployed handler, and the deployed API Gateway/CloudFront router between the edge and the function was not read (terraform source 0 of 763, edge package 0 matches)."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S45",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:22:00Z",
    "one_line": "L9 item 2 (nn-7, risk WORLD): HOLDS on this seat's own re-run against the live function l8egBo/rf.. (LastModified 2026-10-11T04:56:11Z, Active, Successful; differs from KlosR). AC1 in the pin worktree C:/tmp/nn7a-build (HEAD a943b1b412): scoped_amgt.py, listed_identity.py and subject_cap.py each present in the 407-member package and byte-equal to the pin (K1, K2 PASS x3; R88 PACKAGE: YES x3). AC2 r89_peers_deployed.sh: I1 7 of 7 resolvable US members MEASURED, I2 leaked [], I3; served cap 621657.438 @ 2026-10-10T13:01:55Z equals the current model block (stored 541931.78 @ 2026-09-19); R89 PEERS DEPLOYED: YES, exit 0. AC3 r89_deployed_close.sh --want amgt-corpus-dossier/11: P1, P2, W1, W2 (5 of 5), R3 (3 of 3 byte-equal to base); R89 DEPLOYED CLOSE: YES, exit 0. The LOCAL cells re-run at box/dell1 HEAD e8145043c7: nn-2 I1-I3, nn-3 C1-C3, nn-4 A1-A4, nn-5 G1-G4 all PASS; lib/research/identity/tests 273 passed. round-close-check --round 89: 5 of 5 complete, proof_ok 5, judgment 0, MAY-CLOSE.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "L9 item 2 (nn-7, risk WORLD): HOLDS on this seat's own re-run against the live function l8egBo/rf.. (LastModified 2026-10-11T04:56:11Z, Active, Successful; differs from KlosR). AC1 in the pin worktree C:/tmp/nn7a-build (HEAD a943b1b412): scoped_amgt.py, listed_identity.py and subject_cap.py each present in the 407-member package and byte-equal to the pin (K1, K2 PASS x3; R88 PACKAGE: YES x3). AC2 r89_peers_deployed.sh: I1 7 of 7 resolvable US members MEASURED, I2 leaked [], I3; served cap 621657.438 @ 2026-10-10T13:01:55Z equals the current model block (stored 541931.78 @ 2026-09-19); R89 PEERS DEPLOYED: YES, exit 0. AC3 r89_deployed_close.sh --want amgt-corpus-dossier/11: P1, P2, W1, W2 (5 of 5), R3 (3 of 3 byte-equal to base); R89 DEPLOYED CLOSE: YES, exit 0. The LOCAL cells re-run at box/dell1 HEAD e8145043c7: nn-2 I1-I3, nn-3 C1-C3, nn-4 A1-A4, nn-5 G1-G4 all PASS; lib/research/identity/tests 273 passed. round-close-check --round 89: 5 of 5 complete, proof_ok 5, judgment 0, MAY-CLOSE.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO ran round88_prep/checks/r88_package.py --member x3 --ref HEAD in C:/tmp/nn7a-build @a943b1b412: R88 PACKAGE: YES x3",
        "3.0.0_SA_CVO ran deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_peers_deployed.sh: R89 PEERS DEPLOYED: YES, exit=0",
        "3.0.0_SA_CVO ran deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_deployed_close.sh --want amgt-corpus-dossier/11: R89 DEPLOYED CLOSE: YES, exit=0",
        "3.0.0_SA_CVO ran r89_peer_identity.py --where local, r89_subject_cap.py --where local, r89_audit_root.sh, r89_write_pool_guard.py at e8145043c7: YES x4",
        "3.0.0_SA_CVO python .tools/round-close-check.py --project AMGT_RESAPP --round 89: verdict=MAY-CLOSE"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "L9 item 2 (nn-7, risk WORLD): HOLDS on this seat's own re-run against the live function l8egBo/rf.. (LastModified 2026-10-11T04:56:11Z, Active, Successful; differs from KlosR). AC1 in the pin worktree C:/tmp/nn7a-build (HEAD a943b1b412): scoped_amgt.py, listed_identity.py and subject_cap.py each present in the 407-member package and byte-equal to the pin (K1, K2 PASS x3; R88 PACKAGE: YES x3). AC2 r89_peers_deployed.sh: I1 7 of 7 resolvable US members MEASURED, I2 leaked [], I3; served cap 621657.438 @ 2026-10-10T13:01:55Z equals the current model block (stored 541931.78 @ 2026-09-19); R89 PEERS DEPLOYED: YES, exit 0. AC3 r89_deployed_close.sh --want amgt-corpus-dossier/11: P1, P2, W1, W2 (5 of 5), R3 (3 of 3 byte-equal to base); R89 DEPLOYED CLOSE: YES, exit 0. The LOCAL cells re-run at box/dell1 HEAD e8145043c7: nn-2 I1-I3, nn-3 C1-C3, nn-4 A1-A4, nn-5 G1-G4 all PASS; lib/research/identity/tests 273 passed. round-close-check --round 89: 5 of 5 complete, proof_ok 5, judgment 0, MAY-CLOSE."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S46",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:22:00Z",
    "one_line": "D1-W351-S1 dismissed: the issuer's ruling stands (a derivation that raises on a read block is served UNREADABLE, never a 500); this seat's nn-3 C3 run shows the unreadable-block arm serves the stored cap unchanged and says why in cap_refresh.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W351-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W351-S1 dismissed: the issuer's ruling stands (a derivation that raises on a read block is served UNREADABLE, never a 500); this seat's nn-3 C3 run shows the unreadable-block arm serves the stored cap unchanged and says why in cap_refresh.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row AMGT_RESAPP-D1-W351-S1",
        "AMGT-nn-3 status line",
        "3.0.0_SA_CVO r89_subject_cap.py --where local: PASS C3"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W351-S1 dismissed: the issuer's ruling stands (a derivation that raises on a read block is served UNREADABLE, never a 500); this seat's nn-3 C3 run shows the unreadable-block arm serves the stored cap unchanged and says why in cap_refresh."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S47",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:22:00Z",
    "one_line": "D1-W352-S1 (ARMED) dismissed, disarmed: AMENDMENT 1 to nn-4 added the .git-entry guard and checker arm A4; this seat's run of r89_audit_root.sh reads A4 PASS (a submodule commit's row lands in a worktree, never under <super>/.git/modules), with A1-A3 PASS. Residual, as the worker stated: whether the hook fires inside a real submodule commit is not measured; A4 measures where the row lands.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W352-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W352-S1 (ARMED) dismissed, disarmed: AMENDMENT 1 to nn-4 added the .git-entry guard and checker arm A4; this seat's run of r89_audit_root.sh reads A4 PASS (a submodule commit's row lands in a worktree, never under <super>/.git/modules), with A1-A3 PASS. Residual, as the worker stated: whether the hook fires inside a real submodule commit is not measured; A4 measures where the row lands.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row AMGT_RESAPP-D1-W352-S1 (disarm_owner 2.0.0_SA_COO~R1)",
        "AMGT-nn-4 AMENDMENT 1",
        "3.0.0_SA_CVO ran deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_audit_root.sh: PASS A1-A4, R89 AUDIT ROOT: YES"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W352-S1 (ARMED) dismissed, disarmed: AMENDMENT 1 to nn-4 added the .git-entry guard and checker arm A4; this seat's run of r89_audit_root.sh reads A4 PASS (a submodule commit's row lands in a worktree, never under <super>/.git/modules), with A1-A3 PASS. Residual, as the worker stated: whether the hook fires inside a real submodule commit is not measured; A4 measures where the row lands."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S48",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:22:00Z",
    "one_line": "D1-W353-S1 (BLOCKING, ARMED) dismissed, disarmed: AMENDMENT 1 to nn-5 (@f97a368f0a) added test_writers_carry_issuer.py to <paths> and repointed its three patches; this seat reads 0 occurrences of add_security._research_folders_disclosure in that file and in lib/research/identity/*.py, and lib/research/identity/tests reads 273 passed, 0 failed at e8145043c7.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W353-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W353-S1 (BLOCKING, ARMED) dismissed, disarmed: AMENDMENT 1 to nn-5 (@f97a368f0a) added test_writers_carry_issuer.py to <paths> and repointed its three patches; this seat reads 0 occurrences of add_security._research_folders_disclosure in that file and in lib/research/identity/*.py, and lib/research/identity/tests reads 273 passed, 0 failed at e8145043c7.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row AMGT_RESAPP-D1-W353-S1 (disarm_owner 2.0.0_SA_COO~R1)",
        "commit f97a368f0a",
        "3.0.0_SA_CVO pytest -q lib/research/identity/tests: 273 passed"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W353-S1 (BLOCKING, ARMED) dismissed, disarmed: AMENDMENT 1 to nn-5 (@f97a368f0a) added test_writers_carry_issuer.py to <paths> and repointed its three patches; this seat reads 0 occurrences of add_security._research_folders_disclosure in that file and in lib/research/identity/*.py, and lib/research/identity/tests reads 273 passed, 0 failed at e8145043c7."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S49",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:22:00Z",
    "one_line": "D1-W353-S2 dismissed: the issuer's ruling stands; door A of the guard check reads the real opal-data-harvest bucket by GET only, the put side is faked, and this seat's G1-G4 run wrote nothing served.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W353-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W353-S2 dismissed: the issuer's ruling stands; door A of the guard check reads the real opal-data-harvest bucket by GET only, the put side is faked, and this seat's G1-G4 run wrote nothing served.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row AMGT_RESAPP-D1-W353-S2",
        "AMGT-nn-5 status line",
        "3.0.0_SA_CVO r89_write_pool_guard.py: G1-G4 PASS"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W353-S2 dismissed: the issuer's ruling stands; door A of the guard check reads the real opal-data-harvest bucket by GET only, the put side is faked, and this seat's G1-G4 run wrote nothing served."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S50",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:22:00Z",
    "one_line": "D1-W353-S3 dismissed: the issuer's ruling stands under the CTO's device-independent rule; the one-direction disagreement (a non-absent library failure reaches write_pool, which raises ValueError uncaught by main) is strictly safer, since no put happens, and differs from main's REFUSED exit 2 only in text and exit form.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W353-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W353-S3 dismissed: the issuer's ruling stands under the CTO's device-independent rule; the one-direction disagreement (a non-absent library failure reaches write_pool, which raises ValueError uncaught by main) is strictly safer, since no put happens, and differs from main's REFUSED exit 2 only in text and exit form.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row AMGT_RESAPP-D1-W353-S3",
        "AMGT-nn-5 status line",
        "3.0.0_SA_CVO r89_write_pool_guard.py: G2 PASS (no put on absent document)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W353-S3 dismissed: the issuer's ruling stands under the CTO's device-independent rule; the one-direction disagreement (a non-absent library failure reaches write_pool, which raises ValueError uncaught by main) is strictly safer, since no put happens, and differs from main's REFUSED exit 2 only in text and exit form."
  }
]
```
