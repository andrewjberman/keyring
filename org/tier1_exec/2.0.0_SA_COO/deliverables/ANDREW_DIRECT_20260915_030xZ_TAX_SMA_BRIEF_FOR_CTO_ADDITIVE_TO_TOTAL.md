# ANDREW-DIRECT 2026-09-15 ~03:0xZ -- WRITE A BRIEF TO CONNECT THE 49FINANCIAL TAX SMA DATA; A CTO RENDERS IT INTO A PROJECT; THE TAX AMOUNT IS ADDITIVE TO THE TOTAL

**Terminal:** `2.0.0_SA_COO~D`, page-by-page mode. **Recorded by:** `2.0.0_SA_COO~D`, in the same turn. It answers this
seat's ~03:0xZ report:
- 49Financial's Tax-Managed SMA is registered (mdpf_category_registry.py:360, ALT Strategies, basis ADDITIVE) but gets no
  dollars;
- its five accounts sit in Schwab master 0833, while SMA dollars come only from the 0824-based SmartX by_model series
  (mdpf_gold_consolidator.py:880-882).

## VERBATIM AND ENTIRE

> write a brief for what you would need to get the data connected properly, and I will have a CTO render it into a
> project and finish tracking. We can just add that tax amount to the total, even though its technically in a
> different account bucket, it's fine, that just means its additive (is not netted from client residual).

## WHAT IT SETTLES

1. **This seat writes a brief:** what is needed to connect the 49Financial Tax SMA data to the Asset Category Views.
   **A CTO (his pick) renders it into a project** and finishes the tracking.
2. **The Tax SMA amount is ADDED to the firm total.**
   - It is additive: it is NOT netted out of the Client residual, even though its accounts sit in a different Schwab
     master (0833) from the pool the rest of the view is built on (0824).
   - This is his word on the basis. It confirms the registry's existing ADDITIVE declaration (registry :358-360)
     and the consolidator's additive arm (consolidator :746-758, :883).

## WHAT IT DOES NOT SETTLE

- **Which CTO seat renders it.** He names "a CTO" and will hand it over himself. This seat delivers the brief and does
  not route it into the L1-L10 flow on its own.
- **The ~03:0xZ interim display choice** (keep ALT Strategies "$0" for 49Financial, or mark the bucket not yet tracked)
  is not ruled by these words.
- It rules none of the seven open calls (@31f728cea4), does not close DSGN_REBRND and does not promote.
