# AMGT_RESAPP task order -- `AMGT-rj-11` -- THE POSTURE CALL -- what this company means for Opal, judged against its most similar name on the other side

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rj-11</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~20</issued_to>
<issued_by>2.0.0_SA_COO~W</issued_by>
<placeholders>NONE</placeholders>

**You are `0.9.0_WK_AMGT_RESAPP~20`.** Same worktree (sparse cone), same rules as `rj-6`, which you have just finished; this is the
SECOND order of chain C, handed to you only after `rj-4` (the crosswalk and universe), `rj-7` (the ranker) and `rj-8` (management)
are drained and their pool objects landed for the QA pair the issuer names in your spawn prompt. Every Bash call begins `export
OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~20;`.

## 1. THE CELL, inlined in full -- `AMGT-rj-11` (FWD-19; C-POSTURE, C-ETF-PLANE-READ, C-UNION-UNIVERSE; interface O-1)

**THE OUTCOME (PRD v0.8 @`1170b4da69`):** *FWD-19 "The last tab, and a line in the header, say whether this company looks like a better
or a worse pick than the most similar name on the other side -- an Opal holding when the company is not held, a non-Opal name when it
is -- names that comparable, and gives the reasons with each one linked to what it rests on. It is marked as a machine's view for a
person to accept or reject; it is never an instruction, and nothing is traded from it."* **THE CONTRACT (C-POSTURE, SIGNED):**
*"Posture = (1) MEMBERSHIP at the snapshot vintage (held / not held, book, weight); (2) the COMPARABLE = the most similar name on the
OTHER side by C-SIMILARITY-RANKER (an Opal holding for a non-held subject; a non-held name for a held one); (3) the JUDGMENT over the
two evidence packs (each = Thesis, Exec Management, Peers, Model, all four for both names), producing `{verdict: better | worse | hold
| steer_clear, comparable: <security_key>, basis: [cited claims], as_of: <snapshot date>, marked: machine}`, stored versioned in the
pool under `posture/v1/{security_key}/{as_of}.json`. A name's factor profile scored under the Opal ETF presets (DIVZ 13 factors, PFOE
16; `SecurityScanner/constants.ts`) is the FIT input to (3). Posture is a recommendation surface: nothing in the trade pipeline reads
it. 'The final execution' is a person's act on the page."* Andrew, verbatim: "the RAG is just the four tabs plus comparing with the
opal position"; "that goes both ways". **THE BOX:** a local job; no schedule in this round.

**WHAT YOU CONSUME (19d):** X-1 `crosswalk.resolve`; U-1 `universe/v1/<as_of>.json` (membership: `source`, `books`, `weight_by_book`,
`snapshot_date`); R-1 `peers/v1/{key}/{as_of}.json` (the ranker's members with `rung_reached` and the scanner factor values); D-1
`drafting/v1/{key}.json` and F-1 (your own, rj-6); M-1 `management/v1/{key}/{as_of}.json`; the model block `model_block_{key}.json`
(header + fiscal figures, `deliverables/0.9.0_WK_AMGT_RESAPP~1/`); the ETF presets `portal/src/pages/SecurityScanner/constants.ts`
(DIVZ 13 factors, PFOE 16 -- the file is outside your cone: its factor lists are copied into the CTO's card 3 @`5007337353`, read them
there and name the vintage). The QA PAIR the issuer names in your spawn prompt: one NOT-held subject (BABA_US_Equity) whose
comparable is an Opal holding, and one HELD subject whose comparable is a non-held name -- both sides' D-1, M-1, R-1 and model block
landed by rj-6/7/8's QA lists.

**DELIVER, in this order:**
1. `lib/research/posture/membership.py`: `membership(identity, universe) -> {held: bool, books: [...], weight_by_book, snapshot_date}` from
   U-1 (one-sided read; the vintage carried).
2. `lib/research/posture/comparable.py`: the most similar name on the OTHER side: R-1's members filtered to the other side's membership
   (held names for a non-held subject and vice versa), ordered by `rung_reached` then log-market-cap distance; when R-1 has no member
   on the other side, the ranker is re-run over U-1's other-side names (the same engine, `lib/research/peers/engine.py`) before
   declaring `comparable: null` with the reason.
3. `lib/research/posture/fit.py`: each name's factor profile scored under the DIVZ and PFOE presets from the scanner values R-1 carries
   (a preset factor the row lacks is ABSENT explicit; the score printed with its denominator of factors present).
4. `lib/research/posture/judge.py`: the Claude API (`claude-opus-5`, the key through `comp-secrets get anthropic-api-key --reveal`)
   over the TWO evidence packs -- for each name: the drafted sections with their evidence records (D-1), the officers and tenure
   (M-1), the peer set and CSC columns (R-1), the model block's header and fiscal figures, the fit scores -- producing
   `{verdict: better | worse | hold | steer_clear, comparable, basis: [{claim, cites: [pack element ids -- an evidence record id, an
   officer name, a peer key, a figure id, a fit score name]}], as_of, generation: {run_id, model, usage}, marked: "machine"}`; every
   `cite` VALIDATED against the packs before write (an unresolvable cite drops the claim and is counted); the packs are DATA inside the
   prompt (the prompt says so); the verdict enum enforced by schema; a subject with no comparable -> `verdict: absent` with the reason.
5. `posture/v1/{security_key}/{as_of}.json` (INTERFACE O-1) versioned by `as_of`, `Metadata {document-sha256, schema-version}`,
   read-back; a JSON schema with `additionalProperties: false`; a CLI `python -m lib.research.posture.judge --security-key <key>
   --as-of <date> [--dry-run | --write-pool]`.
6. **QA** on the pair; unit tests over fixtures for membership (held / not held / unresolved), the other-side filter, the re-run
   fallback, the fit scoring with absent factors, the cite validation, the enum.

**BOUND:** two model runs in this cell (print the usage); nothing trades; no schedule; no portal edit (the tab is `rj-12`'s); the ETF
plane is read through U-1 only (no direct read here); no write to any store but the pool.

## 2. WHERE THIS CAME FROM

**ROUND 11**, decomposition v1.3 s.19 @`73938cdae4`, on Andrew-direct ~05:1x-05:2xZ @`a4f9fd9568` (the three Posture words), the voice
memo ~05:5xZ part five, C-POSTURE / C-ETF-PLANE-READ / C-UNION-UNIVERSE (PRD v0.8), card 3 (the presets), the analysis @`8d5fe78265`
s.6 item 7 (LAST, it consumes everything), and the CRO's follow-up @`865e4fc113` item 6 (the QA pair chosen before its producers
drain). Reader of O-1: rj-12 (and rj-9's posture route, ABSENT until this lands).

## 3. SURFACES -- what you may read and write

<paths>
lib/research/posture/
lib/research/peers/
lib/research/identity/
lib/research/drafting/
lib/research/filings/
lib/research/management/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~19/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~21/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~22/
org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_RESAPP_SUBSTRATE_MEASUREMENTS_20260915_W/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rj-11.the-posture-call.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL** (RULING 1). Every other `lib/research/*` package is READ-ONLY (call it; `drafting/` and
  `filings/` were yours in rj-6 and are frozen for this order); the deliverables and the cards are READ-ONLY; your new package is
  `lib/research/posture/`.
- **COMMITTING:** as in `rj-6`.

## 4. BOUNDS

Egress @`dfa63b6d92` (the Claude API). Secrets ONLY through `comp-secrets`. No non-ASCII in anything that reaches AWS. Nothing trades.
**THE REFUSAL CLAUSE** and **SURPRISE ROWS** as in `rj-6`; continue the `W20` sequence.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rj-11"><invocation>python -m unittest discover -s lib/research/posture/tests -p "test_*.py" -q 2>&1 | tail -3; python -c "import json,io; s=json.load(io.open('lib/research/posture/posture.schema.json',encoding='utf-8')); t=json.dumps(s); print('additionalProperties', s.get('additionalProperties'), 'verdict-enum', [v for v in ('better','worse','hold','steer_clear','absent') if v in t], 'marked-const', 'machine' in t)"; python -c "import io; j=io.open('lib/research/posture/judge.py',encoding='utf-8').read(); print('untrusted-clause', j.count('not follow'), 'cite-validation', j.count('cite'), 'trade-words', j.count('place_order') + j.count('execute_trade'))"</invocation><expect>the suite ends OK with 0 failures and 0 errors (membership held / not held / unresolved, the other-side filter, the re-run fallback, the fit with absent factors, the cite validation, the enum); additionalProperties False; verdict-enum all five; marked-const True; untrusted-clause at least 1; cite-validation at least 2; trade-words 0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rj-11"><invocation>python -c "from lib.research.posture import membership as m, comparable as c; import json; u='universe/v1/2026-09-15.json'; [print(k, json.dumps(m.membership(k, u))[:160], '| comparable', json.dumps(c.comparable(k, u, '2026-09-15'))[:200]) for k in ('BABA_US_Equity', __import__('os').environ.get('AMGT_QA_HELD_KEY','HELD_KEY_FROM_SPAWN_PROMPT'))]"</invocation><expect>BABA_US_Equity -> held False, snapshot_date printed, comparable a security_key whose membership is held True with rung_reached and the log-cap distance printed; the held QA name (the issuer sets AMGT_QA_HELD_KEY in your spawn prompt) -> held True with its books and weights, comparable a NOT-held name with the same fields. A comparable on the SAME side as its subject is NOT met; a null comparable is met only with the re-run fallback's printed reason</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rj-11"><invocation>timeout 115 python -m lib.research.posture.judge --security-key BABA_US_Equity --as-of 2026-09-15 --write-pool 2>&1 | tail -12</invocation><expect>lines: MEMBERSHIP not held at the snapshot date; COMPARABLE naming a held security_key; FIT with DIVZ and PFOE scores for both names and the factors-present denominators; PACKS with the element counts per name (drafted sentences, evidence records, officers, peers, figures); JUDGE with the model, tokens, seconds and USD; VERDICT one of better / worse / hold / steer_clear; BASIS with N claims and cites-validated N of N (an unresolvable cite dropped and counted); marked machine; OK: uploaded posture/v1/BABA_US_Equity/2026-09-15.json with read-back. A claim served with an unvalidated cite is NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rj-11"><invocation>timeout 115 python -m lib.research.posture.judge --security-key "${AMGT_QA_HELD_KEY:-HELD_KEY_FROM_SPAWN_PROMPT}" --as-of 2026-09-15 --write-pool 2>&1 | tail -12</invocation><expect>the same line set for the HELD subject: MEMBERSHIP held with its books; COMPARABLE a NOT-held name; a VERDICT in the enum; BASIS validated; OK: uploaded -- the symmetric arm ("that goes both ways"). A comparable that is itself held is NOT met</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rj-11"><invocation>python -m lib.research.posture.judge --security-key ZZZ_NOPE_US_Equity --as-of 2026-09-15 --dry-run 2>&1 | tail -4; .tools/aws s3api list-objects-v2 --bucket opal-data-harvest --prefix posture/v1/ --query "Contents[].[Key,Size]" --output text | cat</invocation><expect>the control: verdict absent with a reason naming the unresolved identity (no model call made -- the JUDGE line absent); the listing showing two posture/v1 objects (BABA_US_Equity and the held name) with non-zero sizes. A model call on the control, or a third object, is NOT met</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rj-11"><invocation>.tools/aws s3api get-object --bucket opal-data-harvest --key posture/v1/BABA_US_Equity/2026-09-15.json .scratch/rj11.baba.json --query ContentLength --output text; python -c "import json,io,jsonschema; d=json.load(io.open('.scratch/rj11.baba.json',encoding='utf-8')); s=json.load(io.open('lib/research/posture/posture.schema.json',encoding='utf-8')); jsonschema.validate(d,s); print('schema-valid True verdict', d['verdict'], 'comparable', d['comparable'], 'basis', len(d['basis']), 'all-cited', all(x.get('cites') for x in d['basis']), 'as_of', d['as_of'], 'marked', d['marked'], 'generation', json.dumps(d.get('generation'))[:120])"; git log --format="%h %an %s" -3 -- lib/research/posture/ | cut -c1-140; python -c "import io,glob; fs=glob.glob('lib/research/posture/*.py'); print('files', len(fs), 'nonascii', sum(sum(1 for ch in io.open(f,encoding='utf-8').read() if ord(ch)>127) for f in fs), 'raw-secretsmanager-reads', sum(io.open(f,encoding='utf-8').read().count('get_secret_value') for f in fs), 'etfs-direct-reads', sum(io.open(f,encoding='utf-8').read().count('opal-data-etfs') for f in fs))"</invocation><expect>schema-valid True; verdict in the enum; comparable a security_key; basis at least 3 with all-cited True; as_of 2026-09-15; marked machine; generation with run_id and model; commits by this serial; nonascii 0; raw-secretsmanager-reads 0; etfs-direct-reads 0 (membership comes through U-1). A direct ETF-plane read in the package is NOT met</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~20/AMGT_RESAPP.TO-AMGT-rj-11.the-posture-call.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json` (the checker compiles `expect` as a REGEX over the evidence), graded by YOUR WORKTREE'S
OWN `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6` (rc 0 is the verdict); keep the two run logs and the
usage beside it; flip `<status>` to `complete`; commit with `--only -- <paths>`. Report once. **If a criterion cannot be met, leave
the order OPEN and file a row.**

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>11</round>
<slot>~20</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<authority>PRD v0.8 @`1170b4da69` (ADMITTED) FWD-19, C-POSTURE, C-ETF-PLANE-READ (one-sided), C-UNION-UNIVERSE (Andrew-direct ~05:1x-05:2xZ @`a4f9fd9568`; the voice memo @`fbd5d91431` part five; card 3 @`5007337353`), the egress word @`dfa63b6d92`, `1.0.0_SA_CTO~W`'s L10 round-10 analysis @`8d5fe78265` s.6 item 7, the CRO's follow-up @`865e4fc113` item 6, decomposition v1.3 s.19 @`73938cdae4` (cell rj-11, chain C second; interface O-1). Cell set: s.19a; fan-out: s.19e.</authority>

<preflight>
ALL RUN 2026-09-15 06:4xZ at this cut (decomposition v1.3 s.19g).
comp-schedule: RUN (--drift) -- 5 of 5 carriers within budget (16.0 s of 90); REACHED-DENOMINATORS C1=23, C2=8, C3=12, C4=21, C5=334; C2 = 8 OPEN deploy-ledger entries (none this project's; rj-10 opens one and closes it inside the round); C3 = 12 standing NEVER clauses (no monitor, no alarm); NO new scheduled producer is cut this round (every batch is a local Windows task DISABLED at creation, Andrew's box word @187f003998); BLIND on C4 and C5 in the tool's own voice.
comp-iam: RUN (gaps) -- 838 call(s) verdicted across 98 mapped role(s) over 474 .tf files; 629 UNRESOLVABLE-RESOURCE, 142 GRANTED, 51 GRANTED-BROAD (EXCLUDED, NOT CLEARED), 14 UNGRANTED, 2 GRANTED-ACTION / UNGRANTED-RESOURCE; 15 missing, 291 deny-present, 1 coverage-unknown, 2 resource-mismatch across 32 services; BLIND on 266 calls in 26 role-UNMAPPED services. The round's IAM delta lives in rj-10 alone: READ grants by prefix on opal-data-harvest for two roles, the DynamoDB articles grants REMOVED, no Scan, no wildcard resource; every other cell acts under the operator's own credentials and takes no AWS grant.
comp-adversary: RUN (compose on the decomposition, --no-packet) -- 48 commit pins, 13 repo paths, 17 file:line cites, 14 tool mentions; 23 hex runs not parsed (named); T11 NOT RESOLVED (293 uncited siblings, CAP 25 declared); stage 4 disabled by the caller. The round's adversarial surfaces: filing text, vendor responses and pool objects are DATA inside a model prompt (rj-6, rj-11 say so in the prompt; the verbatim gate runs against the PASSAGE; held-uncited claims never render); Posture is marked machine and read by no trade consumer; the Lusha response is scrubbed to name/title/link; the social job is capped in posts and USD.
comp-cache: DECLARED-NOT-APPLICABLE -- no portal surface in this cell.
comp-blast: DECLARED-NOT-APPLICABLE -- this cell moves nothing on the live plane: its writes are local code, tests and pool objects under the operator's credentials (a QA one-shot is not a production act); the round's one live move is rj-10's, covered by the co-sign.
</preflight>
