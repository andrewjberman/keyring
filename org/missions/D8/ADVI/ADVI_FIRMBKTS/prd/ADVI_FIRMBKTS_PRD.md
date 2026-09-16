# ADVI_FIRMBKTS -- the first migration: three legacy firm buckets into the spelled-out firm buckets, one rule for every key, one registry for every pointer, and each legacy bucket retired only on proof

```json
{
 "project": "ADVI_FIRMBKTS",
 "directive": "D8",
 "fabric": "laptop",
 "prd_version": "v1.2",
 "step": 4,
 "brief_ref": "docs/briefs/d8-legacy-firm-buckets-migration-brief-20260913.md@2b64208047",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7", "FWD-8"],
 "status": "RATIFIED"
}
```

**Brief:** `docs/briefs/d8-legacy-firm-buckets-migration-brief-20260913.md` @`2b64208047`, author `4.0.0_SA_CRO~D`.
- That is its latest content. The last touch adds only a note that the ruled key is the five segments, with the bucket
  as its container, and the REFS `PROJECT` line.
- There are 30 coverage entries below.

**Endpoint:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_D8_LEGACY_FIRM_BUCKETS_MIGRATION_20260913.md`, cut
@`dfcf7c416b`, amended @`653a21c519`, ruling stamps @`e2210bf34c`. Andrew confirmed its DONE WHEN lines ~18:4xZ 2026-09-13.

**Registration and order:**
- Registered @`f25395446e` under D8/ADVI.
- In `org/missions/SEQUENCE.yaml` it is stage 2, HELD at DECOMP. Its PRD and decomposition may proceed. Execution
  waits on two things: LGIC_ENFORCE's admitted PRD, which is MET, and LGIC_ENFORCE's scope-derived fence applied on
  `infra/aws/terraform/shared-infra/s3-49financial.tf`, the manual gate.
- Its FWD-3 also waits on LGIC_ENFORCE's registry.

**Rulings this PRD executes, verbatim anchors:**
- The commission, homed in D8 (Andrew ~01:4xZ and ~02:3xZ 2026-09-13).
- The source-first key string (~03:2xZ), ratified as LGIC_NAMING S1.
- The nine calls (~01:3xZ):
  - D10-2 (the spelled-out firm buckets become THE firm buckets, and the legacy three retire after migration);
  - `platinum/advi/{firm}/` moves into the firm bucket;
  - R21 `state/`;
  - R16's non-application to Lambda artifacts;
  - `opal-data-demo` KEPT.
- Route (c) and the dedicated MDPF runner (2026-09-12 ~13:4xZ).
- Client platinum per firm (~16:01Z 09-12).
- The ~18:4xZ cards:
  - card 1, the fence re-derived on three conditions;
  - card 2, the 45-day window;
  - card 3, read logging, which is delivered (validated @`231cd62ec5`);
  - card 4, DONE WHEN confirmed.
- ~21:3xZ: macro ADVI; cot dropped from FIRMSEP.
- ~03:xxZ 2026-09-14, verbatim: *"none of the legacy channels are quiet because they are the active channels for the
  firms now. the goal here is to ultimately transition to full name -49financial -inflection -cottonwood buckets with
  proper nomenclature, paths, conventions, as dictated in D14 projects Platform Logic."*

**The ENDPOINT section below is the endpoint's outcome block verbatim, except for one removal:** FWD-6's annotation
line (*"CARRIES THE ONE GENUINE WAIT ... expressly qualified below"*). The qualification it pointed to is now Andrew's
ruled window, carried as a CONTRACTS row.

## ENDPOINT (step 2, /endpoint --forward)

```
  FWD-1  Anyone who looks at where a piece of data is kept can tell what it is and
         whose it is, without opening it
         DONE WHEN  EXERCISED -- two people have actually read the same set of
                    locations and compared answers
         ACCEPT     two people who have never worked together read the same list of
                    storage locations and each says, for every one, which system
                    made it, which firm it belongs to, how finished it is and what
                    it holds -- and they agree -- where today the same kind of
                    information is written three different ways and neither reader
                    can tell whose it is
         SOURCE     brief Part I O1; bar Part III O1/O2

  FWD-2  A person moving the old data works out where every piece goes by following
         one rule, never by deciding
         DONE WHEN  EXERCISED -- someone has placed the whole set this way and a
                    second person, working alone, got the same answer
         ACCEPT     one person works through every piece of data in the three old
                    places using a single table; every piece lands in exactly one
                    destination and nothing is left unplaced; a second person doing
                    it alone reaches the same answer; and anything the table cannot
                    place is treated as a fault in the table rather than a decision
                    for whoever is holding it
         SOURCE     brief Part I O2; bar Part III O1/O2

  FWD-3  Anything that needs to know where a firm's data lives looks it up in one
         place instead of having the answer written into it
         DONE WHEN  APPLIED -- each of them reads it from the one place
         ACCEPT     someone changes where one firm's data lives in a single place,
                    and everything that serves, guards or directs that firm's data
                    follows from that one change, with nobody editing it in several
                    files -- where today the same firm is written eight different
                    ways in eight different places
         SOURCE     brief Part I O3; bar Part III O3

  FWD-4  A firm's people see exactly what they saw before on the day their data
         moves, and cannot tell from looking that anything happened
         DONE WHEN  EXERCISED -- a firm has actually been moved and the result was
                    read back deliberately
         ACCEPT     after a firm's data is moved, someone deliberately compares what
                    is being served now against what was served before and finds it
                    identical for everything a user can reach; the sign-off named
                    every piece that moved and how to put each one back; and the old
                    copy is still sitting there untouched for the agreed period.
                    A real user opening the page and noticing nothing is the
                    CONFIRMATION, never the proof
         SOURCE     brief Part I O4; bar Part III O4

  FWD-5  Whoever owns a pipeline can see that everything which sets it running now
         points at the new home, and nothing points at the old one
         DONE WHEN  EXERCISED -- the owner has read the live settings and found it so
         ACCEPT     the person responsible for a pipeline reads the live settings
                    themselves and finds nothing still aimed at the old home, and
                    everything that ought to start their pipeline present on the new
                    one -- read from what is actually running, never from a written
                    procedure that says it was done
         SOURCE     brief Part I O5; bar Part III O5

  FWD-6  An operator can prove, before anything is thrown away, that nothing used the
         old home for an agreed stretch of time
         DONE WHEN  EXERCISED -- the proof has been produced and read for a real case
         ACCEPT     before anything is deleted, the operator shows a record that
                    nothing wrote to the old home and nothing read from it for the
                    whole agreed stretch, measured by a named instrument rather than
                    asserted from memory; everything that pointed at it has been
                    moved or switched off; and throwing the old copy away is treated
                    as its own decision needing your word, because here "deleted" can
                    mean only "hidden" -- where today "retired" means "nobody
                    remembers anyone using it"
         SOURCE     brief Part I O6; bar Part III O6

  FWD-7  The one thing this estate is forbidden to write has either a named
         replacement or a recorded decision to let it go
         DONE WHEN  EXERCISED -- someone has actually pointed at the decision
         ACCEPT     someone asked what became of it points at one recorded decision
                    saying either what took its place, or that nothing did and the
                    thing that watched for it was switched off with it
         SOURCE     brief Part I O7; bar Part III O7/O8

  FWD-8  Something deliberately allowed to stay where it is, inside a place being
         shut down, is either moved by a decision or the place stays open for it
         DONE WHEN  EXERCISED -- someone has actually read the disposition
         ACCEPT     someone reads, in one place, either where it now lives together
                    with the decision that moved it, or the sentence that keeps the
                    old place open for that one thing -- and neither is left to be
                    discovered by whoever is doing the shutting down
         SOURCE     brief Part I O8; bar Part III O7/O8
```

## CONTRACTS

| contract | direction | shape | consumer / producer |
|---|---|---|---|
| the canonical key string, in the firm buckets | **consumed** (ruled) | `{source}/{scope}/{tier}/{table}/{partition}` verbatim, the bucket as its container and the object as its leaf. In a firm bucket, `{scope}` MUST EQUAL that bucket's own firm in the LONG form (`49financial`, `inflection`, `cottonwood`). `{tier}` is `gold`, `platinum` or `state` (R21: `{source}/{scope}/state/{family}/...`), because bronze and silver never live in a firm bucket (R4); `code` is the held family below. The vectors: `key("advi", "49financial", "gold", "fact_account_gains", "date=2026-09-11")` returns `advi/49financial/gold/fact_account_gains/date=2026-09-11`, whose object is `data.parquet`; and `key("advi", "49financial", "platinum", "firm", "header_metrics.json")` returns `advi/49financial/platinum/firm/header_metrics.json`, with the served file in the partition slot the schema calls "a named leaf". **A legacy served file keeps its name byte-for-byte, snake_case included** (`header_metrics.json`; `3.0.0_SA_CVO` reads 12 of 15 ADVI served leaves as snake_case in `adviKeyRepoint.ts` @portal `3ade1aba`), because the frozen portal requests each file by name. The schema's kebab-case rule (`NAMING_SCHEMA` `:35`) governs only NEW served names. Recording that admission is `LGIC_NAMING`'s, in the row `3.0.0_SA_CVO` files there as LGIC_NAMING-S8; until it is recorded, no served file is renamed to satisfy the schema, and none is hand-spelled around a builder that refuses its name. `address()` puts each under `s3://opal-data-49financial/`. **Every NEW address comes from `LGIC_ENFORCE`'s `key()` and `address()`, never typed -- and a family the builders cannot yet construct is HELD, never hand-spelled.** The legacy buckets' existing keys are inputs to the mapping table, not outputs. **Two families are held.** Entity-keyed served files (such as a book per advisor) have NO schema form yet: none is written until `LGIC_NAMING` resolves row LGIC_NAMING-S6. **Code** (R16) has TWO forms that disagree: the brief's root code home `code/{source}/gold/...` (IV.5, IV.6; doctrine R1's non-application of `code/` prefixes), which no builder returns, and the schema's `code` tier, which `key()` would place at `{source}/{scope}/code/{table}/{partition}`. Which is law is `LGIC_NAMING`'s ruling, raised as row LGIC_NAMING-S7; no code object is written in a firm bucket until it resolves. R16's non-application to Lambda artifacts is unchanged | ruled by Andrew ~03:2xZ and ratified as `LGIC_NAMING` S1; the builders are `LGIC_ENFORCE`'s |
| the mapping table | **produced** | every legacy key class in `opal-data-bd`, `-inf` and `-cot` maps to exactly ONE destination -- a firm-bucket key, an `opal-data-assets` key (bronze and silver go home), a `state/` key (R21), a `code/` key (R16) -- or to RETIRE. A key the table cannot place is a fault in the table, never a case for the person holding it. Two rows are not moves but decisions at Andrew: the prohibited key (FWD-7) and the B2 credential (FWD-8) | the three cutovers; the person placing the keys (FWD-2) |
| the identity registry | **consumed** | the firm's bucket and forms, read from `infra/logic/registry/*.json` and its generated views | produced by `LGIC_ENFORCE` (ruling (a)); every consumer this project repoints reads it (FWD-3) |
| the firm buckets and their serving grants | **produced** | `opal-data-inflection` and `opal-data-cottonwood`, minted from the template `s3-49financial.tf`, each born with the scope-derived fence, read logging, versioning and blocked public access. Every firm bucket, `opal-data-49financial` included, carries the CloudFront serving grants before its router row flips, on exactly its served source prefixes with the bucket's own LONG firm fixed in the scope slot: `{source}/{firm}/platinum/*` for each served source, GENERATED from the mapping table's platinum destinations (F2) and the consuming projects' declared prefixes (today `advi/{firm}/platinum/*` and `MDPF_CANON`'s `mdpf/{firm}/platinum/*`), never a bucket-wide grant. The legacy buckets' OAC grant on `gold/*` (brief IV.9) is NOT carried to the new buckets: gold is not served (R12), so any CloudFront read under a legacy `gold/` key that F1's census finds is a served file the table places in platinum, or a fault in the table | `MDPF_CANON` (its firm slices); `IRPT_BCKEND` (its per-firm platinum); the edge routers |
| the separation rule | **consumed** | `LGIC_ENFORCE`'s scope-derived Deny on each firm bucket, applied on the template before either new bucket is minted | produced by `LGIC_ENFORCE` (its cell E5; the sequence's manual gate) |
| the tenant assertion | **produced** | the path's firm segment resolves through the registry, aliases included, to one firm, and a scoped request is served only when that firm's bucket equals the caller's validated tenant bucket: the session's firm through the same map, or for internal Opal staff (`opal-capital`) the `?firm=` selection they already supply. The key is then BUILT with `{scope}` equal to the resolved firm, never copied from the raw path, so a key's scope always equals its bucket's firm. This is today's boundary, no wider and no narrower (`shared-advisor-router/index.mjs:367-373` @`40697fe79d`): the `mockadv` alias and the staff proxy keep working, and another firm's session is refused. The response guard re-derives this on its own and never imports the router's decision | the scoped router and the response guard at the edge; LD-0442's remedy |
| served bytes across a cutover | **produced** | every served key answers from the new bucket with data-bearing leaves identical to the old, and the old bucket stays unmodified through the rollback window | every firm's users |
| the decommission standard | **produced** | per legacy bucket: 45 CONSECUTIVE days in which a named instrument records no data event on the bucket, READ OR WRITE, other than an excluded probe. It starts no earlier than that instrument's observed-live stamp and counts only after the firm's cutover; any other event restarts it. Every removal, and every per-version delete on a versioned bucket, is its own act needing Andrew's word, because on a versioned bucket "deleted" can mean only "hidden" | this project's retirements; `MDPF_CANON`'s FWD-8, which inherits it |
| inherited law | **consumed** (ruled) | the canon's R1, R4-R7, R9, R11, R12, R16-R19 and R21; rows B1 and B2; the template's born-with controls; LD-0442; the S3-notification singleton hazard (`OPAL_ASSETS_CONSOLIDATION_PRD.md` s.2b); Door 6, the one prohibited key (`OPAL_ASSETS_CONSOLIDATION_PRD.md` s.0) | Andrew's words; the law surface |

## THE DECISIONS -- CLOSED AT L4

- **DEC-1 The key string is ruled, and the brief's IV.5 is recorded, not re-decided.**
  - The brief's worked strings are rewritten to the five segments plus an object. The served-file families use the
    "named leaf" partition (CONTRACTS).
  - **One gap is raised, not papered over.** Entity-keyed served files, such as `platinum/advisors/{id}/book.json`,
    fit neither of `NAMING_SCHEMA.json`'s two partition forms (`date=YYYY-MM-DD`, "a named leaf").
  - The form this PRD proposes is a hive entity partition, `{source}/{firm}/platinum/{table}/{entity}={id}/{leaf}.json`.
    The canon's R2 already sanctions an entity id inside a partition, never in the scope slot.
  - The schema is `LGIC_NAMING`'s, so the proposal is raised as row LGIC_NAMING-S6 for an addendum there. The cells
    that write entity-keyed served files wait on it.
  - No key in that family is hand-spelled in the meantime.
- **DEC-2 The mapping table (brief IV.6) is ratified as the FWD-2 rule.** Its rows are restated in the five segments.
  - Served JSON becomes platinum whatever it was called (R12).
  - Analytical files become gold parquet (R5, R11).
  - Operational state goes to `state/` (R21).
  - Code goes to its R16 home, and its construction is HELD on row LGIC_NAMING-S7: F2 places every code key by
    class, and no code object is written until the row resolves. The row decides one vector: `opal-data-bd/code/gold/
    <runner>.py` becomes either `opal-data-49financial/code/advi/gold/<runner>.py` (the brief's root code home) or
    `key("advi", "49financial", "code", "gold", "<runner>.py")`, which is `advi/49financial/code/gold/<runner>.py` (the
    schema's `code` tier). The runners keep reading the legacy code home until then.
  - Bronze and silver go home to `opal-data-assets` (R4).
  - Retire candidates are retired only after `comp-blast` clears each one for a live reader (R17, R18).
  - The prohibited key (FWD-7) and B2 (FWD-8) are their own rows, and decisions.
- **DEC-3 The tenant grain, which is this seat's call under LD-0442.**
  - The path's firm segment resolves through the registry, aliases included, to one firm. The request is served only
    when that firm's bucket equals the caller's validated tenant bucket: the session's firm through the same map, or
    for internal Opal staff the `?firm=` selection they already supply.
  - The key is then BUILT with `{scope}` equal to the resolved firm, never copied from the raw path. A second firm's
    twins inside one bucket can then never be addressed through another firm's session.
  - This keeps today's boundary, no wider and no narrower (`shared-advisor-router/index.mjs:367-373` @`40697fe79d`).
    A bare segment-equals-tenant test would refuse the `mockadv` alias and Opal's own staff, and neither is another
    firm.
  - The response guard re-derives the bucket on its own; it 502'd on the first exercised fetch when it did not know a
    new bucket (brief IV.7).
- **DEC-4 Each firm is its own cutover** (R19). 49 Financial goes first, as a dependency claim: its bucket exists and
  its gold is there. Cottonwood may go before Inflection, because every act on `opal-data-inf` waits on Andrew's two
  rulings (DEC-13). Per firm:
  1. a change-management ledger entry is opened;
  2. the serving grants land on the destination, and representative mapped keys are read through the CloudFront access principal and the page's own route, with another firm's session refused;
  3. the objects are copied by the mapping table, their keys generated by the builders;
  4. the served bytes are compared on data-bearing leaves;
  5. the router row flips, under never-widen sign-off (CTO and COO) that names every served key and its rollback;
  6. the before-and-after comparison is run and read;
  7. the old bucket stays untouched through the rollback window.

  A real user noticing nothing confirms it and never proves it.
- **DEC-5 Minting the two buckets.**
  - They are minted only after `LGIC_ENFORCE` applies its fence on the template, which is the sequence's manual gate.
  - Each is born with read logging, through the template's selector list (card 3).
  - **R-AC15's two residuals, carried (tree row, blocking 4a):**
    - the selector list is literal strings, so the apply orders the selector update AFTER the bucket's creation, by
      an explicit dependency;
    - a deliberate probe read after the apply stamps that bucket's observed-live time.
- **DEC-6 The router's firm map, the response guard's bucket list and IRPT's `FIRM_BUCKET_MAP` are generated from the
  registry** (`LGIC_ENFORCE`'s generated views). The scoped rewrite targets become `advi/{firm}/platinum/...`, in one
  table in the router and one in the response guard.
- **DEC-7 Triggers** (brief IV.8), read from the LIVE plane.
  - Each served-guard rule follows its firm's platinum key. The completion-sentinel rules follow the bronze home to
    the monolith, not to a firm bucket. `inf-otp-state-change` follows `state/`.
  - Scheduled triggers stay as they are, while their Lambdas' configuration repoints.
  - The S3-to-Lambda notification configurations are singletons per bucket, so they are re-created on each
    destination, with the s.2b clobber hazard read first.
  - `inf-canonical-prices-daily` stays DISABLED and HELD, and moving it never re-enables it.
  - **`FIRMSEP-s3-direct-access-bypass` is not an instrument for anything here.** Its SNS delivery has failed on every
    invocation since 2026-05-11, and cot was dropped from it by Andrew ~21:3xZ. Its list follows the buckets only if
    the rule is kept, and its fate is not this project's to rule.
- **DEC-8 Policies.**
  - The three legacy bucket policies are LIVE and not declared in Terraform. They retire with their buckets, after
    cutover.
  - The role-side belts are widened to the new names. That is `NFRA_IAMROLES202609`'s plane, and this project's ask.
  - The existing writers (`bd-exporter-ec2-role`, `opal-advi-stitch-landing-role`, `irpt-directory-refresh-role`) are
    scoped or exempted under `LGIC_ENFORCE`'s DEC-4 (ii) before the fence lands.
- **DEC-9 Bronze and silver go home** (R4). inf's bronze is RE-LANDED raw from its source, never converted (R9). That
  is a call to a vendor's API, so it needs Andrew's per-use word at the act (vendor egress), and the cell says so.
- **DEC-10 FWD-3 is cut at APPLIED, as the endpoint set it.**
  - It waits on `LGIC_ENFORCE`'s registry and generated views (its cells E2 and E6).
  - This project repoints the consumers that compute a firm's location in their own code: the brief's DEF band,
    about 340 definition sites plus about 58 declared surfaces.
  - The history band (534) is never edited.
- **DEC-11 FWD-5 is read from the live plane.** EventBridge Scheduler schedules are invisible to `describe-rule`, so
  they are read through the scheduler's own API.
- **DEC-12 FWD-6: the standard is the CONTRACTS row, and HALF ITS INSTRUMENT IS MISSING.**
  - Reads on all three legacy buckets are recorded (card 3, validated @`231cd62ec5`).
  - **Writes are recorded only under `platinum/firm/`** (the served-key write trail; brief Part V).
  - FWD-6's ACCEPT requires that "nothing wrote to the old home", so a write to `gold/`, `bronze/`, `silver/`, `code/`
    or `state/` during the window would be invisible.
  - **That is one open call at Andrew**, because the logging is billed: record write data events on the three legacy
    buckets. REC: yes.
  - The window counts only after each firm's cutover (~03:xxZ). Until then, the read logging is the census of readers
    the cutover must repoint; cot's `opal-cot-value-parity` is the first named.
- **DEC-13 FWD-7 and FWD-8 are Andrew's, and are carried to him, not decided.**
  - The prohibited key `opal-data-inf/gold/meta/pipeline-complete.json` is his Door 6, watched by the
    `mdpf-feeder-accelerator` rule.
  - B2 (`opal-data-inf/orion/jwt/current.json`) is his standing exception, ruled not to move because moving a live
    credential breaks the chain that refreshes it.
  - **`opal-data-inf` is not TOUCHED until he rules both** (brief Part V). No act that moves, copies, repoints away
    from or writes to it begins before both rulings are recorded: F8, and Inflection's parts of F5, F6, F10, F11 and
    F12. The read-only census (F1) does not wait.
  - Either ruling may keep its object where it is: B2's may keep the bucket open for the credential, and Door 6's may
    name a successor or retire the key with its watcher. Neither is decided here.
- **DEC-14 `mockadv`'s home is carried to Andrew** (brief IV.10). The router maps `mockadv` to 49 Financial's bucket
  today, so retiring `opal-data-bd` moves two map entries. It is a registry alias, never a scope segment. REC: it
  follows 49 Financial, which keeps today's routing unchanged.
- **DEC-15 Records and holds** (brief IV.12). Every hold that names a legacy bucket is re-pointed, or closed
  SUPERSEDED, before that bucket is decommissioned. Deploy ledgers stay as history.
- **DEC-16 What waits on what.**
  - Every cell that writes, repoints or runs against a new address waits on `LGIC_ENFORCE`'s builders (its cell E3).
  - The entity-keyed served files also wait on LGIC_NAMING-S6, and the code family on LGIC_NAMING-S7.
  - Every act on `opal-data-inf` waits on Andrew's FWD-7 and FWD-8 rulings (DEC-13).
  - The minting waits on the fence.
  - The censuses (F1) and the reading exercise's preparation do not wait.
  - Execution past DECOMP waits on the sequence's hold as a whole.
- **DEC-17 Never, in this project:**
  - an apply outside `safe-apply`;
  - a served key moved without never-widen sign-off;
  - a delete without Andrew's word and the FWD-6 proof;
  - a vendor call without his per-use word;
  - any change to `opal-data-demo`;
  - a held rule re-enabled;
  - a dual write or a shadow copy;
  - a bucket-wide serving grant, or a code object written before LGIC_NAMING-S7 resolves.

## PROJECT ARC AND DEFINED OUTCOME

**Defined outcome:**
- Every key in the three firms' data reads the same way in every bucket.
- Every legacy key has one home, by one table.
- Every pointer reads one registry.
- Each firm moved without its users noticing, with every trigger on the new home.
- Each legacy bucket is retired only on a 45-day record, read and write, from a named instrument, and by Andrew's word.

**Arc:**
1. The censuses and the mapping table (F1, F2); they need no builder to be read and drafted.
2. The reading exercise (F3).
3. Once the builders and the fence exist: the two buckets and the serving grants (F4), the registry repoint (F5), and
   the router and guard (F6).
4. The three cutovers, one firm at a time (F7 to F9), each with its triggers (F10) and its bronze and silver (F11).
5. Per bucket, after its cutover: the 45-day record and the retirement (F12).
6. The two dispositions at Andrew (F13).

It closes when every FWD grades REALIZED.

## CELL CANDIDATES

One row per candidate cell. The decomposition at L5 is the COO lane's, and it may split, merge or re-sequence these.

| cell | serves | brief sections consumed | contracts consumed (C) / produced (P) | paths: reuse | paths: new home | fixtures / evidence | acceptance clause draft |
|---|---|---|---|---|---|---|---|
| F1 the censuses | FWD-2, FWD-3, FWD-5, FWD-6 | IV.1; IV.2; IV.3; IV.12; Part VII | -- | `comp-find` over the repo and the live plane; card 3's read logging | `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/CENSUS.md` | the definition sites; the live nodes; the 228 attributed keys by class; the records and holds; every lifecycle rule read (Part VII); the readers seen on each bucket since read logging went live | every set is printed with its denominator and its instrument; a name census is never offered as proof of absence |
| F2 the mapping table | FWD-2 | O2; IV.3; IV.6 | P the mapping table | the 228 keys (F1) | `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/MAPPING_TABLE.md` and its data twin | each legacy key class placed by the table; a second worker places the whole set alone | every key lands in exactly one destination or RETIRE; the second placement matches; an unplaceable key is logged as a table fault |
| F3 the reading exercise | FWD-1 | O1; Part III O1/O2 | C the key string | the destinations F2 produces | `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/` | two workers who never worked together read the same list of new locations | for every location both name the same system, firm, tier and contents |
| F4 the two buckets and the serving grants | FWD-4, FWD-6 | IV.9; Part V bullets 3-4 | C the fence, the template; P the buckets and grants | `infra/aws/terraform/shared-infra/s3-49financial.tf` | the two new buckets' Terraform | after `LGIC_ENFORCE` E5; a plan per bucket; the selector ordered after creation; a probe read after the apply | both buckets exist born with the fence, read logging, versioning and blocked public access; each carries the serving grants on exactly its served `{source}/{firm}/platinum/*` prefixes and no bucket-wide grant; each has an observed-live stamp; before any router row flips, representative mapped keys read through the CloudFront access principal and the page's own route, and another firm's session is refused |
| F5 the registry repoint | FWD-3 | O3; IV.1 (the DEF band); IV.7 | C the registry, `key()`, `address()` | the DEF band's definition sites | -- | each consumer that computes a firm's location, repointed to read the registry or the builders | changing one firm's row changes every place that serves, guards or directs its data, with no second edit |
| F6 the router, the guard and the tenant grain | FWD-4 | IV.7; Part V bullets 4-5 | C the registry's generated views; P the tenant assertion | `infra/aws/lambda-edge/shared-advisor-router/`, `shared-advisor-router-response/` | -- | the rewrite targets moved to `advi/{firm}/platinum/...`; the guard's list re-derived on its own | through the page's own request path: a firm's own session and its alias are served; an internal staff session with its selection is served; another firm's session is refused; every served key's `{scope}` is the resolved firm |
| F7 49 Financial's cutover | FWD-4 | O4; Part V | C the mapping table, `address()`; P served bytes | `opal-data-bd`, `opal-data-49financial` | the destination keys | a ledger entry; never-widen sign-off naming every served key and its rollback; the data-bearing comparison before and after | every served key answers identically from the new bucket; the old bucket is untouched through the rollback window |
| F8 Inflection's cutover | FWD-4 | O4 | as F7 | `opal-data-inf`, `opal-data-inflection` | the destination keys | as F7; begins only after Andrew's FWD-7 and FWD-8 rulings are recorded (DEC-13); the prohibited key and B2 are then moved or kept exactly as he rules | as F7 |
| F9 Cottonwood's cutover | FWD-4 | O4 | as F7 | `opal-data-cot`, `opal-data-cottonwood` | the destination keys | as F7; `opal-cot-value-parity` and every other reader F1 names is repointed first | as F7 |
| F10 the triggers | FWD-5 | O5; IV.8 | C the registry | the live EventBridge rules and Scheduler schedules; the S3 notification configurations | -- | per firm: the pattern rules repointed, the notification singletons re-created, the Lambdas' configuration repointed | each pipeline's owner reads the live settings and finds nothing aimed at the old home, and every trigger present on the new one |
| F11 bronze and silver home | FWD-2, FWD-5 | IV.6 (class d); R4, R9 | C the key string, `address()` | the legacy buckets' ingest tiers | `opal-data-assets/{vendor}/{firm}/{bronze,silver}/` | bd's and cot's copied; inf's bronze re-landed raw from its source on Andrew's per-use word, after his FWD-7 and FWD-8 rulings | every ingest key is in the monolith at builder-generated keys; nothing is converted on the way |
| F12 the retirement proofs | FWD-6 | O6; IV.12; Part V | C the decommission standard | the read and write instruments; the holds F1 names | `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/` | per bucket, after its cutover: the 45-day record, read and write; every pointer moved or off; every hold re-pointed or closed; the policies and state removed; the delete put to Andrew | the record shows no event but the excluded probes for 45 consecutive days on a named instrument; the delete is his word, act by act |
| F13 the two dispositions | FWD-7, FWD-8 | O7; O8; IV.10 | -- | his rulings | `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/` | the recorded decision for the prohibited key and for B2, recorded before any act on `opal-data-inf` | a reader points at one recorded decision for each |

## PATHS

| kind | path | cell | use |
|---|---|---|---|
| new | `s3://opal-data-inflection/`, `s3://opal-data-cottonwood/` and their Terraform on the template | F4 | the two new firm buckets |
| new | `s3://opal-data-{firm}/{source}/{firm}/{gold,platinum,state}/...` | F7-F9 | the destination keys, generated by the builders; the code family is held on LGIC_NAMING-S7 |
| new | `s3://opal-data-assets/{vendor}/{firm}/{bronze,silver}/...` | F11 | the ingest tiers' home |
| new | `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/` | F1-F3, F12, F13 | the censuses, the table, the exercises, the proofs |
| edit | the DEF band's definition sites and the declared surfaces (brief IV.1) | F5 | the registry repoint |
| edit | `infra/aws/lambda-edge/shared-advisor-router/`, `shared-advisor-router-response/`, the IRPT firm map | F6 | the rewrite targets and the tenant assertion |
| edit | the live EventBridge rules, the Scheduler targets' configuration, the S3 notification configurations | F10 | the triggers |
| edit | the three legacy bucket policies, and the role-side belts through `NFRA_IAMROLES202609` | F12, DEC-8 | retired with their buckets; the belts widened |
| read | `infra/logic/02_DOCTRINE.md`, `05_IDENTITY_SPINE.md`, `06_CONFORMANCE_LEDGER.md`, `07_ROUTING_REDERIVATION.md` | F1-F13 | the substrate |

## BRIEF COVERAGE

**Denominator.** The brief @`2b64208047` has **30 headings outside code fences**:
- 8 top-level: the title and Parts I to VII;
- 8 outcomes, O1 to O8;
- 13 findings, IV.1 to IV.13;
- `## REFS TO CARRY`.

Each is an entry. Every entry maps to a decision, a cell and an outcome, or carries `NOT CONSUMED` with its reason.

| # | entry | consumed by | outcome |
|---|---|---|---|
| 1 | title / preamble | the preamble above; DEC-17 | all |
| 2 | PART I heading | structural | -- |
| 3 | O1 a key read the same in every bucket | DEC-1; F3 | FWD-1 |
| 4 | O2 one rule for every legacy key | DEC-2; F2 | FWD-2 |
| 5 | O3 every pointer through the registry | DEC-6, DEC-10; F5 | FWD-3 |
| 6 | O4 the same dashboard the morning after | DEC-3, DEC-4; F6-F9 | FWD-4 |
| 7 | O5 every trigger on the new bucket | DEC-7, DEC-11; F10 | FWD-5 |
| 8 | O6 retirement on a proven quiet window | DEC-12; F12; the decommission row in CONTRACTS | FWD-6 |
| 9 | O7 the prohibited key | DEC-13; F13 | FWD-7 |
| 10 | O8 the exception inside a retiring bucket | DEC-13; F13 | FWD-8 |
| 11 | PART II the boundary | CONTRACTS; DEC-10 (the repoint is this project's, the registry is `LGIC_ENFORCE`'s); DEC-8 | all |
| 12 | PART III the qualitative bar | the ENDPOINT's ACCEPT lines; the acceptance drafts | all |
| 13 | PART IV heading | structural | -- |
| 14 | IV.1 the repo's 781 files; the DEF band | F1, F5; DEC-10 | FWD-3 |
| 15 | IV.2 the live plane's 249 nodes | F1 | FWD-5, FWD-6 |
| 16 | IV.3 the 228 keys in five classes, plus the code class its body names | F1, F2; DEC-2 (code held on LGIC_NAMING-S7) | FWD-2 |
| 17 | IV.4 two grammars disagree | DEC-1 (the ruled string supersedes the template's tier-first form) | FWD-1 |
| 18 | IV.5 the canonical path strings | DEC-1; the key-string row in CONTRACTS; LGIC_NAMING-S6 and S7 | FWD-1, FWD-2 |
| 19 | IV.6 the mapping table | DEC-2; F2 | FWD-2 |
| 20 | IV.7 the portal's pointers | DEC-3, DEC-6; F6 | FWD-3, FWD-4 |
| 21 | IV.8 EventBridge rules and schedules | DEC-7; F10 | FWD-5 |
| 22 | IV.9 policies and serving grants | DEC-8; F4; the grants row in CONTRACTS (source-first prefixes; the legacy `gold/*` OAC grant not carried) | FWD-4, FWD-6 |
| 23 | IV.10 two rulings inside `opal-data-inf`; `mockadv` | DEC-13, DEC-14; F13 | FWD-8 |
| 24 | IV.11 the fence and the runner's name | the separation rule in CONTRACTS (`LGIC_ENFORCE` E5, ruled ~18:4xZ card 1); DEC-8 | FWD-4 |
| 25 | IV.12 the records that name the buckets | DEC-15; F1, F12 | FWD-6 |
| 26 | IV.13 what the identity spine resolved | the registry row in CONTRACTS (the runtime is `LGIC_ENFORCE`'s) | FWD-3 |
| 27 | PART V what must be true | the registry before the first flip (DEC-10); the string ratified (DEC-1); the buckets and grants before cutover (DEC-5, F4); read logging at mint (DEC-5); the tenant grain (DEC-3); the independent guard (DEC-3); FIRMSEP (DEC-7); inf's bronze re-landed (DEC-9); O7 and O8 before `opal-data-inf` (DEC-13); the runner's name (the fence row); `mockadv` (DEC-14); never-widen per served key (DEC-4); the window and its instrument (DEC-12); the per-version delete (the decommission row); each firm its own cutover (DEC-4) | all |
| 28 | PART VI status | NOT CONSUMED: not outcome-bearing; its clocks are superseded (the pause lifted, card 3 delivered) | -- |
| 29 | PART VII what the brief does not claim | producers untraced (F1); schedules read from the map (DEC-11); the rules' targets and the notification targets unread (F10); the template beyond its header (F4 reads it); CloudTrail coverage (DEC-12); lifecycle rules unread (F1); FIRMSEP dark (DEC-7); the belts unread (DEC-8); the COO's 08-21 rejection unread (F6 reads it first); per-class object counts (F1). Effort: NOT CONSUMED, and no estimate is made here | all |
| 30 | REFS TO CARRY | NOT CONSUMED as work: a link list. Its WAITING-ON items: IV.5 ratified (DEC-1); O7 and O8 (DEC-13, at Andrew); `mockadv` (DEC-14, at Andrew); the runner's name (the fence row); the tenant grain (DEC-3) | -- |

## SURFACE MANIFEST

Surfaces this project writes, reads or executes.

| surface | kind | cell | owner |
|---|---|---|---|
| `opal-data-inflection`, `opal-data-cottonwood` | APPLIED: two new buckets on the template | F4 | ADVI_FIRMBKTS, through the infrastructure lane and `safe-apply` |
| the serving grants on each firm bucket's served `{source}/{firm}/platinum/*` prefixes | APPLIED: bucket-policy grants, never bucket-wide | F4 | ADVI_FIRMBKTS, through the infrastructure lane |
| the destination keys in the three firm buckets | APPLIED: served data moves; never-widen sign-off per served key | F7-F9 | ADVI_FIRMBKTS |
| `opal-data-assets/{vendor}/{firm}/{bronze,silver}/` | APPLIED: ingest tiers move home; inf's bronze re-landed on Andrew's per-use word | F11 | ADVI_FIRMBKTS |
| the edge routers and the response guard | APPLIED: rewrite targets and the tenant assertion | F6 | ADVI_FIRMBKTS, through the infrastructure lane |
| the DEF band's definition sites and declared surfaces | edits | F5 | ADVI_FIRMBKTS; deploys ride their owners' paths (Rule 13) |
| the live EventBridge rules, Scheduler targets and S3 notification configurations | APPLIED: repointed or re-created | F10 | ADVI_FIRMBKTS, through the infrastructure lane |
| the three legacy bucket policies; the role-side belts | retired with the buckets; belts widened | F12, DEC-8 | ADVI_FIRMBKTS; `NFRA_IAMROLES202609` for the belts |
| `opal-data-bd`, `opal-data-inf`, `opal-data-cot` | REMOVALS: each only after its 45-day record, and each delete on Andrew's word | F12 | ADVI_FIRMBKTS |
| `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/` | documents | F1-F3, F12, F13 | ADVI_FIRMBKTS |
| `opal-data-demo`; `inf-canonical-prices-daily`; the prohibited key and B2 until Andrew rules | excluded | -- | untouched |
