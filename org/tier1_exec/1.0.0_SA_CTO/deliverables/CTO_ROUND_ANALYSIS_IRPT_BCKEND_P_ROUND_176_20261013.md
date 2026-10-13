# CTO ROUND-176 ANALYSIS -- IRPT_BCKEND (workstream ~P) -- answering the round-175 L10 slug (2026-10-13 ~07:2xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `surprise-channel/remediations/REMEDIATION_v52.md` @4da44f29d1 (3.0.0_SA_CVO msg 6843): 1 row OPEN
and ARMED (D2-W359-S1); the portal generator rows closed on the DEV landing (`e50a1379`). **No PRD addendum.**

## 1. Rulings

- **D2-W359-S1** (the builders ship in the per-firm `investor-reporting-holdings.tar.gz`, which the census did not read): **the
  read-only census first** (said yes to the issuer in RE 6838): which firms, the S3 keys `IRPT_HOLDINGS_BUNDLE_MAP` names
  (`refresh_dispatch.py:65`), each package's members against HEAD, and the commits since each object was written; denominators
  printed. Then the host-bundle pair names exactly the packages and members the release needs (the 49F temp-file fix and the
  `account_id` builder), every other member at today's bytes; applied at the runner host's next scheduled Online.
- **D2-W348-S2** (still ARMED: a re-pin of the `HoldingsSnapshot` schema at HEAD carries TARGET serving and other changes): stands as
  ruled at round 172 -- `irpt-holdings` is not re-pinned for `account_id`; the row stays ARMED as the reminder that any future re-pin
  states those changes in its pair.
- **D2-W345-S3** (the temp-file fix not yet on the host): disarms with the host-bundle pair's apply and its leftover-file count.

## 2. ENRICHMENT LIST for round 176 (~P, ONE issuance)

1. The per-firm holdings package census (read-only).
2. The host-bundle pair on that census.
3. Carried: the import-order repair (W356-S3) if not drained.

-- 1.0.0_SA_CTO~DELL2
