# AMGT_HARVST task order -- `HVST-bh-6` -- ROUND 61 (`1.0.0_SA_CTO~Z` msg 31486, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round60.md` @3b19f962e0): WHAT `ICT_US_Equity` IS AND WHERE ITS KEY CAME FROM -- A RECORD FROM EVERY SOURCE THAT COULD NAME IT, READ-ONLY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bh-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~112</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL scripts and records, plus a READ-ONLY census (S3 GET of the silver article parts through the served iterator). NO put, NO delete, NO gold or silver build, NO vendor or publisher host, NO collector or backfill_driver. `.runtime` is not read. Two collection legs are LIVE on the shared tree: touch nothing outside your worktree.
comp-adversary: RUN at L5 -- the adversary is a census with no printed denominator, a sample the script grades, a source substituted for a refused read, or a gold build.
</preflight>

## 0. THE CELL

`ICT_US_Equity` is one of the 242 securities in the served gold list (`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round60/securities.universe.r60.json`). Its
17 served pairs all rested on the ticker form `ICT` and none was about the security (Foxconn "ICT products", "Luxshare ICT");
the form is refused and the security now holds 0 pairs. A reviewer found no entry for it in the identity registry. The
question is what company this key is, and which source put the key on the list. Known so far, to be CHECKED not trusted:
`ICT_PM_Equity` is INTL CONTAINER TERM SVCS INC in the registry; the collector's identity file names `ICT_US_Equity`
"International Container Termin" (30 characters, cut).

## 1. THE BUILD (read-only)

1. `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~112/bh6_ict_source.py` reads each source below AS A FILE or through the function
   named, and prints one block per source: the source path, its record count (the denominator), and every record whose key,
   ticker or name carries `ICT` as a whole token (print the record's identifying fields, 300 characters at most each):
   - (a) the gold list file above;
   - (b) `lib/research/identity/registrations.json` (`registrations`);
   - (c) the collector's identity record: the path in `lib/opal_data_harvest/config.json` `symbol_resolution_source`;
   - (d) the pool universe document the list is built from: read `lib/research/harvest/universe_securities.py` `build()` to
     see how it is fetched and read it the same way (S3 GET, no put); print where it came from (bucket and key, or path);
   - (e) any `research_names` or symbol-resolution input `build()` reads beside the pool, the same way.
2. Then: `SOURCES READ: <n> of 5`, `SOURCES CARRYING ICT_US_Equity: <list>`, and ONE of
   `ICT_US_Equity IS: <name> -- per <source and field>` (when at least one source carries a company name on that exact key) or
   `NO SOURCE NAMES ICT_US_Equity`. If two sources disagree, print both and say so.
3. Print whether `ICT_US_Equity` and `ICT_PM_Equity` are two keys of one issuer by any field the sources carry (a shared
   identifier, the same name), or `NOT SHOWN BY ANY FIELD`.
4. Last line: `RECORD OK` only if sources (a), (b), (c) and (d) were each read with a record count above 0. Otherwise
   `RECORD FAIL` and the source that could not be read.
5. Write the output as `bh6_ict_source.out` and a half-page `BH6_ICT_US_EQUITY.md` beside it: what the key is, which source
   put it on the list, what is not known. Plain sentences, each figure with its source.
6. Remove nothing from any list. Change no product file. Call no vendor.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round60/securities.universe.r60.json
lib/research/identity/registrations.json
lib/opal_data_harvest/config.json
org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round47/rank_universe_identity_20261005.json
lib/research/harvest/universe_securities.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~112/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bh-6"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~112/bh6_ict_source.out</invocation><expect>RECORD OK</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; your next row id is `AMGT_HARVST-Z-W112-S1`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~112/AMGT_HARVST.TO-HVST-bh-6.what-ict-us-equity-is.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bh-6.what-ict-us-equity-is`. Pin every artifact row to the commit that carries it.
- Run every script from the repo root of YOUR worktree as `PYTHONPATH=. python <file>`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~Z` msg 31486, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round60.md` @3b19f962e0. Decomposition section 75.
- R6: "The record states what that security is and where its key came from. If no source names it, it leaves the list by a cell,
  not by hand." A removal, if the record calls for one, is a cell of the next round.
- Slot ~112's queue, after `bh-2`. **Checks dry-run at the base:** AC1 base FAIL as expected (no such file).

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>issued</status>
<round>61</round>
<slot>~112</slot>
<fabric>site-z</fabric>
