# TO ADVI_COTBKF.TO-CB-cf-1.reasons-for-the-none-rows -- round 84 CB-cf-1: a stated reason for each of the 273 current Black Diamond accounts the reverse match leaves `none` with no reason, from a closed list written before the read; every other row unchanged

<to_id>ADVI_COTBKF.TO-CB-cf-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~167</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>84</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-cf-1` (`decompositions/ADVI_COTBKF_DECOMP.round84.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a READ of S3 tables and of two committed files. You change no code and no committed file. Nothing is built, served, corrected or fetched from a vendor. You write ONE new CSV OUTSIDE the repository (it carries account keys) and a record inside your own deliverables folder (no account key in it).**

**Read first:** the CVO's grade of the clause this cell repairs, `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_82_L9_GRADE_20261013.md` section "CB82cd1-AC3 -- FAIL on one clause": "NOT met: 'says why an account is `none`'. In `REVERSE_MATCH.csv` (this seat's count), 273 of the 300 `none` rows carry the reason `none`. Only 27 carry a reason (`AMBIGUOUS`).
For each of the 273, the record must say why it did not match. Possible reasons include: no crosswalk row for the account, no Commonwealth account under the predecessor key, or a predecessor outside the firm. Remedy: give each of the 273 `none` rows a stated reason, keep every other row unchanged, and record the new sha256."
And the CTO's ruling (msg 7328): "a reason per none row from a closed list written before the read (no Commonwealth account for the household, a new client after the migration, a name/SSN-free mismatch, other)."
The file: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/REVERSE_MATCH.csv` (header `account_key,predecessor_key,match_basis,reason`; 769 rows; sha256 20fb38333542b23beab5a61316cf9acdc0119dbf0be85b55fe150ec191c09a64) and the round-82 record
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~161/ACTIVE_SET_RECORD.json` (its `sources` say what was read and how the 769 were defined and keyed; the migration facts: Commonwealth transactions end 2026-06-22, Black Diamond silver holdings begin 2026-06-08, the gold canonical holdings begin 2026-04-22).

**Your item.**

1. **Write the closed list FIRST, and commit it before you read anything to classify.** A file `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~167/NONE_REASON_LIST.md` holding, for each reason, its code, its definition as a TEST on data you can read (not a story), and the data it reads. Codes, exactly: `NO_COMMONWEALTH_HOUSEHOLD` (no Commonwealth account exists for the household: say what "household" is joined on in the data, or that no such join exists),
   `NEW_CLIENT_AFTER_MIGRATION` (the Black Diamond account's first record is dated after the migration date: state the date you use and why), `MISMATCH_NO_IDENTIFIER` (a candidate Commonwealth account exists but the crosswalk could not match it and the identifiers that would settle it are absent: the CTO's "name/SSN-free mismatch"; state what is absent), `OTHER` (anything else: it carries a sub-code of at most 3 words in the record, never an invented class).
   A reason is assigned by the FIRST test it passes in that order; an account that passes none is `OTHER`. Commit the list alone (`safe-commit`, its own commit) and quote its commit hash in the record; the classification script must not be written before that commit.
2. **Classify the 273.** For each of the 273 rows whose `reason` is `none` (and only those), assign one code by the tests. Reuse the keys the file already carries; do not re-derive the 769 or change `predecessor_key`, `match_basis` or any of the 27 `AMBIGUOUS` rows. Report the count per code, and per code how many accounts had a candidate Commonwealth account (a count only).
3. **Write the new file** `C:/dev/_cotbkf_active_set_20261013/REVERSE_MATCH_V2.csv`: the same header and 769 rows, in the same order, with the `reason` of each of the 273 set to its code and EVERY OTHER byte of EVERY OTHER row identical to the committed file (a byte-for-byte diff over the 496 other rows: report 0 differences and print the control: a copy with one other row changed, on which your diff must report 1). Report its rows, bytes and sha256.
4. **The record** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~167/NONE_REASONS_RECORD.json` and a short `.md`, no account key, number or value in either. Top-level keys, exactly: `list_commit` (the hash of the commit that carried NONE_REASON_LIST.md, with the time), `none_rows` (the 300), `reasonless_before` (273), `by_code` (a dict of counts that sums to 273), `with_candidate_by_code`, `unchanged_rows` (496), `unchanged_rows_byte_equal` (true or false), `diff_control` (`{"mutant_rows_changed", "diff_reported"}`), `file` (`{"path", "rows", "bytes", "sha256"}`), `sources`, `headline`, `not_established`.

### ACCEPTANCE

<criterion id="CB84cf1-AC1" cell_refs="CB-cf-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~167/NONE_REASONS_RECORD.json',encoding='utf-8'));b=d['by_code'];print('NONE-REASONS reasonless_before=%d assigned=%d codes=%s unchanged=%d byte_equal=%s control_reported=%s'%(d['reasonless_before'],sum(b.values()),sorted(b),d['unchanged_rows'],d['unchanged_rows_byte_equal'],d['diff_control']['diff_reported']))"</invocation><expect>NONE-REASONS reasonless_before=273 assigned=273</expect></criterion>
`CB84cf1-AC1` -- every one of the 273 rows has exactly one code, the 496 other rows are byte-equal with a control that fires.

<criterion id="CB84cf1-AC2" cell_refs="CB-cf-1"><invocation>python -c "import json,hashlib,csv;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~167/NONE_REASONS_RECORD.json',encoding='utf-8'));f=d['file'];b=open(f['path'],'rb').read();codes={'NO_COMMONWEALTH_HOUSEHOLD','NEW_CLIENT_AFTER_MIGRATION','MISMATCH_NO_IDENTIFIER','OTHER'};r=list(csv.DictReader(open(f['path'],encoding='utf-8')));n=[x for x in r if x['predecessor_key']=='none'];print('REVERSE-MATCH-V2 rows=%d sha256_match=%s bytes_match=%s none_rows=%d none_without_code_or_reason=%d outside_repo=%s'%(len(r),hashlib.sha256(b).hexdigest()==f['sha256'],len(b)==f['bytes'],len(n),sum(1 for x in n if x['reason'] in ('','none')),not f['path'].startswith('org/')))"</invocation><expect>REVERSE-MATCH-V2 rows=769 sha256_match=True</expect></criterion>
`CB84cf1-AC2` -- the new file has 769 rows at the recorded checksum, no `none` row is left without a reason, and it is outside the repository.

<criterion id="CB84cf1-AC3" cell_refs="CB-cf-1" judgment="true"/>
`CB84cf1-AC3` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the list was committed before the classification was written and its tests are on data, not stories; every one of the 273 rows has a code from the list and `OTHER` carries a sub-code, not an invented class; the 27 `AMBIGUOUS` rows and the 469 matched/near rows are unchanged; the migration date used is stated with its reason; `NO_COMMONWEALTH_HOUSEHOLD` is claimed only if a household join exists in the data, else the record says no such join exists; no account key, number or value appears in the record, the report or any message.

<expected_criteria>CB84cf1-AC1,CB84cf1-AC2,CB84cf1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row), the new folder file `C:/dev/_cotbkf_active_set_20261013/REVERSE_MATCH_V2.csv` (that one file) and the file of this order.
- **You change no code, test, config, manifest or registry, and you do not edit `REVERSE_MATCH.csv`, `ACTIVE_COTTONWOOD_SET.csv` or the scan test.** The exemption for the new file is the issuer's act at the drain (its path and sha256 go into the test's pinned list).
- **AWS: READ-ONLY, through the `.tools/aws` shim,** of the tables the round-82 record lists (the Commonwealth silver tables at `date=2026-06-23/`, the Black Diamond holdings keys); no listing beyond the one prefix listing the record describes (state its denominator); no write, delete or serve; no other bucket; no restricted CRM prefix. If a read is refused, record the exact error and mark that part `not_established`.
- **Account numbers and values are never printed, committed or sent.** Counts, dates, codes and CUSIPs only. Do not run `aws sts get-caller-identity`. Do not list or open `C:/dev/_cotbkf_private_evidence_20261009/` in any way.
- After your commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`; report its DENOMINATOR line (your committed files carry no account key, so it should read 0 hits beyond the two pinned files).
- **NEVER `--apply`, `--remint`, `--overwrite`, a serve, or any S3 write or delete against a real bucket.** No push. No `--refresh`. **No vendor call and no fetch;** no Black Diamond API call.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- Searches go through the estate's tools; a recursive shell search of the repository is denied by a hook and is not retried another way.
- **No gate override** of any kind and no `--force`. Do not weaken, delete, xfail or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D2-W167-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock (`date -u +%FT%TZ`),
  APPENDED to the channel file with `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant for the repository. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round84.md</decomp_doc> (round 84), cell `CB-cf-1`.
<owned_cells>CB-cf-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB84cf1-AC1, CB84cf1-AC2, CB84cf1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~167/ADVI_COTBKF.TO-CB-cf-1.reasons-for-the-none-rows.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB84cf1-AC1,CB84cf1-AC2,CB84cf1-AC3` BEFORE the flip. Mechanical: CB84cf1-AC1, CB84cf1-AC2. A judgment criterion is recorded with status `UNVERIFIABLE-BY-INSTRUMENT` and a `status_reason` that begins `PENDING-ADJUDICATION`, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`. The external CSV is declared in `declared_exclusions` if the checker refuses it as a file artifact. **YOU flip your own order `<status>` to `complete` in the commit that carries the proof instance** (the flip is inside your grant: the order's own face is lane ANY).
</proof_of_spec>

**REPORT:** FIRST the list commit and the count per code (one line). Then: the migration date used and why; whether a household join exists; per code the candidate counts; the diff control; the new file's rows, bytes and sha256; every remote read made; the `NONE-REASONS` and `REVERSE-MATCH-V2` lines; the account-id scan's DENOMINATOR line; what is not established; commits; every gate refusal and hook denial, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read of silver and holdings tables; nothing is scheduled or served.
comp-iam: DECLARED-NOT-APPLICABLE no lens was run: read-only calls on Opal data under the existing role, as the bounds list them; no write, delete or serve, and no new permission.
comp-adversary: RUN -- the list is committed before the classification exists; tests are on data; the 496 other rows are byte-equal with a firing control; `OTHER` is a sub-coded remainder, not an invented class; BLIND: a household join that exists only in a system not read, and an account that opened before the migration but first held a position after it.
lane: the <paths> block IS the grant (worker RULING 1); the one new CSV sits outside the repository by design.
</preflight>

Source: `1.0.0_SA_CTO~DELL2` msg 7328 (ruling on the CVO's slug 7327); `3.0.0_SA_CVO` `ADJUDICATION_v59` @e819f0fc64 and the round-82 L9 grade (CB82cd1-AC3).
