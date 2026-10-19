"""Read back code and published evidence; exercise the existing-date curation guard once."""
from datetime import datetime, timezone
import hashlib
import json

import boto3

from migrate_example import ROOT, SCRATCH, invoke, query

EXPECTED = {
    'finbert-batch-processor': ('bS9apmUaYJS+XrMl9oH7YHPIqkxf1QtO9XNoNFqYv5s=', 'b4e7c36602'),
    'news-trending-analysis': ('bnMiX3uT5TEglVTiP3z1qXDTzezQ0f26AOhdUYnXy/s=', '6d16b9b93f'),
    'opal-news-layer3-curation': ('OSjRnpFUrkRpN+VN/qwZqB62Pyd9wXCvgFMm8rFE6DY=', '5edd941fce'),
    'opal-trending-topics-portal-publisher': ('IR/MduwQlCIdW48IDmRAP285AwB6fs5/XKnDbNj6ENA=', '6d16b9b93f'),
}


def main():
    folder = ROOT / 'org/tier1_exec/4.0.0_SA_CRO/deliverables/NEWS_SENTIMENT_FIX_20261019'
    lam = boto3.client('lambda', region_name='us-east-1')
    release = {}
    for name, (expected, source) in EXPECTED.items():
        live = lam.get_function_configuration(FunctionName=name)
        assert live['CodeSha256'] == expected, name
        assert live['State'] == 'Active' and live['LastUpdateStatus'] == 'Successful', name
        release[name] = {'code_sha256': expected, 'source_commit': source,
                         'revision': live['RevisionId'], 'last_modified': live['LastModified'],
                         'state': live['State'], 'last_update_status': live['LastUpdateStatus']}
    for path in (folder / 'RELEASE_MANIFEST.json', SCRATCH / 'release.json'):
        path.write_text(json.dumps(release, indent=2) + '\n')
    date = str(datetime.now(timezone.utc).date())
    before = sorted(query('opal-news-trending-daily', 'date', date), key=lambda r: r['topic_rank']['S'])
    assert before, 'No existing topics: unsafe idempotence probe'
    response = invoke('opal-news-layer3-curation', {'date': date, 'force_refresh': False})
    assert response.get('skipped') is True, response
    after = sorted(query('opal-news-trending-daily', 'date', date), key=lambda r: r['topic_rank']['S'])
    assert before == after, 'Curation mutated existing topics'
    raw = boto3.client('s3', region_name='us-east-1').get_object(
        Bucket='opal-data-portal-v2', Key='json/trending/latest.json')['Body'].read()
    payload = json.loads(raw)
    total = 0
    for direction in ('bullish', 'bearish'):
        for topic in payload[direction]:
            total += 1
            assert topic['market_direction'] == direction
            urls = [a['url'] for a in topic['top_articles']]
            assert len(urls) == len(set(urls)), topic['topic']
    wanted = set(json.loads((SCRATCH / 'backup/example-before-wire.json').read_text())['urls'])
    coal = max(payload['bearish'], key=lambda t: len(wanted & {a['url'] for a in t['top_articles']}))
    assert len(wanted & {a['url'] for a in coal['top_articles']}) >= 2
    assert len(coal['top_articles']) == 5
    assert coal['article_count'] == 5
    cases = []
    for article in coal['top_articles']:
        impact = article['market_impact']
        assert impact is not None
        coverage = article['evidence_coverage']
        if coverage == 'headline':
            assert impact['direction'] == 'insufficient'
        cases.append({'source': article['source'], 'url': article['url'],
                      'coverage': coverage, 'direction': impact['direction']})
    assert sorted(c['direction'] for c in cases) == ['bearish', 'bearish', 'insufficient', 'insufficient', 'mixed']
    (SCRATCH / 'served-fixtures.json').write_text(json.dumps({'/trending/latest.json': payload}))
    (SCRATCH / 'served-topic.txt').write_text(coal['topic'])
    receipt = {'verified_at': datetime.now(timezone.utc).isoformat(), 'functions_verified': list(release),
               'curation_skipped': True, 'curation_rows_unchanged': len(before),
               'published_topics_checked': total, 'payload_sha256': hashlib.sha256(raw).hexdigest(),
               'topic': coal['topic'], 'topic_direction': coal['market_direction'], 'unique_articles': cases,
               'python_regressions': 21, 'frontend_assertions': 9, 'live_model_cases': 8,
               'portal_prod': '8cd45f623bdfae12ac6e4cfcfc8e0d74325ed4c3',
               'portal_tag': 'portal-v2.1.243', 'ci_run': 39294118121,
               'limits': ['Bounded backfill; historic feed not wholly rescored.',
                          'Nikkei and Seeking Alpha bodies inaccessible; headline-only remains uncertain.',
                          'Browser uses served production assets with captured S3 data and authentication fixture.',
                          'Curation probe before the guard repair regenerated today topics; all four calls ended before final migration.']}
    (folder / 'VALIDATION_RECEIPT.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt))


if __name__ == '__main__':
    main()
