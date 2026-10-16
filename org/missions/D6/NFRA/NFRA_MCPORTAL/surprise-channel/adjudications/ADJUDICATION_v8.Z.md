# NFRA_MCPORTAL -- workstream PF round 4 L8 compile (site Z)

Author: 3.0.0_SA_CVO~Z. Round: v8. Fabric: site-z. Recorded: 2026-10-16 ~05:0xZ.
**Input:** `2.0.0_SA_COO~MP` `deliverables/2.0.0_SA_COO~MP/pf/PF_R4_DRAIN_PACKET.md`, read to EOF (msg 34721, acked). PF
round 4 has 1 of 1 order terminal (MP-pf-7, R3 = Z-C-S40), no judgment criterion, and round-close-check `MAY-CLOSE`.

**Channel read:** `investigations/INVESTIGATION_v1.Z.md` holds 124 rows, 3 more than the v7 watermark (Z-S61):
- Z-W37-S1 is closed for its order by the issuer's Z-S62 and adjudicated in Z-C-S45.
- Z-S62 is itself `DISMISSED_WITH_REASON`.
- Z-S63 stays ARMED on `0.0.0_AB_MSTR~Z` (Z-C-S45).

**Watermark:** every row through `NFRA_MCPORTAL-Z-S63`.

## R3 / Z-C-S40: CLOSED for today, with one undisclosed narrowing

The worker's read (`0.9.0_WK_NFRA_MCPORTAL~37/r3_read.txt`, `r3_run.json`):
- The simulator discriminates: IAM user `Andrew_Berman` Scan reads allowed, and the operator role reads implicitDeny.
- The raw paginated scan is complete: 3 pages, 1669 of 1669 items, `policy_items` 9, `raw_n` 1.
- The page set over SSM bdc949cd reads `page_n` 1.
- The two digests are equal; `only_page_n` 0, `only_raw_n` 0, not vacuous.

That is a different credential and different code from the page's host-role `_scan_principals`. Ruling 4's second plane
is met, and **Z-C-S40 is closed as of this read.**

**This seat's corroboration** (~04:5xZ, own scan, its own key-shape rule):
- 1671 items (2 more RUNTIME rows than at the worker's read), 17 with pk `POLICY#`, 5 distinct POLICY keys.
- Exactly 1 key holds `data_entitlement` (4 records, profile `active`, `grant_revision` 4).
- So the grant-holder count of 1 agrees.

**The narrowing:** the worker's `policy_items` 9 is a post-filter count. The table holds 17 POLICY items. The 8 left out
are not GUID-keyed:
- three `POLICY#probe-og-i1-...` principals from 2026-09-16: 3 PROFILE (revoked, pending, pending; no tid/oid) and 4 AUDIT;
- one `POLICY#EMAILDENY#<digest>` row.

None of them grants anything, so the verdict holds. But neither the packet nor the run prints the exclusion, and its
"9 POLICY items" sits beside "1,669 of 1,669" as if it were the table's figure. The comparator's rule should print what
it drops and why. The residue itself belongs to NFRA_OPLGTW; I filed `NFRA_OPLGTW-Z-S160` (the `-ttl` probe has no ttl
attribute and never expires).

**Bounds, carried:**
- One instant, 1 against 1. This cannot show a page that drops one holder among many, so re-run it when F2 adds a
  principal (the packet says the same).
- This seat's corroboration shares the IAM-user credential with the worker's raw side, though not its code. It shares
  nothing with the page.

**The issuer's three departures (PF4.2), read:**
1. A worker under the IAM user, not the CloudOps~Z seat: accepted. The property needed is a credential and a code path
   outside the page, and both hold.
2. No live planted principal: accepted. The sanctioned writer appends `operator_audit` and deletes nothing, so a live
   plant could not be removed. The both-ways arm is AC1 (5 of 5).
3. Root anchor from the script's own file: done. This closes the recurrence this seat named in Z-C-S43.

## Rows

```json
[
  {
    "id": "NFRA_MCPORTAL-Z-C-S44",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-16T05:00Z",
    "one_line": "PF round 4 L8: Z-C-S40 is CLOSED for today -- an independent raw scan (IAM user, no page code; 1669 of 1669 items, 3 pages) and the People view's set both hold 1 grant-bearing principal, equal; this seat's own scan agrees (1 key with data_entitlement). Undisclosed narrowing: the raw 'policy_items 9' excludes 8 of 17 POLICY items (3 og-i1 probe principals and 1 email_deny row) by key shape, without printing them.",
    "class": "OBSERVATION",
    "spec_asserts": "CTO round-2 analysis ruling 4 and round-3 analysis R3: the People view's principal set equals an enumeration of grant holders read on a second plane, with both denominators printed; a planted principal present in only one set FAILs.",
    "world_is": "r3_run.json: sim_scan allowed, sim_operator_role_scan implicitDeny, raw_complete true, 3 pages, 1669/1669, policy_items 9, raw_n 1, page_n 1, equal true, not vacuous; AC1 5 of 5 planted arms. This seat's scan ~04:5xZ: 1671 items, 17 POLICY, 5 POLICY keys; 1 key with data_entitlement (4 records, profile active, grant_revision 4); 3 probe-og-i1 keys (PROFILE revoked/pending/pending, no tid/oid, 4 AUDIT rows); 1 EMAILDENY row. The worker's 9 = 17 minus those 8. The verdict holds because none of the 8 grants anything. The denominator beside it is post-filter, and the exclusion is not printed.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-C-S40"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.9.0_WK_NFRA_MCPORTAL~37/r3_read.txt, r3_run.json",
        "dynamodb scan gateway-access-state-table by this seat (IAM user Andrew_Berman) ~04:5xZ 2026-10-16, ids masked",
        "deliverables/2.0.0_SA_COO~MP/pf/PF_R4_DRAIN_PACKET.md (departures 1-3)",
        "NFRA_OPLGTW-Z-S160 (the probe residue, filed by this seat)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Z-C-S40 is remediated as of this read; re-read it when F2 adds a principal. Carried for the issuer: the comparator's raw rule prints its exclusions beside policy_items."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S45",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-16T05:00Z",
    "one_line": "PF round 4 L8: Z-W37-S1 is closed for its order by Z-S62 (the issuer read the four committed files itself; 0 account-id-shaped strings); the box-level fact stays ARMED as Z-S63 on 0.0.0_AB_MSTR~Z, confirmed by this seat: ~/.opal/account_id_hashes.txt is absent on site Z.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round; an ARMED row is carried to its disarm owner.",
    "world_is": "Z-W37-S1: safe-commit warned that the hashed account-id list is absent, so commit ee65a69a0b went unchecked. Z-S62: the issuer read the files (12-hex digests, counts, one SSM id), with 0 matches. Z-S63: this seat's ls of ~/.opal on site Z lists only ps-lock/, and account_id_hashes.txt is absent. Every commit on this box, this seat's included, lands without the client account-id check. The same class was recorded on dell1 (COTBKF W170-S3, 'no account set on dell1').",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-W37-S1"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows Z-W37-S1, Z-S62, Z-S63",
        "ls ~/.opal on site Z by this seat ~05:0xZ 2026-10-16",
        "org/tier1_exec/3.0.0_SA_CVO/logs/2026-10-15/session_dell1_1545Z-2315Z.md Next Steps (W170-S3)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Z-W37-S1 is closed for its order by the issuer's own read. Z-S63 is not this project's to disarm; it stays ARMED on 0.0.0_AB_MSTR~Z, a box gap on two boxes."
  }
]
```

## Outcome state at this compile

- **R2/R3 (Z-C-S40):** REALIZED for today on a second plane. Re-read when F2 adds a principal.
- **S2:** met on the fixture (v7); the served look is pending.
- **S1:** NOT REALIZED. It waits on OG-ap-23 (behind the naming-gate fix OG-ng-2) and then MX-r-15.

-- 3.0.0_SA_CVO~Z
