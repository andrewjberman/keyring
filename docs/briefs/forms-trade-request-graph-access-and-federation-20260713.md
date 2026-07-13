# BRIEF -- Microsoft Forms "Opal Capital Trade Request Form": Graph access + ops-team federation

**Author:** 0.7.0_AE_CloudOps~B
**Date:** 2026-07-13
**Requested by:** Andrew (direct)
**Status:** FINDING + RECOMMENDATION. Nothing built, nothing changed.

---

## The question

1. Does the Graph API, under Menachem's Entra ID, have access to the Trade Request form?
2. Can that access be federated to ops team members (e.g. `alyssa@opalinvest.com`)?

## The answer in one line

**No -- and it is not a permissions problem, so no grant, consent, or app registration fixes it.
Microsoft Forms is not exposed on Microsoft Graph at all.** Federation is therefore not a scope
question; it is a question of getting the RESPONSES out of Forms into a surface Graph can already see.
**Moving the form to a Team does both at once, and needs no new infrastructure.**

---

## What is VERIFIED (live, this session, against Graph)

| Fact | How grounded |
|---|---|
| The form is in **our** M365 tenant | Forms URL `id=` is base64 of `[tenant GUID][owner GUID][form id]`. Decoded tenant = `6810043e-d171-4adc-9975-068b35e179da`. Matches the IT-delivered creds recorded at `docs/architecture/NFRA_OPLMCP_PRD.md:166`, and Graph independently stamps that same `tenantId` on our users in the live chat payload. |
| Owner = **Menachem Goldstein**, an internal `aadUser` | Decoded owner GUID `c727d432-161b-435a-9dd0-1e7e20c2c991` resolves live via Graph (`list_chats` -> `from.user.id` + `displayName` + `tenantId`). |
| Form id | `T70NQDA7KHZA02B6QU9ODU2GUX`. Title (from his Teams message, 2026-07-13T14:12:29Z): **"Opal Capital Trade Request Form - Collaboration"**. |
| The link Andrew holds is the **authoring** surface | `DesignPageV2` == design/co-author URL, not a fill-in URL. |
| Our M365 gateway has **no Forms tool**, and a full **SharePoint/Excel read surface** | Gateway tool list: `find_sharepoint_site`, `list_site_drives`, `list_site_files`, `search_site_files`, `read_site_file`, `read_site_workbook`, plus OneDrive equivalents. Zero Forms tools. |
| No response workbook exists in Andrew's OneDrive | `search_files("Microsoft Forms")` and `search_files("Trade Request")` -- neither returns a Forms response workbook. Consistent with the form being owned by Menachem: responses live in **his** OneDrive, and our gateway is delegated as Andrew. |
| Five Teams exist that could own the form | `Opal OCIO`, `Opal CIO Office for 49 Financial`, `49 Financial Internal Channel`, `Opal Consulting`, `Opal Capital`. |

## What is NOT verified -- and it is load-bearing (read this before building)

> **CLAIM (provenance: model knowledge, cutoff 2026-01; NOT source-confirmed):**
> Microsoft Graph exposes **no** Forms API -- no `/forms` resource in v1.0 or beta. Forms is one of the
> few M365 workloads Microsoft never shipped on Graph.
>
> **This claim is the hinge of the entire brief.** If it is FALSE, the answer collapses to "just grant
> the Graph scope" and everything below is unnecessary. It is labelled `INFERRED`, not `CONFIRMED`.
>
> **Closing check (needs Andrew's word -- it is an egress off Opal infrastructure):** fetch the Graph
> v1.0 + beta API reference index and confirm no Forms resource. One request to `learn.microsoft.com`.
> No Opal data leaves.

Two secondary claims carry the **same** provenance and must be confirmed in the same pass, because the
recommendation depends on them:
- **(a)** A **group-owned** form auto-syncs its responses to a live Excel workbook in the owning group's
  SharePoint document library.
- **(b)** An existing **personal** form can be **moved** to a group without losing its response history.

*If (a) is false, Option 2 below (Power Automate) becomes the primary, not the fallback. If (b) is false,
the form must be recreated in the group and the existing responses exported once by hand.*

---

## Why "federate the Graph access" cannot work as asked

Forms has two access layers and only one of them is a Graph object:

- **Forms co-authoring** (`Share to collaborate` -> specific people in the org). This is what the
  "- Collaboration" in the title refers to; Menachem already sent Andrew such a link. It federates
  **humans**. It is a Forms-internal ACL and is **invisible to Graph** -- adding Alyssa as a co-author
  gives her a browser session, and gives our tooling nothing.
- **Graph** sees the tenant's *files, sites, mail, chats, workbooks*. It does not see Forms.

So an ops agent, a Lambda, or the MCP gateway cannot read that form under **anyone's** identity --
Menachem's, Andrew's, or a Global Admin's. There is no endpoint to call.

## The standing risk this exposes (flagged unprompted)

The form is a **single-owner personal object**, and its responses live in **Menachem's OneDrive**.
For a **trade request** form -- which by its nature carries account/client/trade instructions -- that is a
bus-factor and data-governance exposure: **if his account is deprovisioned, the form and its entire
response history go with his OneDrive.** No ops process should depend on one person's mailbox-equivalent.

This is a defect independent of the Graph question, and it should be fixed whether or not we automate.

---

## RECOMMENDED SOLUTION

### Step 1 (does most of the work) -- move the form to an M365 Group / Team

Move "Opal Capital Trade Request Form" from Menachem's personal Forms to a **group-owned form** in
`Opal Capital` or `Opal OCIO` (both exist; ownership choice is Andrew's).

This single move buys three things at once:
- **Ownership federates.** The M365 Group owns the form; every group member is a co-owner. Alyssa's
  access follows from group membership -- no per-person Forms ACL to maintain, and it survives anyone's
  departure. *This is the actual answer to "can it be federated."*
- **Responses land in SharePoint**, in the group's document library -- not in one person's OneDrive.
- **Forms maintains a live Excel workbook there** (claim (a) above -- confirm first), which **is** a
  Graph object.

### Step 2 (zero new infrastructure) -- read it with the gateway we already run

Once the responses are a workbook in a SharePoint site, our existing M365 MCP gateway reads it today,
with no new code and no new Lambda:

```
find_sharepoint_site("Opal Capital")   -> site id
list_site_files(site_id)               -> locate the Forms response workbook
read_site_workbook(...)                -> the responses
```

Delegated as any consented group member. **Alyssa reads it as Alyssa.** That is federation with an audit
trail, and it is the least-effort path from where we stand.

### Step 3 (only if the responses must reach the AWS estate) -- push, do not poll

If trade requests need to join our own pipelines / DynamoDB / alerting, add ONE of:

| Option | Mechanism | Trade-off |
|---|---|---|
| **2 -- Power Automate, standard connectors** | `When a new response is submitted` -> write row to a **SharePoint list** in the group site. Then Graph reads the list. | Standard connectors (Forms + SharePoint) -- **no premium licence**. Event-driven. **Trap: a personally-owned FLOW re-creates the exact bus-factor defect we just fixed -- the flow must be co-owned or live in a shared solution.** |
| **3 -- Power Automate -> our own endpoint** | `When a new response is submitted` -> HTTP POST to API Gateway -> Lambda -> DynamoDB/S3. | Lands directly in our estate, governed by our IAM. **But the HTTP connector is PREMIUM** -- a real per-flow licence cost. Endpoint needs auth (key in Secrets Manager). |
| **4 -- scheduled pull** | Lambda on EventBridge reads the SharePoint list/workbook via Graph -> S3/DynamoDB. | No premium licence, no Power Platform dependency. **Polling: adds latency, and a trade request is latency-sensitive.** Prefer 2 over 4 unless licensing blocks it. |

**Recommended: Step 1 + Step 2 now (they are nearly free and fix the standing risk), then Option 2 if and
when the responses must be machine-consumed.** Do not reach for Option 3 first -- it buys estate-native
delivery at a licensing cost we do not need to pay until the requirement is real.

### Least-privilege note for any unattended (application) access

If a Lambda or app registration ever reads that site **unattended**, the correct Graph application
permission is **`Sites.Selected`**, granted against **that one site only** -- NOT `Sites.Read.All`
(tenant-wide read of every SharePoint site, wildly disproportionate for one form). `Sites.Selected` grants
nothing until an admin explicitly binds the app to a named site, which is exactly the never-widen posture
we hold everywhere else.

**Firm-separation flag (NEVER#1):** if trade requests turn out to be firm-partitioned (49F / Cottonwood /
Inflection), then any AWS landing zone for them inherits the firm-separation rules and must not become a
cross-firm surface. Raise before choosing a bucket. Not decided here.

---

## What I did NOT do

- Did not read the form (cannot -- no API exists).
- Did not read Menachem's OneDrive (out of scope of a delegated-as-Andrew token, and not asked for).
- Did not verify `alyssa@opalinvest.com` exists in the tenant -- **the gateway exposes no directory /
  user-lookup tool** (`whoami` returns only the signed-in user). The mechanism above works for whoever the
  ops members are; I am not asserting her account.
- Did not fetch Microsoft's docs (egress off Opal infra -- needs Andrew's explicit word).
- Changed nothing in the tenant.

## Next step, and who owns it

- **[Andrew]** (i) authorize the one-request docs check that promotes the three `INFERRED` claims above to
  `CONFIRMED`; (ii) choose the owning Team (`Opal Capital` vs `Opal OCIO`).
- **[Menachem]** performs the move (he is the current owner; nobody else can).
- **[0.7.0_AE_CloudOps]** on his move: verify the workbook is Graph-visible via the gateway, and confirm an
  ops member other than the owner can read it. **That read is the acceptance test -- a config inspection is
  not one** (CLAUDE.md 22a: a behavioural claim is grounded by EXERCISING the path).
