# AMGT_RESAPP task order -- `AMGT-rj-4` -- THE CROSSWALK AND THE UNION UNIVERSE -- one identity per security, and the coverage list joined with what Opal holds

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rj-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~19</issued_to>
<issued_by>2.0.0_SA_COO~W</issued_by>
<placeholders>NONE</placeholders>

**You are `0.9.0_WK_AMGT_RESAPP~19`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt (a sparse cone:
`.tools`, `org`, `docs`, `rcg`, `lib`, `infra`; `data/`, `portal/`, `workflows/` are deliberately absent -- if a path outside the
cone is genuinely needed, STOP and file a row; never `sparse-checkout disable`). Your first act prints `git rev-parse --abbrev-ref
HEAD` and tests that `org/`, `.tools/`, `lib/research/identity/` and `lib/opal_data_harvest/` exist; if any is absent, STOP with a
BLOCKING row. **YOU HOLD CHAIN B, a queue of THREE orders (`rj-4`, `rj-5`, `rj-10`); this is the first, and it is the ROUND'S FIRST
ACT: every other chain is spawned at this order's drain, because every cell resolves identities through what you build here.**
Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~19;`.

## 1. THE CELL, inlined in full -- `AMGT-rj-4` (C-ONE-IDENTITY, C-UNION-UNIVERSE, C-ETF-PLANE-READ; interfaces X-1 and U-1)

**THE CONTRACTS (PRD v0.8 @`1170b4da69`, ratified text, SIGNED):**
*C-ONE-IDENTITY: "ONE canonical security identity per economic security, resolved ONCE at the route boundary and carried unchanged
through overlay, thesis, peers, model, coverage, ranking and Posture. A VERSIONED, EXPLICIT crosswalk (`crosswalk/v1` in the pool)
maps that identity to its Bloomberg identifier (`BA US`), display ticker, model/pack key (`BA_US_Equity`) and every
publication-association key already persisted (`BA`, `security-<16 hex>`), carrying the source universe row and the identifier's
provenance. It preserves exchange and share-class distinctions; an unresolved vendor identifier stays UNRESOLVED and is never
guessed as US, never made by appending `US Equity` or stripping a suffix; a folder rename is not a new security; the five pilots
and the other 84 names sit in the same declared system; the full universe reports 89 input names and ONE disposition per name;
re-running the mapper or changing a display label mints no second record. Article bodies need no migration (they are keyed
`publisher:article_id`); the read adapter learns the legacy association aliases ... old links are preserved until the transition
is verified; no deletes."* Measured by `4.0.0_SA_CRO~W`: three conventions on one name (brief @`b90bfdd20d` -- READ IT FIRST).
*C-UNION-UNIVERSE: "the UNION of the coverage list (`universe.json`, 89 name folders; 32 tickers MEASURED / 57 UNRESOLVED at
2026-09-10) and the current holdings of the four Opal ETFs at the snapshot vintage."*
*C-ETF-PLANE-READ: "AMGT_RESAPP READS the ETF holdings plane `s3://opal-data-etfs` (`config/etf_universe.json`, `gold/book/`,
`gold/holding/`, `snapshots/snapshot_<date>.json` written daily at 22:00Z) and NEVER writes it ... the producer-side contract is
NOT established, the read is one-sided, the schema version is carried."*

**MEASURED AT THE CUT (06:3xZ, the issuer's read):** `snapshots/snapshot_2026-09-14.json` is 2,879 bytes -- a LIST of four ETF
header objects (`ticker DIVZ, name, nav, nav_as_of 2026-09-11, market_price, shares_outstanding, net_assets_reported ...`); the
HOLDINGS are NOT in it -- they live under `gold/holding/` (books under `gold/book/`), whose layout you MEASURE FIRST. The coverage
list: `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~4/universe.json` (89 names; the chatter producer reads 34
eligible Bloomberg tickers via `read_universe_tickers()`). The existing resolver `lib/research/identity/resolver.py` and builder
`build_universe.py`. The persisted association keys: list `publication-links/v1/` in `opal-data-harvest` with delimiter `/` (the
harvester's key form for BA, COST, HD), `packs/` (`BABA_US`, `BA_US`, `COST_US`, `NVDA_US_Equity`, `SAP_GY_Equity` at the cut --
two forms), and the model-block file names under `deliverables/0.9.0_WK_AMGT_RESAPP~1/` (`model_block_<key>.json`). The canonical
form is `<TICKER>_<CC>_Equity`.

**DELIVER, in this order:**
1. **Measure** the holdings plane (newest object per book DIVZ / IDVZ / PFDE / PFOE and its fields; the snapshot vintage), and the
   persisted association key forms (the three surfaces above), recording the denominators in your deliverables.
2. **The crosswalk.** `lib/research/identity/crosswalk.py`: a mapper CLI `python -m lib.research.identity.crosswalk --as-of <date>
   [--dry-run | --write-pool]` emitting `crosswalk/v1/<as_of>.json` (INTERFACE X-1) -- one record per canonical identity:
   `{security_key, bloomberg, display_ticker, model_key, association_keys: [...], exchange, share_class, source_row, provenance:
   {field: source}, resolution: MEASURED | UNRESOLVED, raw_identifier}`; UNRESOLVED records kept with their raw identifier and NO
   `security_key`; and a library API `resolve(any_form) -> {security_key, resolution, ...}` and `aliases(security_key) -> [keys]`
   that every other cell calls (the ONE resolver), reading the pool object (or `AMGT_CROSSWALK_PATH` for a local copy). A
   FIXED-POINT test: two runs on unchanged inputs produce byte-identical objects.
3. **The union universe.** Extend `build_universe.py` with `python -m lib.research.identity.build_universe --as-of <date> [--dry-run
   | --write-pool]` emitting `universe/v1/<as_of>.json` (INTERFACE U-1): `{as_of, snapshot_date, schema_version, coverage_source,
   holdings_source: {book: key}, names: [{security_key, ticker, name, source: coverage|holding|both, books, weight_by_book,
   resolution, resolution_reason, cik, filing_identity: {source: edgar|none, cik, form_expected: 10-K|20-F|none}}], denominators:
   {coverage, holdings_distinct, union, both, resolved, unresolved, with_cik}}` -- `cik` and `filing_identity` from the SEC
   ticker-to-CIK table (fetched once under the session egress word, cached in your deliverables with its retrieval time), through
   the crosswalk's identity; a holding identifier that does not resolve is UNRESOLVED with its raw identifier, never dropped,
   never guessed. Uploads follow the harvester's discipline: `put_object` with `Metadata {document-sha256, schema-version}`, then
   `head_object` read back and compared.
4. **Schemas** `crosswalk.schema.json` and `universe.schema.json` (`additionalProperties: false`) and unit tests over fixtures
   (coverage-only, holding-only, both, unresolved; the three association conventions on one name; the fixed point).
5. **The ETF plane is never written**: the object count and newest `LastModified` before and after are your control.

**BOUND:** READ-ONLY on `opal-data-etfs`; no new Bloomberg call; `universe.json` READ-ONLY (its owner is the list register,
FWD-14); no deletes anywhere; nothing deployed (`rj-10`).

## 2. WHERE THIS CAME FROM

**ROUND 11**, decomposition v1.3 s.19 @`73938cdae4` (re-pinned to PRD v0.8 at the issuance), on C-ONE-IDENTITY (the CRO's identity
brief @`b90bfdd20d`; row `Z-S95`), C-UNION-UNIVERSE and C-ETF-PLANE-READ (Andrew-direct ~05:1x-05:2xZ), and the CRO's connection
brief @`0f9a04e81e` seams 2 and 4 (the CIK field; the crosswalk). Readers of X-1: every cell; of U-1: rj-1, rj-5, rj-6, rj-7, rj-8,
rj-11, rj-13.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/identity/
lib/opal_data_harvest/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~4/universe.json
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/
org/tier1_exec/4.0.0_SA_CRO/deliverables/RESAPP_CONNECTION_BRIEF_IDENTITY_20260915_W.md
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rj-4.the-union-universe.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL** (RULING 1). `lib/opal_data_harvest/`, `universe.json`, the `~1` model blocks and the
  CRO's brief are READ-ONLY. Your `deliverables/0.9.0_WK_AMGT_RESAPP~19/` home needs no entry; keep the measurements, the dry-run
  objects and the CIK cache there.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~19 <0.9.0_WK_AMGT_RESAPP~19@opal.agent>" -F <msgfile>
  -- <paths>`, the message file written with the Write tool, ASCII only. Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

Egress: Andrew-direct ~05:42Z @`dfa63b6d92` ("The whole sitez fabric has free egress this session") -- the SEC ticker-to-CIK table
is inside it; record the fetch with its instrument and time. Secrets, if any, ONLY through `comp-secrets get <name> --reveal`. No
non-ASCII in anything that reaches AWS. **THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its
measurement and a row; never repaired, widened or satisfied by a route this order did not name. **SURPRISE ROWS:** *"a worker's row
is `AMGT_RESAPP-Z-W<n>-S<k>` with `<n>` its slot; `<k>` restarts at 1 per coordinate. `"project": "AMGT_RESAPP"` and `"fabric":
"site-z"` on every new row."* Your coordinate is `W19`; your first row is `AMGT_RESAPP-Z-W19-S1`; append by textual splice inside the
one fenced JSON array (never re-serialize it: other rows carry non-ASCII a re-serialization would rewrite); never edit an existing row.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rj-4"><invocation>.tools/aws s3api list-objects-v2 --bucket opal-data-etfs --prefix gold/ --query "[length(Contents), max_by(Contents,&LastModified).Key, max_by(Contents,&LastModified).LastModified]" --output text; .tools/aws s3api list-objects-v2 --bucket opal-data-etfs --prefix snapshots/ --query "sort_by(Contents,&Key)[-1].[Key,Size]" --output text; for b in DIVZ IDVZ PFDE PFOE; do printf "HOLDING %s: " "$b"; .tools/aws s3api list-objects-v2 --bucket opal-data-etfs --prefix "gold/holding/" --query "length(Contents[?contains(Key, '$b')])" --output text; done; .tools/aws s3api list-objects-v2 --bucket opal-data-harvest --prefix publication-links/v1/ --delimiter / --query "CommonPrefixes[].Prefix" --output text | tr "\t" "\n" | cat</invocation><expect>the BEFORE control on the ETF plane (a gold/ object count N, the newest key and its LastModified), the newest snapshot key and size, a per-book holding-object count at least 1 for each of DIVZ, IDVZ, PFDE, PFOE (a book with 0 is a row and its names are UNRESOLVED-SOURCE, not absent), and the harvester's association-key prefixes (at least three, carrying BA, COST and HD in the harvester's own form, recorded verbatim)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rj-4"><invocation>python -m lib.research.identity.crosswalk --as-of 2026-09-15 --dry-run > .scratch/rj4.crosswalk.json; echo rc=$?; python -m lib.research.identity.crosswalk --as-of 2026-09-15 --dry-run > .scratch/rj4.crosswalk.2.json; python -c "import json,io,hashlib; a=io.open('.scratch/rj4.crosswalk.json','rb').read(); b=io.open('.scratch/rj4.crosswalk.2.json','rb').read(); d=json.loads(a); r=d['records']; print('fixed-point', hashlib.sha256(a).hexdigest()==hashlib.sha256(b).hexdigest(), 'input-names', d['denominators'].get('input_names'), 'records', len(r), 'MEASURED', sum(1 for x in r if x['resolution']=='MEASURED'), 'UNRESOLVED', sum(1 for x in r if x['resolution']=='UNRESOLVED'), 'unresolved-with-key', sum(1 for x in r if x['resolution']=='UNRESOLVED' and x.get('security_key')), 'with-association-keys', sum(1 for x in r if x.get('association_keys')), 'conventions-seen', d['denominators'].get('association_conventions'))"</invocation><expect>rc=0; fixed-point True (two runs, identical bytes); input-names 89; records equal to input-names (ONE disposition per name); MEASURED plus UNRESOLVED equal to records; unresolved-with-key 0 (never guessed); with-association-keys at least 3 (BA, COST, HD carry the harvester's key); conventions-seen listing at least the three measured forms. A record count other than 89, or a guessed key, is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rj-4"><invocation>AMGT_CROSSWALK_PATH=".scratch/rj4.crosswalk.json" python -c "from lib.research.identity import crosswalk as x; import json; [print(repr(f), '->', json.dumps(x.resolve(f))[:160]) for f in ('BA US','BA_US_Equity','BA','SAP GY','SAP_GY_Equity','ZZZ NOPE','BABA_US')]; print('aliases BA', x.aliases('BA_US_Equity'))"</invocation><expect>BA US, BA_US_Equity and BA all resolve to security_key BA_US_Equity with resolution MEASURED and a provenance per field; SAP GY and SAP_GY_Equity resolve to SAP_GY_Equity (exchange GY preserved, never made US); ZZZ NOPE -> resolution UNRESOLVED with no security_key and the raw identifier echoed; BABA_US -> BABA_US_Equity (a pack-key form); aliases BA lists the harvester's association key(s) for Boeing. A guessed key for ZZZ NOPE, or SAP resolved to a US key, is NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rj-4"><invocation>AMGT_CROSSWALK_PATH=".scratch/rj4.crosswalk.json" python -m lib.research.identity.build_universe --as-of 2026-09-15 --dry-run > .scratch/rj4.universe.json; echo rc=$?; python -c "import json,io; d=json.load(io.open('.scratch/rj4.universe.json',encoding='utf-8')); n=d['names']; by={x.get('security_key'):x for x in n if x.get('security_key')}; print('snapshot_date', d.get('snapshot_date'), 'schema_version', d.get('schema_version'), 'denominators', json.dumps(d.get('denominators'))); print('names', len(n), 'coverage', sum(1 for x in n if x['source'] in ('coverage','both')), 'holding', sum(1 for x in n if x['source'] in ('holding','both')), 'both', sum(1 for x in n if x['source']=='both'), 'resolved', sum(1 for x in n if x['resolution']=='MEASURED'), 'unresolved', sum(1 for x in n if x['resolution']=='UNRESOLVED'), 'guessed', sum(1 for x in n if x['resolution']=='UNRESOLVED' and x.get('security_key')), 'with-cik', sum(1 for x in n if x.get('cik'))); [print(k, 'cik', by.get(k,{}).get('cik'), 'form', (by.get(k,{}).get('filing_identity') or {}).get('form_expected')) for k in ('BA_US_Equity','COST_US_Equity','HD_US_Equity','SAP_GY_Equity','BABA_US_Equity')]"</invocation><expect>rc=0; snapshot_date equal to the newest snapshot's date from AC1; schema_version 1; denominators printed; coverage 89; holding M at least 1; names equal to 89 plus M minus both; guessed 0; with-cik at least 5; BA_US_Equity, COST_US_Equity and HD_US_Equity with a cik and form 10-K; SAP_GY_Equity with a cik and form 20-F (a foreign private issuer on EDGAR); BABA_US_Equity with a cik and form 20-F. A coverage count other than 89, a guessed key, or a US 10-K expected for SAP is NOT met</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rj-4"><invocation>python -m unittest discover -s lib/research/identity/tests -p "test_*.py" -q 2>&1 | tail -3; python -c "import json,io,jsonschema; [jsonschema.validate(json.load(io.open(o,encoding='utf-8')), json.load(io.open(s,encoding='utf-8'))) or print('schema-valid', o.split('/')[-1], json.load(io.open(s,encoding='utf-8')).get('additionalProperties')) for o,s in (('.scratch/rj4.crosswalk.json','lib/research/identity/crosswalk.schema.json'),('.scratch/rj4.universe.json','lib/research/identity/universe.schema.json'))]"</invocation><expect>the suite ends OK with 0 failures and 0 errors (arms: coverage-only, holding-only, both, unresolved, the three conventions on one name, the fixed point); schema-valid for both objects with additionalProperties False. If jsonschema is not importable, record the ImportError verbatim and name the stdlib check you ran in a row -- never skip the validation silently</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rj-4"><invocation>python -m lib.research.identity.crosswalk --as-of 2026-09-15 --write-pool 2>&1 | tail -3; AMGT_CROSSWALK_PATH=".scratch/rj4.crosswalk.json" python -m lib.research.identity.build_universe --as-of 2026-09-15 --write-pool 2>&1 | tail -3; for k in crosswalk/v1/2026-09-15.json universe/v1/2026-09-15.json; do printf "%s " "$k"; .tools/aws s3api head-object --bucket opal-data-harvest --key "$k" --query "[ContentLength,Metadata.\"document-sha256\",Metadata.\"schema-version\"]" --output text; done; python -c "import hashlib,io; [print(f.split('/')[-1], 'local-sha256', hashlib.sha256(io.open(f,'rb').read()).hexdigest()) for f in ('.scratch/rj4.crosswalk.json','.scratch/rj4.universe.json')]"</invocation><expect>two OK: uploaded lines with read-back; both head-objects with a non-zero ContentLength, a document-sha256 EQUAL to the local sha256 of the same bytes, and schema-version 1. A missing document-sha256 or a mismatch is NOT met</expect></criterion>
  <criterion id="AC7" cell_refs="AMGT-rj-4"><invocation>.tools/aws s3api list-objects-v2 --bucket opal-data-etfs --prefix gold/ --query "[length(Contents), max_by(Contents,&LastModified).Key, max_by(Contents,&LastModified).LastModified]" --output text; .tools/aws s3api list-objects-v2 --bucket opal-data-etfs --prefix snapshots/ --query "[length(Contents), max_by(Contents,&LastModified).LastModified]" --output text; git log --format="%h %an %s" -3 -- lib/research/identity/ | cut -c1-140; python -c "import io,glob; fs=glob.glob('lib/research/identity/*.py'); print('files', len(fs), 'nonascii', sum(sum(1 for ch in io.open(f,encoding='utf-8').read() if ord(ch)>127) for f in fs), 'delete-sites', sum(io.open(f,encoding='utf-8').read().count('delete_object') for f in fs), 'etfs-writes', sum(io.open(f,encoding='utf-8').read().count('Bucket=\"opal-data-etfs\"') for f in fs if 'put_object' in io.open(f,encoding='utf-8').read()))"</invocation><expect>the AFTER control: the same gold/ count, newest key and LastModified as AC1 printed, and the snapshots/ count and newest LastModified unchanged (the ETF plane was read and never written -- any difference is a BLOCKING row); commits by this serial touching lib/research/identity/; nonascii 0; delete-sites 0; etfs-writes 0</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order. A rerun-able
criterion reads COMMITTED state where it grades history (`git log`), never a `git status` snapshot alone.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~19/AMGT_RESAPP.TO-AMGT-rj-4.the-union-universe.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json` (the checker compiles `expect` as a REGEX over the evidence; record a pattern that
matches the evidence), graded by YOUR WORKTREE'S OWN `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6,AC7`
(rc 0 is the verdict); keep the dry-run objects, the plane listings and the CIK cache beside it; flip `<status>` to `complete`; commit
with `--only -- <paths>`. Report once. **If a criterion cannot be met, leave the order OPEN and file a row.**

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>11</round>
<slot>~19</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<authority>PRD v0.8 @`1170b4da69` (ADMITTED: ratified-text half `3.0.0_SA_CVO~W` @`0e6592e88c`, brief half `4.0.0_SA_CRO~W` @`e1d8b2d643`) C-ONE-IDENTITY, C-UNION-UNIVERSE, C-ETF-PLANE-READ; the CRO's identity brief @`b90bfdd20d` and connection brief @`0f9a04e81e` (seams 2, 4); Andrew-direct ~05:1x-05:2xZ @`a4f9fd9568` (the union universe) and ~03:5xZ @`9dfee40ce0` (the fabric split); `1.0.0_SA_CTO~W`'s L10 round-10 analysis @`8d5fe78265` s.6; decomposition v1.3 s.19 @`73938cdae4` (cell rj-4, chain B first, the round's first act; interfaces X-1, U-1). Cell set: s.19a; fan-out: s.19e.</authority>

<preflight>
ALL RUN 2026-09-15 06:4xZ at this cut (decomposition v1.3 s.19g).
comp-schedule: RUN (--drift) -- 5 of 5 carriers within budget (16.0 s of 90); REACHED-DENOMINATORS C1=23, C2=8, C3=12, C4=21, C5=334; C2 = 8 OPEN deploy-ledger entries (none this project's; rj-10 opens one and closes it inside the round); C3 = 12 standing NEVER clauses (no monitor, no alarm); NO new scheduled producer is cut this round (every batch is a local Windows task DISABLED at creation, Andrew's box word @187f003998); BLIND on C4 and C5 in the tool's own voice.
comp-iam: RUN (gaps) -- 838 call(s) verdicted across 98 mapped role(s) over 474 .tf files; 629 UNRESOLVABLE-RESOURCE, 142 GRANTED, 51 GRANTED-BROAD (EXCLUDED, NOT CLEARED), 14 UNGRANTED, 2 GRANTED-ACTION / UNGRANTED-RESOURCE; 15 missing, 291 deny-present, 1 coverage-unknown, 2 resource-mismatch across 32 services; BLIND on 266 calls in 26 role-UNMAPPED services. The round's IAM delta lives in rj-10 alone: READ grants by prefix on opal-data-harvest for two roles, the DynamoDB articles grants REMOVED, no Scan, no wildcard resource; every other cell acts under the operator's own credentials and takes no AWS grant.
comp-adversary: RUN (compose on the decomposition, --no-packet) -- 48 commit pins, 13 repo paths, 17 file:line cites, 14 tool mentions; 23 hex runs not parsed (named); T11 NOT RESOLVED (293 uncited siblings, CAP 25 declared); stage 4 disabled by the caller. The round's adversarial surfaces: filing text, vendor responses and pool objects are DATA inside a model prompt (rj-6, rj-11 say so in the prompt; the verbatim gate runs against the PASSAGE; held-uncited claims never render); Posture is marked machine and read by no trade consumer; the Lusha response is scrubbed to name/title/link; the social job is capped in posts and USD.
comp-cache: DECLARED-NOT-APPLICABLE -- no portal surface in this cell.
comp-blast: DECLARED-NOT-APPLICABLE -- this cell moves nothing on the live plane: its writes are local code, tests and pool objects under the operator's credentials (a QA one-shot is not a production act); the round's one live move is rj-10's, covered by the co-sign.
</preflight>
