# NFRA_OPLGTW task order -- `OG-bf-1` -- backfill the producer's completion records over 13 months, both masters (PRD v2.0 item 4 / C3, FWD-12)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-bf-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~41</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN-BY-ISSUER at the cut -- an ObjectCreated consumer is armed on schwab/08335338/meta/complete/ (the 49F accelerator, infra/aws/terraform/opal-assets/silver.tf:757-763, starting the 49F gold dispatcher); the 49F floor schedule cron(45 12 * * ? *) is the production trigger. No cron, alarm or monitor is created.
comp-iam: RUN -- `comp-iam service opal-assets-silver-schwab` names role opal-assets-silver-schwab-role and detects no AWS operations in lambda_function.py (a FLOOR: the replay's writes run through conversion_manifest.py / schwab_runtime.py helpers it does not trace). Phase B writes completion records under s3://opal-data-assets/schwab/{08242234,08335338}/meta/complete/ only, through the producer's own replay path as OG-c-2 did; the exact identity and its grant are read live and named in the never-widen ask before any write.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is Andrew-direct ~21:2xZ "asap" (record @6233bae5de), PRD v2.0 item 4 and C3 (@e43ee663be, signed @5924aaedbe), round-31 analysis section 4a item 8 (@8ca3947b86).
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-bf-1` (decomposition addendum R3-T.30, round 32 item 8b)

Your previous order, `OG-cc-1`, measured per master every silver date in the 13-month window with no QUALIFIED
completion record. The gateway serves a date only when its record qualifies (PRD C3). C3, verbatim: *"Legacy markers
are nonqualifying until a controlled producer replay or metadata backfill reconciles against original inputs and exact
current output versions. ... Do not repair source data or rewrite silver values as part of this extension."* Section
4a item 8: backfill the producer's completion metadata for every date in the 13 months that has a silver partition,
both existing masters; *"A date with no proven-complete source stays unavailable, never guessed."*

**The precedent.** Cell `OG-c-2` (round 1) ran a controlled producer replay that wrote one qualified record per master
for one date. Read, in this order: its order
`org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-c-2.producer-deploy-replay.md` (its gate G-B, its write
set, its difference control), its result
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~4/producer-deploy-replay.result.md`, and its tools
`.../0.9.0_WK_NFRA_OPLGTW~4/replay/dry_run.py` and `replay/preconditions.md`. The producer is
`infra/aws/lambda/opal-assets/opal-assets-silver-schwab/` (`conversion_manifest.py`, `schwab_runtime.py`).

**The hazard you must plan around.** A completion record written under `schwab/08335338/meta/complete/` fires the
49F accelerator (`silver.tf:757-763`), which starts the 49F gold dispatcher. Hundreds of historical records could start
hundreds of gold runs for past dates, which is a SERVED-OUTPUT move. Read the dispatcher's handling of the record's
date before you plan; the ask must state, per branch, what one historical record causes downstream.

### PHASE A -- plan; NO write

1. From `deliverables/0.9.0_WK_NFRA_OPLGTW~41/closure_census_record.json`, list per master the missing dates.
2. For each, decide whether a proven-complete source exists (the producer's own reconciliation against the original
   bronze inputs and the exact current silver VersionIds, as OG-c-2's replay did). A date that cannot be proven goes to
   `unavailable` with its reason; it is never written.
3. Run the replay's DRY RUN for every candidate date (write nothing) and record the would-be records' verdicts with
   `catalog.validate_closure` (as `OG-cc-1` did).
4. Write `W/NEVER_WIDEN_ASK_OG-bf-1.md` in the form of
   `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-gw-2_20261003.md`: the exact write
   set (keys, count per master), the count and names of every writer of `meta/complete/` (N writers = N rules read),
   every `ObjectCreated` consumer of those keys and what ONE historical record causes in each (both branches: the
   dispatcher acts on it, or it does not), the order and rate of writes, the rollback per key (a completion record is
   versioned: the previous version or its absence), and the 08403355 extension once `OG-tm-1` lands. Halves owed:
   `1.0.0_SA_CTO~O` and `2.0.0_SA_COO~O`.
   If the replay needs any deploy or Terraform apply (a code or configuration change to the producer), name it in the
   ask as a separate leg: site Z's deploys are applied by `0.7.0_AE_CloudOps~Z` (Andrew-direct ~22:0xZ, msg 32057),
   never by you.
5. Commit Phase A and REPORT. Then STOP: the issuer continues you with the signed halves' paths, or with a ruling.

### PHASE B -- only after both halves are signed at HEAD (the issuer's continuation names their commit)

6. Open the NEVER-2 ledger first (`python .tools/deploy_ledger.py open --slug nfra-oplgtw-og-bf-1-marker-backfill ...`)
   and COMMIT the entry and its sentinel `org/critical_paths/.open_deploys/nfra-oplgtw-og-bf-1-marker-backfill.json`.
7. Write `W/backfill_record.json` with `started_utc` BEFORE the first write, then run the replay over the signed write
   set exactly, in the signed order and rate. Record per master `backfilled` (dates written) and `unavailable`
   (`{date: reason}`).
8. Close the ledger and commit BEFORE the criteria. Never leave it half-landed: finish, or roll back per the ask and
   file an ARMED row naming `2.0.0_SA_COO~O`.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~41/`.

## 2. BOUNDS

- Phase B writes completion records ONLY: no bronze or silver object is written, copied, deleted or rewritten (AC2).
- No write before both halves are at HEAD. No grant is changed here (the 13-month grants are set at the release).
- Only `schwab/08242234/` and `schwab/08335338/` (and `08403355/` only if the signed ask extends to it). No other firm.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-og-bf-1-marker-backfill.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~41/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W41-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ` at filing.

## 4. PROOF OF SPEC (literal; run from your worktree root after Phase B's ledger is closed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-bf-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/bf1.sh AC1; echo "exit=$?"</invocation><expect>(?s)08242234: window .*open 0; backfilled-but-not-qualified 0.*08335338: window .*open 0; backfilled-but-not-qualified 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-bf-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/bf1.sh AC2; echo "exit=$?"</invocation><expect>(?s)backfilled dates [1-9]\d*; served objects checked [1-9]\d*.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-bf-1" judgment="true"/>
</proof_of_spec>

- `AC1`: every silver date in each master's 13-month window is now QUALIFIED or named unavailable with a reason.
- `AC2` (difference control): every served object a backfilled record names predates the backfill (silver untouched).
- `AC3` (judgment, graded by `3.0.0_SA_CVO~Z` at L9): what the backfill caused downstream (the 49F accelerator and
  any other consumer) matches the signed ask's statement, read from the consumers' own logs. Record it in the
  instance under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO; never PASS or FAIL it yourself.

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `W/NFRA_OPLGTW.TO-OG-bf-1.closure-marker-backfill-13m.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If AC1 and AC2 PASS, edit the ONE `<status>` tag of this order IN PLACE to `complete`.
4. Report once: literal AC outputs; per master backfilled and unavailable counts; the downstream reads for AC3; the
   ledger's close; commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 32 (R3-T.30), section 4a item 8b; queued after `OG-cc-1` in slot ~41, handed by continuation. Item 8a (the
  gateway's `calendar_months` grant mode) is `OG-cm-1`.
- The judgment criterion exists because the downstream effect of historical records on the 49F chain is a served-output
  question no single instrument here can settle.
- Pre-cut: see the issuance commit.

<status>pending</status>
<round>32</round>
<slot>~41</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
