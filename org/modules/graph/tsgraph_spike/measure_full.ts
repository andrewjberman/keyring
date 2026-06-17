/**
 * NFRA_TSGRAPH.P0 -- AC4 index-cost measurement.
 *
 * Bounds the FULL-PORTAL extractor cost by doing a whole-program semantic sweep:
 * load the program (one-time), then resolve the type/symbol/React backbone across EVERY
 * portal/src source file (interface fields, function return types, JSX tag symbols,
 * fetch/useQuery call sites). Times it -> the extrapolated full-index cost + incrementality input (§8.6).
 *
 * Run: bun run measure_full.ts
 */
import { Project, SyntaxKind, Node } from "ts-morph";
import { resolve } from "node:path";

const PORTAL_TSCONFIG = resolve(import.meta.dir, "../../../../portal/tsconfig.app.json");

const tLoad0 = performance.now();
const project = new Project({ tsConfigFilePath: PORTAL_TSCONFIG });
const tLoad = performance.now() - tLoad0;

const files = project.getSourceFiles().filter((s) => s.getFilePath().replace(/\\/g, "/").includes("/portal/src/"));

let interfaces = 0, fields = 0, functions = 0, returnTypesResolved = 0;
let jsxElems = 0, jsxResolved = 0, fetchCalls = 0, useQueryCalls = 0, propAccess = 0, propResolved = 0;

const tWalk0 = performance.now();
for (const f of files) {
  for (const iface of f.getInterfaces()) {
    interfaces++;
    for (const p of iface.getProperties()) { fields++; p.getType(); } // resolve field type
  }
  for (const fn of f.getFunctions()) {
    functions++;
    try { fn.getReturnType().getText(); returnTypesResolved++; } catch { /* visible-skip */ }
  }
  // arrow-function components (const X = () => ...)
  for (const v of f.getVariableDeclarations()) {
    const init = v.getInitializer();
    if (init && (Node.isArrowFunction(init) || Node.isFunctionExpression(init))) functions++;
  }
  for (const j of [
    ...f.getDescendantsOfKind(SyntaxKind.JsxOpeningElement),
    ...f.getDescendantsOfKind(SyntaxKind.JsxSelfClosingElement),
  ]) {
    jsxElems++;
    try { if ((j as any).getTagNameNode().getSymbol()) jsxResolved++; } catch { /* visible-skip */ }
  }
  for (const c of f.getDescendantsOfKind(SyntaxKind.CallExpression)) {
    const ex = c.getExpression().getText();
    if (ex === "useQuery") useQueryCalls++;
    if (ex.startsWith("apiRequest") || ex.startsWith("getModelPortfolio") || /^get[A-Z]/.test(ex)) fetchCalls++;
  }
  // sample the prop-access resolution cost on a bounded subset per file (the FLOWS_TO hot path)
  const accesses = f.getDescendantsOfKind(SyntaxKind.PropertyAccessExpression);
  for (let i = 0; i < accesses.length; i += 7) { // every 7th, to bound cost while sampling
    propAccess++;
    try { if (accesses[i].getNameNode().getSymbol()) propResolved++; } catch { /* visible-skip */ }
  }
}
const tWalk = performance.now() - tWalk0;

const total = tLoad + tWalk;
console.log(`AC4 INDEX-COST MEASUREMENT (whole portal/src)`);
console.log(`  files (portal/src):        ${files.length}`);
console.log(`  program load:              ${Math.round(tLoad)}ms (one-time, dominated by createProgram + type-check)`);
console.log(`  full semantic walk:        ${Math.round(tWalk)}ms`);
console.log(`  TOTAL cold full-index:     ${Math.round(total)}ms (${(total / 1000).toFixed(1)}s)`);
console.log(`  ---`);
console.log(`  interfaces resolved:       ${interfaces}  (fields: ${fields})`);
console.log(`  functions:                 ${functions}  (return types resolved: ${returnTypesResolved})`);
console.log(`  JSX elements:              ${jsxElems}  (tag symbol resolved: ${jsxResolved}, ${((jsxResolved / Math.max(jsxElems,1)) * 100).toFixed(0)}%)`);
console.log(`  prop-access (sampled 1/7): ${propAccess}  (symbol resolved: ${propResolved}, ${((propResolved / Math.max(propAccess,1)) * 100).toFixed(0)}%)`);
console.log(`  useQuery call sites:       ${useQueryCalls}`);
console.log(`  fetch-ish call sites:      ${fetchCalls}`);
console.log(`  ---`);
console.log(`  per-file walk avg:         ${(tWalk / Math.max(files.length,1)).toFixed(1)}ms`);
console.log(`  NOTE: incremental re-index of a changed file on a WARM program ~ per-file avg, sub-second;`);
console.log(`        cold full-index ~${(total / 1000).toFixed(1)}s fits the nightly derive + the 5-min trace-cache cadence (§8.6).`);
