# NFRA_OPLGTW task order -- `OG-en-7` -- the 49F SmartX served read counts the candidates whose advisor maps to another firm, with the denominator (round 38 E7; CVO v28 enrichment; expected 0)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-en-7</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-en-7</to_id>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy; read-only calls through the installed code.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the calls run as the stand-in principals of your served harness.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CVO's v28 enrichment ("count the served 49F SmartX candidates whose advisor maps to another firm (expected 0)", ADJUDICATION_v28.Z.md) taken into the CTO's round-37 analysis as E7.
EGRESS CLASS, declared: NONE beyond Opal's own host and AWS.
</preflight>

## 1. THE CELL -- `OG-en-7` (decomposition addendum R3-T.93, round 38 item E7, workstream ENRICH-R38, FWD-22)

THE GAP. Your OG-ap-23 served read proved the SmartX two-firm arm (`CODE_SERVED.json` `smartx_two_firm_detail`: firm A's resolve candidates 6, SmartX candidates 3, firm A's holdings 12 rows enveloped, the other firm returned 0 rows and none of firm A's). The CVO graded C2 MET but bounded: the other-firm call is stopped by ROUTING, so the real-data row filter rests on the build cell's planted arm. The enrichment: measure on the REAL served data how many of firm A's SmartX candidates have an advisor that maps to ANOTHER firm. Expected 0.

DO. With your existing served harness (read-only, the installed code on the live host, your stand-in master_admin principal, firm `49financial` as firm A), enumerate the SmartX candidates the tools return for firm A (the resolve and SmartX candidate lists your harness already builds, the whole of them and not a sample), and for each candidate read the advisor-to-firm mapping the gateway itself uses (the same roster/mapping the SmartX adapter reads to decide a row's firm; read `app/client_adapter_smartx.py` for it, and use the module's own function, never a copy of its logic) and count the candidates whose advisor maps to a firm other than `49financial`. Write `W/SMARTX_CROSSFIRM.json` (W = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/`) = `{"read_at": "<iso>", "live_commit": "<sha>", "method": "<one line>", "candidates_checked": n, "candidates_mapping_to_other_firm": k, "denominator": "<what n counts>", "expected": 0, "note": "<one line>"}`. No advisor name, no e-mail address, no account reference, no digit run of 8 or more may appear in the file; counts and the method only. If k is above 0, that is a FINDING: file a BLOCKING row naming the count (not the candidates) and keep the number in the record; do not hide it and do not change any code. Run it once; do not retry in a loop. Nothing is deployed, applied or written to any bucket or table.

## 2. BOUNDS

- Read-only calls through the installed code; one SSM command at most; no deploy, no apply, no `HALT_OVERRIDE`.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print an account number, a token, an advisor's name or an e-mail address.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free; a correction is a NEW row citing the old id), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from the repo root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-en-7"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/en7.AC1.sh; echo "exit=$?"</invocation><expect>(?s)smartx cross-firm count: candidates checked [1-9]\d*; mapping to another firm \d+ \(expected 0\); fields present True; digit runs of 8 or more 0 \(want 0\); e-mail addresses 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the record holds a positive denominator, the count of candidates mapping to another firm (0 is the expectation, any other number is a finding), the method and the live commit, with no long digit run and no e-mail address.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-en-7.smartx-cross-firm-count.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if AC1 PASSes, and report once (commit hash, the AC1 line, n and k).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 38 (CTO round-37 analysis, E7), workstream ENRICH-R38 (decomposition addendum R3-T.93). One mechanical criterion (the record's existence and hygiene); the number itself is the finding and the CVO reads it.
- Pre-cut: en7.AC1 base FAIL as expected (`SMARTX_CROSSFIRM.json` absent).

<status>complete</status>
<round>38</round>
<workstream>ENRICH-R38</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
