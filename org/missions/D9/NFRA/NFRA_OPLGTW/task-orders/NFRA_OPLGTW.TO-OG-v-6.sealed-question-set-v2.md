# NFRA_OPLGTW task order -- `OG-v-6` -- ROUND 2 (E4): sealed question set v2 -- units, a real two-date alignment, declared grains

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-v-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~10</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-time seal; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; ssm PutParameter/GetParameter under /opal/nfra_oplgtw/ogv6/ and S3 GetObject/HeadObject by VersionId use the site Z operator credential, as row S50's /opal/nfra_oplgtw/ogv4/ writes did.
comp-adversary: DECLARED-NOT-APPLICABLE -- the failure it answers is graded (OGV3-J1 FAIL, ADJUDICATION_v2.Z.md) and the scope is ruled (analysis item E4; Q4 @5676f4a48a).
EGRESS CLASS, declared: Opal's own AWS plus the PyPI download for the venv below -- development egress permitted to this project's COO and its workers (Andrew-direct ~21:2xZ, record @7bfa5811c6).
</preflight>

## 1. THE CELL -- `OG-v-6` (decomposition addendum R2-E, item E4)

**The sealed question set, version 2.** Round 1's question set (`OG-v-3`, RQ1-RQ6) was graded FAIL at L9 on its judgment
criterion. You write a new set that exercises what that one did not, compute every expected answer from version-pinned
qualified silver objects with an instrument independent of the Gateway's query engine, and seal it: salted hashes in
the repository, the salt and the plaintext answers in SSM SecureString, never in a file the repository holds and never
on stdout. You ask nothing of the Gateway. This cell is the seal plus the OFFLINE grade only (ruling Q4): FWD-2's live
exercise is the COO's own run at the round's close through the E1 walkthrough identity, and `OG-v-7` grades the
walkthrough's answers against your seal. PRD `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v1.1; contract
`org/standards/NFRA_OPLGTW_CONTRACT.json` v1.3.

**Why round 1's set failed, verbatim from the L9 grade** (`org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/adjudications/ADJUDICATION_v2.Z.md`,
criterion `OGV3-J1`, verdict FAIL): *"Balance-field overlap IS exercised: RQ3 reports three dim_balance fields
separately and RQ4 refuses a cross-master total. Date alignment is exercised on one date only: every question pins
2026-09-15, and the two between-date questions (RQ5, RQ6) resolve to NONE_QUALIFIED refusals because no second
qualified date existed. Units are NOT exercised: no question distinguishes a unit (quantity against value, sign,
scale), and describe-level unit semantics are never asked. 1 of 3 named dimensions is fully exercised."*

**FWD-2, verbatim** (PRD :55-61): *"DONE WHEN: EXERCISED -- chosen questions and date comparisons are checked against
independently prepared examples. ACCEPT: Menachem gets understandable holdings and balance answers for the master and
date he selected, with SmartX and BlackDiamond clearly separate and without adding overlapping balances or different
days together. PROOF: Deliberately chosen examples with independently known answers, including a comparison between
masters and between dates."*

**PRD C3, verbatim** (PRD :161): *"Positions/balances are snapshots at one date. Grouping never removes master/date
identity and never sums snapshots across dates. Both-master questions use separate tool calls/results; date
comparisons use separately authorized snapshots and exact decimal deltas. Vendor balance fields overlap: permit a
named field's sum across approved accounts, never construct a cash/AUA total by adding different balance fields.
Quantity sums require grouping by CUSIP and long/short indicator; price is nonadditive. Duplicate/conflicting source
grains produce unavailable, not silent deduplication. Dataset description records grain, field type, unit, sign and
null semantics from measured source plus independent fixtures. Unsupported/unverified metrics are refused."*
And PRD :175: *"Tie-break rows deterministically using a validated unique source grain. If a dataset lacks that grain,
reject paging until the input is corrected."*

**What you build, in order:**

1. **Fix the two dates.** For each master (`08242234` SmartX, `08335338` BlackDiamond), read the closure markers
   `s3://opal-data-assets/schwab/<master>/meta/complete/date=*.json`, read-only. `D_NEW` is the newest date whose
   marker has `closure.status == "qualified"` in BOTH masters. `D_PREV` is the qualified date immediately before
   `D_NEW` in both masters. Record both dates, each marker's VersionId and its LastModified. Once sealed, both dates
   are FIXED: every question names them literally, and none is resolved again at ask time (ruling R-OG-12, row
   `NFRA_OPLGTW-W6-S5`). Context, not an acceptance value: at drafting, markers existed for both masters through
   `date=2026-09-25`.
2. **Declare the grains, measured** (row `NFRA_OPLGTW-W6-S2`). The Gateway enforces this declared grain, inlined here
   from `infra/aws/ec2/opal-gateway/app/integrations/schwab/query.py:136-140` @73e5968e67 in source column names:
   `dim_position` = (`account_id`, `cusip`, `l_s`); `dim_balance` = (`account_id`); `dim_asset` = (`cusip`). For each
   of the 3 datasets, 2 masters and 2 dates (12 snapshots), read the version-pinned silver object. Count the rows, the
   keys that collide under the declared grain, and the rows beyond each key's first occurrence. Write
   `GRAIN_DECLARATION.json` in your deliverables with, per snapshot: dataset, master, date, key, VersionId, the
   declared grain, rows, colliding keys, extra rows, and `HOLDS` or `COLLIDES`. Counts only; never a key value. For a
   snapshot that COLLIDES, also record the smallest superset of contract columns (`fields` in the contract) that is
   unique on that snapshot, or `NONE_FOUND`. Label it a CANDIDATE: adopting a different grain is a spec decision for
   `1.0.0_SA_CTO~O`, never this cell's.
3. **Write the questions**, RQ2-1 onward, into section 4 of
   `infra/aws/ec2/opal-gateway/tests/acceptance/WALKTHROUGH_PROTOCOL.md`. Replace the RQ1-RQ6 table and the
   paragraph above it, and keep the table's columns (`id | kind | masters | dates | dataset | question`). Each question
   names one master and one date per request. The set must contain at least:
   - **one `units` question**, whose correct answer distinguishes a QUANTITY field from a VALUE field for the same
     `(cusip, l_s)` group, states the SIGN each carries on a short (`l_s` short) group if one exists on that date, and
     asks the dataset's described unit or scale for both fields (the describe-level semantics C3 says the dataset
     description records);
   - **one `between_dates` question per master**, on `D_PREV` and `D_NEW`, answered as two separately authorized
     snapshots and an exact decimal delta of ONE named field (never a sum across the two dates);
   - **one `between_masters` question**, two separate snapshot answers and no combined total;
   - **one balance-overlap question**, several `dim_balance` fields reported separately and never added together
     (round 1's RQ3, which PASSED, may be carried at `D_NEW`).

   **A question whose rows touch a grain that COLLIDES on its date has the C3 refusal as its expected answer**
   (UNAVAILABLE `duplicate_source_grain` for a rows read of the full grain, or `paging_refused_no_unique_grain` for a
   paged read). Its expected answer is never a de-duplicated value.
   Also update A7's step 2 (protocol :107) so actual answers are written to `%LOCALAPPDATA%/opal/og-salt/actual_v2/<id>.txt`
   instead of `C:/tmp/...`, and change the expected observation at :111 to name this order's seal and `D_NEW` in place
   of `OG-v-3` and `2026-09-15`. Change no other row of the protocol.
4. **Seal.** Copy `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/compute_expected.py` to your
   deliverables as `compute_expected_v2.py` and extend it: same decode (pyarrow Parquet read only), same exact
   `decimal.Decimal` arithmetic, same `sha256(salt || canonical_json(answer))` digest, a fresh
   `secrets.token_hex(32)` salt, and new question functions. Set `SEALED_DIR` from `OG_SEALED_DIR`, else
   `%LOCALAPPDATA%/opal/og-salt/v2`, never `C:/tmp`. Row S42 records that a `C:/tmp` salt was lost. Run it ONCE. It
   writes `SEALED_EXPECTED_V2.json` in your deliverables, which holds the dates, the VersionIds used, the question ids
   and digests, and the pre-seal absence record (step 5).
5. **The pre-seal absence record**, the pattern of `d5af54a90a` (`SEALED_EXPECTED.json` `preseal_absence_check`).
   Immediately before running the sealer, run `git cat-file -e HEAD:<path>` on the G-C record
   `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/1.0.0_SA_CTO~A/G-C_CONTROLLED_IDENTITY_AND_GRANT.md` and the
   G-D record `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/CONTROLLED_WALKTHROUGH_RECORD.md`. Write
   the commit, both paths, each rc and each result into `SEALED_EXPECTED_V2.json`. The G-C record may already be
   present (the CTO writes it before E1); the G-D record MUST be absent. If the G-D path is PRESENT, the walkthrough may
   already have happened and a seal is worthless: file a BLOCKING row and stop without sealing.
6. **The copy of record in SSM**, the pattern of row `NFRA_OPLGTW-S50`. Write the salt and every plaintext answer as
   SecureString under `/opal/nfra_oplgtw/ogv6/seal_v2_YYYYMMDD/{<question id>..., SALT}` (YYYYMMDD = the UTC date of your
   sealing run). Read each one back with `--with-decryption` and compare its sha256 to the local bytes. Print only
   names, byte lengths and equality booleans, never a value. The local `%LOCALAPPDATA%` copies stay in place: `OG-v-7`
   reads them at grading, and `OG-v-7`'s drain removes them.

**The probe** for every mechanical criterion is
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~10/probes/og_v6.py`, which you write. It takes the
short id, prints its measurement with its denominator, and then prints exactly one line, `VERDICT: PASS-OGV6-AC<n>` or
`VERDICT: FAIL-OGV6-AC<n> <reason>`. It never prints a customer value, and each run finishes inside 110 s.

## 2. BOUNDS

- **Grant.** You may write the `<paths>` block below. Outside the repository you may write only
  `%LOCALAPPDATA%/opal/og-salt/v2/` and SSM parameters under `/opal/nfra_oplgtw/ogv6/`. If you need a path that is
  not named here, that is a BLOCKING surprise row on the criterion, never an override.
- **AWS: reads, plus one write surface.** You may run GetObject and HeadObject by VersionId on
  `opal-data-assets` `schwab/<master>/silver/dim_{position,balance,asset}/` and `schwab/<master>/meta/complete/`. You
  may run ssm PutParameter and GetParameter under `/opal/nfra_oplgtw/ogv6/` only. Nothing else in AWS: no S3 write, no
  delete, no other parameter. AWS via the `.tools/aws` shim.
- **Independence.** The sealing instrument never reads or imports `infra/aws/ec2/opal-gateway/app/integrations/schwab/`.
  The declared grain is inlined above for exactly that reason.
- **Customer data stays out of the repository and off stdout.** Never commit, print, or echo into a row or result
  file any value, account id, CUSIP or name. Only counts, hashes, VersionIds and dates.
- **No Gateway call.** You make no sign-in, no connector act and no call to Claude, an Anthropic endpoint or any vendor
  API.
- **Worktree.** You work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- **Interpreter.** Build `.venv-og` at your worktree root ONCE:
  `python -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt pytest`.
  This PyPI download is permitted development egress (Andrew-direct ~21:2xZ, record @7bfa5811c6). Site Z has no
  `py -3.12`; `python` is 3.11. Never commit `.venv-og/` or `.scratch/`.
- **Commits.** Commit with `.tools/safe-commit.sh` under your serial. Every `.py` you touch passes `.tools/commit-gate.sh`.
- **Spec frozen; REFUSE what you cannot meet as written.** If you cannot satisfy a criterion as written, refuse it and
  report it with its measurement. Never repair it, widen it, or satisfy it by a route this order does not name.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/tests/acceptance/WALKTHROUGH_PROTOCOL.md
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~10/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md`, id
`NFRA_OPLGTW-Z-W10-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="OGV6-AC1" cell_refs="OG-v-6"><invocation>timeout 110 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~10/probes/og_v6.py AC1</invocation><expect>(?m)^VERDICT: PASS-OGV6-AC1(?![0-9])</expect></criterion>
  <criterion id="OGV6-AC2" cell_refs="OG-v-6"><invocation>timeout 110 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~10/probes/og_v6.py AC2</invocation><expect>(?m)^VERDICT: PASS-OGV6-AC2(?![0-9])</expect></criterion>
  <criterion id="OGV6-AC3" cell_refs="OG-v-6"><invocation>timeout 110 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~10/probes/og_v6.py AC3</invocation><expect>(?m)^VERDICT: PASS-OGV6-AC3(?![0-9])</expect></criterion>
  <criterion id="OGV6-J1" cell_refs="OG-v-6" judgment="true"/>
</proof_of_spec>

- `OGV6-AC1`: `GRAIN_DECLARATION.json` covers 12 of 12 snapshots (3 datasets x 2 masters x 2 dates). For each, the
  probe re-reads the object by its VersionId, recomputes the rows, colliding keys and HOLDS/COLLIDES under the declared
  grain, and finds that they equal the file. The denominator 12 is printed.
- `OGV6-AC2`: the section 4 table of `WALKTHROUGH_PROTOCOL.md` has one row per question in `SEALED_EXPECTED_V2.json`,
  and both sets of ids are equal. The kinds present include `units` (at least 1), `between_dates` (at least 1 per
  master, on `D_PREV` and `D_NEW`, where neither date's answer is `NONE_QUALIFIED`) and `between_masters` (at least 1).
  Every question whose dataset COLLIDES on its date in `GRAIN_DECLARATION.json` is sealed with a C3 refusal. The count
  per kind is printed.
- `OGV6-AC3`: the seal is sound. `SEALED_EXPECTED_V2.json` carries a pre-seal absence record whose commit is an ancestor
  of the seal's own commit and whose G-D read is ABSENT. Every digest re-derives from the SSM copy of record (salt plus
  answer, read with decryption, compared in memory), N of N printed. A scan of every file this order commits, against
  the SSM-held answer values, finds 0 values.
- `OGV6-J1`: graded at L9 by `3.0.0_SA_CVO~O`, re-grading round 1's `OGV3-J1` on the new bytes. The questions exercise
  date alignment, units and balance-field overlap on real snapshots (boundary question 13). RECORD; NO VERDICT.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~10/NFRA_OPLGTW.TO-OG-v-6.sealed-question-set-v2.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>` BEFORE the `complete` flip. Record `OGV6-J1` as
`UNVERIFIABLE-BY-INSTRUMENT`, with a `status_reason` naming `3.0.0_SA_CVO~O` at L9. A PASS or FAIL on a judgment row is
INVALID. The result file is `sealed-question-set-v2.result.md`, beside the instance. Flip to `complete` only when every
MECHANICAL criterion PASSES by output. Report once, in your final message. You cannot send or receive messages;
anything you would ask becomes a surprise row.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Slot ~10, queue position 1 (then `OG-v-7` = E1, then `OG-v-8` = E2). E4 has no upstream cell. It must drain before
  the controlled walkthrough (G-D) happens, because its seal is only worth something while the walkthrough has not yet
  occurred.
- Q4 folded (@5676f4a48a): E4 is the seal plus the offline grade; FWD-2's live run is the COO's one real run at close
  (rule 22) through the E1 walkthrough identity, and not a worker criterion.
- The G-C record path is the CTO's pin (msg 26198): `deliverables/1.0.0_SA_CTO~A/G-C_CONTROLLED_IDENTITY_AND_GRANT.md`.
  The absence record binds on G-D; G-C may be present by design.
- The grain is a spec question. Rows that COLLIDE get the C3 refusal as their sealed answer. The code grain is not
  changed, and neither the contract nor the PRD is given a grain member here; a CONTRACTS addendum, if the CTO wants
  one, comes with a CVO re-sign.
- `<risk>` WORLD is GATE (xii)'s floor (an `infra/` path); the cell also writes SSM parameters.

<status>pending</status>
<round>3</round>
<slot>~10</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
