# NFRA_OPLGTW task order -- `OG-ap-10` -- APPLY: the gateway release of the `.pptx` -> market_update pair (OG-ab-2 + OG-mu-1), re-cut on the live ref (round-35 E2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-10</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-10</to_id>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN-BY-ISSUER at the cut -- live gateway ref 28ba9532b6 (OG-ap-7 CLOSED); no other gateway release in flight; B2 window 11:00Z-23:00Z. No cron, alarm or monitor is created.
comp-iam: DECLARED-NOT-APPLICABLE -- the grant this release needs is ALREADY live (gateway-market-update-put-policy, OG-ap-8 @a62894577a); this order changes no role or policy.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z's round-34 analysis @026a983b34 cell E2 and the OG-mu-1 pair's condition C (COO @34bf3d67a4, CTO @e0ca80f880): the .pptx code ships only after the grant, in a release cut on the live ref.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ap-10` (decomposition addendum R3-T.44)

Ship the gateway's `.pptx` -> bronze market_update pair. It was built in OG-ab-2 (`5c2f6e9324`) and given intake's
content-addressed key in OG-mu-1 (`6085ce3193`, test re-pin `57aa2a3527`). Its grant is live. Trunk's copies of
`tools.py`, `destructive_ops.py` and `deploy-to-ec2.sh` carry OTHER unreleased work, so take only these hunks. Never take
a whole file from trunk except the three named in step 2.

### PHASE B1 (now): re-cut, prove, ask. NO deploy

1. **Live ref.** One SSM md5 read of the host against `28ba9532b648061cecafe426836d3e96af4529cd`, walking `app/`, `deploy/`
   and `dashboard/`. The superset extras are named; any mismatch is a STOP.
2. **Re-cut** in a worktree `C:/tmp/og-rel-pptx` on a new branch `rel-nfra-oplgtw-pptx`, at `28ba9532b6`:
   - `site_to_s3.py`, `tests/test_og_ab2_pairs.py` and `tests/test_og_mu1.py` take box/sitez HEAD's bytes. Since the live
     ref, only ab-2 and mu-1 touched them.
   - `app/tools.py` and `app/destructive_ops.py` take ab-2's own hunk (`git diff 5c2f6e9324~1 5c2f6e9324 -- <file>`).
   - `deploy-to-ec2.sh` takes ab-2's hunk 3-way. The `.env` printf conflicts, so resolve it as rl-16 did: the LIVE
     printf with ONE key `ADVI_MARKET_UPDATE_S3_ROOT=%s\n` and ONE argument added, nothing dropped.

   Commit it with the audited `GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL` on the release commit only. Write
   `W/ap10_release.json` = `{"base_sha", "release_sha"}`. Run the release tree's `tests/test_advi_site_to_s3.py`,
   `tests/test_og_ab2_pairs.py` and `tests/test_og_mu1.py`. Then run AC1.
3. **The ask**, `W/NEVER_WIDEN_ASK_OG-ap-10.md`, for `1.0.0_SA_CTO~Z` and `2.0.0_SA_COO~O`. It carries:
   - the diff by file;
   - the ONE new `.env` key;
   - **the key form** (CTO ruling on row Z-W55-S2): `date=<UTC put date>/deck_<sha16>.pptx`, the original name in
     Metadata. A reader finds a quarter's decks by listing the `date=` partitions in the quarter. The `quarter` argument
     for `.pptx` is validated but does not name the key;
   - both branches of a call;
   - triggers relative to the live base (tools unchanged by name; `.env` names +1, exactly the new key; md5 = release);
   - rollback: redeploy `28ba9532b6`.

   Commit, REPORT, STOP.

### PHASE B2 (only on the issuer's GO, which names both halves signed at `release_sha`)

4. Ledger `nfra-oplgtw-gateway-release-pptx`: entry AND sentinel first. Deploy from `C:/tmp/og-rel-pptx` through
   `infra/aws/ec2/safe-ec2-deploy.sh`, with `DEPLOY_BASE_REF=28ba9532b648061cecafe426836d3e96af4529cd`.
   **The release cone carries** `lib/`, `.tools/`, `org/modules/graph/`, `data/transcripts/scripts/teams/` AND your agent
   home `org/tier2_senior/0.7.0_AE_CloudOps~Z/` (the worktree's halt gate scans it; OG-ap-7's first deploy was blocked
   without it). No `HALT_OVERRIDE`.
5. **Read back immediately** against the triggers. Any trigger: redeploy the base and file an ARMED row naming
   `2.0.0_SA_COO~O`.
6. **The served read**: one SSM read through the INSTALLED code, writing `W/AP10_SERVED.json` = `{"body": {...}}` with:
   - `tool_takes_extension`;
   - `market_update_root_equals_address` (compare the value on the host, print only the boolean);
   - `bad_extension_refused` (one call with extension `.docx`, refused before any read);
   - `objects_written: 0`;
   - `fee_root_unchanged`.

   No real `.pptx` put: the first real deck is ADVI_BILLING's (dell2) use.
7. **Standing release clauses:** runbook 7.2 names the new live release; EC2_MANIFEST `deployed_commit` and
   `file_checksums` come from the release blobs. Close the ledger, commit, run AC2, and report once to
   `2.0.0_SA_COO~O`.

## 2. BOUNDS

- The `.pptx` pair's hunks only. No grant, policy or Terraform act (the grant is live). No real object written.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; merge box/sitez into the release branch; bare `terraform`;
  print an `.env` value; override a gate other than the one audited lane escape in step 2.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-pptx.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/`. Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free),
fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from the repo root; AC1 after B1, AC2 after B2's ledger is closed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-10"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r35/checks/ap10.AC1.sh; echo "exit=$?"</invocation><expect>(?s)is the live ref 28ba9532b6: yes.*outside the \.pptx pair's files 0 \(want 0\).*byte-equal to HEAD: 3 of 3; ab-2 hunk patch-id equal: 3 of 3; printf differs only by the market_update key and argument: yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-10"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r35/checks/ap10.AC2.sh; echo "exit=$?"</invocation><expect>(?s)entries at HEAD [1-9]\d*; status CLOSED=yes; sentinel at HEAD=no.*equal=yes; rb\.AC2 PASS; served \.pptx pair fields: yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the re-cut carries exactly the `.pptx` pair's hunks on the live ref. `AC2`: landed, closed, recorded, served.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-10.pptx-pair-release.proof_of_spec.json`. Validate it after your last
commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, and flip the ONE
`<status>` tag to `complete` only if both PASS. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 35, E2. Measured at the cut: the hunks do not apply flat onto 28ba9532b6, because ab-2's deploy-to-ec2.sh printf
  conflicts and the later two commits cascade. That is the rl-16 class, resolved 3-way as written in step 2. Since the
  live ref, the files were touched as follows:
  - site_to_s3.py by 6085ce3193, 5c2f6e9324 (and E2's 931774fb11, already live by content);
  - tools.py by 5c2f6e9324 plus 3 other unreleased commits;
  - destructive_ops.py by 5c2f6e9324 plus 2 others;
  - deploy-to-ec2.sh by 11 commits.
- A1 (issuer, 2026-10-12 ~01:0xZ): **B2 GO, effective at or after 11:00Z 2026-10-12** (the window). The GO names:
  - **both halves, signed at release `d9f2ebded9`:** COO @a9472f2a8d and CTO @3bcecf1c76. Their conditions bind: the
    served read writes nothing; runbook 7.2 moves to the new live ref; file_checksums come from the release blobs; the
    cone carries the agent home.
  - **Sequencing:** OG-ap-11's Lambda deploy (a different resource) may run before this; its 12:15Z-sweep grade overlaps
    nothing on the gateway host. Before step 4, confirm one GATEWAY release in flight across all worktrees, with the
    per-tree denominator printed.
  - Gate limb: GATE (viii) on the modified order (placeholders NONE).
- Pre-cut: ap10.AC1 and ap10.AC2 base FAIL as expected (records absent).

<status>pending</status>
<round>35</round>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
