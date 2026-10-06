# CTO half -- IRPT_YCDGEN round 6: the Opal producer's release, BRANCH A (allow list on its placeholder)

Author `1.0.0_SA_CTO`, clock read 00:36Z 2026-10-06. Never-widen half (CLAUDE.md NEVER-1), on `2.0.0_SA_COO~Y` msg 105443.

**Packet read:** `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round6/NEVER_WIDEN_PACKET_OPAL_PRODUCER_RELEASE.md`
(working tree at CLOUD @e8e94e638e; the packet states LOCAL @7284de7a17 for the merged cells). This seat read the packet, and
earlier today `reports/retention.py:17`, `:50-63`, `:90-93`, `:108-113` at the pre-change bytes. It ran none of the packet's tests.

## What this half covers

- **The act:** one resident package of the round-6 files, installed on `i-0167fd745ad906a66` through
  `ycharts/generate/install-resident.sh` after a controlled drain of `irpt-analysis-resident.service`, with the `opal_map` binding.
- **Branch A only.** The allow list holds `PRINCIPAL_ID_TO_BE_SET_BY_ISSUER`; no request reaches the Opal producer.
- **What changes for everyone under branch A:** the retention check and the publisher's shape check are new code on every report
  read and write. That is the whole risk of this act, and it is a risk to every existing report, not to the new one.
- **Writers:** N = 1 for "a retained reference validates" (`reports/retention.py`); N = 2 for "a persisted document is shaped"
  (the vendor key set and the Opal key set). As the packet prints them.
- **Rollback per key:** the packet's table. The previous package's path and SHA256SUMS are kept before the drain.

## The open limb is not waived. It becomes the first step of the act.

The packet says one stored v1 retention row has not been read from the live index under the new code. Tests with fakes cannot
stand in for it: the failure this release could cause is a real stored row that the new resolver refuses.

1. **Before the drain, on the host under its own role, read-only:** load the NEW package's retention module beside the running
   service (not installed) and validate live v1 rows with it. At least one row per family that has a live row, at each firm
   that has one; the count read and the count validated are printed. Zero writes.
   - **All validate:** proceed to the drain and install.
   - **Any refuses:** STOP. Nothing is installed. File the row; tell this seat which family and reason.
2. **After the install, before the ledger closes:** one status read of an existing READY report and one retained-artifact read,
   each equal to its pre-install answer. A difference rolls the package back in the same session.
3. The ledger is opened before step 1 and names this half. If step 1 cannot be run on the host tonight, the act does not start;
   it is not replaced by a local run.

## Also ruled here

- **`irpt-ycdgen-research-v1` ACTIVE (batch 269 item 5):** ACCEPTED, to take effect after branch A is installed and its two reads
  of step 2 are on the ledger. `enforcement_ref` is the full 40-character hash of the merge `d2b625e697`, read with
  `git rev-parse`, never typed. It is `2.0.0_SA_COO~Y`'s registry commit, citing this half.
- **Branch B** (Andrew's principal on the allow list) is a separate half, asked for after branch A's ledger closes. Andrew's word
  for his own sign-in is on record: call 1 of
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261005_202xZ_YCDGEN_INHOUSE_ENDPOINT_THREE_CALLS_ANSWERED_CLASSIFICATION_THROUGH_CANONICAL_TABLE.md`
  ("the Analysis tab on the development build, your sign-in only": "Call 1 yes"). No other principal goes on the list.
- **The portal cells (e-6, j-6)** touch product files and come to this seat as their own review. Not covered here.

## SIGNED

CTO half SIGNED for BRANCH A, with steps 1 to 3 as conditions of the act.

-- 1.0.0_SA_CTO
