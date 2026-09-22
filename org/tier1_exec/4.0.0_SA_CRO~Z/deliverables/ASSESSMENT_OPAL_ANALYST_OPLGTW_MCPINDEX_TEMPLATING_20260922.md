# ASSESSMENT -- productizing and templating the Opal Analyst (0.0.3_BG_BBGTerminal), OPLGTW and MCPINDEX

**From** `4.0.0_SA_CRO~Z`, 2026-09-22 ~18:5xZ, on Andrew's words at this terminal (record
`ANDREW_DIRECT_20260922_OPAL_ANALYST_MICROPRODUCT_D9_TO_SITEZ.md` @`67673ed414`). **To** Andrew, and `1.0.0_SA_CTO~Z`
for the L2+ route. **Status:** an assessment, read-only. No repo was created, no file moved, no submodule changed, no
cell cut. Every count carries its instrument; every recommendation is marked as one.

---

## 0. The answer in one screen

1. **The three things are one stack, not three products.** The Opal Analyst is a Claude seat whose only external
   surface is the Opal Gateway; MCPINDEX is a layer built INSIDE the gateway (its catalog is generated into the
   gateway, its query engine is OPLGTW's). So the template is: **an instance-configured gateway** (OPLGTW), **a
   catalog-and-tools layer on it** (MCPINDEX), and **an agent seat template that consumes it** (the Analyst).
2. **The gateway is already modular where it matters.** `app/integrations/` carries an `IntegrationSpec`, three
   `AuthKind`s, a fail-closed registry and a canonical STANDARD (`docs/architecture/NFRA_INTEGRATIONS_STANDARD.md`);
   four integrations exist (ycharts, opal_portal, schwab, globgrph). What is NOT modular is the ESTATE BINDING:
   the Entra app ids and scope list, the tier roster (`MASTER_ADMIN = andrew@ + systems allowlist`), the identity
   providers, the audit bucket, the secret names and the catalog are in code or env by name. Templating the gateway
   is mostly moving those into one instance manifest.
3. **MCPINDEX is 9 of 38 cells done and wound down** (2026-09-21) with one finished cell held unmerged; its design
   already IS the template shape (one catalog entry plus one tool per new property, FWD-10). It moves to site Z with
   D9 as unfinished work, not as a finished module.
4. **The BG seat is TWO functions in one seat, and only one of them is the product.** (a) The Bloomberg terminal
   operator: device-bound daily pulls, tripwires and uploads (`/terminal-upload`, `/bbg-daily`, the OS scheduled
   tasks). (b) The Teams concierge: the Opal Analyst. **`opal_analyst` should carry (b) only.** (a) stays with the
   box and this workspace. Separating them is the first design act, and the prompt already describes them as two
   duties.
5. **"A submodule like the Portal" is not what the Portal is today.** `.gitmodules` is EMPTY (0 bytes); `portal/`
   is a bare gitlink from the initial commit, and `git submodule status` FAILS on a second unmapped gitlink
   (`models/factor_scanner`). A new repo needs a real `.gitmodules` entry, and landing it is the moment to map the
   two existing gitlinks too.
6. **The Analyst's dependency surface is small and countable:** 15 paths outside its home, in five groups (the
   gateway's `DATA_CATALOG.yaml`; the fabric comms in `org/mcp/`; the launcher `.tools/ajb.ps1` and the fence
   `.tools/hooks/bg-concierge-gate.sh`; two portal/Bloomberg data reads; `.claude` settings and skills). Each is a
   named seam in s.4.
7. **Recommended shape** (s.5): three packages -- `opal-gateway` (core + integrations, instance manifest),
   `mcp-index` (catalog schema, generator, discover family, per-property tool kit) and `opal_analyst` (prompt
   template, refs, skills, fence, launcher contract, tools) -- plus ONE instance file per deployment that binds
   identities, secrets, catalog rows and allowlists. The Opal case is the first instance.
8. **What needs Andrew's word before any act** (s.7): the two-function split; whether the Bloomberg operator
   duty stays a workspace seat; the repo names; that the fabric comms coupling (register/inbox) stays as a
   dependency of the product or becomes optional; the D9 move mechanics with MSTR.

---

## 1. Where each of the three stands (measured at HEAD `67673ed414`, site Z)

| | OPLGTW (`NFRA_OPLGTW`) | MCPINDEX (`NFRA_MCPINDEX`) | Opal Analyst (`0.0.3_BG_BBGTerminal`) |
|---|---|---|---|
| directive / fabric | D9, `fabric: laptop` | D9, `fabric: laptop` | not a project seat; charter LD-0220; prior product PRD `OPAL_ANALYST` (D6, **closed**) |
| PRD | v0.9 RATIFIED; 8 outcomes: Menachem uses Schwab data from his work Claude account; masters kept separate; per-person grants; downloads; disclosed scope/date; revocation without re-setup; existing users unaffected | v0.5 ADMITTED (@`b7dc80e2cc`); 10 outcomes: discover family, portal figures, custodian silver (Schwab, BD, Orion, Eclipse, SmartX), ETFs, safe fallback query, one-client view, on-demand history, per-person beta, one-entry onboarding | `docs/architecture/OPAL_ANALYST_PRD.md`, 3,400 lines, titled "0.0.3_BG Teams concierge as a product", sections 1-12 incl. access layers and live-beta memory |
| cells | **30 of 33 complete**, 1 superseded, 2 pending | **9 of 38 complete**, 29 pending; wound down 2026-09-21 (`POSITION_20260921_WIND_DOWN.md`); MX-c-4 finished, held unmerged on `wk-nfra_mcpindex-1-1d` (AC11 fail) | operating since 2026-08-07; skills, fence and refs iterated through 09-16 |
| code home | `infra/aws/ec2/opal-gateway/` -- 256 tracked files; `app/` 66 files, **16,185 Python lines**; `app/integrations/` 21 files; Terraform root `infra/aws/terraform/opal-gateway/` | inside the gateway: `app/refs/DATA_CATALOG.yaml`, `query_v0.py`, the discover/portal/custodian tool families (surfaces S1-S11) | `org/tier0_utility/0.0.3_BG_BBGTerminal/` (1.2 MB: prompt 148 lines, 6 refs ~770 lines, `tools/portal_lookup.py` 389, `threads/`, `logs/`, `deliverables/`) + skills + fence + launcher lines |
| live plane | EC2 `i-07dccb1615503ac99`, `/opt/opal-gateway`, role `opal-gateway-role`, deployed 2026-09-18 @`1764e54a16`; ALB OIDC; `https://mcp.opalinvest.dev/mcp` | the same process | this box; Entra account "Opal Bloomberg" via registration key `opal-gateway-bbg`; secret `opal/mcp/opalbloomberg-login` |

---

## 2. OPLGTW -- what is generic and what is bound

**Generic already (keep as the core):** the enforcement chain (`tools.py::_run`: identity -> tier -> identity scope
-> guard -> entitlements -> blast cap -> destructive confirm -> token after guard -> audit), the tier enum, OAuth
authorization server (`oauth_as.py`, dynamic registration measured live at `/.well-known/oauth-authorization-server`),
rate limiting, revocation, OTP, the integrations framework (`base.py` spec + audited run-path, `registry.py`
fail-closed enablement via `ENABLED_INTEGRATIONS`), the deploy path (`deploy-to-ec2.sh` -> S3 -> SSM, manifest
`EC2_MANIFEST.json`).

**Bound to the Opal estate (the instance manifest to extract), measured in code:**

| binding | where | template treatment |
|---|---|---|
| Entra tenant, app registration, delegated scope list | `config.py` env `TENANT_ID`/`CLIENT_ID`/`CLIENT_SECRET`; the scope list is a hard-coded block with its consent history | `instance.identity_provider` block; the scope list becomes data, validated against consent |
| tier roster | `tier.py`: `MASTER_ADMIN = andrew@ + systems allowlist`; rosters by email | `instance.tiers`: roster file, never emails in code |
| identity providers | `identity.py`: 5 providers (alb_oidc, cloudflare, verified_access, tailscale, header) with per-provider verification state | keep all five in core; the instance picks and configures |
| per-identity scoping | `identity_scope.py`, `identity_tool_allowlist.txt` | instance file |
| audit lake | `s3://opal-mcp-audit` | instance |
| secrets | four ids still carrying the `m365` name (README), `opal/mcp/opalbloomberg-login` | instance; names from the LGIC builder (`name()`) |
| the catalog | `app/refs/DATA_CATALOG.yaml` (the ONE home, CTO~Z ruling 2448/2450) | MCPINDEX's layer, instance rows |
| infrastructure names | EC2 tag, unit and role now `opal-gateway`; README still says 442 files mention `m365` (that figure predates the 08-14 rename and is not re-measured here) | the rename backlog is LGIC's, not this template's |

**Cost of the extraction:** it is a refactor of bindings into one manifest, not a rewrite. The 30-of-33 state and a
deployed, ratified gateway are the reason to template by extraction rather than by a fresh build.

---

## 3. MCPINDEX -- a template shape that is not yet built

MCPINDEX's own FWD-10 is the template statement: *"Adding the next property or tool is one catalog entry plus a
tool."* Its surfaces (S1 catalog schema + S3 home + generation into the gateway; S2 discover family; S3-S5 per-surface
readers; S6 typed query engine; S7 one fenced read role per property; S9 entity resolution; S11 beta roster) ARE the
generic layer, and the per-property analyses (S8, 6 of them complete: portal, Schwab, BD, Orion, Eclipse, SmartX,
ETFs) are the Opal instance.

**State to carry into the move:** 29 pending cells; MX-c-4 (the catalog carrier) held on its branch with AC11 failing
("0 of 49 tools carry a catalog ..." per the position doc); the register still calls the PRD `DRAFT` in its header
while the position doc says ADMITTED. Under a D9 move these come to site Z as-is; the first act here is a
`/canonical-flow NFRA_MCPINDEX` read, not a re-plan.

---

## 4. The Opal Analyst -- the function, and its seams

**The function, from `prompt.md`:** the Opal team's point of contact on Microsoft Teams via the "Opal Bloomberg"
account; answers data questions from SERVED data through an approved catalog; read-only everywhere except its own
Teams replies and local logs; the serve loop is `/bbg-teams-assist` (ack first, recall, classify, research, reply
with vintage, record). Its judgment lives in four refs: `TEAMS_DUTY.md`, `THREAD_MEMORY.md`, `REQUEST_CATALOG.md`,
`BLOOMBERG_GUARDRAILS.md`, plus `PORTAL_RETRIEVAL.md` + `tools/portal_lookup.py` and `BUCKET_ALLOWLIST.yaml`.

**The second function in the same seat (NOT the product):** the daily Bloomberg pipeline on the terminal box
(`/terminal-upload`, `/bbg-daily`, the `OPAL_BBGTML_daily_pull` / `freshness_check` / `FreezeTripwire` scheduled
tasks, the local `integrations/bloomberg/mcp` server bound to DAPI on loopback). The prompt's own words: *"still the
reason this box exists."* This duty is device-bound and stays in `ajb_workspace`.

**Dependency census** (paths referenced by `prompt.md`, `refs/*`, and the four skills; 13 files scanned, 16 distinct
paths, 15 outside the seat home):

| group | paths | seam for the carve-out |
|---|---|---|
| the gateway | `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`, `app/identity_scope.py` | read through the gateway's tools, never the file: the product consumes the catalog by MCP, or the catalog ships as MCPINDEX data |
| fabric comms | `org/mcp/inbox-watch.sh`, `org/mcp/sessions/`, `register_agent`, `org/XXX.md` | a `fabric` adapter: present in the Opal instance, optional in the template |
| launch + fence | `.tools/ajb.ps1` (F8 identity bound at launch, `--session-id`, `ENABLE_TOOL_SEARCH=auto:25`), `.tools/hooks/bg-concierge-gate.sh` (219 lines, 60-case suite) + `.claude/settings.json` hook wiring | the fence and launcher contract are PART of the product (they are what makes the seat safe); they move with it and are re-wired from the parent |
| data reads | `portal/MDPF/`, `integrations/bloomberg/pipeline/`, `lib/trading_calendar.py`, `data/model` | (b) reads served data only via `portal_lookup.py` + the allowlist; the Bloomberg pipeline reads belong to function (a) |
| skills | `.claude/skills/bbg-teams-assist` (150), `teams-assist` (132 + `teams-watch.py` 653), `terminal-upload` (205), `bbg-daily` | the two Teams skills move; the two Bloomberg skills stay |

**One mechanics fact that shapes the carve-out:** Claude Code loads `.claude/skills` and hooks from the PROJECT
ROOT it is launched in. A submodule's skills are not loaded by a session started in the parent. So the Analyst
session must launch with its cwd INSIDE `opal_analyst/` (the launcher already pins a session id and could pin the
cwd), or the parent must re-export the skills. This is the call that decides whether the seat can move at all
without a launcher change.

---

## 5. Recommended shape (recommendation, not a decision)

```
opal-gateway/            core MCP surface + guard chain + integrations framework + deploy
  instance/<name>.yaml   identity provider, tiers roster, scopes, audit lake, secrets, enabled integrations
mcp-index/               catalog schema + generator + discover family + per-property tool kit + query engine
  instance/<name>/       the catalog rows, the per-property analyses, the beta roster
opal_analyst/            the agent seat template: prompt template, refs, the two Teams skills, the fence + its
                         suite, the launcher contract, tools/portal_lookup.py, a fabric adapter
  instance/<name>.yaml   identity (Entra account + registration key), secret name, allowlist, catalog binding
ajb_workspace/           the Opal instance: gitlinks to the three (real .gitmodules), the Bloomberg operator duty,
                         the fabric
```

- **Repo names:** Andrew named `opal_analyst`. The other two are his call; `opal-gateway` already exists as the
  registered system key and the EC2 name, and MCPINDEX has no product name yet.
- **Order:** (1) fix `.gitmodules` and map the two existing gitlinks; (2) carve `opal_analyst` (smallest,
  best-bounded, the product he named), with the fence and the two Teams skills, launched from its own root; (3)
  extract the gateway's instance manifest in place (no repo move needed to template it); (4) finish MCPINDEX on
  site Z under D9, then lift its generic layer.
- **What not to do:** move the Bloomberg operator duty into the product; move the gateway's live deploy while
  templating it (the manifest extraction is a code change deployed through the existing path); fork the fence.

---

## 6. The D9 move, as it touches this

D9 = `Opal Workflows` (register placement LAPTOP since 2026-09-10): members OPAL_TAXSMA, OPAL_TAXROSTER,
OPAL_TAXSMA_PT2, OPAL_TAXSMA_REGISTRY, IRPT_FNTEND, IRPT_BCKEND, NFRA_OPLGTW, NFRA_SPMOVE, NFRA_MCPINDEX. OPLGTW
(2 pending cells) and MCPINDEX (29 pending, one held branch) are the two that this assessment concerns; both PRDs
carry `fabric: laptop` in their headers and would be re-stamped by whoever executes the move. Relayed to
`0.0.0_AB_MSTR~Z` this turn (msg 24337); the mechanics are his and MSTR's.

---

## 7. Calls for Andrew, each with a recommendation

| # | call | recommendation |
|---|---|---|
| 1 | Split the BG seat into the Analyst (product) and the Bloomberg operator (workspace)? | yes; the prompt already describes two duties, and only one is device-bound |
| 2 | Does the product keep the fabric coupling (register/inbox/XXX.md)? | as an optional adapter, on in the Opal instance, off in the template |
| 3 | Repo names for the gateway core and the index layer | `opal-gateway` (already the system key); the index name is yours |
| 4 | Launch model for a submodule-homed seat | launch with cwd inside `opal_analyst/` so its skills and hooks load; the launcher pins it |
| 5 | Fix `.gitmodules` (empty) and map `portal` and `models/factor_scanner` while adding the third? | yes, in the same act |
| 6 | Order | analyst carve-out first, gateway manifest extraction second, MCPINDEX completion on site Z third |
| 7 | Who routes it | `1.0.0_SA_CTO~Z` at L2+, one project per package or one program with three workstreams |

---

## 8. What this assessment does not claim

It did not run the gateway, deploy anything, or read the live EC2; the live-plane facts are the manifest's and the
09-18 deploy record's. The "442 files mention m365" figure is the README's from 08-12 and was not re-measured. The
line counts are `wc -l` and `git ls-files` at HEAD. The skill-loading fact (project root only) is Claude Code's
documented behaviour as this seat understands it and should be tested on the first carve-out, not assumed.
