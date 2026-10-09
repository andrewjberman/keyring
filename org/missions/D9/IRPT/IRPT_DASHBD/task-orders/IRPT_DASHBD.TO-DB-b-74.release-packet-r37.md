# TO IRPT_DASHBD.TO-DB-b-74 -- E2: the activity-and-lot release packet re-cut at HEAD after DB-b-73, with EVERY bundle member pinned to the commit that carries its HEAD bytes (row W47-S4), and the sizing from DB-b-73's kit runs; both halves UNSIGNED

<to_id>IRPT_DASHBD.TO-DB-b-74</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~51</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>37</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's round-36 ADDENDUM 5 (on ADJUDICATION_v21 @37daf4f637; PRD v0.9 @e8f96f579c), enrichment item E2 | **Decomp cell:** `DB-b-74` (decomposition section 39) | **outcome_ref:** FWD-4 | **depends_on:** DB-b-73 (drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-51`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~51/`.

**The cell (`DB-b-74`).** It starts only after DB-b-73 is drained into box/dell2; the issuer spawns it then. Round 36's apply was rolled
back (CTO msg 2393) because four members were packaged at older pins than the signed list (row D2-W47-S4: `lib/opal_naming.py`,
`infra/logic/registry/systems.json`, `exemptions.json`, `reporting_policies.json`), and the sizing failed (S5, repaired by DB-b-73).

1. **The pins table.** List one row per member of `infra/aws/lambda/ci/lambda-source-map.json` entry `irpt-49f-reporting-gold-lambda`
   `staged_from` at HEAD, plus every member the release adds (the round-35 packet's Preconditions table: pins 0 to 4). Each row is
   `| `<repo_path>` | `<pin>` | `<sha256>` |`.
   - `pin` is the newest commit on `origin/CLOUD` whose bytes of that path equal HEAD's. If origin/CLOUD does not carry HEAD's bytes yet,
     print the pin as box/dell2's commit and say so in a line under the table.
   - `sha256` is `git show <pin>:<path> | sha256sum`.
   - Do NOT edit the source map. The deploying cell sets these pins.
2. **Re-cut the packet** as `NEVER_WIDEN_PACKET_ACTIVITY_LOT_RELEASE_R37.md` in your folder, from the R35 packet
   `deliverables/0.9.0_WK_IRPT_DASHBD~46/NEVER_WIDEN_PACKET_ACTIVITY_LOT_RELEASE_R35.md`. Keep its structure and reasoning where it holds.
   - Re-derive what changed: the realized key (DB-b-73), the file list, the pins, and the sizing.
   - Print each kit day's `peak_mb` and `total_s` from `deliverables/0.9.0_WK_IRPT_DASHBD~50/LOTS_KEY_E1.json` exactly, and the line
     `refusals: 0`.
   - State whether the radius widens. Widening is stated, never hidden.
   - Keep both halves `UNSIGNED`.

<criterion id="DB37-2-AC1" cell_refs="DB-b-74"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r37/p37_round37.py" . DB37-2-AC1</invocation><expect>DB37-2-AC1 PASS</expect></criterion>
`DB37-2-AC1` -- every staged_from member has a pin row whose sha256 equals both its pin's bytes and HEAD's bytes. Base: FAIL.

<criterion id="DB37-2-AC2" cell_refs="DB-b-74"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r37/p37_round37.py" . DB37-2-AC2</invocation><expect>DB37-2-AC2 PASS</expect></criterion>
`DB37-2-AC2` -- the packet prints both kit days' peak and time from DB-b-73's record, and refusals: 0. Base: FAIL.

<criterion id="DB37-2-AC3" cell_refs="DB-b-74"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r37/p37_round37.py" . DB37-2-AC3</invocation><expect>DB37-2-AC3 PASS</expect></criterion>
`DB37-2-AC3` -- the packet carries the rollback, writers and both branches, and both halves read UNSIGNED. Base: FAIL.

<expected_criteria>DB37-2-AC1,DB37-2-AC2,DB37-2-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~51/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-74.release-packet-r37.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 39 (round 37), cell `DB-b-74`.
<owned_cells>DB-b-74</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB37-2-AC1, DB37-2-AC2, DB37-2-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~51/IRPT_DASHBD.TO-DB-b-74.release-packet-r37.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB37-2-AC1,DB37-2-AC2,DB37-2-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the pins table count, which pins sit on box/dell2 rather than origin/CLOUD, the sizing printed, and whether the radius widened, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the packet is the blast-radius read of the next apply; this cell applies nothing.
comp-iam: RUN -- 214 IAM roles parsed, 196 services; BLIND on irpt-49f-reporting-gold-role (no service row); the packet's policy delta is the read.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB37-2-AC1/AC2/AC3 FAIL at base (no packet). Rows D2-W47-S4/S5; CTO msg 2393.
lane: the <paths> block IS the grant.
</preflight>
