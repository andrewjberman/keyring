# AMGT_HARVST task order -- `HVST-be-1` -- ROUND 58 (`1.0.0_SA_CTO~Z` msg 31008; signing read @b787ec1026): THE LEGAL NAME IS ALWAYS AN ALIAS, A TAILED POOL NAME NEVER IS, `AI` IS REFUSED AS A TICKER FORM -- LIST REPAIR, NO REBUILD

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-be-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~107</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code, plants and a list comparison. One READ-ONLY S3 GET of the pool universe through `universe_securities.build()`. NO put, NO delete, NO gold or silver build, NO read of silver articles, NO vendor or publisher host, NO collector or backfill_driver. `.runtime` is not read. Collection legs are LIVE on the shared tree: touch nothing outside your worktree.
comp-adversary: RUN at L5 -- the adversary is a legal name dropped when the pool has a name, a tail rule that also refuses a clean pool name (`Hon Hai`, `Air Liquide`), a tail rule written as a list of the five known cases, a name derived from a key or ticker, a ticker form refused with no census entry, or a gold build.
</preflight>

## 0. THE CELL

`lib/research/harvest/universe_securities.py` `securities_from_universe(document, sa_symbols, rule, legal_names)` builds the
`securities` list the gold builders take. Two earlier cells changed it: it takes a legal name from the collector's identity
record when the pool entry has none (`legal_names`, default path read by `build()`), and it carries gold brands and an
anchored brand. The served gold was built from a hand-carried file instead:
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round33/securities.universe.r33.json` (212 securities).

A dry run of a gold build with the list as it stands, against the served gold
(`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round57/GOLD_REBUILD8_SIGNING_READ.md`, with
`securities.universe.r57.json` = the list as it stands, 242 securities), found:

1. **140 served article pairs LOST over 5 securities**, because the pool's own name wins today and is a research-folder name
   with a ticker in it:

   | security | served aliases | aliases as the list stands | identity record `company.value` |
   |---|---|---|---|
   | UNVGY_US_Equity | Universal Music Group NV, Universal Music Group, Universal Music | Universal Music Group UMG NL | Universal Music Group NV |
   | SHOP_CN_Equity | Shopify | Shopify SHOP CA | Shopify |
   | AMD_US_Equity | Advanced Micro Devices Inc, Advanced Micro Devices | AMD Advanced Micro Devices | Advanced Micro Devices Inc |
   | BZLFY_US_Equity | Bunzl PLC, Bunzl | Bunzl BNZL GB | Bunzl PLC |
   | MER_PM_Equity | Manila Electric | Manila MER PER | Manila Electric |

   `BP_US_Equity` is the same class: served `["BP PLC"]`, as the list stands company `BP` with an EMPTY alias set.
   Measured on the two files: 32 of the 212 common securities have a served alias that the list as it stands does not carry
   (`Mastercard Inc`, `Netflix Inc`, `Visa Inc`, `Alphabet Inc` for GOOGL, `Eli Lilly & Co` among them).
2. **A wrong gain: `AI_FP_Equity` (Air Liquide) +3,543 pairs.** The list gives it the exact-case ticker form `AI`. The served
   file carries no ticker form for it.
3. **43 securities carry an exact-case ticker form the served file does not** (`AI`, `BE`, `CAT`, `ED`, `ML`, `DG`, `SAN`,
   `RIO`, `ICT`, `SHOP`, `JD`, `PWR` among them). Each is to be read on a census before it serves; that census is the
   issuer's dry run, not this cell.

The ruling this cell lands:
- **R1. The identity legal name is ALWAYS in a security's alias set and is never replaced.** Where the identity record has
  the security, its `company.value` (after the existing slash-tail step) and that name's existing derived forms are aliases,
  whether or not the pool entry has a name.
- **R2. A pool name with a ticker or exchange tail is NOT added as an alias.** A pool name with no such decoration is still
  an alias, beside the legal name (`Hon Hai`, `Air Liquide`).
- **R3. `AI` joins `ticker_refusals`** in `lib/research/harvest/whole_brand_aliases.json`, with its census.
- Nothing is derived from a key or a ticker. NO gold is built.

## 1. THE BUILD (LOCAL)

1. **R1 and R2** (`universe_securities.py`, both loops that read the name).
   - `company` is the legal name when the identity record has the security; else the pool name; else the key, as today.
   - The alias set is the legal name's forms (through the module's existing `_entry_aliases` path) PLUS the pool name's forms
     when the pool name is not decorated, no duplicates (case-insensitive), legal-name forms first.
   - **Decorated** is ONE stated rule, not a list of cases: after the module's own `strip_ticker_tail`, the pool name still
     carries (a) a token equal to the security's own ticker root or key root as a standalone upper-case token anywhere in the
     name (`AMD Advanced Micro Devices`), or (b) a trailing run `<code> <CC>` where `<CC>` is a two-letter upper-case
     exchange or country code and `<code>` is an upper-case or alphanumeric ticker-like token (`UMG NL`, `SHOP CA`,
     `BNZL GB`, `MER PER` is three letters: read the pool's real tails and state the rule that covers what is there). State
     the rule in the docstring, with what it does NOT catch.
   - A security with NO identity record keeps its pool name as today even when decorated, and is listed.
   - `legal_names=None` still reproduces the pre-`bc-1` output byte for byte (the existing difference control stays green).
   - Summary gains: `pool_name_kept_as_alias` (count), `pool_name_refused_decorated` (count and `{security_key, pool_name,
     reason}` each), `decorated_but_no_identity_record` (keys). The existing counts keep their meaning or are renamed with
     the change stated in your report.
2. **R3** (`whole_brand_aliases.json`): one new `ticker_refusals` entry, `{"ticker": "AI", "census": "..."}`, citing
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round57/gold_rebuild8.signing.out`: `AI_FP_Equity` served 38
   pairs, built 3,581, +3,543 on the exact-case form `AI` (the word for artificial intelligence). Keep the file ASCII.
3. **Plants** in `lib/research/harvest/tests/test_be1_legal_name_always.py` (no network):
   - (i) pool name `Universal Music Group UMG NL` + legal `Universal Music Group NV`: aliases carry the legal name and
     `Universal Music Group`, and carry no alias containing `UMG`;
   - (ii) pool `AMD Advanced Micro Devices`, ticker `AMD US`, legal `Advanced Micro Devices Inc`: aliases carry both legal
     forms and no alias starting `AMD `;
   - (iii) pool `Shopify SHOP CA` + legal `Shopify`: aliases are exactly `["Shopify"]`;
   - (iv) a CLEAN pool name is kept beside the legal name: pool `Mastercard`, legal `Mastercard Inc` gives both, legal first;
     pool `Hon Hai` with legal `Hon Hai Precision Industry Co Ltd` keeps `Hon Hai`;
   - (v) the legal name is never replaced: pool `Apple Computer` (clean) + legal `Apple Inc` carries `Apple Inc`;
   - (vi) no identity record + a decorated pool name: kept, and counted in `decorated_but_no_identity_record`;
   - (vii) the mutant: with R2 off, (i) carries an alias containing `UMG` -- assert it, so the control is shown to bite;
   - (viii) `AI` is refused: an entry with ticker `AI FP` carries no ticker form, and the refusal is counted in
     `ticker_forms_refused_by_reason["refusal_list"]`; a ticker `AIG US` still gets `AIG`;
   - (ix) `legal_names=None` equals the pre-`bc-1` literal already kept in `test_bc1_legal_names.py`.
4. **The list comparison** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~107/be1_list_compare.py`:
   `build()` as you leave it, against the served file `round33/securities.universe.r33.json` and against
   `round57/securities.universe.r57.json`. Print:
   - `DENOMINATOR: served <212>, before <242>, after <n>; common with served <c>`;
   - `SERVED ALIAS MISSING: before <b> of <c> securities, after <a> of <c>`, then each security still missing one after, with
     the alias and ONE reason from a closed set you state (e.g. `slash tail stripped`, `receipt tail`, `hand alias with no
     source`, `legal name cut in the identity record`);
   - `THE SIX: ` one line each for UNVGY, SHOP_CN, AMD, BZLFY, MER_PM and BP_US: served aliases, after aliases, missing;
   - `POOL NAMES REFUSED AS DECORATED: <n>` and each `{security_key, pool_name}`; `POOL NAMES KEPT: <n>`;
   - `NEW EXACT-CASE TICKER FORMS vs served: before <43> after <m>` and the list after;
   - `ALIAS SETS CHANGED vs before: <k> of <n>`, each key with before and after;
   - print `LIST OK` as the LAST line only if ALL hold: after == before in security count; each of THE SIX carries every
     served alias except one whose reason is in your closed set and is printed; no after alias matches your own decorated
     rule; no security carries the ticker form `AI`; every security that has an identity record carries that record's name
     (after the slash-tail step) among its aliases. Otherwise `LIST FAIL` and the failing line.
   - Write the whole output beside it as `be1_list_compare.out`, and the after list as `securities.universe.r58.json`.
5. If the bar is missed, do not add a brand, a hand alias or a case to the rule: report the failing line.
6. You build NO gold, read NO silver article, and write NOTHING to S3.

Worktree: given in your spawn prompt (cut from CLOUD at the issuance commit).

<paths>
lib/research/harvest/universe_securities.py
lib/research/harvest/whole_brand_aliases.json
lib/research/harvest/tests/test_be1_legal_name_always.py
lib/research/harvest/tests/test_bc1_legal_names.py
lib/research/harvest/tests/test_bd1_gold_brands_and_anchor.py
lib/research/harvest/tests/test_alias_rule_round18.py
lib/research/harvest/tests/test_universe_securities.py
lib/opal_data_harvest/test_az1_alias_set.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~107/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You READ, and never write: the two list files and the signing read named in section 0, `lib/opal_data_harvest/config.json`,
the identity record `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round47/rank_universe_identity_20261005.json`,
and `lib/research/harvest/publication_gold.py`. Change an existing test assertion only where this cell's rule is the reason,
and list each in your report.

## 2. PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-be-1"><invocation>python -m pytest lib/research/harvest/tests/test_be1_legal_name_always.py -rA --tb=line -p no:cacheprovider</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-be-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~107/be1_list_compare.out</invocation><expect>LIST OK</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-be-1"><invocation>python -m pytest lib/research/harvest lib/opal_data_harvest/test_az1_alias_set.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; on this fabric a worker row id reads
  `AMGT_HARVST-Z-W107-S<k>`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~107/AMGT_HARVST.TO-HVST-be-1.legal-name-always-and-ticker-forms-read.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-be-1.legal-name-always-and-ticker-forms-read`. Pin every artifact row to the commit that
  carries it.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~Z` msg 31008 (2026-10-07 13:54Z): "1: the identity legal name is ALWAYS in a security's alias set
  and is never replaced; a pool name with a ticker or exchange tail is not added as an alias. 2: 'AI' joins ticker_refusals,
  and every NEW ticker form is read: the re-run prints pairs gained per new form. 3: the re-run's bar is 0 pairs lost AND
  every gained pair assigned to one cause (a new security, a new alias, silver growth), summing to the total." Then a CVO
  grade of 30 pairs from the largest non-silver-growth gainers, bar 29 of 30; then the rebuild's pair. Signing read
  @b787ec1026. Decomposition section 72.
- **This cell reverses this seat's `bc-1` ruling (a)** ("the pool's own name wins over the identity record"), which the dry
  run showed costs 140 served pairs. No gate limb graded that ruling or this reversal.
- **Split of the CTO's three rules:** rules 1 and 2a (the list) are this cell. Rule 2b (pairs gained per new ticker form) and
  rule 3 (0 lost; every gained pair assigned to one cause) need a gold build through the capturing client and are the
  ISSUER's re-run of `round57/gold_rebuild8.signing.py`, extended, at this cell's close: it is the close run. The worker
  reads no silver.
- **Checks dry-run at the base before the cut:** AC1 base FAIL as expected (the test is absent); AC2 base FAIL as expected
  (no such file); AC3 base PASS as expected (397 passed).
- Known at the cut and left for the re-run to measure: `Universal Music` (a hand alias in the served file with no source)
  will be missing after this cell; if any served pair rests on it alone, the re-run shows it lost and it needs a brand entry
  on its own census.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<round>58</round>
<slot>~107</slot>
<fabric>site-z</fabric>
