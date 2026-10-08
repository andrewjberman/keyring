# IRPT_BCKEND -- project sweep 16 remediations

<sweep_watermark>2026-10-08T02:21Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-08 ~02:4xZ. Graduated at sweep 16 (ADJUDICATION_v33.md), round label v75. 8 rows.

```json
[
  {
    "id": "IRPT_BCKEND-W145-S2",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "receipt.build refuses a receipt with no covered account; the release had to carry the finalize wiring (finalize_on_read passes pending account_ids, handler.finalize_export passes them to receipt.build) or every retained export would fail at finalize.",
    "evidence": [
      "investigation row IRPT_BCKEND-W145-S2",
      "ADJUDICATION_v30.md (this seat's live read of the irpt-export-render zip, 2026-10-07T14:38:36Z)",
      "export/finalize_on_read.py:98 and export/handler.py:327-328 at HEAD (this compile's read, dell2 CLOUD HEAD, 2026-10-08 ~02:3xZ)"
    ],
    "remedy": "Wiring is in source and in the live zip; the disarm owner records the disarm on that read.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v75",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v75"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~P2",
      "at": "2026-10-08T08:53:07Z"
    }
  },
  {
    "id": "IRPT_BCKEND-S369",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Four bun test runs on dell2 used plain `bun test` (without --no-install) before the bun egress hazard was known; each ran from a worktree whose node_modules was a junction to a populated tree, so no fetch is expected, but none was measured.",
    "evidence": [
      "investigation row IRPT_BCKEND-S369",
      "CTO msg 501 (bun egress hazard)"
    ],
    "remedy": "Every face and check runs bun --no-install from round 66; the four earlier runs stay recorded as unmeasured.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v75",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v75"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-S382",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "IB-pr-349's after-reads 4-5 (a new export reaching READY, and its irpt_export_read_admitted line) cannot be exercised inside any order's grant: minting an Opal principal is a write to the production auth plane. Ruled OPEN-BY-DESIGN (row S386).",
    "evidence": [
      "investigation row IRPT_BCKEND-S382",
      "investigation row IRPT_BCKEND-S386",
      "IB-pr-349 AMENDMENT 1 @b883510cd9"
    ],
    "remedy": "The issuer records the first real Opal export's READY and its admitted-read line; that record closes this row.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v75",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v75"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W152-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "uploads.py admits an internal principal whose allowedFirmIds names the owner firm, but the production principal did not carry allowedFirmIds, so the admit was unreachable.",
    "evidence": [
      "investigation row IRPT_BCKEND-W152-S1",
      "IB-pr-354 (InteractiveAccess carries allowedFirmIds)",
      "IB-pr-358 (the upload door passes the profile reader)",
      "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_72_P_DRAIN_END_20261007.md @72208311d5"
    ],
    "remedy": "Fixed in source; closes when release 2 (X-1) ships these files and the admit is read on the deployed bytes.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v75",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v75"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W163-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "InteractiveAccess carried allowedFirmIds only from an injected profile reader that no production constructor passed.",
    "evidence": [
      "investigation row IRPT_BCKEND-W163-S1",
      "IB-pr-358: compose_upload passes CanonicalProfileReaders.get_user, memoized once per request",
      "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_72_P_DRAIN_END_20261007.md @72208311d5"
    ],
    "remedy": "Fixed in source; closes with W152-S1 when release 2 ships.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v75",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v75"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W162-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The print page could not mount the custody template: no route read the household document and the bundle carried only its reference.",
    "evidence": [
      "investigation row IRPT_BCKEND-W162-S1",
      "IB-pr-355 (read route), IB-pr-356 (page reads and mounts), IB-pr-359 (validateCustodyReport)",
      "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_72_P_DRAIN_END_20261007.md @72208311d5",
      "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_73_P_DRAIN_END_20261008.md @dc4d808a74"
    ],
    "remedy": "Fixed in source; closes when the custody route releases under its own pair and the portal candidate (wk-IRPT_BCKEND-167-portal @63b9382a) lands on DEV.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v75",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v75"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W165-S2",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The full portal bun suite regenerated 27 tracked contracts/wire/*.ts files, so a worker running it before tsc read a false FAIL or could stage the regenerated files.",
    "evidence": [
      "investigation row IRPT_BCKEND-W165-S2",
      "IB-pr-359: gen-wire.ts generate() takes an out directory and the test writes to os.tmpdir(); 0 tracked files written (IB73-1-AC1)",
      "portal 63b9382a on wk-IRPT_BCKEND-167-portal only, not on DEV (this compile's read, dell2 CLOUD HEAD, 2026-10-08 ~02:3xZ)"
    ],
    "remedy": "Fixed on the portal branch; the disarm owner disarms when it is on DEV, where workers branch from.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v75",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v75"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~P2",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-S388",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Regenerating the portal wire types yields 4 files that differ from the committed contracts/wire copies (AnalysisReport-related), measured at b3fedfea before round 73 and hidden while generate() crashed.",
    "evidence": [
      "investigation row IRPT_BCKEND-S388",
      "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_73_P_DRAIN_END_20261008.md @dc4d808a74"
    ],
    "remedy": "A cell traces which side moved (the schemas or the committed types) and brings them back into agreement, with the generator test as the check.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v75",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v75"
    },
    "closed": false
  }
]
```
