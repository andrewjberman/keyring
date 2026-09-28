# NFRA_OPLGTW task order -- `OG-o-3` -- ROUND 2 (E3): repair the operator runbook's cross-references and its rollback paragraph

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-o-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~13</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- text-only edit of one runbook; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS operation, policy or role.
comp-adversary: DECLARED-NOT-APPLICABLE -- the defects are graded (3.0.0_SA_CVO~O, row NFRA_OPLGTW-Z-C-S11, OGO2-J1 FAIL); this cell repairs exactly them.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-o-3` (decomposition addendum R2-E, item E3)

The operator follows `infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md` during the walkthroughs, so it must
send the operator to the right place. `3.0.0_SA_CVO~O` graded the round-1 runbook FAIL at L9 (OGO2-J1). The reason,
verbatim: *"at their named moments the cross-references send the operator to the wrong place. Onboarding step 4 (:47)
says the admin command is in 'section 7' -- section 7 is ROLLBACK, and the command is in 6.1. Step 5 (:49) says the
disclosure is in 'section 10' -- it is section 8. Section 4.2 (:115) sends grant revision to 'section 7'. :11 claims
ten sections; there are nine (0-8). Section 7.2 (:252) states the live release 1764e54a16 has NO valid rollback, but
the service now runs 6a98a0553a and prior releases fe94911257 and 110d93fb73 carry the guard, so that paragraph
misstates the release it governs. Remedy: a text-only correction of the four references and 7.2."*

The runbook at the issuance base (317 lines, last changed @6c37cc6b00). Its headings are `## 0` .. `## 8`, with
`### 4.1-4.3`, `### 6.1 Grant change`, `### 6.2 Revocation`, `### 7.1-7.3`. The lines to repair (print them first):
- `:10-12` -- "All ten sections below are the ten this cell must carry: named readers and moments; onboarding; connector
  add or reuse; member connection; troubleshooting; audit read / status summary; grant change; revocation; rollback;
  disclosure." There are NINE numbered sections carrying those ten topics; grant change and revocation share section 6.
- `:47` -- "4. Activate the approved scope with the administration command (section 7 names it exactly)". Correct: 6.1.
- `:49` -- "5. Tell Menachem the disclosure (section 10) as part of onboarding, not after." Correct: 8.
- `:115` -- "the identity/data administrator issues a NEW grant revision (section 7)". Correct: 6.1.
- `:250-265`, section 7.2's first paragraph -- it names `1764e54a16` as the live release and says it "has NO VALID
  ROLLBACK under this section".

**What 7.2 must say now.** The rollback rule stands as written (R-56): a target must (i) carry the per-principal guard
`infra/aws/ec2/opal-gateway/app/data_entitlement.py` AND (ii) be a release actually deployed and proven on the host.
The deploy record is `infra/aws/ec2/EC2_MANIFEST.json`, `services.opal-gateway`: each commit of that file records one
`deployed_commit`. Read at the issuance base (re-read it at your HEAD; it moves when a release lands):
- `deployed_commit` `6a98a0553a` (2026-09-27T22:17:33Z) -- live;
- the prior recorded releases, newest first: `fe94911257` (09-27 18:43:56Z), `110d93fb73` (09-27 05:03:54Z),
  `df724ef284`, `c5f8099440`, ... `1764e54a16` (09-18). `git cat-file -e <c>:infra/aws/ec2/opal-gateway/app/data_entitlement.py`
  succeeds for 6a98a0553a, fe94911257, 110d93fb73 and 1764e54a16.
Rewrite the paragraph so that it (a) names the live release by reading the manifest, (b) names at least the newest
prior recorded release that carries the guard as the valid rollback target, with its deploy time, and (c) tells the
operator to re-read `EC2_MANIFEST.json` before acting, because a later release in this round moves both. Keep the
general procedure below the paragraph unchanged. Do not claim any target that is not in the manifest history. In
section 7.2's first two paragraphs, write in backticks ONLY the live commit and the rollback targets: the check reads
every backticked hash there as one of the two, so a historical hash (for example `d88cd32d0c`, which the current text
names) is written without backticks or moved below those paragraphs.

**Keep these anchor phrases** in the three repaired sentences so the checks find them: "administration command"
(onboarding step 4), "the disclosure" (onboarding step 5), "NEW grant revision" (4.2).

Touch nothing else in the runbook. `tests/acceptance/WALKTHROUGH_PROTOCOL.md` is not in this cell.

## 2. BOUNDS

1. Text only. You run no rollback, deploy, grant change or AWS call. Your write surface is `<paths>` below.
2. You work in the worktree named in your identity line; commit there under your serial with `.tools/safe-commit.sh`.
   Never push, merge, rebase, `stash`, `checkout --` or `clean`.
3. Spec frozen. A criterion you cannot meet as written is REFUSED and reported with its measurement. Anything off-spec is
   ONE surprise row, and you keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~13/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md`, id
`NFRA_OPLGTW-Z-W13-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-o-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/rb.AC1.sh; echo "exit=$?"</invocation><expect>anchored references correct 3 of 3 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-o-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/rb.AC2.sh; echo "exit=$?"</invocation><expect>7.2 names live=yes; targets named>=1, without guard 0, not in manifest history 0; NO VALID ROLLBACK sentences 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-o-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/rb.AC3.sh; echo "exit=$?"</invocation><expect>dangling section references 0; stated section count equals headings -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="J1" cell_refs="OG-o-3" judgment="true"/>
</proof_of_spec>

- `AC1` -- the three repaired references name 6.1, 8 and 6.1.
- `AC2` -- section 7.2's live release and rollback targets agree with the manifest's deploy history.
- `AC3` -- every "section N" reference resolves to a heading, and the preamble's section count equals the headings.
- `J1` -- graded at L9 by `3.0.0_SA_CVO~O` on the new bytes (the re-grade of OGO2-J1): an operator can execute each
  section at its named moment without other context. RECORD; NO VERDICT.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~13/NFRA_OPLGTW.TO-OG-o-3.runbook-text-repair.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. `J1` is recorded `UNVERIFIABLE-BY-INSTRUMENT`, naming
`3.0.0_SA_CVO~O` at L9; a PASS or FAIL on it is invalid. Flip `complete` only when AC1-AC3 PASS by output. Report once,
in your final message.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Lands BEFORE `OG-v-7` (E1) is handed, because the operator follows this text in the walkthrough (edge o-3 -> v-7).
  Slot ~13, queue position 1 (then `OG-m-1`, then `OG-h-1` last).
- The live-release facts in section 1 were read from `EC2_MANIFEST.json` at the issuance base (18 recorded opal-gateway
  releases, newest 6a98a0553a). `6a98a0553a` differs from `fe94911257` only in `deploy-to-ec2.sh`
  (SPRINT_VIEW_ALLOWED_EMAILS), so a host md5 over app files cannot tell them apart (record e992df46c4).
- `<risk>` WORLD is GATE (xii)'s floor (an `infra/` path); the cell edits text only.
- Base dry-run: see the issuance commit's check lines.

<status>pending</status>
<round>3</round>
<slot>~13</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
