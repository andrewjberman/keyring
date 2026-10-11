# NFRA_OPLGTW task order -- `OG-db-1` -- drain the transcript-allowlist deploy hunk back onto trunk (round-34 E6)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-db-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-db-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~54</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a source edit on trunk; no deploy, no schedule touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no identity, role or policy is read or changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z's round-33 analysis row Z-S85 ruling (org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round33.md @2672b8d28a, section 2).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-db-1` (decomposition addendum R3-T.42, E6)

The live gateway's deploy script reads `data/transcripts/scripts/teams/meeting_allowlist.json` into
`TRANSCRIPT_MEETING_ALLOWLIST`. The live release `c3af8687e4` has 5 references to that file in
`infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`; trunk (box/sitez HEAD) has 0 and writes the allowlist EMPTY. A release
cut from trunk would therefore silently revoke the 4-meeting allowlist. The hunk was built as OG-tl-1, and the deployed
release is branch `rel-nfra-oplgtw-tl1b` @765fcfb239 (base 4514246d65..; read its diff with
`git diff 765fcfb239~1 765fcfb239 -- infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`, and the original at `78afad4283`).

1. Apply that allowlist hunk to trunk's `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`. Do it 3-way over HEAD's lines:
   - the json read block;
   - the count-4 refusal;
   - ONE `TRANSCRIPT_MEETING_ALLOWLIST=%s` in the `.env` printf, with ONE argument.

   HEAD's printf already carries keys the live release lacks: E2's `ADVI_FEE_STATEMENT_S3_ROOT`, and the unreleased
   `.pptx` pair's market_update key. Keep every one of them; drop no key.
2. Do not change anything else in the file. Make no deploy, run no script and touch no AWS resource.

## 2. BOUNDS

- Write only `deploy-to-ec2.sh` and your deliverables folder.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; run the deploy script; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/deploy-to-ec2.sh
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W54-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-db-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r34/checks/db1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)meeting_allowlist\.json reads: HEAD [1-9]\d*, live [1-9]\d* .*bash -n: yes.*missing 0 \[\].*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: trunk reads the allowlist the way the live release does, the script parses, and no `.env` key is dropped.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-db-1.allowlist-drain-back.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> AC1 --governing-order <this order>`, flip the ONE `<status>` tag to
`complete` only if AC1 PASSES, and report once. Your next order follows on this same slot.
`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~54/`.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 34, cut on 1.0.0_SA_CTO~Z's round-33 analysis @2672b8d28a. This cell runs FIRST in the round; row Z-S85's
  disarm (releases cut on the live ref only) stands until it lands.
- Pre-cut: db1.AC1 base FAIL as expected (HEAD 0, live 5; keys 54 of 54).

<status>pending</status>
<round>34</round>
<slot>~54</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
