"""The one real run of AR-t-31: the real entry point (entry.abstract_request -> drafter.draft) on a realistic reader document,
with a fake model that returns the prompt it was given. Prints names and counts only; never the planted strings."""
import json
import sys

sys.path.insert(0, ".")
from data.transcripts.scripts.commentary import drafter, entry

PLANT = ["Smith Family Trust", "12345678", "$1,250,000"]
composition = {
    "browser": {"request_id": "REQ-" + "a" * 24, "variant": 2},
    "resolved": {},
    "commentary_basis": {
        "account_type": None, "themes": [], "household": "Smith Household",
        "holdings_category_weights": {"equity": 0.6, "fixed_income": 0.4},
        "figures": {
            "variant": 2, "model_names": ["Core Growth", "Balanced Income"],
            "allocation_pct": {"equity": 61.5, "fixed_income": 38.5, "Smith Family Trust": 99.0},
            "sector_pct": {"Technology": 22.0},
            "period_returns_pct": {"1Y": 8.4, "YTD": 5.1, "Smith": 3.0},
            "benchmark_returns_pct": {"1Y": 7.9, "YTD": 4.8},
            "top_holdings": [{"ticker": "AAPL", "weight_pct": 6.2}, {"ticker": "Acme Corp", "weight_pct": 3.0},
                             {"ticker": "MSFT", "weight_pct": "$12,000"}],
            "client_name": "Smith Family Trust", "account_number": "12345678", "balance": "$1,250,000",
        },
    },
}
event = entry.ready_item_from_message("49financial", "REQ-" + "a" * 24)
req = entry.abstract_request(event, lambda rid: composition)
seen = {}


def model(prompt):
    seen["prompt"] = prompt
    return "DRAFT body"


out = drafter.draft(req, [], model=model, wipe_gate_passed=True)
prompt = seen["prompt"]
leaks = [p for p in PLANT if p in prompt]
print("request_keys:", sorted(req))
print("prompt_fields:", json.dumps(out["provenance"]["prompt_fields"], sort_keys=True))
print("withheld:", json.dumps(out["provenance"]["withheld"], sort_keys=True))
print("figures_in_prompt:", "REPORT" not in prompt and '"figures"' in prompt)
print("planted_strings_in_prompt:", len(leaks))
print("no_precedent_branch_says_so:", out["draft_text"].startswith(drafter.NO_PRECEDENT_LINE))
ok = not leaks and '"figures"' in prompt and out["provenance"]["no_precedent"] is True
print("R41-REAL-RUN-" + ("OK" if ok else "FAIL"))
sys.exit(0 if ok else 1)
