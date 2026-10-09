# AMGT_RESAPP task order -- `AMGT-ll-3` -- REDEPLOY THE SCOPED API CARRYING THE FAILED-DESCRIPTION WITHHOLD AND AMGT_CORPUS DOSSIER METHOD /9 (NEVER /8)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ll-3</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~RA1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one code leg.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM, route, memory or schedule change; the function's code only.
comp-adversary: RUN at the cut -- box/dell1 HEAD carries lib/research/corpus/dossier.py at METHOD amgt-corpus-dossier/8, which CTO~DELL1 ruled NEVER served (AMGT_CORPUS/ledger/NEVER_WIDEN_ROUND41_AQ5_CTO_HALF.md ADDENDUM 1): a build from HEAD today ships /8. The build pin must carry /9. Since the live pin 4c929a2ffe the closure roots also moved lib/opal_naming.py and infra/logic/registry (other projects).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- `AMGT-ll-3` (round 87, decomposition s.95)

CTO~DELL1 round-86 analysis R1 (deploy half) + AMGT_CORPUS leg p (`2.0.0_SA_COO~C1` msgs 2900, 2970). One CODE leg on us-east-1
`opal-amgt-scoped-api`, built from a DETACHED worktree at the build pin the GO names: a box/dell1 commit carrying AMGT-ll-1 and
AMGT_CORPUS's dossier.py at METHOD `amgt-corpus-dossier/9`. Before the apply, print the CONTENT-DIFF of the built package against the
kept live package (`HZoC2x`, downloaded and hash-checked); any member the pair's BLAST RADIUS does not admit is a STOP. Rollback: the
kept live package through the module, one `safe-apply`, same session. Change-management entry opened before, closed after.

## 2. BOUNDS

1. The act and nothing else: this function's code; no IAM, route, memory, schedule or store write.
2. No S3 delete, ever.
3. No Bloomberg call. No `bun`, `npm` or `pip install`.
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
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ll-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round87_prep/checks/r87_withheld.py" --crit AC1; echo "exit=$?"</invocation><expect>on the live function no FAILED description carries a sentence and every drafted name answers with the section; W1-W2 PASS; R87 WITHHELD AC1: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ll-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round87_prep/checks/r87_dossier.py" --want amgt-corpus-dossier/9; echo "exit=$?"</invocation><expect>the deployed package's dossier.py reads METHOD amgt-corpus-dossier/9 and not /8; P1-P2 PASS; R87 DOSSIER: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ll-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round84_prep/checks/r84_listing.py" --crit AC1 --where deployed; echo "exit=$?"</invocation><expect>a typed ASML still resolves to ASML_NA_Equity, Micro still lists, the other answers byte-equal; R84 LISTING AC1: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback and base-vs-new CodeSha256 as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/AMGT_RESAPP.TO-AMGT-ll-3.redeploy-withheld-description-and-dossier-9.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry. Report once:
- the build pin and its dossier.py METHOD;
- the content-diff in full, each member with its admission;
- base and new CodeSha256;
- every criterion's output lines;
- the change-management entry's slug and state;
- any row.

Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-86 analysis R1. Pair: NEW -- COO half `ledger/NEVER_WIDEN_ROUND87_LL3_COO_HALF.md` (this issuance); CTO~DELL1's half owed. STAGED: GO waits on AMGT-ll-1 merged AND AMGT_CORPUS round 42 landing dossier /9 (C1 sends the hash). Checks dry-run at the base: AC1 base FAIL as expected (NU FAILED with 1); AC2 base FAIL as expected (deployed /7); AC3 base PASS (a bound).

<status>staged</status>
<round>87</round>
<slot>0.7.0_AE_CloudOps~RA1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
