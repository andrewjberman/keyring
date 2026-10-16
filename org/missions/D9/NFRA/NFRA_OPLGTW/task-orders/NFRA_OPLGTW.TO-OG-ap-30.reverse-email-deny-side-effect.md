# NFRA_OPLGTW task order -- `OG-ap-30` -- APPLY: reverse the browser side effect of OG-mg-1 -- delete exactly TWO `email_deny` records (andrew@ and opalbloomberg@), leave alyssa@ (CTO ruling @e511fa0194 shape b; round-38 analysis E5; PRD C2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-30</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-30</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change. The two deletes run under your own audited AWS identity (the gateway operator role holds no DeleteItem by design and is NOT used). If your identity is denied the delete, STOP and report: do not widen anything.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_OPLGTW_EMAIL_DENY_SIDE_EFFECT_OF_OG_MG_1_20261016_Z.md` (shape b; the CTO half is signed in it for exactly this two-key write set) and the CVO's half `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/3.0.0_SA_CVO~Z/NEVER_WIDEN_HALF_CVO_EMAIL_DENY_REVERSAL_20261016.md` @c39c415178.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ap-30` (decomposition addendum R3-T.98, round 39 cell E5)

WHY. At ~11:22Z `OG-mg-1` Phase B made `andrew@opalinvest.com` and `opalbloomberg@opalinvest.com` RESTRICTED principals. Contract C2 writes an `email_deny` record for every principal made restricted, and the email-only browser routes (`/login`, `/sprint*`, `/rivalfunds*`, `/yearinreview*`; `app/server.py:206-229`) refuse a denied email first. The owners themselves have been refused on four browser routes since 11:22Z. Cause note: `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_BROWSER_DENY_LIST_CAUSE_20261016.md`. This cell reverses ONLY that side effect. The restricted profiles and grants of `OG-mg-1` R1 and R2 stay exactly as signed. `alyssa@opalinvest.com`'s deny (restricted since 09-27) is INTENDED and stays.

THE KEYS. `pk = "POLICY#EMAILDENY#" + sha256hex("og-email-deny/v1|" + email.strip().lower())`, `sk = "email_deny"`, table `gateway-access-state-table` (us-east-1), attribute names `pk` and `sk`. Derive the three keys with `app/access_state.py` `email_deny_key(email)` (or, equivalently, `python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_deny.py keys`). Never scan to find them; never print a hash, an `oid` or a `tid` in any message.

### PHASE A (now, on this order): measure, record, draft the ask. NO WRITE IN ANY FORM

1. GetItem (`ConsistentRead`) the three keys. Expected NOW: all three present with `status` `active`, and a strongly consistent COUNT of `email_deny` items (`begins_with(pk,"POLICY#EMAILDENY#")` and `sk = "email_deny"`) of exactly 3. Anything else is a STOP and a BLOCKING row.
2. Write `W/DENY_BEFORE_OG-ap-30.json` (W = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/`) = `{"read_at": "<iso>", "table": "gateway-access-state-table", "write_set": ["andrew", "opalbloomberg"], "writes": 2, "email_deny_total_before": 3, "items": {"andrew": {"present": true, "status": "active", "sha256": "<sha256 of the item as canonical JSON, sorted keys>"}, "opalbloomberg": {...}, "alyssa": {...}}}`. No hash of a key, no `oid` or `tid`, no e-mail beyond the three labels.
3. Write the FULL items (every attribute) to `W/DENY_ROLLBACK_ITEMS.json` and add that path to `.git/info/exclude` BEFORE the file exists; confirm `git status` does not list it and `git ls-files` does not hold it. It is the rollback source and holds principal identifiers: it is NEVER committed, imaged or mailed.
4. Draft `W/NEVER_WIDEN_ASK_OG-ap-30.md` for THREE halves, each under a heading containing its word (`CTO`, `COO`, `CVO`). Sections: the `diff` (two deletes, the two e-mails named, nothing else); the `widening` (a NARROWING reversal: it RE-OPENS the four browser routes to the two Opal owner emails, which were open before 11:22Z; no data scope changes, the MCP profiles and grants are untouched); `both branches` (the two records present and active as recorded: conditional delete lands; a record absent or changed since the read: that key is NOT written and you STOP); the `rollback` per key (put the saved item back from `DENY_ROLLBACK_ITEMS.json`, or `deny-backfill` for that e-mail); the `read-backs` (below); `alyssa@opalinvest.com` named ONLY as UNTOUCHED. The ask names exactly the two e-mails above, `alyssa@opalinvest.com` as untouched, and NO other e-mail address.
5. Run `ap30.AC1`, commit your files EXCEPT `DENY_ROLLBACK_ITEMS.json`, REPORT, STOP. The CTO half is signed in the ruling, the CVO half is signed at `c39c415178` (and re-reads your ask), the COO half is the issuer's. The issuer's GO names the ask's sha256 and all three halves.

### PHASE B (only on the issuer's GO naming all three halves signed at the ask's sha256)

6. Re-GetItem the three keys. Each must still match its recorded `sha256` and `status` active; else STOP. Then ONE `TransactWriteItems` (us-east-1, your own identity): `Delete` the andrew@ key and the opalbloomberg@ key, each with `ConditionExpression` `attribute_exists(pk) AND #s = :a` (`#s` = `status`, `:a` = `active`), and a `ConditionCheck` on the alyssa@ key (`attribute_exists(pk) AND #s = :a`) so the whole write fails closed if alyssa's record moved. No other write, no scan-and-delete, no loop.
7. READ BACK (strongly consistent): the two records are ABSENT; alyssa's is PRESENT and active; the `email_deny` COUNT is exactly 1 (it was 3). Write `W/DENY_AFTER_OG-ap-30.json` = counts and booleans only. Run `ap30.AC2`, write the proof instance, flip the status only if both ACs PASS, REPORT once (commit hash, the AC lines, the count line). Then the ISSUER does the real run: MC Portal's terminal asks Andrew (or the owner account) to open `/sprint` and `/rivalfunds` once each and says what it answered.

## 2. BOUNDS

- EXACTLY two deletes and one condition check: the write set is a literal two-key list. NEVER touch `alyssa@opalinvest.com`'s record, any `principal_profile`, `data_entitlement` or `operator_audit` record, or any other email_deny key. No deploy, no code change, no IAM change.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a key hash, an `oid` or a `tid`; commit `DENY_ROLLBACK_ITEMS.json`.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/` (the tree convention grants it; it needs no entry). Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-30"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/ap30.AC1.sh; echo "exit=$?"</invocation><expect>(?s)ask: three half headings yes; names the two write-set e-mails yes; alyssa named as untouched yes; other e-mail addresses 0 \(want 0\).*record: write_set \['andrew', 'opalbloomberg'\] \(want \[andrew, opalbloomberg\]\); writes 2 \(want 2\); item sha256 for all three yes; email_deny_total_before 3 \(want 3\).*live table now: live_read=ok andrew_present=yes andrew_active=yes opalbloomberg_present=yes opalbloomberg_active=yes alyssa_present=yes alyssa_active=yes email_deny_total=3.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-30"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/ap30.AC2.sh; echo "exit=$?"</invocation><expect>(?s)live: andrew record present no, opalbloomberg record present no \(want no, no\); alyssa present yes active yes \(want yes, yes\); email_deny total 1 \(want before 3 minus 2\).*rollback file present yes; tracked by git 0 \(want yes, 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1` (Phase A, before any write): the ask names exactly the two write-set e-mails and alyssa as untouched with three half headings, the before-record is complete, and the live table still holds the three records. `AC2` (Phase B): the live table read back after the deletes; the rollback file exists and is not tracked.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-30.reverse-email-deny-side-effect.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 39 cell E5 (decomposition addendum R3-T.98), cut FIRST and alone, ahead of the rest of the round-39 issuance, because the CTO ruled it "now, not batched" (analysis @faa77bd49e) and Andrew is refused on his own browser routes. First order to `0.7.0_AE_CloudOps~NFRA1` (rule 34); `0.0.0_AB_MSTR~Z` is told at the cut.
- The defect is the issuer's: the `OG-mg-1` ask and the COO half named the `email_deny` records for the rollback only, not the browser effect (row Z-S312, ARMED, disarm owner `2.0.0_SA_COO~O`; disarmed when AC2 PASSes and the owner's browser run reads non-deny).
- Pre-cut: `ap30.AC1` base FAIL as expected (ask and before-record absent); PASS arm on a real shape against the live table (all three present, count 3); controls FAIL for their reasons (a third e-mail in the ask; writes 3). `ap30.AC2` base FAIL as expected (record absent; and with a record against the real table, nothing deleted: FAIL); PASS arm via a live-state override; controls FAIL (alyssa also gone; no rollback file).
- Browser read-back (the CTO's "one browser request per route by each account answers non-deny") cannot be driven by the applier (the ALB email comes from Entra sign-in); it is the issuer's close run, by the owner account through MC Portal.

<status>complete</status>
<round>39</round>
<workstream>ENRICH-R39-E5</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
