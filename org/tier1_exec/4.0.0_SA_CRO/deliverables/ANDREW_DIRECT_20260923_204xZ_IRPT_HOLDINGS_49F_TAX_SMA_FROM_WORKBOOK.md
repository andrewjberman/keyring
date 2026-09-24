# ANDREW-DIRECT 2026-09-23 ~20:4xZ (~16:4x ET) -- 49F Tax SMA shows under SMAs > ALT > Tax, from the workbook

**Received by:** `4.0.0_SA_CRO~M`, at its own terminal, answering `/open-calls` CALL 1 of 1 (same session).
**Recorded same turn per `org/XXX.md`.** Follows `ANDREW_DIRECT_20260923_194xZ_IRPT_HOLDINGS_OPAL_TAXONOMY_CLIENT_IS_PLUG.md`
@e5cf6d6549 and the CTO's contract amendment @a62f5e54a7. Scope is NOT adjudicated here; the contract is `1.0.0_SA_CTO`'s.

## The card he answered, verbatim as put to him

> **49 Financial Tax SMA in Holdings: (a) leave in Client, or (b) show under SMAs > ALT Strategies > Tax, read from the
> SharePoint workbook?**
> Your "only applies for SmartX for 49" puts the ~$6.4M (5 accounts) in Client; Model Portfolios shows it as Tax SMA.
> The CTO applied (a) and noted the difference; the first Inflection proof doesn't wait on it.
> REC -- (b), after the first live flow. Otherwise two Opal pages label the same client dollars differently. The
> workbook feed already exists and its data contract is ratified, so this adds no new source.

## His words, VERBATIM -- the phrasing is the ruling

> *"B"*

and, in the next message, on the size:

> *"Also there is apparently 20m in assets for Tax, so we need to understand what we're missing and where if youre
> saying 6m. I would check the Yang Tax SMA spreadsheet sharepoint and corroborate real quick."*

## What it rules (index only; the quotes govern)

For **49 Financial**, the Tax SMA appears in Holdings under **SMAs > ALT Strategies > Tax**, identified from the
SharePoint Tax SMA workbook -- an exception to "this only applies for SmartX for 49" for this one SMA. This
supersedes the CTO's @a62f5e54a7 line that non-SmartX Tax custody "remains in Client". His "B" selects option (b);
the timing ("after the first live flow") was this seat's REC, not his words -- sequencing is the CTO's.

## The corroboration he asked for (read-only; client names and account numbers deliberately omitted)

**Workbook:** "Tax SMA Accounts.xlsx", Sheet1, 22 used rows (header + 20 slots + Total), SharePoint item
`01L6LHKFXVVTRR73M6KZGIHM4FY2ATNK4U` (the item `org/standards/MDPF_TAXSMA_DATA_CONTRACT.json` names), last modified
2026-09-22T19:07:44Z, etag version 223. Workbook "AUM (Mn)" is an intake estimate, which the ratified contract lists
as a REJECTED valuation substitute; custody value below is `net_mv_plus_cash` from
`s3://opal-data-49financial/gold/advi/canonical/canonical_valuation/date=2026-09-22/` (the contract's basis).

| Population (by workbook row) | Accounts | Workbook AUM | Found in 0833 custody | Custody value of those found |
|---|---|---|---|---|
| Traded = Yes | 9 | $15.13M | 7 of 9 | $10.88M |
| Not yet traded, has account number | 5 | $12.32M | 3 of 5 | $4.54M |
| No account number (one "awaiting account opening", one blank placeholder) | 2 | $16.00M | -- | -- |
| **Workbook total** | 16 rows | **$43.45M** | 10 of 14 numbered | $15.42M |

- **Why this seat said ~$6.4M:** that figure is a code comment in `data/mdpf/scripts/gold/mdpf_category_registry.py`
  ($6,445,461.07, 5 accounts), measured around 2026-08-29. The workbook's inception dates show exactly 5 accounts
  trading before September (workbook AUM $6.49M); 4 more traded 9/1-9/17. **The $6.4M was stale, not a different
  population.**
- **Nearest reading of "~$20M":** the 12 numbered accounts not marked "awaiting account opening" carry $21.25M of
  workbook AUM. Traded-only membership (the contract's rule: "Traded=YES alone asserts current live membership") is
  $15.13M by workbook, $10.88M by custody for the 7 we can value.
- **Missing, and where:** 2 of the 9 traded accounts (rows 7 and 8, workbook $3.38M + $1.07M) are in NEITHER landed
  Schwab master (0833 or 0824 `fact_acc`, 2026-09-22; positive control: row 1 found in 0833). Only those two masters
  are landed under `opal-data-assets/schwab/`. So those accounts either sit at a master we do not land, or are too new
  for the 9/22 file -- not determined here.
- **0 of 14** numbered Tax accounts appear in the SmartX account map (2026-09-23) -- which is why "SmartX only"
  would have put every Tax dollar in Client, and why "B" needs the workbook.
- **Model Portfolios today:** a saved copy of the 49F category-views output (as_of 2026-09-21,
  `.scratch/mdpf_qa/served_49financial_category-views_2026-09-21.json`) carries Tax with **no value** (null), not
  $6.4M. This seat's card said Model Portfolios "shows it as Tax SMA"; it shows the Tax node without dollars. That is
  the MDPF_TAXSMA pipeline's open state, read from a saved copy, not the live page.
