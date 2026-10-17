# TO IRPT_DASHBD.TO-DB-b-331 -- the V leg of the 49 Financial filled-report pass, steps (2) and (3): TWO synthetic principals in `opal-users-v2` (a COVERING OPAL_GLOBAL staff viewer and a NON-COVERING Cottonwood viewer), their sessions handed to `2.0.0_SA_COO~S2` by broker, both removed after the issuer's word and read back ABSENT twice (CTO ruling msg 10509) (round 150)

<to_id>IRPT_DASHBD.TO-DB-b-331</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>150</round>
<workstream>VLEGPAIR</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's ruling msg 10509 (no user-to-advisor edit: nobody edits the ownership map or the partner table and no hand-typed link to real data is made; the pair is the FWD-5 shape: COVERING = one synthetic OPAL_GLOBAL internal-staff viewer whose scope covers 49 Financial by role; NON-COVERING = one synthetic Cottonwood viewer with a non-empty scope over Cottonwood accounts that excludes every 49 Financial account) | **Decomp cell:** `DB-b-331` (decomposition section 192).

**Why.** The filled-report pass (`TO-DB-b-328`) wrote 4,012 documents and the V leg graded step (1) only (S2, msg 10462). The route `serve_filled_report` returns a document's bytes only when the guard's permitted account set covers EVERY account the document names; steps (2) (200 with a body whose sha256 equals the object's for COVERING, a coverage refusal for NON-COVERING) and (3) (one export as COVERING) need a live session pair. The CTO requires (2) graded on a live pair before any portal page reads the route.

**Risk class WORLD:** TWO users rows written and removed in `opal-users-v2`. No other write. The canary document is not touched.

---

## WORKER FACE

Your worktree is the absolute path your seat uses for IRPT_DASHBD (a linked worktree cut from the current `box/dell2`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/`. Never push. **A STOP is reported to the issuer at once and removes whatever was minted.** **No password, hash, token, cookie, session value or address appears in any file, log line, commit message or row; each address is NAMED only by its 12-hex digest.** Passwords are generated in memory (a random string of at least 24 bytes), go to the helper on STDIN as one JSON object, and the sessions travel ONLY inside broker messages to `2.0.0_SA_COO~S2` (never a file, argv or environment). Never in the window 11:30Z to 14:15Z on a weekday (today is a Saturday; read the day).

**The two principals (fixed addresses, `@opal.invalid`).**
- COVERING: `v328-cover-r150@opal.invalid`. One internal-staff principal of the class your TO-DB-b-327 design learned (OPAL_GLOBAL, reaching the shared guard through the verified internal-subject predicate): userType, firm `opal-capital`, role, status active, no MFA, an `allowedFirmIds` list that includes `49financial`, a short TTL (`exp`, 3 hours), minus anything personal. Its scope covers 49 Financial BY ROLE.
- NON-COVERING: `v328-ctrl-r150@opal.invalid`. One Cottonwood viewer of the FWD-5 shape (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~219/fwd5_driver/fwd5_mint.py`, READ only): firm `cottonwood`, a NON-EMPTY scope over Cottonwood accounts (its ids taken in memory from the Cottonwood directory, never written anywhere) that contains NO 49 Financial account; a short TTL (3 hours).
Write ONE new helper of your own in your folder (`vleg_pair_mint.py`: `mint` with each password on stdin, ConditionExpression `attribute_not_exists(PK)`, read-back, bcrypt at cost 12 like the helpers; `remove` with the ABSENT polling) that refuses any address but the two fixed ones. **If you cannot make either principal without copying a person's values, editing an existing row, editing the ownership map or the partner table, or hand-typing a user-to-advisor link, STOP and report why.**

**Do, in this order. Record every value named in `VLEG_PAIR_MINT_RECORD.json` as you go (keys exactly as the checker `p197_vleg_pair_mint.py` lists).**
1. **Gates, read only.** Both addresses read ABSENT on a consistent get and on the email index; no ledger under `org/critical_paths/change_management/` and no `.open_deploys` marker at any live worktree (print the denominator) names `opal-users-v2` for these addresses. Open ONE NEVER-2 ledger naming yourself as the applier and this order, legs: mint, hand-over, removal; it stays OPEN until both ABSENT reads of both rows. Record `ledger_entry`.
2. **Mint** each once, no retry: print only the helper's read-back line. Poll the email index (read only, up to 120 s) until each reads 1. Record `principals` (two objects, COVERING then NON_COVERING: `role`, `email_digest12` (the first 12 hex of the sha256 of the fixed address), `user_type` and `firm` as words, `class` ("OPAL_GLOBAL" / "COTTONWOOD_SCOPED"), `scope_nonempty`, `covers_49f` (read from the helper's scope read-back, true for COVERING and false for NON_COVERING)) and `mint` {`minted_utc`, `readback_ok`, `index_counts_after_mint` [1, 1]}.
3. **Sign both in** through the same sign-in the FWD-5 sittings used (record only the HTTP statuses in `notes`, in words). A refusal: remove both rows (step 5) and report the reason word.
4. **Hand over:** send the TWO sessions to `2.0.0_SA_COO~S2` by broker (one message each or one; subject "V leg pair for IRPT_DASHBD.TO-DB-b-331": COVERING first, NON-COVERING second, with their roles named, never an address or password beyond what the sign-in hand-over needs). Record `handed` {`to` "2.0.0_SA_COO~S2", `via` "broker", `handed_utc`, `sessions` 2}. Then WAIT for the issuer's message "V leg done" (S2 grades step (2) and step (3) and tells the issuer, who tells you). If no word comes within the rows' 3-hour TTL, remove both anyway.
5. **Remove** both rows after the issuer's word (or at the TTL, or on any STOP): run the helper's `remove` for each; read `ABSENT GSI` and `ABSENT CONSISTENT` TWICE per row, a minute apart. Record `removal` {`after_issuer_word` (true when the issuer said "V leg done"), `removed_utc`, `absent_reads` {`COVERING`: two entries {`gsi`, `consistent`}, `NON_COVERING`: two entries}}. Close the ledger legs only when all four reads are ABSENT (the issuer closes the ledger after verification).
6. **Record** `VLEG_PAIR_MINT_RECORD.json` (`claim` "measured", `applier`, `ledger_entry`, `principals`, `mint`, `handed`, `removal`, `notes` (words: what you built each principal from, which predicate fields you matched, the sign-in statuses in words, what you could not establish, **and the sentence "the within-firm advisor split is not exercised and is owed once a 49 Financial advisor map exists"**), `reads` {`vendor_calls` 0, `secret_reads` 0}). Flip this order's status to complete as your last commit.

<criterion id="DBC197-1-AC1" cell_refs="DB-b-331"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p197_vleg_pair_mint.py" . DBC197-1-AC1</invocation><expect>DBC197-1-AC1 PASS</expect></criterion>
`DBC197-1-AC1` -- the record: both principals' classes and digests (never the addresses), the covering and non-covering scope reads, the read-backs, the two sessions handed to S2 by broker, the removal after the issuer's word, two ABSENT reads each, no address, the advisor-split sentence. Base: FAIL (no record).
<criterion id="DBC197-2-AC1" cell_refs="DB-b-331"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p197_vleg_pair_mint.py" . DBC197-2-AC1</invocation><expect>DBC197-2-AC1 PASS</expect></criterion>
`DBC197-2-AC1` -- FRESH live reads: both rows are ABSENT on a consistent get and on the email index. Base: FAIL (the checker reads the record first, so no record fails it); graded after step 5, where a row left behind FAILS it.

<expected_criteria>DBC197-1-AC1,DBC197-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus the TWO users rows for the fixed addresses (each written once, removed once) and the sign-in requests of step 3. Everything else is read, never edited.
- **Reads and writes.** No write to any other row, table, bucket, secret, schedule or code; no Terraform; no edit of the ownership map, the partner table or any existing users row; no retry of a mint; the filled documents are not touched.
- **Stop rules.** A principal cannot be made without copying a person's values, editing an existing row or hand-typing a user-to-advisor link; a sign-in refusal; a row that will not read ABSENT inside the window (say so loudly and keep the ledger OPEN; the TTL is 3 hours; delete by no other means).
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired or satisfied by a route this order did not name.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-IB9-S<k>`, with the real current UTC time, BOTH `project` ("IRPT_DASHBD") and `fabric` ("dell2") keys, class OBSERVATION or BLOCKING; append as BYTES. Commit with `.tools/safe-commit.sh`; READ the whole gate output. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-331.vleg-pair-mint-for-the-filled-report-route.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 192 (round 150, workstream VLEGPAIR), cell `DB-b-331`.
<owned_cells>DB-b-331</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC197-1-AC1, DBC197-2-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_DASHBD.TO-DB-b-331.vleg-pair-mint-for-the-filled-report-route.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC197-1-AC1,DBC197-2-AC1` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once, after step 6: each criterion's last line, counts and words only, no address, no password, no session.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: two users rows written and removed; no plan, no apply, nothing deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no IAM or grant changes; the principals are data rows in the application's own users table.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; the sign-in and the existing route are used as they are.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CDN or edge cache is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; the record checker is red on 27 single-fault mutants of a synthetic record and FAILS at the base.
lane: the <paths> block, the two fixed addresses and the CTO's ruling msg 10509 ARE the grant.
</preflight>
