# Deploy Completion Record
**Date opened:** 2026-09-19T12:45:14.563041+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260919T135752Z
**Deploy:** AMGT-rk-36: forecasts FY1-FY3 (BEST_ + SA fallback) on the model block; read_model serves forecast_*; co-signed rk-36 pair
**Authored by:** 0.9.0_WK_AMGT_RESAPP~39
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | producer + fallback module + scopes + adapter committed | commit hash | commit 1de3fb108c (this worktree, wk-amgt-14-39) -- producer + fallback module + scopes + adapter + tests committed | CLOSED 20260919T130013Z |
| L2 | activation | module.scoped_amgt_api.aws_lambda_function.this redeployed | TF apply 0 destroy + 0-diff replan + deployed CodeSha256 == uploaded sha | build 6Kr.kKS6nCiPwLaCJkz1vMLnexahBGcg sha256 7lAqBNEGJWmYGt87UpxFYobyA6jevkFxM5yoIIjB+WY=; targeted plan 0 add/1 change/0 destroy (source_code_hash+s3_object_version+last_modified only); HALT_ACK=1 safe-apply Apply complete 0 added 1 changed 0 destroyed; post-act get-function-configuration CodeSha256 7lAqBNEGJWmYGt87UpxFYobyA6jevkFxM5yoIIjB+WY= == uploaded sha; targeted replan No changes | CLOSED 20260919T135703Z |
| L3 | verify | 13 of 13 GET routes 200 pre/post, LOST=[] GAINED=[]; AC5 | census + AC5 output | 13-route census: pre-deploy 13 of 13 200s, post-deploy 13 of 13 200s, LOST=[] GAINED=[]. AC5: BA_US_Equity 200/SERVED/has_forecast_keys True/forecast_figures 0/forecast_source_counts ABSENT:15/forecast_reason names missing bestdata.json (raw stamp 20260916T201824Z); check_face_len 179 == pre-deploy independent read (header+fiscal only, forecast 0) 179; fiscal_row_count 165 == independent direct read of the SAME unchanged _figures(model_block, fiscal_year_line_item) path. HOLLOW_NONEXISTENT_KEY_Equity 200/ABSENT/has_forecast_keys True/forecast_figures 0/forecast_reason 'no landed model block for this name'. Post-act CodeSha256 7lAqBNEGJWmYGt87UpxFYobyA6jevkFxM5yoIIjB+WY=. | CLOSED 20260919T135728Z |

## Log

- 20260919T124514Z OPENED by 0.9.0_WK_AMGT_RESAPP~39 with 3 leg(s)
- 20260919T130013Z LEG L1 closed: commit 1de3fb108c (this worktree, wk-amgt-14-39) -- producer + fallback module + scopes + adapter + tests committed
- 20260919T135703Z LEG L2 closed: build 6Kr.kKS6nCiPwLaCJkz1vMLnexahBGcg sha256 7lAqBNEGJWmYGt87UpxFYobyA6jevkFxM5yoIIjB+WY=; targeted plan 0 add/1 change
- 20260919T135728Z LEG L3 closed: 13-route census: pre-deploy 13 of 13 200s, post-deploy 13 of 13 200s, LOST=[] GAINED=[]. AC5: BA_US_Equity 200/SERVED/ha
- 20260919T135752Z CLOSED -- all 3 legs proven
