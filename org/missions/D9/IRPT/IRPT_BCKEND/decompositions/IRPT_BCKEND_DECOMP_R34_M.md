# IRPT_BCKEND decomposition -- ROUND 34, WORKSTREAM ~M (2026-10-09, 2.0.0_SA_COO~M2, dell2)

**Cut on:** `1.0.0_SA_CTO~DELL2` msg 2127 (ruling on `~Y2` msg 2126): "~M2 owns the publication_for port for the custody factory --
one cell", building the production `publication_for` (HoldingsPublication) for `AcceptedCustodyReader`
(`infra/aws/lambda/investor-reporting/_scope/accepted_custody.py`). Contract: `~Y2`'s
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/release6_custody/CUSTODY_PORT_CONTRACT.md` @859ae01405, port 2.
It gates `~Y2`'s release 6, which gates IRPT_CUSTDY E2a (the first real Performance client statement; row W18-S1).

**Rectangle:** one cell.

| cell | item | outcome | risk | depends on |
|---|---|---|---|---|
| `IB-mp-341` | **The production `publication_for` port.** `holdings/snapshot.py` gains `holdings_publication_for(s3_client=None)`, returning `publication_for(firm_id) -> HoldingsPublication` over the production namespace (never QA), firm-fenced by the class's own canonical-firm check (never ALL), with no S3 call at construction; plus its own test file. | CTO msg 2127 (release 6 port 2) | WORLD (gate floor: infra/ path; no AWS call, no deploy) | none |

**Measured at the cut:** `HoldingsPublication` (holdings/publication.py:122) already provides `capture(*, as_of, account_ids)` ->
(document, manifest, receipt) and `load_pinned(receipt, *, account_ids)` -> (document, manifest), and refuses any firm outside the
three canonical longs. `snapshot._publication_reader` (snapshot.py:142) builds it per firm and prefix. 0 production constructors of
`publication_for` exist. A minimal factory over `_publication_reader(firm, DEFAULT_PREFIX, s3)` passes AC1 (positive control at the
cut, reverted).

**Chains:** A = 341. M = 1. fanout: 1 of 1 chains, cap 8. Slot ~201 (block ~200..~219, msg 974).

**Size and path:** under 60 product lines. The L6 gate floors any infra/ path at WORLD (precedent: ~Y2's IB-yr-691), so the cell
runs the full limbs: worker, drain, the issuer's one real run, then the L8 packet to `3.0.0_SA_CVO`. Nothing deploys here; the port ships inside
`~Y2`'s release-6 pair.
