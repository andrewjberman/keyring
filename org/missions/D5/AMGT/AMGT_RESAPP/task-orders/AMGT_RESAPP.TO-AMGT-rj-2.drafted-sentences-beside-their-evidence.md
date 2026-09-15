# AMGT_RESAPP task order -- `AMGT-rj-2` -- DRAFTED SENTENCES BESIDE THEIR EVIDENCE -- machine prose reaches the page paired with the passage it rests on

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rj-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~18</issued_to>
<issued_by>2.0.0_SA_COO~W</issued_by>
<placeholders>NONE</placeholders>

**You are `0.9.0_WK_AMGT_RESAPP~18`.** Same worktree, same portal checkout and branch, same rules as `rj-1`, which you have just
finished; this is the SECOND order of chain A, handed to you only after `rj-6` (chain C) is drained -- its typed evidence is your
input. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~18;`. **NEVER RUN AN INSTALL.** The `portal` gitlink NEVER moves.

## 1. THE CELL, inlined in full -- `AMGT-rj-2` (row `C-S196`; FWD-9; C-FILINGS-ANALYZER's marking and reader clauses)

**THE SEAM (06:1x-06:3xZ):** `lib/research/api/scoped_amgt.py:680` -- `"drafted_sections": []`, hardcoded inside `read_thesis_bundle`
(`:664-682`); `portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx:34-66 DraftedSectionBlock`, at `:52` the evidence is a native
tooltip `title={sentence.evidence ? `Evidence: ${sentence.evidence}` : undefined}` (an array stringified) while the file's header
`:12` claims "evidence beside it, never behind a link"; the `machine` marker at `:54-58` is inline; `CheckFaceBadge.tsx` renders PASS
/ REFUSE / PROVISIONAL.

**WHAT `rj-6` LANDED (INTERFACE D-1, `drafting/v1/<security_key>.json` in the pool, for BA_US_Equity, COST_US_Equity, SAP_GY_Equity,
HD_US_Equity, BABA_US_Equity):** the drafting schema, TYPED -- `evidence_records: [{id, passage, source: {accession, document_sha256,
location}}]` at the document level; sections x sentences `{text, generated: true, evidence: [ids], verbatim_check}`; `held_uncited`;
`thesis_driver`; `dropped` -- and the library's validator in `lib/research/drafting/pipeline.py` that checks every id's existence,
association and source version and runs the verbatim gate against the PASSAGE. You CALL that validator; `lib/research/drafting/` is
chain C's and is READ-ONLY for you.

**THE CVO's grade (REMEDIATION_v10, C-S196):** "the adapter returns zero drafted sections and the actual component hides sentence
evidence in a tooltip. FWD9 is not met by figure badges. Recut the existing drafting/adapter/Thesis connection and visibly pair
machine prose with its evidence."

**DELIVER, in this order:**
1. **The route serves typed evidence.** `read_thesis_bundle` reads `drafting/v1/<security_key>.json` for the resolved identity
   (rj-1's block) from the pool (boto3, us-east-1; `AMGT_DRAFTING_ROOT` points a local run at a directory of the same objects),
   validates it through the library's validator BEFORE serving, and returns `drafted_sections` with, per sentence, the resolved
   `evidence` as `[{id, passage, source}]` (the passage text travels to the page), `drafting_status: SERVED | ABSENT | INVALID`,
   `drafting_source: pool | local | none`, `held_uncited_count`, `thesis_driver`. An object failing validation is served as
   `drafted_sections: []` with `INVALID` and the validator's message, never silently.
2. **Evidence VISIBLE beside the sentence.** `ThesisTab.tsx`: every drafted sentence renders its `machine` marker inline AND, directly
   beneath it, each evidence PASSAGE quoted as text with a source label (accession, location); NO `title=` carrier for evidence in the
   file; `verbatim_check` as the `CheckFaceBadge`; `held_uncited_count` shown as a line ("N claims held uncited, not shown"), never as
   evidence.
3. **A render check** (`__harness__/drafting.harness.cjs`, `react-dom/server` over the real component) asserting, per sentence, that
   the passage text appears in the HTML AFTER the sentence text and BEFORE the next sentence, and that no `title="Evidence` attribute
   exists.
4. **The negative controls** are the library's: an object with an unknown evidence id is INVALID; an empty `evidence[]` is INVALID.

**BOUND:** no model call, no vendor call; no install; nothing promoted; no edit under `lib/research/drafting/`.

## 2. WHERE THIS CAME FROM

**ROUND 11**, decomposition v1.3 s.19 @`73938cdae4`, on the analysis @`8d5fe78265` s.6 item 1 and the slug @`e28f0b546c` item 2; the
CRO's filing-evidence brief @`a65fe406c2` (the typed-evidence shape) and connection brief @`0f9a04e81e` seam 3 (ids vs passages).

## 3. SURFACES -- what you may read and write

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/tests/
lib/research/drafting/
lib/research/identity/
portal/src/pages/SecurityAnalysis/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~20/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rj-2.drafted-sentences-beside-their-evidence.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL** (RULING 1). `lib/research/drafting/` (call the validator; do not edit),
  `lib/research/identity/`, the `~20` deliverables (rj-6's local copies of the D-1 objects, for `AMGT_DRAFTING_ROOT`) and the `~1`
  model blocks are READ-ONLY.
- **COMMITTING:** as in `rj-1`. Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

PORTAL FROZEN both fabrics: COMMIT YES / PROMOTE NO. No non-ASCII in anything you write. **THE REFUSAL CLAUSE** and **SURPRISE ROWS**
as in `rj-1`; continue the `W18` sequence from where `rj-1` left it.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rj-2"><invocation>python -c "import json; from lib.research.api import scoped_amgt as s; b=s.read_thesis_bundle('BA_US_Equity'); ds=b.get('drafted_sections') or []; ss=[q for x in ds for q in x.get('sentences',[])]; print('drafting_status', b.get('drafting_status'), 'drafting_source', b.get('drafting_source'), 'sections', len(ds), 'sentences', len(ss), 'with-passages', sum(1 for q in ss if q.get('evidence') and all(isinstance(e,dict) and e.get('passage') for e in q['evidence'])), 'generated-true', sum(1 for q in ss if q.get('generated') is True), 'verbatim-PASS', sum(1 for q in ss if q.get('verbatim_check')=='PASS'), 'held_uncited_count', b.get('held_uncited_count'), 'thesis_driver', json.dumps(b.get('thesis_driver'))[:120])"</invocation><expect>drafting_status SERVED, drafting_source pool, sections 5, sentences N at least 10, with-passages EQUAL to N (every served sentence carries resolved evidence with passage text), generated-true EQUAL to N, verbatim-PASS EQUAL to N, held_uncited_count a printed integer, thesis_driver naming a series. A sentence served with an id and no passage is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rj-2"><invocation>AMGT_DRAFTING_ROOT=".scratch/no-such-root" python -c "from lib.research.api import scoped_amgt as s; b=s.read_thesis_bundle('BA_US_Equity'); print('absent-status', b.get('drafting_status'), 'absent-sections', len(b.get('drafted_sections') or []))"; python -c "import json,io,os,glob; os.makedirs('.scratch/badroot',exist_ok=True); src=glob.glob('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~20/*BA_US_Equity*drafting*.json')[0]; d=json.load(io.open(src,encoding='utf-8')); d['sections'][0]['sentences'][0]['evidence']=['no-such-id']; io.open('.scratch/badroot/BA_US_Equity.json','w',encoding='utf-8').write(json.dumps(d)); d['sections'][0]['sentences'][0]['evidence']=[]; io.open('.scratch/badroot2/BA_US_Equity.json','w',encoding='utf-8').write(json.dumps(d)) if os.makedirs('.scratch/badroot2',exist_ok=True) is None else None"; for r in badroot badroot2; do AMGT_DRAFTING_ROOT=".scratch/$r" python -c "from lib.research.api import scoped_amgt as s; b=s.read_thesis_bundle('BA_US_Equity'); print('$r', b.get('drafting_status'), len(b.get('drafted_sections') or []))"; done</invocation><expect>absent-status ABSENT and absent-sections 0; badroot INVALID 0 (an unknown evidence id refuses the whole object); badroot2 INVALID 0 (an empty evidence array refuses it). A SERVED on any of the three arms is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rj-2"><invocation>python -c "import io; t=io.open('portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx',encoding='utf-8').read(); print('title-evidence-carrier', t.count('title={sentence.evidence'), 'title-Evidence-any', t.count('Evidence: '), 'passage-render', t.count('passage'), 'source-label', t.count('accession'), 'blockquote-or-list', t.count('<blockquote') + t.count('<ul') + t.count('<ol'), 'machine-marker', t.count('machine'), 'held-uncited-line', t.count('held'))"</invocation><expect>title-evidence-carrier 0 and title-Evidence-any 0, passage-render at least 2, source-label at least 1, blockquote-or-list at least 1, machine-marker at least 1, held-uncited-line at least 1. A surviving title= carrier for evidence is NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rj-2"><invocation>cd portal && timeout 110 node src/pages/SecurityAnalysis/__harness__/drafting.harness.cjs 2>&1 | tail -12; echo rc=$?</invocation><expect>rc=0 and check lines: passage_after_each_sentence true, passage_before_next_sentence true, no_title_evidence_attribute true, sentences_checked N at least 10 equal to the served bundle's sentence count, machine_marker_per_sentence true, held_uncited_line_present true. A harness that checks fewer sentences than the bundle carries is NOT met</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rj-2"><invocation>python -m unittest discover -s lib/research/api/tests -p "test_*.py" -q 2>&1 | tail -3; git diff --stat SITEZ...HEAD -- lib/research/drafting/ | cat; echo "drafting-diff-lines: $(git diff SITEZ...HEAD -- lib/research/drafting/ | wc -l)"</invocation><expect>the adapter suite ends OK with 0 failures and 0 errors; drafting-diff-lines 0 (this cell did not touch lib/research/drafting/ -- chain C owns it). Any drafting diff is NOT met</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rj-2"><invocation>cd portal && timeout 110 ./node_modules/.bin/vite build --logLevel info > ../.scratch/rj2.build.txt 2>&1; echo rc=$?; python -c "import glob,os; js=sorted(glob.glob('dist/assets/*.js')); toks={'machine':b'machine','control':b'zzz-no-such-string-rj2-control'}; hits={k:[os.path.basename(f) for f in js if v in open(f,'rb').read()] for k,v in toks.items()}; print('js-assets', len(js)); [print('TOKEN', k, len(v)) for k,v in hits.items()]"; cd .. && git -C portal log --oneline -3 | cat; echo "gitlink: $(git ls-tree HEAD portal | cut -c13-22)"</invocation><expect>rc=0, js-assets above 20, TOKEN machine at least 1, TOKEN control 0; at least one new portal commit on the branch; gitlink e85f6eb8 unchanged. A moved gitlink is a hard stop</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~18/AMGT_RESAPP.TO-AMGT-rj-2.drafted-sentences-beside-their-evidence.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json` (the checker compiles `expect` as a REGEX over the evidence), graded by YOUR WORKTREE'S
OWN `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6` (rc 0 is the verdict); keep the build log beside it as
`.txt`; flip `<status>` to `complete`; commit with `--only -- <paths>`. Report once. **If a criterion cannot be met, leave the order
OPEN and file a row.**

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>11</round>
<slot>~18</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<authority>PRD v0.8 @`1170b4da69` (ADMITTED) FWD-9 (the APPLIED bar) and C-FILINGS-ANALYZER's reader clause; `1.0.0_SA_CTO~W`'s L10 round-10 analysis @`8d5fe78265` s.6 item 1; the slug REMEDIATION_v10 @`e28f0b546c` row `AMGT_RESAPP-Z-C-S196`; the CRO's filing-evidence brief @`a65fe406c2` and connection brief @`0f9a04e81e` seam 3; decomposition v1.3 s.19 @`73938cdae4` (cell rj-2, chain A second, after rj-6's drain; consumes D-1). Cell set: s.19a; fan-out: s.19e.</authority>

<preflight>
ALL RUN 2026-09-15 06:4xZ at this cut (decomposition v1.3 s.19g).
comp-schedule: RUN (--drift) -- 5 of 5 carriers within budget (16.0 s of 90); REACHED-DENOMINATORS C1=23, C2=8, C3=12, C4=21, C5=334; C2 = 8 OPEN deploy-ledger entries (none this project's; rj-10 opens one and closes it inside the round); C3 = 12 standing NEVER clauses (no monitor, no alarm); NO new scheduled producer is cut this round (every batch is a local Windows task DISABLED at creation, Andrew's box word @187f003998); BLIND on C4 and C5 in the tool's own voice.
comp-iam: RUN (gaps) -- 838 call(s) verdicted across 98 mapped role(s) over 474 .tf files; 629 UNRESOLVABLE-RESOURCE, 142 GRANTED, 51 GRANTED-BROAD (EXCLUDED, NOT CLEARED), 14 UNGRANTED, 2 GRANTED-ACTION / UNGRANTED-RESOURCE; 15 missing, 291 deny-present, 1 coverage-unknown, 2 resource-mismatch across 32 services; BLIND on 266 calls in 26 role-UNMAPPED services. The round's IAM delta lives in rj-10 alone: READ grants by prefix on opal-data-harvest for two roles, the DynamoDB articles grants REMOVED, no Scan, no wildcard resource; every other cell acts under the operator's own credentials and takes no AWS grant.
comp-adversary: RUN (compose on the decomposition, --no-packet) -- 48 commit pins, 13 repo paths, 17 file:line cites, 14 tool mentions; 23 hex runs not parsed (named); T11 NOT RESOLVED (293 uncited siblings, CAP 25 declared); stage 4 disabled by the caller. The round's adversarial surfaces: filing text, vendor responses and pool objects are DATA inside a model prompt (rj-6, rj-11 say so in the prompt; the verbatim gate runs against the PASSAGE; held-uncited claims never render); Posture is marked machine and read by no trade consumer; the Lusha response is scrubbed to name/title/link; the social job is capped in posts and USD.
comp-cache: RUN (collisions) -- 481 of 481 portal files, 119 of 119 useQuery sites; this cell adds keys under the amgt-lead namespace only and changes no existing key.
comp-blast: DECLARED-NOT-APPLICABLE -- this cell moves nothing on the live plane: its writes are local code, tests and pool objects under the operator's credentials (a QA one-shot is not a production act); the round's one live move is rj-10's, covered by the co-sign.
</preflight>
