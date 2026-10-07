# L1 BRIEF -- package intake and download tiers: how anything from the internet reaches an Opal box

**Author:** `4.0.0_SA_CRO` (Chief Research Officer), 2026-10-07. **Mode:** NEW scope, added to a project in flight.
**Project:** NFRA_CTLPLN (the four-box control plane, directive D0). This is an ADDITION to it, not a new project:
`1.0.0_SA_CTO` ruling msg 106288. After this brief: the CTO's PRD addendum (new outcomes at the next unused numbers,
FWD-15 onward), then `2.0.0_SA_COO~C` cuts.
**Consumer:** `/endpoint --forward` at L2 (`1.0.0_SA_CTO`).

**Andrew's words, VERBATIM** (three, all 2026-10-07; carrier
`org/tier0_exec/0.0.0_AB_MSTR/deliverables/DELL_BUS_RELAYS_FOR_CTO_20261007_1405Z.md`, records @50df0c2e97, @9e5f28e155,
@e031cd6991 on the two Dell record branches):

1. At the dell2 terminal, ~13:39Z: "High risk downloads include any kind of script/executable (unless it is from a
   tailnet device, sent over taildrop or via git), these are red and should never, ever be downloaded off the raw
   internet. Libraries/packages are yellow, I don't really want any npm/npx packages. Python libraries are also yellow.
   What is preferable is if there is a true dependency, a library that is absolutely needed, it is preferable for the
   laptop device to check it out first, and if clean and clear, it can be taildropped."
2. At the dell2 terminal, earlier: "Websearch is fine, but downloading needs to be gated".
3. At the dell1 terminal, ~14:0xZ: "Ok i like this policy, particularly the framework around approved packages being
   included on requirements.txt. I think there should be some kind of request pipeline for additions to
   requirements.txt and a review process. I would issue all of this information to the laptop, as it is all work that
   should be researched, designed, and folded in to NFRA_CTLPLN"

The policy he accepted in word 3 is section 3 of the dell1 record (@9e5f28e155): install only what
`requirements.txt` lists at an exact version; wheels only; an addition is a reviewed commit, ideally with hashes;
npm and bun fetching stays blocked; the laptop fetches and checks, then Taildrops.

**This brief is not blind to the project.** NFRA_CTLPLN's kit cells were read on purpose (Part IV): the scope is new,
and the kit is what it builds on.

Terms: a **wheel** is a pre-built Python package file that installs without running a setup script. **Taildrop** is the
tailnet's file transfer between Opal's own devices. **The kit** is NFRA_CTLPLN's set of tools that bring a new box to
the laptop's state.

---

## PART I -- THE OUTCOME TERRITORY

### I.0 The candidate thread (one journey, end to end)

**Who:** a lane on a Dell whose work needs a compiled Python package the box cannot be given offline.
**Journey, coarse grain:** one real package from the first batch (finding F11), `PyYAML==6.0.3`: on the approved
list, used by 124 files, installed on the laptop only as a build for Python 3.12, which the Dell's Python 3.14 refuses.
The lane sees it is approved; the laptop fetches the one exact file for the Dell's Python, checks it, and sends it over
the tailnet; the Dell installs it from that file alone; the lane's import works. During all of it the Dell makes no
request to any package index, and a person can read afterwards what was checked, what was not, and by whom.

`1.0.0_SA_CTO` ruled (msg 106318) that the 30 packages of F11 are the first batch this scope carries end to end. The
thread is one of them; the other 29 follow by the same route. The request and review of a NEW package name (O2, O3) is
the enrichment after the batch: every one of the 30 is a version the laptop already runs.

### O1 -- A seat on any box can tell whether a package is approved

Someone about to install a package looks in one place and reads "approved at this exact version" or "not approved". The
place is `requirements.txt` (word 3).

### O2 -- A seat that needs a package not on the list can ask for it

Someone files one request and knows what it must say: the package, the exact version, the file that needs it, and why
nothing already approved or built into Python will do. The request is a file a later reader can find, not a message.

### O3 -- A reviewer decides from the request, and the decision can be read afterwards

Whoever reviews answers yes or no against a fixed list of checks, and Andrew can later read who approved which package,
on what evidence, and when.

### O4 -- A person can say what "checked, clean and clear" covered, and what it did not

For any package that reached a box, someone can state the checks the laptop ran before sending it, and name the risks
those checks do not rule out. "Clean" is never asserted beyond what was measured.

### O5 -- A Dell installs only what the laptop delivered

A seat on a Dell that tries to install a package from the internet is refused on the box, and the refusal names the
route that works. What it installs is the delivered file, verified against the record made on the laptop.

### O6 -- Nobody downloads a script or a program off the raw internet

A seat that reaches for a script or an executable from a public address has no route to it. It gets the file from
another Opal device over the tailnet, by Taildrop or by git, or it does not get it (word 1: "never, ever").

### O7 -- A seat that needs the portal's JavaScript packages gets them without a fetch

Someone building the portal on a Dell has its dependencies from the kit. No npm, npx or bun download happens, including
the silent one bun makes on its own (word 1: "I don't really want any npm/npx packages").

### O8 -- A lane waiting on a package is visible, not stuck

When a cell needs a package that is not yet approved or delivered, the lane holds that cell, files the request, and
keeps working elsewhere. Andrew sees the wait in the same place he sees every box's open decisions.

### O9 -- Every box runs the same version of each tool the gates call

A seat on any box runs the commit gate and gets the laptop's answer, because the tools the gates call (the linter
first) are on the approved list at one version and delivered the same way.

### O10 -- Andrew can ask what a box fetched from the internet, and get an answer

Asked "what did dell1 download today?", someone can answer from a record, on demand. Today's four fetches were found
because seats noticed and filed rows, not because anything could be asked.

---

## PART II -- WHERE THE BOUNDARY SITS

### II.1 This scope OWNS

- The approved list's meaning: what a line in `requirements.txt` permits.
- The request, its carrier and its review.
- The laptop's fetch-and-check step, and what "checked" is.
- The refusal on a Dell of any install that did not come by the delivery route.
- The red tier's rule and where it is refused.

### II.2 It RELIES ON and does not own

- **NFRA_CTLPLN's kit** (contracts C-KIT and C-KIT-PYTHON, PRD v0.14; cell CT-k-2): the census, pack and install tools.
  This scope adds the front half to them (request, review, fetch, check). It does not rebuild delivery.
- **NFRA_CTLPLN FWD-12** (one decision list on the laptop): O8 uses it.
- **The bun disarm** (row NFRA_CTLPLN-S13; `org/devices/kit_bun_no_egress.py`) and the portal tree pack
  (`org/devices/kit_portal_tree.py`): O7 is their outcome stated for a person.
- **The census that generates `requirements.txt`** (`3.0.0_SA_CVO`'s build script): see finding F2.
- **Taildrop and the tailnet.**

### II.3 NOT this scope -- named so no decomposition re-opens it

- **What each Lambda bundles for AWS.** 28 requirements files sit beside Lambdas under `infra/aws/lambda/`. They are
  built and shipped by other pipelines. Whether the tiers bind those builds is call C in Part V, not assumed here.
- **Vendor API calls.** Already ruled: no vendor call without Andrew's per-use word. A download is not an API call and
  this brief does not merge the two rules.
- **Web search and reading web pages.** Permitted by word 2.
- **Terraform providers and the AWS command line.** Programs, delivered today by the kit
  (`org/devices/kit_terraform_providers.py`). They are executables, so the red tier touches them: call B in Part V.
- **Site Z and the laptop as RECEIVERS.** His words were spoken at the Dells about the Dells. Whether the same tiers
  bind site Z, and bind the laptop's own seats when it is not acting as the checker, is call A.

---

## PART III -- THE QUALITATIVE BAR

No number here is a target.

- **O1.** Two seats on two boxes asked "may I install X?" give the same answer without asking anyone.
- **O2.** A request can be judged by someone who was not in the conversation that produced it.
- **O3.** A refusal is as readable as an approval. The alternative it displaces is today's: a worker installed a linter
  from the public index to get past a gate, and the decision was made by nobody.
- **O4.** The statement of what was checked survives the question "would this have caught a package whose own
  maintainer account was taken over?" with an honest answer, even when that answer is "no".
- **O5.** The Dell's refusal is shown by trying: a real install attempt against the public index, made on purpose, is
  stopped, and the delivered file then installs.
- **O6.** A seat cannot comply by accident and fail by accident. A tool that fetches a program as a side effect (a
  browser driver, an auto-installing runtime) is covered, not only a download a seat types.
- **O7.** The count of requests leaving the box is what is measured, not the absence of an error. A blocked fetch and a
  disabled fetch print the same error (the bun tool's own header says so).
- **O8.** A lane that hits a missing package loses the one cell, not the round.
- **O9.** A commit that passes on one box passes on another.
- **O10.** The answer comes from something written at the time, not from a seat's memory of what it did.

---

## PART IV -- THE SUBSTRATE: what exists to build on

Each finding states what was measured, at the laptop, 2026-10-07 ~14:5xZ, working tree near `eb29bf7f37`.

**F1. The approved list exists and is close to the accepted policy, with two gaps.** `requirements.txt` (root, written
@bc10584676): 67 installable lines; 65 carry an exact `==` pin; 2 carry no pin (`botocore` is one, with its reason in
the file); 0 carry a hash. The accepted policy says exact version on every line and "ideally with hashes".

**F2. The list is GENERATED, and its header says do not hand-edit.** It is produced by
`org/tier1_exec/3.0.0_SA_CVO/deliverables/REQUIREMENTS_CENSUS/build_requirements.py` from a read of what the tracked code
imports, pinned to what the laptop has installed. So today the file answers "what does the code import here", and
Andrew's word 3 asks it to answer "what is approved". Those are different questions with one file. A reviewed addition
by hand and a regeneration by script will overwrite each other unless the design says which one owns the file.

**F3. Delivery is built; it carries only what is already on the laptop.** `org/devices/kit_python_census.py`,
`kit_python_pack.py`, `kit_python_install.py` (cell CT-k-2, @5e1482a22a). The pack writes each file's SHA-256 into a
manifest; the install verifies every file against it, refuses the whole set on one mismatch, and every pip command
carries `--no-index`. The pack states "NO PACKAGE INDEX, NO NETWORK": it never fetches. So O5's mechanics exist, and
the laptop's fetch-and-check step (O4) does not exist anywhere.

**F4. The pack cannot serve a compiled package to a box on a different Python version.** The laptop runs Python
3.12.10. The pack rebuilds a compiled package from installed files only when the target's Python minor version equals
the laptop's, and refuses otherwise. The Dells are reported on Python 3.14 (the dell1 record's review checklist names
`cp314 win_amd64`; the CTO's ruling names "the Python 3.12 against 3.14 wheel gap"); not measured from here. If so,
every compiled package on the list (pandas, pyarrow, lxml and others) needs a real wheel for the Dell's version, and
that wheel can only come from the public index, through the laptop. The laptop's pip cache held 0 wheels when the pack
was built (row at `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md:1143`).

**F5. Two lists of "required" exist and they differ in scope.** `org/devices/kit_python_required.json`: 20
distributions, read from `.tools/` and `lib/` only. `requirements.txt`: 67 lines, read from every tracked Python
file. The kit delivers the first; the policy names the second.

**F6. The gate's tool is on the list.** `ruff==0.15.11` is in `requirements.txt` section 2 with the gates that call
it. dell1 held 0.16.10 and the gate refused every Python edit until the laptop Taildropped 0.15.11 (dell1 record).

**F7. The bun fetch is measured and has a tool.** `org/devices/kit_bun_no_egress.py` measures which disarm works on a
box's bun by counting requests at two loopback listeners, and wraps bun with the passing form.

**F8. Four fetches happened today on the Dells, none through any gate** (dell1 record, section 2): about 487 npm
packages by `bun install` during provisioning (row MDPF_SECCLASS-S54); `pip install ruff==0.15.11` by a worker (row
MDPF_SECCLASS-S49); `react` and `react-dom` auto-installed by bun on dell2; `left-pad` fetched by a probe on dell2.

**F9. Nothing found refuses a red-tier download.** No tool or hook was found that stops a seat fetching a script or a
program from a public address. The Dells' cloud policies govern AWS, not the box's own network. This is an absence
found by reading the kit and the hook list, not an exercised refusal.

**F10. One approved line is itself a red-tier fetch.** `requirements.txt` line 11 gives, as the install step for
browser automation, `python -m playwright install`. That command downloads browser programs from the public internet.

**F11. The first batch is measured: 30 packages need a fetch for the Dells' Python.** Source:
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~13/PYTHON_WHEELS_NEEDING_A_FETCH_FOR_CP314.md`
@bd489b912b (read in full; not re-measured). Of the 67 lines, 41 are pure Python and 8 are builds that fit any
Python version: those 49 are re-packed offline and go in the kit now (CTO msg 106318). 18 lines exist on the laptop
only as a Python 3.12 build (among them pandas, numpy, pyarrow, PyYAML, lxml, scipy, torch). 12 more compiled packages
are needed by lines of the file and are not lines themselves (among them aiohttp, cffi, charset-normalizer, regex,
greenlet). 18 + 12 = 30. No wheel file for any of them is on the laptop. Whether a Python 3.14 Windows wheel exists
for each pinned version was not tested by anyone.

**F12. The approved list is not closed.** The same file lists 73 packages that lines of `requirements.txt` depend on
and that are not lines themselves. An install with no index fails on the first one; an install with an index would
fetch names nobody approved. The CTO has filed this with the file's author (`3.0.0_SA_CVO`). For this scope it means:
"approved" has to cover every package that arrives, not only the ones a seat asked for by name.

**F13. The laptop cannot import-test a Python 3.14 package.** The laptop holds no Python 3.14 interpreter (a
`Python314` folder exists with no `python.exe`; row NFRA_CTLPLN-W13-S15). Whatever the laptop's check is, it does not
include running the package on the Dell's Python. The first import happens on the Dell.

**Prior art to carry:** the dell1 record's analysis (why Python packages are not safe by default; why an agent
guessing a package name is the realistic way in; why version drift was today's actual cost) and its seven open design
questions. They are the design's inputs and are not repeated here.

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

Named, not ordered.

- Which artifact owns the approved list, given F2: the generated census, a reviewed file, or one checked against the
  other.
- What the laptop's check consists of. A hash proves the file is the one the index published. It does not prove the
  package is benign. Candidates named by the dell1 record: maintainer and release history, closeness of the name to a
  popular one, whether a wheel exists for the box, the packages it pulls in, the licence. Which of these are measured
  by a tool and which are a person's reading must be said.
- Who reviews (call D).
- The approved list is closed under dependencies (F12) before any batch is fetched, so that the set fetched is the set
  approved.
- A place on the laptop where a fetched file waits between "fetched" and "checked", so an unchecked file is never the
  one Taildropped.
- The standing moratorium (CLAUDE.md, hard stops): no alert, monitor or notification is built unless Andrew asks. O10
  is an answer on demand from a record. It is not a monitor, and the design must keep it that way or put the question
  to him.
- The refusal on a Dell (O5, O6) is a gate on work. Andrew asked for gating in words 1 and 2 ("needs to be gated"), so
  it is his ask, not an inferred one. Its exact reach is calls A to C.
- NFRA_CTLPLN's round state: the addendum is cut between rounds.

### V.1 What "checked" can measure for a compiled wheel (asked by `1.0.0_SA_CTO`, msg 106318)

A compiled wheel holds machine code. Nobody reads it. So "checked" is a set of narrower statements, each of which a
tool or a person can make true or false without running the package. Listed with what each one rules out and what it
leaves. Thresholds (how old, how many) are the design's and Andrew's; none is set here.

| # | The check | Measured by | Rules out | Leaves |
|---|---|---|---|---|
| 1 | The file's SHA-256 equals the digest the index publishes for that exact file name | a tool | a file altered in transit or served by an impostor | anything the real project published |
| 2 | Name, version and Python tag are exactly the approved line and the Dell's Python; one file fetched by exact name, no dependency resolution | a tool | a near-name package; a resolver substituting another version or pulling an unlisted package | a wrong approval |
| 3 | The version is one the laptop already runs (true for all 30 in the batch) | a tool, against the laptop's installed set | a brand-new release nobody has used | a build for Python 3.14 that differs from the 3.12 build of the same version |
| 4 | The release's age on the index, and that the project has earlier releases | a tool | a package or release published days ago | an old compromise not yet found |
| 5 | Whether the index shows the file was built from the project's own source repository (a build attestation), recorded as present or absent | a tool | where present: a file uploaded by hand from a stolen account | where absent: nothing; many projects publish none |
| 6 | The wheel is opened as an archive and listed, never installed: its Python files are byte-identical to the laptop's installed copy of the same version; every compiled file is named and counted; no installer, script or start-up hook file is inside that the 3.12 copy lacks | a tool | code added outside the compiled files | code inside the compiled files |
| 7 | Windows' own malware scan of the file on the laptop, verdict recorded | a tool | known malware | anything new or targeted |
| 8 | A person reads the result of 1 to 7 and signs the batch | a person | a tool's silent failure being read as a pass | what none of 1 to 7 can see |

**What no check here rules out:** a compiled file that the real project's own compromised release process published.
Checks 3 and 4 shrink that case by taking only versions that have been public and in use for a while. They do not
close it. O4 exists so that sentence is written beside every delivery.

**Deliberately absent: running the package on the laptop.** Installing or importing it there would execute it on the
box that holds Andrew's administrator sign-in, which is the thing the check exists to avoid, and the laptop has no
Python 3.14 to run it on (F13). If Andrew wants a run before delivery, it needs a place with no credentials: call F.

**Calls for Andrew, each with a recommendation.**

- **A. Do the tiers bind every box, or the Dells only?** REC: every box as a receiver, with the laptop the one box that
  may fetch a yellow package, and only through the checked route. Site Z is the Bloomberg box and holds the same kinds
  of credentials.
- **B. Are programs the kit already carries (Terraform providers, the AWS command line, browser drivers for
  automation) red?** REC: yes, they are executables; they reach a box only from the laptop over the tailnet, as the kit
  does today for providers. The Playwright browser download (F10) moves to the same route or is dropped from the Dells.
- **C. Do the tiers bind what a Lambda bundles for AWS?** REC: not in this scope. Those builds run in AWS's own build
  service, not on a box. Name it as the next scope if he wants it.
- **D. Who approves a request?** REC: `1.0.0_SA_CTO` approves a version change to a package already on the list;
  Andrew approves each NEW package name, once. A new name is the rare, high-risk case; a version bump is the common one.
- **F. Should a package be run somewhere before a Dell runs it?** REC: not for this batch. All 30 are versions the
  laptop already runs. For a NEW package name, yes, and only in a place that holds no credentials; building that place
  is its own item.
- **E. What does a box do for the portal's JavaScript packages?** REC: as today's kit does: the laptop packs the
  existing tree and sends it. No new JavaScript package is added without the same request and review.

---

## PART VI -- STATUS -- NOT OUTCOME-BEARING

Do not cut outcomes from this part. Measured 2026-10-07 ~14:5xZ at the laptop unless marked as reported.

| Item | State |
|---|---|
| `requirements.txt` | 67 installable lines, 65 pinned, 0 hashed, generated, written today @bc10584676 |
| Python on the laptop | 3.12.10 (measured). On the Dells: 3.14 (reported, two sources; not measured here) |
| Python kit (census, pack, install) | built @5e1482a22a; `--no-index` on every install; no fetch step |
| Kit's required list | 20 distributions from `.tools/` and `lib/` |
| Packages both Dells lack | `pandas_market_calendars` (reported, PRD v0.14 C-KIT-PYTHON); it is pure Python and goes in the kit offline |
| First batch needing a fetch | 30: 18 lines of the list plus 12 compiled dependencies (F11; measured by `0.9.0_WK_NFRA_CTLPLN~13`) |
| Dependencies missing from the list | 73 (F12) |
| Python 3.14 on the laptop | none (F13) |
| Fetches on the Dells today | 4 (reported, dell1 record section 2) |
| A refusal of an index install on a Dell | none found |
| A refusal of a red-tier download on any box | none found |
| Lambda requirements files outside the list | 28 |

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- **Nothing on a Dell was measured by this seat.** Python versions, installed packages, hooks and the four fetches are
  as the Dell records and the CTO's ruling report them.
- **That a check can make a package "clean".** It can make specific claims: the file is the published one; the name is
  not a near-copy of a popular one; the version is not hours old. Each leaves a remainder, and O4 exists so the
  remainder is said.
- **That pip resolves the list from a clean start.** The file's own header says no install or dry run was made.
- **How a box's network could refuse a fetch.** Whether the refusal lives in a tool wrapper, a hook, the operating
  system's firewall or the tailnet's rules is design. F9 says only that none was found.
- **The site Z box.** Not read.
- **Whether `requirements.txt` at 67 lines is the right approved list.** It is every package any tracked file imports,
  including one-file uses. Whether each line would pass the review this scope creates was not asked.
- **The JavaScript side beyond the two kit tools named.** The portal's own dependency list was not read.

---

## REFS TO CARRY

```
BRIEF PATH        docs/briefs/nfra-ctlpln-package-intake-and-download-tiers-brief-20261007.md
PROJECT           NFRA_CTLPLN (D0), an addition by PRD addendum; next unused outcome id FWD-15
EXISTING PRD      org/missions/D0/NFRA/NFRA_CTLPLN/prd/NFRA_CTLPLN_PRD.md (v0.14: C-KIT-PYTHON at :479; FWD-12 at :117)
SIBLING SCOPES    C-KIT, C-KIT-PYTHON, C-ATTENTION (FWD-12), the bun disarm (row NFRA_CTLPLN-S13)
PRIOR ART         requirements.txt @bc10584676 and its builder
                    org/tier1_exec/3.0.0_SA_CVO/deliverables/REQUIREMENTS_CENSUS/build_requirements.py
                  org/devices/kit_python_census.py, kit_python_pack.py, kit_python_install.py, kit_python_required.json
                  org/devices/kit_bun_no_egress.py, kit_portal_tree.py, kit_terraform_providers.py
                  the dell1 record @9e5f28e155 (branch q/dell1/record-package-intake/r1): sections 2, 3 and 4
                  the dell2 record @50df0c2e97 (branch q/dell2/record-download-tiers/r1)
                  org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~13/PYTHON_WHEELS_NEEDING_A_FETCH_FOR_CP314.md
                    @bd489b912b (the first batch, F11 to F13); CTO ruling msg 106318
                  rows MDPF_SECCLASS-S49, MDPF_SECCLASS-S54; NFRA_CTLPLN investigation file line 1143
ANDREW'S WORDS    org/tier0_exec/0.0.0_AB_MSTR/deliverables/DELL_BUS_RELAYS_FOR_CTO_20261007_1405Z.md (untracked at this
                  write; the records are on the two Dell branches)
MEASURED AT       2026-10-07 ~14:5xZ, laptop, working tree near eb29bf7f37
```
