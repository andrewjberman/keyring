# NFRA_OPLGTW task order -- `OG-pa-1` -- APPLY: Menachem's `person_access` tool narrowing to the three buckets Andrew named (46 tools), WRITTEN BY THE GRANT WRITER ON ANDREW'S OWNER CONFIRM through the People route; the applier prepares the candidate and verifies the stored record, and writes nothing (round 47; Andrew-direct 2026-10-21 ~13:xxZ, record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261021_13xxZ_MENACHEM_ENTITLEMENTS_ALL_INDICES_ASSETS_AND_SCHWAB_CONFIRM_LIVENESS.md` @741e63614a: "scoping his use to just opal-data-assets, opal-data-etfs, and opal-data-portal-v2"; the CTO's msgs 36276 and 36277)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-pa-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-pa-1</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no deploy, no schedule; the applier writes no record.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the applier only reads (strong gets and a fresh guarded process); the write is the grant-writer Lambda's, invoked by the owner-gated People route.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is Andrew's recorded word (the record above) and the CTO's msgs 36276 and 36277; the mechanism (`person_access`, read at dispatch) is live in release R3c `2923d1ee99`, and the route that writes it ships in batch17 (`OG-rl-18`, window 2026-10-22 06:45Z-07:45Z).
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-pa-1` (decomposition addendum R3-T.124, amendment A20, round 47, workstream ENRICH-R47-Q)

**What it is:** a NARROWING. On first sign-in Menachem gets the `read_only` floor (the CTO's measure at 13:09Z: etfs 18, harvest 14, portal-v2 18, mdpf 1, dynamodb 4, portal_index 6, globgrph 2, opal_discover 2, M365 35 of 43). Andrew's scope is `opal-data-assets` (`client_*` 5 and `schwab_*` 5, which need a data grant), `opal-data-etfs` (18) and `opal-data-portal-v2` (18): **46 tools**. The `person_access` record's `tools_allow` list carries those 46 names, so the dispatch chokepoint refuses every other tool for him. The record is written ONLY by the grant-writer Lambda (action `set_person_access`), invoked by `POST /api/admin/people/{tid}/{oid}/access` (owner-gated, shipped by batch17) when ANDREW confirms in the People panel. **You write nothing: no direct store write, no Lambda invoke of your own.**

⛔ **TRIGGERS (the CTO's msg 36277): Phase A starts only on my GO, given when (a) batch17's ledger is CLOSED (the People route is live) and (b) Menachem's principal profile exists. Phase B starts only after Andrew's owner confirm has been relayed to me and I send the GO.**

### PHASE A (only on the issuer's GO)
1. Read his profile (`pk` from the principal profile; his tid and oid NEVER typed; if none exists, STOP and report).
2. Derive the candidate from the DEPLOYED registry, never from memory: in ONE fresh process under the cgroup hard guard, import the deployed tree's tool registry, take the tools of the `client_*` family (5), `schwab_*` (5), the etfs bucket (18) and the portal-v2 bucket (18); `tools_allow` = their names, sorted; check the limits (at most 64 items, each at most 128 characters; the writer refuses more) and that the list only NARROWS (no tool outside what his floor plus grants could admit; the five `client_*` tools stay listed but admit nothing until the per-firm client grant code lands, row Z-S432).
3. Run `decide()` in the same fresh process with the candidate record applied to his principal: it admits every non-`client_*` candidate tool, admits NO `client_*` tool without a per-firm grant, and REFUSES an outside sample (one tool from each of harvest, M365, mdpf, ycharts, dynamodb, portal_index, globgrph, blackdiamond and opal_discover).
4. Records: `W/PA1_CANDIDATE.json` = `{"principal": {"role": "menachem", "present": true, "pk_hash": "..."}, "denominator": {"registry_tools": n}, "change": {"counts": {"client": 5, "schwab": 5, "etfs": 18, "portal_v2": 18}, "tools_allow_total": 46, "names_sha256": "<sha256 of the sorted names joined by newline>", "within_limits": true, "source": "registry of the deployed release", "narrows_only": true}}`; `W/PA1_PREFLIGHT_DECIDE.json` = `{"menachem": {"admit_all_non_client_candidate": true, "client_admitted_without_per_firm_grant": false, "refused_outside_count": n, "outside_sample_refused": true}}`; `W/PA1_POST_BODY.json` = the exact `change` object the People panel posts (tool names only). Commit, run AC1 (`.../r47/checks/pa1.AC1.sh`), REPORT, STOP. I route the body to the CTO and Andrew for the owner confirm.

### PHASE B (only on my GO, after Andrew's confirm through the People route has been relayed)
Read the LIVE `person_access` record for him (a strong read through the policy partition): `status` `active`, `tools_allow` = 46 names, names hash equal to `PA1_CANDIDATE.change.names_sha256`. Record the confirm: `W/PA1_READBACK.json` = `{"owner_confirm": {"route": "POST /api/admin/people/{tid}/{oid}/access", "verdict": "written", "by": "owner"}, "decide": {"tree": "deployed", "code_sha": "<the batch17 release sha, read on the host>", "admit_all_non_client_candidate": true, "client_admitted_without_per_firm_grant": false, "outside_sample_refused": true}}`, where `decide` is run against the DEPLOYED tree (not your scratch) on the LIVE record. Take the `verdict` from the writer's own answer or its audit item as Andrew's confirm produced it; never mark `written` that you did not read. Proof instance; commit; run AC2; report once.

## 2. BOUNDS

- Reads only. No `person_access` or grant write of any kind, no Lambda invoke, no delete, no IAM, Terraform, deploy or code change. Counts and hashes only: no e-mail address, account number or token in any record (tool NAMES are not identifiers; they may appear in `PA1_POST_BODY.json` only).
- Never: push, `git stash`, rebase, `checkout --` or `clean`.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-pa-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/pa1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)candidate: menachem present with pk_hash and a printed registry denominator: yes.*change: tools_allow counts client 5, schwab 5, etfs 18, portal_v2 18 \(total 46\).*: yes.*decide\(\) pre-flight with the candidate applied: .*: yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-pa-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/pa1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)live person_access record for menachem: active yes; tools_allow total 46 \(want 46\); names hash equals the candidate's: yes.*written by the grant writer on the owner's confirm through the People route \(verdict written, by owner\): yes.*decide\(\) on the LIVE record against the DEPLOYED tree at the batch17 release: .*: yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1` (Phase A) is graded by me before the owner confirm is routed; `AC2` (Phase B) after Andrew's confirm, against the LIVE record.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-pa-1.round-47-menachems-person-access-tool-narrowing.proof_of_spec.json` after Phase B and validate it with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` (`python3`, not `python`: ruling msg 35901). The `<status>` flip is mine.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 47, workstream ENRICH-R47-Q, amendment A20 of R3-T.124. Source: Andrew-direct 2026-10-21 ~13:xxZ (the record above) routed by the CTO's msgs 36276 and 36277. STAGED: it runs on Andrew's owner confirm through the batch17 People route, after Menachem's principal exists.
- READINGS DISCLOSED TO THE CTO: (1) the 46 tools are the buckets' CURRENT registry members (client 5, schwab 5, etfs 18, portal-v2 18, the CTO's counts), taken from the deployed registry at Phase A, so a count that differs is a finding, not a typo; (2) the applier writes nothing: the narrowing is Andrew's act through the owner-gated route, which is what `person_access` was built for; (3) the five `client_*` tools are listed now and admit nothing until the per-firm client grant code lands (row Z-S432).
- Pre-cut: `AC1` and `AC2` base FAIL as expected (no `PA1_*` records, no `person_access` record for him); `AC1` read OK on synthetic records built to the same fields and NO with one count changed (arm, not committed).

<status>staged</status>
<round>47</round>
<workstream>ENRICH-R47-Q</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
