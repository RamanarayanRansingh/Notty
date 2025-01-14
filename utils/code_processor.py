# utils/code_processor.py
import re
from typing import List, Dict
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

class CodeProcessor:
    @staticmethod
    def extract_code_blocks(content: str) -> List[Dict]:
        """Extract code blocks with language detection"""
        pattern = r'```(\w+)?\n(.*?)\n```'
        matches = re.findall(pattern, content, re.DOTALL)
        
        blocks = []
        for lang, code in matches:
            blocks.append({
                'language': lang or 'text',
                'code': code.strip(),
                'highlighted': CodeProcessor.highlight_code(code.strip(), lang)
            })
        return blocks

    @staticmethod
    def highlight_code(code: str, language: str) -> str:
        """Syntax highlight code using Pygments"""
        try:
            lexer = get_lexer_by_name(language)
            formatter = HtmlFormatter(style='monokai')
            return highlight(code, lexer, formatter)
        except:
            return code

    @staticmethod
    def parse_line_numbers(line_input: str) -> List[int]:
        """Parse line number input (e.g., '1-3, 5, 7-9')"""
        numbers = set()
        for part in line_input.split(','):
            part = part.strip()
            if '-' in part:
                start, end = map(int, part.split('-'))
                numbers.update(range(start, end + 1))
            else:
                numbers.add(int(part))
        return sorted(list(numbers))