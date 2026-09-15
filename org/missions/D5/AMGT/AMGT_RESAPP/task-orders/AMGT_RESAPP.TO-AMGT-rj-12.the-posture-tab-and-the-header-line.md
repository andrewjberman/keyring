# AMGT_RESAPP task order -- `AMGT-rj-12` -- THE POSTURE TAB AND THE HEADER LINE -- a machine's view a person accepts or rejects, beside what it rests on

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rj-12</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~18</issued_to>
<issued_by>2.0.0_SA_COO~W</issued_by>
<placeholders>NONE</placeholders>

**You are `0.9.0_WK_AMGT_RESAPP~18`.** Same worktree, same portal checkout and branch, same rules as `rj-1`, `rj-2` and `rj-9`; this is
the FOURTH order of chain A, handed to you only after `rj-11` (the Posture call) is drained and its two pool objects landed. Every
Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~18;`. **NEVER RUN AN INSTALL.** The `portal` gitlink NEVER moves.

## 1. THE CELL, inlined in full -- `AMGT-rj-12` (FWD-19; C-PAGE-LAYOUT; the rendering half of C-POSTURE)

**THE OUTCOME (PRD v0.8 @`1170b4da69`, FWD-19):** *"The last tab, and a line in the header, say whether this company looks like a better
or a worse pick than the most similar name on the other side ... names that comparable, and gives the reasons with each one linked to
what it rests on. It is marked as a machine's view for a person to accept or reject; it is never an instruction, and nothing is traded
from it."*

**WHAT `rj-11` LANDED (INTERFACE O-1, `posture/v1/{security_key}/{as_of}.json`):** `{verdict: better | worse | hold | steer_clear | absent,
comparable, basis: [{claim, cites: [pack element ids]}], as_of, generation: {run_id, model, usage}, marked: "machine", reason}` for
BABA_US_Equity and the held QA name; rj-9's `/security/{key}/posture` route already serves it (ABSENT when no object) and the header
carries an ABSENT-explicit Posture line; `PostureTab.tsx` is a placeholder.

**DELIVER, in this order:**
1. `PostureTab.tsx`: the verdict in words a person reads ("looks like a BETTER pick than <comparable>", "STEER CLEAR", ...), the
   comparable rendered as a link into its own page (`/security-analysis/<comparable key>`, through the identity's display ticker),
   the `as_of` snapshot date, the machine marker (the round-4 `machine` marker component) prominent, and EVERY basis claim with its
   cites rendered beside it -- each cite resolved to the pack element it names (an evidence record's passage, an officer's name and
   role, a peer's ticker, a figure's label and value, a fit score) by reading the same bundles the other tabs read; an unresolvable
   cite rendered as "cite not resolved" and never dropped; ABSENT-explicit when the object is absent, with the reason when the
   verdict is `absent`.
2. The header line (`LeadPanel.tsx`): one sentence with the verdict and the comparable's display ticker, the same machine marker,
   ABSENT-explicit otherwise; it never renders an instruction.
3. A harness arm (`tabs.harness.cjs` extended or `posture.harness.cjs`): the tab and the header line rendered from the two O-1 objects
   (local copies in the `~20` deliverables), asserting the verdict text, the comparable link href, the marker, every claim with at
   least one resolved cite beside it, the absent arm, and that no element carries a trade action (no `buy`, `sell`, `order` button).

**BOUND:** no install; no vendor call; nothing promoted; no adapter edit needed (rj-9's route serves O-1) -- if one is, it is a row;
no edit under `lib/`.

## 2. WHERE THIS CAME FROM

**ROUND 11**, decomposition v1.3 s.19 @`73938cdae4`, on Andrew-direct ~05:1x-05:2xZ ("Posture ... either sits in the header and/or has a
full tab at the very end"), C-POSTURE and C-PAGE-LAYOUT, the analysis @`8d5fe78265` s.6 item 7.

## 3. SURFACES -- what you may read and write

<paths>
portal/src/pages/SecurityAnalysis/
portal/src/api/endpoints/amgt-lead-panel.ts
lib/research/api/scoped_amgt.py
lib/research/api/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~20/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rj-12.the-posture-tab-and-the-header-line.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL** (RULING 1). The `~20` deliverables are READ-ONLY; `scoped_amgt.py` is in your grant
  only for a route defect you row first.
- **COMMITTING:** as in `rj-1`. Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

PORTAL FROZEN both fabrics: COMMIT YES / PROMOTE NO. No non-ASCII in anything you write. Nothing trades. **THE REFUSAL CLAUSE** and
**SURPRISE ROWS** as in `rj-1`; continue the `W18` sequence.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rj-12"><invocation>python -c "import io; t=io.open('portal/src/pages/SecurityAnalysis/tabs/PostureTab.tsx',encoding='utf-8').read(); l=io.open('portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx',encoding='utf-8').read(); print('tab-verdict-words', sum(t.count(w) for w in ('BETTER','WORSE','HOLD','STEER CLEAR')), 'comparable-link', t.count('/security-analysis/'), 'machine-marker', t.count('machine'), 'cites-rendered', t.count('cite'), 'unresolved-cite-text', t.count('not resolved'), 'absent-explicit', t.count('ABSENT'), 'header-posture-line', l.count('posture'), 'header-marker', l.count('machine'), 'trade-actions', t.count('Buy') + t.count('Sell') + t.count('order'))"</invocation><expect>tab-verdict-words at least 4, comparable-link at least 1, machine-marker at least 1, cites-rendered at least 2, unresolved-cite-text at least 1, absent-explicit at least 1, header-posture-line at least 1, header-marker at least 1, trade-actions 0. A trade action anywhere is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rj-12"><invocation>cd portal && timeout 110 node src/pages/SecurityAnalysis/__harness__/posture.harness.cjs 2>&1 | tail -14; echo rc=$?</invocation><expect>rc=0 and check lines for both O-1 objects: verdict_text_rendered true, comparable_href_present true, marker_present true, claims_rendered N at least 3, claims_with_resolved_cite N (equal), absent_arm_explicit true, header_line_present true, no_trade_action true. A claim rendered without its cite beside it is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rj-12"><invocation>python -c "import json; from lib.research.api import scoped_amgt as s; p=s.read_posture('BABA_US_Equity'); print('route verdict', p.get('verdict'), 'comparable', p.get('comparable'), 'basis', len(p.get('basis') or []), 'marked', p.get('marked')); z=s.read_posture('ZZZ_NOPE_US_Equity'); print('control', z.get('status') or z.get('verdict'))"</invocation><expect>route verdict in the enum with a comparable and basis at least 3 and marked machine (served by rj-9's route from O-1, unchanged by this cell); control ABSENT or absent. A route edit in this cell without a row is NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rj-12"><invocation>cd portal && timeout 110 ./node_modules/.bin/vite build --logLevel info > ../.scratch/rj12.build.txt 2>&1; echo rc=$?; python -c "import glob,os; js=sorted(glob.glob('dist/assets/*.js')); toks={'steer-clear':b'STEER CLEAR','control':b'zzz-no-such-string-rj12-control'}; hits={k:[os.path.basename(f) for f in js if v in open(f,'rb').read()] for k,v in toks.items()}; print('js-assets', len(js)); [print('TOKEN', k, len(v)) for k,v in hits.items()]"; cd .. && git -C portal log --oneline 9aef3734..HEAD | wc -l; echo "gitlink: $(git ls-tree HEAD portal | cut -c13-22)"; for h in errorEmpty.harness.cjs drafting.harness.cjs tabs.harness.cjs; do printf "HARNESS %s: " "$h"; (cd portal && timeout 110 node src/pages/SecurityAnalysis/__harness__/$h 2>&1 | tail -1); done</invocation><expect>rc=0, js-assets above 20, TOKEN steer-clear at least 1, TOKEN control 0; portal commits above 9aef3734 at least 4; gitlink e85f6eb8 unchanged; the three prior harnesses still ending at their met values (the regression control). A moved gitlink is a hard stop</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~18/AMGT_RESAPP.TO-AMGT-rj-12.the-posture-tab-and-the-header-line.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json` (the checker compiles `expect` as a REGEX over the evidence), graded by YOUR WORKTREE'S
OWN `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4` (rc 0 is the verdict); keep the harness output and the build log
beside it as `.txt`; flip `<status>` to `complete`; commit with `--only -- <paths>`. Report once. **If a criterion cannot be met, leave
the order OPEN and file a row.**

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>11</round>
<slot>~18</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<authority>PRD v0.8 @`1170b4da69` (ADMITTED) FWD-19, C-POSTURE, C-PAGE-LAYOUT (Andrew-direct ~05:1x-05:2xZ @`a4f9fd9568`; the voice memo @`fbd5d91431` part five), `1.0.0_SA_CTO~W`'s L10 round-10 analysis @`8d5fe78265` s.6 item 7, decomposition v1.3 s.19 @`73938cdae4` (cell rj-12, chain A fourth, after rj-11's drain; consumes O-1). Cell set: s.19a; fan-out: s.19e.</authority>

<preflight>
ALL RUN 2026-09-15 06:4xZ at this cut (decomposition v1.3 s.19g).
comp-schedule: RUN (--drift) -- 5 of 5 carriers within budget (16.0 s of 90); REACHED-DENOMINATORS C1=23, C2=8, C3=12, C4=21, C5=334; C2 = 8 OPEN deploy-ledger entries (none this project's; rj-10 opens one and closes it inside the round); C3 = 12 standing NEVER clauses (no monitor, no alarm); NO new scheduled producer is cut this round (every batch is a local Windows task DISABLED at creation, Andrew's box word @187f003998); BLIND on C4 and C5 in the tool's own voice.
comp-iam: RUN (gaps) -- 838 call(s) verdicted across 98 mapped role(s) over 474 .tf files; 629 UNRESOLVABLE-RESOURCE, 142 GRANTED, 51 GRANTED-BROAD (EXCLUDED, NOT CLEARED), 14 UNGRANTED, 2 GRANTED-ACTION / UNGRANTED-RESOURCE; 15 missing, 291 deny-present, 1 coverage-unknown, 2 resource-mismatch across 32 services; BLIND on 266 calls in 26 role-UNMAPPED services. The round's IAM delta lives in rj-10 alone: READ grants by prefix on opal-data-harvest for two roles, the DynamoDB articles grants REMOVED, no Scan, no wildcard resource; every other cell acts under the operator's own credentials and takes no AWS grant.
comp-adversary: RUN (compose on the decomposition, --no-packet) -- 48 commit pins, 13 repo paths, 17 file:line cites, 14 tool mentions; 23 hex runs not parsed (named); T11 NOT RESOLVED (293 uncited siblings, CAP 25 declared); stage 4 disabled by the caller. The round's adversarial surfaces: filing text, vendor responses and pool objects are DATA inside a model prompt (rj-6, rj-11 say so in the prompt; the verbatim gate runs against the PASSAGE; held-uncited claims never render); Posture is marked machine and read by no trade consumer; the Lusha response is scrubbed to name/title/link; the social job is capped in posts and USD.
comp-cache: RUN (collisions) -- 481 of 481 portal files, 119 of 119 useQuery sites; this cell adds keys under the amgt-lead namespace only and changes no existing key.
comp-blast: DECLARED-NOT-APPLICABLE -- this cell moves nothing on the live plane: its writes are local code, tests and pool objects under the operator's credentials (a QA one-shot is not a production act); the round's one live move is rj-10's, covered by the co-sign.
</preflight>
