# Deckset Presentation Expert

Claude Code skill for creating Deckset presentations with markdown. Includes 29 documentation files, 3 example presentations, and auto-scraper.

## Installation

**Quick install:**
```bash
/plugin marketplace add alexislutun/deckset-claude-skill
/plugin install deckset-presentation-expert
```

**Or direct:**
```bash
/plugin install deckset-presentation-expert@deckset-claude-skill
```

**Or local:**
```bash
git clone https://github.com/alexislutun/deckset-claude-skill.git
cd deckset-claude-skill
/plugin marketplace add .
/plugin install deckset-presentation-expert
```

## Usage

Just mention "Deckset", "slides", or "presentation" and the skill activates automatically.

Examples:
- "Create a Deckset presentation about ML basics"
- "Add presenter notes to these slides"
- "How do I add background images in Deckset?"

## What's Included

- 📚 **29 docs** from official Deckset documentation (formatting, media, presenting, customization)
- 🎨 **3 examples** (simple, technical, visual presentations)
- 🔧 **Scraper script** to update docs from deckset.com

## Quick Reference

**Slide separator** (must have blank lines):
```markdown
---
```

**Headings:**
```markdown
# Title Slide
## Slide Heading
```

**Images:**
```markdown
![](background.jpg)              # Full-screen
![inline](logo.png)              # Inline
![inline fill](photo.jpg)        # Fill space
```

**Presenter notes:**
```markdown
^ This is a presenter note (starts with ^)
```

**Config** (at top of file):
```markdown
theme: Plain Jane, 1
footer: My Presentation
slidenumbers: true
```

## Structure

```
skills/deckset-presentation-expert/
├── SKILL.md                 # Main skill
├── docs/                    # 29 organized docs
│   ├── formatting/          # 13 files
│   ├── media/               # 5 files
│   ├── presenting/          # 5 files
│   ├── customization/       # 2 files
│   └── general/             # 4 files
└── examples/                # 3 complete examples
```

## Update Docs

```bash
source venv/bin/activate
python scripts/scrape-deckset-docs.py
```

## Resources

- Deckset: https://www.decksetapp.com
- Docs: https://docs.deckset.com/English.lproj/
- Issues: https://github.com/alexislutun/deckset-claude-skill/issues

## License

MIT - Alexis Lutun

Unofficial community skill. Not affiliated with Deckset or Anthropic.