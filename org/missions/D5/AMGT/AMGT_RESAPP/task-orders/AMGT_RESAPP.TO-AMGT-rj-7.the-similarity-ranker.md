# AMGT_RESAPP task order -- `AMGT-rj-7` -- THE SIMILARITY RANKER -- a comparable set computed over one database, never copied from a workbook

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rj-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~21</issued_to>
<issued_by>2.0.0_SA_COO~W</issued_by>
<placeholders>NONE</placeholders>

**You are `0.9.0_WK_AMGT_RESAPP~21`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt (a sparse cone:
`.tools`, `org`, `docs`, `rcg`, `lib`; `data/`, `infra/`, `portal/`, `workflows/` are absent by design). Your first act prints
`git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and `lib/research/peers/` exist; if any is absent, STOP with a
BLOCKING row. **YOU HOLD CHAIN D, ONE order, spawned after `rj-4`'s drain: the crosswalk `lib/research/identity/crosswalk.py` (X-1) and the union universe `universe/v1/<as_of>.json` (U-1) exist when you start, and every identity in your objects is resolved through X-1.** Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~21;`.

## 1. THE CELL, inlined in full -- `AMGT-rj-7` (FWD-8; C-SIMILARITY-RANKER; FWD-19's comparable; interface R-1)

**THE CONTRACT (PRD v0.8 @`1170b4da69`, ratified text, SIGNED), verbatim in its rule:** *"The comparable set of a subject is computed, never
copied from a workbook (the F6 defect), by ONE ranker over ONE database: the database = the Security Scanner's universe data
(`UniverseDataRow`: ticker, name, mktVal, country, sector, industryGroup, universe weight for sp500 / r1000 / r1000v / acwx / eafe /
eafev) UNION the harvest universe's model-block header scalars (classification, market cap, country); the rungs, lexicographic, in
Andrew's order: same SECTOR, then a SIZE BAND (the existing engine's 0.2x-5x market-cap band), then same COUNTRY, then same
SUBSECTOR (industry group); a numeric similarity within the last rung breaks ties (log market-cap distance); the four postulates:
(i) MECE over the database -- every candidate is in exactly one rung or excluded, written as the database MINUS the excluded, with
the denominator printed; (ii) same grain -- one security per row, one classification field named in every emitted set's `test`
string; (iii) one intent -- similarity of business and scale, never valuation; (iv) state coherence -- the set carries `basis` =
analyst | derived | absent as the engine already does, and a Seeking Alpha comparables list, if its API exposes one, is an INPUT
candidate measured first, never the rule."*

**THE SEAM (06:1x-06:3xZ):** `lib/research/peers/engine.py` (222 lines): `CLASSIFICATION_MNEMONIC = "GICS_SECTOR_NAME"` (the finest
field the landed model blocks carry), `MARKET_CAP_MNEMONIC = "CUR_MKT_CAP"`, `MARKET_CAP_BAND_LOW = 0.2`, `MARKET_CAP_BAND_HIGH = 5.0`
(`:55-58`); `BASES = ("analyst","derived","absent")` (`:60`); `peers(...)` `:118-215` -- `analyst_override` => `analyst`; missing
classification or cap => `absent`; **`:176-184 if not candidate_universe: => absent` with the reason "candidate universe not
classified" -- every real name reads `absent` today because no candidate universe was ever loaded**; the derived path `:191-213` is
complete and unfed. Subject read: `MODEL_BLOCK_DIR_DEFAULT` = `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1`
(no new Bloomberg call). Tests `lib/research/peers/tests/test_peers.py`; `shared_defect.py`; `lib/research/rules/peer.py`. The
scanner's universe files: `s3://opal-data-portal-v2/json/security_scanner/latest/universes/{sp500,r1000,r1000v,acwx,eafe,eafev}/
universe_data.json` -- `{asOf: "2026-08-06", universeId, sourceUniverseColumn, securities: [{ticker, name, mktVal, country, sector,
industryGroup, universeWeight, divzWeight, price, values: {284 factor codes}}]}`; sp500 is 3.7 MB, acwx 12.4 MB; **asOf 2026-08-06 is a
VINTAGE the set must carry** (six weeks old at this cut). The route: `scoped_amgt.py:850-857 read_peer_set` reads
`peer_set_{key}.json` from `AMGT_PEER_SET_ROOT` (default the `~4` deliverables) and synthesizes `absent` on a miss. Adam's `CSC` sheet
(card 3 @`5007337353`): per peer Price, Shares, Debt, Preferred, Minority, Cash, Market Cap, EV, P/E x3, leverage ratios, five-year
growth of Revenue / EBIT / FCF, with Average / Median / Min / Max rows.

**DELIVER, in this order:**
1. `lib/research/peers/universe.py`: the loader over the six scanner files (boto3 GetObject, cached under your deliverables as the
   read vintage) UNION the harvest model-block headers, ONE candidate per ticker (a ticker in several universes is one row carrying
   every universe weight), the vintage `asOf` carried on the loaded set; the denominator printed (per file, union, duplicates folded).
2. `engine.py`: rungs three (`country`) and four (`industryGroup`) after the existing two, lexicographic; a log-market-cap distance
   tiebreak inside the last rung reached; `test` strings naming the field per rung; the emitted set carries `rung_reached` per member,
   `denominators` per rung (database MINUS excluded), `universe_vintage`, `basis` (analyst | derived | absent as before). The subject's
   own sector/country/industry group come from the model block header when present, else from the scanner row for its ticker, else
   `absent` with the reason.
3. A batch CLI `python -m lib.research.peers.engine --as-of <date> --write-pool` over the union universe (U-1 `universe/v1/<as_of>.json`
   from the pool; the `universe.json` fallback) writing `peers/v1/{security_key}/{as_of}.json` (INTERFACE R-1) for every resolved
   name -- an `absent` object with its reason for a name without classification, never a skipped name; the five QA names of 19e
   (BA_US_Equity, COST_US_Equity, HD_US_Equity, SAP_GY_Equity, BABA_US_Equity) and up to two more the issuer names in your spawn
   prompt are printed individually in the batch summary -- and a `--dry-run` for one
   `--security-key`; uploads with `Metadata {document-sha256, schema-version}` and read-back.
4. `csc_columns`: in every R-1 object, the CSC columns mapped to scanner factor codes where one exists (name the code) and listed
   under `absent` where none does -- the Rule 24 subtraction, printed, never a forward list.
5. **The Seeking Alpha input candidate, MEASURED once:** read `lib/opal_data_harvest/` for an SA endpoint that returns comparables;
   if one exists and is reachable under this session's egress WITHOUT the CRO's session vault, call it ONCE for BA and record the
   list beside R-1 as `sa_candidates` (an input, never the rule); if it needs the vault, record `ABSENT-ACCESS` and stop there.
6. Tests: the four rungs on a fixture universe, the tiebreak, the MECE denominator (rung counts sum to the database), the
   `absent` arms.

**BOUND:** no new Bloomberg call; no portal edit (the Peers tab's table is `rj-9`'s over R-1); no deploy; the route
(`scoped_amgt.py`) is chain A's -- your interface is the pool object.

## 2. WHERE THIS CAME FROM

**ROUND 11**, decomposition v1.3 s.19 @`73938cdae4`, on the voice memo ~05:5xZ part three ("a similarity function to generate those
peers from some database"), the fifth page word (Adam's `CSC` multiples; the Security Scanner's ranking material), card 3, and the
analysis @`8d5fe78265` s.6 item 4. Readers of R-1: rj-9, rj-11.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/peers/
lib/research/identity/
lib/opal_data_harvest/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~4/universe.json
org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_RESAPP_SUBSTRATE_MEASUREMENTS_20260915_W/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rj-7.the-similarity-ranker.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL** (RULING 1). `lib/research/identity/`, `lib/opal_data_harvest/`, the `~1` model
  blocks, `universe.json` and the CTO's cards are READ-ONLY.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~21 <0.9.0_WK_AMGT_RESAPP~21@opal.agent>" -F <msgfile>
  -- <paths>`, message file by the Write tool, ASCII only. Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

Egress @`dfa63b6d92` (Opal's own S3; one optional SA read as stated). Secrets ONLY through `comp-secrets`. No non-ASCII in anything
that reaches AWS. **THE REFUSAL CLAUSE** and **SURPRISE ROWS** as in the other orders; your coordinate is `W21`; your first row is
`AMGT_RESAPP-Z-W21-S1`; append by textual splice; never edit an existing row.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rj-7"><invocation>timeout 115 python -c "from lib.research.peers import universe as u; c=u.load_candidate_universe(); print('vintage', c.get('vintage'), 'per-file', c.get('denominators'), 'candidates', len(c.get('rows') or []), 'with-sector', sum(1 for r in c['rows'] if r.get('sector')), 'with-industryGroup', sum(1 for r in c['rows'] if r.get('industryGroup')), 'with-country', sum(1 for r in c['rows'] if r.get('country')), 'with-mktVal', sum(1 for r in c['rows'] if r.get('mktVal')))"</invocation><expect>vintage 2026-08-06 (or the asOf the files carry at your read, printed), per-file denominators for six files plus the model-block headers, candidates at least 2000 (the six universes folded to one row per ticker), with-sector, with-industryGroup, with-country and with-mktVal each at least 90 percent of candidates. A loader that reads fewer than six files without naming which failed is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rj-7"><invocation>python -m lib.research.peers.engine --security-key BABA_US_Equity --as-of 2026-09-15 --dry-run 2>&1 | tail -16</invocation><expect>a set with basis derived, members N at least 5 and at most 25, EVERY member with the subject's sector, a market cap inside 0.2x-5x of the subject's, rung_reached printed per member, denominators per rung (sector, band, country, industryGroup) whose excluded plus retained equals the database at each rung, universe_vintage printed, csc_columns listing present codes and absent columns. A member outside the sector or the band, or a rung without its denominator, is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rj-7"><invocation>python -m lib.research.peers.engine --security-key ZZZ_NOPE_US_Equity --as-of 2026-09-15 --dry-run 2>&1 | tail -4; python -m unittest lib.research.peers.tests.test_peers -q 2>&1 | tail -3</invocation><expect>basis absent with a reason naming the missing classification (the control: an unknown subject produces an absent set, never an empty derived one); the suite ends OK with 0 failures and 0 errors and covers the four rungs, the tiebreak, the MECE sum and the absent arms</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rj-7"><invocation>timeout 115 python -m lib.research.peers.engine --as-of 2026-09-15 --write-pool 2>&1 | tail -6; .tools/aws s3api list-objects-v2 --bucket opal-data-harvest --prefix peers/v1/ --query "length(Contents)" --output text</invocation><expect>a batch summary: names N from the universe object, derived D, absent A with D plus A equal to N, uploaded N with read-back; the pool's peers/v1 object count at least N. A skipped name (N greater than uploaded) is NOT met; a batch over 115 s is split by --limit and --offset flags the worker adds and names in a row, never truncated</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rj-7"><invocation>.tools/aws s3api get-object --bucket opal-data-harvest --key peers/v1/BABA_US_Equity/2026-09-15.json .scratch/rj7.baba.json --query "[ContentLength,Metadata]" --output json; python -c "import json,io; d=json.load(io.open('.scratch/rj7.baba.json',encoding='utf-8')); print('basis', d['basis'], 'members', len(d['members']), 'vintage', d.get('universe_vintage'), 'sa_candidates', (d.get('sa_candidates') or {}).get('status') if isinstance(d.get('sa_candidates'), dict) else ('LIST' if d.get('sa_candidates') else 'ABSENT'), 'csc-present', len((d.get('csc_columns') or {}).get('present') or []), 'csc-absent', len((d.get('csc_columns') or {}).get('absent') or []))"</invocation><expect>Metadata with document-sha256 and schema-version 1; basis derived; members equal to AC2's N; vintage printed; sa_candidates LIST, ABSENT-ACCESS or ABSENT (measured and recorded, never the rule); csc-present plus csc-absent equal to the CSC column count you enumerated (at least 15). A CSC map that lists only the present columns is NOT met (the absent half is the subtraction)</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rj-7"><invocation>git log --format="%h %an %s" -4 -- lib/research/peers/ | cut -c1-140; python -c "import io,glob; fs=glob.glob('lib/research/peers/*.py'); print('files', len(fs), 'nonascii', sum(sum(1 for ch in io.open(f,encoding='utf-8').read() if ord(ch)>127) for f in fs), 'bloomberg-calls', sum(io.open(f,encoding='utf-8').read().count('blpapi') + io.open(f,encoding='utf-8').read().count('bloomberg_reference_data') for f in fs))"</invocation><expect>commits by this serial touching lib/research/peers/; nonascii 0; bloomberg-calls 0 (no new Bloomberg call; F2/G-24). A Bloomberg call in the ranker is NOT met</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~21/AMGT_RESAPP.TO-AMGT-rj-7.the-similarity-ranker.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json` (the checker compiles `expect` as a REGEX over the evidence), graded by YOUR WORKTREE'S
OWN `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6` (rc 0 is the verdict); keep the batch summary and the
BABA dry-run beside it; flip `<status>` to `complete`; commit with `--only -- <paths>`. Report once. **If a criterion cannot be met,
leave the order OPEN and file a row.**

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>11</round>
<slot>~21</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<authority>PRD v0.8 @`1170b4da69` (ADMITTED) C-SIMILARITY-RANKER and FWD-8 (the voice memo ~05:5xZ @`fbd5d91431` part three; the fifth page word @`473526f738`; card 3 @`5007337353`; row F6 -- 48 of 54 stale peer sets), the round-4 engine (AMGT-s-8), `1.0.0_SA_CTO~W`'s L10 round-10 analysis @`8d5fe78265` s.6 item 4, decomposition v1.3 s.19 @`73938cdae4` (cell rj-7, chain D, interface R-1). Cell set: s.19a; fan-out: s.19e.</authority>

<preflight>
ALL RUN 2026-09-15 06:4xZ at this cut (decomposition v1.3 s.19g).
comp-schedule: RUN (--drift) -- 5 of 5 carriers within budget (16.0 s of 90); REACHED-DENOMINATORS C1=23, C2=8, C3=12, C4=21, C5=334; C2 = 8 OPEN deploy-ledger entries (none this project's; rj-10 opens one and closes it inside the round); C3 = 12 standing NEVER clauses (no monitor, no alarm); NO new scheduled producer is cut this round (every batch is a local Windows task DISABLED at creation, Andrew's box word @187f003998); BLIND on C4 and C5 in the tool's own voice.
comp-iam: RUN (gaps) -- 838 call(s) verdicted across 98 mapped role(s) over 474 .tf files; 629 UNRESOLVABLE-RESOURCE, 142 GRANTED, 51 GRANTED-BROAD (EXCLUDED, NOT CLEARED), 14 UNGRANTED, 2 GRANTED-ACTION / UNGRANTED-RESOURCE; 15 missing, 291 deny-present, 1 coverage-unknown, 2 resource-mismatch across 32 services; BLIND on 266 calls in 26 role-UNMAPPED services. The round's IAM delta lives in rj-10 alone: READ grants by prefix on opal-data-harvest for two roles, the DynamoDB articles grants REMOVED, no Scan, no wildcard resource; every other cell acts under the operator's own credentials and takes no AWS grant.
comp-adversary: RUN (compose on the decomposition, --no-packet) -- 48 commit pins, 13 repo paths, 17 file:line cites, 14 tool mentions; 23 hex runs not parsed (named); T11 NOT RESOLVED (293 uncited siblings, CAP 25 declared); stage 4 disabled by the caller. The round's adversarial surfaces: filing text, vendor responses and pool objects are DATA inside a model prompt (rj-6, rj-11 say so in the prompt; the verbatim gate runs against the PASSAGE; held-uncited claims never render); Posture is marked machine and read by no trade consumer; the Lusha response is scrubbed to name/title/link; the social job is capped in posts and USD.
comp-cache: DECLARED-NOT-APPLICABLE -- no portal surface in this cell.
comp-blast: DECLARED-NOT-APPLICABLE -- this cell moves nothing on the live plane: its writes are local code, tests and pool objects under the operator's credentials (a QA one-shot is not a production act); the round's one live move is rj-10's, covered by the co-sign.
</preflight>
