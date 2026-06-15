import json, re, glob, os
from collections import Counter, defaultdict

PROJ = 'C:/Users/AndrewBerman/.claude/projects/C--Users-AndrewBerman-Desktop-ajb-workspace'
files = glob.glob(os.path.join(PROJ, '*.jsonl'))

# HIGH-CONFIDENCE target classifiers: (label, comp-tool, regex) -- precision over recall.
# Each maps a search target to the comp call that answers it deterministically.
CLASS = [
    # gold/silver/bronze script id (D_04, INF_C_01, A_03, B_02b, S_00) -> comp-pipescript io/feeds/consumers
    ('gold-script-id', 'comp-pipescript io/feeds/consumers',
     re.compile(r'(?<![A-Za-z0-9_])(INF_)?[A-DIS]_[0-9]{2}[a-z]?(?![A-Za-z0-9_])')),
    # S3 served key / artifact path -> comp-pipescript io / pipescript --resource
    ('s3-artifact-key', 'comp-pipescript io / pipescript --resource',
     re.compile(r'(s3://opal-|opal-data-[a-z]+|/(gold|platinum|silver|bronze)/[a-z]|\.parquet)')),
    # deployed lambda name -> comp-iam service / comp-aws / pipescript --resource
    ('lambda-name', 'comp-iam service / comp-aws / pipescript --resource',
     re.compile(r'\b(opal-[a-z0-9-]+|inf-[a-z0-9-]+(-trigger|-daily|-runner|-publisher)|bd-[a-z0-9-]+(-trigger|-runner|-publisher|-processor)|yang-generate-[a-z-]+|causality-[a-z-]+|aws lambda (list|get|invoke))')),
    # portal component / endpoint -> comp-transform / comp-routes
    ('portal-component-route', 'comp-transform / comp-routes',
     re.compile(r'(portal/src/|\.tsx\b|/api/(scoped|general|public)/|getAdvisor|DistributionTab|use[A-Z]\w+Query)')),
    # IAM role/policy -> comp-iam
    ('iam-role-policy', 'comp-iam',
     re.compile(r'(iam[_-]?role|assume_?role|aws_iam_policy|:role/|PolicyDocument)')),
    # AWS resource census (lambda list / s3 ls / cloudwatch) -> comp-aws / comp-pipescript deployed
    ('aws-resource-census', 'comp-aws / comp-pipescript deployed',
     re.compile(r'(aws s3 ls|aws cloudwatch|aws lambda list-functions|aws stepfunctions|describe-alarms)')),
]
# Natural-language QUESTION inference (for #2 router) from the search shape
def question_for(label, text):
    t = text[:120]
    return {
        'gold-script-id': 'what does <gold-id> read/write / who consumes it?',
        's3-artifact-key': 'what produces/consumes this S3 key, who reads the artifact?',
        'lambda-name': 'what does this lambda do / its IAM / its place in a thread?',
        'portal-component-route': 'which producer/endpoint feeds this portal component?',
        'iam-role-policy': 'what perms does this role have / is it a real grant?',
        'aws-resource-census': 'what AWS resources exist / which thread owns them?',
    }.get(label, label)

def extract_searches(f):
    """Yield (tier, tool, text). TIER-1 = relationship-search (grep/find/aws-census) where a comp
    tool gives the deterministic answer = the high-confidence signal. TIER-2 = Read/cat inspect
    (softer -- reading source to edit is legit, so lower confidence as 'blind')."""
    for ln in open(f, encoding='utf-8', errors='replace'):
        try: d = json.loads(ln)
        except: continue
        msg = d.get('message') or {}
        content = msg.get('content') if isinstance(msg, dict) else None
        if not isinstance(content, list): continue
        for c in content:
            if not (isinstance(c, dict) and c.get('type') == 'tool_use'): continue
            nm = c.get('name'); inp = c.get('input') or {}
            if not isinstance(inp, dict): continue
            if nm == 'Grep': yield ('T1', 'Grep', str(inp.get('pattern','')) + ' ' + str(inp.get('path','')))
            elif nm == 'Glob': yield ('T1', 'Glob', str(inp.get('pattern','')))
            elif nm == 'Read': yield ('T2', 'Read', str(inp.get('file_path','')))
            elif nm in ('Bash','PowerShell'):
                cmd = str(inp.get('command',''))
                # exclude aws-cli AGAINST-LIVE (F5 verification of own change = LEGIT, not a comp-bypass)
                if re.search(r'\baws (s3|lambda|cloudwatch|stepfunctions|iam|sqs|sns)\b', cmd):
                    yield ('AWS', 'aws-cli', cmd)   # F5-verify-or-census, reported separately
                elif re.search(r'(\b(grep|rg|egrep)\b|\bfind\b .*-name)', cmd):
                    yield ('T1', 'Bash-search', cmd)   # repo/relationship search = clean bypass signal
                elif re.search(r'\b(cat|head|tail)\b\s', cmd):
                    yield ('T2', 'Bash-view', cmd)

tot = {'T1': Counter(), 'T2': Counter(), 'AWS': Counter()}
matched = {'T1': Counter(), 'T2': Counter(), 'AWS': Counter()}
matched_tool = {'T1': Counter(), 'T2': Counter(), 'AWS': Counter()}
samples = defaultdict(list)
excluded = Counter()
n_files = 0
for f in files:
    n_files += 1
    for tier, tool, text in extract_searches(f):
        # PRECISION FILTER: a comp-tool use / git / ps / commit-wrapper is NOT a bypass-candidate -> exclude from BOTH num+denom
        if re.search(r'(comp-[a-z]+|\bpipescript\b|\bgit \b|\bps -ef\b|safe-commit|safe-deploy)', text):
            excluded[tier] += 1; continue
        tot[tier][tool] += 1
        for label, ctool, rx in CLASS:
            if rx.search(text):
                matched[tier][label] += 1
                matched_tool[tier][ctool] += 1
                if tier=='T1' and len(samples[label])<3: samples[label].append(text[:90])
                break

for tier, name in [('T1','TIER-1 (Grep/Glob/bash grep/find = REPO relationship search, HIGH-CONFIDENCE comp-bypass)'),
                   ('AWS','AWS-CLI (aws s3/lambda/cw... = F5-verify-own-change OR census; LEGIT or soft, NOT clean bypass)'),
                   ('T2','TIER-2 (Read/cat file-view = softer, reading-to-edit often legit)')]:
    total = sum(tot[tier].values()); hit = sum(matched[tier].values())
    print(f"\n=== {name} ===")
    print(f"  ops: {total}  by-tool: {dict(tot[tier])}")
    if total: print(f"  WHERE-A-COMP-TOOL-EXISTS: {hit}  =>  {100*hit/total:.1f}%")
    for label, ctool, rx in CLASS:
        if matched[tier][label]: print(f"    {matched[tier][label]:5}  {label:22} -> {ctool}")

print("\n=== BURIED-TOOL ranking (TIER-1, comp tool that SHOULD have answered) ===")
for ct, n in matched_tool['T1'].most_common(): print(f"  {n:5}  {ct}")
print(f"\nFILES: {n_files} | window 2026-05-20..06-15")

print("\n=== PRECISION SPOT-CHECK (sample TIER-1 matched patterns per class) ===")
for label, ctool, rx in CLASS:
    if samples.get(label):
        print(f"  [{label}]")
        for s in samples[label]: print(f"     {s}")
