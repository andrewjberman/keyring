# TO ADVI_COTBKF.TO-CB-ca-3.store-writer -- round 79 CB-ca-3: what wrote the live price store object: which code, which run, whose, from its retained versions and the tree's history

<to_id>ADVI_COTBKF.TO-CB-ca-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~153</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>79</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-ca-3` (`decompositions/ADVI_COTBKF_DECOMP.round79.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a READ of one object's versions and of the tree's history. You change no code. Nothing is written to any bucket.**

**Read first:** `org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md`, the two sections headed `## ADDENDUM v0.8` (near line 292: it is also the round-79 analysis and holds the ENRICHMENT LIST) and `## ADDENDUM v0.9` (near line 343, the SIGNED text: it REPLACES item 2 of C-BASIS; v0.8's two tokens AS_TRADED and ADJUSTED are WITHDRAWN and are not used anywhere), the paragraph accepting rows D2-W149-S1 and D2-W149-S2, and ENRICHMENT LIST item 3, word for word: "What
wrote the live store object: which code, which run, whose (row D2-W149-S1), from the object's two retained versions and the tree's
history." Then row ADVI_COTBKF-D2-W149-S1 in the channel (the live store object has no `source_firm` column, which the writer at
HEAD writes at `build_canonical_prices_v2.py:873`, and carries a `scoped_override` source on 12,042 rows, which that writer never
assigns), the round-78 record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~149/STORE_UNADJUSTED_FIELD.json` (the object: its key as the code names it, 97,443,387 bytes, 11,289,398 rows, last
modified 2026-10-09T13:41:04Z; the writer is not in the live step list) and the census `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~143/CLOSE_READERS.json` (the writer's step, its
schedule state, its owner not established).

**The object on disk:** the live version is already at `C:/dev/wk-cotbkf-84/.scratch/w149/store/` (downloaded by the round-78 worker; this firm's).

**Your item.**

1. **The object's versions:** every retained version of that ONE key (a version listing of the one key; the analysis expects two):
   version id, last-modified time (UTC), size, which is current. For the NON-current version: its schema and its distinct `source`
   values with counts (ONE get of that one version, read-only), set beside the live one's. What changed between them: columns,
   rows, sources, the date range, and for the 15 funds (VEIRX, PCBIX, ABNFX, SGIIX, GFFFX, FOCPX, FCNTX, PRILX, BALCX, AGTHX, DISVX, DFLVX, NFFFX, MEIIX, VGHAX) whether their prices changed (count of changed fund-days).
2. **Which code wrote the live one, from the tree's history:** every file in the tree that writes this key or assigns the source
   `scoped_override` (search with the estate's tools, each sweep's denominator printed); for the writer `build_canonical_prices_v2.py`
   and any sibling, the commits that changed its output columns or its sources, with dates (`git log` on the NAMED file), so the
   live object's shape can be matched to a version of the code: the commit range in which a writer produced exactly these columns
   and these sources. Deployed code may differ from the repository: where the pipeline's deployed copy is named in the tree (a code
   prefix the steps run from), say so and say it was not read.
3. **Which run, and whose:** what the tree records of a run at or near each version's time: a step list or schedule that names the
   writer (file and line), a deploy or change-management entry, a drive log, a commit message, a task order that says it ran the
   step; the seat and project named there. If the tree names none, `run` is `not_established` and you say which record WOULD
   settle it (an execution log, a command history) without reading outside the grant.
4. **The owner today:** the project and seat that own the writer and the store now, from the tree; or `not_established`, with the
   closed projects that built it named.
5. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~153/STORE_WRITER.json` and a short `.md`. Top-level keys, exactly: `key_as_named_in_code`, `versions` (a list of
   `{"version", "last_modified", "size", "current", "columns", "sources"}`), `changed_between_versions`, `the_15_changed_fund_days`,
   `writers_in_the_tree` (a list, with each sweep's denominator), `code_that_matches_the_live_shape` (`{"file", "commit_range",
   "matches": true|false|"not_established"}`), `run` (`{"when", "what_the_tree_records", "whose"}` or the string `not_established`),
   `owner_today`, `headline`, `not_established`.

### ACCEPTANCE

<criterion id="CB79ca3-AC1" cell_refs="CB-ca-3"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~153/STORE_WRITER.json',encoding='utf-8'));v=d['versions'];m=d['code_that_matches_the_live_shape'];r=d['run'];print('STORE-WRITER versions=%d current=%d live_columns=%d live_sources=%d writers_in_the_tree=%d code_matches=%s commit_range=%s run=%s owner_today=%s the_15_changed_fund_days=%s'%(len(v),sum(1 for x in v if x['current']),len([x for x in v if x['current']][0]['columns']),len([x for x in v if x['current']][0]['sources']),len(d['writers_in_the_tree']),m['matches'],str(m['commit_range'])[:40],('not_established' if isinstance(r,str) else str(r.get('whose'))[:40]),str(d['owner_today'])[:40],d['the_15_changed_fund_days']))"</invocation><expect>STORE-WRITER versions=</expect></criterion>
`CB79ca3-AC1` -- the one key's retained versions are listed with exactly one current; the writers in the tree are swept; the live
object's shape is matched to a range of the code's history or stated as not matched. The issuer reads the run and the owner.

<criterion id="CB79ca3-AC2" cell_refs="CB-ca-3" judgment="true"/>
`CB79ca3-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: "which code" rests on the object's own columns and
sources matched to the code's history, not on a file's name; "which run" and "whose" rest on a record in the tree, and
`not_established` is used where there is none; deployed code is not assumed equal to the repository's; one key's versions were
read and nothing was written.

<expected_criteria>CB79ca3-AC1,CB79ca3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.**
- **AWS: READ-ONLY, ONE key of THIS project's firm:** a version listing of that one key, a head of each version, and ONE get of the
  one non-current version. No other key, no bucket listing, no write, no delete, no restore of a version, no serve.
- **Another firm's data is never opened.** No account id: this cell reads prices, dates, tickers and the tree's history.
- Searches go through the estate's tools; a recursive shell search of the repository is denied by a hook and is not retried another way.
- After your commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`;
  keep CUSIPs in CSV columns named exactly `cusip` and tickers elsewhere; report its DENOMINATOR line.
- **NEVER `--apply`, `--remint`, `--overwrite`, a serve, or any S3 write or delete against a real bucket.** No push. No `--refresh`.
  **No vendor call and no fetch** (no Yahoo, no Bloomberg, no gateway series pull): what is on disk is read, never refreshed. A
  read of the store's versions is a read of an Opal artifact, not of a vendor.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity, share balance or return. Counts, dates, CUSIPs, tickers, a
  security's price or per-share distribution, ratios and reason codes only.
- **No gate override** of any kind and no `--force`. Do not weaken, delete, xfail or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W153-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round79.md</decomp_doc> (round 79), cell `CB-ca-3`.
<owned_cells>CB-ca-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB79ca3-AC1, CB79ca3-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~153/ADVI_COTBKF.TO-CB-ca-3.store-writer.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB79ca3-AC1,CB79ca3-AC2` BEFORE the flip. Mechanical: CB79ca3-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the one key's retained versions with their times, sizes, columns and sources; what changed between them, and for the 15 funds; every writer of the key or of the scoped_override source in the tree, each sweep with its denominator; the commits that changed the writer's output, and the range that matches the live shape, or that none does; the run and whose, from a record in the tree, or not established with what would settle it; the owner today; every remote read made; the `STORE-WRITER` line; the account-id scan's DENOMINATOR line; what is not established; commits; every gate refusal and hook denial, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read of one key's versions and of the tree's history; nothing is scheduled or served.
comp-iam: DECLARED-NOT-APPLICABLE no lens was run: read-only calls on this firm under the existing role, as the bounds list them; no write, delete or serve, and no new permission.
comp-adversary: RUN -- which code is decided by the object's own columns and sources against the code's history, never by a file's name; which run and whose need a record in the tree, and not-established is legal with what would settle it; deployed code is not assumed equal to the repository's; no version is restored or deleted; BLIND: a run made from a shell that left no record in the tree.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` PRD ADDENDUM v0.8 @fab39b5beb, which is also the round-79 analysis (msg 6275), its ENRICHMENT LIST item 3, with ADDENDUM v0.9 @95da777fbf (msg 6282), the SIGNED text; `3.0.0_SA_CVO` REMEDIATION_v47 @77527824fd.
