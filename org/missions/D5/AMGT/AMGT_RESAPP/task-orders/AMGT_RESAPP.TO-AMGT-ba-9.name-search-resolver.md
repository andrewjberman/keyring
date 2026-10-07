# AMGT_RESAPP task order -- `AMGT-ba-9` -- THE NAME SEARCH: A TYPED NAME OR TICKER RESOLVES TO CANDIDATES, NEVER TREATED AS A KEY (ROW Z-S228)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ba-9</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~275</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a pure resolver and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- reads the crosswalk the function already loads; no new read path.
comp-adversary: RUN by the issuer at the cut -- `crosswalk.resolve("Lenovo")` reads UNRESOLVED while `resolve("992 HK")` reads 992_HK_Equity (237 records, 1,044 indexed forms, 0 of them a company name). r77_ba9 AC1 and AC2 FAIL at the base (no module, no test file).
EGRESS CLASS, declared: NONE. No vendor, SEC or model call.
</preflight>

**Your worktree:** `C:/tmp/r77-275` (branch `wk-AMGT_RESAPP-275`, cut from the issuance commit with `--portal-ref 13509c52`, the portal DEV head at the cut (the api suite reads a portal fixture)). Work and commit only there. Start every shell call with `cd /c/tmp/r77-275`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ba-9` (round 77, decomposition s.85)

Row Z-S228, ruled by the CTO (`ledger/CTO_ADJUDICATION_REMEDIATION_ROWS_ROUND76.md` @4a89bef967, section E). Today there is no
name search: the page passes the typed string as a key and the server does an exact lookup, so "Lenovo" can never match. The
contract: **`GET /api/scoped/amgt/resolve?q=` over the crosswalk. An exact key passes through. A name or ticker returns
candidates `{security_key, name, ticker}`. No match returns a reason. The page search calls it and never treats a typed name as a
key.**

Build the resolver as a NEW module, `lib/research/api/name_search.py`, exporting ONE function:

`resolve_query(q)` returns `{query, status, security_key, candidates, reason}`.
1. **Exact.** If `lib.research.identity.crosswalk.resolve(q)` returns a security key, answer `status: "exact"` with that
   `security_key`, and `candidates` holding that one record. Every stored form keeps working exactly as it does today.
2. **Candidates.** Otherwise match `q`, case-insensitively and ignoring surrounding space, against each keyed record's company
   name and ticker. The name is the research folder name the record already carries (`source_row.folder`, such as
   "Lenovo 992 HK"); the ticker is its `display_ticker`. A record matches when `q` is a whole word, or the start of a word, of
   its name, or equals its ticker root. Answer `status: "candidates"`, `security_key: None`, and one candidate per matching
   record: `{security_key, name, ticker}`, all three non-empty, ordered by name. Cap the list at 20 and say so in `reason` when
   it was cut.
3. **None.** An empty query, or one that matches nothing, answers `status: "none"`, `candidates: []` and a plain `reason` (for
   example "no company we cover matches 'zzqx'"). Never a guessed key.
4. A query shorter than 2 characters that is not an exact form is `none` with its reason (a one-letter search lists nothing).

Plant tests in `lib/research/api/tests/test_name_search.py`: exact, name, lower-case name, ticker, no match, empty, the cap.

**You do NOT edit `lib/research/api/scoped_amgt.py` or the gateway route list.** The route `GET /api/scoped/amgt/resolve` is
mounted by the round's adapter cell, AMGT-ba-11. Your report names the hookup: the function, the query parameter, and the status
code the route should answer for each `status` (200 for all three is the default; say if you built otherwise).

Run `lib/research/api/tests/` before your commit and report its last line. If one api test fails only because it reads a portal function absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W275-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. `lib/research/identity/crosswalk.py` is READ, never edited: no new alias is added to the crosswalk, and `resolve()` keeps its answers.
3. Any reason you serve is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/name_search.py
lib/research/api/tests/test_name_search.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~275/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ba-9"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba9.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>"992 HK" and "992_HK_Equity" pass through as exact; "Lenovo" and "lenovo" list 992_HK_Equity with a name and a ticker; no match and an empty query read a plain reason; every keyed record's own key passes through (N of N); C1-C4 PASS; R77 BA9 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ba-9"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba9.py" --crit AC2 --where local; echo "exit=$?"</invocation><expect>every plant case in test_name_search.py passes; R77 BA9 AC2 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~275 <0.9.0_WK_AMGT_RESAPP~275@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~275/AMGT_RESAPP.TO-AMGT-ba-9.name-search-resolver.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the api suite's last line;
- the hookup the adapter cell needs (function, query parameter, status codes);
- how many of the keyed records carry a usable name and a ticker, and any that do not;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-76 analysis item 10 (the name-search route); CTO adjudication @4a89bef967 section E, row Z-S228. The route mount and the gateway route entry are AMGT-ba-11's; the page search box is DSGN_AMGTV1's. Checks dry-run at the base: ba-9 AC1 base FAIL as expected, AC2 base FAIL as expected.

<status>pending</status>
<round>77</round>
<slot>0.9.0_WK_AMGT_RESAPP~275</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
