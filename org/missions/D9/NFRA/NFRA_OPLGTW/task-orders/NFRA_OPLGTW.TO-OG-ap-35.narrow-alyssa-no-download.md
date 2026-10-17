# NFRA_OPLGTW task order -- `OG-ap-35` -- APPLY: narrow alyssa's live Schwab grant by ONE key, removing `download_filtered` (CTO ruling on open call sitez-20261016T111519Z-bd68, msg 35321)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-35</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-35</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one operator grant write and reads; no cron, alarm, monitor or cadence. It does not touch the gateway host, so it does not queue behind a release.
comp-iam: RUN-BY-ISSUER at the cut, as in `OG-mg-1` (amendment A1): the writes run under the role `opal-gateway-access-admin` through the admin module's `activate` (`dynamodb:PutItem` and `dynamodb:UpdateItem` with the `dynamodb:LeadingKeys` condition `POLICY#*`; `activate()` builds only Put operations and never deletes). Phase A SIMULATES those two actions on the role WITH that context and records allowed or implicitDeny; the before-record reads (strong `Scan` or `Query`) run under the CALLING principal. An implicitDeny is a STOP and a BLOCKING row, never a widening by this seat.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_OPLGTW_BD68_ALYSSA_DOWNLOADS_ENFORCE_HIS_WORD_20261017_Z.md` @aed4469fa6 (upheld by the laptop CTO 02:52Z): Andrew's word of 2026-10-08, "no downloads needed yet", is enforced; his live grant holds `download_filtered` (row Z-S173, `OG-mg-1` section 3). Andrew can reverse it with one word, "Alyssa may download".
EGRESS CLASS, declared: NONE beyond Opal's own AWS (STS, DynamoDB).
</preflight>

## 1. THE CELL -- `OG-ap-35` (decomposition addendum R3-T.108, round 40, workstream ENRICH-R40-G)

THE ACT. alyssa's principal holds ONE active `principal_profile` in `gateway-access-state-table` (restricted kind; her grant revision was 4 at `OG-mg-1`; read the live revision). Its `operations` field carries `describe`, `download_filtered`, `list`, `query`. The act is a NARROWING of a real client's served access: write the next grant revision with `operations` minus `download_filtered`, and NOTHING else changed.

**The writer is the same one module as `OG-mg-1`:** `infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py` (`prepare` then `activate`, one `operator_transact`), under `opal-gateway-access-admin`, with `--approver "Andrew Berman"` and `--source-authorization` naming the CTO ruling above. No other path writes a grant. No tid, oid, email, account id or grant value is ever written to the repo: hashes, roles, operation NAMES (fixed words) and counts only; identities live only in `X` = `%LOCALAPPDATA%/opal/og-salt/ag1/`.

### PHASE A -- read, prepare, ask. NO write

1. **Before-record and usage (the CTO's step 1; counts only).** Write `W/AG1_BEFORE.json` = `{"body": {"read_at", "denominator": {"policy_items_scanned": n}, "alyssa": {"pk_hash", "profile_revision", "grant_revision", "operations": [names], "scope_without_operations_hash"}, "usage": {"download_filtered_calls_since_grant": n, "last_use": "<iso or null>", "window_start": "<iso of her grant's activation>", "source": "<fixed words naming the audit source>"}, "others_hash": {"andrew": h, "bbg": h}}}` from a strongly consistent, fully paginated POLICY# scan. `pk_hash`, `scope_without_operations_hash` and the `others_hash` values are the first 10 hex of sha256 over the pk, over her canonical grant scope with `operations` removed, and over each of the other two active principals' canonical grant (so the act can prove they did not move). The usage count is the number of tool calls of `download_filtered` made by her principal since her grant's activation, from the gateway's own audit records of tool calls (the census method of `OG-bd-1` step 2, row `Z-W57-S2`); resolve her principal in-process, never print it.
2. **Operator identity and comp-iam.** Assume `opal-gateway-access-admin`; `sts get-caller-identity` names it; simulate the two actions with the `POLICY#*` context; record allowed or implicitDeny in `W/AG1_PREFLIGHT.md`.
3. **Candidate and diff.** Write `X/alyssa_narrow_candidate.json` = her live grant scope with `operations` minus `download_filtered`. Call `prepare(store, raw, load_contract(None), out=...)` in-process under the operator role; it validates and prints the diff and writes nothing. The diff against her live grant may change ONLY `operations` (and the revision and timestamp fields the module itself manages). Any other changed key: STOP, file a BLOCKING row. Save the changed-key list (keys only) and the diff line count in `W/AG1_PREFLIGHT.md`.
4. **The ask**, `W/NEVER_WIDEN_ASK_OG-ap-35.md`, for THREE halves (`1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~O`, `3.0.0_SA_CVO~Z`), each under a heading containing its word. It carries: what changes and for whom (her principal loses one operation; her other operations are unchanged; nobody gains anything); the line `Changed keys: operations only.`; her current value (hashes and operation names); the usage counts of step 1; the `Rollback:` as a restore (the next revision is the before scope, written through `activate`, never a delete or a tombstone); the `Read-back:` (below); the writers of the property (N = 1 module, read); the condition that no seat contacts the client or her firm (state the line `No seat contacts the client or the firm.`); and that Andrew can reverse the rule with one word. Run AC1, commit, REPORT (the usage counts go to the issuer, who relays them to the CTO for Andrew), STOP.

### PHASE B -- only on the issuer's GO naming all three halves signed

5. Ledger `nfra-oplgtw-alyssa-no-download` (entry AND sentinel committed first).
6. Re-read step 1 and confirm nothing moved since Phase A (her grant revision and the other principals' hashes). Then `activate --candidate X/alyssa_narrow_candidate.json` under the operator role with `--approver "Andrew Berman"`, the CTO ruling as `--source-authorization`, and a one-line `--summary`. Record the `ACTIVATED profile_revision=... grant_revision=...` or `REFUSED:` line in `W/AG1_WRITE.md`. A stale-revision refusal re-cuts Phase A once.
7. **Read-back, through the INSTALLED code on the host** (the way `OG-ap-30` read the deny guard back; no call is made AS her, no message goes to her or her firm): the entitlement decision for her principal and the operation `download_filtered` is a REFUSAL, and for one other operation of hers (`list`, or `describe`) it ANSWERS (allowed). Write `W/AG1_AFTER.json` = `{"body": {"read_at", "alyssa": {"profile_revision", "grant_revision", "operations": [names], "scope_without_operations_hash"}, "others_hash": {"andrew": h, "bbg": h}, "read_back": {"download_refused": bool, "other_operation": "<name>", "other_operation_answers": bool}}}`. On any failure of AC2, restore (activate the before scope), re-read, close the ledger ROLLED BACK and report. Then close the ledger, commit, run AC2 and report once to `2.0.0_SA_COO~O`.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/`.

## 2. BOUNDS

- The one record, through the module's `activate` under `opal-gateway-access-admin`. No IAM, policy, Lambda, gateway, allowlist or env change. No other principal's grant is touched (their hashes must be equal before and after).
- No tid, oid, email, account id or grant value in any repo file, row, message or report: hashes, roles, operation names and counts only.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; a delete action; override a gate; contact the client or her firm in any way; make a call as her principal.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-alyssa-no-download.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` as above (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from the repo root; AC1 after Phase A, AC2 after Phase B's ledger is closed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-35"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/ag1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)before-record complete \(operations carry download_filtered, usage counts numeric, hashes 10 hex, denominator printed\): yes.*ask: three half headings yes; items 4 of 4 \(all present\).*content hygiene: long digit runs 0 \(want 0\); e-mail addresses 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-35"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/ag1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)ledger CLOSED 1 of 1; sentinel at HEAD 0.*operations after == before minus download_filtered: yes; scope without operations equal: yes; grant revision \+1: yes; other principals unchanged: yes.*read-back: download refused True; one other operation answers True; content hygiene: long digit runs 0, e-mail addresses 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the narrowing is prepared and asked with her current state, the usage counts, the one-key diff, the restore rollback and the no-contact line. `AC2`: the one key is gone, nothing else moved, the other principals are unchanged, and the read-back through the installed code refuses her download and answers another operation.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-35.narrow-alyssa-no-download.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, and flip the ONE `<status>` tag to `complete` only if AC1 and AC2 PASS. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 40, workstream ENRICH-R40-G (decomposition addendum R3-T.108). Template: `OG-mg-1` (the same writer, role and ledger shape). The act does not touch the gateway host; it can run beside the release work.
- The CTO's ruling (msg 35321) asks for: (1) the usage counts before the write, reported to the CTO for Andrew; (2) a one-key write with the before-state recorded and a restore rollback; (3) a read-back that refuses her download and answers one other operation; (4) no seat contacts her or her firm. Each is a step above.
- The usage count may be 0 or small; it does not gate the act (the ruling enforces Andrew's word either way), but it goes to the CTO before Phase B so Andrew sees it. The halves still sign on the ask.
- Pre-cut: `ag1.AC1` and `ag1.AC2` base FAIL as expected (records absent); PASS arms on synthetic records; controls FAIL (AC1: before lacks `download_filtered`, a non-numeric count, the ask without the CVO half, without the no-contact line, an e-mail in the ask; AC2: no ledger, a second key removed, `download_filtered` still present, another scope key changed, another principal moved, the download not refused, the revision jumping by 2). The 10-hex hash values are exempt from the digit-run scan (a hash can be all digits).

<status>complete</status>
<round>40</round>
<workstream>ENRICH-R40-G</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
