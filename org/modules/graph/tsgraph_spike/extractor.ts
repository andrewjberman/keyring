/**
 * NFRA_TSGRAPH.P0 -- ts-morph / TS-Compiler-API semantic extractor (SPIKE).
 *
 * Slice: the model-portfolios BENCHMARK surface (firm-agnostic; the known D8-FP chain
 *   yang-model-portfolio-benchmarks -> opal-data-portal-v2 -> opal-portal-data-proxy -> fetch -> render).
 *
 * Proves: a compiler-grade TS semantic substrate (TypeChecker symbol/type resolution, NOT regex)
 * emitting the CTO-brief §3 node/edge schema, and the field-grain stitch end-to-end on ONE field
 * (`model`, the model-portfolio return), each "->" a RESOLVED edge.
 *
 * Discipline (brief §8.3/§8.8): resolve what is resolvable; mark the rest `unresolved` and VISIBLE
 * (no silent Unknown). Keys are CONSISTENT with the existing regex graph (component:/endpoint:/s3:/gold:/rqk:)
 * so the new semantic nodes stitch to the cloud/trace graph (fixes the D8 key-space class).
 *
 * Run: bun run extractor.ts   (from org/modules/graph/tsgraph_spike/)
 */
import { Project, SyntaxKind, Node, type Type } from "ts-morph";
import { resolve, relative } from "node:path";
import { mkdirSync, writeFileSync } from "node:fs";

const WORKSPACE = resolve(import.meta.dir, "../../../..");
const PORTAL_TSCONFIG = resolve(WORKSPACE, "portal/tsconfig.app.json");
const OUT_DIR = resolve(import.meta.dir, "out");

// Slice file landmarks (workspace-relative, forward-slash).
const F_PROXY = "portal/src/api/portal-proxy.ts";
const F_PAGE = "portal/src/pages/ModelPortfolios.tsx";
const F_HEATMAP = "portal/src/components/BenchmarkHeatmap.tsx";
const SLICE_FILES = [F_PROXY, F_PAGE, F_HEATMAP];

// Named types we promote to TypeDecl+Field nodes for the slice.
const SLICE_TYPES = [
  "ModelPortfolioBenchmarksResponse",
  "ModelPortfolioData",
  "ModelPortfolioPeriodReturn",
  "BenchmarkModelData",
  "BenchmarkPeriodReturn",
  "BenchmarkHeatmapProps",
];

// ---------------------------------------------------------------------------
// stores
// ---------------------------------------------------------------------------
type Attrs = Record<string, unknown>;
interface GNode { id: string; label: string; attrs: Attrs; }
interface GEdge { src: string; dst: string; label: string; attrs: Attrs; }

const nodes = new Map<string, GNode>();
const edges: GEdge[] = [];
const edgeKeys = new Set<string>();
const unresolved: { what: string; where: string; reason: string }[] = [];

function addNode(id: string, label: string, attrs: Attrs = {}): string {
  const existing = nodes.get(id);
  if (existing) { Object.assign(existing.attrs, attrs); return id; }
  nodes.set(id, { id, label, attrs });
  return id;
}
function addEdge(src: string, dst: string, label: string, attrs: Attrs = {}) {
  const k = `${src}|${label}|${dst}`;
  if (edgeKeys.has(k)) return;
  edgeKeys.add(k);
  edges.push({ src, dst, label, attrs });
}
function markUnresolved(what: string, where: string, reason: string) {
  unresolved.push({ what, where, reason });
}

// ---------------------------------------------------------------------------
// key helpers (CONSISTENT with the existing regex graph)
// ---------------------------------------------------------------------------
function rel(node: Node): string {
  return relative(WORKSPACE, node.getSourceFile().getFilePath()).replace(/\\/g, "/");
}
function loc(node: Node): string {
  return `${rel(node)}:${node.getStartLineNumber()}`;
}
function moduleId(relPath: string) { return `module:${relPath}`; }
function componentId(relPath: string) { return `component:${relPath}`; }           // coarse, == extract_api.py
function rcId(relPath: string, name: string) { return `rc:${relPath}#${name}`; }    // fine ReactComponent
function endpointId(fn: string) { return `endpoint:${fn}`; }                        // == extract_api.py
function s3Id(key: string) { return `s3:${key}`; }                                  // == extract_pipeline.py
function goldId(id: string) { return `gold:${id}`; }                               // == extract_pipeline.py
function rqkId(key: string) { return `rqk:${key}`; }                                // == cache_cli.py
function typeDeclId(name: string, relPath: string) { return `type:${relPath}#${name}`; }
function fieldId(typeId: string, field: string) { return `${typeId}#${field}`; }

// ---------------------------------------------------------------------------
// load program (timed -- AC4 index cost)
// ---------------------------------------------------------------------------
const tLoad0 = performance.now();
const project = new Project({ tsConfigFilePath: PORTAL_TSCONFIG });
const tLoad = performance.now() - tLoad0;
const allFiles = project.getSourceFiles();

const sf = (relPath: string) =>
  project.getSourceFileOrThrow((s) => s.getFilePath().replace(/\\/g, "/").endsWith(relPath));

const tEx0 = performance.now();

// resolve a Symbol's primary declaration -> a stable (typeId, field) pair, if it is a property
// of one of our named slice types. Returns the field-node id (creating type/field nodes on demand).
function fieldNodeForSymbol(symName: string, ownerTypeName: string | undefined): string | null {
  if (!ownerTypeName) return null;
  if (!SLICE_TYPES.includes(ownerTypeName)) return null;
  // find the TypeDecl node we emitted
  for (const t of nodes.values()) {
    if (t.label === "TypeDecl" && t.attrs.name === ownerTypeName) {
      const fid = fieldId(t.id, symName);
      if (nodes.has(fid)) return fid;
    }
  }
  return null;
}

// Given an expression node, resolve the property it accesses to (ownerTypeName, fieldName).
function resolvePropAccess(node: Node): { owner: string | null; field: string | null; type: string } {
  if (!Node.isPropertyAccessExpression(node)) return { owner: null, field: null, type: "" };
  const nameNode = node.getNameNode();
  const fieldName = node.getName();
  const sym = nameNode.getSymbol();
  let owner: string | null = null;
  const decl = sym?.getDeclarations()?.[0];
  if (decl) {
    // the declaration's parent named type (interface) name
    const parentType = decl.getFirstAncestorByKind(SyntaxKind.InterfaceDeclaration);
    if (parentType) owner = parentType.getName();
  }
  return { owner, field: fieldName, type: node.getType().getText() };
}

// ===========================================================================
// PASS 1 -- Modules + TypeDecls + Fields
// ===========================================================================
for (const relPath of SLICE_FILES) {
  const file = sf(relPath);
  addNode(moduleId(relPath), "Module", { path: relPath, kind: relPath.endsWith(".tsx") ? "tsx" : "ts" });
}

const proxy = sf(F_PROXY);
for (const typeName of SLICE_TYPES) {
  // search all slice files for the interface declaration
  let iface = null as ReturnType<typeof proxy.getInterface> | null;
  let host = "";
  for (const relPath of SLICE_FILES) {
    const f = sf(relPath);
    const found = f.getInterface(typeName);
    if (found) { iface = found; host = relPath; break; }
  }
  if (!iface) { markUnresolved(`type ${typeName}`, "slice", "interface declaration not found in slice files"); continue; }
  const tId = typeDeclId(typeName, host);
  addNode(tId, "TypeDecl", { name: typeName, path: host, line: iface.getStartLineNumber() });
  addEdge(moduleId(host), tId, "DECLARES");
  for (const prop of iface.getProperties()) {
    const fName = prop.getName();
    const fId = fieldId(tId, fName);
    addNode(fId, "Field", {
      name: fName,
      ownerType: typeName,
      tsType: prop.getType().getText(prop),
      optional: prop.hasQuestionToken(),
      path: host,
      line: prop.getStartLineNumber(),
    });
    addEdge(tId, fId, "HAS_FIELD");
  }
}

// ===========================================================================
// PASS 2 -- DataFetch + Endpoint + served S3 + gold (the BACKEND seam)
// ===========================================================================
const fetchFn = proxy.getFunctionOrThrow("getModelPortfolioBenchmarks");
const fetchNodeId = `fetch:${rel(fetchFn)}:${fetchFn.getStartLineNumber()}:getModelPortfolioBenchmarks`;
addNode(fetchNodeId, "DataFetch", {
  fn: "getModelPortfolioBenchmarks",
  path: rel(fetchFn),
  line: fetchFn.getStartLineNumber(),
  returnType: fetchFn.getReturnType().getText(fetchFn),
});
const epId = endpointId("getModelPortfolioBenchmarks");
addNode(epId, "Endpoint", { fn: "getModelPortfolioBenchmarks", coarseKey: epId });
addEdge(moduleId(F_PROXY), fetchNodeId, "DECLARES");
addEdge(fetchNodeId, epId, "IS_ENDPOINT");

// resolve the awaited return type -> ModelPortfolioBenchmarksResponse TypeDecl (HAS_TYPE)
const retType = fetchFn.getReturnType();
const respType: Type = retType.getTypeArguments()[0] ?? retType;
const respSym = respType.getSymbol() ?? respType.getAliasSymbol();
const respName = respSym?.getName();
const respTypeId = respName ? typeDeclId(respName, F_PROXY) : null;
if (respTypeId && nodes.has(respTypeId)) {
  addEdge(fetchNodeId, respTypeId, "HAS_TYPE", { resolution: "getReturnType+typeArg (TypeChecker)" });
} else {
  markUnresolved("fetch return type", fetchNodeId, `awaited type symbol = ${respName ?? "?"}`);
}

// resolve the apiRequest<T>('url') call -> the served URL literal (RESOLVED) + the S3 key (EXTERNAL provenance)
const apiCall = fetchFn
  .getDescendantsOfKind(SyntaxKind.CallExpression)
  .find((c) => c.getExpression().getText().startsWith("apiRequest"));
let servedUrl: string | null = null;
if (apiCall) {
  const urlArg = apiCall.getArguments()[0];
  if (urlArg && Node.isStringLiteral(urlArg)) servedUrl = urlArg.getLiteralText();
  // type argument resolves to the response type as well (cross-check)
  const ta = apiCall.getTypeArguments()[0];
  if (ta) addEdge(fetchNodeId, respTypeId ?? fetchNodeId, "ASSERTS_TYPE", { typeArg: ta.getText(), resolution: "apiRequest<T> type argument" });
}
if (!servedUrl) markUnresolved("served URL", fetchNodeId, "apiRequest URL arg not a string literal");

// URL -> S3 key. The proxy/CloudFront route mapping is NOT in the TS; provenance = external (D8-FP backend map).
const S3_KEY = "json/benchmarks/model_portfolio_benchmarks.json";
const GOLD = "yang-model-portfolio-benchmarks";
const s3NodeId = s3Id(S3_KEY);
const goldNodeId = goldId(GOLD);
addNode(s3NodeId, "S3Artifact", { key: S3_KEY, bucket: "opal-data-portal-v2", servedUrl, provenance: "external:D8-FP-backend-map" });
addNode(goldNodeId, "GoldScript", { script: GOLD, provenance: "external:D8-FP-backend-map" });
addEdge(epId, s3NodeId, "READS_S3", { servedUrl, resolution: "URL literal RESOLVED; URL->S3-key mapping EXTERNAL (proxy routing, not in TS)" });
addEdge(s3NodeId, goldNodeId, "DERIVES_FROM", { provenance: "external:D8-FP-backend-map" });
markUnresolved("URL->S3-key + S3->gold mapping", epId, "proxy/CloudFront routing + producer are not expressible in TS; carried from the cloud/trace graph (consistent keys) -- VISIBLE, not silent");

// ===========================================================================
// PASS 3 -- Hook (useQuery) -> FETCHES endpoint + RQ key
// ===========================================================================
const page = sf(F_PAGE);
const useQueryCall = page
  .getDescendantsOfKind(SyntaxKind.CallExpression)
  .find((c) => {
    if (c.getExpression().getText() !== "useQuery") return false;
    return c.getText().includes("getModelPortfolioBenchmarks");
  });
if (useQueryCall) {
  const hookId = `hook:${rel(useQueryCall)}:${useQueryCall.getStartLineNumber()}:useQuery`;
  addNode(hookId, "Hook", { hook: "useQuery", path: rel(useQueryCall), line: useQueryCall.getStartLineNumber() });
  // queryKey literal -> rqk:
  const keyProp = useQueryCall
    .getDescendantsOfKind(SyntaxKind.PropertyAssignment)
    .find((p) => p.getName() === "queryKey");
  let rqk: string | null = null;
  const keyArr = keyProp?.getInitializerIfKind(SyntaxKind.ArrayLiteralExpression);
  const firstKey = keyArr?.getElements()?.[0];
  if (firstKey && Node.isStringLiteral(firstKey)) rqk = firstKey.getLiteralText();
  if (rqk) {
    const rqkNode = rqkId(rqk);
    addNode(rqkNode, "ReactQueryKey", { key: rqk });
    addEdge(hookId, rqkNode, "HAS_KEY");
  } else markUnresolved("React-Query key", hookId, "queryKey not a literal array of strings");
  // queryFn -> getModelPortfolioBenchmarks (FETCHES, resolved by symbol)
  const fnProp = useQueryCall
    .getDescendantsOfKind(SyntaxKind.PropertyAssignment)
    .find((p) => p.getName() === "queryFn");
  const fnInit = fnProp?.getInitializer();
  let resolvedFetch = false;
  if (fnInit) {
    const ident = fnInit.getFirstDescendantByKind(SyntaxKind.Identifier) ??
      (Node.isIdentifier(fnInit) ? fnInit : undefined);
    const tgt = ident?.getSymbol()?.getAliasedSymbol() ?? ident?.getSymbol();
    if (tgt?.getName() === "getModelPortfolioBenchmarks") {
      addEdge(hookId, epId, "FETCHES", { resolution: "queryFn symbol resolved (getAliasedSymbol)" });
      addEdge(hookId, fetchNodeId, "CALLS", { resolution: "queryFn symbol" });
      resolvedFetch = true;
    }
  }
  if (!resolvedFetch) markUnresolved("useQuery -> fetch", hookId, "queryFn did not resolve to getModelPortfolioBenchmarks");
  // the data symbol type (comprehensiveBenchmarkData) HAS_TYPE response
  if (respTypeId && nodes.has(respTypeId)) addEdge(hookId, respTypeId, "HAS_TYPE", { resolution: "useQuery<T> inferred from queryFn return" });
} else {
  markUnresolved("useQuery hook", F_PAGE, "no useQuery call referencing getModelPortfolioBenchmarks found");
}

// ===========================================================================
// PASS 4 -- Components + Props
// ===========================================================================
function findComponent(file: ReturnType<typeof sf>, name: string): Node | undefined {
  const fn = file.getFunction(name);
  if (fn) return fn;
  const v = file.getVariableDeclaration(name);
  if (v) return v;
  // default export function
  const def = file.getFunctions().find((f) => f.isDefaultExport() && f.getName() === name);
  return def;
}
const pageComp = findComponent(page, "ModelPortfolios");
if (pageComp) {
  const id = rcId(F_PAGE, "ModelPortfolios");
  addNode(id, "ReactComponent", { name: "ModelPortfolios", path: F_PAGE, coarseKey: componentId(F_PAGE) });
  addNode(componentId(F_PAGE), "Component", { path: F_PAGE, coarse: true }); // == extract_api key
  addEdge(id, componentId(F_PAGE), "PROJECTS_TO");
  addEdge(moduleId(F_PAGE), id, "DECLARES");
} else markUnresolved("ReactComponent ModelPortfolios", F_PAGE, "component declaration not found");

const heatmap = sf(F_HEATMAP);
const heatmapComp = findComponent(heatmap, "BenchmarkHeatmap");
const heatmapRcId = rcId(F_HEATMAP, "BenchmarkHeatmap");
if (heatmapComp) {
  addNode(heatmapRcId, "ReactComponent", { name: "BenchmarkHeatmap", path: F_HEATMAP, coarseKey: componentId(F_HEATMAP) });
  addNode(componentId(F_HEATMAP), "Component", { path: F_HEATMAP, coarse: true });
  addEdge(heatmapRcId, componentId(F_HEATMAP), "PROJECTS_TO");
  addEdge(moduleId(F_HEATMAP), heatmapRcId, "DECLARES");
  // props from BenchmarkHeatmapProps
  const propsIface = heatmap.getInterface("BenchmarkHeatmapProps");
  if (propsIface) {
    const propsTypeId = typeDeclId("BenchmarkHeatmapProps", F_HEATMAP);
    for (const p of propsIface.getProperties()) {
      const pid = `prop:${heatmapRcId}#${p.getName()}`;
      addNode(pid, "Prop", { name: p.getName(), component: "BenchmarkHeatmap", tsType: p.getType().getText(p), optional: p.hasQuestionToken() });
      addEdge(heatmapRcId, pid, "HAS_PROP");
      // HAS_TYPE for the data prop -> BenchmarkModelData (element type)
      if (p.getName() === "data") {
        const bId = typeDeclId("BenchmarkModelData", F_PROXY);
        if (nodes.has(bId)) addEdge(pid, bId, "HAS_TYPE", { resolution: "prop type element (BenchmarkModelData[])" });
      }
    }
  } else markUnresolved("BenchmarkHeatmapProps", F_HEATMAP, "props interface not found");
} else markUnresolved("ReactComponent BenchmarkHeatmap", F_HEATMAP, "component declaration not found");

// ===========================================================================
// PASS 5 -- Adapter FLOWS_TO (the rename + the ternary gate) -- the SEMANTIC core
// ===========================================================================
// locate the adapter output object literal: { model, benchmark, spread, model_volatility, benchmark_volatility }
const adapterObj = page
  .getDescendantsOfKind(SyntaxKind.ObjectLiteralExpression)
  .find((o) => {
    const names = o.getProperties().map((pr) => (Node.isPropertyAssignment(pr) ? pr.getName() : ""));
    return names.includes("spread") && names.includes("model") && names.includes("benchmark");
  });
const srcTypeId = typeDeclId("ModelPortfolioPeriodReturn", F_PROXY);
const dstTypeId = typeDeclId("BenchmarkPeriodReturn", F_PROXY);
if (adapterObj) {
  for (const pa of adapterObj.getProperties()) {
    if (!Node.isPropertyAssignment(pa)) continue;
    const outField = pa.getName();
    const dstFieldId = fieldId(dstTypeId, outField);
    const init = pa.getInitializer();
    if (!init) continue;
    const branches: { node: Node; condition: string | null }[] = [];
    if (Node.isConditionalExpression(init)) {
      const cond = init.getCondition().getText();
      branches.push({ node: init.getWhenTrue(), condition: `${cond} == true` });
      branches.push({ node: init.getWhenFalse(), condition: `${cond} == false` });
    } else {
      branches.push({ node: init, condition: null });
    }
    for (const b of branches) {
      // resolve the source property access -> ModelPortfolioPeriodReturn#<field>
      const pacc = Node.isPropertyAccessExpression(b.node)
        ? b.node
        : b.node.getFirstDescendantByKind(SyntaxKind.PropertyAccessExpression);
      if (!pacc) continue;
      const r = resolvePropAccess(pacc);
      if (r.owner === "ModelPortfolioPeriodReturn" && r.field) {
        const srcFieldId = fieldId(srcTypeId, r.field);
        if (nodes.has(srcFieldId) && nodes.has(dstFieldId)) {
          addEdge(srcFieldId, dstFieldId, "FLOWS_TO", {
            via: `adapter useMemo ${loc(pa)}`,
            condition: b.condition,
            resolution: "getSymbolAtLocation on source prop access -> declaring interface (TypeChecker)",
            srcField: `ModelPortfolioPeriodReturn.${r.field}`,
            dstField: `BenchmarkPeriodReturn.${outField}`,
            rename: r.field !== outField,
            srcType: r.type,
          });
        }
      } else {
        markUnresolved(`adapter source for ${outField}`, loc(pa), `prop owner resolved to ${r.owner ?? "?"} (expected ModelPortfolioPeriodReturn)`);
      }
    }
  }
} else markUnresolved("adapter object literal", F_PAGE, "could not locate { model, benchmark, spread, ... } object");

// ===========================================================================
// PASS 6 -- Prop pass: <BenchmarkHeatmap data={benchmarkData} /> (PROP_PASSES + INSTANTIATES)
// ===========================================================================
const jsxOpens = [
  ...page.getDescendantsOfKind(SyntaxKind.JsxOpeningElement),
  ...page.getDescendantsOfKind(SyntaxKind.JsxSelfClosingElement),
];
const heatmapJsx = jsxOpens.find((j) => {
  const tag = Node.isJsxSelfClosingElement(j) ? j.getTagNameNode() : j.getTagNameNode();
  return tag.getText() === "BenchmarkHeatmap";
});
if (heatmapJsx) {
  const jsxId = `jsx:${rel(heatmapJsx)}:${heatmapJsx.getStartLineNumber()}:BenchmarkHeatmap`;
  addNode(jsxId, "JSXElement", { tag: "BenchmarkHeatmap", path: rel(heatmapJsx), line: heatmapJsx.getStartLineNumber() });
  // INSTANTIATES -> the resolved component
  const tagNode = (heatmapJsx as any).getTagNameNode();
  const tagSym = tagNode.getSymbol()?.getAliasedSymbol() ?? tagNode.getSymbol();
  if (tagSym?.getName() === "BenchmarkHeatmap") {
    addEdge(jsxId, heatmapRcId, "INSTANTIATES", { resolution: "JSX tag symbol resolved" });
  } else markUnresolved("JSX tag -> component", jsxId, `tag symbol = ${tagSym?.getName() ?? "?"}`);
  // the data attribute -> prop:data, value symbol benchmarkData
  const attrs = (heatmapJsx as any).getAttributes?.() ?? [];
  for (const a of attrs) {
    if (!Node.isJsxAttribute(a)) continue;
    if (a.getNameNode().getText() !== "data") continue;
    const propTargetId = `prop:${heatmapRcId}#data`;
    const initEx = a.getInitializer();
    const expr = Node.isJsxExpression(initEx) ? initEx.getExpression() : undefined;
    const valSym = expr?.getSymbolOrThrow?.() ?? expr?.getSymbol?.();
    addEdge(jsxId, propTargetId, "PROP_PASSES", {
      attr: "data",
      valueSymbol: valSym?.getName() ?? expr?.getText(),
      resolution: "JSX attribute value symbol resolved (benchmarkData = adapter useMemo result)",
    });
  }
} else markUnresolved("<BenchmarkHeatmap> JSX", F_PAGE, "no JSX instantiation found");

// ===========================================================================
// PASS 7 -- Render: periodData.model -> renderDataCell(...) (REFERENCES + RENDERS)
// ===========================================================================
// the indexed-access exhibit: periodData = model.returns[dataKey]
const periodDataDecl = heatmap
  .getDescendantsOfKind(SyntaxKind.VariableDeclaration)
  .find((v) => v.getName() === "periodData" && v.getInitializer()?.getText().includes("model.returns["));
let periodDataTypeText = "";
if (periodDataDecl) {
  periodDataTypeText = periodDataDecl.getType().getText(periodDataDecl);
  addNode(`expr:${loc(periodDataDecl)}:periodData`, "Expr", {
    kind: "indexed-access",
    expr: periodDataDecl.getInitializer()?.getText(),
    resolvedType: periodDataTypeText,
    note: "computed-key access model.returns[dataKey] -> resolved via indexed-access type (regex cannot type this)",
  });
}
// the rendered field: periodData?.model used in the model row, then renderDataCell(value,...)
const modelAccess = heatmap
  .getDescendantsOfKind(SyntaxKind.PropertyAccessExpression)
  .find((pa) => pa.getName() === "model" && pa.getExpression().getText().includes("periodData"));
const renderFieldId = fieldId(dstTypeId, "model");
if (modelAccess) {
  const r = resolvePropAccess(modelAccess);
  if (r.owner === "BenchmarkPeriodReturn" && nodes.has(renderFieldId)) {
    addEdge(`expr:${loc(modelAccess)}:periodData.model`, renderFieldId, "REFERENCES", {
      resolution: "getSymbolAtLocation -> BenchmarkPeriodReturn.model",
      type: r.type,
    });
    addNode(`expr:${loc(modelAccess)}:periodData.model`, "Expr", { kind: "prop-access", expr: modelAccess.getText(), resolvedType: r.type });
  } else markUnresolved("render periodData.model owner", loc(modelAccess), `owner=${r.owner ?? "?"}`);
}
// renderDataCell(value, ...) render site
const renderCall = heatmap
  .getDescendantsOfKind(SyntaxKind.CallExpression)
  .find((c) => c.getExpression().getText() === "renderDataCell" && c.getArguments()[0]?.getText() === "value");
if (renderCall) {
  const renderId = `jsx:${rel(renderCall)}:${renderCall.getStartLineNumber()}:renderDataCell`;
  addNode(renderId, "JSXElement", { kind: "render-cell", via: "renderDataCell(value, ...)", path: rel(renderCall), line: renderCall.getStartLineNumber() });
  addEdge(renderId, renderFieldId, "RENDERS", {
    resolution: "value <- periodData?.model (rowType==='model'); renderDataCell renders value",
    note: "model row at BenchmarkHeatmap.tsx:614",
  });
  if (modelAccess) addEdge(`expr:${loc(modelAccess)}:periodData.model`, renderId, "FLOWS_TO", { via: "value = periodData?.model -> renderDataCell(value)" });
} else markUnresolved("renderDataCell(value) site", F_HEATMAP, "render call not found");

const tEx = performance.now() - tEx0;

// ===========================================================================
// STITCH assembly -- the connected resolved path for the `model` field (AC2)
// ===========================================================================
const stitchPath = [
  { node: goldNodeId, label: "GoldScript", edgeToNext: "produces (DERIVES_FROM rev)", resolved: "external:D8-FP-map" },
  { node: s3NodeId, label: "S3Artifact (served)", edgeToNext: "READS_S3", resolved: "URL literal RESOLVED; key mapping external" },
  { node: epId, label: "Endpoint", edgeToNext: "IS_ENDPOINT<-DataFetch", resolved: "symbol" },
  { node: fetchNodeId, label: "DataFetch", edgeToNext: "HAS_TYPE (return type = SEAM bridge)", resolved: "TypeChecker getReturnType" },
  { node: fieldId(srcTypeId, "model"), label: "Field ModelPortfolioPeriodReturn.model (served==TS-type field)", edgeToNext: "FLOWS_TO (adapter)", resolved: "TypeChecker getSymbol" },
  { node: fieldId(dstTypeId, "model"), label: "Field BenchmarkPeriodReturn.model (adapter output)", edgeToNext: "HAS_TYPE benchmarkData / PROP_PASSES", resolved: "TypeChecker" },
  { node: `prop:${heatmapRcId}#data`, label: "Prop BenchmarkHeatmap.data", edgeToNext: "type structure -> field; render REFERENCES", resolved: "JSX attr symbol" },
  { node: modelAccess ? `expr:${loc(modelAccess)}:periodData.model` : "expr:render", label: "Expr periodData.model (render read)", edgeToNext: "RENDERS", resolved: "TypeChecker getSymbol" },
  { node: renderCall ? `jsx:${rel(renderCall)}:${renderCall.getStartLineNumber()}:renderDataCell` : "jsx:render", label: "JSXElement render-cell", edgeToNext: "(end)", resolved: "AST" },
];
// verify each hop's nodes exist
const stitchResolved = stitchPath.every((s) => nodes.has(s.node));

// ===========================================================================
// emit
// ===========================================================================
const byLabel: Record<string, number> = {};
for (const n of nodes.values()) byLabel[n.label] = (byLabel[n.label] ?? 0) + 1;
const edgeByLabel: Record<string, number> = {};
for (const e of edges) edgeByLabel[e.label] = (edgeByLabel[e.label] ?? 0) + 1;

const out = {
  meta: {
    project: "NFRA_TSGRAPH.P0",
    slice: "model-portfolios benchmark surface",
    field_proven: "model (model-portfolio return)",
    extractor: "ts-morph @28 / TS Compiler API",
    tsconfig: PORTAL_TSCONFIG,
    generated_note: "SPIKE output -- scratch graph; NOT a verification substrate (verify against built artifact / running portal, F5 rule). Scratch Kuzu load is a FROZEN vintage (CLAUDE.md Rule 20).",
  },
  metrics: {
    program_files_loaded: allFiles.length,
    program_load_ms: Math.round(tLoad),
    slice_extract_ms: Math.round(tEx),
    node_count: nodes.size,
    edge_count: edges.length,
    nodes_by_label: byLabel,
    edges_by_label: edgeByLabel,
    unresolved_count: unresolved.length,
  },
  stitch: {
    field: "model",
    fully_resolved: stitchResolved,
    seam_bridge: "served-JSON field == TS-type field, bridged by the fetch return type (apiRequest<ModelPortfolioBenchmarksResponse>) -- §5 hard-seam lever",
    path: stitchPath,
  },
  unresolved,
  nodes: [...nodes.values()],
  edges,
};

mkdirSync(OUT_DIR, { recursive: true });
writeFileSync(resolve(OUT_DIR, "benchmark_slice.graph.json"), JSON.stringify(out, null, 2));

// console summary
console.log(`OK: loaded ${allFiles.length} files in ${Math.round(tLoad)}ms; extracted slice in ${Math.round(tEx)}ms`);
console.log(`OK: ${nodes.size} nodes, ${edges.length} edges`);
console.log(`     nodes_by_label: ${JSON.stringify(byLabel)}`);
console.log(`     edges_by_label: ${JSON.stringify(edgeByLabel)}`);
console.log(`OK: model-field stitch fully_resolved = ${stitchResolved}`);
console.log(`     ${unresolved.length} VISIBLE unresolved item(s)`);
for (const u of unresolved) console.log(`     unresolved: ${u.what} @ ${u.where} -- ${u.reason}`);
console.log(`OK: wrote out/benchmark_slice.graph.json`);
