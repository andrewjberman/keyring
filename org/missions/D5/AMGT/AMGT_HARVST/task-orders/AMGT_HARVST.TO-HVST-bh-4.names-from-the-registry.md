# AMGT_HARVST task order -- `HVST-bh-4` -- ROUND 61 (`1.0.0_SA_CTO~Z` msg 31486, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round60.md` @3b19f962e0): A SECURITY THE LIST KNOWS ONLY BY ITS KEY TAKES ITS NAME FROM THE IDENTITY REGISTRY -- THREE TODAY: CAT, CSL, KEYENCE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bh-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~110</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and plants, plus a READ-ONLY census (S3 GET of the pool universe and the silver article parts through the served iterator). NO put, NO delete, NO gold or silver build, NO vendor or publisher host, NO collector or backfill_driver. `.runtime` is not read. Two collection legs are LIVE on the shared tree: touch nothing outside your worktree.
comp-adversary: RUN at L5 -- the adversary is a changed output for a security the rule does not name, a test with no negative control, a rule loosened to meet the census, a second list where the cell says one, or a gold build.
</preflight>

## 0. THE CELL

`lib/research/harvest/universe_securities.py` builds the gold securities list. A security's company name comes from the pool
entry, else from the collector's identity map (`load_legal_names`, `_company_name`, `_entry_name_aliases`), else it is the
security key itself. Three of the 242 securities end on the key: `CAT_US_Equity`, `CSL_AU_Equity`, `6861_JP_Equity`. The
first two match through their exact-case ticker form alone; the third matches nothing.

`lib/research/identity/registrations.json` (`registrations`, 72 entries) carries all three by `security_key` with
`identity.name`: `CATERPILLAR INC`, `CSL LTD`, `KEYENCE CORP`.

## 1. THE BUILD (LOCAL)

1. **The join** (`universe_securities.py`). Where a security has no pool name AND no identity-map name, its company name is
   `identity.name` of the registry entry with the same `security_key`. Order: pool, identity map, registry, key. The registry
   is read AS A FILE, once, beside `load_legal_names` and in its style: a missing or unreadable file RAISES with the path
   named; an entry with no key or an empty name is counted, not joined.
2. The name is taken as written and goes through the SAME alias path every other company name takes (suffix forms, tail
   rules, `_usable_alias`, the rule that an all-caps name equal to the security's exact-case ticker form is carried by that
   form). Add no special case for the three keys.
3. The build summary gains `names_from_registry`: a list of `{security_key, name}`, and the loader's counts.
4. A security that has a pool name or an identity-map name returns a dict byte-equal to today's.
5. No vendor call. `lib/research/identity/registrations.json` is read, never written.
6. **Plants** `lib/research/harvest/tests/test_bh4_registry_names.py` (no network):
   - (i) a key-only security in a fixture pool document, with a registry fixture naming it `KEYENCE CORP`, gets that company
     and an alias set containing `KEYENCE`;
   - (ii) THE NEGATIVE CONTROL: the same security with the registry fixture lacking its key keeps the key as its name, as today;
   - (iii) a security with a pool name is byte-equal with and without the registry;
   - (iv) the identity map wins over the registry when both carry the key;
   - (v) a registry entry with an empty name is not joined and is counted;
   - (vi) a missing registry file raises with the path in the message;
   - (vii) from the REAL registry file: `CAT_US_Equity`, `CSL_AU_Equity`, `6861_JP_Equity` each resolve to the three names
     above, and what `CSL LTD` yields as name aliases beside the ticker form `CSL` is asserted as the code gives it and stated
     in your report.
7. **The census** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~110/bh4_census.py`: BEFORE = `build()` with the registry join switched off
   (a parameter or a patched loader, stated in the file); AFTER = `build()` as you leave it. Counts from the REAL
   `pg._security_mentions` over every latest silver article (`pg._iter_latest_articles()`), progress every 500 articles:
   - `DENOMINATOR: securities <S>, silver articles <N>`;
   - `NAMES FROM REGISTRY: <k>` and each `{security_key, name, aliases}`;
   - per named security: `pairs before <p0> after <p1> gained <g>; mention_count before <m0> after <m1>`;
   - `OTHER SECURITIES CHANGED: <c> of <S>`;
   - last line `CENSUS OK` only if N > 0, k == 3, no named security lost a pair, and OTHER SECURITIES CHANGED is 0;
     otherwise `CENSUS FAIL` and the failing line. Write the output as `bh4_census.out`.
8. If the S3 read is refused or returns 0 articles: BLOCKING row, stop on AC2. Build no gold. Do not regenerate any list
   file under `deliverables/2.0.0_SA_COO_H/`.

Change an existing test assertion only where this cell's rule is the reason, and list each in your report.

<paths>
lib/research/harvest/universe_securities.py
lib/research/harvest/publication_gold.py
lib/research/identity/registrations.json
lib/research/harvest/tests/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~110/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bh-4"><invocation>python -m pytest lib/research/harvest/tests/test_bh4_registry_names.py -rA --tb=line -p no:cacheprovider</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bh-4"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~110/bh4_census.out</invocation><expect>CENSUS OK</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-bh-4"><invocation>python -m pytest lib/research/harvest lib/opal_data_harvest/test_az1_alias_set.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; your next row id is `AMGT_HARVST-Z-W110-S1`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~110/AMGT_HARVST.TO-HVST-bh-4.names-from-the-registry.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bh-4.names-from-the-registry`. Pin every artifact row to the commit that carries it.
- Run every script from the repo root of YOUR worktree as `PYTHONPATH=. python <file>`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~Z` msg 31486, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round60.md` @3b19f962e0. Decomposition section 75.
- R4: "The built list takes a security's name from `lib/research/identity/registrations.json` where the gold list holds only a
  key. No vendor call."
- Slot ~110's queue: `bh-4`, `bh-5`, `bh-3`, in that order (all three write `universe_securities.py`; `bh-3` needs CSL's name).
  `publication_gold.py` is in `<paths>` for the census import only; this cell does not change it.
- **Checks dry-run at the base:** AC1 base FAIL as expected (the test is absent); AC2 base FAIL as expected (no such file);
  AC3 base PASS as expected (419 passed).

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<round>61</round>
<slot>~110</slot>
<fabric>site-z</fabric>
