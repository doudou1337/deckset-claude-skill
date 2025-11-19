#!/usr/bin/env python3
"""
Deckset Documentation Scraper

This script downloads the Deckset documentation from https://docs.deckset.com/English.lproj/
and converts it to organized markdown files for use in the Claude Code skill.

Usage:
    python scripts/scrape-deckset-docs.py

Requirements:
    pip install requests beautifulsoup4 html2text
"""

import os
import sys
import re
import time
from pathlib import Path
from typing import Dict, List, Tuple
from urllib.parse import urljoin, urlparse

try:
    import requests
    from bs4 import BeautifulSoup
    import html2text
except ImportError:
    print("Error: Required packages not installed.")
    print("Please run: pip install requests beautifulsoup4 html2text")
    sys.exit(1)


class DecksetDocScraper:
    def __init__(self, base_url: str, output_dir: str):
        self.base_url = base_url
        self.output_dir = Path(output_dir)
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        self.html_converter = html2text.HTML2Text()
        self.html_converter.ignore_links = False
        self.html_converter.ignore_images = False
        self.html_converter.body_width = 0  # Don't wrap lines

    def fetch_page(self, url: str) -> Tuple[str, BeautifulSoup]:
        """Fetch a page and return its content and parsed HTML."""
        print(f"Fetching: {url}")
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            return response.text, soup
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None, None

    def extract_content(self, soup: BeautifulSoup) -> str:
        """Extract main content from the page."""
        # Try to find the main content area
        content = soup.find('article') or soup.find('main') or soup.find('div', class_='content')

        if not content:
            # Fallback to body if no specific content area found
            content = soup.find('body')

        if not content:
            return ""

        # Remove navigation, headers, footers
        for tag in content.find_all(['nav', 'header', 'footer', 'script', 'style']):
            tag.decompose()

        return str(content)

    def html_to_markdown(self, html_content: str, title: str = "") -> str:
        """Convert HTML to clean markdown."""
        markdown = self.html_converter.handle(html_content)

        # Add title if provided
        if title:
            markdown = f"# {title}\n\n{markdown}"

        # Clean up excessive blank lines
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)

        return markdown.strip()

    def sanitize_filename(self, name: str) -> str:
        """Convert a name to a safe filename."""
        # Remove or replace invalid characters
        name = re.sub(r'[^\w\s-]', '', name)
        name = re.sub(r'[-\s]+', '-', name)
        return name.lower().strip('-')

    def discover_documentation_pages(self) -> Dict[str, str]:
        """Discover all documentation pages from the main page."""
        print("Discovering documentation pages...")
        html, soup = self.fetch_page(self.base_url)

        if not soup:
            return {}

        pages = {}

        # Find all links in the documentation
        for link in soup.find_all('a', href=True):
            href = link['href']

            # Skip external links, anchors, and non-HTML files
            if href.startswith(('http://', 'https://', '#', 'mailto:')):
                continue

            if not href.endswith('.html'):
                continue

            full_url = urljoin(self.base_url, href)

            # Get link text for categorization
            link_text = link.get_text(strip=True)

            if link_text and full_url not in pages.values():
                pages[link_text] = full_url

        print(f"Discovered {len(pages)} documentation pages")
        return pages

    def categorize_page(self, title: str) -> str:
        """Determine which category a page belongs to."""
        title_lower = title.lower()

        # Define categories based on content
        categories = {
            'formatting': ['heading', 'list', 'text', 'quote', 'link', 'code',
                          'table', 'formula', 'emoji', 'footer', 'footnote',
                          'line break', 'autoscale', 'column'],
            'media': ['image', 'video', 'audio', 'background', 'inline', 'graph', 'mermaid'],
            'presenting': ['presenter', 'note', 'build', 'transition', 'hide', 'display'],
            'customization': ['theme', 'configuration', 'custom', 'style', 'color'],
        }

        for category, keywords in categories.items():
            if any(keyword in title_lower for keyword in keywords):
                return category

        return 'general'

    def scrape_all(self):
        """Scrape all documentation pages and save to markdown files."""
        print(f"Starting documentation scrape from {self.base_url}")
        print(f"Output directory: {self.output_dir}")

        # Create output directory structure
        self.output_dir.mkdir(parents=True, exist_ok=True)
        for category in ['formatting', 'media', 'presenting', 'customization', 'general']:
            (self.output_dir / category).mkdir(exist_ok=True)

        # Discover all pages
        pages = self.discover_documentation_pages()

        if not pages:
            print("No pages discovered. Trying to scrape main page only...")
            pages = {'Getting Started': self.base_url}

        # Scrape each page
        for idx, (title, url) in enumerate(pages.items(), 1):
            print(f"\n[{idx}/{len(pages)}] Processing: {title}")

            # Fetch and parse
            html, soup = self.fetch_page(url)

            if not soup:
                print(f"  Skipping due to fetch error")
                continue

            # Extract content
            content_html = self.extract_content(soup)

            if not content_html:
                print(f"  No content found")
                continue

            # Convert to markdown
            markdown = self.html_to_markdown(content_html, title)

            # Determine category and filename
            category = self.categorize_page(title)
            filename = self.sanitize_filename(title) + '.md'
            filepath = self.output_dir / category / filename

            # Save to file
            filepath.write_text(markdown, encoding='utf-8')
            print(f"  Saved to: {filepath}")

            # Be nice to the server
            time.sleep(0.5)

        print(f"\n✅ Scraping complete! Documentation saved to {self.output_dir}")
        self.print_summary()

    def print_summary(self):
        """Print a summary of scraped documentation."""
        print("\n" + "="*60)
        print("Documentation Summary")
        print("="*60)

        for category in ['formatting', 'media', 'presenting', 'customization', 'general']:
            category_dir = self.output_dir / category
            if category_dir.exists():
                files = list(category_dir.glob('*.md'))
                if files:
                    print(f"\n{category.upper()}: {len(files)} files")
                    for f in sorted(files):
                        print(f"  - {f.name}")


def main():
    """Main entry point."""
    base_url = "https://docs.deckset.com/English.lproj/"
    output_dir = "skills/deckset-presentation-expert/docs"

    print("="*60)
    print("Deckset Documentation Scraper")
    print("="*60)
    print()

    scraper = DecksetDocScraper(base_url, output_dir)

    try:
        scraper.scrape_all()
    except KeyboardInterrupt:
        print("\n\n⚠️  Scraping interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Error during scraping: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
