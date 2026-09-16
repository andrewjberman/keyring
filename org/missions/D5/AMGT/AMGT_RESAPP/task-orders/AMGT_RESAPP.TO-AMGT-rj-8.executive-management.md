# AMGT_RESAPP task order -- `AMGT-rj-8` -- EXECUTIVE MANAGEMENT -- who runs the company, from the filing first, and how long they have

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rj-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~22</issued_to>
<issued_by>2.0.0_SA_COO~W</issued_by>
<placeholders>NONE</placeholders>

**You are `0.9.0_WK_AMGT_RESAPP~22`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt (a sparse cone:
`.tools`, `org`, `docs`, `rcg`, `lib`, `data`; `infra/`, `portal/`, `workflows/` are absent by design). Your first act prints
`git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/`, `lib/research/identity/crosswalk.py`, `lib/research/filings/` and
`data/find/imo/scripts/_util/lusha_client.py` exist; if any is absent, STOP with a BLOCKING row. **YOU HOLD CHAIN E, a queue of TWO
orders (`rj-8`, then `rj-13`); this is the first, spawned after `rj-4` (the crosswalk and the union universe) and `rj-6` (the filings,
persisted in the pool) are drained.** Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~22;`.

## 1. THE CELL, inlined in full -- `AMGT-rj-8` (FWD-17; C-EXEC-MANAGEMENT; interface M-1)

**THE OUTCOME (PRD v0.8 @`1170b4da69`):** *FWD-17 "One tab lists the company's senior executives, each with their role, a profile link
and how long they have held the role, and states how the team's average tenure compares with the average across every company the
page covers. Where a person cannot be confirmed from the company's own filings, the page says so."* **THE CONTRACT (C-EXEC-MANAGEMENT,
SIGNED):** *"The roster and each officer's role start come from the FILING's executive-officer section (the authority); Lusha
prospecting enriches each CONFIRMED officer with a profile link and title (card 2: the `c-suite` filter is loose and carries no
tenure); a targeted web search on the company's own IR domain fills the CEO's public profile; the pool-average tenure is computed
over the union universe from the same filing field. No contact data point is stored. Owner of the collection lane: the harvest
estate under the same loop discipline Andrew set at ~04:3xZ."* Andrew's words: "pull the whole c suite and also have a piece in
there that is like average tenor of exec management as compared to the rest of the pool" (~05:4xZ); "Exec Management profile (CEO
from Lusha + Maybe a targeted web search)" (~05:1xZ).

**MEASURED (card 2 @`5007337353`; READ `measure_lusha_csuite.py` and `boeing_csuite_prospecting.json` FIRST):** Lusha v3
`contacts/prospecting` via the estate's own client (`data/find/imo/scripts/_util/lusha_client.py`, `LushaClient`), boeing.com,
seniority `c-suite` (id 9): 1.6 s, 2 credits, 50 of 50 results, 9 fields per person (`id, name, jobTitle{title, department},
socialLinks, company, location, has, canReveal`), NO tenure or role-start field; the filter is LOOSE (an IT operations manager beside
a CTO). So the FILING is the authority for who the officers are and since when; Lusha attaches a profile link. The key:
`comp-secrets get <the find-insure/lusha-ai/* name> --reveal` (list the names with `comp-secrets list` first; never a raw
secretsmanager read); the estate's SERP primitive for the IR-domain search: `data/find/dualbiz/scripts/serp.py serp_brightdata()`
(a dedicated SERP zone; capped pages).

**WHAT `rj-6` LANDED FOR YOU:** `filings/v1/{security_key}/{accession}.source.json` in the pool -- the persisted filing with its
officer section (Item 10 of a 10-K / the directors-and-senior-management item of a 20-F) for BA_US_Equity, COST_US_Equity,
HD_US_Equity, SAP_GY_Equity, BABA_US_Equity and up to two more names the issuer names in your spawn prompt; identities through
`lib/research/identity/crosswalk.py` (X-1); the union universe `universe/v1/<as_of>.json` (U-1).

**DELIVER, in this order:**
1. `lib/research/management/roster.py`: from the persisted filing's officer section, the officers `{name, role, role_start (year or
   date as the filing states it), source: filing, confirmed: true}`; where the section is absent or unparseable, the object says
   `roster_status: UNRESOLVED-SOURCE` with the reason -- never a guessed roster. The role-start field is EXERCISED on a real filing
   (the contract's last clause): print, per name, how many officers carry a role start and how many do not.
2. `lib/research/management/enrich.py`: for each CONFIRMED officer, Lusha prospecting by company domain + name match -> `profile_url`
   (the LinkedIn link Lusha carries) and Lusha's title beside the filing's role; an officer Lusha cannot match keeps `profile_url:
   null`, `enrichment: ABSENT`; a targeted SERP on the company's IR domain for the CEO (one query, capped pages) -> `ceo_public_profile:
   {url, title, snippet}` or ABSENT. NO contact field is ever stored: the schema FORBIDS `email`, `phone`, `mobile`, and the record is
   scrubbed before write. Credits used printed per call.
3. `management/v1/{security_key}/{as_of}.json` (INTERFACE M-1: `{security_key, as_of, roster_status, source_accession, officers:
   [{name, role, role_start, tenure_years, profile_url, lusha_title, source, confirmed, enrichment}], avg_tenure_years, ceo_public_profile,
   generated: true}`) and `management/v1/_pool/{as_of}.json` (`{as_of, pool_avg_tenure_years, pool_denominator: {names_in_union,
   names_with_roster, officers_with_role_start}}`) -- the pool average over EVERY name of U-1 that has a roster object (today: the QA
   names; the batch below covers the rest), the denominator printed; uploads with `Metadata {document-sha256, schema-version}` and
   read-back. A JSON schema with `additionalProperties: false`.
4. A local batch `python -m lib.research.management.batch --universe <U-1 key> [--limit N] [--dry-run]` over the union universe and
   a Windows task DEFINITION left DISABLED (`OpalResearch-ExecManagement`, weekly); the production loop is the harvest estate's.
5. **QA one-shot** on the QA names above; unit tests over a fixture officer section (parse, a missing section, the scrub, the pool
   average with its denominator, the Lusha match with a stubbed client).

**BOUND:** Lusha credits: at most 2 per name in this cell (the prospecting call returns the roster page; no `reveal`); no contact
data; no portal edit (the tab is `rj-9`'s over M-1); no deploy; the batch defined, not run over the universe; no loop started.

## 2. WHERE THIS CAME FROM

**ROUND 11**, decomposition v1.3 s.19 @`73938cdae4`, on Andrew-direct ~05:04Z @`7cf62a165f` (executive managers; Lusha), ~05:1xZ,
~05:4xZ @`a5c6a066de` (the whole C-suite; tenure vs the pool), the voice memo part two, card 2 @`5007337353`, and the analysis
@`8d5fe78265` s.6 item 5. Readers of M-1: rj-9, rj-11.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/management/
lib/research/identity/
lib/research/filings/
data/find/imo/scripts/_util/lusha_client.py
data/find/dualbiz/scripts/serp.py
org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_RESAPP_SUBSTRATE_MEASUREMENTS_20260915_W/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~19/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~20/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rj-8.executive-management.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL** (RULING 1). `lib/research/identity/`, `lib/research/filings/` (call it), the two
  clients, the CTO's cards and the `~19` / `~20` deliverables are READ-ONLY; your new package is `lib/research/management/`.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~22 <0.9.0_WK_AMGT_RESAPP~22@opal.agent>" -F <msgfile>
  -- <paths>`, message file by the Write tool, ASCII only. Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

Egress: Andrew-direct ~05:42Z @`dfa63b6d92` -- Lusha and the SERP zone are inside it; every call recorded with its instrument,
credits and time. Secrets ONLY through `comp-secrets get <name> --reveal`. No non-ASCII in anything that reaches AWS. **THE REFUSAL
CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row. **SURPRISE ROWS:** *"a worker's row is
`AMGT_RESAPP-Z-W<n>-S<k>` ... `"project": "AMGT_RESAPP"` and `"fabric": "site-z"` on every new row."* Your coordinate is `W22`; your
first row is `AMGT_RESAPP-Z-W22-S1`; append by textual splice; never edit an existing row.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rj-8"><invocation>python -m unittest discover -s lib/research/management/tests -p "test_*.py" -q 2>&1 | tail -3; python -c "import json,io; s=json.load(io.open('lib/research/management/management.schema.json',encoding='utf-8')); t=json.dumps(s); print('additionalProperties', s.get('additionalProperties'), 'forbids-email', 'email' in t and ('not' in t or 'forbid' in t.lower()), 'has-role_start', 'role_start' in t, 'has-confirmed', 'confirmed' in t)"</invocation><expect>the suite ends OK with 0 failures and 0 errors (parse, missing section, the scrub, the pool average with denominator, a stubbed Lusha match); additionalProperties False; forbids-email True (the schema names email/phone/mobile as forbidden, and the scrub test proves it); has-role_start True; has-confirmed True</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rj-8"><invocation>timeout 115 python -m lib.research.management.roster --security-key BA_US_Equity --dry-run 2>&1 | tail -8</invocation><expect>SOURCE naming the persisted filing's accession from the pool; roster_status RESOLVED; officers N at least 5, each with name, role and source filing; with-role-start M printed beside without-role-start (the field EXERCISED on a real filing: M at least 1 is the claim, M 0 is a row that the 10-K's section carries no dates and a stated fallback); confirmed N. A guessed roster, or a roster built from Lusha rather than the filing, is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rj-8"><invocation>timeout 115 python -m lib.research.management.enrich --security-key BA_US_Equity --write-pool 2>&1 | tail -10</invocation><expect>LUSHA with the domain, the credits used (at most 2) and matched K of N officers (each with a profile_url); unmatched officers listed with enrichment ABSENT; SERP with one query on the IR domain and the CEO's public profile url or ABSENT; SCRUB confirming 0 contact fields stored; OK: uploaded management/v1/BA_US_Equity/2026-09-15.json with read-back. A stored email or phone, or more than 2 credits, is NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rj-8"><invocation>for k in COST_US_Equity HD_US_Equity SAP_GY_Equity BABA_US_Equity; do timeout 115 python -m lib.research.management.enrich --security-key $k --write-pool 2>&1 | grep -E "SOURCE|roster_status|LUSHA|SCRUB|uploaded|UNRESOLVED" | cut -c1-180; done; .tools/aws s3api list-objects-v2 --bucket opal-data-harvest --prefix management/v1/ --query "Contents[].Key" --output text | tr "\t" "\n" | cat</invocation><expect>four more names processed (a 20-F filer whose section lacks the officers is roster_status UNRESOLVED-SOURCE with its reason, never a guessed roster); the listing showing management/v1/<key>/2026-09-15.json for the five QA names (and any extra the issuer named) plus management/v1/_pool/2026-09-15.json. Fewer objects than names processed is NOT met</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rj-8"><invocation>.tools/aws s3api get-object --bucket opal-data-harvest --key management/v1/_pool/2026-09-15.json .scratch/rj8.pool.json --query ContentLength --output text; python -c "import json,io; d=json.load(io.open('.scratch/rj8.pool.json',encoding='utf-8')); print('pool_avg_tenure_years', d.get('pool_avg_tenure_years'), 'denominator', json.dumps(d.get('pool_denominator')))"; .tools/aws s3api get-object --bucket opal-data-harvest --key management/v1/BA_US_Equity/2026-09-15.json .scratch/rj8.ba.json --query ContentLength --output text; python -c "import json,io; d=json.load(io.open('.scratch/rj8.ba.json',encoding='utf-8')); o=d['officers']; print('officers', len(o), 'avg_tenure_years', d.get('avg_tenure_years'), 'with-profile', sum(1 for x in o if x.get('profile_url')), 'contact-fields', sum(1 for x in o for k in x if k in ('email','phone','mobile')))"</invocation><expect>pool_avg_tenure_years a number (or null with the denominator explaining names_with_roster 0), pool_denominator with names_in_union, names_with_roster and officers_with_role_start printed; BA: officers at least 5, avg_tenure_years a number when role starts exist, with-profile at least 1, contact-fields 0. Any contact field is NOT met</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rj-8"><invocation>python -m lib.research.management.batch --universe universe/v1/2026-09-15.json --dry-run 2>&1 | tail -4; MSYS_NO_PATHCONV=1 schtasks /Query /TN OpalResearch-ExecManagement /FO LIST /V 2>&1 | tr -d "\r" | grep -E "TaskName|Scheduled Task State|Schedule Type" | cat; git log --format="%h %an %s" -3 -- lib/research/management/ | cut -c1-140; python -c "import io,glob; fs=glob.glob('lib/research/management/*.py'); print('files', len(fs), 'nonascii', sum(sum(1 for ch in io.open(f,encoding='utf-8').read() if ord(ch)>127) for f in fs), 'raw-secretsmanager-reads', sum(io.open(f,encoding='utf-8').read().count('get_secret_value') for f in fs), 'reveal-calls', sum(io.open(f,encoding='utf-8').read().count('reveal') for f in fs))"</invocation><expect>the dry-run prints the batch denominators and runs nothing; the task exists with Scheduled Task State Disabled; commits by this serial; nonascii 0; raw-secretsmanager-reads 0; reveal-calls 0 (no Lusha contact reveal anywhere in the package). An enabled task or a reveal call is NOT met</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~22/AMGT_RESAPP.TO-AMGT-rj-8.executive-management.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json` (the checker compiles `expect` as a REGEX over the evidence), graded by YOUR WORKTREE'S
OWN `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6` (rc 0 is the verdict); keep the run logs and the credits
table beside it; flip `<status>` to `complete`; commit with `--only -- <paths>`. Report once. **If a criterion cannot be met, leave
the order OPEN and file a row.**

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>11</round>
<slot>~22</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<authority>PRD v0.8 @`1170b4da69` (ADMITTED) FWD-17 and C-EXEC-MANAGEMENT (Andrew-direct ~05:04Z @`7cf62a165f`, ~05:1xZ and ~05:4xZ @`a5c6a066de`, the voice memo @`fbd5d91431` part two; card 2 @`5007337353`), the egress word @`dfa63b6d92`, the comp-secrets word, `1.0.0_SA_CTO~W`'s L10 round-10 analysis @`8d5fe78265` s.6 item 5, the CRO's follow-up @`865e4fc113` item 4 (after rj-6's drain), decomposition v1.3 s.19 @`73938cdae4` (cell rj-8, chain E first; interface M-1). Cell set: s.19a; fan-out: s.19e.</authority>

<preflight>
ALL RUN 2026-09-15 06:4xZ at this cut (decomposition v1.3 s.19g).
comp-schedule: RUN (--drift) -- 5 of 5 carriers within budget (16.0 s of 90); REACHED-DENOMINATORS C1=23, C2=8, C3=12, C4=21, C5=334; C2 = 8 OPEN deploy-ledger entries (none this project's; rj-10 opens one and closes it inside the round); C3 = 12 standing NEVER clauses (no monitor, no alarm); NO new scheduled producer is cut this round (every batch is a local Windows task DISABLED at creation, Andrew's box word @187f003998); BLIND on C4 and C5 in the tool's own voice.
comp-iam: RUN (gaps) -- 838 call(s) verdicted across 98 mapped role(s) over 474 .tf files; 629 UNRESOLVABLE-RESOURCE, 142 GRANTED, 51 GRANTED-BROAD (EXCLUDED, NOT CLEARED), 14 UNGRANTED, 2 GRANTED-ACTION / UNGRANTED-RESOURCE; 15 missing, 291 deny-present, 1 coverage-unknown, 2 resource-mismatch across 32 services; BLIND on 266 calls in 26 role-UNMAPPED services. The round's IAM delta lives in rj-10 alone: READ grants by prefix on opal-data-harvest for two roles, the DynamoDB articles grants REMOVED, no Scan, no wildcard resource; every other cell acts under the operator's own credentials and takes no AWS grant.
comp-adversary: RUN (compose on the decomposition, --no-packet) -- 48 commit pins, 13 repo paths, 17 file:line cites, 14 tool mentions; 23 hex runs not parsed (named); T11 NOT RESOLVED (293 uncited siblings, CAP 25 declared); stage 4 disabled by the caller. The round's adversarial surfaces: filing text, vendor responses and pool objects are DATA inside a model prompt (rj-6, rj-11 say so in the prompt; the verbatim gate runs against the PASSAGE; held-uncited claims never render); Posture is marked machine and read by no trade consumer; the Lusha response is scrubbed to name/title/link; the social job is capped in posts and USD.
comp-cache: DECLARED-NOT-APPLICABLE -- no portal surface in this cell.
comp-blast: DECLARED-NOT-APPLICABLE -- this cell moves nothing on the live plane: its writes are local code, tests and pool objects under the operator's credentials (a QA one-shot is not a production act); the round's one live move is rj-10's, covered by the co-sign.
</preflight>

**AMENDMENT 1 (2026-09-15 ~11:2xZ, `2.0.0_SA_COO~W`, issuer):** rows `AMGT_RESAPP-Z-W20-S2` and `W20-S3` (worker `~20`, rj-6 AC6; the same shape sits in this order's AC6): the task-query invocation cannot produce the fields it names on this device -- MSYS argv conversion rewrites the first argument `/Query` into `C:/Program Files/Git/Query` so the literal command emits zero lines, and `schtasks /FO LIST` carries neither `Scheduled Task State` nor `Schedule Type` without `/V`. The worker measured the world-state as correct (TaskName present, Schedule Type Weekly, Scheduled Task State Disabled; 0 of 4 fields as written, 2 of 4 with MSYS_NO_PATHCONV=1, 4 of 4 with /V) and REFUSED the criterion as written. The invocation is re-cut with the `MSYS_NO_PATHCONV=1` prefix and `/V`; the expectation is unchanged. No other clause moved. Re-cut here BEFORE this order's spawn.
