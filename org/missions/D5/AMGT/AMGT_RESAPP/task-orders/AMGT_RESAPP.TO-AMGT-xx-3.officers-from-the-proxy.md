# AMGT_RESAPP task order -- `AMGT-xx-3` -- OFFICERS FROM THE PROXY WHEN THE ANNUAL REPORT'S OFFICER SECTION POINTS ELSEWHERE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-xx-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~175</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- local reads; nothing served, nothing written to AWS.
comp-adversary: RUN by the issuer at the cut -- AC1 proves the reader on the walked no-officer name against the real proxy; AC2 is the census with every denominator printed and a reason on every name that does not gain.
EGRESS CLASS, declared: EDGAR (data.sec.gov, www.sec.gov) through the EXISTING lib/research/filings/fetch.py path and its SEC User-Agent -- read-only, no new vendor. Authorized for this order at its spawn (see the record face).
</preflight>

## 1. THE CELL -- `AMGT-xx-3` (round 49, decomposition s.57)

Exec Management's officer list comes from the persisted annual report's OFFICER SECTION: `lib/research/management/roster.py`
parses Item 10 of a 10-K / Item 6 of a 20-F in seven declared shapes. When the section points elsewhere ("incorporated by
reference" to the proxy statement), roster marks it UNRESOLVED-SOURCE with `section_refers_to` = the filing's own pointer sentence
(`_find_reference_pointer`, `_find_exec_officer_pointer`; HAL, INTU and CAT are named in its header). The page then shows no
officers. The walked case is `INTU_US_Equity`: its 10-K (accession 0000896878-26-000037) lists no officers.

**Build a NEW module `lib/research/management/proxy_officers.py`:**
- `officers_from_proxy(security_key) -> dict` -- for a name whose roster is UNRESOLVED-SOURCE with `section_refers_to`, read the
  company's LATEST proxy statement (form `DEF 14A`) through the SAME filings path already in use
  (`lib/research/filings/fetch.py`: `latest_filing`, `http_get`, `html_to_text`, the SEC User-Agent it carries -- import them; do
  not copy or edit that file), find its executive-officer section, and parse officers with roster's own shape parsers where one
  fits (import them; a title is never a name -- roster's `_is_title_only` rule). Returns
  `{"status": "SERVED" | "UNRESOLVED-SOURCE", "officers": [{"name", "role", ...}], "source": {"form": "DEF 14A", "accession",
  "url", "filing_date", "retrieved_at", "document_sha256"}, "reason"}` -- UNRESOLVED-SOURCE always carries a reason (no proxy, no
  officer section, no declared shape), never an empty list read as "no officers".
- `census() -> dict` -- over the identified research-library names (the same population FWD-30 uses: `lib.research.corpus.library`
  folders, `crosswalk.harvester_key` -> `scoped_amgt.resolve_identity`): `identified`, `pointer` (names whose persisted officer
  section points elsewhere), `gained` (pointer names whose proxy read is SERVED) and `rows` (one per pointer name:
  `security_key`, `status`, `officers` count, `reason`).
- A module CLI: `python -m lib.research.management.proxy_officers --census` prints the census line and rows.
- Tests (no network: a stubbed fetch over a small proxy-text fixture you write from the real INTU proxy's section) pinning the
  SERVED parse, a proxy with no officer section, and a title-only candidate refused.

Nothing is served or persisted by this order; serving is a later round's, under a pair.

## 2. BOUNDS

1. Write only the new module and its tests. `roster.py`, `fetch.py`, the scoped API and the page are READ-ONLY.
2. EDGAR reads only through fetch.py's functions; honour its User-Agent; no other host. No S3 write, no deploy.
3. Standing: no install, no push, no promote, no vendor call. REFUSE, do not rescue.
4. Python from the repo root with `PYTHONPATH="$(pwd)"`.

## 3. SURFACES

<paths>
lib/research/management/proxy_officers.py
lib/research/management/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~175/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; the persisted filing objects roster reads; EDGAR through fetch.py.

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-xx-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round49/checks/xx-3.AC1.py; echo "exit=$?"</invocation><expect>status SERVED, form DEF 14A, an accession, officers N (N &gt;= 3), malformed 0, OFFICERS FROM THE PROXY ON THE WALKED NAME: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-xx-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round49/checks/xx-3.AC2.py; echo "exit=$?"</invocation><expect>census: identified I; officer section points elsewhere P; gain officers from the proxy G of P (0 &lt; G &lt;= P &lt;= I), THE CENSUS PRINTS ITS DENOMINATORS: YES -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 the built reader on the walked name against the real proxy; AC2 the census with its denominators.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~175/AMGT_RESAPP.TO-AMGT-xx-3.officers-from-the-proxy.proof_of_spec.json`. Report once: what you built and where, the census counts, the EDGAR requests made (count), the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-48 analysis s.4 row 3 (@1dfd5c0970; DSGN_AMGTV1 round-4 analysis @177c576c80 s.2 ruling 5). Base: AC1
FAIL, AC2 FAIL (no proxy_officers module). **SPAWN HELD at the cut:** EDGAR is egress off Opal infrastructure (CLAUDE.md Agent
Autonomy exclusion); fetch.py's own authority is Andrew-direct 2026-09-15 ~05:42Z, a session grant. The call is put to
1.0.0_SA_CTO~Z (its arm pitches a reserved call to 3.0.0_SA_CVO~Z). On a GRANT the issuer spawns ~175 on this face unchanged and
records the grant here; on a REFUSAL the issuer amends this order to a no-network cut (fixture-only) and says so.

<status>pending</status>
<round>49</round>
<slot>~175</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
