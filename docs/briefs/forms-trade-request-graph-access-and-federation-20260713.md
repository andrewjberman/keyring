# BRIEF -- Microsoft Forms "Opal Capital Trade Request Form": Graph access + ops-team federation

**Author:** 0.7.0_AE_CloudOps~B
**Date:** 2026-07-13
**Requested by:** Andrew (direct)
**Status:** CONFIRMED against Microsoft's own documentation. Nothing built, nothing changed in the tenant.

**Egress authorization (Andrew-direct, verbatim, interactive channel 2026-07-13):** *"you have permission, go
ahead"* -- granted for the `learn.microsoft.com` / `support.microsoft.com` docs check that promotes the three
claims below from `INFERRED` to `CONFIRMED`. Narrow, per-use, public documentation only; no Opal data left the
estate.

---

## The question

1. Does the Graph API, under Menachem's Entra ID, have access to the Trade Request form?
2. Can that access be federated to ops team members (e.g. `alyssa@opalinvest.com`)?

## The answer

**No -- and it is not a permissions problem, so no grant, consent, or app registration fixes it. Microsoft Graph
has no Forms endpoints, under any identity.** Federation is therefore not a scope question; it is a question of
getting the RESPONSES onto a surface Graph already sees. **Moving the form to a Team does that** -- but the move
is **NOT self-completing**, and it does **NOT** fully sever the dependency on Menachem's account. Both traps are
below, and both are load-bearing.

---

## VERIFIED -- our tenant, the owner, our reach

| Fact | How grounded |
|---|---|
| The form is in **our** M365 tenant | Forms URL `id=` is base64 of `[tenant GUID][owner GUID][form id]`. Decoded tenant = `6810043e-d171-4adc-9975-068b35e179da`, grounded on **all three planes** (22a): **DESIRED** -- `infra/aws/terraform/m365-mcp-gateway/alb.tf:106-108`, the OIDC issuer/authorize/token endpoints our own gateway ALB authenticates against @ `31b8aa98a`; **APPLIED** -- `org/critical_paths/change_management/20260623T1731Z_oplmcp02-golive-cutover_deploy_completion.md` (post-apply re-plan converged, tag `m365-mcp-gateway-v1.2.0`); **EXERCISED** -- that record's `curl https://mcp.opalinvest.dev/` -> HTTP 302 -> `login.microsoftonline.com/6810043e-.../oauth2/v2.0/authorize`. Corroborated by Graph stamping the same `tenantId` on our users live, and by the IT creds at `docs/architecture/NFRA_OPLMCP_PRD.md:166`. |
| Owner = **Menachem Goldstein**, an internal `aadUser` | Decoded owner GUID `c727d432-161b-435a-9dd0-1e7e20c2c991` resolves live via Graph (`list_chats` -> `from.user.id` + `displayName` + `tenantId`). |
| Form id / title | `T70NQDA7KHZA02B6QU9ODU2GUX` -- **"Opal Capital Trade Request Form - Collaboration"** (his Teams message, 2026-07-13T14:12:29Z). The link Andrew holds is `DesignPageV2` = the **authoring** surface, not a fill-in link. |
| Our gateway has **no Forms tool** and a **full SharePoint/Excel read surface** | Gateway tool list: `find_sharepoint_site`, `list_site_drives`, `list_site_files`, `search_site_files`, `read_site_file`, `read_site_workbook` + OneDrive equivalents. Zero Forms tools. |
| No response workbook in Andrew's OneDrive | `search_files("Microsoft Forms")` and `search_files("Trade Request")` return none. Consistent with Menachem owning the form: responses are in **his** OneDrive; our gateway is delegated as Andrew. |
| Five candidate owning Teams | `Opal OCIO`, `Opal CIO Office for 49 Financial`, `49 Financial Internal Channel`, `Opal Consulting`, `Opal Capital`. |

## CONFIRMED against Microsoft (the three former `INFERRED` claims)

| Claim | Verdict | Source |
|---|---|---|
| Graph exposes no Forms API | **CONFIRMED.** *"There is currently no support for Forms endpoints within the Graph API."* Microsoft's own answer; Forms remains on the product backlog. No `/forms` resource exists in the v1.0 or beta reference. | [MS Q&A -- Using Microsoft Graph to access Microsoft Forms responses](https://learn.microsoft.com/en-us/answers/questions/1650918/using-microsoft-graph-to-access-microsoft-forms-re) |
| A personal form can be **moved** to a group, responses preserved | **CONFIRMED, with two preconditions.** Only the **owner** can move it, **and the owner must be a member of the target group.** All previously captured responses come across. | [MS Support -- Move your form to a group](https://support.microsoft.com/en-us/office/move-your-form-to-a-group-921a6361-a4e5-44ea-bce9-c4ed63aa54b4) |
| A group form's responses land in a Graph-readable Excel workbook | **CONFIRMED, but NOT automatic** -- see TRAP 1. | same |

*Honest calibration on claim 1: the strongest available statement is a Microsoft-moderated Q&A answer plus the
absence of any Forms resource from the API reference. There is no single canonical "there is no Forms API" doc
page -- because Microsoft does not publish pages about APIs it never shipped. Absence-of-endpoint is exactly the
kind of claim that cannot be proven by a citation, only by the reference not containing it. Recorded as such.*

---

## TRAP 1 -- the workbook does not exist until a human opens it once

> *"a new Excel workbook will be created in the Documents folder of the SharePoint page and include all previously
> captured responses **after performing an initial sync by opening the workbook from the form responses page**
> after the form is moved."*

**The move alone produces nothing for Graph to read.** Somebody must open the workbook once, from the form's
responses page, to materialize it. Skip that step and the SharePoint Documents folder is empty, our
`read_site_workbook` call finds nothing, and the natural (wrong) conclusion is *"the Graph approach doesn't
work"* -- when in fact the runbook was simply not finished. **This step is mandatory and it is manual. It is in
the runbook below, and it is in the acceptance test.**

## TRAP 2 -- I WAS WRONG: the move does NOT fully sever the dependency on his account

My earlier brief said group-ownership means the form *"survives anyone's departure."* **That is true of the form
and its response history. It is FALSE of the link already in circulation.**

> *"the link pointing to the original form will still work after the form has been moved to a group, **as long as
> the original form owner account still exists within Azure AD** ... If the original form owner is hard deleted
> (30 days after soft delete), the original form link will no longer work."*

The old link **is already distributed** -- it is how trade requests get submitted today. So after the move, the
intake channel still sits on a **30-day fuse wired to one person's employment**: Menachem is offboarded, soft
delete lapses, and every outstanding link to the Trade Request form goes dead. Responses already captured are
safe (they are in the group's SharePoint). **The intake path is not.**

**Therefore the move is necessary but not sufficient. It must be followed by re-issuing the NEW group-form link
to every submitter and retiring the old one.** A migration that stops at "moved" looks complete and leaves a
timer running.

## TRAP 3 -- there IS an unofficial Forms endpoint, and someone will find it

`https://forms.office.com/formapi/api/{tenant-id}/users/{owner-object-id}/forms('{form-id}')/responses`, with a
token scoped `https://forms.office.com/.default`. Microsoft's own answer: *"The /formsapi endpoint you referenced
above is not something officially supported."*

**Naming it so nobody re-discovers it and ships it as a win.** It is the only way to read the form *directly*,
which makes it exactly the shortcut a competent engineer reaches for -- and it is undocumented, uncontracted, and
free to change or vanish without notice. For a **trade request** path carrying client and account instructions,
an unsupported endpoint is a silent-failure generator with no recourse. **Do not build on it.** If it is ever
used, it is an explicit ledgered risk decision by CTO/Andrew, never an implementation convenience.

---

## RECOMMENDED SOLUTION

### Step 1 -- move the form to an M365 Group / Team  *(Menachem; only he can)*

Move it to `Opal Capital` or `Opal OCIO` (Andrew's choice; both exist).

**Preconditions, both confirmed as hard requirements:** he must be the **owner** (he is), and he must be a
**member of the target group** (verify before choosing the Team -- if he is not in it, either add him or pick a
Team he is in).

This buys: group co-ownership (Alyssa's access follows **group membership**, not a per-person Forms ACL), the
response history moves to the group's SharePoint, and it sets up the Graph-readable workbook.

### Step 2 -- **materialize the workbook** (TRAP 1)  *(anyone with access, once)*

Open the workbook from the form's responses page. This performs the initial sync and creates it, with all prior
responses, in the group site's **Documents** folder. **Without this step there is nothing to read.**

### Step 3 -- **re-issue the link, retire the old one** (TRAP 2)  *(ops)*

Distribute the new group-form link to submitters. The old link keeps working only while Menachem's account
exists; do not leave the intake path on that fuse.

### Step 4 -- read it with the gateway we already run  *(zero new infrastructure)*

```
find_sharepoint_site("Opal Capital")   -> site id
list_site_files(site_id)               -> the Forms response workbook, in Documents/
read_site_workbook(...)                -> the responses
```

Delegated as any consented group member. **Alyssa reads it as Alyssa** -- federated, audited, no new code.

### Step 5 (only if responses must reach the AWS estate) -- push, do not poll

| Option | Mechanism | Trade-off |
|---|---|---|
| **A -- Power Automate, standard connectors** | `When a new response is submitted` -> row into a **SharePoint list** in the group site; Graph reads the list. | Standard connectors (Forms + SharePoint) -- **no premium licence.** Event-driven. **Trap: a personally-owned FLOW re-creates the exact bus factor Step 1 just removed** -- co-own it or put it in a shared solution. |
| **B -- Power Automate -> our endpoint** | response -> HTTP POST -> API Gateway -> Lambda -> DynamoDB/S3. | Estate-native, our IAM. **But the HTTP connector is PREMIUM** (real per-flow licence). Endpoint needs auth (key in Secrets Manager). |
| **C -- scheduled pull** | EventBridge -> Lambda reads the workbook/list via Graph -> S3/DynamoDB. | No premium licence, no Power Platform dependency. **Polling adds latency, and a trade request is latency-sensitive.** Prefer A unless licensing blocks it. |

**Recommended: Steps 1-4 now** (near-free, and they close the standing risk), **then Option A** if and when
responses must be machine-consumed. Do not reach for B first -- it buys estate-native delivery at a licensing
cost we need not pay until the requirement is real.

### Also required, and easy to forget
- **Outlook notification setting:** after the move, a setting must be changed in Outlook for group members to
  receive email on new responses. Otherwise responses arrive silently.
- **Departed-owner fallback:** an admin *can* transfer a form belonging to someone who has left. Good to know --
  but it is a recovery path, not a plan.

### Least-privilege, for any unattended (application) read
**`Sites.Selected`**, bound to **that one site** -- never `Sites.Read.All` (tenant-wide read of every SharePoint
site, for one form). `Sites.Selected` grants nothing until an admin binds the app to a named site: the same
never-widen posture we hold everywhere else.

**Firm-separation flag (NEVER#1):** if trade requests turn out to be firm-partitioned (49F / Cottonwood /
Inflection), any AWS landing zone inherits firm-separation and must not become a cross-firm surface. Raise before
choosing a bucket. Not decided here.

---

## The standing risk, restated precisely

The form is a **single-owner personal object** and its responses live in **Menachem's OneDrive**. It is a **trade
request** form -- account/client/trade instructions. Today, if his account is deprovisioned, **the form and its
entire response history go with it.** Steps 1-3 fix that: Step 1 moves the data to group ownership, Step 3 moves
the intake path off his account. **Either one alone leaves a hole.** This is worth doing whether or not we ever
automate.

## What I did NOT do
- Did not read the form (no supported API exists; the unofficial one is off-limits per TRAP 3).
- Did not read Menachem's OneDrive.
- Did not verify `alyssa@opalinvest.com` exists in the tenant -- **the gateway exposes no directory/user-lookup
  tool** (`whoami` returns only the signed-in user). The mechanism works for whoever the ops members are; I am
  not asserting her account.
- Did not verify Menachem is a member of `Opal Capital` / `Opal OCIO` -- same gateway limitation (I can enumerate
  **Andrew's** Teams, not another user's memberships). **This is a precondition of Step 1 and must be checked.**
- Changed nothing in the tenant.

## Next step, and who owns it
- **[Andrew]** choose the owning Team (`Opal Capital` vs `Opal OCIO`).
- **[Menachem]** confirm he is a member of that Team, then **Move** the form, then **open the workbook once** to
  force the initial sync (Steps 1-2). Only he can do the move.
- **[Ops]** re-issue the new link, retire the old (Step 3).
- **[0.7.0_AE_CloudOps]** on his move: read the workbook through the gateway **as a non-owner**, and confirm the
  response count matches. **That read is the acceptance test -- a config inspection is not one** (22a: a
  behavioural claim is grounded by EXERCISING the path, never by reading config).

## Sources
- [Microsoft Q&A -- Using Microsoft Graph to access Microsoft Forms responses](https://learn.microsoft.com/en-us/answers/questions/1650918/using-microsoft-graph-to-access-microsoft-forms-re)
- [Microsoft Support -- Move your form to a group](https://support.microsoft.com/en-us/office/move-your-form-to-a-group-921a6361-a4e5-44ea-bce9-c4ed63aa54b4)
- [Microsoft Q&A -- Extract Microsoft Forms responses data using API](https://learn.microsoft.com/en-us/answers/questions/5810347/extract-microsoft-forms-responses-data-using-api)
- [Microsoft Community Hub -- Microsoft Forms API](https://techcommunity.microsoft.com/discussions/microsoftforms/microsoft-forms-api/4480628)
