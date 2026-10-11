# TO IRPT_DASHBD.TO-DB-b-117 -- E1: the R45 never-widen packet, SECOND refresh, at the bytes after the handler fix -- four members from their live pins, one kit day on HEAD's members with the five output hashes equal, every manifest compared field by field against the live one, halves UNSIGNED

<to_id>IRPT_DASHBD.TO-DB-b-117</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~92</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>61</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's rulings msg 3940 (refresh at the new bytes), msg 3999 (four members and what the packet shows), msg 4029 (the manifest compared field by field), enrichment item E1 | **Decomp cell:** `DB-b-117` (decomposition section 63) | **outcome_ref:** FWD-4 | **depends_on:** DB-b-113, DB-b-115 (both drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-92`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~92/`.

**THE CLIENT-DATA RULE (binding):** evidence carrying account numbers or client figures is written OUTSIDE the repo, under
`C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/<your serial>/`. The repo carries counts, sha256 and reason codes only. Never print an account
number or a client figure in a commit message, a record, a row or a report.

**The cell (`DB-b-117`).** DB-b-113 refreshed the R45 packet as a four-member candidate and MEASURED that the returns manifest would state the method
as the literal `absent` (row `IRPT_DASHBD-D2-W88-S3`). DB-b-115 fixed the handler (drained @bbc9e11292: both `ard.emit_day` calls pass `src`). The
handler's bytes moved, so the packet is refreshed once more, and the CTO ruled (msg 4029) that the manifest is compared field by field against the
live one, because the table hashes passed while the manifest did not. This cell writes the final packet and its evidence only.

Read in `C:/dev/wk-irpt-dashbd-92` first, and REUSE rather than rebuild:
- DB-b-113's folder `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~88/`: `R45_REFRESH_CENSUS.json`, `R45_REFRESH_DELTA0.json`,
  `NEVER_WIDEN_PACKET_R45_RELEASE_REFRESH.md` (the template: keep its sources.json diff, readers and per-member rollback sections, re-verified),
  the harness `refresh_delta0_run.py` and `manifest_probe.py`;
- DB-b-115's record `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~90/HANDLER_SRC_FIX.json`.
- DB-b-113's LIVE-pinned kit run outputs and scratch members are outside the repo under
  `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~88/`. Reuse the live run: re-hash its five outputs and confirm they equal
  the committed `sha256_live` values before relying on them; re-run live only if they do not.

1. **Census** `R45_REFRESH2_CENSUS.json`, same shape as DB-b-113's: the four members (`handler.py`, `account_return_daily.py`,
   `account_activity_lots.py`, `sources.json`), each with pin (the box/dell2 commit carrying HEAD's bytes), sha256, base_sha256 and EVERY commit since
   its live pin. `handler.py` now also carries `080dc90d92` (DB-b-115). Re-verify that no OTHER member moved since DB-b-113's census, and that
   the live base is unchanged: ONE `get-function-configuration` and ONE `head-object`.
2. **DELTA=0** `R45_REFRESH2_DELTA0.json`: ONE kit-day run of 2026-10-08 (about 16 to 18 minutes) with all four members at HEAD, every other member
   as pinned, the pinned thresholds file (sha256 `551920f0c364490d87cac260d5df2ad601ff7dac44f56043176065a3c3c2d177`, verified). Record {day, method,
   members_at_head, thresholds_sha256, tables: {<table>: {rows, sha256_live, sha256_new}}, output_hash_equal, peak_mb: {live, new}}. If a table
   hash differs: record it as it is, file a row and STOP.
3. **Manifests, field by field.** For EVERY manifest (or status record) the handler's run writes -- returns, class, the lots tables, anything else:
   list them from the code with file and line and print the denominator -- capture what the LIVE-pinned members write and what HEAD's four members
   write, by calling each kit's own emit functions with the arguments the handler passes (as `manifest_probe.py` did for returns; a capturing stub, no
   network write). Record under `manifests`: [{manifest, fields: [{field, live, new, verdict}]}] with verdict `EQUAL`, `ADDED` (in new, not in live),
   `CHANGED`, or `REMOVED` (in live, not in new). Under `expected_changes`: [{manifest, field, reason}] for every CHANGED field you can tie to a named
   order (for example a build pin or a timestamp that differs by construction). A CHANGED field you cannot tie to an order, or any REMOVED field, is
   a row; record it as it is.
4. **Packet** `NEVER_WIDEN_PACKET_R45_RELEASE_REFRESH_2.md`:
   - **## Supersedes:** both earlier packets by path and sha256; halves signed on either are void for the apply.
   - **Radius**, **## Branch A**, **## Branch B** from the handler's own rules at HEAD with file and line; count the writers again.
   - **## Rollback** per member (four pins restored) plus the base S3 version.
   - **## Memory headroom** against 3008 MB and its 85 percent line (2,556.8 MB); say which figures are local RSS and which are the Lambda's own.
   - **## DELTA=0 evidence:** the five hashes and both run identities.
   - **## Manifest comparison:** the table of every ADDED and CHANGED field, stated plainly as what a reader of the served manifest will see differ
     after the release. The three method fields ADDED to the returns manifest are a widening of what the manifest states: say so; the halves decide.
   - **## COO half** and **## CTO half**, each reading UNSIGNED.

**Read-only on AWS** (S3 GETs for the kit day, one get-function-configuration, one head-object). No build, upload, source-map edit or apply.

<criterion id="DB61-1-AC1" cell_refs="DB-b-117"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r61/p61_round61.py" . DB61-1-AC1</invocation><expect>DB61-1-AC1 PASS</expect></criterion>
`DB61-1-AC1` -- the census over live oNgy4rnr lists exactly the four members, each pinned to HEAD bytes with its commits since the live pin, with the rollback version. Base: FAIL.

<criterion id="DB61-1-AC2" cell_refs="DB-b-117"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r61/p61_round61.py" . DB61-1-AC2</invocation><expect>DB61-1-AC2 PASS</expect></criterion>
`DB61-1-AC2` -- the five output tables hash equal between the live-pinned members and HEAD's four on the 2026-10-08 kit day, under the pinned thresholds. Base: FAIL.

<criterion id="DB61-1-AC3" cell_refs="DB-b-117"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r61/p61_round61.py" . DB61-1-AC3</invocation><expect>DB61-1-AC3 PASS</expect></criterion>
`DB61-1-AC3` -- every manifest is compared field by field with no field REMOVED, the returns manifest states method_version 2 as live does, every CHANGED field is explained, and the packet carries its sections with two UNSIGNED halves. Base: FAIL.

<expected_criteria>DB61-1-AC1,DB61-1-AC2,DB61-1-AC3</expected_criteria>

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
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~92/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~92/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-117.r45-packet-refresh-2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 63 (round 61), cell `DB-b-117`.
<owned_cells>DB-b-117</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB61-1-AC1, DB61-1-AC2, DB61-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~92/IRPT_DASHBD.TO-DB-b-117.r45-packet-refresh-2.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB61-1-AC1,DB61-1-AC2,DB61-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the census, the five hashes live and new, every manifest's ADDED, CHANGED and REMOVED fields with the manifest denominator, the base S3 version, the memory statement, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the packet scopes a later release of the gold Lambda with four source members; this cell reads only.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no role or policy change; no new key.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the schedule is unchanged.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB61-1-AC1, DB61-1-AC2 and DB61-1-AC3 FAIL at base (no census, no record, no packet). CTO msgs 3940, 3999, 4029.
lane: the <paths> block IS the grant.
</preflight>
