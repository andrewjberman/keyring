# TO ADVI_COTBKF.TO-CB-ci-2.yahoo-readers-of-active-accounts -- round 87 CB-ci-2: every reader that can put a Yahoo-index price into an active Cottonwood account's value or return, listed with file and line and whether it filters on use_class, porting_verdict or claim

<to_id>ADVI_COTBKF.TO-CB-ci-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~173</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>87</round>
<workstream>~C1</workstream>

**Directive:** D8 | **Fabric:** dell1 (placement DELL1) | **Decomp cell:** `CB-ci-2` (`decompositions/ADVI_COTBKF_DECOMP.round87.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Why.** Andrew, 2026-10-15: "Active accounts should get BBG pricing exclusively." The CTO's guard: a Yahoo price held under the label `NOT_FOR_ACTIVE` must never feed an active account's return. The guard is only as wide as the set of places that read Yahoo prices. One reader, `commonwealth_price_need.py`, is being fixed in another cell. Nobody has listed the others. **This cell is a READ. You change no code, no test and no committed file.** You list every place in the repository that can carry a price from the Yahoo price store or its index into an account's daily value or return, say whether each one filters on the new class, and count them.

**The Yahoo price store:** per-CUSIP files under `opal_naming.address("yahoo","global","silver","price_history", ...)` (`cusip=<CUSIP>/` folders and an `index/index.parquet`), written by the MDPF_DEMQUE code in `data/mdpf/scripts/demque/price_store.py` (read its docstring: `write`, `index`, `s3_root`). The index carries `cusip, valid_from, valid_to, claim`, a `porting_verdict` column, and (landing now) a `use_class` column whose values are `NOT_FOR_ACTIVE` (names held in the active set V2) and `INACTIVE_USE`.

**Read first (under the repository root):**
1. `data/assets/scripts/silver/commonwealth_price_need.py` (one known reader; its sections "the porting verdict" and `need_rows` show what a filter looks like).
2. The valuation chain: `data/assets/scripts/silver/commonwealth_daily_valuation.py`, `commonwealth_daily_returns.py`, `commonwealth_daily_holdings.py`, and the ARD mint path (files under `data/assets/scripts/silver/` whose names contain `ard`): how a holding is priced, and from which store.
3. `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ACTIVE_COTTONWOOD_SET_V2.csv` is the active set; you do NOT need to open it (it carries raw account numbers). "Active account" in this cell means an account in that set.

**Your items.**

1. **The search.** Search the repository checkout at `C:/dev/ajb_workspace` (READ only: your own worktree is sparse and does not carry the whole tree; state the commit you searched with `git -C C:/dev/ajb_workspace rev-parse HEAD`). Use the estate's search tool (`comp-find`, with `--files` and `-i` for a token census; a recursive shell grep is denied by a hook and is not retried another way) and the native Grep tool. Search, as a census with the denominator printed, for each of these tokens over `data/`, `lib/`, `infra/aws/lambda/`, `integrations/` and `org/modules/`: `price_history`, `yahoo/global`, `price_store`, `demque_index` / `index.parquet` next to `yahoo`, `porting_verdict`, `use_class`, `as_traded_close`. Print each token's count of files.
2. **The readers.** From the hits, list every file that READS a Yahoo-store price or its index (not the code that writes the store, not a test, not a document), and for each decide the one question: can the price it reads reach an account's daily value, an account return, or a figure shown for an account? Classify each reader exactly one of: `FEEDS_ACCOUNT_VALUE` (the price becomes part of an account-day value or return), `RANKS_OR_REPORTS` (a need list or report that does not value an account), `FEEDS_OTHER` (reaches a non-account figure, say what), `NOT_A_READER` (a false hit, say why). For each `FEEDS_ACCOUNT_VALUE` and `RANKS_OR_REPORTS` reader record `file`, `line` (the line that reads the price or index), `filters_on` (a subset of `use_class`, `porting_verdict`, `claim`, `valid_range`, `none`), and `fails_closed` (true / false / `not_applicable`).
3. **Count, do not judge.** The record counts readers by class and by `filters_on`, and names the readers that are `FEEDS_ACCOUNT_VALUE` with `filters_on` not containing `use_class` (the GAPS). It does not propose a fix and does not edit anything. A reader you cannot classify from the code is `UNREAD` with the reason, never a guess.
4. **The record** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~173/READERS_RECORD.json` with exactly these top-level keys: `searched_commit`, `tokens` (a list of `{"token", "files"}`), `denominator` (what was searched and the scope each token's count covers), `readers` (a list of `{"file", "line", "class", "filters_on", "fails_closed", "note"}`; `note` at most one line, no account number), `counts` (`{"feeds_account_value", "ranks_or_reports", "feeds_other", "not_a_reader", "unread", "gaps"}`), `gaps` (the list of `{"file", "line"}`), `not_established`; and a short `.md` with the same table. No account number, name or dollar value appears in either.

### ACCEPTANCE

<criterion id="CB87ci2-AC1" cell_refs="CB-ci-2"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~173/READERS_RECORD.json',encoding='utf-8'));c=d['counts'];n=len(d['readers']);s=c['feeds_account_value']+c['ranks_or_reports']+c['feeds_other']+c['not_a_reader']+c['unread'];print('YAHOO-READERS readers=%d feeds_account_value=%d ranks=%d other=%d unread=%d gaps=%d counts_sum=%s tokens=%d'%(n,c['feeds_account_value'],c['ranks_or_reports'],c['feeds_other'],c['unread'],c['gaps'],s==n,len(d['tokens'])))"</invocation><expect>counts_sum=True</expect></criterion>
`CB87ci2-AC1` -- the readers are counted by class, the counts sum to the list, and the tokens searched are listed.

<criterion id="CB87ci2-AC2" cell_refs="CB-ci-2"><invocation>python -c "import json,os;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~173/READERS_RECORD.json',encoding='utf-8'));root='C:/dev/ajb_workspace/';bad=[];[bad.append(r['file']) for r in d['readers'] if r['class'] in ('FEEDS_ACCOUNT_VALUE','RANKS_OR_REPORTS','FEEDS_OTHER') and not (os.path.isfile(root+r['file']) and len(open(root+r['file'],encoding='utf-8',errors='replace').read().splitlines())>=int(r['line']))];g=[x for x in d['readers'] if x['class']=='FEEDS_ACCOUNT_VALUE' and 'use_class' not in x['filters_on']];print('YAHOO-READERS-CITES unresolved=%d gaps_match=%s'%(len(bad),len(g)==d['counts']['gaps']==len(d['gaps'])))"</invocation><expect>unresolved=0 gaps_match=True</expect></criterion>
`CB87ci2-AC2` -- every cited file exists and has at least the cited line, and the gaps count equals the account-value readers that do not filter on `use_class`.

<expected_criteria>CB87ci2-AC1,CB87ci2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below only: your own deliverables folder and your own NEW channel row. You change no code, test, config or existing file; this is a read.
- **Reads.** The repository checkout at `C:/dev/ajb_workspace` by absolute path (read only), through `comp-find` and the native Read / Grep / Glob tools. No S3 read is needed and none is allowed except `git`-free local reads; no vendor call; no AWS call of any kind.
- **No account number, name or dollar value** in the record, the report or any message. File paths, line numbers, token names and counts only. Do not open the active-set file.
- **NEVER** edit, run a script that writes, apply, deploy or push. No gate override and no `--force`. Scratch under the worktree `.scratch/`, never committed.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D1-W173-S<k>` (k from 1), `"fabric": "dell1"`, `surfaced_at` read from the clock (`date -u +%FT%TZ`), APPENDED to the channel file with `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant for the repository. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round87.md</decomp_doc> (round 87), cell `CB-ci-2`.
<owned_cells>CB-ci-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB87ci2-AC1, CB87ci2-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~173/ADVI_COTBKF.TO-CB-ci-2.yahoo-readers-of-active-accounts.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB87ci2-AC1,CB87ci2-AC2` BEFORE the flip. Both criteria are mechanical. An artifact already committed and not changed in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`. **YOU flip your own order `<status>` to `complete` in the commit that carries the proof instance, and only when every criterion PASSES** (the flip is inside your grant: the order's own face is lane ANY).
</proof_of_spec>

**REPORT:** FIRST the counts line (readers, by class; the gaps). Then: the token census with its denominator; the gaps by file and line; the readers you could not classify and why; the two criterion lines; commits; every gate refusal and hook denial, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read of source files; nothing is scheduled, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call at all.
comp-adversary: RUN -- the census counts files by token, so a reader that builds the store address from parts, or reads it through an intermediate file or table, would not match any token; BLIND by design, and the record's `not_established` must say so; the cell counts and cites, it does not certify that the guard is complete.
lane: the <paths> block IS the grant (worker RULING 1). A read: nothing outside the deliverables folder and the one channel row is written.
</preflight>

Source: `1.0.0_SA_CTO~DELL1` msg 6119 (condition C3: the guard is that a NOT_FOR_ACTIVE Yahoo price never feeds an active account's return); `MDPF_DEMQUE/ledger/NEVER_WIDEN_R9_INACTIVE_YAHOO_CTO_HALF.md`.
