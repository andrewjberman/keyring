// Executes pinned source with already-installed dependencies; no checkout or install.
const fs = require('fs');
const cp = require('child_process');
const vm = require('vm');
const {createRequire} = require('module');
const dep = createRequire('C:/tmp/wk-amgt-7-2/portal/package.json');
const ts = dep('typescript');
const React = dep('react');
const {renderToStaticMarkup} = dep('react-dom/server');
const input = JSON.parse(fs.readFileSync(0, 'utf8'));
function source(path) {return cp.execFileSync('git',['-C','portal','show','83cc87f2:'+path],{encoding:'utf8'});}
function compile(text) {return ts.transpileModule(text,{compilerOptions:{target:ts.ScriptTarget.ES2020,module:ts.ModuleKind.CommonJS,jsx:ts.JsxEmit.ReactJSX}}).outputText;}
const chartSource = source('src/pages/SecurityAnalysis/components/RankedChart.tsx');
const chartContext = {exports:{}, require:dep};
vm.runInNewContext(compile(chartSource), chartContext);
const chart = {};
for (const [name,data] of Object.entries(input.chart)) {
  chart[name] = renderToStaticMarkup(React.createElement(chartContext.exports.RankedChart,{data,isLoading:false}));
}
const thesisSource = source('src/pages/SecurityAnalysis/tabs/ThesisTab.tsx');
const ast = ts.createSourceFile('ThesisTab.tsx', thesisSource,ts.ScriptTarget.Latest,true,ts.ScriptKind.TSX);
const check = ast.statements.find(n=>ts.isFunctionDeclaration(n)&&n.name.text==='checkFor');
if (!check) throw Error('Actual checkFor function absent');
const ctx = {};
vm.runInNewContext(compile(check.getText(ast)),ctx);
const joins = {};
for (const [key,bundle] of Object.entries(input.thesis)) {
  joins[key] = {};
  for (const kind of ['header_figures','fiscal_year_figures']) {
    const matches = bundle[kind].map(f=>ctx.checkFor(bundle.check_face,f));
    joins[key][kind] = {figures:matches.length,matched:matches.filter(Boolean).length,refused:matches.filter(x=>x?.verdict==='REFUSE').length};
  }
  joins[key].actual_check_ids = bundle.check_face.slice(0,3).map(x=>x.figure_id);
  joins[key].fiscal_check_ids = bundle.check_face.filter(x=>x.figure_id.startsWith('fiscal_year_line_item:PX_LAST')).map(x=>x.figure_id);
}
const figure={fiscal_year:2025,mnemonic:'PX_LAST'};
const controls={positive:ctx.checkFor([{figure_id:'fy2025:PX_LAST',verdict:'REFUSE'}],figure),negative:ctx.checkFor([],figure)??null};
process.stdout.write(JSON.stringify({pin:'83cc87f2',typescript:ts.version,chart,chart_absent_equals_exhaust:chart.absent===chart.exhaust,checkFor_source:check.getText(ast),joins,controls,limits:'Actual RankedChart static server render; actual extracted checkFor executed against adapter output. No browser layout, deployed transport, source edits or dependency install.'}));
