# TO NFRA_OPLGTW.TO-OG-v-3 -- real-data expected answers, sealed by hash

<to_id>NFRA_OPLGTW.TO-OG-v-3</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~6</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-15</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.2 @f0aa50dbc0 (ADMITTED) | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.0 | **Decomp cell:** `OG-v-3` | **outcome_ref:** FWD-2 | **depends_on:** `OG-c-2` | **slot:** ~6, queue position 3

---

## WORKER FACE

### THE CELL

`OG-v-3` -- **real-data expected answers, sealed by hash.** For each real-data question in `OG-v-1`'s
`WALKTHROUGH_PROTOCOL.md`, compute the expected answer from the qualified silver objects `OG-c-2` produced, with an
instrument independent of the Gateway's query engine, BEFORE anyone asks the Gateway. Commit only salted hashes; keep the
values outside the repository.

FWD-2, verbatim: *"DONE WHEN: EXERCISED -- chosen questions and date comparisons are checked against independently
prepared examples. ACCEPT: Menachem gets understandable holdings and balance answers for the master and date he selected,
with SmartX and BlackDiamond clearly separate and without adding overlapping balances or different days together.
PROOF: Deliberately chosen examples with independently known answers, including a comparison between masters and between
dates."* And the PRD's evidence rule: *"never tokens/customer data in repository evidence."* The certified rectangle's
boundary question 13 (S3-data) is answered here too: *"Are date alignment, metric units, balance overlaps and future
security join uniqueness established? ... obtain sanitized data-owner evidence for value/partition date consistency and
key uniqueness before rollout."*

**Where the values live:** `C:/tmp/nfra-oplgtw-sealed/expected/` (outside the repository), with the salt beside them.
Retention: kept until `OG-v-4` has graded, then removed by the COO at that drain; state this in your result file. The
qualified object keys and VersionIds are in `OG-c-2`'s result file under
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~4/`. Read each object by its VersionId, read-only.

**Read:** `infra/aws/ec2/opal-gateway/tests/acceptance/WALKTHROUGH_PROTOCOL.md` (the questions); `OG-c-2`'s result file;
the PRD's "C3"; the contract's `fields` and `additive_fields`. **Do not open `app/integrations/schwab/`.**

**The probe** for every mechanical criterion is `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v3.py`,
taking the short id, printing its measurement with its denominator, then exactly one line `VERDICT: PASS-OGV3-AC<n>` or
`VERDICT: FAIL-OGV3-AC<n> <reason>`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGV3-AC1" cell_refs="OG-v-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v3.py AC1</invocation><expect>(?m)^VERDICT: PASS-OGV3-AC1(?![0-9])</expect></criterion>
`OGV3-AC1` -- each chosen question's expected answer is computed from qualified VersionIds (after `OG-c-2`) by an instrument independent of the engine, named.

<criterion id="OGV3-AC2" cell_refs="OG-v-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v3.py AC2</invocation><expect>(?m)^VERDICT: PASS-OGV3-AC2(?![0-9])</expect></criterion>
`OGV3-AC2` -- only a salted hash of each expected answer and the VersionIds used are committed.

<criterion id="OGV3-AC3" cell_refs="OG-v-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v3.py AC3</invocation><expect>(?m)^VERDICT: PASS-OGV3-AC3(?![0-9])</expect></criterion>
`OGV3-AC3` -- no customer value appears in any committed file of the cell, by a scan against the sealed values.

<criterion id="OGV3-AC4" cell_refs="OG-v-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v3.py AC4</invocation><expect>(?m)^VERDICT: PASS-OGV3-AC4(?![0-9])</expect></criterion>
`OGV3-AC4` -- the location outside the repo that holds the values, and its retention, are stated.

<criterion id="OGV3-J1" cell_refs="OG-v-3" judgment="true"/>
`OGV3-J1` -- graded at L9 by 3.0.0_SA_CVO: the questions exercise date alignment, units and balance-field overlap on real snapshots (boundary question 13). RECORD; NO VERDICT.

<expected_criteria>OGV3-AC1, OGV3-AC2, OGV3-AC3, OGV3-AC4, OGV3-J1</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/` and this order's own file (for the `<status>` flip). Outside the repository you write only under `C:/tmp/nfra-oplgtw-sealed/`. Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Customer data stays out of the repository.** Values, account IDs and names are never committed, printed into a result file or echoed into a row. Hashes and VersionIds only.
- **Read only.** GetObject by VersionId on the qualified silver objects; no write, copy or delete in AWS.
- **Independence.** You never read or import `app/integrations/schwab/`.
- **Branch.** You work in the worktree named in your identity line, cut from `CLOUD` at hand-off (after `OG-c-2` merged). Never push, merge, rebase, `checkout --` or `clean`.
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
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 @8768f46770, cell `OG-v-3`, round 1 (section 3, S10; section 2 question 13).
<owned_cells>OG-v-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGV3-AC1` .. `OGV3-AC4`, `OGV3-J1` (5). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/NFRA_OPLGTW.TO-OG-v-3.sealed-real-expectations.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @f0aa50dbc0, decomp_ref.doc the
decomposition @8768f46770, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGV3-AC1,OGV3-AC2,OGV3-AC3,OGV3-AC4,OGV3-J1` BEFORE the `complete`
flip. Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming
`3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.** Result file `sealed-real-expectations.result.md`
beside it (`SEALED_EXPECTED.json` holds the hashes). **Flip `complete` only when every MECHANICAL criterion PASSES by
output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers scanned (C1 230, C2 8, C3 12, C4 21, C5 334), 27 gates armed, none naming NFRA_OPLGTW. This cell waits on OG-c-2, which is HELD on G-B.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell reads objects with the issuing laptop's existing read access and adds no AWS operation, policy, principal or role.
comp-adversary: RUN at L5 on the PRD v0.2 (@f0aa50dbc0) -- 4 of 4 cited commits verified; 7 cited paths, 6 stable, 1 GONE (an external RFC URL parsed as a repo path). Blindness stated: T11, filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant).
</preflight>

Seating: slot ~6, queue position 3, handed after `OG-c-2` merges; a slot that authored no engine code. Round 1 of
NFRA_OPLGTW, issued by `2.0.0_SA_COO~O` (seated msg 96971, LD-0567). Decomposition v1 @8768f46770.
