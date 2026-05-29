# ws-charter cycle — 2026-05-29 2108Z

**archetype:** SCRIBE
**secondary_archetypes:** COORDINATE

**CLASS:** NOVEL (Andrew-direct sales-enablement deliverable + F4b flex-fix)

## Inbox / direction (window since 2023/2036Z ticks)
- ANDREW_DIRECTION: (1) write a sales case-study brief on Chris Surrichio walking the full enrichment process; (2) generate a prospect-dossier IMAGE with all company+person info, to desktop.
- DRIVE (COO): F4b acceptance-flex on AC-F4b.2 (cross-tie invalid) — concurred, PRD fixed.

## Actions
1. **Chris Surrichio case-study brief** (committed 3f60f6ac7): docs/briefs/find-insure-case-study-chris-surrichio-20260529.md — sales walkthrough of web-scrape→Lusha→Bright Data→FINRA→SEC process. Lincoln Investment #2/24 post-licensing (0.79), ~$22B reg AUM (~$60B client assets), SEC RIA + FINRA BD; Chris = CFA charterholder, CRD 2473601, Series 7/24(principal)/6/6TO/87/SIE, direct contact verified.
2. **Prospect-dossier PNG** rendered to C:\Users\AndrewBerman\Desktop\Chris_Surrichio_Prospect_Dossier.png (HTML→python-playwright @2x full-page). One-page card: company panel + person panel + 6-step process strip with free/paid tags. Verified visually. (Desktop deliverable; not repo-committed.)
3. **F4b PRD flex-fix** (committed 8a5b87d29): retired AC-F4b.2 cross-tie per DS~B empirical (nmec_nmnc_nna.json is single-day snapshot, different NNA computation than canonical window-sum = apples-to-oranges); AC-F4b.1 intra-artifact closure ($0.00 all advisors×windows) is the rigorous invariant. F4b accepted on AC1+AC3.

## Project-state sweep
- FIND_INSURE active: enrichment arsenal complete (FINRA re-rank live, secadv AUM, NERG architecture saved 46aea4f08); DS~C Prudent Man deep-drill + BrokerCheck-with-aliases in flight; case study delivered.
- ADVI_INFMVP active: F4b shipped+accepted (f5ac50af1); still Andrew-smoke-gated for close.
- MDPF_SCOPED active (reopened): FE remediation — DE on D3-unblock (cf558a525), RD~B on D1/D2; /frontend-dev visual close-gate.
- origin/CLOUD current; no unpushed CTO commits.

## Follow-on / pending Andrew (parked, non-blocking)
- NERG hop-0 build (free insurance-scan on IR connections) + Bright Data experience-field probe (gates multi-hop) + connections_graph module.
- AUM-band scoring: hard-filter vs soft-penalty.
- DS~C Prudent Man drill RAVC2 → me.
- MDPF-FE visual-verified close.
- ADVI_INFMVP Andrew smoke.

## Compiler Tools
None gold/portal this tick — doc + image deliverable. Live secadv/web-scrape pulls for the case-study data (Lincoln AUM $22B via SEC ADV, site-language term-class counts). comp-* N/A (find/imo uninstrumented).
