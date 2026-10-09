# AMGT_RESAPP task order -- `AMGT-jj-4` -- PUBLISH THE NAME LIST WITH MEASURED ISSUER CIKS AS A NEW DATED KEY, UNDER ITS OWN PAIR

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-jj-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~341</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one hand-run publish.
comp-iam: RUN by round85_prep/GROUP_LISTING_BUILD_NOTES.md -- the writer's existing grant on crosswalk/v1/; no grant moves.
comp-adversary: RUN at the cut -- the live function reads the LATEST crosswalk/v1/ key at request time, so the published list is served the moment it lands; the deployed code ignores `issuer`, so served answers stay as today until AMGT-jj-5 redeploys.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-341`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-jj-4` (round 85, decomposition s.93)

Publish the list AMGT-jj-3 builds as ONE new dated key `crosswalk/v1/<date>.json` with the crosswalk's own `--write-pool` path
(union-first; put-if-absent by date), on the code merged at the GO's commit. Before the write, record the prior latest key and its
VersionId in the change-management entry and list `crosswalk/v1/`; after it, list again and write the diff into the entry's leg
(one new key, nothing else). Rollback, never a delete: a newer dated key re-carrying the prior document.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W341-S<k>` (dell1's registered coordinate is D1), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. The act and nothing else: one new key under `crosswalk/v1/`, no other store write, no deploy, no schedule.
2. No S3 delete, ever.
3. No Bloomberg call. No `bun`, `npm` or `pip install`.
4. Standing: no push of shared branches.
5. (dell1 IAM parity, CTO~DELL1 ADDENDUM 3 @947dd446e5) A send that writes a firm data bucket, or assumes the 49F principal
   outside the runner's own job, is told to the laptop FIRST.
6. Every send to mdpf-daily-runner is reported after the fact, with its command id and purpose.
7. 49 Financial data never goes into another firm's tree.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~341/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-jj-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round85_prep/checks/r85_crosswalk.py" --crit AC1; echo "exit=$?"</invocation><expect>the latest stored name list drops no record of the prior one, both ASML listings carry measured issuer.cik 937966, every issuer.cik is measured with a source, the four other 20-F names carry their filer CIKs; C1-C4 PASS; R85 CROSSWALK AC1: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-jj-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round84_prep/checks/r84_store.py" --key ASML_NA_Equity,BABA_US_Equity,NU_US_Equity,PBR_US_Equity,SAP_GY_Equity --crit AC2 --where deployed; echo "exit=$?"</invocation><expect>every 20-F name's live /thesis still answers 200 from its business item in English (no regression from the new list); R84 STORE AC2 ALL: YES 5 of 5; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~341 <0.9.0_WK_AMGT_RESAPP~341@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~341/AMGT_RESAPP.TO-AMGT-jj-4.publish-the-name-list-with-issuer-ids.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- the prior and new crosswalk keys and VersionIds, record counts, the before/after listing diff;
- every criterion's output lines;
- the change-management entry's slug and state;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-84 analysis item 3 (hop 2 of 3). STAGED: waits for AMGT-jj-3 merged and a NEW pair (COO + 1.0.0_SA_CTO~DELL1; writer census N = 3 entry points through write_pool). Checks dry-run at the base: AC1 base FAIL (0 of 243 carry issuer); AC2 base PASS (a bound).

<status>staged</status>
<round>85</round>
<slot>0.9.0_WK_AMGT_RESAPP~341</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
