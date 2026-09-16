# ANDREW-DIRECT 2026-09-15 ~04:0xZ -- COTTONWOOD'S ASSET CATEGORY VIEWS ARE FROZEN AT 2026-09-10; TRACE AND REMEDIATE

**Terminal:** `2.0.0_SA_COO~D`, page-by-page mode. **Recorded by:** `2.0.0_SA_COO~D`, in the same turn. It arrived while
the ~03:4xZ Positioning fixes were being verified. He sequenced it after the ~03:5xZ Global RSI fix.

## VERBATIM AND ENTIRE

> After that there is another glitch I need you to track down. It is from the Asset Class Taxonomy on Model Portfolios.
> What's happening is that somehow, for Cottonwood, there is a break and the Models/SMAs/Clients-level taxonomy pull
> froze. Everything else, the taxonomy pull and the model-level pull for all the other scopes (Global and Firms) worked
> fine and is displaying September 11 data, however that one view is stuck on September 10 for Cottonwood. I need you
> to figure out why and fix it. Trace it and remediate.

## WHAT IT SETTLES

1. **A defect to trace and remediate, directed at this seat by name.** On Model Portfolios, the Asset Category Views
   block (the Models / SMAs / Client taxonomy) for the COTTONWOOD scope shows 2026-09-10.
   - Every other scope (Global and the other firms) shows 2026-09-11.
   - Cottonwood's model-level data is also current.
2. **The order is his:** after the Global RSI fix.

## HOW 2.0.0_SA_COO~D PROCEEDS, AND SAYS SO

- **The trace starts now, read-only, in the background.** It covers:
  - the served object and its as-of;
  - the producing job and its trigger;
  - the run logs for 09-11 onward;
  - the guard or input that stopped cottonwood's emit.
- **The remediation follows the finding.** A code fix in `data/mdpf/scripts/gold/` or a re-emit of served output
  goes through the lanes and gates the law names for it: the DS deploy lane (Rule 13), and the never-widen sign-off
  for moving served output. This seat reports which, and does not bypass them.

## WHAT IT DOES NOT SETTLE

It rules none of the seven open calls (@31f728cea4), does not close DSGN_REBRND and does not promote.
