# BRIEF — project OPAL_GATEWAY

**To:** `1.0.0_SA_CTO~Z` · **From:** `4.0.0_SA_CRO~Z` · **2026-08-12**
**Origin:** Andrew-direct at the CRO~Z terminal, VERBATIM:

> *"we need to formalize that whole thing too, especially because the backend is incorrectly
> qualified still as 'm365' even though we're actively expanding its capabilities beyond the single
> vendor… it needs to be rendered canonical on name throughout the repo/backend + entitlements need
> to be registered and structured + maintained in that /projects/opal-gateway folder."*

**Current state is documented at `integrations/opal-gateway/README.md` (landed with this brief).**
This is a recon brief for a project, not a plan I am authorised to execute. Scoping and sequencing
are yours.

---

## 0. ⛔ CORRECT THE PREMISE BEFORE SCOPING — half the defect is already fixed

**The SERVER identity is already `opal-gateway`.** `app/tools.py:54` reads
`FastMCP("opal-gateway", streamable_http_path="/", stateless_http=True, ...)`, renamed and deployed
**2026-07-31** (ledger `20260731T0145Z_gateway-rename-opal-gateway_deploy_completion.md`), client key
re-keyed 2026-08-06.

⚠ **`NFRA_BBGMCP_PRD.md` §3 still cites `tools.py:37 -> FastMCP("m365-gateway")`. That citation is
STALE** — wrong line, wrong value. A project scoped off that PRD would open by "fixing" something
that shipped six weeks ago, and would likely repeat the PRD's own struck error about blast radius.

**What is actually still `m365` is the INFRASTRUCTURE AND ITS OPERATIONAL IDENTIFIERS**, which is a
harder and riskier surface than a string in a constructor.

---

## 1. THE RENAME SURFACE — measured, classified by RISK not by count

**Denominator: 442 tracked files contain `m365`** (`git grep -lI m365`). Counting them is useless;
**they are not the same kind of thing**, and a project that treats them as one workstream will do the
cheap 241 and stall on the 12 that matter (Rule 24(iv): members needing different remedies are
several workstreams presenting as one).

| # | Class | Files | Risk | Why |
|---|---|---|---|---|
| **R1** | **Runtime identifiers** — EC2 name tag, remote path `/opt/m365-mcp-gateway`, systemd unit, IAM role `m365-mcp-gateway-role` | (not file-counted) | ⛔ **HIGHEST** | Renaming a **running service's** unit/role/path is a live-service migration, not an edit. Wrong order = an outage on the estate's only authenticated MCP surface. |
| **R2** | **Secret ids** — `opal/mcp/m365-{login,graph,fernet,gateway-jwt}` | 4 secrets | ⛔ **HIGH** | The consumer is a running service reading them at boot. A rename is create-new → repoint → verify → retire-old, never a rename in place. Rotation runbook must move with them. |
| **R3** | **Gateway source tree** — the `infra/aws/ec2/m365-mcp-gateway/` directory itself | 12 | **HIGH** | Moving it changes `EC2_MANIFEST.json` `source_path`, `deploy_script`, and the deploy pipeline's assumptions. Same class as the Bloomberg move I just did, one order of magnitude up. |
| **R4** | **Other infra** — 2 Lambdas (`m365-ms-ingest-liveness`, `m365-otp-liveness`), lambda-source-map, trigger-map, TF drift indexes | 36 | **MEDIUM** | Lambda function names are live AWS resources with their own triggers. |
| **R5** | **LIVE SKILL CONSUMERS** — `tax-pt1/2/3`, `taxsma-step1`, `teams-assist` (+ `teams-watch.py`) | **6** | ⛔ **HIGH, and the sequencing trap** | These are Alyssa's daily flows. **Retire consumers FIRST** (the `comp-surface-check` lesson: a gate whose binary vanishes does not fail loudly — `command -v` fails and the caller SILENTLY SKIPS). |
| **R6** | Docs / runbooks | 33 | LOW | Prose. Correct after the mechanism moves, not before. |
| **R7** | Org deliverables / governance | 241 | LOW | Mostly prose; a few carry stale citations (see §0). |
| **R8** | **RECORDS** — logs, inbox, threads | **86** | ⛔ **DO NOT REWRITE** | Point-in-time records. A vintage-pinned citation edited to match a later tree **stops being a citation.** |

**So the real project is ~60 files across R1–R5, not 442.** R6–R8 are 360 of the 442 and are prose or
records.

### 1a. ⛔ AMENDED 2026-08-12 ~1940Z — SEPARATE THE **RETIRED SERVER NAME** FROM THE **INFRASTRUCTURE IDENTIFIERS**. They are two different jobs and only one of them is large.

`1.0.0_SA_CTO~Z` measured `m365-gateway` surviving in **72 files including `.tools/commit_gate_runner.py`** —
live gate code — and flagged *"72 places, at least one of which executes."* **I re-measured rather than
inheriting it, and the escalation does not hold.**

| | measured |
|---|---|
| files containing `m365-gateway` | **77** (not 72; **2 of the delta are my own README + this brief**, which necessarily quote the string; the rest is later commits — the gap is explained-in-part, not fully, and neither number is asserted as canonical) |
| of those, **executable file types** | **6** |
| of those, strings in an **EXECUTED EXPRESSION** | ⭐ **EXACTLY ONE** |

**The one:** `infra/aws/ec2/m365-mcp-gateway/deploy-to-ec2.sh:106` —
`aws secretsmanager get-secret-value --secret-id opal/mcp/m365-gateway-jwt`. A real secret id in a real
shell expression. **That is R2, and it is already classified HIGH.**

**Everything else is prose or human-facing text:** `config.py` (a comment pointing at a runbook),
`tools.py` (three comments *explaining the rename itself*), and the two liveness Lambdas (docstrings
plus **alert message strings a human reads** — cosmetic-but-visible, not functional).

**The gate-code hit is a DOCSTRING**, inside a block describing the 2026-07-31 incident that motivated
that check. The FILE executes; the STRING does not. Renaming it changes nothing functional.

> ⚠ **THREE SUCCESSIVE CLASSIFICATIONS MISREAD THE SAME FILE, EACH BY A DIFFERENT PROXY — worth
> carrying, because the project will be tempted to triage 77 files by exactly these heuristics.**
> **(1)** my first pass keyed on **path prefix** → `.tools/` fell into "other", low risk.
> **(2)** CTO~Z's keyed on **file type** → "live gate code that executes."
> **(3)** my second keyed on **line-prefix comment markers** → flagged it LOAD-BEARING, a **false
> positive**, because it is a docstring *continuation* line carrying no marker.
> **The discriminator is LEXICAL POSITION — is the literal inside an evaluated expression — and none
> of the three proxies measured it.** Only reading the surrounding block answered it.

⛔ **DO NOT LET THIS DEFLATE R1–R3.** This finding is scoped to the literal string `m365-gateway`
(the retired **server** name). The **infrastructure** identifiers — the `m365-mcp-gateway` directory,
EC2 name tag, `/opt` remote path, systemd unit, `m365-mcp-gateway-role`, the four `opal/mcp/m365-*`
secret ids, two `m365-*` Lambda function names — **are functional, are not the string measured here,
and remain the real work.**

**Net effect on scope:** the *retired-server-name* limb is **1 functional reference plus ~76 files of
prose, records and human-facing message text.** The *infrastructure-rename* limb is unchanged and is
where the risk lives.

### 1b. The sequencing hazard that is not obvious

**A server-side rename does NOT change what agents see.** The client-visible prefix
(`mcp__opal-gateway__*`) comes from the **registration key in per-device `~/.claude.json`**, not from
`FastMCP()`. The gateway is the estate's only component where the two differ, which makes it the
oracle — and the PRD already recorded (and struck) a wrong blast-radius claim on exactly this point.

**Consequence for scoping:** the client-facing half is **already done** and was a per-device act on
each machine, not a deploy. **The remaining work is entirely server/infra-side and changes nothing an
agent can observe** — which means **it will produce no visible confirmation that it worked.** Plan the
verification accordingly: the success signal has to be constructed, because the system will not offer
one.

---

## 2. ENTITLEMENTS — what exists, and what "registered + structured + maintained" would add

**What exists today, source-confirmed** (and it is more than a naive read suggests):

| Layer | Where | Form |
|---|---|---|
| Tier model | `app/tier.py` | 3 ranked tiers + `tier_meets_min`; spoofable-provider rejection in prod |
| Per-identity scoping | `app/identity_scope.py` + `identity_tool_allowlist.txt` | **13-line text overlay**, deny-by-default for scoped identities, each row carrying an inline `# andrew-asked:` |
| Write-class entitlement | `app/entitlements.py` | per-resource-class, hot-reloaded from `ENTITLEMENTS_PATH`; `write_delete` needs explicit master entitlement **even for MASTER_ADMIN** |
| Integration gating | `IntegrationSpec.min_tier` + `read_only` + `hosts` | validated by `validate_integration_spec` |
| Enablement | `ENABLED_INTEGRATIONS` | opt-in, fail-closed |

**THE GAP IS NOT THE MECHANISM — IT IS THAT THE POLICY HAS NO SINGLE MAINTAINED HOME.** Entitlement
truth is currently spread across a code seed, a 13-line text file, integration specs, and rulings
recorded in prose. **Nothing enumerates "who can reach what" in one place**, and nothing detects
drift between the four.

**Andrew's ask is `projects/opal-gateway/`.** Design questions that are yours, not mine:

1. **Is the registry GENERATIVE or DESCRIPTIVE?** A descriptive one drifts the moment code changes —
   that is the stale-record class this estate keeps paying for. A generative one (registry is source,
   gateway loads it) makes policy a reviewable artifact but puts a data file on the critical boot
   path of the authenticated surface. **I would not pick this without you.**
2. **Rule 24 applies at authoring time.** Tier × identity-scope × write-class × integration-min-tier
   are **four different axes** and today they are enforced at four different points in `_run`.
   A registry that flattens them into one table will be MECE-violating and will misclassify.
3. **The 13 allowlist rows each carry their authorization inline.** Whatever structure replaces it
   must not lose that — **an entitlement without its authorization is the rot with a tidier label.**

---

## 3. WHAT I RECOMMEND THE PROJECT NOT DO

- **Do not open with a repo-wide `m365` → `opal` sweep.** 86 of the 442 are records, and a global
  substitution corrupts them.
- **Do not rename secrets in place.** Create-new → repoint → verify → retire-old.
- **Do not rename the running unit/role/path before the consumers.** Skills first (R5), then infra.
- **Do not scope from `NFRA_BBGMCP_PRD.md` §3** without re-reading it against source (§0).
- **Do not treat 442 as the size of the job.** It is ~60.

---

## 4. WHAT THIS BRIEF IS NOT

I have **not** proposed an owner, a wave structure, TOs, or a schedule — those are yours. I have
**not** verified deployed-vs-repo currency of the gateway (Rule 22a CODE layer: that is a live read by
whoever owns the deploy, and the repo↔deploy question is exactly where a rename project can be
misled). I have **not** touched the gateway source, `EC2_MANIFEST.json`, or any entitlement artifact.

**Landed with this brief:** `integrations/opal-gateway/README.md` — the current-state front door,
including the enforcement-chain order, the tier model, the integration framework, the 42-tool roster,
and the `read_document` no-text capability boundary that the document-extract research project (Andrew,
same directive, held until he re-opens it) will address.
