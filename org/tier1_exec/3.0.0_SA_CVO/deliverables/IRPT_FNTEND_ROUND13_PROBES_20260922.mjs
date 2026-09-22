import { createRequire } from 'node:module';
import { readFileSync, mkdirSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';
const root=process.cwd(), portal=resolve(root,'portal');
const require=createRequire(resolve(portal,'package.json'));
const {chromium}=require('playwright-core');
const out=resolve(root,'.runtime/codex-seats/3.0.0_SA_CVO~F/r13-browser'); mkdirSync(out,{recursive:true});
const origin='http://127.0.0.1:5995';
const results={};
function save(){writeFileSync(resolve(out,'measurements.json'),JSON.stringify(results,null,2));}
async function closePage(page){save();await Promise.race([page.close(),new Promise(resolve=>setTimeout(resolve,3000))]);}
console.log('LAUNCH');const browser=await chromium.launch({channel:'msedge',headless:true,timeout:30000});console.log('LAUNCHED');
async function open(fixture,width=1440){
 const map=JSON.parse(readFileSync(resolve(portal,fixture),'utf8'));
 const page=await browser.newPage({viewport:{width,height:900}});page.setDefaultTimeout(15000);
 const served=new Set(); const keys=Object.keys(map).sort((a,b)=>b.length-a.length);
 await page.route('**/*',r=>{
  const url=r.request().url(); const headers={'Access-Control-Allow-Origin':origin,'Access-Control-Allow-Credentials':'true','Access-Control-Allow-Headers':'*','Access-Control-Allow-Methods':'*','Content-Type':'application/json'};
  if(r.request().method()==='OPTIONS')return r.fulfill({status:204,headers,body:''});
  const key=keys.find(k=>url.includes(k));
  if(key){served.add(key);return r.fulfill({status:200,headers,body:JSON.stringify(map[key])});}
  if(url.includes('/auth/refresh'))return r.fulfill({status:200,headers,body:JSON.stringify({accessToken:'cvo-r13-fixture-only',user:{email:'dev@opalcapital.com',name:'Dev User',role:'admin',userType:'Dev',firmId:'opal-capital',firmRole:null,advisorId:null,advisorRole:null,mustChangePassword:false}})});
  return url.startsWith(origin)&&!new URL(url).pathname.startsWith('/api/')?r.continue():r.abort();
 });
 console.log('OPEN',fixture);await page.goto(origin+'/investor-reporting',{waitUntil:'networkidle',timeout:45000});console.log('LOADED',page.url());
 await page.waitForTimeout(1600);
 return {page,served,keys};
}
async function styles(page,selector){return page.locator(selector).first().evaluate(el=>{
 const s=getComputedStyle(el);let p=el,effectiveOpacity=1;const ancestors=[];
 while(p){const ps=getComputedStyle(p);effectiveOpacity*=Number(ps.opacity);if(ps.backgroundColor!=='rgba(0, 0, 0, 0)')ancestors.push({tag:p.tagName,slot:p.getAttribute('data-slot'),background:ps.backgroundColor});p=p.parentElement;}
 return {text:el.textContent,colour:s.color,weight:s.fontWeight,decoration:s.textDecorationLine,background:s.backgroundColor,border:s.borderColor,shadow:s.boxShadow,focusVisible:el.matches(':focus-visible'),effectiveOpacity,ancestors};
});}
try{
 const h=await open('src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json'); const p=h.page;
 await p.getByRole('button',{name:'Holdings',exact:true}).or(p.getByRole('tab',{name:'Holdings',exact:true})).first().click();await p.waitForTimeout(1200);console.log('HOLDINGS');
 const label=p.locator('[data-slot="view-breakdown-link"]').first(),tile=label.locator('xpath=ancestor::button[1]');
 results.linkRest=await styles(p,'[data-slot="view-breakdown-link"]');
 await tile.hover();await p.waitForTimeout(500);results.linkHover=await styles(p,'[data-slot="view-breakdown-link"]');
 await p.mouse.move(1,1);await p.waitForTimeout(500);
 // A real keyboard Tab changes modality; focusing the actual tile then exercises :focus-visible.
 await p.keyboard.press('Tab');await tile.focus();await p.waitForTimeout(500);
 results.linkKeyboard=await styles(p,'[data-slot="view-breakdown-link"]');
 results.tileKeyboard=await tile.evaluate(el=>({focusVisible:el.matches(':focus-visible'),shadow:getComputedStyle(el).boxShadow,outline:getComputedStyle(el).outline}));
 await tile.screenshot({path:resolve(out,'keyboard-tile.png')});
 await p.keyboard.press('Tab');await p.waitForTimeout(500);results.linkBlur=await styles(p,'[data-slot="view-breakdown-link"]');
 await p.locator('[data-slot="slice-row"]').filter({hasText:'Models'}).first().click();await p.waitForTimeout(500);
 results.breadcrumbCurrent=await styles(p,'span[data-slot="holdings-breadcrumb"]');
 results.breadcrumbAncestor=await styles(p,'button[data-slot="holdings-breadcrumb"]');
 results.holdingsWire={matched:h.served.size,declared:h.keys.length};await closePage(p);
 for(const [name,fixture] of [['complete','src/pages/InvestorReporting/fixtures/smoke/reporting-answer-bearing.json'],['qualified','src/pages/InvestorReporting/__tests__/fe-s-84/fixtures/reporting-qualified.json']]){
  const x=await open(fixture);const page=x.page;
  results[name]=await styles(page,'[data-slot="answer-status"]');results[name+'State']=await styles(page,'[data-slot="answer-state"]');
  if(name==='qualified')results.qualifier=await styles(page,'[data-slot="answer-qualifier"]');
  await page.locator('[data-slot="answer-status"]').screenshot({path:resolve(out,name+'-status.png')});
  results[name+'Wire']={matched:x.served.size,declared:x.keys.length};await closePage(page);
 }
}catch(e){results.error=String(e);for(const page of browser.contexts().flatMap(c=>c.pages())){await page.screenshot({path:resolve(out,'error.png')}).catch(()=>{});}throw e;}finally{writeFileSync(resolve(out,'measurements.json'),JSON.stringify(results,null,2));console.log(JSON.stringify(results,null,2));const closeTimer=setTimeout(()=>{console.error('BROWSER_CLOSE_TIMEOUT: measurements retained');process.exit(2);},15000);await browser.close();clearTimeout(closeTimer);}
