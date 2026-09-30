# AMGT_RESAPP task order -- `AMGT-ac-4` -- EVERY FILINGS/V1 KEY GOES THROUGH SLASH_SAFE_KEY, AND THE STORE DOCSTRING (AMENDMENT 1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ac-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~192</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- code and text only; the checks use a stub client and no AWS call.
comp-adversary: RUN by the issuer at the cut -- AC1 plants BP/_LN and NG/_LN keys and a stubbed reverify read (base: all raw), with a slash-free control that must stay byte-identical; AC2 reads the docstring's text and a dynamic probe (base: 1 stale clause).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AMGT-ac-4` (round 53, decomposition s.61; AMENDMENT 1 per CTO msg 27175)

**(1) The filings/v1 key.** The estate's rule (CTO ruling @c9081e03d6) is that every S3 path built from a `security_key` goes through
`lib.research.identity.crosswalk.slash_safe_key` (`BP/_LN_Equity` -> `BP-SLASH-_LN_Equity`; a slash-free key is unchanged). CORPUS z-4 routed
most writers and readers, but `lib/research/filings/fetch.py` `pool_key(security_key, accession, suffix="source")` (`:472`) still builds
`filings/v1/<security_key>/<accession or UNRESOLVED-SOURCE>.<suffix>.json` with the RAW key, and four callers inherit it: `analyze.py:1345`,
`:1470` (the `reverify_stored_thesis_driver` read), `:1636` (the `.analysis.json` write in `write_outputs`), and `filings/batch.py:478`.
**Build:** `pool_key` builds its path segment with `crosswalk.slash_safe_key(security_key)`; the four callers then read and write encoded
keys with no change of their own (change a caller only if it builds a filings/v1 path itself). A slash-free key's path is byte-identical
to today's. Tests: BP/_LN encodes, a slash-free key is unchanged.

**(2) The docstring.** A docstring in `lib/research/api/scoped_amgt.py` (near `:2175`) says "... never `lib.research.harvest.store` ...
and never `lib.opal_naming` ...: the first is unavailable in the deployed package." The last clause is false: `harvest.store` is packaged and
the /thesis path imports it (`corpus.dossier` -> `harvest.store`). Correct that clause, text only: this reader does not import
harvest.store (why, if the reason still holds), and harvest.store is packaged and imported on the /thesis path.

## 2. BOUNDS

1. `fetch.pool_key` (and a caller only where it builds a filings/v1 path itself), that one docstring's wording in `scoped_amgt.py`, and new
   test files. No S3 write, no live reverify. Standing: no install, no push, no promote, no deploy, no vendor call. REFUSE, do not rescue.
2. Python from the repo root with `PYTHONPATH="$(pwd)"`.

## 3. SURFACES

<paths>
lib/research/filings/fetch.py
lib/research/filings/analyze.py
lib/research/filings/batch.py
lib/research/filings/tests/
lib/research/api/scoped_amgt.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~192/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ac-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round53/checks/ac_4_fetch.py; echo "exit=$?"</invocation><expect>(a) BP-SLASH-/NG-SLASH- keys; (b) AMD_US_Equity unchanged; (c) the read path requests filings/v1/BP-SLASH-_LN_Equity/...; EVERY FILINGS/V1 KEY GOES THROUGH SLASH_SAFE_KEY: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ac-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round53/checks/ac_4_store.py; echo "exit=$?"</invocation><expect>claims that store is unavailable in the deployed package: 0; dynamic: True; THE ADAPTER'S TEXT STATES HARVEST.STORE IS PACKAGED: YES -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ac-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" timeout 115 python -m pytest lib/research/filings/tests -q; echo "exit=$?"</invocation><expect>N passed and 0 failed, N &gt; 127 (plus your new tests) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~192/AMGT_RESAPP.TO-AMGT-ac-4.the-store-docstring.proof_of_spec.json`. Report once: what you changed (and any caller you touched and why), the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-52 analysis item 4 (Z-S315) + AMENDMENT 1 (CTO msg 27175, on the ac-3 reader census, msg 27169: fetch.pool_key is
the one reader class still on the raw path). Base: AC1 FAIL (plant and read path raw; control unchanged), AC2 FAIL (1 clause), AC3 PASS 127.
ac-3's pair is signed only after ac-4 drains and its reader census reads 0 raw-path readers. The file name keeps its original slug.

<status>complete</status>
**AMENDMENT 1 (`2.0.0_SA_COO~Z`, 2026-09-30 ~13:2xZ, before spawn):** CTO msg 27175 -- ac-4 becomes the filings/v1 reader cell: route `fetch.pool_key` through `crosswalk.slash_safe_key` (all four raw callers), keep the docstring fix; class worker (was worker-light); AC1 `ac_4_fetch.py` added (the docstring check is AC2).
<round>53</round>
<slot>~192</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
