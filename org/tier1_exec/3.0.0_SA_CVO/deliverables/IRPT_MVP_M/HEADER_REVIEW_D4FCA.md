# Independent bounded header and selection review

**archetype:** VALIDATE

Reviewer: `3.0.0_SA_CVO~M`. Date: 2026-09-22.

**Bounded PASS for the exercised mounted selection/header behavior at portal `d4fca0e5692730e9f79c3fa013159ffa63ba5b6b`.** This is a controlled-API browser review, not composed browser-to-guarded-backend or three-firm/live acceptance. Full M1/M3/M5 and S1/S2/S5/S7 are not closed by this result. Integration remains with the implementation owner; no source or shared portal integration by this CVO.

Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`. Request: exact COO~M message `20260922T223930Z_2.0.0_SA_COO_M_IRPT_M_header_candidate_d4fca0e5_on_P_ty.md`; ACK delivered before review. The request to test/integrate is applied within the contract's independent-review role: CVO grades; the designated owner integrates.

## Pins and isolation

- Isolated reviewer checkout: `C:/Users/AndrewBerman/Desktop/ajb_irpt_cvo_m_portal_review`, detached at exact candidate, tracked and untracked status clean after tests. Implementer's checkout was not used as the running test source.
- Candidate parent chain: `d4fca0e5692730e9f79c3fa013159ffa63ba5b6b` -> `e001b6d59ed08522d6ba98a4fa5a6b695bb065eb` -> `e2df1c04a26028516559b72a0f0b62842867497f` -> final F `8e6e2e38cc299c4415d42b0fe627edc50ec35e1b`.
- Consumed P `e001b6d5` and original `61983ce9` have identical stable patch ID `52ba1fae777440334711cf78a983d20d2685f9f1`. Do not duplicate that cherry-pick during owner integration.
- Unit schema/route inputs extracted from immutable backend `3c14153eeb3b41ac3c7dbcd5c35cc5b969b28c83` with `git archive`, into reviewer runtime. `IRPT_CONTRACTS_DIR` points to that extraction, not the mutable producer checkout.
- `bun install --frozen-lockfile --ignore-scripts` completed rc0, 377 packages in 159.29 seconds. Bun 1.3.9; browser drivers ran with Node 26.9.0 and installed headless Microsoft Edge. Dedicated reviewer Vite used `127.0.0.1:5448`, separate from the producer's 5440 server.
- Push state LOCAL; no push by this seat. Measured portal `origin/DEV` at review end: `b3d5f59b4534eb653105f9bedc9e178384111c9f` (local remote-tracking ref, no fetch performed).

## Actual verification

| Instrument | Result and scope |
|---|---|
| Typecheck discrimination | Temporary isolated `src/cvo_typecheck_negative.ts` assigned a string to a number. `bun run typecheck` refused TS2322, rc2. Exact temporary file removed before positive build. |
| `bun run build` | rc0, actual `tsc -b` then Vite production build; 3,462 modules, Vite build 18.38s. Three CSS BadUrl warnings, dynamic/static import warnings, stale Browserslist notice and oversized chunk warning retained; not warning-free. |
| `bun test ./src/pages/InvestorReporting/__tests__/mvp-selection/selection.test.ts ./src/pages/InvestorReporting/__tests__/m-selection/selectionRequest.test.ts` | 11 pass, zero fail, 25 expectations across two files, 1.69s; schemas/routes from the immutable backend extraction above. |
| Supplied mounted `header-race.mjs` | PASS, zero page errors: acceptance gating, whole-client request, retained ID distinct from fingerprint, changed-selection clear, late resolve suppression, keyed context reset and refusal. |
| Supplied mounted `holdings-race.mjs` | PASS, zero page errors: synchronous A->B/null clear, late C cannot replace D, date/root identity changes, request failure leaves no holdings body. |
| Independent extended mounted driver below | 17 checks pass, zero page errors. Uses actual SelectionWorkspace/ClientSearch/TabShell/tab components and controlled API; mutates only harness rows and scope. External and API HTTP requests blocked by reviewer routing. |

Independent extension specifically exercised: no initial custody/provider calls; Analysis mounts without a custody selection (not proof that prospect submission succeeds); orphan-account selection submits its account despite an empty permitted intersection; whole relationship submits its identity despite an empty permitted intersection; selected fingerprint and retained ID stay distinct; accepted directory revision supplies cache context; inactive reporting is not called; changed selection hides old holdings; a late rejection from the prior relationship cannot replace the current answer or add its error; switching to Reporting uses the current retained ID and real date bounds rather than synthetic 1970 preload; switching does not prefetch inactive holdings; pending and rejected new selections expose neither old reporting nor holdings content.

The supplied scripts were independently rerun, which is repetition of producer instruments. The additional driver changes the population and failure controls: actual account/relationship rows with an empty permitted list, late rejection after a newer accepted selection, and active/inactive tab switching. It still shares the producer's fixture scaffold and does not constitute an independent live backend instrument.

Initial reviewer harness attempt timed out before mount: it fulfilled the raw HTML fixture and bypassed Vite's import transformation. Corrected to fetch Vite-transformed HTML and expose only harness API/rows/scope. The corrected run passes. This harness correction changed no candidate source and the initial timeout is not graded as a candidate failure.

## Limits and handoff

The controlled API substitutes methods; it does not exercise browser HTTP serialization and a real guarded entry in one composed run. Supplied API/parser tests separately exercise LiveClient, not that composition. No current-access revocation during an actual backend request, provider egress, three-firm custody/source correctness, real prospect submit/recovery, report/export lifecycle, deployment or full S7 acceptance is established. Source adapter work remains open with COO~M. Header export anchors are absent by design in this candidate; actual report identity/export wiring remains a separate product obligation.

Attributed peer evidence: CVO~P exact `20260922T224230Z_3.0.0_SA_CVO_P_IRPT_P__shared_selection_API_bounded_PAS.md` reports API/parser review `8a94798594` on portal `61983ce9` / backend `c5eace08c7`, supplied7 plus independent16 PASS, fixture capture reused, no mounted UI/HTTP guard composition. This is attributed, not independently rerun as P's sixteen-case instrument here.

Screenshot `.runtime/codex-seats/3.0.0_SA_CVO~M/header_d4_review.png` was opened: explicit authorization refusal and selection-required state are visible, and no custody/report body remains. SHA256 `C13F1E1D87FCC66345DE929B04684F758F7B9B6B8E3740A8A11087F587517EE8`. This standalone fixture page is not the full authenticated app shell or a full DESIGN.md visual acceptance.

Return the bounded review pin to COO~M, CTO and CVO~P. No shared-source integration, activation or release permission is implied. Compiler routing used bare comp-which/comp-read before contextual reads, followed by exact Git source and tests. Documentation-only diff checks do not replace runtime proof; stale compiler risk-map output cannot clear the change.

## Reproduction driver

Save the script below as `header_d4_review.mjs` under the review runtime. Start the exact checkout with `bun run dev --host 127.0.0.1 --port 5448 --strictPort`; run `node <driver> <absolute-screenshot-path>`. The installed `playwright-core` package resolves from the existing user environment. Script SHA256: `60AC3FA440F7655A26C8434AE2A4C0B6BB52D4282A86B08D63283966ADB601B0`. Raw result JSON and screenshot are in the same runtime directory. The driver is embedded for durable reproduction.

```javascript
import {chromium} from 'playwright-core';
import assert from 'node:assert/strict';
import fs from 'node:fs';
const root='C:/Users/AndrewBerman/Desktop/ajb_irpt_cvo_m_portal_review';
const origin='http://127.0.0.1:5448';
const fixture='/src/pages/InvestorReporting/__tests__/m-selection/header-race.html';
const original=fs.readFileSync(root+fixture,'utf8');
const html=original.replace('window.exercise = {','window.audit = {api, entries, scope};\nwindow.exercise = {');
const browser=await chromium.launch({executablePath:'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',headless:true});
const results=[];
try {
 const page=await browser.newPage();
 const errors=[]; page.on('pageerror',e=>errors.push(e.message));
 await page.route('**/*',async route=>{
  const url=new URL(route.request().url());
  if(url.origin!==origin || /^\/(api|auth|v1)\//.test(url.pathname)) return route.abort();
  if(url.pathname===fixture) {
    const response=await route.fetch();
    const transformed=await response.text();
    return route.fulfill({response,body:transformed.replace('window.exercise = {','window.audit = {api, entries, scope};\nwindow.exercise = {')});
  }
  return route.continue();
 });
 const check=(name,condition)=>{assert.ok(condition,name);results.push(name);console.error('PASS: '+name);};
 await page.goto(origin+fixture);
 await page.waitForSelector('[data-slot="selection-required"]');
 check('initial no selection means zero custody/provider calls',(await page.evaluate(()=>window.exercise.calls.length))===0);
 await page.getByRole('button',{name:'Analysis',exact:true}).click();
 await page.waitForSelector('[data-slot="analysis-tab"]');
 check('analysis available without custody selection',(await page.evaluate(()=>window.exercise.calls.length))===0);
 await page.getByRole('button',{name:'Holdings',exact:true}).click();
 await page.evaluate(()=>{
   const {entries,scope}=window.audit;
   entries[0]={...entries[0],kind:'account',accountId:'account-orphan',clientId:null,relationshipId:null};
   entries[1]={...entries[1],kind:'relationship',accountId:null,clientId:null,relationshipId:'relationship-Beta'};
   scope.permittedAccountIds=[];
   const old=window.exercise.resolve;
   window.exercise.resolve=(id,token)=>old(id,token);
 });
 const choose=async name=>{
  await page.getByRole('combobox',{name:'Client search'}).fill(name);
  await page.getByRole('option').filter({hasText:name}).click();
 };
 await choose('Alpha');
 await page.waitForFunction(()=>window.exercise.pending('account-orphan'));
 assert.deepEqual(await page.evaluate(()=>window.exercise.calls.at(-1).request),{scope_kind:'ACCOUNT',scope_ids:['account-orphan']});
 check('orphan account row submits exact account despite empty permitted intersection',true);
 await page.evaluate(()=>window.exercise.resolve('account-orphan','a'));
 await page.waitForSelector('[data-slot="holdings-tab"]');
 const first=await page.evaluate(()=>window.exercise.calls.find(c=>c.kind==='holdings').request);
 check('selected fingerprint never replaced by permitted fingerprint',first.scopeFingerprint==='selected-a');
 check('accepted retained ID used by holdings',first.accountSetId==='sel_'+'a'.repeat(64));
 check('accepted directory revision used as cache context',first.revision==='directory-accepted');
 check('inactive reporting provider never called',(await page.evaluate(()=>window.exercise.calls.filter(c=>c.kind==='performance').length))===0);
 await choose('Beta');
 await page.waitForFunction(()=>window.exercise.pending('relationship-Beta'));
 assert.deepEqual(await page.evaluate(()=>window.exercise.calls.at(-1).request),{scope_kind:'RELATIONSHIP',scope_ids:['relationship-Beta']});
 check('whole relationship submitted despite zero permitted intersection',true);
 check('old holdings removed while relationship acceptance pending',await page.locator('[data-slot="holdings-tab"]').count()===0);
 await choose('Gamma');
 await page.waitForFunction(()=>window.exercise.pending('client-Gamma'));
 await page.evaluate(()=>window.exercise.resolve('client-Gamma','c'));
 await page.waitForSelector('[data-slot="holdings-tab"]');
 await page.evaluate(()=>window.exercise.reject('relationship-Beta'));
 await page.waitForTimeout(80);
 check('late prior rejection does not replace current accepted answer',await page.locator('[data-slot="holdings-tab"]').count()===1);
 check('late prior rejection does not display current authorization error',await page.getByText('This selection could not be authorized. Search and select it again.').count()===0);
 const before=await page.evaluate(()=>window.exercise.calls.filter(c=>c.kind==='holdings').length);
 await page.getByRole('button',{name:'Reporting',exact:true}).click();
 await page.waitForFunction(()=>window.exercise.calls.some(c=>c.kind==='performance'));
 const perf=await page.evaluate(()=>window.exercise.calls.find(c=>c.kind==='performance').request);
 check('active reporting receives retained selection identity',perf.accountSetId==='sel_'+'c'.repeat(64));
 check('reporting dates present and no synthetic 1970 preload',!!perf.start&&!!perf.end&&!perf.start.startsWith('1970')&&!perf.end.startsWith('1970'));
 check('switching to reporting does not prefetch inactive holdings',(await page.evaluate(()=>window.exercise.calls.filter(c=>c.kind==='holdings').length))===before);
 await choose('Beta');
 await page.waitForFunction(()=>window.exercise.pending('relationship-Beta'));
 check('reporting unmounted while changed selection awaits authorization',await page.locator('[data-slot="reporting-tab"]').count()===0);
 await page.evaluate(()=>window.exercise.reject('relationship-Beta'));
 await page.getByText('This selection could not be authorized. Search and select it again.').waitFor();
 check('rejected selection exposes neither reporting nor holdings body',await page.locator('[data-slot="reporting-body"],[data-slot="holdings-tab"]').count()===0);
 await page.screenshot({path:process.argv[2],fullPage:true});
 assert.deepEqual(errors,[]);results.push('zero page errors');
 console.log(JSON.stringify({candidate:'d4fca0e5692730e9f79c3fa013159ffa63ba5b6b',passed:results.length,results,errors},null,2));
} finally {await browser.close();}

```
