# TO IRPT_DASHBD.TO-DB-b-113 -- E1: the R45 never-widen packet REFRESHED at the new source bytes -- census against the live bundle's pins shows three members, one kit day run on the live-pinned members and on HEAD's shows the five output hashes equal, halves UNSIGNED

<to_id>IRPT_DASHBD.TO-DB-b-113</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~88</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>57</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's ruling msg 3940 (on ADDENDUM 20: the stage cut rides R45), enrichment item E1 | **Decomp cell:** `DB-b-113` (decomposition section 59) | **outcome_ref:** FWD-4 | **depends_on:** DB-b-105, DB-b-110 (both drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-88`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~88/`.

**THE CLIENT-DATA RULE (binding):** evidence carrying account numbers or client figures is written OUTSIDE the repo, under
`C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/<your serial>/`. The repo carries counts, sha256 and reason codes only. Never print an account
number or a client figure in a commit message, a record, a row or a report.

**The cell (`DB-b-113`).** The R45 pair was signed on `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~80/NEVER_WIDEN_PACKET_R45_RELEASE.md`,
whose census shows one member (`handler.py`). Two staged members have moved since: DB-b-110 cut the lots read (drained @5d339ced5b; it edits
`account_activity_lots.py` and `account_return_daily.py`), and @354214c55f redacted a docstring in `account_return_daily.py`. The CTO ruled (msg 3940) that
both halves re-sign on a packet refreshed at the new bytes. This cell writes that packet and its evidence only.

The live bundle `irpt-49f-reporting-gold-lambda` `oNgy4rnrduvN9N2axhsHBfe9izZKd8dZGeFGXAIh+cM=` is built from the PINS in
`infra/aws/lambda/ci/lambda-source-map.json` (`functions.irpt-49f-reporting-gold-lambda.staged_from`), not from HEAD. So "what this release changes"
is measured from each member's LIVE PIN to HEAD, never from the commit before DB-b-110.

Read in `C:/dev/wk-irpt-dashbd-88` first:
- the old packet and its census `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~80/R45_RELEASE_CENSUS.json` (the template; note its `staged_pins_differ_from_head`);
- DB-b-110's record `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~85/STAGE_MEMORY.json` and its harness `stage_memory_run.py` in the same folder;
- the memory-step record `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~87/MEMSTEP_APPLY_RECORD.json` (live MemorySize is now 3008).

1. **Census.** Compare every source-map member against HEAD, as the old census did. Record `R45_REFRESH_CENSUS.json` {base_codesha256,
   members_changed: [{path, pin, sha256, base_sha256, commits_since_live_pin: [{commit, subject, order}], owner_orders}], members_compared,
   rollback: {base_s3_version, base_codesha256}, live_reads}.
   - `pin` is the box/dell2 commit carrying HEAD's bytes; `sha256` is those bytes; `base_sha256` is the live-pinned bytes (for `handler.py`, the R44 build blob the old census names).
   - `commits_since_live_pin` lists EVERY commit that touched the member between its live pin and HEAD, not only DB-b-110's. Read each one's diff.
   - The members expected to be in this release are `handler.py`, `account_return_daily.py` and `account_activity_lots.py`. The old census also
     shows `sources.json`, `lib/opal_naming.py` and `reporting_policies.json` differing from HEAD while staying at their pins: they stay out, and you say so.
   - Any OTHER member differing, or a commit in a member's list that is not a DB-b-97, DB-b-104, DB-b-110 or redaction change and that changes an
     executable statement, means a row and a STOP on that member: name it in the packet as an open question for the halves; do not decide it.
   - ONE `get-function-configuration` and ONE `head-object` for the live base and the rollback S3 version.
2. **DELTA=0 evidence.** Run the 2026-10-08 kit day twice with DB-b-110's harness method (S3 GETs only; the status write to a stub):
   - **live:** the three members materialized from their LIVE bytes (`git show <live pin>:<path>`; `handler.py` from the R44 build commit) into a
     scratch directory outside the repo, every other member as pinned;
   - **new:** the same directory with the three members at HEAD's bytes.
   - Both runs use the PINNED thresholds file: `git show 6be02af162eaeff01ca19d2e5b228ffce6091cc7:"org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.4.0_DS_ClientPlatform~S/MEASURED_THRESHOLDS_R1.json"`,
     sha256 `551920f0c364490d87cac260d5df2ad601ff7dac44f56043176065a3c3c2d177`. Verify the sha256 before use, and write the file outside the repo. Say
     whether the private copy DB-b-110 used (row D2-W85-S1) has the same sha256.
   - Record `R45_REFRESH_DELTA0.json` {day, method, thresholds_sha256, tables: {<table>: {rows, sha256_live, sha256_new}}, output_hash_equal,
     peak_mb: {live, new}} for the five outputs: returns, class, account_activity_daily, account_lot_realized, account_lot_unrealized_daily.
   - If a hash differs, record it as it is, set `output_hash_equal` false, file a row and STOP. Do not edit a producer.
3. **Packet** `NEVER_WIDEN_PACKET_R45_RELEASE_REFRESH.md`:
   - **## Supersedes:** the old packet's path and sha256, and that halves signed on it are void for the apply (CTO msg 3940).
   - **Radius:** no new key, read or grant. Count the writers of each output and of the status key again at the new bytes.
   - **## Branch A** and **## Branch B**, both from the handler's own rules with file and line at HEAD, as the old packet stated them.
   - **## Rollback** to `oNgy4rnr` by its S3 version, and the three source-map pins restored.
   - **## Memory headroom:** against the 3008 MB setting and its 85 percent line (2,556.8 MB), using DB-b-110's and your own measured peaks. State
     which figures are local RSS and which are the Lambda's own.
   - **## DELTA=0 evidence:** the five hashes and both run identities.
   - **## COO half** and **## CTO half**, each reading UNSIGNED.

**Read-only on AWS** (S3 GETs for the kit day, one get-function-configuration, one head-object). No build, upload, source-map edit or apply.

## AMENDMENT 1 (issuer 2.0.0_SA_COO~D2, 2026-10-11 ~03:4xZ): sources.json is the fourth member -- row IRPT_DASHBD-D2-W88-S1 ruled

**Ruling on W88-S1.** You stopped correctly. The returns difference is one column: `method_version` reads 2 on all 6,901 rows live and null at HEAD,
because DB-b-96 (`08194d1e33`) and DB-b-102 (`26a3f3a38b`) made `account_return_daily.py` read the method fields from the source entry, and
`sources.json` stayed at its live pin, which names none. Those two orders changed the two files as one unit, so the release candidate carries both:
`sources.json` at HEAD is the FOURTH member. Whether R45 ships four members is the halves' decision at signing; this cell supplies the evidence for it.

Do this, in `C:/dev/wk-irpt-dashbd-88`:
1. **Census.** Add `data/assets/scripts/gold/irpt_reporting/sources.json` to `members_changed`, with its pin, sha256, base_sha256 and EVERY commit since
   its live pin. Two of those commits belong to ADVI_COTBKF (`d41d82a633`, `f043506a7c`: the `_commonwealth_delivery` entry). Say from the code, with
   file and line, whether the reporting-gold handler's 49F run reads that entry at all.
2. **DELTA=0, third run.** Run the kit day once more with all FOUR members at HEAD (the three plus `sources.json`), every other member as pinned. In
   `R45_REFRESH_DELTA0.json` set `members_at_head` to the four paths and make `sha256_new` this run's hashes. Keep the three-member run you already
   made under `three_member_run` (its hashes and the `method_version` finding), so the record shows both.
3. **The manifest question you read from the code** (`handler.py:579` and `:620` call `ard.emit_day` without `src`): do not argue it, measure it. From
   the live run and the four-member run, record the returns manifest's `method_version` and the three method fields as written by each, under
   `manifest_method_fields: {live, new}`. If the four-member run writes the literal `absent` where live writes a value, that is a second row and it
   goes in the packet as an open question; it does not stop you.
4. **Packet.** Update every section to the four-member candidate, and replace the READ FIRST note with what the third run shows.
5. If a table hash still differs in the four-member run: record it as it is, file a row, and STOP as before.

Gate limb: none graded this modification (to-pipeline-gate LIMB 6 fires on a newly added order only; GATE (viii) does not apply, `<placeholders>` is NONE).
The check `p57_round57.py` is amended in the same commit: DB57-1-AC1 wants exactly the four members; DB57-1-AC2 wants `members_at_head` naming the four.
The `<paths>` grant is unchanged.

<criterion id="DB57-1-AC1" cell_refs="DB-b-113"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r57/p57_round57.py" . DB57-1-AC1</invocation><expect>DB57-1-AC1 PASS</expect></criterion>
`DB57-1-AC1` -- the census over live oNgy4rnr lists exactly the three members, each pinned to HEAD bytes with its commits since the live pin, with the rollback version. Base: FAIL.

<criterion id="DB57-1-AC2" cell_refs="DB-b-113"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r57/p57_round57.py" . DB57-1-AC2</invocation><expect>DB57-1-AC2 PASS</expect></criterion>
`DB57-1-AC2` -- the five output tables hash equal between the live-pinned members and HEAD's on the 2026-10-08 kit day, under the pinned thresholds. Base: FAIL.

<criterion id="DB57-1-AC3" cell_refs="DB-b-113"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r57/p57_round57.py" . DB57-1-AC3</invocation><expect>DB57-1-AC3 PASS</expect></criterion>
`DB57-1-AC3` -- the refreshed packet carries the supersession, both branches, the rollback, the memory headroom, the DELTA=0 evidence and two UNSIGNED halves. Base: FAIL.

<expected_criteria>DB57-1-AC1,DB57-1-AC2,DB57-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception:** S3 GETs for the kit day and two live AWS READS (get-function-configuration, head-object). Scratch copies of members
  live outside the repo. No write anywhere in the repo outside your folder.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~88/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~88/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-113.r45-packet-refresh.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 59 (round 57), cell `DB-b-113`.
<owned_cells>DB-b-113</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB57-1-AC1, DB57-1-AC2, DB57-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~88/IRPT_DASHBD.TO-DB-b-113.r45-packet-refresh.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB57-1-AC1,DB57-1-AC2,DB57-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the census (each member's commits since its live pin), the five hashes live and new, the base S3 version, the thresholds sha256 answer, the memory statement, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the packet scopes a later release of the gold Lambda with three source members; this cell reads only.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no role or policy change; no new key.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the schedule is unchanged.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB57-1-AC1, DB57-1-AC2 and DB57-1-AC3 FAIL at base (no census, no record, no packet). CTO ruling msg 3940.
lane: the <paths> block IS the grant.
</preflight>
