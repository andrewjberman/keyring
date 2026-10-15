# Finding: r32 is the resident leg only; the stamps and the upload door run in the irpt-ycharts-generate Lambda (2.0.0_SA_COO~G2, 2026-10-15 ~21:0xZ)

**Measured** at trial pin `cbf05a6afa` (package built by `r32_build.py`, 310 members) and in the tree at HEAD.

## What runs where

The static import walk from the resident's entry modules (`r32_reachability.py`, st12's script extended to `ycharts/research`) reaches 74 modules in r32 (69 in r31). Of the members r32 changes or adds:

| member (cell) | in the resident | also staged into |
|---|---|---|
| `reports/resident_installed.py` (AR-g-85 map by variant, AR-g-87 commentary revision, AR-g-90 pricing binding) | REACHABLE | -- |
| `ycharts/generate/resident_worker.py` (AR-g-91 producer list r41b) | REACHABLE | `irpt-ycharts-generate` |
| `ycharts/research/{opal_producer, layout_overview}.py`, `runner.py`, `portfolio_series.py`, `price_source.py`, `tr_level.py`, `price_adapter_bbg.py`, `price_adapter_yfinance.py` (AR-g-86, 88, 89, 93, 68, 80..84) | REACHABLE | -- |
| `price_adapter_demque.py`, `price_adapter_ycharts.py`, `swap_replacement.py` | not reachable | -- |
| `ycharts/generate/acceptance.py` (AR-g-67, AR-g-85: the accept step WRITES `ticket_confirmed` and `report_variant`) | reachable (the resident READS records) | `irpt-ycharts-generate`, `irpt-status`, `irpt-commentary-composition-read-lambda`, `irpt-commentary-draft-store-lambda` |
| `ycharts/generate/submission_service.py`, `reports/generate_installed.py`, `ycharts/generate/prospect_submission.py`, `ycharts/generate/ticket_confirmation.py` (AR-g-67) | NOT reachable | `irpt-ycharts-generate` (the first two; the last two have NO staged row) |
| `intake/uploads.py`, `intake/portfolio.py` (AR-g-68 keep as UNRESOLVED, AR-g-95 the door derives the price date) | reachable (frozen-input reads) | `irpt-ycharts-generate` (the upload door) |

Source: `infra/aws/lambda/ci/lambda-source-map.json` (`staged_from` rows) and `infra/aws/terraform/investor-reporting/ycharts/generate.tf:375` (`handler = "generate_installed.lambda_handler"`).

## What this means

- r32 delivers the resident's READING side: the producer list (r41b), the map chosen by a record's `report_variant`, the commentary revision, the pricing binding (off), and the Opal engine's figures when pricing is switched on.
- The WRITING side lives in `irpt-ycharts-generate`: the accept step that stamps `ticket_confirmed` (AR-g-67) and `report_variant` (AR-g-85), the upload door that keeps an unknown symbol as UNRESOLVED (AR-g-68) and derives the price date (AR-g-95). Until that Lambda carries the new code, a Comparison or Multi-Comp record has no `report_variant` (the resident reads it as an overview), no staff filing is stamped `ticket_confirmed`, a kept NOT_FOUND symbol is refused as today, and a client-sent `price_date` is still honoured.
- That Lambda leg also needs: a `staged_from` row for `ticket_confirmation.py` (the import is lazy and only runs when `IRPT_TICKETS_TABLE` is set, so nothing breaks today); the environment variable `IRPT_TICKETS_TABLE` in `generate.tf`; and `dynamodb:GetItem` on the tickets table for the Lambda's role (the IAM leg named in the AR-g-67 read). Each is a Terraform or CI change with its own pair.

## The call

Who issues the Lambda leg, and under which pair? The CTO's ruling made `~G2` the resident's single issuer; it is silent on `irpt-ycharts-generate`.
