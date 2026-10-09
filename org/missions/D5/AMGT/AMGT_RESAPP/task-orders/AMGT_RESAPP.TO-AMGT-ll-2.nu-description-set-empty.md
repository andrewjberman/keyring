# AMGT_RESAPP task order -- `AMGT-ll-2` -- NU'S STORED COMPANY DESCRIPTION IS SET EMPTY, ONE DRAFTING KEY, IN PLACE, UNDER KK-3'S PAIR

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ll-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~347</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one in-place write.
comp-iam: RUN by round 86's kk-3 (the drafting/v1 grant) -- no grant moves.
comp-adversary: RUN at the cut -- the one sentence kk-3 kept ("Item 4.B") is a Colombia launch metric, not a description; the section's own verdict reads FAILED. Edit only company_description; never rebuild from the stored analysis.
EGRESS CLASS, declared: NONE (no fetch, no model call).
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-347`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ll-2` (round 87, decomposition s.95)

CTO~DELL1 round-86 analysis R2. IN PLACE, ONE key `s3://opal-data-harvest/drafting/v1/NU_US_Equity.json`: its `company_description`
section's `sentences` becomes `[]`; nothing else in the object changes. Build it locally first under `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~347/edited/`, from the
CURRENT stored object (read it, never rebuild), and print a JSON diff showing that section alone changed. Open the change-management
entry (`python .tools/deploy_ledger.py open ...`) BEFORE the write, record the prior VersionId in it, write once, list versions
before and after. Rollback is a re-put of the prior VersionId's bytes, never a delete. Close the entry.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W347-S<k>` (dell1's registered coordinate is D1), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. The act and nothing else: this one drafting key; no other key, no deploy, no schedule.
2. No S3 delete, ever.
3. No fetch, no model call, no Bloomberg call. No `bun`, `npm` or `pip install`.
4. Standing: no push of shared branches.
5. (dell1 IAM parity, CTO~DELL1 ADDENDUM 3 @947dd446e5) A send that writes a firm data bucket, or assumes the 49F principal
   outside the runner's own job, is told to the laptop FIRST.
6. Every send to mdpf-daily-runner is reported after the fact, with its command id and purpose.
7. 49 Financial data never goes into another firm's tree.
8. CLIENT DATA (0.0.0_AB_MSTR~DELL1 msgs 2720/2747/2766/2804): never open, search, copy or `git show` any
   `org/**/W73_S*_EVIDENCE.json`, the COTBKF ~74 / ~66 / ~70 cottonwood manifests, or the IRPT_DASHBD tie-out files, in the tree or
   in history. Search only inside named paths, never the whole repository.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~347/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ll-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round87_prep/checks/r87_withheld.py" --crit NU --keys NU_US_Equity; echo "exit=$?"</invocation><expect>on the live function NU serves 0 company_description sentences; N1 PASS; R87 WITHHELD NU: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ll-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round85_prep/checks/r85_sentences.py" --crit AC1 --where deployed --exclude-section company_description --base-file "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round86_prep/checks/r86_sentences_base.json"; echo "exit=$?"</invocation><expect>on the live function, outside company_description, no sentence glued or restated over the five names and none below the pre-act base; S1-S3 PASS; R85 SENTENCES AC1: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~347 <0.9.0_WK_AMGT_RESAPP~347@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~347/AMGT_RESAPP.TO-AMGT-ll-2.nu-description-set-empty.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- prior and new VersionIds and the before/after version listing;
- the local JSON diff (one section);
- every criterion's output lines;
- the change-management entry's slug and state;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-86 analysis R2, under kk-3's pair (COO @1380a0f2cd + its ADDENDUM 1 in this issuance; CTO half signed, conditions 4-5). STAGED behind AMGT-ll-1's report (ll-1's AC2 needs NU's FAILED sentence live). Checks dry-run at the base: AC1 base FAIL as expected (NU 1 sentence); AC2 base PASS (a bound).

<status>staged</status>
<round>87</round>
<slot>0.9.0_WK_AMGT_RESAPP~347</slot>
<fabric>dell1</fabric>
<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
