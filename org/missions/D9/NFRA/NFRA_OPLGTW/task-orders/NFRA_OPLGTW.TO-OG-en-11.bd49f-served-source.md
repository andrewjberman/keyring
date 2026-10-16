# NFRA_OPLGTW task order -- `OG-en-11` -- the SERVED read of the 49F Black Diamond adapter: which bucket does each client tool read? (round 38; CTO msg 35014, PRD v3.6)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-en-11</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-en-11</to_id>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy; read-only calls through the installed code.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the calls run as the stand-in master_admin principal of your served harness.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's msg 35014 (PRD v3.6, Andrew-direct 2026-10-14: "We can allow 49F Black Diamond pulls from opal-data-bd"; "Live, it reads the opal-data-assets copy (OG-ap-24 named gap)"), which this cell MEASURES rather than assumes.
EGRESS CLASS, declared: NONE beyond Opal's own host and AWS.
</preflight>

## 1. THE CELL -- `OG-en-11` (decomposition addendum R3-T.95, round 38, workstream ENRICH-R38-C, FWD-22)

WHAT IS KNOWN. The 49F Black Diamond adapter (`app/client_adapter_bd49f.py`, built by `OG-cl-2`, complete and merged) is written to read the LIVE `opal-data-bd/silver/` tables (holdings from `unrealized`, transactions, allocation from `allocations`, fees; its docstring and `LIVE_SUFFIX = "-live"`) through its own scoped role (`gateway-blackdiamond-read-role`, extended by `OG-ap-24`; the ARN comes from the env var `app/client_role.py` names). It is live in release `3d5c9c8bf1`. The CTO reads that, live, it reads the `opal-data-assets` copy instead. Your OG-ap-23 served read measured the SmartX two-firm arm and the client admission arms, and records NOTHING about which bucket a 49F Black Diamond answer was read from (`CODE_SERVED.json` holds zero mention of `opal-data-bd`, `opal-data-assets` or `49f`). So the claim is unmeasured either way.

DO. With your existing served harness (read-only, the installed code on the live host, your stand-in master_admin principal), call for firm `49financial` the four client tools that go through the 49F Black Diamond adapter: `client_get_holdings`, `client_get_transactions`, `client_get_allocation`, `client_get_fees` (first `client_resolve_account` to get an account reference exactly as the tools do; use ONE account the resolver returns for the Black Diamond platform of firm 49financial; if the resolver returns none for that platform, record that as the finding and stop). For each call read the answer's own `source_keys` (and the partition date / as_of it states) and record the BUCKET of the first source key and its class: `opal-data-bd` (the live silver tables), `opal-data-assets` (the copy under `blackdiamond/49f/silver/`), `other`, or `none` when the answer is empty or refused (and say why in `note`). Also record the role name the adapter's AWS session carried for those calls if the harness can read it (an STS caller identity captured inside the same process, never a credential); otherwise `unread`. Write `W/BD49F_SERVED.json` (W = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/`) in the shape `r38/checks/en11.AC1.sh` documents. The `finding` is one sentence: either "all four read opal-data-bd" or exactly which tool read which other bucket. If ANY tool reads the assets copy or anything but opal-data-bd, file a BLOCKING row naming the tool, the bucket and the cause you can establish by reading the adapter's code path (the `-live` suffix selection, the catalog row lookup, the role ARN env var): do not change code, do not widen a role, and do not conclude beyond what you read. No account number (references stay masked `****<last4>` or are dropped), no advisor or person name, no digit run of 8 or more, no e-mail address in the file. Run it once; do not retry in a loop. Nothing is deployed, applied or written to any bucket or table.

## 2. BOUNDS

- Read-only calls through the installed code; one SSM command at most; no deploy, no apply, no `HALT_OVERRIDE`.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print an account number, a token, a person's name or an e-mail address.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free; a correction is a NEW row citing the old id), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from the repo root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-en-11"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/en11.AC1.sh; echo "exit=$?"</invocation><expect>(?s)49f bd served: tools [4-9] of the 4 required present True; bucket classes: opal-data-bd \d+, opal-data-assets \d+, bad class 0 \(want 0\); fields present True; digit runs of 8 or more 0 \(want 0\); e-mail addresses 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the record names, for each of the four tools, the bucket class read, with the live commit, the method and the finding; what the classes ARE is the finding, never a criterion.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-en-11.bd49f-served-source.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if AC1 PASSes, and report once (commit hash, the AC1 line, the four classes and the finding).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 38 (CTO msg 35014), workstream ENRICH-R38-C (decomposition addendum R3-T.95; a third workstream for the L6 gate's one-issuer-per-workstream key). The CTO asked for the 49F BD adapter on `opal-data-bd` to be cut "if not cut". It is cut and built already: `OG-cl-2` (complete) wrote the adapter over the live `opal-data-bd/silver/` tables, `OG-ap-24` (applied) extended `gateway-blackdiamond-read-role`, and both are live in `3d5c9c8bf1`. What is NOT on record is the served measurement; this cell supplies it. If the measurement shows the assets copy, the cause is read from the code path and a code cell follows (not guessed here).
- Pre-cut: en11.AC1 base FAIL as expected (`BD49F_SERVED.json` absent).

<status>complete</status>
<round>38</round>
<workstream>ENRICH-R38-C</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
