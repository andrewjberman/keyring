# Context: the agents on this box, the launchable template agent, the MCP tool index, and entitlements

**From:** 4.0.0_SA_CRO~Z. **For:** Andrew (record beside this file,
`ANDREW_DIRECT_20261008_140xZ_LOCAL_AGENT_FOR_THIS_BOX_TEMPLATES_VS_BG_AND_MCPINDEX_ENTITLEMENTS_CONTEXT.md`).
**Measured:** 2026-10-08 ~13:3x-14:2xZ on site Z, read-only. A context document, not a brief.

**How to read the evidence.** "Measured" means I read it today from the box, the code or git. "Recorded" means a
project file or a seat's record says so and I did not re-measure. Project status fields are dated 2026-10-01 and
10-02 and several are stale; where I could, I measured instead.

---

## 1. The answer first

**Stay with the existing agent for operating this box. Cut only the Teams half over to the template agent, which
is one sitting away. A template agent that OPERATES the box does not exist yet and would be a new build.**

| Question | Answer |
|---|---|
| What state are the template agents in? | One implementation exists and is built: the Teams agent `Opal_Agent`, in the `opal_ai` repository. Its account, folders and credential exist on this box. It has never served a colleague: the first live run is waiting on you. The repository's `template/` folder is reserved and empty |
| Can one be given the permissions and guardrails to operate this device? | Not this one, and not by widening it. It is built to have no workspace, no AWS, no agent mail and no route to the Bloomberg Terminal. Operating the box needs exactly those four. Giving them to the Teams-facing agent undoes the design |
| Is it easier to proceed with the existing agent for now? | Yes for box operation. `0.0.3_BG_BBGTerminal` is running and holds both jobs today |
| What should change now | Three things, all yours: the gateway sign-in you said you would handle; a decision on the existing agent's fence, which is switched off; and the 10-minute first run of `Opal_Agent` with Alyssa, which also unblocks two other projects |

**One finding you should see before the rest.** The existing agent's tool-layer fence is off. Section 3 has the
detail.

**How I read "modular, launchable agent templates".** As the `opal_ai` runtime agent. Two other things here fit
those words: the control-plane seat kinds (section 4.3) and the LDO Terraform module (section 2). If you meant one
of those, sections 4.3 and 2 are the relevant ones and the recommendation in section 7 still holds.

---

## 2. The agents on or behind this box today

| Agent | Where it runs | What it does | State today |
|---|---|---|---|
| `0.0.3_BG_BBGTerminal` | this box, under the `Opal Bloomberg` Windows account, which is an administrator | Two jobs by your 2026-08-24 word: Bloomberg data and the `/terminal-upload` schedule; and answering Opal staff on Teams as the "Opal Bloomberg" account | **Measured:** running since 2026-10-07 04:17 local. Its Teams side is DOWN: the gateway connection refuses its identity check until your sign-in (your item 5, "I will handle") |
| `Opal_Agent` (the `opal_ai` runtime) | this box, its own non-administrator Windows account | Teams answers for Opal staff only | **Measured:** account present and enabled, created 2026-09-28, last logon 2026-10-01 23:01; `C:\opal_runtime` present; operator credential file present; not running. Never served a colleague |
| LDO-001, the Kimi Teams assistant | AWS (a Lambda Durable Object) | Your own Teams assistant: drafts texted to you, nothing sent to Teams without your "1"; the End of Day post | **Recorded:** `status: live` in `infra/aws/terraform/modules/ldo/REGISTER.json` |
| The MSP Analyst (NFRA_MCPMSP) | planned: one Opal-hosted Teams agent for partner firms | Inflection and Cottonwood first | **Recorded:** parked 2026-10-01 on a gate at you (G-MSPID, "Not yet") |
| The 12 fabric seats | this box, same administrator account as the first row | project work | **Measured:** 13 `claude.exe` sessions, every one owned by `Opal Bloomberg` |

Two things follow from the last column:

- **Every agent session on this box runs as the same administrator.** The first row is not separated from the
  fabric seats by anything the operating system enforces. `Opal_Agent` is the only agent here with its own account.
- **The Teams service for Opal staff is currently off**, for a reason that has nothing to do with which agent
  serves it: the gateway sign-in.

---

## 3. The existing agent: what holds it, and what does not

`0.0.3_BG_BBGTerminal` was designed with a short prompt, reference files it must open before acting, and a
tool-layer fence, `.tools/hooks/bg-concierge-gate.sh`. The fence limited file writes to its own folders, denied git
and cloud changes, denied Bloomberg download-class calls, and denied every call on your own gateway identity.

| Guardrail | State | Evidence |
|---|---|---|
| The tool-layer fence | **OFF since 2026-09-17.** The script is on disk; nothing registers it | Commit `4c179f1826`: "Andrew-direct 'pull that off right now': unwire the PreToolUse hook ... script left on disk, unwired". **Measured today:** 0 lines naming it in the project's and the user's Claude settings files (4 files) |
| The gateway's server-side tool list for the "Opal Bloomberg" identity | **ON.** 11 tools in code plus 2 added by rows that each quote your word | `app/identity_scope.py`, `identity_tool_allowlist.txt` |
| Asker-scoped data: an answer is limited to what the PERSON ASKING may see | ON in the gateway | `app/asker_scope.py` |
| Its prompt and reference files | binding by reading only | its `prompt.md` still describes the fence as live |
| Operating-system separation | none | same administrator account as every seat |

So today the agent's limits on the Teams and data side are real and enforced by the gateway. Its limits on THIS
BOX (what it may write, whether it may run git or cloud commands, how much Bloomberg it may pull) rest on its
prompt alone. The record of why the fence came off is one line; I did not find the reason. Whether it goes back on
while this agent stays is your call (section 7).

---

## 4. The template agent: what is built

### 4.1 What `opal_ai` holds

Repository `Opal-Capital/opal_ai`, a submodule of the workspace. **Measured:** `DEV` and `PROD` both at `de5ce25`
(2026-10-06), 36 files.

| Slice | Contents |
|---|---|
| `opal/agent/` | The Teams agent: prompt, 7 reference files, the serve-loop skill, the Teams watcher, the fence hook and its test. Moved from the existing agent's folder |
| `opal/runtime/` | The launcher, the launch gate, the account provisioning script, the boundary check, the two Bloomberg-port wall scripts |
| `template/` | **RESERVED. A README only**: "No code yet. Reserved for a template product cut from `opal/`'s implementation once one is ordered" |
| `clients/` | RESERVED, README only, for a client-specific product |

So the repository is laid out for templates, and holds one implementation. Nothing has been cut into a reusable
template yet.

### 4.2 Its guardrails, layer by layer

| Layer | What it does | Fails how |
|---|---|---|
| Its own Windows account | `Opal_Agent`, not an administrator (**measured** today) | - |
| File permissions | Inheritance broken on the runtime folder. It can read its checkout, write only its state folder, and is denied the workspace | The boundary check runs four probes as the account, including one that must SUCCEED, so "denied everywhere" cannot pass as "boundary held" |
| Launch gate | Three checks before every start: the workspace is unreadable to it; its checkout is clean and exactly at `PROD`; it is in no administrator group | Prints every failing reason and refuses |
| Launcher | Run by you, never elevated; passes the agent no operator credential or environment | Refuses an elevated shell |
| Fence hook | On every tool call. Writes only to its state folder; git and cloud changes denied; Bloomberg download-class denied; your gateway identity denied | **Fail-closed:** no configuration or no `jq` means every call is denied |
| Gateway tool list | The same 13-tool server-side list as section 3 | - |
| Asker scope | It answers through one data tool, limited to what the asker may see | A colleague with no profile is refused, with how to get access |
| Bloomberg port wall | The Terminal's local port 8194 is closed to this account | **Recorded** live 2026-10-02 (a Windows Filtering Platform rule). I did not re-measure it; a search for firewall rules named 8194 returned none, which is consistent with a rule that is not a named firewall rule |

This is a considerably stronger set than the existing agent runs under today.

### 4.3 The two other "launchable templates" on this box

- **Control-plane seat kinds (NFRA_CTLPLN).** `org/ref/SEAT_ROLES.json` defines 8 kinds of seat (MSTR, CTO, COO,
  CVO, CRO, CLOUDOPS, TIER2, WORKER) from your 2026-10-07 words, and the launcher hands a seat its statement at
  start. `org/ref/SEAT_RULES.json` holds 47 rules, each with the one place that enforces it and a harmless probe
  that tries the forbidden act. **Measured:** `0.0.3_BG_BBGTerminal` resolves to `UNKNOWN`. No kind covers a box
  operator or a Teams agent, so this system says nothing about that seat today.
- **The LDO Terraform module.** A template for cloud functions that keep state (16 numbered parts per object).
  LDO-001 is your Teams assistant. It is a cloud pattern and cannot operate a box.

### 4.4 Where the project stands (NFRA_OPALAI)

By the last status in each task-order file, round 2 reads 35 complete and 3 pending (my count, today). What is
left is one event and what follows it:

1. **The first live run** (the "item-0 close run"), about 10 minutes, yours: start the launcher from a
   non-elevated shell; Alyssa asks the Opal Bloomberg account one question the portal answers; you ask one and are
   correctly refused, since you have no asker profile. The reviewer grades the answer against the portal.
2. **On a pass, in the same sitting:** the existing agent's Teams files are removed from the workspace and its
   launch line retires. The project's rule is that the cutover drops nothing silently, so this never happens
   before the pass.
3. A speed measurement.

**Measured today:** the runtime checkout is at `9c0a80b`; `PROD` is at `de5ce25`. The launcher fast-forwards at
launch. The record carries one caution: after a push that changes the launcher itself, the checkout is pulled by
hand before the next launch. I did not check whether `de5ce25` changes the launcher.

---

## 5. Can a template agent operate this box?

What "operating this box" needs, read from the existing agent's duties:

| Duty | Needs |
|---|---|
| The daily Bloomberg run and its checks | the Terminal's local port, the workspace's pipeline scripts, an upload path |
| Recovering a signed-out Terminal | the login secret from AWS, and control of the desktop |
| Reading run records, restarting a failed leg | the workspace and the scheduled tasks |
| Fabric mail | the agent broker |

`Opal_Agent` is denied every one of these on purpose. Its design rests on one idea: **the agent that reads messages
from people must not be the agent that holds the keys.** A Teams message is untrusted input.

| Option | What it is | Verdict |
|---|---|---|
| A. Keep the existing agent as box operator; move Teams to `Opal_Agent` | The plan already on record | **Do this now.** It needs one sitting |
| B. Build a second template, an OPERATOR, with no Teams at all | Its own account; the Bloomberg port and the login secret allowed; workspace read where the scripts need it; no way for a colleague to message it | **The right intermediate step.** It is what the `template/` slice is reserved for. It is a new build: an account profile, a fence, a launch gate, and a seat kind so the control plane knows what it is |
| C. One template agent doing both jobs | Rebuilding the existing agent inside the runtime | **Not recommended.** It puts the untrusted channel and the privileged one back in one agent |

Option B is also where splitting pays: after it, the Teams agent cannot touch Bloomberg and the operator cannot be
talked to by anyone on Teams.

---

## 6. The MCP tool index, channels and entitlements

### 6.1 What is served

**Recorded:** gateway release r28 is live (`aa75078e1b`, since 2026-10-07 21:49Z), reading 66 tools and 9 scopes.
**Measured** in code: 61 tool functions by decorator. My count missed at least the Schwab tools, which live in a
module it did not catch, so 61 is a floor. I did not reconcile the two counts.

| Channel | Tools | Notes |
|---|---|---|
| Microsoft 365 (mail, Teams, OneDrive, SharePoint, calendar, transcripts) | about 40 | reads, searches, and the sends (mail, chat, channel), which pass a confirm step |
| Opal portal data | `mdpf_get_*` (4), `etfs_get_positioning`, `opal_asker_query` | Model Portfolios and ETF positioning |
| Discover | `opal_discover`, `opal_describe`, `gateway_query_catalog` | routes a plain question to the right tool |
| Schwab | `schwab_query` and exports | four silver tables: asset, balance, position, transaction |
| Black Diamond | `blackdiamond_list_fees` | one tool |
| YCharts | 6 tools | a vendor: your per-use word applies |
| The cloud graph | `graph_cypher`, `graph_status` | - |
| Bloomberg data refresh | `opal_data_refresh_upload`, `opal_data_refresh_status` | the daily file send |
| Bloomberg Terminal | a separate local server on this box, not the gateway | the standing-read channel in the catalog has its own guardrails file |

### 6.2 The catalog (the index)

One file, `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`, version 0.4, with one writer.

| Part | Count | What it is |
|---|---|---|
| Channels | 16 | each with keywords, example questions, the paths it serves and its as-of field |
| Silver datasets | 5 | Black Diamond fees; four Schwab tables. All firm-scoped |
| Portal datasets | 5 | four Model Portfolios views, one ETF positioning view |
| Refused | 5 portal pages | advisor intelligence, ticket center, portfolio management, trade submission, data refresh |
| Never served | 10 entries | trade drafts, binaries, personal data tables, frozen legacy files |
| Held at you | 2 | `benchmark_returns.json` and Cottonwood's `account-units.json` |

A second file, the bucket allowlist, decides which storage prefixes may answer at all. The catalog cannot grant.

### 6.3 Where the project stands (NFRA_MCPINDEX)

**Recorded**, round-6 analysis of 2026-10-02; later commits (to 2026-10-06) are Black Diamond pipeline repairs.

| Outcome | Grade | Why |
|---|---|---|
| A cold question reaches the right tool | HELD | every author-side measure is met; it waits on Alyssa's cold run |
| Portal figures equal the portal's | not realized | the advisor data is held on a gate |
| Schwab | HELD | live and routed; waits on the same cold run |
| Custodian and platform tools | not realized | **Black Diamond passes end to end. Orion, Eclipse and SmartX are not started** |
| ETF tools | not realized | holdings, net assets and daily NAV are not each answered by a purpose-built tool |
| History, market data and five more | deferred | - |

Round tally: 0 realized, 3 not realized, 2 held, 5 deferred. The two HELD outcomes need one sitting with Alyssa.

### 6.4 The entitlements layout

Seven layers, outermost first. Each is in `infra/aws/ec2/opal-gateway/app/`.

| # | Layer | Question it answers | Module |
|---|---|---|---|
| 1 | Identity | Who is this? A Microsoft tenant id and object id, verified; never an email | `identity.py`, `oauth_as.py` |
| 2 | Tier | How privileged is this caller? Read-only unless the identity provider's signature was verified | `tier.py` |
| 3 | Write gates | May this tier write this kind of thing? Is the blast radius small, or confirmed? | `guard.py`, `entitlements.py`, `blast_cap.py` |
| 4 | Service-identity tool list | Is this service account limited to a named tool set? | `identity_scope.py` + `identity_tool_allowlist.txt` |
| 5 | Data entitlement | What data may this PERSON read? A profile and a versioned grant: masters, datasets, accounts, dates | `data_entitlement.py`, `access_state.py` |
| 6 | Asker scope | For a Teams answer: the INTERSECTION of the asker's grant and the calling agent's tool list | `asker_scope.py` |
| 7 | Firm boundary | For a partner firm: only four sender domains are served; the read runs under that firm's own AWS role, with no fallback to Opal's | `sender_gate.py`, `tenant_registry.py`, `firm_role.py` |

### 6.5 How entitlements are managed

| What | Who changes it | How |
|---|---|---|
| A person's data grant | You, from the operator console at `mcp.opalinvest.dev` (NFRA_MCPORTAL) | "narrow" and "widen" actions through one grant writer; takes effect on the next call; every change logged |
| A partner tenant's registration | the same grant writer | one record per tenant |
| A service account's tool list | a committed line in the allowlist file | each line quotes your word; widening is your ruling only |
| The catalog and the bucket allowlist | their one writer, by commit | neither widens itself |
| Killing access | the revocation path | by token, by session family, or by person |

**Recorded** state: the grant writer is live; Alyssa Keith's portal-only grant is active; Menachem's is not, waiting
on his verified ids. The console project is parked on the same Alyssa sitting.

I read these modules' own descriptions, not every line. `tier.py`'s description still calls itself staged and not
yet wired; I did not establish whether that is stale.

---

## 7. The operational route

### Immediate (this week, all small)

| # | Act | Whose | What it gets |
|---|---|---|---|
| 1 | The gateway sign-in | yours (you said so) | Teams answers for staff come back, on the existing agent |
| 2 | Decide the existing agent's fence: back on, or left off knowingly | yours | While this agent keeps the box, its limits here are enforced or they are not. Turning it on is re-registering the hook that commit `4c179f1826` removed |
| 3 | The first live run of `Opal_Agent`, with Alyssa | yours and hers, about 10 minutes | The Teams half moves to the isolated agent. **The same sitting is what the tool index (two HELD outcomes) and the operator console are waiting on.** Three projects move on one appointment |

### Intermediate

| # | Step | Why |
|---|---|---|
| 4 | Order the operator template (option B) | The existing agent then retires fully, and the box operator has its own account and fence |
| 5 | Add a seat kind for it | The control plane then knows what the box operator is; today it reads `UNKNOWN` |
| 6 | Cut the `template/` slice from the two implementations | Only after two exist is there something real to generalise |
| 7 | Tool index: Orion, Eclipse, SmartX; the ETF tools | The unstarted half of the index |
| 8 | Partner firms (the MSP Analyst) | Parked on your gate; you placed it downstream of staff use |

### Calls that are yours

1. Which reading of "templates" you meant (section 1).
2. The fence on the existing agent: on or off while it stays.
3. When the Alyssa sitting happens.
4. Whether to order the operator template now or after the Teams cutover has run for a while.

---

## What bounds this document

- I did not launch anything, sign in anywhere, or change any account, hook, grant or setting.
- Live reads were taken on this box only. The laptop and the two Dells are not covered.
- Project states in 4.4 and 6.3 are the projects' own records. The seats that own them (`1.0.0_SA_CTO~O`,
  `2.0.0_SA_COO~AI`, `2.0.0_SA_COO~MI`) are not all live on this box today; I did not ask them.
- The gateway's live state (release, tool count, grants) is recorded, not read from the running service.
- Tool counts by channel are from function names in code and are approximate for Microsoft 365.
