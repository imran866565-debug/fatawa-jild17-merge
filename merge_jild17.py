#!/usr/bin/env python3
"""Merge Jild 17 tashreeh chunks into jild-17.json.

Re-runnable: reads every jild-17-chunk-*.json listed in the manifest,
merges in chunk order, validates (unique ids, page coverage vs manifest,
no empty jawab), writes jild-17.json, and updates the manifest statuses.

COMBINE RULES (from the Jild 17 coordinator's self-contained final
report, verified by the parent on disk: 286 items, 630/630 unique
pages, only the 2 intended duplicate-id pairs, exactly 1 empty
jawab — chunk 06's masala-198 [370], a split-start half). 7 combine
cases are ONE mas'ala split across chunks and must be COMBINED into
a single item, NOT renamed by the duplicate-id rule. After combining
all 7 cases, the merged file has 252 items (286 - 34) covering 630
unique pages. Combine rules (parts ordered by min page; sawal as
specified per rule; jawab = all parts concatenated in page order;
pages = UNION of all parts' pages; notes = all parts' notes):
  masala 33 (RENAME + combine): chunk 01 'jild17-33' [119, 120] +
              chunk 02 'jild17-masala-33' [121] (empty sawal) ->
              ONE item 'jild17-masala-33', pages [119-121]. RENAME
              chunk 01's id first. Sawal from chunk 01; jawab = 01
              + 02 concatenated.
  masala 141 (RENAME + combine): chunk 05 'jild17-141' [320] +
              chunk 06 'jild17-masala-141' [321, 322] -> ONE item
              'jild17-masala-141', pages [320-322]. RENAME chunk
              05's id first. Sawal: KEEP chunk 05's (342 chars —
              the original, from p. 320 where the question sits,
              and fuller); DISCARD chunk 06's sawal (325 chars — a
              full restatement; Jild 11 masala-16 precedent).
              Jawab = 05 + 06 concatenated.
  masala 198 (same id): chunk 06 'jild17-masala-198' [370] (full
              sawal, EMPTY jawab — the volume's only empty jawab)
              + chunk 07 'jild17-masala-198' [371-374] (sawal
              restatement) -> ONE item, pages [370-374]. Sawal:
              KEEP chunk 06's (1,902 chars — the original,
              question begins p. 370, and longer); DISCARD chunk
              07's sawal (1,841 chars — restatement beginning
              "یہ مسئلہ صفحہ ۳۷۰ سے شروع ہوا تھا…"; Jild 11
              masala-16 precedent). Jawab = chunk 07's.
  masala 255 (RENAME + combine): chunk 11 'jild17-masala-255'
              [610, 611] + chunk 12 'jild17-255' [612, 613]
              (empty sawal) -> ONE item 'jild17-masala-255',
              pages [610-613]. RENAME chunk 12's id first. Sawal
              from chunk 11; jawab = 11 + 12 concatenated.
  masala 280 (same id): chunk 12 'jild17-280' [657-660] + chunk 13
              'jild17-280' [661-670] (empty sawal) -> ONE item
              'jild17-280', pages [657-670]. Sawal from chunk 12;
              jawab = 12 + 13 concatenated.
  masala 217, RISALA 1 — کفل الفقیہ الفاہم فی احکام قرطاس
              الدراہم (۱۳۲۴ھ): 11 parts -> ONE item
              'jild17-masala-217', pages [395-502]. Sawal = chunk
              07's 12-question sawal. Jawab = all 11 parts'
              jawabs concatenated in page order. Parts: chunk 07
              'jild17-masala-217' [395-420]; chunk 08
              'jild17-kasir-6' [421-424], 'jild17-kasir-7' [424],
              'jild17-kasir-8' [424], 'jild17-kasir-9' [425-440],
              'jild17-kasir-10' [441-444], 'jild17-kasir-11'
              [445-470]; chunk 09 'jild17-p471' [471-482],
              'jild17-p483' [483-486], 'jild17-p486' [486-493],
              'jild17-masala-12' [493-502]. Evidence (coordinator
              verified from the source): p. 395 prints the risala
              title + مسئلہ ۲۱۷ with the 12 questions; p. 501
              prints the colophon "انتہی الجواب … وسمیتہ کفل
              الفقیہ الفاہم فی احکام قرطاس الدراھم ۱۳۲۴ھ".
              P. 502 RESOLVED BY THE PARENT (do not re-open):
              chunk 09's 'jild17-masala-12' notes state "یہ رسالہ
              صفحہ 501 پر تمام ہوا اور صفحہ 502 پر اس کا اختتامی
              حصہ (دعا و دستخط) ہے", its jawab tail is the closing
              dua + Ala Hazrat's signature, and the source p. 502
              text (1,964 chars) IS that closing dua. So masala-12's
              jawab DOES cover p. 502 content — the combined
              masala-217 pages end at 502, i.e. [395-502]. Note
              p. 502 is ALSO the first page of masala-218 [502-504]
              (shared page — expected; the page union stays 630).
  masala 219, RISALA 2 — کاسر السفیہ الواہم فی ابدال قرطاس
              الدراہم / الذیل المنوط لرسالۃ النوط (۱۳۲۹ھ): 20 parts
              -> ONE item 'jild17-masala-219', pages [505-560].
              Sawal = EMPTY by design (no printed question — p. 505
              is the risala's intro/hamd referring back to risala
              1, covered in the first part's jawab; the rest is the
              ردّ, وجوہ 1-18). Jawab = all 20 parts' jawabs
              concatenated in page order. Parts: chunk 09
              'jild17-masala-219' [505, 506], 'jild17-p506'
              [506-514], 'jild17-p514' [514-520]; chunk 10
              'jild17-p521' [521, 522], 'jild17-p522' [522, 523],
              'jild17-p523' [523, 524], 'jild17-p524' [524, 525],
              'jild17-p526' [526, 527], 'jild17-p527' [527, 528],
              'jild17-p528' [528, 529], 'jild17-p529' [529, 530,
              531], 'jild17-p531' [531-536], 'jild17-p536'
              [536, 537], 'jild17-p537' [537, 538, 539],
              'jild17-p539' [539-544], 'jild17-p544' [544, 545,
              546], 'jild17-p546' [546-549], 'jild17-p550'
              [550, 551, 552, 553], 'jild17-p553' [553, 554, 555,
              556, 557], 'jild17-p557' [557, 558, 559, 560].
              Evidence (coordinator verified from the source):
              p. 505 prints the second risala's title + مسئلہ ۲۱۹.
              This is a DIFFERENT risala from Rule 6 (different
              year ۱۳۲۹ھ vs ۱۳۲۴ھ) — NEVER combine Rules 6 and 7
              together.
For every combined item: pages = union of all parts' pages,
start_page = min, notes = all parts' notes combined.

EXPLICITLY NOT COMBINES (keep separate):
- Chunk 03's 'jild17-masala-75' (p. 168, wood for Hindu cremation)
  vs 'jild17-p173' (p. 173, house sold with buy-back condition —
  printed ۷۵ a second time, sequentially ۸۵). Distinct ids,
  distinct masail.
- Chunk 12's 'jild17-257' (مارہرہ, p. 614) vs 'jild17-p615'
  (بنگال, p. 615 — printed ۲۵۷ a second time, sequentially 258).
  Distinct ids, distinct masail.
- Chunk 09's 'jild17-masala-12' (risala 1, question 12 — absorbed
  into rule 6) is NOT chunk 01's mas'ala 12 — chunk 01 groups
  masail 6-16 into ONE item 'jild17-6-16', so no 'jild17-12' id
  exists at all. Never merge these.
- Masala-218 [502-504] stays its own item (it starts on the shared
  p. 502 after risala 1's closing dua/signature).
- Do NOT globally normalise bare ids ('jild17-NNN') to masala-form.
  Keep every chunk's ids exactly as written EXCEPT the three renames
  in Rules 1, 2, 4 (33, 141, 255). Bare ids that stay bare: chunk 01
  ('jild17-1'...'jild17-32', 'jild17-6-16', 'jild17-pesh-lafz'),
  chunk 05 ('jild17-115'...'jild17-140'), chunk 12
  ('jild17-256'...'jild17-279'), chunk 13 ('jild17-281'...'jild17-298',
  'jild17-khatima').

Any duplicate id left after the 7 combines is a bug: fail loudly,
do NOT silently rename.
"""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))

# result id -> list of selectors, in page order.
# Selector forms:
#   ('id', sid)            — every item with this id (1 or 2 halves)
#   ('id_start', sid, sp)  — the item with this id starting at page sp
#   ('file', fname)        — every item in this chunk file
COMBINES = {
    'jild17-masala-33': [
        ('id', 'jild17-masala-33'),
    ],
    'jild17-masala-141': [
        ('id', 'jild17-masala-141'),
    ],
    'jild17-masala-198': [
        ('id', 'jild17-masala-198'),
    ],
    'jild17-masala-255': [
        ('id', 'jild17-masala-255'),
    ],
    'jild17-280': [
        ('id', 'jild17-280'),
    ],
    'jild17-masala-217': [
        ('id', 'jild17-masala-217'),
        ('id', 'jild17-kasir-6'),
        ('id', 'jild17-kasir-7'),
        ('id', 'jild17-kasir-8'),
        ('id', 'jild17-kasir-9'),
        ('id', 'jild17-kasir-10'),
        ('id', 'jild17-kasir-11'),
        ('id', 'jild17-p471'),
        ('id', 'jild17-p483'),
        ('id', 'jild17-p486'),
        ('id', 'jild17-masala-12'),
    ],
    'jild17-masala-219': [
        ('id', 'jild17-masala-219'),
        ('id', 'jild17-p506'),
        ('id', 'jild17-p514'),
        ('id', 'jild17-p521'),
        ('id', 'jild17-p522'),
        ('id', 'jild17-p523'),
        ('id', 'jild17-p524'),
        ('id', 'jild17-p526'),
        ('id', 'jild17-p527'),
        ('id', 'jild17-p528'),
        ('id', 'jild17-p529'),
        ('id', 'jild17-p531'),
        ('id', 'jild17-p536'),
        ('id', 'jild17-p537'),
        ('id', 'jild17-p539'),
        ('id', 'jild17-p544'),
        ('id', 'jild17-p546'),
        ('id', 'jild17-p550'),
        ('id', 'jild17-p553'),
        ('id', 'jild17-p557'),
    ],
}

# result id -> start_page of the part whose sawal to keep.
# Absent = sawal from the FIRST part (lowest min page).
# Rule 2 (141): keep chunk 05's sawal (start 320), discard chunk
# 06's restatement (start 321). Rule 3 (198): keep chunk 06's sawal
# (start 370), discard chunk 07's restatement (start 371). Both are
# the Jild 11 masala-16 rule.
SAWAL_FROM_START = {
    'jild17-masala-141': 320,
    'jild17-masala-198': 370,
}

# Every combined item must have a non-empty sawal after combining,
# EXCEPT masala-219: no printed question exists for risala 2, so its
# sawal is EMPTY by design.
SAWAL_REQUIRED = set(COMBINES.keys()) - {'jild17-masala-219'}


def combine_parts(result_id, parts):
    parts = sorted(parts, key=lambda it: min(it['pages']))
    first = parts[0]
    sawal_start = SAWAL_FROM_START.get(result_id)
    if sawal_start is not None:
        sawal_parts = [p for p in parts if p['start_page'] == sawal_start]
        assert len(sawal_parts) == 1, \
            f'{result_id}: sawal source start_page {sawal_start} matched {len(sawal_parts)} parts'
        sawal = sawal_parts[0].get('tashreeh_sawal', '') or ''
    else:
        sawal = first.get('tashreeh_sawal', '') or ''
    combined = {
        'id': result_id,
        'title': first.get('title') or '',
        'volume_id': 53,
        'pages': sorted(set().union(*[set(p['pages']) for p in parts])),
        'start_page': min(min(p['pages']) for p in parts),
        'tashreeh_sawal': sawal,
        'tashreeh_jawab': ''.join((p.get('tashreeh_jawab', '') or '') for p in parts),
        'notes': [n for p in parts for n in (p.get('notes') or [])],
    }
    return combined


def select_parts(all_items, selectors):
    """Resolve selectors to the matching items (each used at most once)."""
    parts = []
    used = set()
    for sel in selectors:
        if sel[0] == 'id':
            hits = [it for it in all_items
                    if it['id'] == sel[1] and id(it) not in used]
        elif sel[0] == 'id_start':
            hits = [it for it in all_items
                    if it['id'] == sel[1] and it['start_page'] == sel[2]
                    and id(it) not in used]
        elif sel[0] == 'file':
            hits = [it for it in all_items
                    if it.get('_src_file') == sel[1] and id(it) not in used]
        else:
            raise ValueError(f'unknown selector {sel}')
        assert hits, f'no items matched selector {sel}'
        for it in hits:
            used.add(id(it))
        parts.extend(hits)
    return parts


def run_merge(manifest_path, base, write=False):
    manifest = json.load(open(manifest_path, encoding='utf-8'))
    all_items = []
    merged_chunks = []
    for entry in manifest['chunks']:
        nn = entry['chunk']
        if entry.get('status') == 'split-halves':
            print(f'chunk {nn}: split-halves placeholder — halves are separate entries, skipping')
            continue
        path = os.path.join(base, entry['file'])
        if not os.path.exists(path):
            print(f'chunk {nn}: not yet written')
            continue
        try:
            d = json.load(open(path, encoding='utf-8'))
        except json.JSONDecodeError as e:
            # File may still be streaming from its translator; skip it
            # for now instead of crashing the whole merge.
            print(f'chunk {nn}: not valid JSON yet ({e}) — skipping for now')
            continue
        items = d['masail']
        # Normalize: some translators omit start_page; derive it from pages.
        for it in items:
            if 'start_page' not in it:
                assert it.get('pages'), f'chunk {nn} item {it.get("id")} has no pages'
                it['start_page'] = it['pages'][0]
                print(f'chunk {nn}: derived start_page={it["start_page"]} for {it["id"]}')
            assert it['start_page'] == min(it['pages']), \
                f'chunk {nn} item {it["id"]}: start_page != first page'
            it['_src_file'] = entry['file']
        all_items.extend(items)
        merged_chunks.append(nn)
        entry['status'] = 'merged'
        print(f'chunk {nn}: {len(items)} items merged')
    print(f'items before combines: {len(all_items)}')
    assert len(all_items) == 286, f'expected 286 chunk items, got {len(all_items)}'
    # PAGE-COUNT NOTE: the manifest's missing_pages for chunk 01 lists
    # only [108] — the source-DB gap pp. 9-80 (72 pages) is NOT listed
    # there, so the manifest's start/end ranges CANNOT be used to derive
    # the expected page set (that is why the first simulation failed:
    # range-derived "expected" was 702, not 630). The ground truth is
    # the union of the chunk items' own pages (630 unique pages,
    # verified by the parent against the source DB), cross-checked
    # against the manifest's pages_present total (also 630). The merge
    # must cover exactly those pages — no page dropped by a combine,
    # no page added.
    chunk_pages = set()
    for it in all_items:
        chunk_pages.update(it['pages'])
    manifest_total = sum(e.get('pages_present', 0) for e in manifest['chunks'])
    print(f'chunk page union: {len(chunk_pages)} pages | manifest pages_present total: {manifest_total}')
    assert len(chunk_pages) == 630, f'expected 630 chunk pages, got {len(chunk_pages)}'
    assert manifest_total == 630, f'manifest pages_present total is {manifest_total}, expected 630'
    # RENAME PRE-STEPS (before combining): three bare ids must become
    # masala-form so they combine with their masala-form halves.
    #   Rule 1: chunk 01 'jild17-33' [119-120] -> 'jild17-masala-33'
    #   Rule 2: chunk 05 'jild17-141' [320] -> 'jild17-masala-141'
    #   Rule 4: chunk 12 'jild17-255' [612-613] -> 'jild17-masala-255'
    # Each rename is pinned to its exact start_page so no other item
    # with the same id (there is none) can be touched.
    renames = [
        ('jild17-33', 119, 'jild17-masala-33'),
        ('jild17-141', 320, 'jild17-masala-141'),
        ('jild17-255', 612, 'jild17-masala-255'),
    ]
    for old_id, start_page, new_id in renames:
        hits = [it for it in all_items
                if it['id'] == old_id and it['start_page'] == start_page]
        assert len(hits) == 1, \
            f'rename pre-step: expected exactly 1 item {old_id} at start {start_page}, got {len(hits)}'
        print(f"RENAME {old_id} (start {start_page}) -> {new_id}")
        hits[0]['id'] = new_id
    print('rename pre-steps OK: 3 renames applied')
    # COMBINE the 7 cases (one mas'ala split across chunks).
    for result_id, selectors in COMBINES.items():
        parts = select_parts(all_items, selectors)
        combined = combine_parts(result_id, parts)
        assert combined['tashreeh_jawab'], f'{result_id}: combined jawab is empty!'
        if result_id in SAWAL_REQUIRED:
            assert combined['tashreeh_sawal'], f'{result_id}: combined sawal is empty!'
        assert combined['start_page'] == min(combined['pages']), f'{result_id}: start_page != min(pages)'
        used_ids = set(id(p) for p in parts)
        all_items = [it for it in all_items if id(it) not in used_ids]
        all_items.append(combined)
        print(f'COMBINED {result_id}: {len(parts)} parts, pages {combined["pages"][0]}-{combined["pages"][-1]} '
              f'({len(combined["pages"])} pages), sawal {len(combined["tashreeh_sawal"])} chars, '
              f'jawab {len(combined["tashreeh_jawab"])} chars, notes {len(combined["notes"])}')
    ids = [it['id'] for it in all_items]
    assert len(ids) == len(set(ids)), f'STILL DUPLICATE IDS: {[i for i in ids if ids.count(i) > 1]}'
    empty = [it['id'] for it in all_items if not it.get('tashreeh_jawab')]
    assert not empty, f'EMPTY JAWAB: {empty}'
    pages = set()
    for it in all_items:
        pages.update(it['pages'])
    missing_covered = chunk_pages - pages
    extra = pages - chunk_pages
    print(f'total items: {len(all_items)} | pages covered: {len(pages)} | chunk pages: {len(chunk_pages)}')
    print(f'pages dropped by combines: {sorted(missing_covered)}')
    print(f'pages added by combines: {sorted(extra)}')
    assert not missing_covered, 'pages missing from merged chunks!'
    assert not extra, 'pages outside merged chunks!'
    assert len(all_items) == 252, f'expected 252 items after combines, got {len(all_items)}'
    assert len(pages) == 630, f'expected 630 pages, got {len(pages)}'
    # sort by start_page for the final file
    all_items.sort(key=lambda it: it['start_page'])
    for it in all_items:
        it.pop('_src_file', None)
    if write:
        with open(os.path.join(base, 'jild-17.json'), 'w', encoding='utf-8') as f:
            json.dump({'masail': all_items}, f, ensure_ascii=False, indent=1)
        with open(os.path.join(base, 'chunks-manifest-jild17.json'), 'w', encoding='utf-8') as f:
            json.dump(manifest, f, ensure_ascii=False, indent=2)
        print(f'WROTE jild-17.json: {len(all_items)} items, {len(pages)} pages, chunks merged: {merged_chunks}')
    return all_items, pages, merged_chunks


def main():
    manifest_path = os.path.join(BASE, 'chunks-manifest-jild17.json')
    run_merge(manifest_path, BASE, write=True)


if __name__ == '__main__':
    main()
