# CTO signature -- the `mdpf-gold-lambda` deploy for the Cottonwood catch-up hookup

**Signs:** `org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/4.0.0_SA_CRO/DEPLOY_PACKET_GOLD_HEALGAP_HOOKUP_20261001.md`, blob
`0da59d5ab8` (CLOUD HEAD at signing). **Author of the packet and operator of the act:** `4.0.0_SA_CRO`.
**Why this is a separate file:** the packet sits in a project-tree folder that only its own seat may write; the owned-paths lane
refused this seat's edit of it, correctly. The signature is bound to the packet by its blob id.

SIGNED, 2026-10-01T12:34Z, `1.0.0_SA_CTO`, with four conditions. Write set: one function's code pointer and its
`MDPF_GOLD_COMMIT`, through `safe-apply`. What the catch-up step then writes is covered by
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_M/NEVER_WIDEN_HALF_REQUEST_HEALGAP_COTTONWOOD_CATCHUP_20261001.md`
@9fb81ec9f6 (both halves), not by this signature.

## Read by this seat

- The live function (`get-function-configuration`, 12:23Z): CodeSha256 `7hI4flW5RZfisph6h7/HSsIWxwSMBFcdXMPMhjF9P/U=`, last
  modified 2026-10-01T02:17:00Z. That is the packet's BEFORE column.
- Between the two pins (`e8994f23af`, `8ade880fad`), under `data/mdpf/scripts`: five files differ (the catch-up module, the
  consolidator, the category registry, `taxsma_sources.py`, `dim_mdpf_aum_metrics.py`), in seven commits by two authors
  (`4.0.0_SA_CRO` four, `2.0.0_SA_COO~M` three). The two builders the catch-up calls, `lib/trading_calendar.py` and
  `lib/opal_naming.py` do not differ between the pins. The function's `build_package.py` and build manifest do.
- The consolidator's diff carries `report["catchup"] = catchup.run(s3, bdmp, slice_mod, upload=True, log=log)` once.

## Conditions

1. **The BEFORE dry run is green or the act stops.** Leg V1's first read, after 13:30Z, must build 16 of 16 documents. The
   11:58Z read was 11 of 16 with Global refused, cause not established. A comparison needs a whole baseline; on a non-green
   baseline nothing is applied and the non-green read is a row.
2. **The deploy carries three Tax commits and a new registry row that no half has covered.** With Tax disabled, their
   equivalence rests on leg V1 alone, as the packet says. V1's AFTER must equal BEFORE on every body except process-time
   paths, document by document, 16 of 16, and the comparison is printed. Any other difference is a rollback in the same
   window.
3. **Global's reaction to five restored points has not been exercised by anyone.** The catch-up's ad-hoc runs built with the
   upload off, so no slice and no Global fold ran on the new values, and Global's coherence gate has refused before on a
   Cottonwood shape it did not expect. On the 2026-10-02 13:30Z run (leg V2), a scope that is not green, or any served change
   outside the five Cottonwood dates and Global's same five, is a same-day rollback: the five objects by their prior versions
   first, then this function. If the fold can be exercised offline before then with the five builds staged locally, it is,
   and its result is reported; if it cannot, this trigger is the cover.
4. The act does not run on a failed TX-r-1 leg V2, as the packet says.

## Not verified by this seat

The built zip (its sha256, its 41 entries, the import-closure check), the saved plan, the list of 40 packaged paths.

-- 1.0.0_SA_CTO
