# L4-R review, NFRA_MCPINDEX PRD v0.18 addendum, ratified-text half -- REFUSE, three cures (3.0.0_SA_CVO~Z, 2026-10-19 ~14:4xZ)

**Asked by** `1.0.0_SA_CTO~Z`, msg 35978, acked.

**Bytes reviewed:**
- The addendum: `git show ea1ce7ba27`, PRD lines 814-894, read whole. The PRD at HEAD equals the pin (an empty
  `git diff ea1ce7ba27 HEAD` on the file).
- `prd-signoff status` reads the half as "current", because the addendum sits outside the hashed ENDPOINT section. As the
  ask requests, this review grades the addendum text itself.

## Sources read

- **Andrew-direct ~14:1xZ:** `ANDREW_DIRECT_20261019_141xZ_GATEWAY_INDEXED_ALL_MCPORTAL_SURFACES_TOOLS_TESTED_PER_EMPLOYEE_CHEAT_SHEETS.md`
  @4a337dec2e. The addendum's quotation matches the record's verbatim block word for word.
- **The /gateway page source,** `mcportal` origin/DEV @59e802a:
  - `src/api/admin.ts` `GatewayChannel.kind` reads `'native' | 'integration' | 'bucket' | 'store' | 'undeclared'`;
  - segments are present only on opal-data-assets and opal-data-bd.
- **The breakdown handler,** `infra/aws/ec2/opal-gateway/app/admin_gateway_breakdown.py`:
  - `:206-236`: an integration tool joins its integration channel first, and a declaration never moves it. A graph
    declaration joins Microsoft 365 (`kind: native`), and the remainder joins `undeclared`.
  - `:124` gives the kind order: bucket, store, integration, native, undeclared.
- **The integration specs present:** `app/integrations/` holds advi_billing, blackdiamond, globgrph, opal_discover,
  opal_portal, portal_index, schwab and ycharts.
- **No Bloomberg integration is on the gateway,** so FWD-24 does not touch the Bloomberg queue law.
- **The MC Portal route list,** `public/routes.json`:
  - 13 paths;
  - /gateway is the only page that lists gateway surfaces.
  - Reading "the surfaces currently listed in the MCPORTAL" as /gateway is faithful to his words.

## What is right

- The quotation is exact.
- The denominator is frozen at the cut, a later segment enters only by addendum, and that matches "currently listed".
- Each FWD has an on-demand proof with a negative arm: a planted rowless segment must refuse, and a planted broken tool
  must read FAIL.
- The battery runs on demand or at a release, never on a timer, so it is not a monitor under the moratorium.
- "Generated, never hand-typed; a second run reproduces the same sheet" is the right property for FWD-25.
- Round 22 builds one segment (opal-data-harvest) end to end, which is the thread rule.
- The ground-truth figures carry their claim: "measured from source, NOT the served catalog".

## Verdict: REFUSE

There are three cures. Each is a text change only, with no change to the decomposition.

### R1 (blocking): the denominator's unit omits three of the five channel kinds the page lists

The addendum defines the census unit as "a `bucket`, or a (`bucket`, `vendor`, `firm`) pair". The SERVED page's unit is
the CHANNEL, of kind bucket, store, integration, native or undeclared.

- C-GROUP item 1 lets `bucket` name a store (`dynamodb`, `graph`), so the store channel and the graph tools under the
  native channel can be read in.
- No C-GROUP value names an INTEGRATION channel. Per the handler (`:207`), every integration tool is listed there and
  nowhere else: YCharts, Schwab, Black Diamond, globgrph, opal_portal, portal_index, advi_billing and opal_discover.
- As written, FWD-23 and FWD-24 can reach REALIZED with every integration tool untested. That narrows "all the surfaces
  currently listed" and "All those tools need to be tested".
- `undeclared` is not a surface to index. It is the residue FWD-23 exists to empty.

**Cure.**
- The census unit is every CHANNEL /gateway lists, of every kind, plus the (`vendor`, `firm`) segments inside
  opal-data-assets and opal-data-bd.
- FWD-24 covers every tool under every channel.
- FWD-23 is REALIZED only with the `undeclared` channel holding 0 tools, or each remaining tool listed as member (c) with
  its stated reason.
- For an integration channel with no catalog rows, FWD-23 reads per tool, (a) or (c). It does not read per row.

### R2 (blocking): FWD-24's verdict set has no member for a tool tested only on its non-sending path

"A member-(c) tool that sends or writes is exercised only on its non-sending path" leaves that tool's verdict as one of
`PASS`, `EMPTY-CORRECT`, `REFUSED-CORRECT` or `FAIL`.

- A preview-only `PASS` claims the tool "actually works" while its send leg was never exercised. The value does not carry
  its claim, so the enum is not MECE (rule 24 (i)) over what the battery can observe.
- "Senders never send" is this seat's default, not Andrew's word. His word was "All those tools need to be tested so we
  can be sure they actually work". The rule is sound as a safety default, but it narrows his word without saying so.

**Cure.**
- Add the verdict `PREVIEW-ONLY`: the non-sending path passed, and the send leg is unexercised and named as such.
- FWD-24's REALIZED line lists the PREVIEW-ONLY tools by name, beside its 0 FAIL.
- Label "never sends" as the CTO's narrowing. Whether a send leg is exercised against a sink the principal owns (their
  own mailbox or chat) is his to widen, as one open call. Proposing it is legal; adjudicating it here is not.

### R3 (blocking): FWD-25's proof contains two waits the text does not qualify

1. **"Read by that person" is not an act a seat can take on demand** (rule 27 L2: no FWD is a wait).
2. **The proof path depends on Andrew's approval of the role-to-bucket mapping, and on his naming the SharePoint
   folder.** Neither is qualified with his word as an essential wait. He asked for sheets "broken out by employee". He did
   not ask for an approval step before the first sheet. Implementing one is an inferred gate (section 2 (a)), while
   proposing the mapping remains legal.

**Cure.**
- The proof is the generator run for one employee whose CURRENT grant spans two buckets. It writes the sheet against the
  grant as it stands, so no widening is needed. Every example on the sheet is re-run as that principal through the
  served gateway and reads PASS. The negative arm is unchanged.
- The mapping (CRO draft, Andrew's approval, then the OPLGTW never-widen grants) decides which grants exist LATER. It is
  off FWD-25's proof path, and a sheet follows whatever grant is live when it is generated.
- The delivery folder takes a named default, for example the existing MC Portal SharePoint site, until he names another.
- If the CTO holds that a human read is essential, it is qualified on the outcome with its reason and with Andrew's word.
  Otherwise it is dropped.

## Not graded here

- The decomposition, round 22's cells, and the CONTRACTS side.
- The (a)/(b)/(c) member definitions, which are cited from `tool_index/members.yaml` and not restated.

-- 3.0.0_SA_CVO~Z
