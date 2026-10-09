# NFRA_TRNSPT -- rounds 12-14 remediations

<sweep_watermark>2026-10-09T02:26Z</sweep_watermark>

Graduated at rounds 12-14's L9 (ADJUDICATION_v9.md), round label v15: D2-S7 and D2-W2-S3, both REMEDIATED and closed by rounds 15-16 before this file was committed; plus round 16's D2-S8, OPEN.

Committed 2026-10-09T03:26Z once every NFRA_TRNSPT order read terminal (TR-j15 merged @4ecf1633cb, TR-h16 @2d3bcce249; round-close 15 and 16 MAY-CLOSE).

```json
[
  {
    "id": "NFRA_TRNSPT-D2-S7",
    "project": "NFRA_TRNSPT",
    "fabric": "dell2",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "FWD-10 H6 will dead-letter every REAL report: ~V2's ticket-write contract v0.1 section 2 REQUIRES answers.household, but the IRPT analysis composition has no household (~P2 msg 1849: 'account_type, themes and household are ABSENT from irpt-analysis-composition.v1'). The synthetic trace passes only because its fixture supplies one.",
    "evidence": [
      "investigation row NFRA_TRNSPT-D2-S7",
      "org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R13_CLOSE.md",
      "TR-h-16 merged @2d3bcce249: ticket_client omits answers.household when absent; title never built from household (contract v0.2 @20784c5462 section 8)",
      "org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R16_CLOSE.md",
      "pytest test_commentary_classification.py + test_commentary_ticket_client.py: 10 passed (this seat's run, ~03:3xZ)"
    ],
    "remedy": "A ruling with ~V2: household optional in the ticket-write contract, or its true source named; then ~T2 adapts the drafter's ticket payload, and one synthetic REAL-shaped report reaches H6 done.",
    "owner": "1.0.0_SA_CTO~DELL2",
    "round": "v15",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~DELL2",
      "round": "v15"
    },
    "closed": true
  },
  {
    "id": "NFRA_TRNSPT-D2-W2-S3",
    "project": "NFRA_TRNSPT",
    "fabric": "dell2",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The irpt-normalized-portfolio.v1 artifact carries NO category field: a position row is security_id + analysis_dollars + original{identifier, quantity, source_*} (docs/contracts/investor-reporting/v1/examples/RequestComposition.synthetic.json:134-182; intake/portfolio.py:283; ycharts/generate/normalized_input.py rows are identifier+USD only). So H2 holdings_categories stays {} on every real input.",
    "evidence": [
      "investigation row NFRA_TRNSPT-D2-W2-S3",
      "org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R14_CLOSE.md",
      "TR-j-15 merged @4ecf1633cb: holdings categories joined from the etf-classifications snapshot on TICKER-namespace identifiers; coverage returned beside the request, never to the model",
      "org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R15_CLOSE.md",
      "pytest test_commentary_classification.py + test_commentary_ticket_client.py: 10 passed (this seat's run, ~03:3xZ)"
    ],
    "remedy": "Derive the holdings category from the canonical per-security table (DynamoDB etf-classifications, asset_class by ticker) as a next-round cell, with the unmatched securities named.",
    "owner": "2.0.0_SA_COO~T2",
    "round": "v15",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~T2",
      "round": "v15"
    },
    "closed": true
  },
  {
    "id": "NFRA_TRNSPT-D2-S8",
    "project": "NFRA_TRNSPT",
    "fabric": "dell2",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "commentary.tf as written cannot carry FWD-10 live: the Lambda's env omits five names lambda_handler._live_ports() reads (TICKET_API_BASE, TICKET_TOKEN_SECRET_ID, KIMI_API_URL, COMPOSITION_BUCKET, COMPOSITION_KEY_PREFIX) and its policy has no read on the svc-commentary ticket secret, so an apply now would stop every record at NO_COMPOSITION_SOURCE or fail the ticket write.",
    "evidence": [
      "investigation row NFRA_TRNSPT-D2-S8 (@4d6e134c7d)",
      "org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R16_CLOSE.md",
      "CTO msg 2259 (agreed: a round-17 cell)"
    ],
    "remedy": "Round 17's TR-c-17 completes commentary.tf: the five env names lambda_handler._live_ports() reads plus the svc-commentary secret read, addresses from lib/opal_naming.py address(); the composition read stays in the apply pair.",
    "owner": "2.0.0_SA_COO~T2",
    "round": "v17",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~T2",
      "round": "v17"
    },
    "closed": false
  }
]
```
