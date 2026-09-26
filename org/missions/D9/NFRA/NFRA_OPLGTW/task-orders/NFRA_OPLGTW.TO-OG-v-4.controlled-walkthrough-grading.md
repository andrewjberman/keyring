# TO NFRA_OPLGTW.TO-OG-v-4 -- grading the controlled-identity walkthrough

<to_id>NFRA_OPLGTW.TO-OG-v-4</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~6</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-15</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.2 @f0aa50dbc0 (ADMITTED) | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.0 | **Decomp cell:** `OG-v-4` | **outcome_ref:** FWD-1, FWD-3 .. FWD-8 | **depends_on:** `OG-r-2`, `OG-o-2`, `OG-i-3`, `OG-v-3`; **HELD on gates G-C and G-D** | **slot:** ~6, queue position 4

---

## WORKER FACE

### THE CELL

**THIS ORDER IS HANDED TWICE. PHASE 1 RUNS WHILE G-C AND G-D ARE ABSENT; PHASE 2 RUNS AFTER THEY ARE AT HEAD.**
The order is NOT re-cut and no new order exists -- one order, two hand-offs, exactly as `OG-r-1` was handed twice.

- **PHASE 1 -- RE-SEAL (`OGV4-AC8`).** `OG-v-3`'s sealed expectations are UNUSABLE: the salt they hash against lived
  ONLY at `C:/tmp/nfra-oplgtw-sealed/expected/SALT.txt` and that tree is GONE (row `NFRA_OPLGTW-S42`; the whole
  out-of-repo surface, 16 of 16 paths, row `NFRA_OPLGTW-S43`). You re-seal. **PHASE 1 IS VALID ONLY WHILE THE
  WALKTHROUGH HAS NOT HAPPENED**, so it is handed while G-C and G-D are ABSENT and your artifact must RECORD that
  absence at a named commit -- see `OGV4-AC8`. You then STOP and report; you are re-handed for phase 2.
- **PHASE 2 -- GRADING (everything else in this order).** Handed only once G-C and G-D are at HEAD.

`OG-v-4` -- **grading the controlled-identity walkthrough.** A person at a work browser has run the walkthrough in
`OG-v-1`'s protocol against the released Gateway, with a controlled identity and its approved synthetic grant, and the
record is at HEAD. You grade that record against the protocol, the audit sink and the sealed expectations. You perform
none of the walkthrough yourself.

The two inputs, both required at HEAD before you are spawned:
- **G-C** `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/1.0.0_SA_CTO~A/G-C_CONTROLLED_IDENTITY_AND_GRANT.md` -- the
  controlled identity's verified `tid`/`oid` and its approved grant (owner `1.0.0_SA_CTO` -- re-assigned
  from `1.0.0_SA_CTO~A`, which is not seated, by CTO ruling msg 98451 @`a0e4748ac2`, carried here by the
  issuer under Rule 27. ⛔ THE PATH ABOVE IS UNCHANGED AND STILL READS `1.0.0_SA_CTO~A/` DELIBERATELY:
  it is pinned by `SEALED_EXPECTED.json`'s pre-seal absence check at commit `15edf9f07b` and by
  `probes/og_v4.py:27` `GC_PATH`, so moving it would break the seal PHASE 1 exists to hold -- row S54).
  ⭐ **AND THE EVIDENCE-SUPPLYING PARTY IS NOW ASSIGNED: `0.7.0_AE_CloudOps`** -- ANDREW-DIRECT
  2026-09-20 ~18:0xZ, VERBATIM *"0.7.0_AE_CloudOps is the admin. Should be the default admin for all
  testing tasks of cloud projects/workflows/resources."* (record
  `org/tier1_exec/2.0.0_SA_COO/ANDREW_DIRECT_20260920_180xZ_O_IDENTITY_ADMIN_IS_CLOUDOPS_DEFAULT_FOR_CLOUD_TESTING.md`
  @`768e6df290`). The decomposition's G-C owner column names TWO parties -- the CLOSING owner and
  *"the identity administrator supplying the evidence"* -- and R-OG-26 measured that the PRD named
  the second role and never assigned it. **It is assigned now.** ⛔ This does NOT change the closing
  owner, does NOT move the path, and does NOT make G-C exist: it is still a person's act against the
  live tenant, and Andrew's word was *"we will handle that shortly"*.
- **G-D** `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/CONTROLLED_WALKTHROUGH_RECORD.md` -- the
  walkthrough record, in `OG-v-1`'s template.

**IN PHASE 2**, if either is absent, file a BLOCKING row and stop. **IN PHASE 1 THE OPPOSITE HOLDS: if either is
PRESENT, the re-seal's only property is already lost -- file a BLOCKING row and stop, and do NOT re-seal.**

The protocol and expectations are `infra/aws/ec2/opal-gateway/tests/acceptance/WALKTHROUGH_PROTOCOL.md` and
`A_ROWS.json` (`OG-v-1`); the sealed real-data hashes are **PHASE 1's re-sealed `SEALED_EXPECTED.json`** in this slot's deliverables (it
REPLACES `OG-v-3`'s, whose salt is gone -- `OG-v-3`'s file stays committed as history and is NEVER graded against),
and the operator's actual answers sit outside the repository at `%LOCALAPPDATA%/opal/og-salt/actual/`. The source-bucket
baseline is `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/BASELINE.json` (`OG-p-1`). Audit records
are read-only under `opal-mcp-audit` `audit/schwab/`.

The PRD's ACCEPT clauses this record is read against are FWD-3 through FWD-8 in its ENDPOINT section; quote each one you
grade in your result file.

**The probe** for every mechanical criterion is `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v4.py`,
taking the short id, printing its measurement with its denominator, then exactly one line `VERDICT: PASS-OGV4-AC<n>` or
`VERDICT: FAIL-OGV4-AC<n> <reason>`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGV4-AC1" cell_refs="OG-v-4"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v4.py AC1</invocation><expect>(?m)^VERDICT: PASS-OGV4-AC1(?![0-9])</expect></criterion>
`OGV4-AC1` -- every person-operated A-row of `OG-v-1`'s protocol has a recorded observation in the walkthrough record, denominator printed.

<criterion id="OGV4-AC2" cell_refs="OG-v-4"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v4.py AC2</invocation><expect>(?m)^VERDICT: PASS-OGV4-AC2(?![0-9])</expect></criterion>
`OGV4-AC2` -- every recorded server correlation resolves to a sanitized audit record carrying the expected decision.

<criterion id="OGV4-AC3" cell_refs="OG-v-4"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v4.py AC3</invocation><expect>(?m)^VERDICT: PASS-OGV4-AC3(?![0-9])</expect></criterion>
`OGV4-AC3` -- no audit record the walkthrough produced holds a disallowed field.

<criterion id="OGV4-AC4" cell_refs="OG-v-4"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v4.py AC4</invocation><expect>(?m)^VERDICT: PASS-OGV4-AC4(?![0-9])</expect></criterion>
`OGV4-AC4` -- the source-bucket readbacks after grant change, revocation and rollback equal `OG-p-1`'s baseline.

<criterion id="OGV4-AC5" cell_refs="OG-v-4"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v4.py AC5</invocation><expect>(?m)^VERDICT: PASS-OGV4-AC5(?![0-9])</expect></criterion>
`OGV4-AC5` -- the actual answers to RQ1-RQ6, each asked at the fixed business date `2026-09-15` per the protocol's section 4, hash-match `OG-v-3`'s sealed expectations, denominator 6 printed.

<criterion id="OGV4-AC6" cell_refs="OG-v-4"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v4.py AC6</invocation><expect>(?m)^VERDICT: PASS-OGV4-AC6(?![0-9])</expect></criterion>
`OGV4-AC6` -- for each master (`08242234`, `08335338`), the latest qualified date the record shows returned by A7's no-date request equals the newest `schwab/<master>/meta/complete/date=*.json` marker in `opal-data-assets` whose `closure.status` is `qualified` and whose LastModified precedes the recorded ask time, read-only, denominator 2 printed.

<criterion id="OGV4-AC7" cell_refs="OG-v-4"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v4.py AC7</invocation><expect>(?m)^VERDICT: PASS-OGV4-AC7(?![0-9])</expect></criterion>
`OGV4-AC7` -- for each master, the available-dates list the record shows returned by A7's no-date request contains `2026-09-15`, denominator 2 printed.

<criterion id="OGV4-J1" cell_refs="OG-v-4" judgment="true"/>
`OGV4-J1` -- graded at L9 by 3.0.0_SA_CVO: each walkthrough step's observation matches the protocol's expected observation. RECORD; NO VERDICT.

<criterion id="OGV4-J2" cell_refs="OG-v-4" judgment="true"/>
`OGV4-J2` -- graded at L9 by 3.0.0_SA_CVO: the record meets the ACCEPT clauses of FWD-3, FWD-4, FWD-5, FWD-6, FWD-7 and FWD-8. RECORD; NO VERDICT.

<criterion id="OGV4-AC8" cell_refs="OG-v-4"><invocation>cd <WS> && timeout 300 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v4.py AC8</invocation><expect>(?m)^VERDICT: PASS-OGV4-AC8(?![0-9])</expect></criterion>
`OGV4-AC8` -- (PHASE 1, the re-seal) a NEW `SEALED_EXPECTED.json` is produced in this slot's deliverables, computed from
the SAME version-pinned objects `OG-v-3` recorded (`qualified_objects_used[]`, each with its `key` AND `version_id`) by
the same instrument, with a FRESH salt written to `%LOCALAPPDATA%/opal/og-salt/expected/SALT.txt`; and **THE ARTIFACT
ITSELF RECORDS, AT THE MOMENT IT IS CUT, THE MEASURED ABSENCE OF G-C AND G-D AT A NAMED COMMIT** -- the commit-ish, both
paths, and the read that returned absent. **A VALID RE-SEAL AND A WORTHLESS POST-WALKTHROUGH ONE ARE BYTE-IDENTICAL
WITHOUT THAT RECORD**, which is the whole reason this criterion exists: the seal's only property is that expectations
were fixed BEFORE the result was observable, and a forward-looking claim is unfalsifiable at its own cut unless it is
bound to a fact readable at the event. The probe prints the new digests beside the old ones and states that they DIFFER
by construction (a new salt), never that the old ones were reproduced.

<criterion id="OGV4-AC9" cell_refs="OG-v-4"><invocation>cd <WS> && timeout 300 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v4.py AC9</invocation><expect>(?m)^VERDICT: PASS-OGV4-AC9(?![0-9])</expect></criterion>
`OGV4-AC9` -- (PHASE 2, AFTER `OGV4-AC5` has been graded) the salt and the expected-answer files are COMMITTED into this
slot's deliverables as drain evidence, and the probe RE-DERIVES every digest in `SEALED_EXPECTED.json` from the committed
salt plus the committed answers and prints the count that match against the denominator. **The secrecy of the salt
matters only until AC5 is graded; after that, an uncommitted salt is a permanently unguarded dependency for no benefit.**
This converts the out-of-repo window from "as long as the cell stays held" to "the span of one walkthrough", and leaves a
record the next reader can RE-DERIVE instead of trust. **ORDERING IS THE CRITERION: committing the salt BEFORE AC5 is
graded destroys the seal and FAILS this criterion** -- the probe checks AC5's recorded verdict exists first.

<expected_criteria>OGV4-AC1, OGV4-AC2, OGV4-AC3, OGV4-AC4, OGV4-AC5, OGV4-AC6, OGV4-AC7, OGV4-AC8, OGV4-AC9, OGV4-J1, OGV4-J2</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **G-C and G-D.** Both records at HEAD, or a BLOCKING row and a stop.
- **PHASE 1 WRITES, AND ONE OF ITS WRITES IS OUTSIDE THE REPOSITORY.** For `OGV4-AC8` only, your write surface
  ADDITIONALLY includes `%LOCALAPPDATA%/opal/og-salt/` (AMENDED: never `C:/tmp`, laptop 1.0.0_SA_CTO msg 101169) -- the out-of-repo bound `OG-v-3` carried, moved here
  because the re-seal cannot mint a salt anywhere else without destroying the property it exists to create. Nothing
  else outside the repository, ever.
- **AMENDED by the issuer (2.0.0_SA_COO~O, 2026-09-26 ~16:5xZ) on laptop 2.0.0_SA_COO~Y's hold (via MSTR~Z 16:41:57Z) and
  laptop 1.0.0_SA_CTO's ruling (msg 101169): the sealed tree lives under `%LOCALAPPDATA%/opal/og-salt/`, NEVER `C:/tmp`
  (the `C:/tmp` salt was lost, row `NFRA_OPLGTW-S42`). The ONE permitted edit to the instrument is
  `compute_expected.py:51`: `SEALED_DIR = "C:/tmp/nfra-oplgtw-sealed"` becomes
  `SEALED_DIR = os.path.join(os.environ["LOCALAPPDATA"], "opal", "og-salt").replace("\\", "/")` (import `os` if absent). No
  other line of the instrument changes; commit that one-line edit on its own, before the run, and cite it in the
  AC8 artifact. That is a path, not a reimplementation.
- **PHASE 1 RE-RUNS A COMMITTED INSTRUMENT; IT DOES NOT REIMPLEMENT ONE.** `OG-v-3`'s sealing script SURVIVES in this
  slot's deliverables at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/compute_expected.py` --
  it mints the salt (`secrets.token_hex(32)`), computes each RQ's answer from the version-pinned objects with pyarrow
  decode plus stdlib `decimal.Decimal`, writes the plaintext answers outside the repository and emits
  `SEALED_EXPECTED.json`. RUN THAT FILE. "The same instrument" is then provable rather than asserted, because it is
  the same file. If it cannot run as committed, that is a BLOCKING row naming the failure -- never a reimplementation.
- **You grade; you do not operate -- IN PHASE 2.** No sign-in, no connector act, no grant change, no rollback, no call to the Gateway as a user. Reads only: the records, the audit sink, the bucket settings, and (AC6) the closure markers under `schwab/<master>/meta/complete/` in `opal-data-assets`.
- **Customer data stays out of the repository.** Answers are compared by hash; no value is committed or printed.
  **THIS BINDS PHASE 1 HARDEST**, because phase 1 is the step that HANDLES the real answers: they are written only
  under `%LOCALAPPDATA%/opal/og-salt/expected/`, never into a deliverable, a row, a result file or a probe's stdout.
  `OGV4-AC9`'s later commit of those files is the ONE exception and it happens only after `OGV4-AC5` is graded --
  by then the walkthrough is over, the values are no longer a seal, and committing them is what makes every digest
  re-derivable.
- **Branch.** You work in the worktree named in your identity line, cut from `CLOUD` at hand-off. Never push, merge, rebase, `checkout --` or `clean`.
- **Interpreter.** Your venv `.venv-og` (`cd <WS> && py -3.12 -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt msal moto pytest`) serves every invocation. Never commit `.venv-og/` or `.scratch/`.
- **No egress off Opal infrastructure.** No call to Claude, an Anthropic endpoint, an interactive Entra sign-in or any vendor API.
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh`.
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and reported with its measurement -- never repaired, widened or satisfied by a route this order does not name. Anything off-spec is one surprise row, and you keep working.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_OPLGTW-W6-S<k>`. Keep working after filing.
- **The preloaded context.** Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 @8768f46770, cell `OG-v-4`, round 1 (section 3, S10; section 6 G-C, G-D).
<owned_cells>OG-v-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGV4-AC1` .. `OGV4-AC9`, `OGV4-J1`, `OGV4-J2` (11). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/NFRA_OPLGTW.TO-OG-v-4.controlled-walkthrough-grading.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @f0aa50dbc0, decomp_ref.doc the
decomposition @8768f46770, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGV4-AC1,OGV4-AC2,OGV4-AC3,OGV4-AC4,OGV4-AC5,OGV4-AC6,OGV4-AC7,OGV4-AC8,OGV4-AC9,OGV4-J1,OGV4-J2` BEFORE the
`complete` flip. Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming
`3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.** Result file
`controlled-walkthrough-grading.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by
output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers scanned (C1 230, C2 8, C3 12, C4 21, C5 334), 27 gates armed, none naming NFRA_OPLGTW. This cell is HELD on project gates G-C (owner 1.0.0_SA_CTO, re-assigned from 1.0.0_SA_CTO~A by ruling 98451 @a0e4748ac2) and G-D (the operator's record, landed by 2.0.0_SA_COO~O); the vendor-egress moratorium is why the walkthrough is a person's act and not a worker's.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell reads records, the audit sink and bucket settings with existing read access; it adds no AWS operation, policy, principal or role.
comp-adversary: RUN at L5 on the PRD v0.2 (@f0aa50dbc0) -- 4 of 4 cited commits verified; 7 cited paths, 6 stable, 1 GONE (an external RFC URL parsed as a repo path). Blindness stated: T11, filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant).
</preflight>

Seating: slot ~6, queue position 4. **TWO HAND-OFFS.** PHASE 1 (`OGV4-AC8`, the re-seal) is handed AS SOON AS
POSSIBLE and REQUIRES G-C and G-D to be ABSENT -- it is the one act in this order whose validity EXPIRES when the
walkthrough happens. PHASE 2 (every other criterion) is handed after `OG-r-2`, `OG-o-2`, `OG-i-3` and `OG-v-3` merge AND
the G-C and G-D records are at HEAD. Round 1 of NFRA_OPLGTW, issued by `2.0.0_SA_COO~O` (seated msg 96971, LD-0567).

Amended 2026-09-18 ~12:5xZ by `2.0.0_SA_COO~O` on `1.0.0_SA_CTO`'s re-seal ruling (msg 97968 @`f16e7f02ea`), which
ordered the re-seal to land BEFORE G-C and chose AMENDING THIS ORDER as the vehicle precisely because an amendment adds
no order and LD-0521's open-order arithmetic is untouched. **THE VEHICLE IS ADOPTED WITH ONE CORRECTION THIS ISSUER OWES
IT: the ruling placed the re-seal as this order's "FIRST STEP", and this order's own seating clause hands its worker only
once G-C and G-D are AT HEAD -- G-D IS THE WALKTHROUGH RECORD, so a first step would have executed AFTER the walkthrough
and been exactly the worthless re-seal the ruling exists to prevent.** The fix keeps the ruling's vehicle and its
sequencing: ONE order, TWO hand-offs, phase 1 gated on those records being ABSENT. The precedent is this project's own --
`OG-r-1` was handed, drained, amended and re-handed within one order. Both of the ruling's substantive requirements are
built: the absence-at-a-named-commit record (`OGV4-AC8`) and the salt committed as drain evidence after AC5 is graded
(`OGV4-AC9`). Two criteria added, none removed or re-cut; no grant changed; no new order, so the open-order count is
unchanged.

Amended AGAIN minutes later, same issuer, BEFORE any hand-off, because the amendment above ordered work this order's
own BOUNDS forbade. **This order grants writes to the `<paths>` block, the slot's deliverables and its own file --
and `OGV4-AC8` must write a salt to `%LOCALAPPDATA%/opal/og-salt/`, which none of those cover; its "Reads only" bound
forbids writing at all.** A worker handed phase 1 would have been RIGHT to file a BLOCKING row on the first act and
stop. The grant is restored from `OG-v-3`, which carried exactly this out-of-repo bound, and the reads-only clause is
scoped to phase 2. Found by checking the order's BOUNDS against the work just ordered, which is the check the first
amendment skipped: A NEW CRITERION IS NOT ORDERED UNTIL ITS GRANT IS READ. Also named here rather than left implicit:
`compute_expected.py` -- `OG-v-3`'s actual sealing instrument -- IS COMMITTED and survives the loss of everything it
wrote, so the re-seal is a RE-RUN of a committed file and "the same instrument" is provable instead of asserted. Decomposition v1
@8768f46770. After this cell drains, the COO removes `%LOCALAPPDATA%/opal/og-salt/` (the retention `OG-v-3` states), and NOT before phase 2 is graded.

Amended 2026-09-17 ~15:0xZ, before hand-off, by `2.0.0_SA_COO~O` on `1.0.0_SA_CTO` ruling R-OG-12 (msg 97602
@df750f1e26; row `NFRA_OPLGTW-W6-S5`): AC5 grades RQ1-RQ6 at the fixed date `2026-09-15`; AC6 and AC7 grade one live,
unsealed no-date request per master, so PRD C3's explicit-latest coverage stays in the walkthrough and cannot drift. The
protocol edit rides `TO-OG-o-2`, which precedes this cell (see that order's record). No criterion removed.
