# IRPT_CUSTDY decomposition -- ROUND 1, the THREAD (issuer 2.0.0_SA_COO~K2; drafted 2026-10-07 ~08:1xZ, dell2)

**Status: DRAFT -> ISSUED in one issuance** (the issuance commit carries the `fanout:` line).

**Cut on:**
- PRD `org/missions/D9/IRPT/IRPT_CUSTDY/prd/IRPT_CUSTDY_PRD.md` v0.2 @c2bc15f427, ADMITTED (`python .tools/prd-signoff.py status
  IRPT_CUSTDY`: ratified-text SIGNED by `3.0.0_SA_CVO`, current; brief half accepted, the CRO wrote the brief).
- Receiving check: `python .tools/receiving-check.py <PRD>` -> ACCEPT (v0.1 was HANDED BACK, msg 4; v0.2 answers it, msg 78).
- Seating: `0.0.0_AB_MSTR~DELL2` on `1.0.0_SA_CTO` relay (bus d186faa0); `/canonical-drive IRPT_CUSTDY` per Andrew-direct ~07:16Z (msg 1).
- Adopted-work inventory (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ADOPTED_WORK_INVENTORY_FOR_THE_DELLS_20261007.md` @83d5e34919):
  0 rows for IRPT_CUSTDY. Nothing to adopt; nothing duplicated.

**Round 1 is the PRD's section 2 THREAD (FWD-1)**, decomposed over its six hops:
1. the advisor and the client list; 2. Schwab's records for those accounts; 3. the figures; 4. the securities; 5. the report;
6. the firm's read.

**Rule 24.** Domain: the six hops of the thread, nothing else (Cottonwood, Inflection, the field map, both comparisons and the
switch-off view are the ENRICHMENT BACKLOG, later rounds; PRD section 2 last line). Hop 2 is a CONSUME folded into hop 3's cell (its
only reader; no write of its own). Hop 6 is a person's read, never a worker cell: it is the issuer's act after the drain. Hops 1, 3,
4 and 5 are one cell each: one intent each (list / compute / describe / render), one write set each, no remainder.

## Measured constraints (read at the base, dell2 CLOUD @3e9c4be7d3 + origin, 2026-10-07 ~07:5xZ-08:1xZ)

1. **Code paths named by the thread: 7 of 7 PRESENT** at HEAD -- `infra/logic/registry/scopes.json` @0146e0c954,
   `data/assets/scripts/gold/investor_reporting/directory_runner.py` @8e9ed1b539, `data/assets/scripts/silver/schwab_conversion.py`
   @6bfea3fdf5, `data/assets/scripts/gold/investor_reporting/holdings_49f.py` @0b7d3c77a1,
   `infra/aws/lambda/v2_portal/_shared/etf_classification.py` @96f17cdbe9, `infra/aws/terraform/investor-reporting/export/b2_render.tf`
   @f35dfe003c, `lib/opal_naming.py` @4991b8b11b. The returns producer is `data/assets/scripts/gold/irpt_reporting/account_return_daily.py`
   (sources declared in `.../irpt_reporting/sources.json`; firm resolved by `opal_naming.lookup()`, never typed).
2. **Schwab data (S02), live** (`.tools/aws s3api list-objects-v2 --bucket opal-data-assets --delimiter /`): `schwab/08242234/` holds
   `_ops/ bronze/ meta/ silver/`; `schwab/08335338/` holds `_ops/ bronze/ gold/ meta/ silver/`. Freshness through 2026-09-30 is
   UNMEASURED here: the hop-3 cell measures it (partition dates printed) before computing anything.
3. **Firm scope:** `opal_naming.lookup('08242234')` and `lookup('08335338')` both -> firm `49financial`. One firm, two masters.
4. **The render (S07), live:** `irpt-export-render` Active, LastModified 2026-10-06T01:35:28Z (`aws lambda get-function`). IRPT_BCKEND
   owns it (PRD section 4). **Its input is NOT a document:** `export/b2_render.tf` (lines 1-17) shows `submit-export` minting a render
   token (SSM `/irpt/render-token/<ATT-id>`) and dispatching a render host that renders the read functions' render ports, i.e. portal
   pages. Whether that path can render a client-report document is UNMEASURED (the PRD's S07 claim "held" is for the path, not for this
   input). CU-a-4 measures it from the source first; a gap it finds is a ROW and, at the drain, the issuer's request to IRPT_BCKEND's COO
   -- never a write into its paths.
5. **Builder output (rule 30; the CTO's L4 "owed at L5" for S06)**, `lib/opal_naming.address('irpt', <lookup firm>, <tier>, <table>,
   'date=2026-09-30')`:
   - the per-client report figures (hops 3 + 4 joined): `s3://opal-data-49financial/irpt/49financial/gold/client_report/date=2026-09-30`
   - the per-firm template is DATA under the firm's own scope (state tier, as the IRPT reporting policy keeps request state):
     `s3://opal-data-49financial/irpt/49financial/state/report_template/version=1` (`address('irpt', <lookup firm>, 'state',
     'report_template', 'version=1')`). One firm's template is one object under one firm's prefix, so changing it cannot touch another
     firm's (FWD-3 ACCEPT, C-FIRM), and no firm token is typed into a repo path or string. Its authored content lives in the cell's
     `tests/fixtures/`; the upload is the issuer's act after the drain.
   - S09 (field map) and S12 (switch-off view) are later rounds; their builder output is owed when they are cut.
   Code never types these: it calls `address()` with the firm from `lookup()`.
6. **Standard periods -- ISSUER RULING for round 1.** The PRD defers the set to "the 49 Financial template"; no such template exists in
   Opal (brief F6; brief line 151: the firms' required sections are not known). The estate's ruled set is IRPT_BCKEND's
   `parity_period_returns.RULED_PERIODS = ("QTD", "YTD", "1Y", "SI")` (task order `IRPT_BCKEND.TO-IB-pr-192`); 3Y raises
   `WindowNotRuled`. **Round 1 reports QTD, YTD, 1Y and SI, read from that constant, never re-typed.** The firm's read (hop 6) states
   whether its report needs another period; a period it names is an ENRICHMENT item, not a round-1 recut.
7. **The named advisor -- OPEN, at Andrew.** Not in the brief, the PRD or the register. Hop 6 needs a real person at the firm to read
   the run, so the choice is Andrew's (routed to `1.0.0_SA_CTO~DELL2`, who adjudicates this box's open calls). **No cell waits on it:**
   every tool takes the advisor as an argument; only the issuer's real run after the drain needs the name.
8. **Fees (S04), PRD ruling 2:** round 1 reads the fee rows Schwab's transactions carry, labels them "Schwab transaction fee rows", and
   names every account where those rows are not the billed fee. The billed-fee source (Q-2) is not measured and not guessed.
9. **Dependency graph:** `comp-blast irpt-export-render` -> TOOL-FAILED on dell2 (the box user cannot read `opal/mcp/graph-read-token`;
   row `NFRA_CTLPLN-S7` @4561c1b67d). A coverage limitation, never absence: every cell's write set is NEW files; no existing producer,
   Lambda or route is modified this round. `comp-routes behaviors`: no IRPT route matched (no route touched). `comp-cache`: portal React
   Query only; no portal surface in round 1.

## THE CLIENT-REPORT CONTRACT (fixed here so the four cells run in parallel)

One JSON document per client (household), written by CU-a-2 + CU-a-3's join and read by CU-a-4:

```
{"firm": <lookup firm>, "advisor": <as given>, "as_of": "2026-09-30", "household": {"id", "name"},
 "periods": [<RULED_PERIODS, in order>],
 "accounts": [{"account": <last 4 only in any printed output>, "registration",
   "returns": {<period>: {"value": <float|null>, "window": [<start>, <end>], "status": "OK|NO_DATA|WINDOW_NOT_RULED"}},
   "market_value": {"start", "end"},
   "holdings": [{"symbol", "cusip", "quantity", "market_value", "weight",
                 "class", "sector", "described": true|false, "description_source": "MDPF_SECCLASS|NONE"}],
   "activity": [{"date", "type", "symbol", "amount"}],
   "fees": {"amount", "source": "SCHWAB_TXN_FEE_ROWS", "is_billed_fee": "UNKNOWN"}}],
 "household_returns": {<period>: {...same shape...}},
 "lineage": {"schwab_partitions": [...], "returns_partition", "classification_vintage"}}
```
Every figure carries `status`; a figure that cannot be made says so in place (never dropped, never zero-filled).

## The cells

| cell | what | serves | status | placement | risk | chain / slot |
|---|---|---|---|---|---|---|
| `CU-a-1` | hop 1: the advisor's client list -- given an advisor (rep code or name), resolve it against the registry and the IRPT_BCKEND directory, print accounts and households with their counts (account numbers masked to last 4); refuses an advisor with zero accounts | FWD-1 | NOT-EVALUATED | dell2 | LOCAL | A, `0.9.0_WK_IRPT_CUSTDY~1` |
| `CU-a-2` | hops 2 + 3: the figures -- for an account list, prints the Schwab partition dates it read (refuses if 2026-09-30 is not covered), then computes per account and household the RULED_PERIODS returns from the `account_return_daily` gold, start/end market value, holdings, activity from the transaction rows, and fee rows labelled; writes the contract's JSON locally by default, `--apply` to the `address()` prefix | FWD-1 | NOT-EVALUATED | dell2 | WORLD | B, `0.9.0_WK_IRPT_CUSTDY~2` |
| `CU-a-3` | hop 4: the securities -- given holdings, returns class and sector per holding from the one classification table (`etf_classification.py` reader) and `described: false` with `description_source: NONE` for any holding it cannot describe; prints described/undescribed counts | FWD-1, FWD-6 | NOT-EVALUATED | dell2 | LOCAL | C, `0.9.0_WK_IRPT_CUSTDY~3` |
| `CU-a-4` | hop 5: the 49 Financial template and its render input -- the per-firm template (sections, period order, wording, branding slots) as data read from the firm's `address()` (fixture locally), and a builder that lays one contract document into the template; prints the render path's input contract as read from IRPT_BCKEND's source (`submit-export` and the render host), and renders one fixture locally through the template | FWD-1, FWD-3 | NOT-EVALUATED | dell2 | LOCAL | D, `0.9.0_WK_IRPT_CUSTDY~4` |

## Write sets (disjoint)

- **CU-a-1:** `data/assets/scripts/gold/irpt_custody/advisor_client_list.py`, `data/assets/scripts/gold/irpt_custody/tests/test_advisor_client_list.py`.
- **CU-a-2:** `data/assets/scripts/gold/irpt_custody/client_report_figures.py`, `data/assets/scripts/gold/irpt_custody/tests/test_client_report_figures.py`.
- **CU-a-3:** `data/assets/scripts/gold/irpt_custody/security_descriptions.py`, `data/assets/scripts/gold/irpt_custody/tests/test_security_descriptions.py`.
- **CU-a-4:** `data/assets/scripts/gold/irpt_custody/report_render_request.py`,
  `data/assets/scripts/gold/irpt_custody/tests/test_report_render_request.py`,
  `data/assets/scripts/gold/irpt_custody/tests/fixtures/report_template_firm_a.json` (the 49 Financial template's content; the fixture name
  carries no firm token -- the firm is bound only by the `address()` the issuer uploads it to).
- Each: its own deliverables folder `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/<worker serial>/` and the investigation file.

**Ordering and fan-out:** `fanout: 4 of 4 chains, cap 8` -- A, B, C and D are independent once the contract above is fixed; each builds and
tests against its own fixture. CU-a-2's real-data read and every `--apply` are the issuer's acts after the drain.

## The issuer's acts after the drain (L7 close; the COO's one real run of FWD-1)

1. Andrew's named advisor in hand (constraint 7); if not, the real run waits on that one call and nothing else.
2. `CU-a-1` for that advisor: the account and household list, counts printed.
3. Open the ledger entry `org/critical_paths/change_management/` (a write into a NEW prefix whose key list the issuer controls: the
   never-widen pair does not apply -- CLAUDE.md section 5 non-application).
4. Upload the template fixture to its `address()` (state tier, constraint 5); read back. Then `CU-a-2 --apply` joined with `CU-a-3`: one
   contract document per household under the gold `address()` prefix; read back (count = households).
5. `CU-a-4` for each document, through `irpt-export-render`: one report per client; each opened and looked at.
6. Close the ledger entry with the measured keys and counts.
7. Hop 6: the reports go to the firm's reader Andrew names; nothing reaches a client (C-TEMPLATE). The read, with each report it would
   not send and the reason, is FWD-1's EXERCISED evidence and goes to the L8 packet.
