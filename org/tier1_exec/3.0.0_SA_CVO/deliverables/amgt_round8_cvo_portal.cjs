// Pinned source, retained installed dependencies, actual React static components.
const fs = require('fs');
const cp = require('child_process');
const vm = require('vm');
const path = require('path').posix;
const crypto = require('crypto');
const {createRequire} = require('module');
const dep = createRequire('C:/tmp/wk-amgt-7-2/portal/package.json');
const ts = dep('typescript');
const React = dep('react');
const {renderToStaticMarkup} = dep('react-dom/server');
const home = __dirname;
const input = JSON.parse(fs.readFileSync(home+'/AMGT_RESAPP_ROUND8_CVO_EVIDENCE_20260913_Z.json','utf8')).input;
const hashes = {};
function source(pin, file) {
  const b = cp.execFileSync('git',['-C','portal','show',pin+':'+file]);
  hashes[pin+':'+file] = crypto.createHash('sha256').update(b).digest('hex');
  return b.toString('utf8');
}
const cache = new Map();
const filesByPin = new Map();
function load(pin,file) {
  const key=pin+':'+file;
  if(cache.has(key)) return cache.get(key).exports;
  const code=ts.transpileModule(source(pin,file),{compilerOptions:{target:ts.ScriptTarget.ES2020,module:ts.ModuleKind.CommonJS,jsx:ts.JsxEmit.ReactJSX}}).outputText;
  const mod={exports:{}}; cache.set(key,mod);
  function req(name) {
    if(name.startsWith('.') || name.startsWith('@/')) {
      const target=name.startsWith('@/')?'src/'+name.slice(2):path.normalize(path.join(path.dirname(file),name));
      if(target==='src/pages/SecurityAnalysis/hooks/useLeadPanelApi') {
        source(pin,target+'.ts');
        return {useThesisBundle:key=>({data:input.thesis[key],isLoading:false})};
      }
      if(!filesByPin.has(pin)) filesByPin.set(pin,new Set(cp.execFileSync('git',['-C','portal','ls-tree','-r','--name-only',pin],{encoding:'utf8'}).trim().split(/\r?\n/)));
      const actual=[target,target+'.ts',target+'.tsx',target+'/index.ts',target+'/index.tsx'].find(f=>filesByPin.get(pin).has(f));
      if(!actual) throw Error('Unresolved pinned module '+target);
      return load(pin,actual);
    }
    return dep(name);
  }
  vm.runInNewContext(code,{module:mod,exports:mod.exports,require:req,console,setTimeout,clearTimeout},{filename:key});
  return mod.exports;
}
const repaired='a845a8be75', before='83cc87f2';
const components={};
for(const pin of [before,repaired]) {
  const chart=load(pin,'src/pages/SecurityAnalysis/components/RankedChart.tsx').RankedChart;
  components[pin]={};
  for(const [name,data] of Object.entries(input.chart)) {
    const html=renderToStaticMarkup(React.createElement(chart,{data,isLoading:false}));
    components[pin][name]={length:Buffer.byteLength(html),sha256:crypto.createHash('sha256').update(html).digest('hex'),html};
  }
}
const fixed=components[repaired], old=components[before];
const checkFor=load(repaired,'src/pages/SecurityAnalysis/figureIdentity.ts').checkFor;
const ProvenanceLine=load(repaired,'src/pages/SecurityAnalysis/components/ProvenanceLine.tsx').ProvenanceLine;
const joins={};
for(const [name,bundle] of Object.entries(input.thesis)) {
  joins[name]={};
  for(const kind of ['header_figures','fiscal_year_figures']) {
    const values=bundle[kind];
    const rendered=values.map(figure=>{const row=checkFor(bundle.check_face,figure);return renderToStaticMarkup(React.createElement(ProvenanceLine,{figure,verdict:row?.verdict,reason:row?.reason}));});
    const pre=figure=>bundle.check_face.find(c=>c.figure_id===(figure.fiscal_year!=null?`fy${figure.fiscal_year}:${figure.mnemonic}`:`header:${figure.mnemonic}`));
    joins[name][kind]={total:values.length,joined:values.filter(f=>checkFor(bundle.check_face,f)).length,pre_joined:values.filter(pre).length,refused:values.filter(f=>checkFor(bundle.check_face,f)?.verdict==='REFUSE').length,html:rendered};
  }
}
const ctrl=input.thesis.BABACVOCTRL_US_Equity;
const html=joins.BABACVOCTRL_US_Equity.fiscal_year_figures.html[0];
const chart=load(repaired,'src/pages/SecurityAnalysis/components/RankedChart.tsx').RankedChart;
const signalFlip=structuredClone(input.chart.exhaust);
signalFlip.read_completeness=structuredClone(input.chart.absent.read_completeness);
for(const s of signalFlip.series) s.unresolved_point_count=0;
const flipped=renderToStaticMarkup(React.createElement(chart,{data:signalFlip,isLoading:false}));
const reading=load(repaired,'src/pages/SecurityAnalysis/readCompleteness.ts').readCompletenessReading(input.chart.exhaust);
const ThesisTab=load(repaired,'src/pages/SecurityAnalysis/tabs/ThesisTab.tsx').ThesisTab;
const thesisRenders=Object.fromEntries(Object.keys(input.thesis).map(key=>[key,renderToStaticMarkup(React.createElement(ThesisTab,{securityKey:key}))]));
const tests={
  old_named_pair_collides:old.absent.html===old.exhaust.html,
  repaired_three_pairs_distinct:new Set([fixed.absent.html,fixed.partial.html,fixed.exhaust.html]).size===3,
  exhausted_denominator_rendered:fixed.exhaust.html.includes(reading.denominatorLine),
  only_signal_changed_switches_to_complete_empty:flipped.includes('data-completeness-state="COMPLETE_EMPTY"') && flipped!==fixed.exhaust.html,
  partial_keeps_chart_caption:fixed.partial.html.includes('Rank over time') && fixed.partial.html.includes('INCOMPLETE READ'),
  fiscal_join_183_of_183:joins.BABA_US_Equity.fiscal_year_figures.joined===183 && joins.BABA_US_Equity.fiscal_year_figures.total===183,
  header_join_13_of_13:joins.BABA_US_Equity.header_figures.joined===13 && joins.BABA_US_Equity.header_figures.total===13,
  old_fiscal_zero:joins.BABA_US_Equity.fiscal_year_figures.pre_joined===0,
  unresolved_joined_and_refused:joins.BABACVOCTRL_US_Equity.fiscal_year_figures.joined===1 && html.includes('[REFUSED:'),
  unresolved_raw_value_absent:!html.includes(String(ctrl.fiscal_year_figures[0].value)),
  pass_header_still_shows_value:joins.BABACVOCTRL_US_Equity.header_figures.html[0].includes(String(ctrl.header_figures[0].value)),
  populated_thesis_renders_196_rows:(thesisRenders.BABA_US_Equity.match(/flex items-baseline gap-2/g)||[]).length===196,
  populated_thesis_control_refuses:thesisRenders.BABACVOCTRL_US_Equity.includes('[REFUSED:') && !thesisRenders.BABACVOCTRL_US_Equity.includes(String(ctrl.fiscal_year_figures[0].value)),
  legend_preserves_producer_series_order:input.chart.partial.series.every((s,i,all)=>i===0 || fixed.partial.html.indexOf(all[i-1].ticker+':')<fixed.partial.html.indexOf(s.ticker+':'))
};
const workerFixture=JSON.parse(source(repaired,'src/pages/SecurityAnalysis/__harness__/rankSeriesCompleteness.json'));
const out={utc:new Date().toISOString(),pin:repaired,prior_pin:before,typescript:ts.version,dependencies:'C:/tmp/wk-amgt-7-2/portal/node_modules; already installed, no install',input_basis:'Fresh actual offline adapter outputs in round8 CVO EVIDENCE, stubbed DynamoDB responses, local model blocks; no served data',components,joins,tests,source_sha256:hashes,worker_chart_fixture:workerFixture,limits:'TranspileModule checks no semantic types. Actual static RankedChart and ProvenanceLine with real React/recharts; no whole-route browser/layout/effects/JWT/PRINT, deployed reads or publication. No worker typecheck gap is filled by transpilation.'};
out.thesisRenders=thesisRenders;
out.thesis_boundary='Actual ThesisTab, actual Panels and ProvenanceLine; only useThesisBundle data boundary supplied offline adapter outputs synchronously. No query transport or effects exercised.';
fs.writeFileSync(home+'/AMGT_RESAPP_ROUND8_CVO_PORTAL_20260913_Z.json',JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({tests,chart:Object.fromEntries(Object.entries(components).map(([pin,cases])=>[pin,Object.fromEntries(Object.entries(cases).map(([n,c])=>[n,{length:c.length,sha256:c.sha256}]))])),provenance:workerFixture._provenance}));
if(Object.values(tests).some(v=>!v)) process.exitCode=1;
