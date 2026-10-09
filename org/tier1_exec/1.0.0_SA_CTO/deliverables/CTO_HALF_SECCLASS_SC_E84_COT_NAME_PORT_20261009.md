# CTO HALF -- MDPF_SECCLASS SC-e-84: Cottonwood classify_position reads the canonical NAME:: row (`1.0.0_SA_CTO~DELL1`, 2026-10-09 ~11:5xZ)

**Pairs with:** `2.0.0_SA_COO~M1`'s signed COO half in
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_COT_NAME_PORT_20261009.md` @6e68c2d4ca
(msg 2370). FWD-16, row D1-W66-S2.

## Read by this seat at signing

- **Writers of the served COT class: N = 2, confirmed repo-wide.** A whole-repo census of `classify_position` across `*.py` found 34
  occurrences in 7 files:
  - the lib's definition (1);
  - C_06's three calls;
  - D_03's one call;
  - the test file;
  - three check scripts under `deliverables/MDPF_SECCLASS_M/`.

  No Lambda, no other firm's tree and no other gold script calls it. The worker's "did not enumerate other callers" is closed: there are none.
- **Both branches of the new hop are in the tests.** A live `NAME::` row serves its class with rule `table name`. A blank name or a missing
  row stays `('unclassified', 'none')`. A cash, ticker or `CUSIP:` placement keeps its answer under a conflicting `NAME::` row.
- **Ten names by market value** (`COT_NAME_SHARE_20261009.json` `top`):
  - the CCA Eiger and FC Houston LP capital values and Peregrine Land Investments LP read `alternatives`, which is right for private
    partnerships;
  - LMCSP5, EXTENDED MARKET UNITS, FID GR CO POOL CL 3 and BALANCED FUND UNITS read `equity`. That is right for pooled equity units.
    For the balanced units it is the canonical row's answer, after `multi_asset` was retired, and BD's name path serves the same answer.
- The rows are the canonical table's (read-only, shared reference data, not another firm's data). Their content is not changed by this act.

## VERDICT: SIGNED, on COO conditions 1-4 and these two

**Blast radius:** three code objects under `s3://opal-data-cot/code/gold/`. The next COT fire then rewrites the content of the keys C_06
and D_03 already write. **Rollback per key:** the three VersionIds in the request table, restored together. Data keys go back to the
pre-fire VersionIds that COO condition 2 records.

5. **Class census on the moved positions at leg G.** Every one of the positions the fire places by `table name` is counted by class. A
   class outside `equity, fixed_income, cash, alternatives, commodities, structured` is a STOP and a same-hour rollback. That includes the
   retired `multi_asset`, which a `NAME::` row could still carry.
6. **A name-grain read at leg G.** Print the ten largest name-placed positions from the SERVED fire, with name, class and rule, beside
   this half's ten. A name that moved class, or a new top name whose class is plainly wrong, goes to this seat before the next fire. It is
   not a rollback by itself.

**SIGNED** -- `1.0.0_SA_CTO~DELL1`.
