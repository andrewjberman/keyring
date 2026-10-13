# NFRA_OPLGTW task order -- `OG-ap-15` -- APPLY: the per-family DLQ drain releases (OG-fd-1 + OG-fd-2) for schwab, etf, orion, eclipse and blackdiamond, one family at a time (round-37 R2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-15</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-15</to_id>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN-BY-ISSUER at the cut -- the converters fire on bronze ObjectCreated and on their scheduled sweeps, read from infra/aws/terraform/opal-assets/silver.tf local.silver_sweep_slots (:279-285): schwab cron(15 12), blackdiamond cron(0 13), orion and eclipse cron(0 16), etf cron(30 23), all UTC; the schwab pulls land 09:45-10:45Z and 21:45-22:45Z. Apply a family only outside [09:15,11:35)Z, [12:00,13:35)Z, [15:45,16:35)Z and [21:15,23:59)Z. The live grade USES the next scheduled sweep; no ad-hoc sweep invoke. No cron, alarm or monitor is created. These are Lambda acts, not gateway releases, so they do not wait on the gateway queue.
comp-iam: RUN-BY-ISSUER -- the new code's AWS calls: sqs ReceiveMessage, DeleteMessage, ChangeMessageVisibility on opal-assets-silver-dlq (all three live for all 7 converter roles since OG-ap-12, policy opal-assets-silver-dlq-access v2), and s3 PutObject of {source}/{scope}/meta/backfill-status.json in opal-data-assets (the write each sweep already makes; OG-fd-2 adds a key, not a call). No role or policy changes.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z's round-36 analysis R2 (org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round36.md @713305ee56), rows Z-S91 and Z-S100, on the census and ask org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~61/NEVER_WIDEN_ASK_OG-fd-2.md @fa831797e4.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ap-15` (decomposition addendum R3-T.49, R2)

The per-family drain (OG-fd-1) and its after-the-fact record (OG-fd-2) are in source for every family. Live today:
- **schwab** runs the per-family drain without the record;
- **etf, orion, eclipse and blackdiamond** still drain the WHOLE shared queue `opal-assets-silver-dlq` at their 16:00Z sweep.
  On 2026-10-13 the blackdiamond sweep deleted an eclipse record (row Z-S91).
- **smartx and bd49finsurance** hold no DLQ read, so they are NOT in this order.

READ the census and ask first: `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~61/NEVER_WIDEN_ASK_OG-fd-2.md`
and `FD2_DRIFT.json` beside it.

What each family's rebuild ships:

| family | ships | drift lines |
|---|---|---|
| schwab | the drain record, plus the drain moving AHEAD of the lanes. This is a change of order, so the ask DISCLOSES it (CVO note, REMEDIATION_v19). | -- |
| etf | the drain + the record | 19 |
| orion | the drain + the record | 282 |
| eclipse | the drain + the record | 398 |
| blackdiamond | the drain + the record, plus held rebalancer work (`rebalancer_schemas.py`, `rebalancer_conversion.py`) and `opal_strategy_matcher.py`, which the live package never received | 298 |

### PHASE A (now) -- build off trunk, ask. NO deploy, NO trunk change

1. **Build branch.** Work in a worktree `C:/tmp/og-rel-fd2` on a new branch `rel-nfra-oplgtw-fd2`, at box/sitez HEAD. Do
   NOT commit a re-vendored package dir to box/sitez: an untargeted apply by any seat would ship it (row Z-W15-S25 class).
2. **Re-vendor** each of the five package dirs from source with `infra/aws/lambda/ci/vendor-manifest.sh` (it copies every
   `BUILD_MANIFEST.json` `vendored_modules` entry). One commit per family on the build branch, with the audited
   `GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL` on those commits only.
3. **Package and read the prior state** per family, without uploading:
   - the package's sha256;
   - the prior live `CodeSha256` from `get-function-configuration` (one resource each);
   - the prior S3 object version of `opal-assets/opal-assets-silver-<family>.zip`;
   - the drift lines, re-measured against the live package as FD2_DRIFT measured them.

   Write `W/ap15_build.json` = `{"build_branch", "families": [{"family", "build_commit", "package_sha256",
   "prior_code_sha256", "prior_s3_version", "drift_lines", "carries": "drain-only" | "drain+drift", "held_modules":
   [..]}]}`.
4. **The ask**, `W/NEVER_WIDEN_ASK_OG-ap-15.md`, for `1.0.0_SA_CTO~Z` and `2.0.0_SA_COO~O`, ONE section per family.
   Each section is signed or refused on its own, and names:
   - what ships, with the drift by file and its owner (FD2_DRIFT's two owners);
   - the blast radius (that converter's code; its trees);
   - the new `OPAL_BUILD_COMMIT` pin row it adds in `infra/aws/terraform/opal-assets/silver.tf` `local.silver_build_commit`,
     whose value is the build commit;
   - the rollback: the prior S3 object version and prior `CodeSha256`, with the pin row removed.

   The schwab section discloses the drain-ahead-of-lanes move. The blackdiamond section names the held modules, so a
   half can refuse it alone.

   Run AC1, commit, REPORT, STOP.

### PHASE B -- per family, only on the issuer's GO naming that family's two halves signed

5. One family at a time, in the GO's order. Ledger `nfra-oplgtw-fd2-<family>-drain`: entry AND sentinel first.
   - Merge that family's build commit into box/sitez by `.tools/safe-merge.sh`, carrying the package dir and the one
     `silver_build_commit` row.
   - Apply with `bash .tools/safe-apply.sh -target='module.silver_converter["<family>"]'`. The plan reads that one
     function changed: code fields plus the one `OPAL_BUILD_COMMIT` environment value. Any other row is a STOP.
   - Never use `aws lambda update-function-code`.
   - Read back `CodeSha256` = the package, State Active, LastUpdateStatus Successful.
6. **Live grade** at that family's NEXT SCHEDULED sweep. Read the sweep's `meta/backfill-status.json` (writer:
   `data/assets/scripts/lib/backfill_status.py`, `status_key`): its silver section carries the `dlq_drain` key with
   `family` = that family. Then update `infra/aws/lambda/ci/lambda-source-map.json`'s entry for the family and close the
   ledger.
7. A family a half REFUSES is not deployed. Record `released: false` and the refusal file's `path@hash`.
8. Write `W/AP15_GRADE.json` = `{"families": [{"family", "released", "live_code_sha256", "sweep_request_id",
   "sweep_was_scheduled", "dlq_drain_present", "refusal_ref"}]}`. Run AC2, commit, report once to `2.0.0_SA_COO~O`.
   Rollback, if a read-back disagrees: restore the prior object version and pin by the same path, then file an ARMED
   row naming `2.0.0_SA_COO~O`.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/`.

## 2. BOUNDS

- The five families' converters only. No IAM, queue or schedule change. No message deleted or planted by you.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; bare `terraform`; an ad-hoc sweep invoke; override a gate
  other than the audited lane escape in step 2.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/terraform/opal-assets/silver.tf
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/lambda/opal-assets/opal-assets-silver-schwab/
infra/aws/lambda/opal-assets/opal-assets-silver-etf/
infra/aws/lambda/opal-assets/opal-assets-silver-orion/
infra/aws/lambda/opal-assets/opal-assets-silver-eclipse/
infra/aws/lambda/opal-assets/opal-assets-silver-blackdiamond/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-fd2-schwab-drain.json
org/critical_paths/.open_deploys/nfra-oplgtw-fd2-etf-drain.json
org/critical_paths/.open_deploys/nfra-oplgtw-fd2-orion-drain.json
org/critical_paths/.open_deploys/nfra-oplgtw-fd2-eclipse-drain.json
org/critical_paths/.open_deploys/nfra-oplgtw-fd2-blackdiamond-drain.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from the repo root; AC1 after Phase A, AC2 after the last family is terminal)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-15"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ap15.AC1.sh; echo "exit=$?"</invocation><expect>(?s)families named 5; expected set equal: yes.*families built from source with fields: 5 of 5; ask names all five: yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-15"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ap15.AC2.sh; echo "exit=$?"</invocation><expect>(?s)families released and graded [1-5]; refused with a file [0-4]; of 5; defects 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: each package is the source, built off trunk, with each family's ask. `AC2`: every family is released and
  graded on its real scheduled sweep, or refused with a file.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-15.per-family-drain-releases.proof_of_spec.json`. Validate it after your
last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, and flip the ONE
`<status>` tag to `complete` only if both PASS. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, R2 (`ledger/ROUND_ANALYSIS.round36.md` @713305ee56). The CTO's ruling: per-family releases, NOT in R1, and
  the pair discloses schwab's drain move.
- Issuer ruling at the cut: each family is signed alone, so blackdiamond's held modules cannot ride in on the others'
  signatures. Z-S91 closes for each family as it ships and stays open for any family that is refused.
- Pre-cut dry runs:
  - ap15.AC1 base FAIL as expected (record absent). Discrimination arm: all five pointed at schwab's live pin
    a11240c01c read 0 of 5 byte-equal (schwab 10 of 11, etf 5 of 8, orion 3 of 6, eclipse 3 of 6, blackdiamond 4 of 9),
    so the check sees an un-re-vendored package.
  - ap15.AC2 base FAIL as expected (record absent).

<status>pending</status>
<round>37</round>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
