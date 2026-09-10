# BRIEF — Ticket Center is a TWO-WAY MIRROR, and only one face is built

**Author:** `0.7.0_AE_CloudOps~X` · 2026-09-09
**Owner of the work:** **site Z** (Andrew-direct, verbatim below). This brief hands off; it does not implement.
**Trigger:** Andrew-direct while granting the demo tenant its page set.

> "Yeah prospects should only see tickets that they filed, if they did not file any obviously those
> would be empty. This is a crucial detail of the ticket center that needed to get handled but for
> whatever reason never was, it is sitez responsibility though, I would write a little brief about
> the 2 way mirror that is ticket center, how one side should see whats open for them (i.e. Opal
> Sees All, Client only sees Client Open)."

---

## 1. The model in one line

Ticket Center is **one board seen from two sides**:

```
            OPAL SIDE  (internal)                CLIENT SIDE  (partner firm / prospect)
            -------------------------            ------------------------------------
  scope     EVERY ticket, every firm             ONLY tickets THIS filer filed
  empty?    never                                YES, and empty is the CORRECT render
  verbs     claim, complete, reassign            file, read own, comment
  identity  firmId === 'opal-capital'            any authenticated non-internal user
```

The asymmetry is the product, not a permission afterthought. "Opal sees all / client sees own" is a
**scoping rule on the READ**, and it has a hard prerequisite the estate does not currently satisfy.

## 2. Measured current state (live reads, 2026-09-09)

| what | measured | instrument |
|---|---|---|
| viewer surface | ONE, internal-only: `<ProtectedRoute requireInternal>` | `portal/src/App.tsx:454` |
| that guard | `claims?.firmId !== 'opal-capital'` -> bounce | `portal/src/components/ProtectedRoute.tsx:44` |
| list call | `listTickets({status?, assignee?, ticket_type?})` — **no firm/requester param** | `portal/src/api/endpoints/tickets.ts:69` |
| table | `opal-tickets`, PK `ticket_id`, **only** GSI `status-index` (`status` + `created_at`) | `infra/aws/terraform/ticket-center/main.tf:47-66` |
| firm in infra | **0 hits for `firmId`** across the whole ticket-center Terraform (4 files) | `comp-find` |
| live rows | 12 | `dynamodb scan` |
| `requester_email` populated | **0 of 12 — NULL on every row** | same scan |
| `requester_firm` populated | **0 of 12 — NULL on every row** | same scan |
| what IS populated | `source`, `created_by` | same scan |

## 3. THE DEFECT, precisely — and why the obvious fix fails

`Ticket` **declares** `requester_name` / `requester_email` / `requester_firm`
(`tickets.ts:60-65`). **Nothing writes them.** They are null on 12 of 12 rows.

So the intuitive fix — *"filter the list by `requester_email` = the caller"* — **returns ZERO ROWS FOR
EVERY CLIENT, FOREVER**, and does so silently: an empty board is exactly what a client with no
tickets is *supposed* to see. **The bug and the correct behaviour render identically.** A client who
filed ten tickets and a client who filed none would both see an empty board, and nothing in the UI
distinguishes them. That is the trap this brief exists to prevent site Z walking into.

What the rows actually carry instead:

```
source      = "dashboard_form:49financial"   (6 of 12)   <-- the FIRM, as a SUFFIX IN A FREE-TEXT STRING
            = "portal"                       (4 of 12)   <-- no firm at all
created_by  = "svc-ticket-form"                          <-- a SERVICE PRINCIPAL, not the human
            = "andrew@opalinvest.com"                    <-- an actual human, on portal-filed rows
            = "svc-analyst-intake"
```

Two consequences, both load-bearing:

1. **A client-filed ticket does not record which human filed it.** `created_by` is the service
   principal `svc-ticket-form`. Per-USER scoping ("tickets *they* filed") is therefore not derivable
   from the existing data at all — only per-FIRM might be, and only by parsing a string.
2. **The only firm signal is a substring of `source`.** Scoping a security boundary by
   `source.split(':')[1]` means an identity claim carried in free text that the write path can set to
   anything. That is not a scoping key; it is a label.

## 4. One more finding, free

Row 12 of 12 has **`status`, `source` and `created_by` all NULL**. `status-index` is a GSI keyed on
`status`, and **DynamoDB does not index an item missing the index key** — so that row is invisible to
every status-scoped query while still being returned by a `scan`. Any count taken through the GSI is
already short by it, and nothing surfaces the discrepancy. Worth a look independently of the mirror.

## 5. What has to land, in order

The order matters — steps 4 and 5 are unsafe before 1-3.

1. **Write path records identity.** Populate `requester_email` (the authenticated human) and
   `requester_firm` (their `firmId` from the JWT, server-side — never client-supplied) on every
   create, both the portal path and the `dashboard_form` path. Server-derived only: a requester
   field the client can set is a spoofing surface, and the whole mirror rests on this field.
2. **Decide the 12 existing rows.** They are all internal test/battery/acceptance tickets, so the
   honest options are backfill-as-internal or delete. Do NOT leave them null: null is unscopable and
   will read as "belongs to nobody" or "belongs to everybody" depending on how the filter is written.
3. **Read path scopes server-side.** The tickets Lambda derives the caller's identity from the
   authorizer context and filters there — **not** in the client. A client-side filter over a
   full-board response still ships every firm's tickets over the wire.
   Add the access pattern to the table (a `requester-index`, or a firm-partitioned key) rather than
   scanning and filtering in code.
4. **Client view surface.** The client side is a different page from the internal board: read-own +
   file, no claim/complete/reassign.
5. **Only then relax `requireInternal`.** Until step 3 is live and verified, that guard is the only
   thing preventing a cross-firm read, and it should not be touched.

## 6. Verification bar (name it now, before it's convenient to skip)

The two failure modes are indistinguishable from success without a **negative control**:

- **Positive:** client A files a ticket, sees exactly that ticket.
- **NEGATIVE, the one that matters:** client A files a ticket; client B at a *different* firm loads
  the board and does **not** see it — asserted against the **API response bytes**, not the rendered
  DOM. A UI that filters correctly over a response containing every firm's tickets passes the visual
  test and fails the real one.
- **Empty-vs-broken:** a client with zero tickets must be distinguishable, in the response, from a
  client whose scoping silently matched nothing. Otherwise §3's trap ships undetected.

## 7. Scope note

`/ticket-center` was asked for in the same instruction that granted the demo tenant `/attribution`
and `/factor-tilts`. Those two shipped; **`/ticket-center` was deliberately held off the demo
allowlist** (`portal/src/lib/firmAccess.ts`, with the reason recorded inline). Granting it today
would have shown two external VM Wealth prospects the internal board — currently 12 engineering test
tickets, and every real client-service ticket from the moment one is filed. The grant becomes safe
when §5 steps 1-3 are live, and it is one line at that point.
