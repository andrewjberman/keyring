# IRPT_ANLREQ round 58, workstream ~G (ENGINE) -- decomposition: where the Opal model compositions live (the read the comparison side of the price pages needs)

Issuer `2.0.0_SA_COO~G2`, 2026-10-19.

**Input.** CTO msg 10778 (ruling on the comparison portfolio): in an Analysis Request the comparison portfolios are the selected entries of the comparison catalogue (up to five), each an Opal model or a ticker (`ycharts/generate/comparison_catalogue.py:1-15`, `submission.py:67-72`). A ticker uses its own series from the existing price stage; **a model uses the composite of its catalogue weights, priced the same way; a model's weight read is a cell of its own if no reader exists.** Measured now (this seat, 2026-10-19): the catalogue entries in `ycharts/generate/templates.json` (`comparison_catalog.entries`, 5 entries) carry NO weights, holdings or components: only a model code (`vendor_id` UST, ST, INT, LT, ULT; `yang-model-portfolio-benchmarks/lambda_function.py:66` `MODEL_CODES`) and mapping evidence. The estate names the composition's producers elsewhere (the MDPF pipeline: `data/mdpf/scripts/bronze/pull_orion_model_composition.py`, `workflows/atom_decomposition/catalog_entries/opal_data_mdpf_feeds_model_composition.yaml`, `.../opal_data_assets_silver_eclipse_inflection_fact_model_composition.yaml`), but this seat has NOT read which one a resident reader should use, in which bucket, under which firm.

**Why a trace first, and why now.** The comparison side of the comparison and multi maps (19 and 27 price-based elements) cannot be cut until the model-weight read has an address and a reader. The trace is read-only, LOCAL, independent of round 57 (which is mid-build) and of every other cell, so it runs now. The map cells for the portfolio side wait for round 57 to merge and are cut as the next round.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-169` | a read-only record answering six labelled questions about the Opal model compositions, each with a `file:line` citation or `NOT READ` | the worker's own folder only | LOCAL (code read; no AWS call, no run, no deploy) |

## Edges and chains

ONE chain, no dependency. `fanout: 1 of 1 chains, cap 8`.

## The six questions (inlined in the order)

Q1 where the compositions (model code, ticker, weight) are stored: producer, bucket or table, builder address, columns, as-of grain. Q2 whose bucket it is: firm-private or shared (CLAUDE.md section 5, never reference another firm's data from a pipeline tree). Q3 whether a reader already exists that returns `{ticker: weight}` for a model code on a date (module, signature). Q4 how fresh and on what schedule. Q5 which role a resident reader would run as and whether IAM already grants the read (read the `.tf`, no AWS call). Q6 how a catalogue `vendor_id` maps to the composition's own model identifier.

## Four-postulate record

(i) Domain: the five catalogue model codes of `comparison_catalog.entries`; the five entries are printed by this seat, and the tickers path is out of scope (it needs no weight read). (ii) One grain: a model code. (iii) One intent: find and cite the read; build nothing. (iv) What this cut does NOT move: any code, map, bucket, role or run.

fanout: 1 of 1 chains, cap 8, reason: one read-only worker cell.
