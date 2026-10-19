"""Authorized read-only retrieval/model validation; no production data writes."""
import concurrent.futures
import json
from pathlib import Path
import sys

import boto3
from boto3.dynamodb.conditions import Key

ROOT = Path.cwd()
sys.path.insert(0, str(ROOT / 'infra/aws/lambda/finbert_batch_processor'))
from article_context import assess_article, judge_evidence  # noqa: E402
from lambda_function import invoke_finbert_lambda  # noqa: E402

SCRATCH = ROOT / '.runtime/news-sentiment-fix-20261019'
REPORT = ROOT / 'org/tier1_exec/4.0.0_SA_CRO/deliverables/NEWS_SENTIMENT_FIX_20261019'


def main():
    scratch = SCRATCH / 'validation'
    scratch.mkdir(parents=True, exist_ok=True)
    secret = boto3.client('secretsmanager', region_name='us-east-1').get_secret_value(
        SecretId='opal/openai/news-trending')['SecretString']
    try:
        parsed = json.loads(secret)
        key = parsed.get('api_key') or parsed.get('key') or parsed.get('OPENAI_API_KEY')
    except ValueError:
        key = secret
    cases = json.loads((ROOT / 'tests/news_sentiment/market_cases.json').read_text())
    def evaluate_case(case):
        evidence = {'title': case['title'], 'text': case['text'], 'coverage': 'article_text', 'truncated': False}
        judgment = judge_evidence(evidence, key)
        expected = case['expected'] if isinstance(case['expected'], list) else [case['expected']]
        return {'id': case['id'], 'expected': expected, 'actual': judgment['direction'],
                'pass': judgment['direction'] in expected, 'reason': judgment['reason'], 'usage': judgment['usage']}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(evaluate_case, cases))
    (REPORT / 'MODEL_VALIDATION.json').write_text(json.dumps(results, indent=2))
    print('MODEL_CASES', json.dumps(results))
    portal = json.loads((SCRATCH / 'backup/portal-before.json').read_text())
    coal = next(t for t in portal['bearish'] if 'Coal' in t['topic'])
    articles = []
    seen = set()
    for row in coal['top_articles']:
        if row['url'] in seen:
            continue
        seen.add(row['url'])
        articles.append({'title': row['title'], 'url': row['url'], 'summary': ''})
    # Use actual stored summaries, rather than withholding evidence from the comparison.
    table = boto3.resource('dynamodb', region_name='us-east-1').Table('opal-news-articles')
    all_rows = []
    for day in range(13, 20):
        args = {'KeyConditionExpression': Key('article_date').eq(f'2026-10-{day}')}
        while True:
            response = table.query(**args)
            all_rows.extend(response['Items'])
            if 'LastEvaluatedKey' not in response:
                break
            args['ExclusiveStartKey'] = response['LastEvaluatedKey']
    backup = SCRATCH / 'backup/articles-before.json'
    if not backup.exists():
        backup.write_text(json.dumps(all_rows, default=str))
    lookup = {r['url']: r for r in all_rows}
    def evaluate_live(article):
        article['summary'] = lookup.get(article['url'], {}).get('summary', '')
        try:
            assessment = assess_article(article, key, invoke_finbert_lambda)
        except Exception as exc:
            return {'url': article['url'], 'title': article['title'], 'error': str(exc)}
        fingerprint = assessment['evidence']['input_sha256']
        (scratch / (fingerprint + '.json')).write_text(json.dumps(assessment, default=float, indent=2))
        e, impact = assessment['evidence'], assessment['market_impact']
        return {'url': article['url'], 'title': article['title'], 'coverage': e['coverage'],
                'extraction': e['extraction'], 'characters': e['characters'], 'truncated': e['truncated'],
                'direction': impact['direction'], 'reason': impact['reason'],
                'input_sha256': fingerprint, 'finbert_windows': assessment['finbert_tone']['chunk_count']}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        live = list(pool.map(evaluate_live, articles))
    (REPORT / 'LIVE_VALIDATION.json').write_text(json.dumps(live, indent=2))
    print('LIVE_ARTICLES', json.dumps(live))
    if not all(r['pass'] for r in results) or any('error' in r for r in live):
        raise SystemExit('MODEL OR LIVE VALIDATION FAILED')


if __name__ == '__main__':
    main()
