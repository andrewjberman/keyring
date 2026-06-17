/**
 * NFRA_TSGRAPH.P1 Leg C -- validate the READS_FIELD pass for comp-types `fields` parity.
 *
 * For fields, grep on the field NAME is ambiguous (name/code are everywhere), so the authoritative
 * ground truth is findReferences ON THE FIELD SYMBOL (resolves THIS type's field references precisely).
 * Compares the graph's READS_FIELD consumer-module set vs findReferences per field.
 *
 * Run: bun run field_parity_check.ts
 */
import { Project, SyntaxKind, Node } from "ts-morph";
import { resolve, relative } from "node:path";
import { readFileSync } from "node:fs";

const WORKSPACE = resolve(import.meta.dir, "../../../..");
const project = new Project({ tsConfigFilePath: resolve(WORKSPACE, "portal/tsconfig.app.json") });
const rel = (n: any) => relative(WORKSPACE, n.getSourceFile().getFilePath()).replace(/\\/g, "/");

const g = JSON.parse(readFileSync(resolve(import.meta.dir, "out/portal_full.graph.json"), "utf-8"));
const nbi = new Map(g.nodes.map((n: any) => [n.id, n]));
const readsField = new Map<string, Set<string>>(); // fieldId -> consumer module rel paths
for (const e of g.edges) {
  if (e.label !== "READS_FIELD") continue;
  const set = readsField.get(e.dst) ?? new Set<string>();
  set.add(e.src.replace("module:", ""));
  readsField.set(e.dst, set);
}

const PROXY = "portal/src/api/portal-proxy.ts";
const fid = (t: string, f: string) => `type:${PROXY}#${t}#${f}`;
const SAMPLE: [string, string][] = [
  ["BenchmarkModelData", "name"], ["BenchmarkModelData", "code"], ["BenchmarkModelData", "returns"],
  ["ModelPortfolioData", "code"], ["ModelPortfolioData", "name"], ["ModelPortfolioData", "returns"],
  ["BenchmarkPeriodReturn", "spread"], ["BenchmarkPeriodReturn", "model"],
];

const proxy = project.getSourceFileOrThrow((s) => s.getFilePath().replace(/\\/g, "/").endsWith(PROXY));

function findRefModules(typeName: string, field: string): Set<string> {
  const iface = proxy.getInterface(typeName);
  const prop = iface?.getProperty(field);
  const out = new Set<string>();
  if (!prop) return out;
  for (const r of prop.findReferencesAsNodes()) {
    if (r.getSourceFile() === prop.getSourceFile() && r.getStartLineNumber() === prop.getNameNode().getStartLineNumber()) continue; // skip decl
    out.add(rel(r));
  }
  return out;
}

console.log(`${"TYPE.field".padEnd(36)}${"findRefs".padStart(9)}${"READS_FIELD".padStart(12)}${"RECALL".padStart(8)}${"extra".padStart(7)}`);
console.log("-".repeat(74));
let allok = true;
for (const [t, f] of SAMPLE) {
  const truth = findRefModules(t, f);
  const sem = readsField.get(fid(t, f)) ?? new Set<string>();
  const missed = [...truth].filter((x) => !sem.has(x));
  const extra = [...sem].filter((x) => !truth.has(x));
  const recall = missed.length === 0 ? "PASS" : `MISS${missed.length}`;
  if (missed.length) allok = false;
  console.log(`${(t + "." + f).padEnd(36)}${String(truth.size).padStart(9)}${String(sem.size).padStart(12)}${recall.padStart(8)}${String(extra.length).padStart(7)}`);
  for (const m of missed) console.log(`     MISSED (findRefs has, READS_FIELD lacks): ${m}`);
}
console.log("-".repeat(74));
console.log(`FIELD PARITY vs findReferences ground truth: ${allok ? "RECALL PASS on all sampled fields" : "RECALL GAP remains -- see MISSED"}`);
