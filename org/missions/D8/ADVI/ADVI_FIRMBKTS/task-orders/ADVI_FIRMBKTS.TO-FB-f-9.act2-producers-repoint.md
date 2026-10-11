# ADVI_FIRMBKTS task order -- `FB-f-9` -- WINDOW ACT 2: REPOINT THE PLATINUM PRODUCERS TO `address()` KEYS IN opal-data-49financial

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R3.md</decomp_doc>
<owned_cells>FB-f-9</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~16</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>WRITER_SCRIPTS, WRITER_GATE_CHECK, NEW_HOME_FRESHNESS_CHECK, OLD_HOME_QUIET_CHECK</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the cut adds or changes no cadence. A producer whose trigger or environment changes is named by the census (FB-f-6) and read with comp-schedule at the amendment; such a change reopens this line.
comp-iam: DECLARED-NOT-APPLICABLE at the cut -- no grant is created. Whether each producer role may write `advi/49financial/platinum/*` of opal-data-49financial is read from the census at the amendment: a role-level simulation is refused to the dell1 identity (L5_FACTS section 2), so the amendment reads the policy text.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut -- every criterion names a value that exists only after the act (a version, a hash, a second manifest) or a check the amendment writes; at the cut each reads FAIL by construction. The amendment writes each scripted check, dry-runs it at the base and tests it against a mutant BEFORE the GO.
EGRESS CLASS, declared: NONE.
</preflight>

## 0. THIS ORDER IS STAGED. IT IS NOT A SPAWNABLE FACE UNTIL THE ISSUER'S AMENDMENT SAYS SO.

Un-park conditions, all required, each read from a file at HEAD:
1. `FB-f-6` is `complete` with `PRODUCER_CENSUS.json` VALID, merged, and its `bucket_seam.separable_per_output` read by the
   issuer. If it reads `false`, this act is not a script edit: the producers' environment value moves every read, and the
   amendment says so and routes the form of the act to `1.0.0_SA_CTO~DELL1` before any pair is drafted.
2. Act 1 (`FB-f-8`) is `complete`.
3. The never-widen pair for this act reads SIGNED in both halves
   (`ledger/NEVER_WIDEN_ROUND3_ACT2_PRODUCERS_COO_HALF.md`, `..._CTO_HALF.md`), naming every producer script from the
   census as the blast radius and the rollback per script.
4. The actor's change-management entry is OPEN and committed first.
5. The amendment commit fills the placeholders' meaning (section 4) and sets `<status>pending</status>`.

## 1. THE CELL -- `FB-f-9` (round 3, enrichment item 1, step 2; PRD F10)

The producers that write the 11 served classes of `opal-data-bd` are repointed so each served key is written ONCE, at its
`address()` key in `opal-data-49financial`, and no served key is written to the old home after the act. Dual write is
DEC-17's NEVER: there is no window in which both homes are written. The old bucket's keys are untouched (the rollback
window); a delete is Andrew's word. The scripts, lines, runners and schedules are the census's; the act edits exactly
those and nothing the census does not name. The key text each producer writes comes from
`lib/opal_naming.py address()` (never typed).

## 2. BOUNDS

1. Only the census's writer scripts change; only the lines that build a served key's bucket or key. The producers' other
   reads and writes (silver, the other tiers, other firms) are unchanged.
2. No schedule, rule or environment value changes unless the amendment names it and the pair covers it.
3. No run of a producer outside its schedule unless the amendment names an ad-hoc QA run (permitted for QA; the artifacts
   are never production evidence).
4. If the live state differs from the pair's blast radius, STOP before the first write and file a BLOCKING row.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

(The amendment adds the census's writer scripts, each named by path, and nothing else.)

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/ADVI_FIRMBKTS.TO-FB-f-9.act2-producers-repoint.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-f-9"><invocation><WRITER_GATE_CHECK></invocation><expect>WRITERS: 0 of <WRITER_SCRIPTS> still build a served key against opal-data-bd</expect></criterion>
  <criterion id="AC2" cell_refs="FB-f-9"><invocation><NEW_HOME_FRESHNESS_CHECK></invocation><expect>NEW HOME: every class written since the act, 0 key outside address()</expect></criterion>
  <criterion id="AC3" cell_refs="FB-f-9"><invocation><OLD_HOME_QUIET_CHECK></invocation><expect>OLD HOME: 0 served-class keys written since the act</expect></criterion>
</proof_of_spec>

Placeholders at the amendment: `WRITER_SCRIPTS` is the census's writer count; `WRITER_GATE_CHECK` is an issuer-written file
that re-reads each writer's lines at HEAD; `NEW_HOME_FRESHNESS_CHECK` and `OLD_HOME_QUIET_CHECK` are issuer-written
listing checks, bounded, over the 11 classes. Each is dry-run at the base before the GO: AC1 reads FAIL at base, AC2 reads
FAIL at base (nothing written at the new home since), AC3 reads PASS at base by construction.

## 5. WHEN YOU ARE DONE

Close the change-management entry; flip `<status>` to `complete` in the SAME commit as the proof instance; report once.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** staged. Class WORLD. The seam measured at the cut (L5_FACTS section 4): one `BD_S3_BUCKET`-derived
`S3_BUCKET` serves every read and write of the gold scripts, 42 importers in the fixture count. A bucket edit would move
silver reads as well, so the form of this act (a per-output bucket in each writer, or a producer migration of its own)
is read from `FB-f-6`, not assumed. The producers rewrite the served keys daily in a window that closes about 06:15Z; the
act is timed so no producer run straddles it. After this act and before act 4 the router still serves the OLD home, so
users read the last pre-act day: the window is one window, acts 2-4 close together (round-2 analysis, section 2 item 1).

<status>staged</status>
<round>3</round>
<to_id>ADVI_FIRMBKTS.TO-FB-f-9</to_id>
<slot>~16</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
