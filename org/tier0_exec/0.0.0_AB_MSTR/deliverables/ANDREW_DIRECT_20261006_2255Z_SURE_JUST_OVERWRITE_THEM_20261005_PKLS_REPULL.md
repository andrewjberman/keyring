# ANDREW-DIRECT 2026-10-06 ~22:55Z -- "sure just overwrite them": the two 20261005 PKLs, so the Bloomberg re-pull fetches fresh data

Given at the `0.0.0_AB_MSTR~Z` terminal (site Z), in-session, ~22:55Z (6:55 PM ET).

## The question put to him (0.0.0_AB_MSTR~Z, asked since ~19:2xZ, last form)

"may BG rename this morning's two Bloomberg data files (`data 20261005 v1.pkl` and `model 20261005 v1.pkl`, to
`v1 bkp`) so the re-pull fetches fresh data, or should Yang re-pull himself? I recommend the rename; it deletes
nothing and can be undone."

## Verbatim

Andrew: "sure just overwrite them"

## Why it was needed

`market_indices_data_pull.ipynb` cell 16 loads an existing PKL for the target date instead of querying Bloomberg. The
two files were written 08:27 / 08:29 ET on 2026-10-06, before Yang Liu re-saved the CIX definitions. A re-pull with
them in place reports success and serves the same pre-fix benchmarks (finding: `0.0.3_BG_BBGTerminal`, msg 30244).
The files sit in the OneDrive production output folder, outside BG's fence, so the act needed Andrew's word.

## Scope as read (surfaced, not adjudicated)

- The two files named in the question, and only those.
- His word is that the fresh pull replaces them. Relayed to `0.0.3_BG_BBGTerminal` to carry out as the rename to
  `v1 bkp` (Yang's staging convention): it has the same effect on the pull and keeps a copy. Nothing is deleted.
- The re-pull is step 1 of the integrate order Andrew gave at the laptop MSTR terminal ~21:4xZ ("the BBG fix has to
  precede these"), so it runs during the fabric hold.
