# AMGT_RESAPP task order -- `AMGT-jj-3` -- THE NAME LIST CARRIES A MEASURED ISSUER CIK, AND A TYPED NAME WHOSE LISTINGS SHARE ONE ISSUER RESOLVES TO THE COVERED LISTING

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-jj-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~340</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; code, tests and one local list build.
comp-iam: DECLARED-NOT-APPLICABLE -- reads the stored name list, filings and the SEC ticker table read-only; writes no store.
comp-adversary: RUN at the cut (round84_prep/GROUP_LISTING_NOTES.md, round85_prep/GROUP_LISTING_BUILD_NOTES.md) -- 0 of 243 records carry `issuer`; both ASML records have identity null; ASML_NA's CIK 937966 is measured from its OWN stored 20-F's EDGAR path and ASML_US's from the SEC ticker table on its own US ticker. "Micro" must still list three issuers.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-340`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-jj-3` (round 85, decomposition s.93)

DSGN route ruling ADDENDUM 2 and CTO~DELL1 round-84 analysis item 3. Read
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round85_prep/GROUP_LISTING_BUILD_NOTES.md` and
`.../round84_prep/GROUP_LISTING_NOTES.md` WHOLE first.

1. `lib/research/identity/crosswalk.py` `build_crosswalk`: every record carries `issuer` = {cik, claim, source} by the notes'
   precedence -- `identity.cik` where registered; else the record's own stored filing's EDGAR CIK; else the SEC ticker table on a
   `_US_Equity` record's OWN ticker. Never the ticker table on a non-US root, never a CIK read from text; no measured source ->
   no `issuer.cik`. Union-first as today: no record dropped.
2. `lib/research/api/name_search.py` `resolve_query`: when EVERY candidate carries the same non-null measured `issuer.cik` and
   exactly ONE is covered, resolve to the covered listing; the served body names that listing and the others (the
   `identity.other_listings` line in `lib/research/api/scoped_amgt.py`). Otherwise answer exactly as today. Never collapse on a name.
3. Tests for both, with "Micro"-shaped different issuers that must still list.
4. **Build the new list locally, NO store write:** run the crosswalk build without `--write-pool`, writing the document to
   `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~340/crosswalk_local.json`.

Run `lib/research/identity/` and `lib/research/api/` tests before your commit and report both last lines (api: 2 failed at the base,
both `No module named 'pypdf'` -- name them, file no row).

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W340-S<k>` (dell1's registered coordinate is D1), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call.
2. No `bun`, `npm` or `pip install` of any kind. Nothing is fetched from the internet.
3. Standing: no S3 delete, no push of shared branches.
4. You edit `crosswalk.py`, `name_search.py`, the `identity.other_listings` serving in `scoped_amgt.py`, and their tests.

## 3. SURFACES

<paths>
lib/research/identity/crosswalk.py
lib/research/identity/tests/
lib/research/api/name_search.py
lib/research/api/scoped_amgt.py
lib/research/api/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~340/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-jj-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round85_prep/checks/r85_crosswalk.py" --crit AC1 --path "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~340/crosswalk_local.json"; echo "exit=$?"</invocation><expect>the local list drops no record, both ASML listings carry measured issuer.cik 937966 with a named source, every issuer.cik is measured with a source, and the four other 20-F names carry their filer CIKs; C1-C4 PASS; R85 CROSSWALK AC1: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-jj-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" AMGT_CROSSWALK_PATH="org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~340/crosswalk_local.json" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round84_prep/checks/r84_listing.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>with the local list, "ASML" resolves to ASML_NA_Equity naming the other listing, "Micro" still answers its candidate list, and the single-candidate and no-match answers are byte-equal to the base; R1-R3 PASS; R84 LISTING AC1: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~340 <0.9.0_WK_AMGT_RESAPP~340@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~340/AMGT_RESAPP.TO-AMGT-jj-3.one-issuer-collapses-to-the-covered-listing.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- issuer.cik coverage by source (counts with the 243 denominator);
- the two test folders' last lines;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-84 analysis item 3; route ruling ADDENDUM 2. Not a site-Z producer path (crosswalk, name_search, scoped_amgt are not the 20-F producers). Checks dry-run at the base: AC1 base FAIL as expected (0 of 243 carry issuer); AC2 base FAIL as expected (R1 NO: ASML answers two candidates; R2, R3 PASS).

<status>pending</status>
<round>85</round>
<slot>0.9.0_WK_AMGT_RESAPP~340</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
