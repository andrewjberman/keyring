# NFRA_OPLGTW task order -- `OG-sa-1` -- APPLY: the site Z harvest cycle runner captures Seeking Alpha again (PRD v3.8, CTO msg 34216)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-sa-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-sa-1</to_id>
<issued_to>0.7.0_AE_CloudOps~ZW</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN-BY-APPLIER at the act (`comp-schedule --drift`): no hold or moratorium may name the scheduled task "Opal Data Harvest - Continuous Cycle" or its installer; none is known at the cut. AMGT_HARVST is PARKED (dell1's allocation); this cell is the harvest-producer defect v3.5 and v3.8 carry here.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change. The runner writes to the buckets it already writes; `sa` adds a publisher, not a bucket or a prefix.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z's decision (msg 34216, PRD v3.8 @3bb7fb022e) on the relay of the laptop CTO's ruling (msg 34214). Andrew's standing word is to keep Seeking Alpha ("also seeking alpha will renew, we're keeping that", `ANDREW_DIRECT_20260929_204xZ_OPEN_CALLS_ALL_FINE_SEEKING_ALPHA_RENEWS.md`).
EGRESS CLASS, declared: the Seeking Alpha account read (step 1) and, when access holds, the runner's capture under the use already worded for the harvester. No new vendor use.
</preflight>

## 1. THE CELL -- `OG-sa-1` (decomposition addendum R3-T.55, workstream G1-FIX, FWD-22)

Live today (CTO read ~20:3xZ, issuer read 20:4xZ): the task "Opal Data Harvest - Continuous Cycle" is Running with `--publishers bbg wsj barrons --refresh-once`; `sa` is absent from its registration
(`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round85/bz10_task.xml` line 77). The four Seeking Alpha bronze tables the pages read
(`opal-data-harvest/seeking-alpha/harvest/bronze/{symbol,report,analysis,news}/security_key=<key>/`) were last written 2026-09-22. The 2026-10-13T23:53Z stop was `HVST-bz-10`'s own stop and re-registration
(`fcfb0cec38`, `887a47f05e`), not Andrew's word, and `sa` was already absent before it.

1. **Read Seeking Alpha access first**, before anything is changed. Row AMGT_HARVST-Z-W37-S4 recorded HTTP 402 ("renewal pending, at the account holder"). Read the access the way the harvester's own SA capture does it
   (the same account and entry point; read-only, one request, no capture), name the source, and write `W/SA1_ACCESS.json` =
   `{"read_at": "<iso>", "source": "<what you read>", "http_status": N|null, "runner_profile_login": true|false, "reason": "<one sentence>", "outcome": "ACCESS_HOLDS"|"ACCESS_REFUSED"}`.
   ACCESS_HOLDS needs BOTH a 2xx from the account read AND `runner_profile_login` true (the runner's own SA profile carries a login, so the capture can authenticate). Anything else is ACCESS_REFUSED, with `reason` saying which half failed
   (`http_status` is null when no request was made). A1 (issuer): the one request step 1 allows is made through the main tree's SA profile (the profile the account is signed in under); it reads the ACCOUNT state only and nothing
   is copied from that profile into the runner's. The runner's profile carrying no login is a person act (a sign-in), not yours.
2. **If ACCESS_REFUSED: STOP.** Change nothing on the runner. Write `W/SA1_PROOF.json` = `{"branch": "refused", "runner_changed": false}`, file an OBSERVATION row naming the status, and report once: the renewal is Andrew's act and
   no capture runs against a refusing account. No ledger is opened on this branch.
3. **If ACCESS_HOLDS:** open ledger `nfra-oplgtw-harvest-runner-sa`, entry AND sentinel first. Read `install-cycle-schedule.ps1 -Plan` with `-Publishers bbg,wsj,barrons,sa -Windowless -RefreshOnce` and the current state dir and runtime root
   (unchanged: the live task's `--state-dir` and `--runtime-root` arguments). Stop the runner by its own STOP file at a cycle boundary (zero pairs lost, as bz-10 proved), then re-register through
   `install-cycle-schedule.ps1 -Publishers bbg,wsj,barrons,sa -Windowless -RefreshOnce`. Wait for the task to be Running. Rollback: re-register with `-Publishers bbg,wsj,barrons`.
4. **Place the trading-day trigger for the four SA tables** (CRO findings
   `org/tier1_exec/4.0.0_SA_CRO/deliverables/SECURITY_ANALYSIS_DAILY_PULLS_DEMQUE_DOSSIER_FINDINGS_20261014.md` G6, line 666). First READ what already moves them: the runner's cycle is the capture; then what converts the four bronze tables
   to the silver `seeking-alpha/harvest/silver/` tables. If the cycle and the existing silver trigger already run on trading days once `sa` is registered, record that in one sentence in `W/SA1_PROOF.json` (`trigger`). If a trigger must be NEW
   (a schedule, a Terraform file, a name): STOP that step, file a BLOCKING row naming exactly what is missing and the name the registry would need (names come from `lib/opal_naming.py`, never typed by hand), and keep step 3 as done. The issuer rules it.
5. **Prove it.** After one cycle, at least one object newer than your re-registration exists under the four bronze tables for the sampled securities BA, BABA and COST (`...bronze/<table>/security_key=<key>_US_Equity/`); write `W/SA1_PROOF.json` =
   `{"branch": "restored", "restored_at": "<iso of the re-registration>", "runner_changed": true, "trigger": "<one sentence>"}`. If no object lands inside two hours of the cycle's end, STOP and file an ARMED row naming this seat; do not re-register again.
6. Close the ledger (if opened), commit, run the criteria, report once.

## 2. BOUNDS

- ONE change of yours: the runner's registered publisher list (adding `sa`). The state dir, runtime root, STOP-file path, cycle cadence and every other task stay as they are. No object is written to or deleted from any bucket by you.
- On ACCESS_REFUSED you change nothing. You never put a credential, token or cookie into a file, row or message.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; a capture against a refusing account; a second vendor read beyond step 1's one request.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-harvest-runner-sa.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~ZW/`. Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from the repo root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-sa-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/sa1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)access read: status (?:\d+|none), outcome ACCESS_(HOLDS|REFUSED), source named yes, read_at in the order window yes, outcome consistent with status yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-sa-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/sa1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)branch (refused: runner Running, publishers .*sa registered False|restored: runner Running, publishers .*sa registered True, --refresh-once True).*sentinel at HEAD 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the access was read and named before any change. `AC2`: the runner's LIVE registration matches the branch AC1 chose; on the restored branch the check reads the four SA bronze tables for the three sampled securities and finds an object newer than the re-registration.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-sa-1.harvest-runner-seeking-alpha.proof_of_spec.json`. Validate it after your last commit with
`python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once to `2.0.0_SA_COO~O`.
A refused-access outcome is a complete order with branch "refused": say so in the first line of the report.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G1-FIX2 (addendum R3-T.55). PRD v3.8 ADMITTED at the cut (CTO msg 34215). A defect cell on a producer that keeps a FWD-22 table (`seeking-alpha/harvest/silver/*`) from landing; not a gateway release, so no never-widen halves.
- Seat: `0.7.0_AE_CloudOps~ZW` (ran HVST-bz-10; live, idle at the cut). The GO is the issuer's message citing this order.
- Pre-cut: sa1.AC1 and sa1.AC2 base FAIL as expected (the two records are absent). The AC2 parsing was dry-run on a simulated refused record against the live task (Running; publishers bbg wsj barrons).


- A1 (issuer, 2026-10-14 ~21:5xZ, rows Z-S127/Z-S128, msg 34228): at pin 3d88eccbc3 `sa` is a browser-tab publisher whose account id is the profile's `user_id` cookie, and the runner's own SA profile holds no login: step 1 as written returned NotAuthorized with 0 requests.
  Ruled: the one allowed request goes through the main tree's SA profile and reads the account state; the outcome needs the runner profile's login as well (a sign-in is Andrew's act, routed by the issuer to the CTO). `SA1_ACCESS.json` gains `runner_profile_login`
  and `reason`; `http_status` may be null. sa1.AC1 reads the new consistency rule. Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>complete</status>
<round>37</round>
<workstream>G1-FIX2</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
