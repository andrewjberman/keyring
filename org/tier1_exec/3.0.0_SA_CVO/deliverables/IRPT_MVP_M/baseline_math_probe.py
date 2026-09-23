import ast
import json
from pathlib import Path
import pandas as pd

source = Path("data/assets/scripts/gold/investor_reporting/holdings_snapshot.py")
tree = ast.parse(source.read_text(encoding="utf-8"))
names = {
    "_node",
    "_unknown_classification",
    "stamp_clocks",
    "holdout_block",
    "build_inf",
    "build_49f",
    "_pad10",
    "build_cot",
    "expand_model",
    "ExpansionResult",
    "dedupe_cot_holdings",
}
body = [
    ast.ImportFrom(module="__future__", names=[ast.alias(name="annotations")], level=0)
] + [
    n
    for n in tree.body
    if isinstance(n, (ast.FunctionDef, ast.ClassDef)) and n.name in names
]
ns = {
    "pd": pd,
    "opaque_id": lambda kind, firm, raw: "acc_" + str(raw),
    "firm_bucket_map": lambda: {},
    "_directory_account_ids": lambda *a: None,
    "_latest_complete_eclipse_date": lambda *a: "2026-09-21",
    "_latest_date_partition": lambda *a, **kw: "2026-09-21",
    "OPAL_ECLIPSE_MODEL_IDS": {3},
}
exec(
    compile(
        ast.fix_missing_locations(ast.Module(body=body, type_ignores=[])),
        str(source),
        "exec",
    ),
    ns,
)


def reader_inf(s3, bucket, key):
    if "portfolios_simple" in key:
        return pd.DataFrame(
            [
                {"id": 1, "account_id": "a", "model_id": 3},
                {"id": 1, "account_id": "b", "model_id": 3},
            ]
        )
    if "portfolios_full" in key:
        return pd.DataFrame([{"id": 1, "managed_value": 100.0, "excluded_value": 20.0}])
    return pd.DataFrame(
        [
            {"account_id": "a", "current_value": 70.0},
            {"account_id": "b", "current_value": 50.0},
        ]
    )


ns["_read_parquet"] = reader_inf
nodes, meta = ns["build_inf"](None, "2026-09-21")
accounts = [n for n in nodes if n["node_kind"] == "ACCOUNT"]
out = {
    "network_calls": 0,
    "synthetic_only": True,
    "inflection": {
        "input_unique_portfolio_managed": 100,
        "input_unique_portfolio_excluded": 20,
        "input_custody_total": 120,
        "output_account_total": sum(n["amount"]["value"] for n in accounts),
        "output_child_totals": [
            sum(
                c["amount"]["value"]
                for c in nodes
                if c.get("parent_node_id") == n["node_id"]
            )
            for n in accounts
        ],
        "output_account_values": [n["amount"]["value"] for n in accounts],
    },
}


def reader_49f(s3, bucket, key):
    if "account_map" in key:
        return pd.DataFrame(
            [
                {
                    "account_number": "123",
                    "allocation_id": "x",
                    "model_id": None,
                    "aum_value": 100.0,
                }
            ]
        )
    if "valuation" in key:
        return pd.DataFrame([{"owner_id": "x", "equity": 100.0, "cash": 0.0}])
    if "roster" in key:
        return pd.DataFrame([{"allocation_id": "x", "status": "ACTIVE"}])
    return pd.DataFrame()


ns["_read_parquet"] = reader_49f
nodes, meta = ns["build_49f"](None, "2026-09-21")
out["49financial"] = {
    "input_unassigned_account_value": 100,
    "output_account_total": sum(
        n["amount"]["value"] for n in nodes if n["node_kind"] == "ACCOUNT"
    ),
    "account_nodes": sum(n["node_kind"] == "ACCOUNT" for n in nodes),
    "unique_account_ids": len(
        {n["node_id"] for n in nodes if n["node_kind"] == "ACCOUNT"}
    ),
    "model_children_for_unassigned_account": sum(
        n["node_kind"] == "MODEL_LEAF" for n in nodes
    ),
}


def reader_cot(s3, bucket, key):
    if "model_assignment" in key:
        return pd.DataFrame(
            [
                {"external_id": "a", "strategy_name": "model"},
                {"external_id": "b", "strategy_name": "model"},
            ]
        )
    if "model_blend" in key:
        return pd.DataFrame()
    if "model_roster" in key:
        return pd.DataFrame([{"model_id": "model", "is_opal": True}])
    return pd.DataFrame(
        [
            {"AccountID": "a", "AssetID": "security_a", "Market Value": 100.0},
            {"AccountID": "b", "AssetID": "security_b", "Market Value": 300.0},
        ]
    )


ns["_read_parquet"] = reader_cot
nodes, meta = ns["build_cot"](None, "2026-09-21")
leaves = [n for n in nodes if n["node_kind"] == "MODEL_LEAF"]
out["cottonwood"] = {
    "input_custody_total": 400,
    "model_dollars": [n["amount"]["value"] for n in leaves],
    "output_pct_of_total": [n["percentages"]["of_total"] for n in leaves],
    "expected_pct_of_total": [0.25, 0.75],
    "security_nodes": sum(n["node_kind"] == "SECURITY" for n in nodes),
}
Path(__file__).with_suffix(".json").write_text(
    json.dumps(out, indent=2), encoding="utf-8"
)
print(json.dumps(out, indent=2))
