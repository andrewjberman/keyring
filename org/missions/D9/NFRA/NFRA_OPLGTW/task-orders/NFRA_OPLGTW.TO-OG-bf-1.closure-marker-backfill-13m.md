# NFRA_OPLGTW task order -- `OG-bf-1` -- backfill the producer's completion records over 13 months, both masters (PRD v2.0 item 4 / C3, FWD-12)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-bf-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-bf-1</to_id>
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

### AMENDMENT A1 (issuer, 2026-10-09 ~00:4xZ) -- what is signed, and the 08335338 leg

**Phase B is SIGNED for master 08242234 ONLY** (option W). COO half
`deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_HALF_COO_OG-bf-1_20261009.md` @35ca8013bb; CTO half
`deliverables/1.0.0_SA_CTO~O/NEVER_WIDEN_HALF_CTO_OG-bf-1_20261009.md` @f9b1f1fd31 (read both with `git show <commit>:<path>`;
they are not on your branch). The write set is the ask's section 2 for 08242234: 256 records + 256 manifests, nothing else.
Run order, per the CTO half: newest date first; one invocation in flight; outside 09:30-10:30Z, 12:40-13:00Z and
21:30-22:30Z and away from the 12:15Z sweep; STOP on the first record that is not QUALIFIED and on any Lambda error,
throttle or timeout. In `backfill_record.json`, list 08335338's dates under `unavailable` with the reason
`held: 49F accelerator; Y leg pending (A1)` until Phase D writes them; never under `backfilled`.

**PHASE C -- the Y leg build (ruled by the CTO half section 2; NO deploy by you).** In
`infra/aws/lambda/opal-assets/advi-49f-gold-dispatch/lambda_function.py`, inside the existing accelerator branch, AFTER
the qualified check and BEFORE any EC2 or SSM call: parse the record's date from its key (`date=YYYY-MM-DD`; the key may
arrive URL-encoded, `date%3D`); compare it with the T-1 trading date that `chain_49f_entrypoint.py --production` would
take at invocation, computed by the estate's one frontier `lib/trading_calendar.py` PACKAGED INTO THE ZIP (a byte copy
placed beside `lambda_function.py`, with a test that it equals `lib/trading_calendar.py`; never a re-derivation). If they
differ, return `dispatched: false` with `skip_reason: "accelerator marker date=<D> is not the production T-1 <T>;
historical record, not dispatched"`. If the calendar cannot be read, SKIP. The floor (scheduled) path and its source are
unchanged; a non-qualified record still SKIPs on the qualified check first.
- Tests: `infra/aws/lambda/opal-assets/tests/test_advi_49f_gold_dispatch_dategate.py`, named exactly
  `test_ogbf1y_ac01` .. `test_ogbf1y_ac04` as the header of
  `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/bf1.AC4.sh` lists them, in the style of
  `tests/test_advi_49f_gold_dispatch_remedy.py`. That existing file must still pass whole: if a test there fails only
  because its marker date (2026-09-25) is not today's T-1, pin the production T-1 in a fixture or setUp (patch the
  packaged calendar's "today"), never change an assertion, and name each such test in your report.
- Write `W/NEVER_WIDEN_ASK_OG-bf-1-Y.md` (the form of the first ask): the one Lambda's code change, `CodeSha256` before
  (`TjIWGFWkbUswLkA+mUac9NS+LRZ1q7o6lR1iQLb0kI4=`) and the built zip's after, the rollback (the previous zip), the deploy
  path (Terraform `module.advi_49f_gold_dispatch` by `0.7.0_AE_CloudOps~Z` under a NEVER-2 ledger), and the proof both
  arms on the deployed function (a synthetic historical qualified record SKIPs with no EC2/SSM call in its log; the next
  daily T-1 record dispatches as today). Commit, report, STOP.

**PHASE D -- 08335338 (only after the Y leg's ledger is closed, its read-back committed, and a fresh pair of halves on
the 08335338 write set is at HEAD; the issuer's continuation names all three).** The ask's section 2 write set for
08335338 under the same run rules. The CTO half allows a first set limited to dates on or after 2026-04-08 (the earliest
Tax roster inception); the issuer's continuation says which.

## 2. BOUNDS

- Phase B writes completion records ONLY: no bronze or silver object is written, copied, deleted or rewritten (AC2).
- No write before both halves are at HEAD. No grant is changed here (the 13-month grants are set at the release).
- Only `schwab/08242234/` and `schwab/08335338/` (and `08403355/` only if the signed ask extends to it). No other firm.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/lambda/opal-assets/advi-49f-gold-dispatch/
infra/aws/lambda/opal-assets/tests/test_advi_49f_gold_dispatch_dategate.py
infra/aws/lambda/opal-assets/tests/test_advi_49f_gold_dispatch_remedy.py
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
  <criterion id="AC4" cell_refs="OG-bf-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/bf1.AC4.sh; echo "exit=$?"</invocation><expect>(?s)dategate: pytest rc=0; named tests passed 4 of 4.*remedy: pytest rc=0 .*removed or renamed 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: every silver date in each master's 13-month window is now QUALIFIED or named unavailable with a reason.
- `AC2` (difference control): every served object a backfilled record names predates the backfill (silver untouched).
- `AC3` (judgment, graded by `3.0.0_SA_CVO~Z` at L9): what the backfill caused downstream (the 49F accelerator and
  any other consumer) matches the signed ask's statement, read from the consumers' own logs. Record it in the
  instance under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO; never PASS or FAIL it yourself.
- `AC4` (A1; a fourth mechanical criterion because the Y leg is a code build this order now carries): the dispatcher's
  date gate, both arms and the unreadable-calendar arm, and the OG-m-2a suite unchanged.

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
- A1 (2026-10-09): Phase B signed for 08242234 only (W; halves @35ca8013bb, @f9b1f1fd31); Phase C carries the Y leg the
  CTO half ruled (NFRA_OPLGTW owns it; placed here, not round 33, so 08335338's 13 months is not held behind the round
  close); Phase D writes 08335338 after Y's ledger closes and fresh halves land. AC4 added (bf1.AC4 base: FAIL as
  expected, test file absent; remedy arm PASS 6 of 6). Graded by no gate limb as a modification (placeholders NONE).
- Pre-cut: see the issuance commit.
- A2 (issuer, 2026-10-09 ~07:5xZ): `bf1.sh` AC2's bound raised 115s -> 330s. With both masters backfilled the check
  HEADs 2048 objects (~151s unbounded); the old bound returned rc 124 with no output (row Z-W41-S4). The check's
  predicate and expect are unchanged. Graded by no gate limb as a modification (placeholders NONE).

<status>pending</status>
<round>32</round>
<slot>~41</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
