# SEAT BRIEF -- 2.0.0_SA_COO~T on NFRA_TRNSPT (D9, laptop)

**From:** 1.0.0_SA_CTO, 2026-09-30. **Andrew-direct** (verbatim): "I want COO~T spawned to get on the NFRA_TRNSPT work now." Spawned by `0.0.0_AB_MSTR`.
**Your one project:** NFRA_TRNSPT. Register row: `org/missions/D9/NFRA/NFRA_TRNSPT/project.json` (you are its `coo_lane`).

## Read, in this order
1. `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_NFRA_TRNSPT_20260930.md` (FWD-1..FWD-11, CONFIRMED by Andrew, record `6a861c4e18`).
2. `docs/briefs/nfra-trnspt-commentary-ingestion-expansion-brief-v3-20260930.md` (the CRO's consolidated brief) and the L1 brief `docs/briefs/nfra-trnspt-opal-transcript-database-brief-20260929.md`.
3. The PRD `org/missions/D9/NFRA/NFRA_TRNSPT/prd/NFRA_TRNSPT_PRD.md`: the CTO is writing it now (L4). Do not decompose against it until it exists, is committed, and `python .tools/prd-signoff.py status NFRA_TRNSPT` says what is owed.
4. The Andrew-direct records the briefs cite, all under `org/tier1_exec/{1.0.0_SA_CTO,4.0.0_SA_CRO}/deliverables/ANDREW_DIRECT_20260930_*`.

## Your work, in order (spine L5-L10; `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md`)
- L5 decomposition and battery, L6 ONE issuance, only after the PRD's two halves are signed. Round 1 is the THREAD: FWD-1 (a Monday meeting to the readable transcript, unattended) is the live journey end to end; decompose over its hops.
- Two workstreams, disjoint write surfaces (a workstream is a scope, not a round): **transcripts** (FWD-1..5) and **communications** (FWD-6..11). The CTO's suggested round-1 split for the communications side follows the CRO's v3 section 9: registry rows, bronze landing from Andrew's mailbox, silver with the PII wipe and its planted-token test as the gate, gold first run, the slicer over a replay.
- Not round 1: production sign-in identity, the PDF holdings parser, the Kimi serving Lambda and ticket write, the market-update backfill.

## Owned dependencies (not yours to build; name them in the decomposition)
NFRA_OPLGTW (site Z): attachment-download tool, filtered paged mail list, Cc returned. IRPT_BCKEND: the hook when a report is READY. D7 OPAL_TICKET_VNEXT (laptop): the analysis-request ticket type, a service identity, dropping the requester-cannot-claim block on all tickets, attachments. Ask the CTO to relay to site Z; you cannot message across fabrics.

## Standing rules that bite here
- Kimi K3 only, and only after the wipe test passes; a vendor call carries Andrew's word per use (his word for the first commentary call is in `ANDREW_DIRECT_20260930_03xxZ_TRNSPT_OPEN_CALLS_ANSWERED_...`).
- Every S3 address is `lib/opal_naming.py address()` output; `outlook` and `sharepoint` need registry rows first. No alert, SNS/SES send, freshness checker or monitor (standing moratorium).
- Bronze has two named readers only (Andrew and `opalbloomberg@opalinvest.com`). Test fetches use `andrew@opalinvest.com`, never Alyssa's mailbox.

## A seating fact to resolve early
The `~T` lane was earlier the issuer of MDPF_TAXSMA task orders (`MDPF_TAXSMA.TO-TX-c-2`, issued 2026-09-15, plus about 26 more from `2.0.0_SA_COO~T`). One project per Tier-2 seat instance is checked by `.tools/to-decomp-ref-lint.py`. Report to the CTO which of those orders are still non-terminal; the CTO tells Andrew and, if the lint refuses, seats a different lane letter on his word.
