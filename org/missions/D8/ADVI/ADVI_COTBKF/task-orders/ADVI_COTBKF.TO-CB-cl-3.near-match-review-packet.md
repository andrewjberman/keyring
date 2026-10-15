# TO ADVI_COTBKF.TO-CB-cl-3.near-match-review-packet -- round 90 CB-cl-3: ONE review packet of the candidate links for a person to confirm: link ids and corroboration flags only, one row per distinct pair, no personal value; nothing is applied

<to_id>ADVI_COTBKF.TO-CB-cl-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~180</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>90</round>
<workstream>~C1</workstream>

**Directive:** D8 | **Fabric:** dell1 (placement DELL1) | **Decomp cell:** `CB-cl-3` (`decompositions/ADVI_COTBKF_DECOMP.round90.md`) |
**outcome_ref:** FWD-8, FWD-9 | **depends_on:** none (reads round 87's outputs)

---

## WORKER FACE

### THE CELL

**Why.** FWD-9: a link is never guessed. Round 87 produced candidate links by two routes, which are not links until a person confirms them: the R4 route (a Commonwealth account's name reaches one Black Diamond household, then the holdings fingerprint inside it; 99 CANDIDATE links, 85 of them to one of the 219 reachable unmatched active accounts) and the exact-name route (14 one-to-one pairs, 13 among the 219). The CTO's round-88 analysis item 4: ONE review packet, link ids and corroboration flags, no personal value; who the person is (Andrew, or a Cottonwood operator he names) goes to Andrew with the packet. Nothing is applied, no candidate is promoted, and nobody at Cottonwood is contacted. You build the packet.

**Read first (under the repository root `C:/dev/wk-cotbkf-180`, with the outside inputs by their absolute path):**
1. `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~175/R4_RECORD.json` and `.md` (the R4 rule, its tiers, the derived window, the control result; the file columns: `commonwealth_account,bd_account_id,tier,household_via,fingerprint_score,window_ok,candidates_in_household`).
2. `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~176/NAME_REVIEW_RECORD.json` and `REVIEW_LIST.csv` (committed; columns `link_id,date_window_ok,same_registration_class,holdings_candidate,already_claimed,corroborations,in_219,tier`) and the module `data/assets/scripts/silver/commonwealth_match_names.py` (`link_id(cw_account, bd_account)`: the first 12 hex digits of `sha256("commonwealth_account|bd_account_id")` of the two raw ids; reuse by `import`).
3. The outside files (raw account ids, OUTSIDE the repository; read them in memory, never copy a value out): `C:/dev/_cotbkf_match_20261015/R4_LINKS.csv` (110 rows: 11 DETERMINISTIC, 99 CANDIDATE), `C:/dev/_cotbkf_match_20261015/REVIEW_KEY.csv` (columns `link_id,commonwealth_account,bd_account_id`; 14 rows) and `C:/dev/_cotbkf_match_20261015/R3_LINKS.csv` (R3: 88 links, 0 to active accounts; context only).
4. The reverse match `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/REVERSE_MATCH_V3.csv` (sha256 `0783f088aecbf29e46751aa5d80239b8aa53f16484778162e34ee1c09783c66f`; `account_key,predecessor_key,match_basis,reason`): its `none` rows whose reason is not `NEW_CLIENT_AFTER_MIGRATION` are the 219 reachable accounts; its `near_match_waiting_on_a_person` rows are accounts already waiting on a person.

**Your items.**

1. **The pair set.** Union, by the pair (Commonwealth account, Black Diamond account): the R4 CANDIDATE rows, the R4 DETERMINISTIC rows (kept in the packet because a person should know they exist and that they rest on a fingerprint; they carry tier DETERMINISTIC and are NOT part of the 'to confirm' count), and the exact-name rows. One row per DISTINCT pair; a pair found by both routes is ONE row with `routes` naming both (`R4`, `NAME`). Print the denominators: R4 rows, name rows, overlap, distinct pairs.
2. **The row, ids and flags only.** Columns exactly `link_id,routes,r4_tier,r4_household_via,r4_window_ok,r4_fingerprint_band,name_corroborations,in_219,bd_account_state,competing_pairs`:
   - `link_id` as above; `routes` `R4`, `NAME` or `R4+NAME`; `r4_tier` DETERMINISTIC, CANDIDATE or blank; `r4_household_via` `name` or `client_line` or blank; `r4_window_ok` true, false or blank; `r4_fingerprint_band` the R4 fingerprint score in the band `<0.5`, `0.5-0.8`, `>=0.8` (a band, never the number); `name_corroborations` the integer 0 to 3 from the name list or blank; `in_219` true or false; `bd_account_state` `unmatched_active`, `new_client`, `near_match_waiting` or `other` (from the reverse match); `competing_pairs` the count of OTHER distinct pairs in the packet that share the same Commonwealth account or the same Black Diamond account (a pair with a competitor is a conflict a person must see).
   No account number, no name, no name token, no hash other than `link_id`, no raw fingerprint score and no value of any kind appears in the row.
3. **The packet.** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~180/NEAR_MATCH_REVIEW_PACKET.csv` (committed; the columns above, sorted by `link_id`, LF, header line) and `NEAR_MATCH_REVIEW_PACKET.md` (committed; a short plain-English page for a person: what the packet is, what each column means, how many rows by `routes` and `r4_tier`, how many are among the 219, how many have a competing pair, and the line "no link here is applied; a link applies only on a person's word; Andrew names who confirms"). The KEY that lets that person resolve a link id to its two accounts goes OUTSIDE the repository: `C:/dev/_cotbkf_match_20261015/NEAR_MATCH_REVIEW_KEY.csv` (columns `link_id,commonwealth_account,bd_account_id`; one row per packet row).
4. **The consistency checks (counts, in the record).** Every `link_id` of the committed `REVIEW_LIST.csv` that is in `REVIEW_KEY.csv` appears in the packet with the same flags where both carry one (state any disagreement by count); every R4 CANDIDATE row appears; every packet `link_id` resolves in the outside key; the packet's `in_219` rows are a subset of the 219.
5. **The script and test.** `data/assets/scripts/silver/cotbkf_review_packet.py` builds the packet from the three outside files and the reverse match (pure functions on frames; `main()` takes `--out-key PATH` and `--out-dir DIR`), with a test `data/assets/scripts/silver/tests/test_cotbkf_review_packet.py` on stub frames and made-up ids (`A1`, `B1`) proving four things, one test each: a pair found by both routes is ONE row with `R4+NAME`; `competing_pairs` counts the other pairs sharing an account; the row has exactly the ten columns and no id column other than `link_id`; a fingerprint score is emitted only as a band. The script carries no account number or name.
6. **The record** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~180/REVIEW_PACKET_RECORD.json` with exactly these top-level keys: `denominators` (`{"r4_rows", "name_rows", "overlap", "distinct_pairs"}`), `rows` (`{"total", "by_routes", "by_r4_tier", "in_219", "to_confirm", "with_competing_pair"}`), `consistency` (`{"review_list_rows_found", "flag_disagreements", "r4_candidates_present", "unresolved_link_ids"}`), `files` (a list of 3: `{"name", "path", "rows", "sha256"}`: the committed csv, the committed md, the outside key), `scratch_deleted` (true only when you deleted every value-bearing scratch file), `not_established`; and a short `.md`. No account number or name in either.

### ACCEPTANCE

<criterion id="CB90cl3-AC1" cell_refs="CB-cl-3"><invocation>python -c "import csv,re;p='org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~180/NEAR_MATCH_REVIEW_PACKET.csv';r=list(csv.reader(open(p,encoding='utf-8')));cols='link_id,routes,r4_tier,r4_household_via,r4_window_ok,r4_fingerprint_band,name_corroborations,in_219,bd_account_state,competing_pairs';ids=[x[0] for x in r[1:]];ok=all(re.fullmatch('[0-9a-f]{12}',i) for i in ids);print('REVIEW-PACKET columns=%s rows=%d ids12hex=%s unique=%s sorted=%s'%(','.join(r[0])==cols,len(r)-1,ok,len(set(ids))==len(ids),ids==sorted(ids)))"</invocation><expect>REVIEW-PACKET columns=True rows=\d+ ids12hex=True unique=True sorted=True</expect></criterion>
`CB90cl3-AC1` -- the committed packet has exactly the ten columns, one row per distinct pair, ids only in the row, sorted.

<criterion id="CB90cl3-AC2" cell_refs="CB-cl-3"><invocation>python -c "import json,hashlib,csv;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~180/REVIEW_PACKET_RECORD.json',encoding='utf-8'));ok=all(hashlib.sha256(open(f['path'],'rb').read()).hexdigest()==f['sha256'] for f in d['files']);k=[f for f in d['files'] if f['name'].endswith('KEY.csv')][0];n=sum(1 for _ in open(k['path'],encoding='utf-8'))-1;print('REVIEW-PACKET-FILES files=%d sha_match=%s key_outside_repo=%s key_rows_eq_packet=%s unresolved=%d scratch_deleted=%s'%(len(d['files']),ok,not k['path'].startswith('org/'),n==d['rows']['total'],d['consistency']['unresolved_link_ids'],d['scratch_deleted']))"</invocation><expect>REVIEW-PACKET-FILES files=3 sha_match=True key_outside_repo=True key_rows_eq_packet=True unresolved=0 scratch_deleted=True</expect></criterion>
`CB90cl3-AC2` -- the three files carry the recorded checksums, the key sits outside the repository with one row per packet row, every link id resolves, and the value-bearing scratch is deleted.

<criterion id="CB90cl3-AC3" cell_refs="CB-cl-3"><invocation>python -m pytest data/assets/scripts/silver/tests/test_cotbkf_review_packet.py -q</invocation><expect>4 passed</expect></criterion>
`CB90cl3-AC3` -- the four packet rules hold on stubs.

<expected_criteria>CB90cl3-AC1,CB90cl3-AC2,CB90cl3-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below and the one outside file `C:/dev/_cotbkf_match_20261015/NEAR_MATCH_REVIEW_KEY.csv`. You edit no existing file, module or test, and you do not edit the outside inputs.
- **NO S3 call of any kind, no AWS call, no CRM key.** This is a pure local read of committed files and the outside files named above.
- **No account number, name, name token, or value** in any committed file, test fixture, log line, message or report: the packet carries link ids and flags; counts only in the record and the report. Scratch under the worktree `.scratch/` never committed and deleted when you finish (it holds per-pair values).
- After your last commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`; if it fails closed because the pinned set is absent on this box, report the exact error and do NOT look for the set.
- **NEVER** apply or promote a link, edit the crosswalk or the reverse match, contact Cottonwood, push, override a gate or `--force`; do not weaken, delete, xfail or skip any test. If a gate refuses a function name or a dtype call, rename or adapt without behaviour change; never override.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D1-W180-S<k>` (k from 1), `"fabric": "dell1"`, `surfaced_at` read from the clock (`date -u +%FT%TZ`), APPENDED to the channel file with `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only.

<paths>
data/assets/scripts/silver/cotbkf_review_packet.py
data/assets/scripts/silver/tests/test_cotbkf_review_packet.py
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant for the repository. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round90.md</decomp_doc> (round 90), cell `CB-cl-3`.
<owned_cells>CB-cl-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB90cl3-AC1, CB90cl3-AC2, CB90cl3-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~180/ADVI_COTBKF.TO-CB-cl-3.near-match-review-packet.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB90cl3-AC1,CB90cl3-AC2,CB90cl3-AC3` BEFORE the flip. All three criteria are mechanical. An artifact already committed and not changed in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`. Declare the outside key in `declared_exclusions` if the checker refuses it as a file artifact. **YOU flip your own order `<status>` to `complete` in the commit that carries the proof instance, and only when every criterion PASSES** (the flip is inside your grant: the order's own face is lane ANY).
</proof_of_spec>

**REPORT:** FIRST the packet line: distinct pairs, rows by `routes` and `r4_tier`, `to_confirm`, among the 219, with a competing pair. Then: the denominators (R4 rows, name rows, overlap); the consistency counts; the three criterion lines; the account-id scan result or exact error; commits; every gate refusal and hook denial, verbatim. Say that no account number or name left memory except into the outside key, and that scratch was deleted.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a local read of committed files and outside files; nothing is scheduled, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call at all; no role, no permission.
comp-adversary: RUN -- FWD-9 says a link is never guessed: the packet applies nothing and says so; the row carries ids and bands, so a person reading it sees no personal value; AC2 requires every link id to resolve in the outside key; BLIND: a link id is a 12-hex prefix of a hash of two raw ids, so anyone holding the raw ids can recompute it (the ids are client account numbers; the packet is for a person who already holds them, and a leak of the packet alone reveals no value), the fingerprint is shown as a band so a person cannot see the score the rule used, and the packet cannot say which candidate is RIGHT (only that it passed or failed the rule's tests).
lane: the <paths> block IS the grant (worker RULING 1). A local read: nothing is written to S3 or applied.
</preflight>

**ISSUER NOTES:** Source: CTO round-88 analysis item 4 (msg 6222): "ONE review packet, the 85 R4 candidates and the 13 exact-name rows, as link ids and corroboration flags, with no PII values. Who the person is (Andrew, or a Cottonwood operator he names) is carried to him with the packet." Row `W175-S4` (links land on near matches and new-client accounts) is why `bd_account_state` is a column.
