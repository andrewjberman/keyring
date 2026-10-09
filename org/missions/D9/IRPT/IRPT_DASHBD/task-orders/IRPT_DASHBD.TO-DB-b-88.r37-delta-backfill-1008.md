# TO IRPT_DASHBD.TO-DB-b-88 -- E6: the R37 packet DELTA for DB-b-87's producer change, its release (the producer re-pinned, artifact rebuilt, a targeted safe-apply under the R37 half) and ONE backfill event of 2026-10-08's lots -- no off-schedule fire is forced

<to_id>IRPT_DASHBD.TO-DB-b-88</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~63</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>42</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's ADDENDUM 10 (msg 3225; row S40 BLOCKING @a1ca17786a), enrichment item E6 | **Decomp cell:** `DB-b-88` (decomposition section 44, round 42) | **outcome_ref:** FWD-4 | **depends_on:** DB-b-87 (drained, decision EXTEND_KEY).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-63`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~63/`.

**The cell (`DB-b-88`).** It starts after DB-b-87 has drained, and only if DB-b-87's decision is EXTEND_KEY. On SOURCE_DUPLICATE this order is
superseded; the issuer amends it. The CTO's ruling (ADDENDUM 10, item 4) says: backfill 10-08's lots under the R37 half, as a packet DELTA naming
the new key and the day.

Read:
- the R37 packet `C:/dev/wk-irpt-dashbd-63/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~51/NEVER_WIDEN_PACKET_ACTIVITY_LOT_RELEASE_R37.md`;
- both halves (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_ACTIVITY_LOT_RELEASE_R37_COO_HALF.md`,
  `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_ACTIVITY_LOT_RELEASE_R37_CTO_HALF.md`);
- DB-b-78's record `deliverables/0.9.0_WK_IRPT_DASHBD~55/R37_APPLY_RECORD.json` (the procedure and the traps).

1. **The DELTA packet** (`R37_DELTA_PACKET_1008.md` in your folder) names:
   - the one changed member (`account_activity_lots.py`, its new pin and sha256);
   - the new realized key;
   - the day 2026-10-08;
   - "radius unchanged" (no new prefix, read or grant);
   - the backfill event.
2. **Ledger first, pinned** to the delta packet's sha256 (`python .tools/deploy_ledger.py`). Commit after each leg. Record `ledger_entry`.
3. **Re-pin.** Re-pin `account_activity_lots.py` in the source map to the commit carrying DB-b-87's bytes on `origin/CLOUD`, or the drain
   commit with a line saying so. Rebuild with `infra/aws/lambda/ci/build-and-upload.sh`.
4. **Plan and apply.** The targeted plan reads `0 to add, 1 to change, 0 to destroy` (the function only; the root is already at the release
   bytes). Anything else is a STOP. Run ONE `.tools/safe-apply.sh`, then read back CodeSha256 and stamp it with `record-deploy-scope.py`.
5. **Backfill.**
   - Hash the 2026-10-08 returns partition first.
   - Invoke ONE backfill event `{"accounts": "population", "backfill": {"start": "2026-10-08", "end": "2026-10-08"}}` (accounts at event
     level).
   - Record `backfill` {day, lots_skipped, realized_rows, unrealized_rows, activity_rows, returns_bytes_equal}.
   - Returns not byte-equal is a STOP: roll back by the packet's route.
6. **No other invoke.** The next scheduled fire is the organic read.

Record `R37_DELTA_RECORD.json` with `plan`, `apply`, `readback`, `delta_packet` (path), `ledger_entry` and `backfill`. Report the deploy to
`0.0.0_AB_MSTR~DELL2` through the issuer.

<criterion id="DB41b-2-AC1" cell_refs="DB-b-88"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r41b/p41b_lotkey.py" . DB41b-2-AC1</invocation><expect>DB41b-2-AC1 PASS</expect></criterion>
`DB41b-2-AC1` -- the delta packet names the new key and 2026-10-08, the ledger is pinned to it, plan 0/1/0 applied, live equals the source map. Base: FAIL.

<criterion id="DB41b-2-AC2" cell_refs="DB-b-88"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r41b/p41b_lotkey.py" . DB41b-2-AC2</invocation><expect>DB41b-2-AC2 PASS</expect></criterion>
`DB41b-2-AC2` -- one backfill lands 2026-10-08's realized, unrealized and activity rows with no skip, returns byte-equal. Base: FAIL.

<expected_criteria>DB41b-2-AC1,DB41b-2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's acts, under the R37 half:**
  - edit the source map;
  - upload ONE artifact;
  - run ONE targeted `safe-apply`;
  - invoke ONE backfill event;
  - write the ledger.
- No other function, role, bucket or key. No S3 delete. Roll back by the packet's per-key route only.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~63/
infra/aws/lambda/ci/lambda-source-map.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-88.r37-delta-backfill-1008.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 44 (round 42, lot-key chain), cell `DB-b-88`.
<owned_cells>DB-b-88</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB41b-2-AC1, DB41b-2-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~63/IRPT_DASHBD.TO-DB-b-88.r37-delta-backfill-1008.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB41b-2-AC1,DB41b-2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the delta packet path and sha, the plan and apply lines, CodeSha256 before and after, the backfill rows and returns hashes, and the ledger, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the R37 radius unchanged (one member re-pinned); the delta packet states it; returns byte-equal is the backfill's stop line.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no role change; the plan touches the function only.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the targeted plan changes the function only (0/1/0); the schedule cron(41 7 ? * MON-FRI *) is not a target and is not touched.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB41b-2-AC1/AC2 FAIL at base (no record). CTO ADDENDUM 10 item 4.
lane: the <paths> block IS the grant.
</preflight>
