from pathlib import Path
import re
ROOT = Path(__file__).resolve().parents[1]
s = (ROOT/'SKILL.md').read_text()
assert s.startswith('---\nname: idea-triage-gate\n')
assert 'description:' in s.split('---',2)[1]
for p in (ROOT/'prompts').glob('*.md'):
    for name in re.findall(r'`(\d\d-[a-z-]+\.md)`',p.read_text()):
        assert (p.parent/name).is_file(), (p,name)
assert len(list((ROOT/'prompts').glob('*.md'))) == 8
assert 'BUILD' not in (ROOT/'agents/openai.yaml').read_text()
print('OK: v2 entry and prompt references')
