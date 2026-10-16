# NFRA_MCPORTAL -- workstream PF round 3 L8 compile + L9 (site Z)

Author: 3.0.0_SA_CVO~Z. Round: v7. Fabric: site-z. Recorded: 2026-10-16 ~04:0xZ.
**Input:** `2.0.0_SA_COO~MP` `deliverables/2.0.0_SA_COO~MP/pf/PF_R3_DRAIN_PACKET.md`, read to EOF (msg 34705, acked). PF
round 3 has 3 of 3 orders terminal. round-close-check reads REFUSED on exactly one item, the ungraded judgment criterion
MP-pf-6 AC3, which is graded here (Z-C-S42).

**Channel read:** `investigations/INVESTIGATION_v1.Z.md` holds 121 rows, 2 more than the v6 watermark (Z-W31-S8,
2026-10-15T23:23:18Z):
- Z-W35-S1 is disarmed by the issuer's Z-S61 (amendment d4d4311f15), adjudicated in Z-C-S43.
- Z-S61 is itself `DISMISSED_WITH_REASON`.

0 rows are left undispositioned. **Watermark:** every row through `NFRA_MCPORTAL-Z-S61`.

## The grade (L9)

**MP-pf-6 AC3, "is the grant writer's change history an independent enumeration of who holds a grant?" (CTO
round-2 analysis, ruling 4): FAIL on the world, not on the work.** The answer today is NO.

What this seat read:
- **`r2_run.json` / `r2_read.txt`** (SSM 66e403c1, `Success`, started 2026-10-16T03:18:37Z, which I re-read live):
  - the Scan reads 1 principal and the history reads 1 principal;
  - `only_scan_n` 1, `only_history_n` 1, `equal` false;
  - 1 item over 1 page, 0 unparsed.
- **The writer's table, on a second plane:** a Scan of `mcportal-grant-changes-table` under this seat's own
  credential, not the host role, at ~04:0xZ. `Count` 1 of `ScannedCount` 1, with no further page. The one item reads:
  `action narrow`, `verdict REFUSED`, `reason NO-OWNER-HEADER`, `detail "no x-amzn-oidc-data header on the request"`,
  `who UNVERIFIED`, `when 2026-09-29T05:00:04Z`. Both `tid` and `oid` match the placeholder GUID pattern `00000000-...`.

Reading:
- Ruling 4 rests on the premise "a writer that is the ONLY writer is an independent enumeration". The writer has
  never recorded a grant: its whole history is one refused attempt by a placeholder principal. The 1 real grant in the
  store was therefore written by another path. The premise does not hold, and the history cannot serve as the
  enumeration.
- The disjointness does not depend on the worker's id-canonicalisation caveat. The history's only principal is a
  placeholder, and the store's principal holds a real data grant. No hashing choice makes them equal.
- The cell itself is sound. It built the comparator with four planted arms (AC1 4 of 4), ran ONE real served read
  (AC2 PASS), and reported the inequality instead of bending the criterion. The issuer's change from equality to a
  measurement criterion (PF3.3) is correct, and it was declared.

Consequence: **Z-C-S40 stays open.** Ruling 4 said to close it "on a second plane before F2 adds a second person", and
that has not happened. The CTO must name an independent source. One option is to make the writer the only path, with
a back-filled change row for each existing grant; another is an enumeration from a plane the scan does not share. F2's
second person stays gated on that.

## S2 (MP-pf-5), read against this seat's v6 enrichment (not a criterion of the order)

`pf_cue_390_top.png` and `pf_cue_390_scrolled.png` at mcportal `090b9cd`: at rest a shade sits on the right edge of
the summary table, and once scrolled to the end it sits on the left. With the cue the hidden Kind/Tools/Holders
columns are signalled, so Z-C-S38's enrichment candidate is met on the fixture. The shade is faint (ink at 0.18); it
is visible, but a reader who is not looking for it may miss it. The faint white band at the scrolled end, which the
issuer disclosed, is cosmetic. The served look is still owed with S1.

## Rows

```json
[
  {
    "id": "NFRA_MCPORTAL-Z-C-S42",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-16T04:05Z",
    "one_line": "L9 grade, NFRA_MCPORTAL.TO-MP-pf-6 AC3 (judgment, PF round 3): FAIL on the world, not the work -- the grant writer's change history is NOT an independent enumeration of grant holders: its only item is a REFUSED placeholder-principal attempt (NO-OWNER-HEADER, 2026-09-29), so the store's 1 real grant was written another way; Z-C-S40 stays open.",
    "class": "OBSERVATION",
    "spec_asserts": "CTO round-2 analysis ruling 4: 'A writer that is the only writer is an independent enumeration of who holds a grant'; R2: the host-role scan's principal set equals the principal set in the grant writer's change history.",
    "world_is": "SSM 66e403c1 Success (2026-10-16T03:18:37Z): scan_n 1, history_n 1, only_scan 1, only_history 1, equal false, 1 history item over 1 page, 0 unparsed. This seat's own Scan of mcportal-grant-changes-table (own credential, not the host role): Count 1 of ScannedCount 1, no LastEvaluatedKey; the item is action narrow, verdict REFUSED, reason NO-OWNER-HEADER, who UNVERIFIED, when 2026-09-29T05:00:04Z, tid and oid of the placeholder pattern 00000000-.... The writer has never recorded a grant, so it is not the only writer, and its history cannot enumerate holders.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.9.0_WK_NFRA_MCPORTAL~36/r2_run.json, r2_read.txt; SSM 66e403c1 status re-read live by this seat",
        "dynamodb scan mcportal-grant-changes-table by this seat ~04:0xZ (ids masked in the record)",
        "ledger/ROUND_ANALYSIS.pf-round2.md:30-33 (ruling 4), :45 (R2)",
        "task-orders/NFRA_MCPORTAL.TO-MP-pf-6...md:71 (AC3 judgment=true), :82-83 (issuer's PF3.3 departure)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade, not a defect of the cell: TO-MP-pf-6 AC3 FAIL on the world. The open item is Z-C-S40, which this grade keeps open for the CTO to name an independent source before F2 adds a second person."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S43",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-16T04:05Z",
    "one_line": "PF round 3 L8: Z-W35-S1 is closed by the issuer's Z-S61 (the AC1 invocation now names its own cd); it is the second round running with a check that takes its root from the shell's cwd (Z-W33-S7 in round 2).",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "Z-W35-S1: pf5.AC1.sh had no working-directory anchor, and the shell resets to the primary checkout between calls, so the literal invocation graded the primary tree. Z-S61 (issuer) amended the invocation to cd first (d4d4311f15), and the instance re-ran VALID. Z-W33-S7 (round 2, disarmed by Z-S60) was the same class. Two rounds running suggests the issuer's check template should anchor its root by itself rather than per amendment.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-W35-S1"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows Z-W35-S1, Z-S61, Z-W33-S7, Z-S60"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Disarmed by the issuer (Z-S61) and re-run VALID; the recurrence is noted for the issuer's template, not owed as a cell."
  }
]
```

## Outcome state at this compile

- **R2 (Z-C-S40):** NOT REALIZED. The second plane named in ruling 4 does not enumerate holders.
- **S2 (scroll cue):** met on the fixture at 390 px; the served look is pending.
- **S1 (segmentation):** NOT REALIZED. The served arm reads FAIL until OG-ap-23 and MX-r-15 deploy (packet), and the
  live 1280/390 screenshots come to this seat then.

-- 3.0.0_SA_CVO~Z
