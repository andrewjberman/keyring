# AMGT_RESAPP task order -- `AMGT-rk-32` -- battery step 1 reads the LIVE SEC ticker table with the existing name guard; a miss is reported against the table actually read

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-32</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~36</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence; the standing
  collection-stays-off / no-monitor moratorium is unaffected; the landing is idempotent per UTC day by
  put-if-absent, not by any schedule, and nothing polls.
comp-iam: DECLARED-NOT-APPLICABLE -- this order writes only to the bronze prefix `AMGT-rk-33` already
  established and wrote in s3://opal-data-harvest (sec/harvest/bronze/company_tickers/; registry-gated, see the issuer amendment) at the builder's address,
  under the device's existing credentials; it grants no permission, provisions no resource and touches no
  Terraform.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~36`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/`,
`lib/research/identity/build_universe.py` and `lib/opal_naming.py` exist; if any is absent, STOP with a
BLOCKING row. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~36;`. **NEVER RUN AN
INSTALL.** **YOU ARE STEP 2 OF A TWO-STEP SEQUENTIAL QUEUE ON `lib/research/identity/build_universe.py`:**
`AMGT-rk-33` (chain H, slot ~37) edits the same file BEFORE you and establishes the pool home you read. Your
SECOND act is AC1 -- it verifies that rk-33 landed (no `~19` literal in the file, `sec_table_address()` and
`sec_table_prefix()` present, the pool object present). **If AC1 fails, STOP: file a row naming what is absent
and report; do not build against the worker folder and do not re-do rk-33's work.**

## 1. THE CELL, inlined in full -- `AMGT-rk-32` (R14-I2; FWD-18, V2/D1; co-sign NO)

**The analysis row, verbatim (ROUND_ANALYSIS.round13.md s.4 @9c8e04cd9a, :122):** battery step 1 reads the
LIVE SEC ticker table with the existing name guard; a miss is reported against the table actually read.

**THE MEASURED DEFECT (code @075227f4c0 before rk-33; the validation @b527b93214).** Battery step 1 IS
`filing_identity_for()` (`build_universe.py:491-539`): it joins the canonical ROOT (:487-488, :502) against
`sec_cache["rows"]` (:503) -- a 33-root PROJECTION of the SEC table (`sec_ticker_cik_cache.json:15-20`: 33
probed, 15 present, 18 absent) -- and on a miss reports "the SEC ticker-to-CIK table (%s rows, retrieved %s)
carries no ticker %r" using the DELIVERY's `row_denominator` 10,422 (:505-507, :12), so a projection miss reads
as absence from the full table. Validation D1 (:174-176) and s.7 item 2 (:266-268): Caterpillar is MISSED by
the estate ("table (10422 rows) carries no ticker 'CAT'" is FALSE, :96) while the LIVE table (10,438 rows on
2026-09-18) resolves CAT to SEC ID 18230 (:97) and, with the existing name guard, correctly REFUSES CSL as
Carlisle (:108; the guard :509-517, described in the module's own docstring :433-437) and misses Keyence
honestly (:121). PRD v0.13 s.10's evidence list carries the same D1 (:1669-1671). Downstream,
`fetch.py:377-388` reads the CIK from the universe row this function writes, so a false miss here is a name
the whole battery never sees.

**WHAT `AMGT-rk-33` LEAVES YOU (read it, do not rebuild it):** `sec_table_address(partition_date, object_name)`
-> the builder's address (`s3://opal-data-harvest/sec/harvest/bronze/company_tickers/date=<YYYY-MM-DD>/<object>`,
`lib/opal_naming.py address()` :1558-1571 with the `sec` VENDOR row); `sec_table_prefix()` -> (bucket,
key_prefix); the 2026-09-15 projection landed at `.../date=2026-09-15/sec_ticker_cik_cache.json` (its
`submissions.by_cik` block, 15 CIKs, :188-192, is still what `form_expected` reads at :518-520);
`load_sec_cache(path=None)` reading the newest partition's `sec_ticker_cik_cache.json` and returning the
existing document shape plus `ticker_to_cik_table.object`; `AMGT_SEC_CACHE_PATH` (:454) and `--sec-cache-path`
(:929) as the LOCAL override for tests; `SEC_CACHE_DEFAULT` gone.

**RULED -- what you build.**
1. **The LIVE table is landed BEFORE it is read (`C-RAW-BEFORE-DERIVED`, PRD :899).** A new
   `fetch_sec_ticker_table(date_utc)` GETs `https://www.sec.gov/files/company_tickers.json` ONCE with the
   estate's own instrument (`urllib.request`, the User-Agent exactly as `sec_ticker_cik_cache.json:3` records
   it), and lands the bytes BYTE-FOR-BYTE at `sec_table_address(date_utc, "company_tickers.json")` with
   put-if-absent and head read-back (`document-sha256` metadata; the `crosswalk.write_pool()` discipline,
   :609-657, takes a bucket). Idempotent per UTC day: if that day's object exists, NO GET is made and the
   line prints `GET performed=no ... already-current`. The CLI flag is
   `python -m lib.research.identity.build_universe --refresh-sec-table` (a new, standalone mode beside the two
   at :906-919); it prints ONE line: `SEC TABLE: GET performed=<yes|no> url=... rows=<N> sha256=... landed=<address>
   readback=OK address_builder=lib/opal_naming.py`. **`--dry-run` (:854-860, :931) makes NO GET and lands
   nothing:** it reads the newest landed table, and if none exists it refuses loudly naming the address it
   expected (never a fallback to any repo path, never a silent empty table).
2. **`load_sec_cache()` returns the FULL table.** `rows` = every row of the newest landed `company_tickers.json`
   keyed by `ticker.upper()` as `{present: True, cik: <int>, title: <str>}` (the file's own `cik_str`, `ticker`,
   `title` fields); `ticker_to_cik_table` = `{url, row_denominator: len(rows) AS READ, retrieved_at: the landed
   object's partition date and LastModified, sha256: of the bytes read, object: the address}`; `submissions` =
   carried from the newest `sec_ticker_cik_cache.json` (rk-33's object) when present, else `{}` with the
   loader saying so. The document SHAPE `filing_identity_for()` reads is unchanged, so its fixture arms
   (`test_union_universe.py:30`, :163-195) still pass as written.
3. **`filing_identity_for()` (:491-539): the guard STAYS, the miss becomes TRUE.** The name-agreement guard
   (:509-517, `_significant_tokens` :470-475 over `_CORPORATE_TOKENS` :460-467) is NOT loosened, not widened, not
   moved. The miss message (:505-507) keeps its `(%s rows, retrieved %s)` phrase (AC5 parses it) and NAMES the
   object read (`ticker_to_cik_table.object`); its numbers are the table ACTUALLY READ (AC5's fixture control
   proves the denominator is not typed). A hit on a US listing joins as today (:527); a hit on a non-US
   listing still runs the guard (CSL -> Carlisle REFUSED, AC4). `form_expected` for a CIK the `submissions`
   block does not carry reads `none` with the note saying "no EDGAR submissions measurement for CIK <n> in
   <object>" -- measuring forms from EDGAR is chain F's (`R14-F1`), NOT yours: no `data.sec.gov` request.
4. **The union's `--dry-run` writes nothing, anywhere** (rk-33's AC covers the whole; yours proves step 1's read
   is a read, AC6).
5. **Tests:** `test_union_universe.py` gains arms for the loader's shaping of a 3-row fixture table (the
   denominator control), the loud refusal when no landed table exists, and the miss note naming the object.

## 2. WHERE THIS CAME FROM

**ROUND 14**, decomposition s.21c (round-14 block), on `1.0.0_SA_CTO~Z`'s L10 round-13 analysis s.2 (:55-61),
s.4 row R14-I2 (:122) @`9c8e04cd9a`; PRD v0.13 @`1699960261` s.10 (:1608-1685): the stage row "universe row +
filing identity" :1623, `C-PRODUCTION-HOME` :1643-1650 (the SEC cache instance :1649), `C-VALIDATION-NAMES`
:1652-1658, the s.10 evidence list's D1 :1669-1671; `C-FILINGS-ANALYZER`'s ratified US battery order (EDGAR
first, :665) -- the SEC's `company_tickers.json` is the public table that order's step 1 reads;
`C-RAW-BEFORE-DERIVED` :899; the validation @`b527b93214` :96-97, :107-108, :121, :174-176, :266-268.

**ISSUER AMENDMENT -- THE REGISTRY GATE (`2.0.0_SA_COO~Z`, 2026-09-18 ~21:3xZ, on Andrew's words relayed by
`1.0.0_SA_CTO~Z` msg 23778):** Andrew, VERBATIM: *"Yeah i hope its clear and foundational in all associated AMGT_RESAPP art
that the opal-data-harvest bucket is the designated folder for all RESAPP data content/pipelines"* and *"then it has to be
structured in said bucket in proper form"*. So: EVERY AMGT_RESAPP byte this order lands -- bronze raw included -- lands in
`opal-data-harvest`, at an address PRINTED BY `lib/opal_naming.py address()`, never typed. MEASURED at the cut: the registry
(`infra/logic/registry/tiers.json:27`) still homes bronze/silver in the shared `opal-data-assets`; the two registry rows that
re-home this project (the home registration + the R20 departure entry) are being placed by `0.0.0_AB_MSTR~Z` on the laptop
fabric and land here by merge. THE RULE, replacing every literal bucket in this order: before ANY live write at a builder
address, print the builder's output for the address the order names with the scope token `harvest` (the L4 RULING,
`1.0.0_SA_CTO~Z` @2560e04f46: vendor bronze is `<vendor>/harvest/bronze/<table>/<partition>/<object>`, our own derivations
`amgt/harvest/<tier>/<table>/...`; NO `global` route and NO `amgt` scope row -- a scope spelled `amgt` is refused by the
builder, and `global` is not this project's route; where this order's older text says `global`, read `harvest`); the naming gate at commit is ENFORCING and its grader is WIDER than the builder, so a
hand-typed key can pass the commit and resolve nowhere -- never type one); the live
arm is LIVE iff that address's bucket is `opal-data-harvest`. If the builder REFUSES or returns any other bucket, DO NOT
WRITE THERE: the offline, read-only and dry-run criteria run in full; each live criterion is recorded with the builder's
printed line as its output and the verdict REFUSED-BY-REGISTRY; ONE surprise row carries it (`spec_asserts`: Andrew's words
above and CTO msg 23778; `world_is`: the builder's exact output at spawn), and the worker keeps working. A write to
`opal-data-assets` of any AMGT_RESAPP object is NOT AUTHORIZED by this order under any branch. Where this order's text below
reads `s3://opal-data-harvest/...` for a builder address, that is the EXPECTED bucket once the rows land, and the address is
still read from the builder's print, never from this text.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/identity/build_universe.py
lib/research/identity/tests/test_union_universe.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~36/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-32.step-one-live-sec-table.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant (`lib/opal_naming.py`, `crosswalk.py`,
  `fetch.py`, the pool objects rk-33 landed). Scratch is `<your worktree>/.scratch/` only.
- **NOT your write:** `sec_table_address()`/`sec_table_prefix()`/the loader's pool plumbing rk-33 built (extend
  the loader's RETURN, do not re-home it); `fetch.py` and `batch.py` (chain F); `crosswalk.py` (rk-31); the
  registry (rk-33's row is in; you add none).
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~36 <0.9.0_WK_AMGT_RESAPP~36@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by a NON-SHELL writer). Every `.py` passes `.tools/commit-gate.sh`. Never push, merge,
  rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

PORTAL FROZEN (not your surface). **COLLECTION STAYS OFF.** **NO alarm, monitor, SNS/SES-send, notification or
freshness checker.** Secrets through `comp-secrets` only. No non-ASCII in anything you write. **PUSH: never.**
LD-0522 puts the push with `0.0.0_AB_MSTR~Z`.
**EGRESS -- the ceiling is NAMED:** exactly the ONE GET the cell text names, `https://www.sec.gov/files/company_tickers.json`
(a public SEC file, not a vendor API; the ratified US battery order reads EDGAR first, PRD :665; the estate
fetched this same file on 2026-09-15 under the instrument recorded at `sec_ticker_cik_cache.json:3`), at most
ONCE per UTC day by construction (put-if-absent). NO `data.sec.gov` submissions request (chain F's), NO
Bloomberg, NO other vendor, NO web. If the spawn prompt says the COO wants a per-use word on this GET before it
fires, AC2 waits for that word and AC1/AC3-AC7 run against rk-33's landed object only -- say so in the report.
**NO FLEET RUN, NO RE-RUN:** `--write-pool` of the union is never run by this order; the validation names are
exercised through `filing_identity_for()` directly (AC3-AC5), never by rebuilding `universe/v1`.
**POOL WRITES:** `sec/harvest/bronze/company_tickers/date=<today>/company_tickers.json` in `opal-data-harvest` (registry-gated, see the issuer amendment) --
nothing else.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row;
never repaired, widened, or satisfied by a route this order did not name.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- the live table's row count
(10,438 on 2026-09-18, validation :97) is re-measured by the landing itself.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W36-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never
re-serialize it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-32"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3
src = open('lib/research/identity/build_universe.py', encoding='utf-8').read().split('\n')
print('tilde19_literals', [i + 1 for i, l in enumerate(src) if '0.9.0_WK_AMGT_RESAPP~19' in l], 'SEC_CACHE_DEFAULT', any('SEC_CACHE_DEFAULT' in l for l in src))
from lib.research.identity import build_universe as bu
print('interface', hasattr(bu, 'sec_table_address'), hasattr(bu, 'sec_table_prefix'), hasattr(bu, 'load_sec_cache'))
addr = bu.sec_table_address('2026-09-15', 'sec_ticker_cik_cache.json'); bucket, key = addr[5:].split('/', 1)
head = boto3.client('s3', region_name='us-east-1').head_object(Bucket=bucket, Key=key)
print('rk33_object', addr, 'ContentLength', head['ContentLength'], 'sha', (head.get('Metadata') or {}).get('document-sha256', 'NONE')[:16])
print('prefix', bu.sec_table_prefix())
"</invocation><expect>THE PRECONDITION (rk-33 landed): tilde19_literals [] and SEC_CACHE_DEFAULT False; interface True True True; rk-33's object present at the builder's address with its document-sha256 metadata; the prefix printed. Any other reading STOPS this order with a row naming what is absent -- nothing below is attempted against a worker folder</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-32"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.identity.build_universe --refresh-sec-table 2>&1 | tail -3 && python -m lib.research.identity.build_universe --refresh-sec-table 2>&1 | tail -2</invocation><expect>the first run prints ONE line `SEC TABLE: GET performed=yes url=https://www.sec.gov/files/company_tickers.json rows=N sha256=... landed=s3://opal-data-harvest/sec/harvest/bronze/company_tickers/date=<today UTC>/company_tickers.json readback=OK address_builder=lib/opal_naming.py` with N >= 10000 (10,438 on 2026-09-18 -- print whatever is live) and the address printed BY the builder; the second run, the same UTC day, prints `GET performed=no` and `already-current` with the same sha256 -- ONE GET per day by construction, and the landed bytes are the delivery byte-for-byte</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-32"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
from lib.research.identity import build_universe as bu
cache = bu.load_sec_cache(); t = cache['ticker_to_cik_table']
print('object', t.get('object'), 'rows_read', t.get('row_denominator'), 'retrieved_at', t.get('retrieved_at'), 'sha', str(t.get('sha256'))[:16])
print('rows_in_document', len(cache.get('rows') or {}), 'submissions_ciks', len((cache.get('submissions') or {}).get('by_cik') or {}))
cik, ident, note = bu.filing_identity_for('CAT_US_Equity', 'US', 'Caterpillar Inc', cache)
print('CAT cik', cik, ident); print(note[:400])
"</invocation><expect>rows_read == rows_in_document >= 10000 (the FULL table, not 33) with the object named; CAT cik 18230 and ident.source 'edgar' (the validation's live-table result, :97); form_expected reads 'none' with the note naming the missing submissions measurement for CIK 18230 in the object, or a measured form if the submissions block carries it -- either way the note says which, and this order made no data.sec.gov request; submissions_ciks 15 (rk-33's carried block)</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-32"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
from lib.research.identity import build_universe as bu
cache = bu.load_sec_cache()
cik, ident, note = bu.filing_identity_for('CSL_AU_Equity', 'AU', 'CSL Ltd', cache)
print('CSL cik', cik, 'source', ident['source']); print(note[:500])
cik2, ident2, note2 = bu.filing_identity_for('BA_US_Equity', 'US', 'Boeing BA', cache)
print('BA cik', cik2, 'source', ident2['source'], 'form', ident2['form_expected'])
"</invocation><expect>THE STANDING NEGATIVE CONTROL: CSL cik None, source 'none', the note beginning REFUSED COLLISION and naming Carlisle (CIK 790051, validation :108) -- the existing guard (:509-517) unchanged and exercised on a non-US listing whose ticker collides on the live table; and the positive control BA cik 12927, source 'edgar', form '10-K' (from rk-33's carried submissions block, sec_ticker_cik_cache.json:193-204) -- the join for a US listing is unchanged</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-32"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import re
from lib.research.identity import build_universe as bu
cache = bu.load_sec_cache()
cik, ident, note = bu.filing_identity_for('6861_JP_Equity', 'JP', 'Keyence Corp', cache); print('KEYENCE', cik, note[:400])
fixture = {'ticker_to_cik_table': {'row_denominator': 3, 'retrieved_at': 'fixture', 'object': 'fixture://3rows'}, 'rows': {'AAA': {'present': True, 'cik': 1, 'title': 'AAA CORP'}, 'BBB': {'present': True, 'cik': 2, 'title': 'BBB CORP'}, 'CCC': {'present': True, 'cik': 3, 'title': 'CCC CORP'}}, 'submissions': {'by_cik': {}}}
cik2, ident2, note2 = bu.filing_identity_for('CAT_US_Equity', 'US', 'Caterpillar Inc', fixture); print('CONTROL', cik2, note2[:300])
n_live = int(re.search(r'\((\d+) rows', note).group(1)); n_fix = int(re.search(r'\((\d+) rows', note2).group(1))
print('live_denominator', n_live, 'fixture_denominator', n_fix, 'denominator_is_the_table_read', n_live == cache['ticker_to_cik_table']['row_denominator'] and n_fix == 3)
"</invocation><expect>THE HONEST MISS: KEYENCE cik None with a note reading "the SEC ticker-to-CIK table (N rows, retrieved ...) carries no ticker '6861'" AND naming the object read (fixture://... vs s3://...); CONTROL: the same call over a 3-row fixture reports "(3 rows" for CAT -- denominator_is_the_table_read True: the number in the miss is the table ACTUALLY READ, never a typed 10422 (the D1 defect was a 33-row projection reporting the delivery's count)</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-32"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3
from lib.research.identity import build_universe as bu
s3 = boto3.client('s3', region_name='us-east-1')
bucket, prefix = bu.sec_table_prefix()
def count(b, p):
    n = 0
    for page in s3.get_paginator('list_objects_v2').paginate(Bucket=b, Prefix=p): n += len(page.get('Contents', []))
    return n
before = (count(bucket, prefix), count('opal-data-harvest', 'universe/v1/'))
cache = bu.load_sec_cache(); _ = bu.filing_identity_for('CAT_US_Equity', 'US', 'Caterpillar Inc', cache); _ = bu.filing_identity_for('ZZZZQQ_US_Equity', 'US', 'No Such Co', cache)
after = (count(bucket, prefix), count('opal-data-harvest', 'universe/v1/'))
print('bucket', bucket, 'prefix', prefix); print('before', before, 'after', after, 'step1_read_writes_nothing', before == after)
"</invocation><expect>step1_read_writes_nothing True -- the object counts under the bronze prefix and under universe/v1/ are equal before and after a load plus two lookups (a hit and a planted miss): step 1's read is a read; the landing happens ONLY under --refresh-sec-table (AC2), never as a side effect of a lookup or a --dry-run</expect></criterion>
  <criterion id="AC7" cell_refs="AMGT-rk-32"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m unittest discover -s lib/research/identity/tests -p "test_*.py" -q 2>&1 | tail -4</invocation><expect>OK with the count printed, 0 failures, 0 errors -- the existing fixture arms (test_union_universe.py:163-195, the fixture at :30 passed directly) unchanged and green, plus the three new arms of RULED 5 (the 3-row fixture shaping and denominator, the loud refusal when no landed table exists, the miss note naming the object)</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this
order. AC1 runs BEFORE any edit; AC2 lands the day's table (or waits, per BOUNDS); AC3-AC7 run after your edit.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~36/AMGT_RESAPP.TO-AMGT-rk-32.step-one-live-sec-table.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6,AC7` (rc 0 is the verdict); flip
`<status>` to `complete`; commit with `--only -- <paths>`. Report once: the GET count (0 or 1), the landed
address and row count, CAT/CSL/Keyence's three dispositions with their notes, and AC7's count.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>superseded</status>
<superseded_by>AMGT-rk-84 (H2, filings harvest writer): its fetch key sec/harvest/bronze/company_tickers is H2's channel and C-DEDUPE-BY-KEY allows one writer per fetch key; its universe-builder consumer change is re-cut after H2 drains. RULED by 1.0.0_SA_CTO~Z, ROUND_ANALYSIS.round20.md s.2 @ab54fb15e0 (msg 24109): SUPERSEDED is terminal, not acceptance (R4); the remedy stays owed by the successor. Flipped in the round-21 issuance by 2.0.0_SA_COO~Z.</superseded_by>
<round>14</round>
<slot>~36</slot>
<fabric>site-z</fabric>
