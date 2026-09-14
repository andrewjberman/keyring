const fs=require('fs'),path=require('path'),vm=require('vm'),crypto=require('crypto');
const {createRequire}=require('module');
const base='C:/tmp/wk-amgt-9-1/portal';
const req=createRequire(base+'/package.json');
const ts=req('typescript'),React=req('react'),{renderToStaticMarkup}=req('react-dom/server');
let state;const loaded={};const hashes={};
const box=({children})=>React.createElement('section',null,children);
const noop=()=>{};
function source(rel){
 const file=path.join(base,rel),text=fs.readFileSync(file,'utf8');
 hashes[rel]=crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex');
 const js=ts.transpileModule(text,{compilerOptions:{module:ts.ModuleKind.CommonJS,jsx:ts.JsxEmit.ReactJSX,target:ts.ScriptTarget.ES2022}}).outputText;
 const mod={exports:{}};
 function load(name){
  if(name==='@/ui/components/panels')return {Panel:box,PanelHeader:box,PanelContent:box};
  if(name==='@/ui/components/Select')return {Select:()=>null};
  if(name==='@/hooks/useAuth')return {useAuth:()=>({claims:{firmId:'CVO-OFFLINE-CONTROL'}})};
  if(name==='@/lib/utils')return {cn:(...xs)=>xs.filter(Boolean).join(' ')};
  if(name==='../hooks/useLeadPanelApi')return {
   useLeadPanelRankings:()=>state,useRankTimeSeries:()=>({}),useStarredList:()=>({data:[]}),
   useSetStarred:()=>({mutate:noop}),useRequestRefresh:()=>({mutate:noop}),useSecurityOverlay:()=>({})};
  if(name==='./RankedList')return loaded.ranked;
  if(name==='./RankedChart')return {RankedChart:()=>null};
  if(name==='./StarredList')return {StarredList:()=>null};
  if(name==='./SecurityOverlay')return {SecurityOverlay:()=>null};
  if(name==='../constants')return source('src/pages/SecurityAnalysis/constants.ts');
  return req(name);
 }
 vm.runInThisContext('(function(require,module,exports){'+js+'\n})',{filename:file})(load,mod,mod.exports);
 return mod.exports;
}
loaded.ranked=source('src/pages/SecurityAnalysis/components/RankedList.tsx');
const {LeadPanel}=source('src/pages/SecurityAnalysis/components/LeadPanel.tsx');
const props={movement:'TRENDING',subject:'CHATTER',starredOnly:false,view:'list',selectedSecurityKey:null,searchInput:'',setMovement:noop,setSubject:noop,setStarredOnly:noop,setView:noop,onSelectSecurity:noop,onClearSecuritySelection:noop,setSearchInput:noop};
const cases={
 successful_empty:{data:{rows:[]},isLoading:false,isError:false},
 failed_request:{data:undefined,isLoading:false,isError:true,error:new Error('CVO controlled rejected request')},
 loading:{data:undefined,isLoading:true,isError:false},
 populated:{data:{rows:[{axis:'TRENDING_CHATTER',axis_date:'2026-09-13',ticker:'CVO-CONTROL',rank:1,score:50,raw_chatter_count:2}]},isLoading:false,isError:false}
};
const results={};
for(const [name,s] of Object.entries(cases)){
 state=s;const html=renderToStaticMarkup(React.createElement(LeadPanel,props));
 results[name]={html,bytes:Buffer.byteLength(html),sha256:crypto.createHash('sha256').update(html).digest('hex')};
}
const checks={error_equals_empty:results.failed_request.html===results.successful_empty.html,loading_differs:results.loading.html!==results.successful_empty.html,populated_differs:results.populated.html!==results.successful_empty.html,error_claims_no_daily_row:results.failed_request.html.includes('daily job has not written a row'),populated_names_security:results.populated.html.includes('CVO-CONTROL')};
const out={at:new Date().toISOString(),portal_pin:'a845a8be7522c20ebc3dad896933c5cc84a8f332',method:'Actual LeadPanel and RankedList TypeScript transpiled with installed TypeScript; actual React static rendering; deterministic query-result stubs, layout/auth stubs; no browser, HTTP, credentials, AWS, or source writes',hashes,results,checks,limits:'This proves a frontend error/empty collision, not which response the historical browser received. Fixture names and ranked values are synthetic controls, not live data or FWD realization.'};
fs.writeFileSync('org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND9_CVO_RENDER_20260914_Z.json',JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({checks,cases:Object.fromEntries(Object.entries(results).map(([k,v])=>[k,{bytes:v.bytes,sha256:v.sha256}]))},null,2));
if(Object.values(checks).some(v=>!v))process.exitCode=1;
