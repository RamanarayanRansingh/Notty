# utils/docs_processor.py
from bs4 import BeautifulSoup
import markdown
import re

class DocsProcessor:
    @staticmethod
    def clean_content(content: str) -> str:
        """Clean and normalize documentation content"""
        soup = BeautifulSoup(content, 'html.parser')
        
        # Preserve code blocks
        code_blocks = []
        for code in soup.find_all('code'):
            placeholder = f'CODE_BLOCK_{len(code_blocks)}'
            code_blocks.append(code.string)
            code.replace_with(placeholder)
        
        # Get clean text
        text = soup.get_text()
        
        # Restore code blocks
        for i, code in enumerate(code_blocks):
            text = text.replace(f'CODE_BLOCK_{i}', f'```\n{code}\n```')
        
        return text

    @staticmethod
    def format_for_export(content: str, format: str) -> str:
        """Format content for different export formats"""
        if format == "html":
            return markdown.markdown(
                content,
                extensions=['fenced_code', 'tables', 'toc']
            )
        return content