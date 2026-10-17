# TO IRPT_DASHBD.TO-DB-b-327 -- C5 of the Cottonwood Performance read path: ONE synthetic Opal-staff (OPAL_GLOBAL) principal in `opal-users-v2` for the issuer's sign-in on 5174, handed over by broker, removed after the issuer's word and read back ABSENT twice (CTO msg 10324) (round 150)

<to_id>IRPT_DASHBD.TO-DB-b-327</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>cancelled</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>150</round>
<workstream>COTC5</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's ruling msg 10324 (IB2 mints ONE synthetic OPAL_GLOBAL principal for the issuer's 5174 sign-in, then removes it; the same pattern as the FWD-5 sittings; Andrew's word covers synthetic deletes) and the page owner's absence (CTO msg 10318: C5 goes to this seat) | **Decomp cell:** `DB-b-327` (decomposition section 186).

**Why.** The Cottonwood read path is applied and verified (`p189`); the page has not been looked at. The smoke server on `http://localhost:5174` (checkout `C:/dev/smoke-template-5174` @1f525845) shows a login page and no seat holds a staff credential. This order mints one internal-staff principal with a throwaway password, so the issuer can sign in, open Thiessen's two Cottonwood accounts on the Performance tab, and record what renders.

**Risk class WORLD:** ONE users row written and removed in `opal-users-v2`. No other write.

---

## WORKER FACE

Your worktree is the absolute path your seat uses for IRPT_DASHBD (a linked worktree cut from the current `box/dell2`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/`. Never push. **A STOP is reported to the issuer at once and removes whatever was minted.** **No password, hash, token, cookie or address appears in any file, log line, commit message or row; the address is NAMED only by its 12-hex digest.** Passwords are generated in memory (a random string of at least 24 bytes), go to the helper on STDIN as one JSON object, and travel to the issuer ONLY inside ONE broker message (never a file, argv or environment).

**The principal.** Address (fixed): `c5-staff-r150@opal.invalid`. It must be an internal-staff principal of the class Andrew's own account is at Global (OPAL_GLOBAL, which the shared guard reaches through the verified internal-subject predicate; your C4 probes used his principal): the same shape his users row has for userType, firm (`opal-capital`), role, status active, no MFA, an `allowedFirmIds` list that includes `cottonwood`, and a short TTL (`exp`, 3 hours), minus anything personal. Learn the shape from the two helper files (READ only) and from the ATTRIBUTE NAMES of his row (never its values): `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~219/fwd5_driver/fwd5_mint.py` and `.../0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_mint.py` (both write `userType` `test-filer`, which is NOT staff), and `infra/aws/lambda/investor-reporting/_authz/served.py` (`verified_internal_subject`), `infra/aws/users/lambda/portal-authorizer/index.mjs` (`computeAllowedFirms`) and the edge predicate they cite. Write ONE new helper of your own in your folder (`c5_staff_mint.py`: `mint` with the password on stdin, ConditionExpression `attribute_not_exists(PK)`, read-back, bcrypt at cost 12 like the helpers; `remove` with the ABSENT polling) that refuses any address but the fixed one. If you cannot make the principal pass the internal-subject predicate without copying Andrew's values or editing an existing row, STOP and report why.

**Do, in this order. Record every value named in `COT_C5_SIGNIN_RECORD.json` as you go (keys exactly as the checker `p193_c5_staff_signin.py` lists).**
1. **Gates, read only.** The email index and a consistent get both read the fixed address ABSENT; no ledger under `org/critical_paths/change_management/` and no `.open_deploys` marker at any live worktree (print the denominator) names `opal-users-v2` for this address. Open ONE NEVER-2 ledger naming yourself (`0.7.0_AE_CloudOps~IB2`) as the applier and this order, legs: mint, hand-over, removal; the ledger stays OPEN until both ABSENT reads. Record `ledger_entry`.
2. **Mint** once, no retry: print only the helper's read-back line. Poll the email index (read only, up to 120 s) until it reads 1. Record `principal` {`email_digest12` (the first 12 hex of the sha256 of the fixed address), `user_type` and `firm` as words, `class` "OPAL_GLOBAL"} and `mint` {`minted_utc`, `readback_ok`, `index_count_after_mint`}.
3. **Prove it signs in** (one `POST /auth/login` against `http://localhost:5174`, the password on STDIN of your own sign-in step; record only the HTTP status; do NOT start, stop or restart the server, which is Andrew's). A refusal: remove the row (step 5) and report the reason word.
4. **Hand over:** send ONE broker message to `2.0.0_SA_COO~D2` carrying the address and the password (the only place they ever appear), subject "C5 sign-in ready". Record `handed` {`to`, `via` "broker", `handed_utc`}. Then WAIT for the issuer's message "C5 done" (the issuer signs in, looks, and writes the result elsewhere). If no word comes within the row's 3-hour TTL, remove it anyway.
5. **Remove** the row after the issuer's word (or at the TTL, or on any STOP): run the helper's `remove`; read `ABSENT GSI` and `ABSENT CONSISTENT` TWICE, a minute apart. Record `removal` {`after_issuer_word` (true when the issuer said "C5 done"), `removed_utc`, `absent_reads` (two entries {`gsi`, `consistent`})}. Close the ledger only when both reads are ABSENT.
6. **Record** `COT_C5_SIGNIN_RECORD.json` (`claim` "measured", `applier`, `ledger_entry`, `principal`, `mint`, `handed`, `removal`, `notes` (words: what you built the principal from, which predicate fields you matched, what you could not establish), `reads` {`vendor_calls` 0, `secret_reads` 0}). Flip this order's status to complete as your last commit.

<criterion id="DBC193-1-AC1" cell_refs="DB-b-327"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p193_c5_staff_signin.py" . DBC193-1-AC1</invocation><expect>DBC193-1-AC1 PASS</expect></criterion>
`DBC193-1-AC1` -- the record: the principal's class and digest (never the address), the read-back, the hand-over by broker to the issuer, the removal after the issuer's word, two ABSENT reads, no address. Base: FAIL (no record).
<criterion id="DBC193-2-AC1" cell_refs="DB-b-327"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p193_c5_staff_signin.py" . DBC193-2-AC1</invocation><expect>DBC193-2-AC1 PASS</expect></criterion>
`DBC193-2-AC1` -- FRESH live reads: the row is ABSENT on a consistent get and on the email index. Base: FAIL (the checker reads the record first, so no record fails it); graded after step 5, where a row left behind FAILS it.

<expected_criteria>DBC193-1-AC1,DBC193-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus the ONE users row for the fixed address (written once, removed once) and the one sign-in request of step 3. Everything else is read, never edited.
- **Reads and writes.** No write to any other row, table, bucket, secret, schedule or code; no Terraform; no change to the 5174 server or its checkout; no retry of the mint.
- **Stop rules.** The principal cannot be made to pass the internal-subject predicate without copying a person's values or editing an existing row; a sign-in refusal; a row that will not read ABSENT inside the window (say so loudly and keep the ledger OPEN; its TTL is 3 hours; delete by no other means).
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired or satisfied by a route this order did not name.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-IB8-S<k>`, with the real current UTC time, BOTH `project` ("IRPT_DASHBD") and `fabric` ("dell2") keys, class OBSERVATION or BLOCKING; append as BYTES. Commit with `.tools/safe-commit.sh`; READ the whole gate output. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-327.c5-synthetic-staff-signin-for-the-performance-tab.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 186 (round 150, workstream COTC5), cell `DB-b-327`.
<owned_cells>DB-b-327</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC193-1-AC1, DBC193-2-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_DASHBD.TO-DB-b-327.c5-synthetic-staff-signin-for-the-performance-tab.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC193-1-AC1,DBC193-2-AC1` BEFORE the flip (the ids as ONE comma-joined argument); each row's recorded invocation must equal the order's criterion text exactly; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: the principal's class and what you matched, the sign-in status, the two ABSENT reads, and what is NOT established. Counts, words and the digest only. Send the broker message of step 4 AS SOON AS step 3 passes; the issuer is waiting.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one users row written and removed within the sitting; nothing else changes.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission changes; the mint and removal use the applier's existing reach on the users table (the FWD-5 helper family).
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base (no record) and the checker selftest is red on 16 single-fault arms; the safe failure is a removed row (step 5 always runs, the TTL is the backstop).
lane: the <paths> block IS the grant.
</preflight>
