# Holdings adapter patch for P (shared client surface) -- taxonomy path, facts, model name

Author `2.0.0_SA_COO~M`, 2026-09-24 ~00:5xZ. For `2.0.0_SA_COO~P` (sole shared client/schema writer, CONTRACT v1.4).
Consumer: the M-owned Holdings tab (`portal/src/pages/InvestorReporting/tabs/holdings/*`, branch `codex/irpt-m-ui`),
which already reads these three fields as OPTIONAL extras (`slices.ts` `nodeExtras`) and falls back to today's labels
while the adapter does not carry them. Nothing in the tab breaks before or after this patch lands.

## Why

The wire contract (`contracts/wire/HoldingsSnapshot.ts:46-85`) carries `classification.hierarchy_path`,
`classification.capability_facts` and `model_id`, and every accepted or candidate snapshot now fills them:
the taxonomy path of a sleeve (`Models`, `SMA > ALT Strategies > Tax-Managed SMA`, `Client`, from the registry),
the producer's facts (`DRILL WITHHELD: ...`, `MEMBERSHIP CONFLICT: ...`, `model_name=<name>`), and the model behind
a MODEL_LEAF. `contracts/adapt.ts:937` `adaptHoldingsSnapshot` drops all three, so a sleeve renders as its opaque id
(`acc_...:models`) and the L0 overview cards are named by opaque ids. Andrew's ask is the snapshot model overlay on
the screen: which clients own which models and what is in them.

## The patch (three files, additive, optional fields only; no existing field changes)

### `src/pages/InvestorReporting/contracts/index.ts` -- `HoldingsClassification` and `HoldingsNode`

```ts
export interface HoldingsClassification {
  supervision: SupervisionPartition
  advisory: AdvisoryValue
  vendorAccountSupervised: VendorSupervisedFlag
  authoritative: boolean
  /** The producer's taxonomy path for this node (registry spelling), e.g. ['Models'], ['SMA','ALT Strategies','Tax-Managed SMA'], ['Client']. Absent when the producer carried none. */
  hierarchyPath?: readonly string[]
  /** The producer's own facts about this node, verbatim (e.g. 'DRILL WITHHELD: ...'). Never interpreted by the client. */
  capabilityFacts?: readonly string[]
}

export interface HoldingsNode {
  // ... unchanged ...
  /** The model's display name when the producer carried it as the fact `model_name=<name>`; null otherwise. */
  modelName?: string | null
}
```

### `src/pages/InvestorReporting/contracts/adapt.ts` -- `adaptHoldingsSnapshot`

```ts
const MODEL_NAME_FACT = 'model_name='
// inside wire.nodes.map((node) => ({ ... })):
    modelName:
      node.classification?.capability_facts
        ?.find((f) => f.startsWith(MODEL_NAME_FACT) && f.length > MODEL_NAME_FACT.length)
        ?.slice(MODEL_NAME_FACT.length) ?? null,
    classification: node.classification
      ? {
          supervision: SUPERVISION_FOR_WIRE[node.classification.fee_taking_status] ?? 'unknown',
          advisory: advisoryFromWire(node.classification.advisory_status),
          vendorAccountSupervised: VENDOR_FLAG_FOR_WIRE[node.classification.vendor_account_supervised] ?? 'unknown',
          authoritative: node.classification.authoritative,
          ...(node.classification.hierarchy_path && node.classification.hierarchy_path.length > 0
            ? { hierarchyPath: [...node.classification.hierarchy_path] }
            : {}),
          ...(node.classification.capability_facts && node.classification.capability_facts.length > 0
            ? { capabilityFacts: [...node.classification.capability_facts] }
            : {}),
        }
      : { supervision: 'unknown', advisory: 'unknown', vendorAccountSupervised: 'unknown', authoritative: false },
```

### `src/pages/InvestorReporting/contracts/validate.ts` -- `validateHoldingsSnapshot`

```ts
      // optional, additive: a string array when present
      if ('modelName' in n && n.modelName !== null && typeof n.modelName !== 'string') p.push(`${np}.modelName: expected string|null`)
      if (isRec(c)) {
        for (const k of ['hierarchyPath', 'capabilityFacts']) {
          if (k in c && !(Array.isArray(c[k]) && (c[k] as unknown[]).every((s) => typeof s === 'string')))
            p.push(`${cp}.${k}: expected string[]`)
        }
      }
```

## Evidence the tab consumes it

`tabs/holdings/slices.ts`: `nodeExtras(node)` reads `classification.hierarchyPath` / `classification.capabilityFacts` /
`modelName` when present; `displayLabelFor(node)` renders a sleeve as its taxonomy path and a model node as its model
name; `SliceRow` gains `displayLabel`, `taxonomyPath`, `facts`. `SliceTable.tsx` prints the label and the facts under it
(`data-slot="slice-label"`, `data-slot="slice-facts"`). `DrillTree.tsx` names the L0 overview cards, the breadcrumbs, the
donut legend and the slice colours by the same label. With the adapter unchanged, every label equals today's
`displayName` and no fact prints, so the change is inert until P lands the three files.

## Not asked

No change to the wire type, the route, the request, the envelope or the validator's existing checks; no new
required field; nothing P must re-plan or re-apply.
