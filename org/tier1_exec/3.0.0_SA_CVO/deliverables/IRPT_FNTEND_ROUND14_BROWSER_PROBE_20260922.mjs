// Fixture-fed CVO probe; all unmatched API/external traffic blocked. Run from workspace.
import {createRequire} from 'node:module';
import {readFileSync,mkdirSync,writeFileSync} from 'node:fs';
import {resolve} from 'node:path';
const root=process.cwd(),portal=resolve(root,'portal'),require=createRequire(resolve(portal,'package.json'));
const {chromium}=require('playwright-core');
const answer=process.argv[2]==='answer';
const out=resolve(root,'.runtime/codex-seats/3.0.0_SA_CVO~F/r14-browser'+(answer?'-answer':''));mkdirSync(out,{recursive:true});
const origin='http://localhost:6020',results={};
const token=Buffer.from(JSON.stringify({aud:'irpt-render',role:'renderer',firmId:'49financial'})).toString('base64url');
const queryToken='e30.'+token+'.synthetic';
const save=()=>writeFileSync(resolve(out,'measurements.json'),JSON.stringify(results,null,2));
const browser=await chromium.launch({channel:'msedge',headless:true});
async function open(fixture,path='/investor-reporting',auth='admin'){
 const map=JSON.parse(readFileSync(resolve(portal,fixture),'utf8')),served=new Set(),keys=Object.keys(map).sort((a,b)=>b.length-a.length);
 const page=await browser.newPage({viewport:{width:1440,height:900}});page.setDefaultTimeout(15000);
 await page.route('**/*',r=>{
  const url=r.request().url(),headers={'Access-Control-Allow-Origin':origin,'Access-Control-Allow-Credentials':'true','Access-Control-Allow-Headers':'*','Access-Control-Allow-Methods':'*','Content-Type':'application/json'};
  if(r.request().method()==='OPTIONS')return r.fulfill({status:204,headers,body:''});
  const key=keys.find(k=>url.includes(k));if(key){served.add(key);return r.fulfill({status:200,headers,body:JSON.stringify(map[key])});}
  if(url.includes('/auth/refresh'))return r.fulfill({status:auth==='none'?401:200,headers,body:JSON.stringify(auth==='none'?{error:'unauthenticated'}:{accessToken:'fixture-only',user:{email:'cvo@test.invalid',name:'CVO',role:auth==='admin'?'admin':'user',firmId:auth==='admin'?'opal-capital':'49financial',userType:null,advisorId:null,firmRole:null,advisorRole:null,mustChangePassword:false}})});
  return url.startsWith(origin)&&!new URL(url).pathname.startsWith('/api/')?r.continue():r.abort();
 });
 await page.goto(origin+path,{waitUntil:'networkidle',timeout:60000});await page.waitForTimeout(1500);
 return {page,wire:()=>({matched:served.size,total:keys.length,keys:[...served]})};
}
const slot=x=>'[data-slot="'+x+'"]';
async function style(page,name){return page.locator(slot(name)).evaluateAll(els=>els.map(el=>({text:el.textContent,weight:getComputedStyle(el).fontWeight,background:getComputedStyle(el).backgroundColor})));}
try{
 for(const [name,fixture] of (answer?[]:[['ready','src/pages/InvestorReporting/fixtures/smoke/reporting-answer-bearing.json'],['partial','src/pages/InvestorReporting/__tests__/fe-s-84/fixtures/reporting-qualified.json']])){
  const x=await open(fixture),p=x.page;
  results[name]={state:await style(p,'answer-state'),qualifier:await style(p,'answer-qualifier'),ground:await style(p,'answer-status'),wire:x.wire()};
  await p.locator(slot('answer-status')).screenshot({path:resolve(out,name+'.png')});
  if(name==='ready'){await p.addStyleTag({content:slot('answer-status')+'{background-color:#c4cbdb !important}'});results.wrongGround=await style(p,'answer-status');await p.locator(slot('answer-status')).screenshot({path:resolve(out,'wrong-ground.png')});}
  save();await p.close();
 }
 const fixture=answer?'src/pages/InvestorReporting/fixtures/smoke/reporting-answer-bearing.json':'src/pages/InvestorReporting/fixtures/smoke/fe-s-14-print-v1.json';
 const base='/investor-reporting/print?bundle=report-1&tenant=49financial&scope=scope-1&revision=revision-1';
 for(const [name,path,auth] of [['renderPrint',base+'&renderToken='+queryToken,'none'],['noToken',base,'none'],['renderNonPrint','/investor-reporting?renderToken='+queryToken,'none'],['humanAdmin',base,'admin'],['humanAdvisor',base,'advisor']]){
  const x=await open(fixture,path,auth),p=x.page;
  results[name]={url:p.url(),printStates:await p.locator('[data-print-state]').evaluateAll(es=>es.map(e=>({state:e.getAttribute('data-print-state'),text:e.textContent.slice(0,1500)}))),body:(await p.locator('body').innerText()).slice(0,1600),wire:x.wire()};
  await p.screenshot({path:resolve(out,name+'.png')});save();await p.close();
 }
}catch(e){results.error=String(e);throw e;}finally{save();console.log(JSON.stringify(results,null,2));const timer=setTimeout(()=>{console.error('CLOSE_TIMEOUT: evidence retained');process.exit(2);},10000);await browser.close();clearTimeout(timer);}
