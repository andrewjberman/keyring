# AMGT_CORPUS task order -- `CRPS-l-1` -- ROUND 10: a served case's unit carries its claim -- the team's symbol as written, and a currency only when the symbol names exactly one ISO code that is the listing's

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-l-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface; the served rewrite is the issuer's drain act.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads only in this cell.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 10, SECOND order on this slot (you completed `CRPS-l-3` on the same
file). Serves **FWD-12** (a value must carry its claim).

## 1. THE CELL -- `CRPS-l-1`

**Where this came from.** Each served case (`fields.cases.{upside,base,downside}` in `lib/research/corpus/dossier.py`) carries
`unit`: the currency symbol the team's table values carry, or null. Round 9's census: `unit_carried 10` -- AZN_LN_Equity
U+00A3 (pound), ML U+20AC (euro), `$` on BP, CPA, ORA, SAP, SHOP, SPOT, TTE, UNVGY. The CVO measured that on 5 of 8 names
read the symbol is NOT the listing's currency: `$` on three EUR listings and one CAD listing; U+00A3 on a GBp (pence)
listing, a 100x unit step. `$` cannot tell USD from CAD, and whether the EUR names carry real dollar figures is not decidable
from the pack. The listing's currency is on the name's stored model block, which `build()` already reads
(`_model_block_read`; the block carries a `currencies` field -- read it to find the quote currency's key).

**RULED -- what you build (the CTO's round-9 analysis, ruling 1 -- "A VALUE MUST CARRY ITS CLAIM"):**
1. Each served case carries `unit_as_written`: the team's symbol, verbatim (replacing `unit`; keep no second copy).
2. Each served case carries `currency` (an ISO 4217 code) set ONLY when the symbol maps to exactly ONE ISO code AND that code
   equals the listing's currency (e.g. U+20AC -> EUR on a EUR listing). Otherwise `currency: null` and `currency_basis`
   states why, one of: `"not stated in the pack"` (no symbol), `"symbol is ambiguous across currencies"` (e.g. `$`, U+00A5),
   `"symbol's currency differs from the listing"` (e.g. U+00A3 = GBP on a GBp listing), `"listing currency not on the block"`.
   When `currency` is set, `currency_basis` is `"symbol maps to one ISO code equal to the listing"`.
3. Nothing converts and nothing is inferred from the listing: the listing is used only to REFUSE a currency.
4. Keep the mapping table small and in code as `\u` escapes (pure ASCII source); name every symbol you map.
5. The census (`python -m lib.research.corpus.dossier --case-census`) keeps its line and APPENDS two columns, final line
   EXACTLY: `case_census names <N> slots <3N> body <B> heading_only <H> absent <A> sum <S> ordering_held <h> ordering_violated <v> ordering_na <n> unit_carried <u> currency_set <c> currency_null <z>`
   where `currency_set` + `currency_null` = `unit_carried` + (names with a readable table and no symbol) -- i.e. every name
   with served cases is in exactly one of the two.
6. `lib/research/corpus/tests/test_dossier_case_unit.py` (new): euro on a EUR listing -> EUR; `$` on a USD listing -> null,
   ambiguous; pound on a GBp listing -> null, differs; no symbol -> null, not stated; no listing currency -> null.

## 3. SURFACES

<paths>
lib/research/corpus/dossier.py
lib/research/corpus/tests/test_dossier_case_unit.py
lib/research/corpus/tests/test_dossier_case_table.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-l-1.case-unit-carries-its-claim.md
</paths>

READ-ONLY: every other file, every S3 object. Scratch `.scratch/l1/`.

## 4. BOUNDS
- Pure ASCII source, LF, Python 3.9-compatible. NO S3 write: never run `dossier --write`.
- **Bump `METHOD_VERSION` to `"amgt-corpus-dossier/3"`** (this chain changes what a case serves but not the dossier's
  `inputs`; `write_one` writes nothing when the stored method AND inputs are unchanged, so without the bump the issuer's
  rewrite would write 0 on every name). `read_dossier` already prefers the current method version.
- `test_dossier_case_table.py` may change only where it pins the old `unit` key or the old census line; name each such test.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W1-S<k>`,
  `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 600`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-l-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round10/l1_AC1.sh</invocation><expect>(?m)^\d+ passed(, \d+ subtests passed)? in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-l-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round10/l1_AC2.sh</invocation><expect>case_census names ([1-9]\d*) slots \d+ body [1-9]\d* heading_only 0 absent \d+ sum \d+ ordering_held \d+ ordering_violated \d+ ordering_na \d+ unit_carried \d+ currency_set \d+ currency_null \d+</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-l-1" judgment="true"/>
</proof_of_spec>

- AC1 the built behaviour; AC2 the seam probe over every resolved name's real extraction and block. AC3 (JUDGMENT, graded by
  `3.0.0_SA_CVO~Z` at L9 on the served rewrite, never by you): *does every served case's unit say only what the pack states,
  with a currency only where the pack and the listing agree on exactly one?* Record it under `UNVERIFIABLE-BY-INSTRUMENT`
  with a `status_reason` naming the CVO.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-l-1.case-unit-carries-its-claim.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every mechanical criterion passes; commit the files you changed plus the instance.
4. Report ONCE: AC2's line; per name with a unit: symbol, listing currency, `currency`, `currency_basis`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-9 analysis s.2 ruling 1 + s.4 item 1 @`abfad1355c`. Checks dry-run at the base: AC1 FAIL (no tests
ran); AC2 FAIL (base line ends at `unit_carried 10`). The drain: ONE pair for chain A's rewrite (l-3 + l-1); `METHOD_VERSION` /3 (ruled at
the cut: the chain moves no input, so without the bump `write_one`'s no-op would write 0 on every name) -> every name writes.

<risk>SERVED</risk>
<status>pending</status>
<round>10</round>
<slot>~1</slot>
<fabric>site-z</fabric>
