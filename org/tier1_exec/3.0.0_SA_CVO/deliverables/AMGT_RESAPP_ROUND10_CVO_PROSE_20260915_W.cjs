// Controlled offline render of the actual ThesisTab. No network or source writes.
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const crypto = require('crypto');
const { createRequire } = require('module');
const base = 'C:/tmp/portal-resapp-view';
const req = createRequire(path.join(base, 'package.json'));
const ts = req('typescript');
const React = req('react');
const {renderToStaticMarkup} = req('react-dom/server');
const file = path.join(base, 'src/pages/SecurityAnalysis/tabs/ThesisTab.tsx');
const source = fs.readFileSync(file, 'utf8');
let bundle;
const box = ({children}) => React.createElement('section', null, children);
const js = ts.transpileModule(source, {compilerOptions:{module:ts.ModuleKind.CommonJS,jsx:ts.JsxEmit.ReactJSX,target:ts.ScriptTarget.ES2022}}).outputText;
const mod = {exports:{}};
function load(name) {
  if (name === '@/ui/components/panels') return {Panel:box,PanelHeader:box,PanelContent:box};
  if (name === '../hooks/useLeadPanelApi') return {useThesisBundle:()=>({data:bundle,isLoading:false})};
  if (name === '../components/ProvenanceLine') return {ProvenanceLine:()=>null};
  if (name === '../figureIdentity') return {checkFor:()=>null};
  return req(name);
}
vm.runInThisContext('(function(require,module,exports){'+js+'\n})',{filename:file})(load,mod,mod.exports);
const result={instrument:'Actual ThesisTab through installed TypeScript and react-dom/server; query, panel layout and unused figure children stubbed. Synthetic prose only. No browser, HTTP, model, vendor, or live evidence.',source_sha256:crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex'),cases:{}};
for (const [name,sentences] of Object.entries({generated:[{text:'CVO_SYNTHETIC_SENTENCE',generated:true,evidence:'CVO_EVIDENCE_SENTINEL'}],firm:[{text:'CVO_SYNTHETIC_SENTENCE',generated:false,evidence:'CVO_EVIDENCE_SENTINEL'}],empty:[]})) {
  bundle={header_figures:[],fiscal_year_figures:[],check_face:[],drafted_sections:[{section_id:'control',label:'Control',sentences}]};
  const html=renderToStaticMarkup(React.createElement(mod.exports.ThesisTab,{securityKey:'CVO_SYNTHETIC_KEY'}));
  const visible=html.replace(/<[^>]*>/g,'');
  result.cases[name]={html,visible,machine_visible:visible.includes('machine'),sentence_visible:visible.includes('CVO_SYNTHETIC_SENTENCE'),evidence_visible:visible.includes('CVO_EVIDENCE_SENTINEL'),evidence_title:html.includes('title="Evidence: CVO_EVIDENCE_SENTINEL"')};
}
console.log(JSON.stringify(result,null,2));
