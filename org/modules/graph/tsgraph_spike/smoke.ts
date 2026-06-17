/**
 * NFRA_TSGRAPH.P0 smoke test.
 *
 * Proves the central blocker the CTO brief flags ("ts-morph absent on this machine")
 * is resolvable: that we can stand up a ts-morph Project over the portal's real
 * tsconfig and do REAL symbol/type resolution (TypeChecker), not string matching.
 *
 * Run: bun run smoke.ts   (from org/modules/graph/tsgraph_spike/)
 */
import { Project, SyntaxKind } from "ts-morph";
import { resolve } from "node:path";

const PORTAL_TSCONFIG = resolve(import.meta.dir, "../../../../portal/tsconfig.app.json");

console.log(`[smoke] tsconfig: ${PORTAL_TSCONFIG}`);

const t0 = performance.now();
const project = new Project({ tsConfigFilePath: PORTAL_TSCONFIG });
const tLoad = performance.now() - t0;

const sourceFiles = project.getSourceFiles();
console.log(`OK: loaded ${sourceFiles.length} source files in ${tLoad.toFixed(0)}ms`);

// --- Resolution check 1: a function's return type resolves to the real interface ---
const proxy = project.getSourceFileOrThrow((sf) =>
  sf.getFilePath().endsWith("api/portal-proxy.ts"),
);
const fn = proxy.getFunctionOrThrow("getModelPortfolioBenchmarks");
const ret = fn.getReturnType();
console.log(`OK: getModelPortfolioBenchmarks() return type = ${ret.getText()}`);

// Promise<T> -> unwrap the response type and enumerate its fields (REAL type, not regex)
const respType = ret.getTypeArguments()[0] ?? ret;
const respProps = respType.getProperties().map((p) => p.getName());
console.log(`OK: response type fields = [${respProps.join(", ")}]`);

// --- Resolution check 2: follow models[].returns[period] to the period-return field set ---
const modelsProp = respType.getProperty("models");
const modelsType = modelsProp?.getTypeAtLocation(fn); // ModelPortfolioData[]
const elemType = modelsType?.getArrayElementType();
const returnsProp = elemType?.getProperty("returns");
const returnsType = returnsProp?.getTypeAtLocation(fn);
// period value type (e.g. the 'QTD' property) -> ModelPortfolioPeriodReturn | null
const qtdProp = returnsType?.getProperty("QTD");
const qtdType = qtdProp?.getTypeAtLocation(fn);
const periodFields = qtdType
  ?.getNonNullableType()
  .getProperties()
  .map((p) => p.getName());
console.log(`OK: ModelPortfolioPeriodReturn fields = [${(periodFields ?? []).join(", ")}]`);

// --- Resolution check 3: getSymbolAtLocation on a real reference resolves to its declaration ---
const mp = project.getSourceFileOrThrow((sf) =>
  sf.getFilePath().endsWith("pages/ModelPortfolios.tsx"),
);
// find the `data.model` property access inside the adapter useMemo
const dotModel = mp
  .getDescendantsOfKind(SyntaxKind.PropertyAccessExpression)
  .find((pa) => pa.getName() === "model" && pa.getExpression().getText() === "data");
if (dotModel) {
  const sym = dotModel.getNameNode().getSymbol();
  const decls = sym?.getDeclarations() ?? [];
  const d0 = decls[0];
  console.log(
    `OK: resolved \`data.model\` -> symbol '${sym?.getName()}' declared at ${
      d0 ? `${d0.getSourceFile().getBaseName()}:${d0.getStartLineNumber()}` : "?"
    } (type ${dotModel.getType().getText()})`,
  );
} else {
  console.log("WARN: could not locate `data.model` access in ModelPortfolios.tsx");
}

console.log("OK: smoke complete -- ts-morph resolves symbols + types over the portal program.");
