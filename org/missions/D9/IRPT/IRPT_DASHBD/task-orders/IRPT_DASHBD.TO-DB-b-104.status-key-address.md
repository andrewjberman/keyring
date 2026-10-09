# TO IRPT_DASHBD.TO-DB-b-104 -- E1: the lots status key is built by opal_naming.address('irpt', firm, 'gold', 'account_activity_daily', '_status', 'lots_not_computed.json'), never a typed suffix (rule 30), with the key's bytes unchanged

<to_id>IRPT_DASHBD.TO-DB-b-104</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~79</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>51</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** the issuer, on laptop 4.0.0_SA_CRO's naming ruling relayed by 0.0.0_AB_MSTR~DELL2 (msg 3555), enrichment item E1 | **Decomp cell:** `DB-b-104` (decomposition section 53) | **outcome_ref:** FWD-4 | **depends_on:** DB-b-97 (drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-79`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~79/`.

**The cell (`DB-b-104`).** In `C:/dev/wk-irpt-dashbd-79/infra/aws/lambda/investor-reporting/reporting-gold/handler.py`, DB-b-91 types
`LOTS_STATUS_KEY = "_status/lots_not_computed.json"` (around line 448) and joins it to the activity prefix. The naming registry's writer,
laptop 4.0.0_SA_CRO, ruled (relayed in MSTR msg 3555) that no registry row is owed: `address('irpt', firm, 'gold', 'account_activity_daily',
'_status', 'lots_not_computed.json')` already builds the key and grades CONFORMANT. Rule 30 says every S3 address is `address()` output, so the
handler must build it.

1. Build the status object's bucket and key from that `address()` call. Remove the typed suffix constant and every other typed form of it.
2. **The key's bytes must not change.** For each firm the handler serves, print the old key and the new one, and record `key_equal_before_after`.
   If they differ, file a row and STOP; changing the key would orphan the live object.
3. Tests: the status object's key equals the `address()` output; every existing reporting-gold test still passes.
4. Record `STATUS_KEY_ADDRESS.json` {tests: {passed, failed, new_test}, keys: {<firm>: {before, after}}, key_equal_before_after}.

No deploy: this rides the next gold release with DB-b-97, under its own pair (CTO ADDENDUM 16 item 1).

<criterion id="DB51-1-AC1" cell_refs="DB-b-104"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r51/p51_round51.py" . DB51-1-AC1</invocation><expect>DB51-1-AC1 PASS</expect></criterion>
`DB51-1-AC1` -- the handler builds the status key with address(), with the key unchanged, tested. Base: FAIL.

<expected_criteria>DB51-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception:** you edit the reporting-gold handler and its tests folder. No deploy, no AWS call.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~79/
infra/aws/lambda/investor-reporting/reporting-gold/handler.py
infra/aws/lambda/investor-reporting/reporting-gold/tests/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~79/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-104.status-key-address.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 53 (round 51), cell `DB-b-104`.
<owned_cells>DB-b-104</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB51-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~79/IRPT_DASHBD.TO-DB-b-104.status-key-address.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB51-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the old and new keys per firm, the tests, and any row, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the reporting-gold handler's status key construction; the key's bytes are held equal; it ships in a later release under its own pair.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call; the key is unchanged and inside the existing write set.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB51-1-AC1 FAIL at base (the suffix is typed at handler.py:448; no record). Rule 30; CRO ruling via MSTR msg 3555.
lane: the <paths> block IS the grant.
</preflight>
