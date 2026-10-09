# TO NFRA_OPSWKF.TO-OW-k1 -- the operations lead's starter kit: one command, two panels, one adapter, no credentials

<to_id>NFRA_OPSWKF.TO-OW-k1</to_id>
<project>NFRA_OPSWKF</project>
<issued_to>0.9.0_WK_NFRA_OPSWKF~6</issued_to>
<issued_by>2.0.0_SA_COO~O2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>K</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a new folder; nothing served, nothing applied) | **Decomp cell:** `OW-k-1` |
**outcome_ref:** FWD-7 (PRD C-OPS-KIT) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_NFRA_OPSWKF~6`. Your worktree is `C:/tmp/opswkf-r1-6` (branch `wk-NFRA_OPSWKF-6`, cut from box/dell2 at the
issuance commit). Work and commit ONLY there with `bash .tools/safe-commit.sh --author "0.9.0_WK_NFRA_OPSWKF~6
<0.9.0_WK_NFRA_OPSWKF~6@opal.agent>" -F <msgfile> -- <paths>`; write the message file with the Write tool.

### WHAT THIS IS FOR

Opal's operations lead gets a light dashboard that runs on his own Windows machine. He shapes it himself by asking his own Claude
to edit its code. Opal ships the first layout and the one data adapter. Any further data he needs is a request to Opal. The kit
ships with NO alert, notification or monitor. Build it simple enough that a Claude session new to it can change a panel in
minutes.

### THE CELL

`OW-k-1`. A new folder, `tools/ops_kit/`, built on the **Python standard library only**: no pip install, no node, no build step.

- `serve.py`:
  - `python serve.py` serves `static/` and one JSON route `/api/panel/<name>` on `127.0.0.1` only (port 8765, `--port` to
    change it), and prints the URL.
  - `python serve.py --selftest` loads each panel through the adapter, prints exactly one line per panel,
    `PANEL <name> rows=<n> source=<mode>`, and exits 0 (non-zero if any panel fails to load).
- `adapter.py`, THE one data entry:
  - `get_panel(name) -> {"source": <mode>, "as_of": <date>, "rows": [...]}`;
  - the mode comes from env `OPS_KIT_SOURCE`, default `fixture`;
  - `fixture` reads `fixtures/<name>.json`;
  - `mcpindex` is a stub that reads `OPAL_MCP_URL` and `OPAL_MCP_TOKEN` from the environment and, until Opal serves the readers,
    returns `{"source": "unavailable", "rows": [], "reason": "..."}` without raising;
  - no AWS SDK, no credentials, no network call in `fixture` mode.
- `fixtures/trade_rec.json` and `fixtures/billing.json`, **SYNTHETIC data only** (obviously fake account numbers like `TEST-0001`
  and fake names; never a real client, account or figure), 8-15 rows each:
  - `trade_rec` rows: `account, custodian, trade_date, symbol, side, quantity, opal_status, custodian_status, matched`;
  - `billing` rows: `account, household, billing_period, aum, fee_rate_bps, fee_amount, status`.
- `static/index.html`, `static/app.js` and `static/theme.css`:
  - one page with a header band carrying the Opal logo and name, and two panels (Trade reconciliation, Billing);
  - each panel shows a table, a one-line summary (unmatched count; total fees), and a visible stamp `source: fixture` (or
    `unavailable`) with `as_of`;
  - `theme.css` carries the portal colour law as CSS variables: canvas `#F4F6FA`, panels `#FFFFFF` with a 1px `#C4CBDB`
    hairline, navy ink, and the header band navy `rgb(25,38,67)`;
  - copy the logo into `static/` from the portal's public assets.
- `README.md`: one command to start; "ask your Claude to change anything in `static/`"; "need more data? ask Opal and we wire it
  through `adapter.py`"; a statement that it holds no credentials and sends nothing anywhere.
- `CLAUDE.md`, for HIS Claude: where layout lives (`static/`); the contract of `get_panel` and that it must not be changed by
  hand; "never add credentials, never call AWS"; how to add a panel from an existing data name.

### ACCEPTANCE

<criterion id="OW-k1-AC1" cell_refs="OW-k-1"><invocation>python org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/2.0.0_SA_COO~O2/R1_CHECKS/ow_checks.py k1-selftest</invocation><expect>OW-K1-SELFTEST-OK</expect></criterion>
`OW-k1-AC1`: `serve.py --selftest` prints both panels with rows and `source=fixture`.

<criterion id="OW-k1-AC2" cell_refs="OW-k-1"><invocation>python org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/2.0.0_SA_COO~O2/R1_CHECKS/ow_checks.py k1-bounds</invocation><expect>OW-K1-BOUNDS-OK</expect></criterion>
`OW-k1-AC2`: no AWS SDK or credential reference anywhere in the kit.

<criterion id="OW-k1-AC3" cell_refs="OW-k-1"><invocation>python org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/2.0.0_SA_COO~O2/R1_CHECKS/ow_checks.py k1-theme</invocation><expect>OW-K1-THEME-OK</expect></criterion>
`OW-k1-AC3`: `theme.css` carries the colour-law values.

<expected_criteria>OW-k1-AC1, OW-k1-AC2, OW-k1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block, your deliverables folder `org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/0.9.0_WK_NFRA_OPSWKF~6/`,
  and this order's file (status flip only). READ only: `portal/src/lib/designTokens.ts`, `portal/DESIGN.md`, `portal/public/`.
- Nothing outside `tools/ops_kit/`. Never call AWS or any live API. No real client data, ever.
- No non-ASCII in `.py` files. Rows go in as `NFRA_OPSWKF-D2-W6-S<k>`, appended in BINARY mode.

<paths>
tools/ops_kit/
org/missions/D9/NFRA/NFRA_OPSWKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPSWKF/decompositions/NFRA_OPSWKF_DECOMP.md</decomp_doc> (round 1, workstream K), cell `OW-k-1`.
<owned_cells>OW-k-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: OW-k1-AC1, OW-k1-AC2, OW-k1-AC3. The instance is at
`org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/0.9.0_WK_NFRA_OPSWKF~6/NFRA_OPSWKF.TO-OW-k1.ops-starter-kit.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> OW-k1-AC1 OW-k1-AC2 OW-k1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT (once):** the three check lines verbatim, the commits, and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, hold or gate is created or consumed by this cell
comp-iam: DECLARED-NOT-APPLICABLE the kit holds no credentials by contract (AC2)
comp-adversary: DECLARED-NOT-APPLICABLE local, synthetic data only; AC2 is the bound
lane: new folder tools/ops_kit/; Andrew-direct record @1740ba55ec; PRD v0.3 C-OPS-KIT.
</preflight>
