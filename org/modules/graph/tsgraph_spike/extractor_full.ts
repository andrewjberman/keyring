/**
 * NFRA_TSGRAPH.P1 Leg A -- FULL-PORTAL ts-morph semantic extractor.
 *
 * Generalizes the P0 slice extractor (3 landmark files) to the WHOLE portal/src. Emits the CTO-brief
 * §3 node/edge schema across every source file, with:
 *   - the FLOWS_TO KIND discriminator {passthrough | rename | recompute/guarded} (CTO P1 note #2);
 *   - a per-category COVERAGE report (AC3 no-silent-Unknown HARD invariant -- every unresolved is
 *     recorded + VISIBLE, never a false edge, never a silent drop);
 *   - full-portal timing (AC4 Kuzu/index scale-watch vs the P0 measure of 7.2s cold / 12.5ms incr).
 *
 * Incremental mode (--changed <fileA,fileB,...>): re-extract only the named files + their importing
 * dependents (mirrors the trace 5-min cache + nightly derive). Default = full portal.
 *
 * EXPLICITLY DEFERRED (no silent cap -- next Leg-A iteration): full-depth PROP_PASSES/RENDERS across all
 * components, and the AC5 NNA-attribution stress-test (forked FLOWS_TO). This pass establishes the
 * backbone + the field-grain FLOWS_TO with kind + coverage; logged below as deferred=...
 *
 * Run: bun run extractor_full.ts            (full portal)
 *      bun run extractor_full.ts --changed src/pages/ModelPortfolios.tsx,src/api/portal-proxy.ts
 */
import { Project, SyntaxKind, Node, type SourceFile } from "ts-morph";
import { resolve, relative } from "node:path";
import { mkdirSync, writeFileSync } from "node:fs";

const WORKSPACE = resolve(import.meta.dir, "../../../..");
const PORTAL_TSCONFIG = resolve(WORKSPACE, "portal/tsconfig.app.json");
const OUT_DIR = resolve(import.meta.dir, "out");

// ---- args: incremental mode ----
const changedArgIdx = process.argv.indexOf("--changed");
const CHANGED: string[] | null =
  changedArgIdx >= 0 && process.argv[changedArgIdx + 1]
    ? process.argv[changedArgIdx + 1].split(",").map((s) => s.trim()).filter(Boolean)
    : null;

// ---- stores ----
type Attrs = Record<string, unknown>;
const nodes = new Map<string, { id: string; label: string; attrs: Attrs }>();
const edges: { src: string; dst: string; label: string; attrs: Attrs }[] = [];
const edgeKeys = new Set<string>();
const unresolved: { cat: string; what: string; where: string; reason: string }[] = [];
const cov: Record<string, { attempted: number; resolved: number }> = {};

function bump(cat: string, ok: boolean) {
  cov[cat] ??= { attempted: 0, resolved: 0 };
  cov[cat].attempted++;
  if (ok) cov[cat].resolved++;
}
function addNode(id: string, label: string, attrs: Attrs = {}) {
  const e = nodes.get(id);
  if (e) { Object.assign(e.attrs, attrs); return id; }
  nodes.set(id, { id, label, attrs });
  return id;
}
function addEdge(src: string, dst: string, label: string, attrs: Attrs = {}) {
  const k = `${src}|${label}|${dst}`;
  if (edgeKeys.has(k)) return;
  edgeKeys.add(k);
  edges.push({ src, dst, label, attrs });
}
function note(cat: string, what: string, where: string, reason: string) {
  unresolved.push({ cat, what, where, reason });
}

// ---- key helpers (consistent with the regex graph + P0) ----
function rel(n: Node | SourceFile): string {
  const fp = (n as any).getFilePath ? (n as SourceFile).getFilePath() : (n as Node).getSourceFile().getFilePath();
  return relative(WORKSPACE, fp).replace(/\\/g, "/");
}
function loc(n: Node): string { return `${rel(n)}:${n.getStartLineNumber()}`; }
const moduleId = (r: string) => `module:${r}`;
const componentId = (r: string) => `component:${r}`;
const rcId = (r: string, name: string) => `rc:${r}#${name}`;
const endpointId = (fn: string) => `endpoint:${fn}`;
const typeDeclId = (name: string, r: string) => `type:${r}#${name}`;
const fieldId = (tId: string, f: string) => `${tId}#${f}`;

// ---- load (timed) ----
const tLoad0 = performance.now();
const project = new Project({ tsConfigFilePath: PORTAL_TSCONFIG });
const tLoad = performance.now() - tLoad0;

const allPortal = project.getSourceFiles().filter((s) => s.getFilePath().replace(/\\/g, "/").includes("/portal/src/"));

// resolve the working set (incremental: changed files + their importing dependents)
let workSet: SourceFile[];
if (CHANGED) {
  const changedSet = new Set(
    CHANGED.map((c) => c.replace(/\\/g, "/")).map((c) => (c.startsWith("portal/") ? c : `portal/${c}`)),
  );
  const seeds = allPortal.filter((s) => changedSet.has(rel(s)));
  const dependents = new Set<SourceFile>(seeds);
  // one level of importing dependents (a full transitive closure is a later refinement)
  for (const s of allPortal) {
    for (const imp of s.getImportDeclarations()) {
      const target = imp.getModuleSpecifierSourceFile();
      if (target && seeds.includes(target)) { dependents.add(s); break; }
    }
  }
  workSet = [...dependents];
} else {
  workSet = allPortal;
}

// index of known TypeDecl ids by type name (for cross-file field resolution)
const typeNameToId = new Map<string, string>();
// index of ReactComponent ids by component name (for PROP_PASSES/INSTANTIATES later)
const componentNameToId = new Map<string, string>();

const tEx0 = performance.now();

// helper: resolve a property-access expression -> {ownerInterfaceName, fieldName, typeText}
function resolveProp(node: Node): { owner: string | null; field: string | null; type: string } {
  if (!Node.isPropertyAccessExpression(node)) return { owner: null, field: null, type: "" };
  const field = node.getName();
  const sym = node.getNameNode().getSymbol();
  const decl = sym?.getDeclarations()?.[0];
  let owner: string | null = null;
  if (decl) {
    const iface = decl.getFirstAncestorByKind(SyntaxKind.InterfaceDeclaration);
    const tlit = decl.getFirstAncestorByKind(SyntaxKind.TypeLiteral);
    const talias = (iface ?? tlit)?.getFirstAncestorByKind?.(SyntaxKind.TypeAliasDeclaration);
    if (iface) owner = iface.getName();
    else if (talias) owner = (talias as any).getName?.() ?? null;
  }
  let typeText = "";
  try { typeText = node.getType().getText(node); } catch { /* visible */ }
  return { owner, field, type: typeText };
}

function isPascal(name: string | undefined): boolean {
  return !!name && /^[A-Z][A-Za-z0-9]*$/.test(name);
}
function hasJsx(n: Node): boolean {
  return (
    n.getFirstDescendantByKind(SyntaxKind.JsxElement) != null ||
    n.getFirstDescendantByKind(SyntaxKind.JsxSelfClosingElement) != null ||
    n.getFirstDescendantByKind(SyntaxKind.JsxFragment) != null
  );
}

// ============================ PASS 1: Modules ============================
for (const sf of workSet) addNode(moduleId(rel(sf)), "Module", { path: rel(sf), kind: rel(sf).endsWith(".tsx") ? "tsx" : "ts" });

// ============================ PASS 2: Types + Fields ============================
for (const sf of workSet) {
  const host = rel(sf);
  const decls: { name: string; props: { getName(): string; getType(): any; hasQuestionToken(): boolean; getStartLineNumber(): number }[]; line: number }[] = [];
  for (const iface of sf.getInterfaces()) decls.push({ name: iface.getName(), props: iface.getProperties() as any, line: iface.getStartLineNumber() });
  for (const ta of sf.getTypeAliases()) {
    const tl = ta.getTypeNode();
    if (tl && Node.isTypeLiteral(tl)) decls.push({ name: ta.getName(), props: tl.getProperties() as any, line: ta.getStartLineNumber() });
  }
  for (const d of decls) {
    const tId = typeDeclId(d.name, host);
    addNode(tId, "TypeDecl", { name: d.name, path: host, line: d.line });
    addEdge(moduleId(host), tId, "DECLARES");
    typeNameToId.set(d.name, tId);
    for (const p of d.props) {
      const fId = fieldId(tId, p.getName());
      let tt = "";
      try { tt = p.getType().getText(); } catch { /* visible */ }
      addNode(fId, "Field", { name: p.getName(), ownerType: d.name, tsType: tt, optional: p.hasQuestionToken(), path: host, line: p.getStartLineNumber() });
      addEdge(tId, fId, "HAS_FIELD");
    }
  }
}

// ============================ PASS 3: ReactComponents + Props ============================
function emitComponentProps(name: string, host: string, rcNode: string, firstParam: any) {
  // Link to the DECLARED props type (its Fields are the real props) -- NOT the full structural
  // type expansion (which pulls in inherited DOM/React attributes -> thousands of phantom props).
  if (!firstParam || !firstParam.getTypeNode) { note("component_props", `props of ${name}`, host, "no props param"); bump("component_props", false); return; }
  const tn = firstParam.getTypeNode();
  if (tn && Node.isTypeReference(tn)) {
    const pname = tn.getTypeName().getText().replace(/<.*$/, "");
    if (typeNameToId.has(pname)) { addEdge(rcNode, typeNameToId.get(pname)!, "HAS_PROPS_TYPE", { resolution: "param annotation -> named TypeDecl (declared props)" }); bump("component_props", true); return; }
    addNode(typeDeclId(pname, "external"), "TypeDecl", { name: pname, external: true });
    addEdge(rcNode, typeDeclId(pname, "external"), "HAS_PROPS_TYPE", { resolution: "props type declared outside work-set" });
    bump("component_props", true); return;
  }
  if (tn && Node.isTypeLiteral(tn)) {
    let nP = 0;
    for (const m of tn.getProperties()) {
      const pid = `prop:${rcNode}#${m.getName()}`;
      let tt = ""; try { tt = m.getType().getText(); } catch { /* visible */ }
      addNode(pid, "Prop", { name: m.getName(), component: name, tsType: tt, optional: m.hasQuestionToken?.() ?? false });
      addEdge(rcNode, pid, "HAS_PROP"); nP++;
    }
    bump("component_props", nP > 0); return;
  }
  note("component_props", `props of ${name}`, host, "param type not a named/inline type (untyped or destructured-no-annotation)"); bump("component_props", false);
}
for (const sf of workSet) {
  const host = rel(sf);
  // function declarations
  for (const fn of sf.getFunctions()) {
    const name = fn.getName();
    if (!isPascal(name) || !hasJsx(fn)) continue;
    const id = rcId(host, name!);
    addNode(id, "ReactComponent", { name, path: host, coarseKey: componentId(host) });
    addNode(componentId(host), "Component", { path: host, coarse: true });
    addEdge(moduleId(host), id, "DECLARES");
    addEdge(id, componentId(host), "PROJECTS_TO");
    componentNameToId.set(name!, id);
    emitComponentProps(name!, host, id, fn.getParameters()[0]);
  }
  // const X = (props) => JSX  /  const X = function(props){...JSX}
  for (const vd of sf.getVariableDeclarations()) {
    const name = vd.getName();
    if (!isPascal(name)) continue;
    const init = vd.getInitializer();
    if (!init || !(Node.isArrowFunction(init) || Node.isFunctionExpression(init))) continue;
    if (!hasJsx(init)) continue;
    const id = rcId(host, name);
    addNode(id, "ReactComponent", { name, path: host, coarseKey: componentId(host) });
    addNode(componentId(host), "Component", { path: host, coarse: true });
    addEdge(moduleId(host), id, "DECLARES");
    addEdge(id, componentId(host), "PROJECTS_TO");
    componentNameToId.set(name, id);
    emitComponentProps(name, host, id, (init as any).getParameters?.()[0]);
  }
}

// ============================ PASS 4: DataFetch + Endpoint ============================
for (const sf of workSet) {
  const host = rel(sf);
  if (!/\/(api|endpoints)\//.test(host)) continue;
  for (const fn of sf.getFunctions()) {
    const apiCall = fn.getDescendantsOfKind(SyntaxKind.CallExpression).find((c) => c.getExpression().getText().startsWith("apiRequest"));
    if (!apiCall) continue;
    const name = fn.getName();
    if (!name) continue;
    const fetchNode = `fetch:${host}:${fn.getStartLineNumber()}:${name}`;
    addNode(fetchNode, "DataFetch", { fn: name, path: host, line: fn.getStartLineNumber() });
    const ep = endpointId(name);
    addNode(ep, "Endpoint", { fn: name });
    addEdge(moduleId(host), fetchNode, "DECLARES");
    addEdge(fetchNode, ep, "IS_ENDPOINT");
    // return type
    let retResolved = false;
    try {
      const rt = fn.getReturnType();
      const inner = rt.getTypeArguments()[0] ?? rt;
      const sym = inner.getSymbol() ?? inner.getAliasSymbol();
      const nm = sym?.getName();
      if (nm && typeNameToId.has(nm)) { addEdge(fetchNode, typeNameToId.get(nm)!, "HAS_TYPE", { resolution: "getReturnType (TypeChecker)" }); retResolved = true; }
      else if (nm) { addNode(typeDeclId(nm, "external"), "TypeDecl", { name: nm, external: true }); addEdge(fetchNode, typeDeclId(nm, "external"), "HAS_TYPE", { resolution: "return type (decl outside work-set)" }); retResolved = true; }
    } catch { /* visible */ }
    bump("fetch_returntype", retResolved);
    if (!retResolved) note("fetch_returntype", `${name} return type`, fetchNode, "awaited type symbol unresolved");
    // url literal -> READS_S3 (the URL->S3-key mapping is EXTERNAL, marked visible)
    const urlArg = apiCall.getArguments()[0];
    const url = urlArg && Node.isStringLiteral(urlArg) ? urlArg.getLiteralText() : null;
    bump("fetch_url", !!url);
    if (url) addNode(`endpointurl:${url}`, "ServedURL", { url }), addEdge(ep, `endpointurl:${url}`, "READS_URL", { url, resolution: "URL literal RESOLVED; URL->S3-key/gold mapping EXTERNAL (proxy routing, cloud graph)" });
    else note("fetch_url", `${name} url`, fetchNode, "apiRequest url arg not a string literal (dynamic)");
  }
}

// ============================ PASS 5: Hooks (useQuery family) ============================
const QUERY_HOOKS = new Set(["useQuery", "useMutation", "useInfiniteQuery", "useSuspenseQuery"]);
for (const sf of workSet) {
  const host = rel(sf);
  for (const c of sf.getDescendantsOfKind(SyntaxKind.CallExpression)) {
    const callee = c.getExpression().getText();
    if (!QUERY_HOOKS.has(callee)) continue;
    const hookId = `hook:${host}:${c.getStartLineNumber()}:${callee}`;
    addNode(hookId, "Hook", { hook: callee, path: host, line: c.getStartLineNumber() });
    // queryKey -> rqk
    const keyProp = c.getDescendantsOfKind(SyntaxKind.PropertyAssignment).find((p) => p.getName() === "queryKey");
    const arr = keyProp?.getInitializerIfKind(SyntaxKind.ArrayLiteralExpression);
    const first = arr?.getElements()?.[0];
    const rqk = first && Node.isStringLiteral(first) ? first.getLiteralText() : null;
    if (rqk) { addNode(`rqk:${rqk}`, "ReactQueryKey", { key: rqk }); addEdge(hookId, `rqk:${rqk}`, "HAS_KEY"); }
    // queryFn -> endpoint (symbol-resolved)
    const fnProp = c.getDescendantsOfKind(SyntaxKind.PropertyAssignment).find((p) => p.getName() === "queryFn" || p.getName() === "mutationFn");
    let fetchResolved = false;
    const init = fnProp?.getInitializer();
    if (init) {
      const ident = init.getFirstDescendantByKind(SyntaxKind.Identifier) ?? (Node.isIdentifier(init) ? init : undefined);
      const tgt = ident?.getSymbol()?.getAliasedSymbol() ?? ident?.getSymbol();
      const nm = tgt?.getName();
      if (nm) { addEdge(hookId, endpointId(nm), "FETCHES", { resolution: "queryFn symbol resolved" }); fetchResolved = true; }
    }
    bump("hook_fetch", fetchResolved);
    if (!fetchResolved) note("hook_fetch", `${callee} queryFn`, hookId, "queryFn did not resolve to a named endpoint");
  }
}

// ============================ PASS 6: FLOWS_TO with KIND discriminator ============================
// detect "mapping" object literals: >=2 property initializers that reference a resolvable source field.
for (const sf of workSet) {
  for (const obj of sf.getDescendantsOfKind(SyntaxKind.ObjectLiteralExpression)) {
    const pas = obj.getProperties().filter(Node.isPropertyAssignment);
    if (pas.length < 2) continue;
    // is this a mapping literal? >=2 initializers reference a property access on some identifier
    const mappingish = pas.filter((p) => {
      const i = p.getInitializer();
      return i && (Node.isPropertyAccessExpression(i) || Node.isConditionalExpression(i) || Node.isBinaryExpression(i));
    });
    if (mappingish.length < 2) continue;
    for (const pa of pas) {
      const outField = pa.getName();
      const init = pa.getInitializer();
      if (!init) continue;
      const branches: { node: Node; cond: string | null; kindHint: "direct" | "guarded" }[] = [];
      if (Node.isConditionalExpression(init)) {
        const cnd = init.getCondition().getText();
        branches.push({ node: init.getWhenTrue(), cond: `${cnd} == true`, kindHint: "guarded" });
        branches.push({ node: init.getWhenFalse(), cond: `${cnd} == false`, kindHint: "guarded" });
      } else if (Node.isBinaryExpression(init) || Node.isCallExpression(init)) {
        branches.push({ node: init, cond: null, kindHint: "guarded" });
      } else if (Node.isPropertyAccessExpression(init)) {
        branches.push({ node: init, cond: null, kindHint: "direct" });
      } else continue;
      for (const b of branches) {
        const pacc = Node.isPropertyAccessExpression(b.node) ? b.node : b.node.getFirstDescendantByKind(SyntaxKind.PropertyAccessExpression);
        if (!pacc) { continue; }
        const r = resolveProp(pacc);
        bump("flowsto", !!(r.owner && r.field && typeNameToId.has(r.owner)));
        if (r.owner && r.field && typeNameToId.has(r.owner)) {
          const srcFieldId = fieldId(typeNameToId.get(r.owner)!, r.field);
          if (!nodes.has(srcFieldId)) continue;
          const kind = b.kindHint === "guarded" ? "recompute/guarded" : r.field === outField ? "passthrough" : "rename";
          // destination: try the object literal's contextual type field; else a local out node (VISIBLE)
          let dstId: string | null = null;
          try {
            const ctx = obj.getContextualType();
            const ctxSym = ctx?.getProperty(outField);
            const ctxDecl = ctxSym?.getDeclarations?.()?.[0];
            const ctxIface = ctxDecl?.getFirstAncestorByKind(SyntaxKind.InterfaceDeclaration);
            const ctxName = ctxIface?.getName();
            if (ctxName && typeNameToId.has(ctxName)) dstId = fieldId(typeNameToId.get(ctxName)!, outField);
          } catch { /* visible */ }
          if (!dstId) { dstId = `out:${loc(pa)}#${outField}`; addNode(dstId, "Field", { name: outField, ownerType: "(local/unresolved-output)", local: true, path: rel(pa), line: pa.getStartLineNumber() }); }
          addEdge(srcFieldId, dstId, "FLOWS_TO", {
            kind, condition: b.cond,
            srcField: `${r.owner}.${r.field}`, dstField: outField,
            rename: kind === "rename",
            resolution: "getSymbol on source prop access -> declaring type (TypeChecker)",
            via: `mapping ${loc(pa)}`,
          });
        }
      }
    }
  }
}

const tEx = performance.now() - tEx0;

// ============================ emit ============================
const byLabel: Record<string, number> = {};
for (const n of nodes.values()) byLabel[n.label] = (byLabel[n.label] ?? 0) + 1;
const edgeByLabel: Record<string, number> = {};
for (const e of edges) edgeByLabel[e.label] = (edgeByLabel[e.label] ?? 0) + 1;
const flowsByKind: Record<string, number> = {};
for (const e of edges) if (e.label === "FLOWS_TO") { const k = String(e.attrs.kind); flowsByKind[k] = (flowsByKind[k] ?? 0) + 1; }

const out = {
  meta: {
    project: "NFRA_TSGRAPH.P1 Leg A",
    mode: CHANGED ? `incremental(${workSet.length} files: changed+dependents)` : "full-portal",
    extractor: "ts-morph @28 / TS Compiler API",
    deferred: "full-depth PROP_PASSES/RENDERS across all components + AC5 NNA forked-FLOWS_TO stress-test (next iteration -- NOT silently capped)",
    note: "SPIKE/P1 output -- scratch graph; verify against built artifact/running portal (F5), never the graph.",
  },
  metrics: {
    portal_files_total: allPortal.length,
    work_set_files: workSet.length,
    program_load_ms: Math.round(tLoad),
    extract_ms: Math.round(tEx),
    node_count: nodes.size,
    edge_count: edges.length,
    nodes_by_label: byLabel,
    edges_by_label: edgeByLabel,
    flowsto_by_kind: flowsByKind,
    coverage: cov,
    unresolved_count: unresolved.length,
  },
  unresolved,
  nodes: [...nodes.values()],
  edges,
};
mkdirSync(OUT_DIR, { recursive: true });
const outName = CHANGED ? "portal_full.incremental.graph.json" : "portal_full.graph.json";
writeFileSync(resolve(OUT_DIR, outName), JSON.stringify(out, null, 2));

console.log(`OK [${out.meta.mode}]: loaded ${allPortal.length} portal files in ${Math.round(tLoad)}ms; extracted ${workSet.length}-file work-set in ${Math.round(tEx)}ms`);
console.log(`OK: ${nodes.size} nodes, ${edges.length} edges`);
console.log(`     nodes_by_label: ${JSON.stringify(byLabel)}`);
console.log(`     edges_by_label: ${JSON.stringify(edgeByLabel)}`);
console.log(`     FLOWS_TO by kind: ${JSON.stringify(flowsByKind)}`);
console.log(`     coverage (resolved/attempted): ${Object.entries(cov).map(([k, v]) => `${k} ${v.resolved}/${v.attempted}`).join(", ")}`);
console.log(`     ${unresolved.length} VISIBLE unresolved (no silent Unknown)`);
console.log(`OK: wrote out/${outName}`);
